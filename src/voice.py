

class VoiceManager():
    """VC管理
    """

    def __init__(self, db_manager, guild):
        self.dm = db_manager
        self.guild = guild

    async def update_room_info(self, member, before, after):
        if before.channel.id == after.channel.id:
            return

        # DBボイス情報取得
        vc_guild = dm.get_guilds({'id': member.guild.id})
        before_vc = dm.get_voice_state_channels(
            {'voice_id': before.channel.id})
        after_vc = dm.get_voice_state_channels({'voice_id': after.channel.id})

        if before_vc is None:
            # 入室
        elif after_vc is None:
            # 退室
        else:
            return

        print(
            '--- voice state update ---'
            f'Server: {self.guild.name}'
            f'User: {member.display_name}'
            f'Before: {before.channel} - Mute: {before.self_mute}'
            f'After: {after.channel} - Mute: {after.self_mute}'
        )
