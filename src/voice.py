

class VoiceManager():
    """VC管理
    """

    def __init__(self, db_manager, guild):
        self.dm = db_manager
        self.guild = guild

    async def update_room_info(self, member, before, after):
        if before.channel.id == after.channel.id:
            return

        # TODO DBボイス情報取得

        print(
            '--- voice state update ---'
            f'Server: {self.guild.name}'
            f'User: {member.display_name}'
            f'Before: {before.channel} - Mute: {before.self_mute}'
            f'After: {after.channel} - Mute: {after.self_mute}'
        )
