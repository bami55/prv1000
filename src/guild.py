

class GuildManager():
    """Guild管理
    """

    def __init__(self, db_manager, guild):
        self.dm = db_manager
        self.guild = guild

    async def create_prv_channel(self):
        """プラベチャンネル作成
        """
        name = 'prv1000'
        text_name = f'{name}-text'
        voice_name = f'{name}-voice'
        category = await self.guild.create_category(name=name)
        text = await self.guild.create_text_channel(name=text_name, category=category)
        voice = await self.guild.create_voice_channel(name=voice_name, category=category)
        ch = {
            'category': category,
            'text': text,
            'voice': voice
        }
        self.dm.add_guild(guild, ch)

    def get_prv_channel(self):
        self.dm.get_guilds()
        category = self.guild.get_channel(766104828774449153)
        text = self.guild.get_channel(766104830112038943)
        voice = self.guild.get_channel(766104831400083456)
        return {
            'category': category,
            'text': text,
            'voice': voice
        }
