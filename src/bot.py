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
        dm = DBManager()

    async def on_guild_join(self, guild):
        # サーバーに参加
        print('Joined guild {0}'.format(guild.name))

        # チャンネル作成
        gm = GuildManager(guild)
        ch = await gm.create_prv_channel()
        print('カテゴリ:{0}, テキスト:{1}, ボイス:{2}'.format(
            ch['category'].name, ch['text'].name, ch['voice'].name))

    async def on_message(self, message):
        # メッセージ受信
        if message.content.startswith('$hello'):
            gm = GuildManager(message.guild)
            ch = await gm.create_prv_channel()
            print('カテゴリ:{0}, テキスト:{1}, ボイス:{2}'.format(
                ch['category'].name, ch['text'].name, ch['voice'].name))

        if message.content.startswith('$ch'):
            gm = GuildManager(message.guild)
            ch = gm.get_prv_channel()
            print('カテゴリ:{0}, テキスト:{1}, ボイス:{2}'.format(
                ch['category'], ch['text'], ch['voice']))

    async def on_voice_state_update(self, member, before, after):
        # VCステータス変更
        vm = VoiceManager()
        vm.update_room_info(member, before, after)


client = DiscordClient()
client.run(os.environ['DISCORD_TOKEN'])
