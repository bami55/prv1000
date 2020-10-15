
class GuildManager():
    """Guild管理
    """
    
    def __init__(self, guild):
        self.guild = guild

    async def create_prv_channel(self):
        name = 'prv1000'
        text_name = f'{name}-text'
        voice_name = f'{name}-voice'
        category = await self.guild.create_category(name=name)
        text = await self.guild.create_text_channel(name=text_name, category=category)
        voice = await self.guild.create_voice_channel(name=voice_name, category=category)
        return {
            'category': category,
            'text': text,
            'voice': voice
        }
