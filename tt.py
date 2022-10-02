# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor

# bot = Bot(token = "5355485558:AAGvUcfxgesXykH2Aqftak3gMqRYSGUbImQ")
# dp = Dispatcher(bot)

# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     await message.reply("Привет мир")

# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     await message.reply("Я эхо бот")    

# @dp.message_handler(commands = ['photo'])
# async def photo(message: types.Message):
#     await message.reply("https://docs.aiogram.dev/en/dev-3.x/_static/logo.png")

# @dp.message_handler()
# async def echo(message: types.Message):
#     r1 = 'https://docs.aiogram.dev/en/dev-3.x/_static/logo.png'
#     with open('photo', 'rb') as pic1:
#          await bot.send_photo(message.from_user.id, pic1, caption=XXXXX, reply_markup=KB)



# if __name__ == '__main__':
#     executor.start_polling(dp)