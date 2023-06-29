import motor.motor_asyncio
import os


class DataBase:
    __database = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('MONGO_URI_DEV'))
    __current_database = __database['translator-bot']

    @classmethod
    async def InsertOne(cls, coll, data=None):
        if data is None:
            return

        db = cls.__current_database[coll]
        await db.insert_one(data)




