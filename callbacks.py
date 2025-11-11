from telegram import (
    Update, Message,
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    WebAppInfo, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton,
    ReplyKeyboardRemove,
)
from telegram.ext import CallbackContext, ConversationHandler

from db import is_user


def send_menu(message: Message) -> None:
    message.reply_text(
        text=f'Birorta bo\'limni tanlang!',
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

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user

    if is_user(user.id):
        send_menu(update.message)
    else:
        update.message.reply_text(
            text=f'Assalomu alaykum, {user.full_name}!',
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text='Ro\'yxatdan o\'tish'),
                        KeyboardButton(text='Davom etish'),
                    ]
                ]
            )
        )

def continue_chat(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Ogohlantirish: biror ish qilmoqchi bo\'lsangiz ro\'yxatdan o\'tish talab qilishi mumkin')
    send_menu(update.message)

def start_registration(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='Ro\'yxatadan o\'tish uchun malumotlaringizni kitiring?',
        reply_markup=ReplyKeyboardRemove()
    )

    return ask_name(update, context)

def ask_name(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='Ismingiz?',
        reply_markup=ReplyKeyboardRemove()
    )

    return 0

def set_name(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text='Yoshingiz?')

    return 1

def set_age(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='Location?',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text='Yuborish',
                        request_location=True
                    )
                ]
            ]
        )
    )

    return 2

def set_location(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='Contact?',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text='Yuborish',
                        request_contact=True
                    )
                ]
            ]
        )
    )

    return 3

def set_contact(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='Tasdiqlash?',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton('Ha'),
                    KeyboardButton('Yo\'q')
                ]
            ]
        )
    )

    return 4

def confirm(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='Tasdiqlandi',
        reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

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

