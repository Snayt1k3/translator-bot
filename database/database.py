import motor.motor_asyncio
import os


class DataBase:
    """Class for manage MongoDB"""
    __database = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('MONGO_DOCKER_URI'))
    __current_database = __database['translator-bot']

    @classmethod
    async def InsertOne(cls, coll, data=None):
        if data is None:
            return

        db = cls.__current_database[coll]
        await db.insert_one(data)




