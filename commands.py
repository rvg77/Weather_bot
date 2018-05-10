import weather
import images


def start_command(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Введите /help чтобы понять как работает бот.'
                          '\n\n'
                          'Type /help to find out how bot works.')


def help_command(bot, update):
    response = 'Чтобы посмотреть текущую погоду, введите название города ' \
               'на русском или английском языке.\n' \
               'Note: \nДобавьте в конец "ru" или другой двухбуквенный ' \
               'псевдоним страны для точности.\n\n' \
               'Type a name of the city to watch current weather' \
               '(in Russian or in English).\n' \
               'Note: \nYou can add "ru" or other 2-letter name of the country to the and of request.'

    bot.send_message(chat_id=update.message.chat_id, text=response)


def text_message_command(bot, update):
    city = update.message.text
    try:
        response, status = weather.info(city)
    except BaseException:
        bot.send_message(chat_id=update.message.chat_id,
                         text='Incorrect city. Please, try again.\n\n'
                              'Некорректный город. Пожалуйста, попробуйте еще раз.')
        return
    bot.send_message(chat_id=update.message.chat_id, text=response)
    try:
        photo = images.get([city, status])
        bot.send_photo(chat_id=update.message.chat_id, photo=photo)
    except BaseException:
        return
