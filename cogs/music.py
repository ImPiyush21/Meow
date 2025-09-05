import discord
from discord.ext import commands
from discord import app_commands
import yt_dlp, asyncio

YTDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist': True, 'quiet': True}
FFMPEG_OPTIONS = {'options': '-vn'}

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queues = {}

    def ensure(self, gid):
        if gid not in self.queues:
            self.queues[gid] = []
        return self.queues[gid]

    async def _play_next(self, interaction):
        q = self.queues.get(interaction.guild.id, [])
        if q:
            url = q.pop(0)
            await self._play(interaction, url)
        else:
            vc = interaction.guild.voice_client
            if vc and vc.is_connected():
                await vc.disconnect()

    async def _play(self, interaction, url):
        try:
            vc = interaction.guild.voice_client
            if not vc:
                vc = await interaction.user.voice.channel.connect()
            with yt_dlp.YoutubeDL(YTDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                audio_url = info.get('url')
                title = info.get('title', url)
            def after(err):
                asyncio.run_coroutine_threadsafe(self._play_next(interaction), self.bot.loop)
            source = discord.FFmpegPCMAudio(audio_url, **FFMPEG_OPTIONS)
            vc.play(source, after=after)
            await interaction.followup.send(f'🎶 Now playing: **{title}**')
        except Exception as e:
            await interaction.followup.send(f'Error: {e}')

    @app_commands.command(name='play', description='Play a song from a URL')
    async def play(self, interaction: discord.Interaction, url: str):
        await interaction.response.defer()
        if not interaction.user.voice:
            await interaction.followup.send('Join a voice channel first!')
            return
        q = self.ensure(interaction.guild.id)
        q.append(url)
        vc = interaction.guild.voice_client
        if not vc or not vc.is_playing():
            await self._play(interaction, q.pop(0))
        else:
            await interaction.followup.send('✅ Added to queue.')

    @app_commands.command(name='pause', description='Pause playback')
    async def pause(self, interaction: discord.Interaction):
        vc = interaction.guild.voice_client
        if vc and vc.is_playing():
            vc.pause()
            await interaction.response.send_message('⏸ Paused')
        else:
            await interaction.response.send_message('Nothing is playing.')

    @app_commands.command(name='resume', description='Resume playback')
    async def resume(self, interaction: discord.Interaction):
        vc = interaction.guild.voice_client
        if vc and vc.is_paused():
            vc.resume()
            await interaction.response.send_message('▶️ Resumed')
        else:
            await interaction.response.send_message('Nothing is paused.')

    @app_commands.command(name='skip', description='Skip current track')
    async def skip(self, interaction: discord.Interaction):
        vc = interaction.guild.voice_client
        if vc and vc.is_playing():
            vc.stop()
            await interaction.response.send_message('⏭ Skipped')
        else:
            await interaction.response.send_message('Nothing to skip.')

    @app_commands.command(name='stop', description='Stop and clear the queue')
    async def stop(self, interaction: discord.Interaction):
        self.queues[interaction.guild.id] = []
        vc = interaction.guild.voice_client
        if vc and vc.is_connected():
            await vc.disconnect()
        await interaction.response.send_message('⏹ Stopped and cleared queue.')

async def setup(bot):
    await bot.add_cog(Music(bot))
