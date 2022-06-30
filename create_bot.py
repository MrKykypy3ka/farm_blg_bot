from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


API_TOKEN = '5135631699:AAGje63b9qb8ovRZ9aTq67sSGq5SWw_gKaw'
storage = MemoryStorage()

bot = Bot(token=API_TOKEN)
#bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)

