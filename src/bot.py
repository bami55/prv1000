import discord
import os
from dotenv import load_dotenv
from guild import GuildManager
from voice import VoiceManager
from db import DBManager

load_dotenv()


class DiscordClient(discord.Client):
    async def on_ready(self):
        # 起動確認
        print('Logged on as {0}!'.format(self.user))
        self.dbm = DBManager()

    async def on_guild_join(self, guild):
        """サーバーに参加

        Args:
            guild ([type]): サーバー情報
        """
        # プラベチャンネル作成
        gm = GuildManager(dbm, guild)
        ch = await gm.create_prv_channel()

    async def on_message(self, message):
        """メッセージ受信

        Args:
            message ([type]): メッセージ情報
        """
        if message.content.startswith('$hello'):
            gm = GuildManager(dbm, message.guild)
            ch = await gm.create_prv_channel()

        if message.content.startswith('$ch'):
            gm = GuildManager(dbm, message.guild)
            ch = gm.get_prv_channel()

    async def on_voice_state_update(self, member, before, after):
        """ボイスステータス変更

        Args:
            member ([type]): メンバー
            before ([type]): ステータス変更前
            after ([type]): ステータス変更後
        """
        vm = VoiceManager(dbm, member.guild)
        vm.update_room_info(member, before, after)


client = DiscordClient()
client.run(os.environ['DISCORD_TOKEN'])
