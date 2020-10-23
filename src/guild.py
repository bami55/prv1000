import discord


class GuildManager():
    """Guild管理
    """

    def __init__(self, db_manager, guild):
        self.dbm = db_manager
        self.guild = guild

    async def create_prv_channel(self):
        """プラベチャンネル作成
        """

        # infoチャンネル権限
        info_overwrites = {
            self.guild.default_role: discord.PermissionOverwrite(
                create_instant_invite=False,
                manage_channels=False,
                manage_messages=False,
                manage_permissions=False,
                manage_webhooks=False,
                send_messages=False,
                send_tts_messages=False,
            )
        }

        category = await self.guild.create_category(name='prv1000')
        info = await self.guild.create_text_channel(name='info', category=category, overwrites=info_overwrites)
        general = await self.guild.create_text_channel(name='general', category=category)
        voice = await self.guild.create_voice_channel(name='voice', category=category)
        ch = {
            'category': category,
            'info': info,
            'general': general,
            'voice': voice
        }
        self.dbm.add_guild(self.guild, ch)

    def get_prv_channel(self):
        self.dbm.get_guilds()
        category = self.guild.get_channel(766104828774449153)
        text = self.guild.get_channel(766104830112038943)
        voice = self.guild.get_channel(766104831400083456)
        return {
            'category': category,
            'text': text,
            'voice': voice
        }
