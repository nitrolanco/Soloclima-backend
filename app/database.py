from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()


class MongoDBService:
    _client = None

    @classmethod
    async def get_client(cls):
        if cls._client is None:
            mongo_uri = os.getenv("MONGO_URI")
            mongo_dbname = os.getenv("MONGO_DBNAME")
            print(mongo_uri, mongo_dbname)
            if not mongo_uri or not mongo_dbname:
                raise ValueError(
                    "MONGO_URI and MONGO_DBNAME must be set in the environment variables"
                )

            try:
                cls._client = AsyncIOMotorClient(mongo_uri, server_api=ServerApi("1"))
                await cls._client.admin.command("ping")
                print("Pinged your deployment. You successfully connected to MongoDB!")
            except Exception as e:
                print(f"Error connecting to MongoDB: {e}")
                raise

        return cls._client

    @classmethod
    async def get_database(cls):
        client = await cls.get_client()
        return client[os.getenv("MONGO_DBNAME")]
