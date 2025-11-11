from telegram.ext import (
    Updater, CommandHandler, 
    MessageHandler, Filters,
    CallbackQueryHandler,
    ConversationHandler,
)

from config import Config
from callbacks import (
    start, send_orders, 
    send_about, change_language, 
    send_settings, set_language,
    continue_chat, 
    start_registration,
    ask_name, set_name, set_age, set_location, set_contact, confirm,
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
            filters=Filters.text('Davom etish'),
            callback=continue_chat
        )
    )

    dispatcher.add_handler(
        handler=ConversationHandler(
            entry_points=[
                MessageHandler(
                    filters=Filters.text('Ro\'yxatdan o\'tish'),
                    callback=start_registration
                ),
            ],
            states={
                0: [
                    MessageHandler(
                        filters=Filters.text,
                        callback=set_name
                    ),
                ],
                1: [
                    MessageHandler(
                        filters=Filters.text,
                        callback=set_age
                    ),
                ],
                2: [
                    MessageHandler(
                        filters=Filters.location,
                        callback=set_location
                    ),
                ],
                3: [
                    MessageHandler(
                        filters=Filters.contact,
                        callback=set_contact
                    ),
                ],
                4: [
                    MessageHandler(
                        filters=Filters.text('Ha'),
                        callback=confirm
                    ),
                    MessageHandler(
                        filters=Filters.text('Yo\'q'),
                        callback=ask_name
                    ),
                ],
            },
            fallbacks=[]
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

    # ConversationHandler
    updater.start_polling()
    updater.idle()

main()
