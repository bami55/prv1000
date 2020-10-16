

class VoiceManager():
    """VC管理
    """

    async def update_room_info(self, member, before, after):
        guild = member.guild
        if before.channel.id == after.channel.id:
            return

        print(
            '--- voice state update ---'
            f'Server: {member.guild.name}'
            f'User: {member.display_name}'
            f'Before: {before.channel} - Mute: {before.self_mute}'
            f'After: {after.channel} - Mute: {after.self_mute}'
        )
