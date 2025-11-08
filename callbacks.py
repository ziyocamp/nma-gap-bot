from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text=f'Assalomu alaykum {update.message.from_user.first_name}!',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text='🛍 Buyurtma berish',
                        web_app=WebAppInfo(url='https://uzum.uz')
                    )
                ],
                [
                    KeyboardButton(
                        text='📦 Buyurtmalarim'
                    ),
                    KeyboardButton(
                        text='⚙️ Sozlamalar'
                    )
                ],
                [
                    KeyboardButton(
                        text='ℹ️ Biz haqimizda'
                    ), 
                    KeyboardButton(
                        text='✍️ Fikr qoldirish'
                    )
                ]
            ],
            resize_keyboard=True,
        )
    )
    
def send_orders(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Sizda hali birorta ham buyurtma yo`q')

