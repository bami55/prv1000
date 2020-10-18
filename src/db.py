import os
from pymongo import MongoClient


class DBManager():
    """Database管理
    """

    def __init__(self):
        self.client = MongoClient(
            "mongodb+srv://mongo:{password}@cluster0.7zwnv.mongodb.net/{dbname}?retryWrites=true&w=majority".format(dbname=os.environ['DB_USER'], password=os.environ['DB_PASSWORD']))
        self.db = self.client[os.environ['DB_NAME']]
        self.guilds = self.db.get_collection('guilds')
        self.voice_state_channels = self.db.get_collection(
            'voice_state_channels')

    def add_guild(self, guild, channels=None):
        """サーバー新規登録

        Args:
            guild ([type]): サーバー情報
            channels ([type], optional): チャンネル情報. Defaults to None.
        """
        guild_doc = {
            'id': guild.id,
            'name': guild.name
        }
        if channels is not None:
            guild_doc['category_id'] = channels['category'].id
            guild_doc['category_name'] = channels['category'].name
            guild_doc['text_id'] = channels['text'].id
            guild_doc['text_name'] = channels['text'].name
            guild_doc['voice_id'] = channels['voice'].id
            guild_doc['voice_name'] = channels['voice'].name

            # ボイス新規登録
            self.voice_state_channels.insert_one({
                'guild_id': guild_doc['id'],
                'voice_id': guild_doc['voice_id']
            })

        # サーバー新規登録
        self.guilds.insert_one(guild_doc)

    def get_guilds(self, filter=None, sort=None):
        """サーバー情報取得

        Args:
            filter ([type], optional): フィルター. Defaults to None.
            sort ([type], optional): ソート. Defaults to None.

        Returns:
            [type]: サーバー情報
        """
        return self.guilds.find(filter=filter, sort=sort)

    def get_voice_state_channels(self, filter=None, sort=None):
        """ボイス情報取得

        Args:
            filter ([type], optional): フィルター. Defaults to None.
            sort ([type], optional): ソート. Defaults to None.

        Returns:
            [type]: ボイス情報
        """
        return self.voice_state_channels.find(filter=filter, sort=sort)
