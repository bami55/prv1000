

class VoiceManager():
    """VC管理
    """

    def __init__(self, db_manager, guild):
        self.dbm = db_manager
        self.guild = guild

    def update_voice_state_channels(self, member, before, after):
        """
        """
        if before.channel.id == after.channel.id:
            return

        # DBボイス情報取得
        vc_guild = self.dbm.get_guilds({'id': member.guild.id})
        before_vc = self.dbm.get_voice_state_channels({'voice_id': before.channel.id})
        after_vc = self.dbm.get_voice_state_channels({'voice_id': after.channel.id})

        # DBボイス情報更新
        if after_vc is not None:
            # 入室
            if member.id not in after_vc['members']:
                after_vc['members'].append(member.id)
                self.dbm.set_voice_state_channels(after_vc)
        elif before_vc is not None:
            # 退室
            if member.id in before_vc['members']:
                before_vc['members'] = [m for m in before_vc['members'] if m != member.id]
                self.dbm.set_voice_state_channels(before_vc)
        else:
            return
