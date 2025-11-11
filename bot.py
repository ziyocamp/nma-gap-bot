from telegram.ext import (
    Updater, CommandHandler, 
    MessageHandler, Filters,
    CallbackQueryHandler,
)

from config import Config
from callbacks import (
    start, send_orders, 
    send_about, change_language, 
    send_settings, set_language,
)


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

    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('ℹ️ Biz haqimizda'),
            callback=send_about
        )
    )

    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('⚙️ Sozlamalar'),
            callback=send_settings
        )
    )

    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('Orqaga'),
            callback=start
        )
    )

    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('🌐 Tilni o\'zgartirish'),
            callback=change_language
        )
    )

    dispatcher.add_handler(
        handler=CallbackQueryHandler(
            callback=set_language
        )
    )

    updater.start_polling()
    updater.idle()

main()
