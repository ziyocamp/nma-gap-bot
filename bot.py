from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import Config
from callbacks import start, send_orders


def main() -> None:
    updater = Updater(Config.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        handler=CommandHandler(
            command='start',
            callback=start
        )
    )

    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('📦 Buyurtmalarim'),
            callback=send_orders
        )
    )

    updater.start_polling()
    updater.idle()

main()
