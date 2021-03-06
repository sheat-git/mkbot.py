from components import ColoredEmbed as Embed
from discord import Message
from discord.ext import commands
from mk8dx import Track


class TrackCog(commands.Cog, name='Track'):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command(name='nicks', aliases=['nick'], brief='Shows all registered nicknames')
    async def get_nicks(self, ctx: commands.Context, nick: str):
        track = Track.from_nick(nick)
        if track is None:
            await ctx.send(f'Track Not Found: {nick}')
            return
        embed = Embed(
            title=f'{track.abbr} {track.abbr_ja}',
            description='\n'.join(track.nicks)
        )
        await ctx.send(embed=embed)

    @commands.Cog.listener(name='on_message')
    async def get_track(self, message: Message):
        if message.author.bot:
            return
        track = Track.from_nick(message.content)

        if track is None:

            # my team HαM's joke
            if message.guild is not None and message.guild.id == 899957283230994442:
                if message.content == 'どかんがどっかーん':
                    track = Track.BPP
                elif message.content in {'きらーうらいか', 'キラー裏イカ'}:
                    track = Track.DCL
                elif message.content == 'いるかはいるか':
                    track = Track.DS
                elif message.content == 'はむで試行回数をこなしすぎるコース':
                    track = Track.RMP
                else:
                    return

            else:
                return

        embed = Embed(
            title=f'{track.abbr} {track.abbr_ja}',
            description=f'{track.full_name}\n{track.full_name_ja}'
        )
        if track.id < 56:
            embed.set_image(url=f'https://raw.githubusercontent.com/sheat-git/mk8dx/main/tracks/{track.id}.jpg')
        embed.set_footer(text='Map: © Mario Kart Blog')
        await message.channel.send(embed=embed)

    # not needed
    # existed only for joke
    @staticmethod
    def setup(bot: commands.Bot):
        # my old team BP's joke
        if bot.user.id == 810319965164535848:
            Track.RMP.nicks.add('seimei')
            Track.TH.nicks.add('ｾｲﾒｲ')
            Track.RMMM.nicks.add('ﾜﾀｶﾞｼ')
            Track.SA.nicks.update({'dra', 'ﾄﾞﾗ'})
            Track.DEA.nicks.update({'kichi', 'ｷﾁ'})
            Track.DBP.nicks.update({'kami', 'kami track', 'ｵﾐｸｼﾞｺｰｽ'})
            Track.DWGM.nicks.update({'gomi', 'gomi track'})
            Track.DBB.nicks.add('ﾓｻﾞﾋﾞｰ')
            Track.RDKJ.nicks.add('jk')
            Track.CC.nicks.update({'新潟県', 'ﾆｲｶﾞﾀｹﾝ'})
