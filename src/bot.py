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
        self.dm = DBManager()

    async def on_guild_join(self, guild):
        """サーバーに参加

        Args:
            guild ([type]): サーバー情報
        """
        print('Joined guild {0}'.format(guild.name))

        # プラベチャンネル作成
        gm = GuildManager(dm, guild)
        ch = await gm.create_prv_channel()

    async def on_message(self, message):
        """メッセージ受信

        Args:
            message ([type]): メッセージ情報
        """
        if message.content.startswith('$hello'):
            gm = GuildManager(dm, message.guild)
            ch = await gm.create_prv_channel()
            print('カテゴリ:{0}, テキスト:{1}, ボイス:{2}'.format(
                ch['category'].name, ch['text'].name, ch['voice'].name))

        if message.content.startswith('$ch'):
            gm = GuildManager(dm, message.guild)
            ch = gm.get_prv_channel()
            print('カテゴリ:{0}, テキスト:{1}, ボイス:{2}'.format(
                ch['category'], ch['text'], ch['voice']))

    async def on_voice_state_update(self, member, before, after):
        """ボイスステータス変更

        Args:
            member ([type]): メンバー
            before ([type]): ステータス変更前
            after ([type]): ステータス変更後
        """
        vm = VoiceManager(dm, member.guild)
        vm.update_room_info(member, before, after)


client = DiscordClient()
client.run(os.environ['DISCORD_TOKEN'])
