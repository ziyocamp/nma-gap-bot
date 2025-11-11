from telegram import (
    Update, 
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    WebAppInfo, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton,
)
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
    
def send_about(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('shu yerda joylashganmiz')
    update.message.reply_markdown_v2('*Elektron pochta*: ||abror4work@gmail\.com||')
    
def send_settings(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='⚙️ Sozlamalar',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text='🌐 Tilni o\'zgartirish'
                    )
                ],
                [
                    KeyboardButton(
                        text='🌐 Raqamni o\'zgartirish'
                    )
                ],
                [
                    KeyboardButton(
                        text='Orqaga'
                    )
                ],
            ]
        )
    )
    
def change_language(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='tilni tanlang',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Uzbek',
                        callback_data='change_lang:uz'
                    ),
                    InlineKeyboardButton(
                        text='English',
                        callback_data='change_lang:en'
                    )
                ]
            ]
        )
    )

def set_language(update: Update, context: CallbackContext) -> None:
    data = update.callback_query.data
    
    selected_lan = data.split(':')[1]
    
    if selected_lan == 'uz':
        update.callback_query.message.reply_text('O\'zbek tili tanlandi')
    elif selected_lan == 'en':
        update.callback_query.message.reply_text('Ingliz tili tanlandi')

