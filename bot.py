from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config
import commands

updater = Updater(token=config.bot_token, request_kwargs=config.proxy)
dispatcher = updater.dispatcher


start_command_handler = CommandHandler('start', commands.start_command)
text_message_handler = MessageHandler(Filters.text, commands.text_message_command)
help_command_handler = CommandHandler('help', commands.help_command)


dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(help_command_handler)


updater.start_polling(clean=True)
updater.idle()
