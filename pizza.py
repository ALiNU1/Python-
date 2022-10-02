
# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor

# bot = Bot(token = "5387893307:AAFNwVxqX80KtGzqFMQk5t6iZEDHzCWhgwE")
# dp = Dispatcher(bot)

# '''********************************КЛИЕНТСКАЯ ЧАСТЬ**************************************'''

# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     await message.reply("Привет мир")

# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     await message.reply("Я эхо бот")    

# '''*********************************АДМИНСКАЯ ЧАСТЬ********************************************'''



# '''*********************************ОБЩАЯ ЧАСТЬ************************************************'''


# executor.start.polling(dp,skip_updates = True)


# if __name__ == '__main__':
#     executor.start_polling(dp)