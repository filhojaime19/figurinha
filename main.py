# Criar polyfill para imghdr
import sys
import mimetypes

if 'imghdr' not in sys.modules:
    class imghdr:
        @staticmethod
        def what(file):
            try:
                mime_type, _ = mimetypes.guess_type(file)
                if mime_type and mime_type.startswith('image/'):
                    return mime_type.split('/')[1]
                return None
            except:
                return None
    sys.modules['imghdr'] = imghdr

# Agora importar as bibliotecas
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Lista de usuários premium
PREMIUM_USERS = [1195062240]

def start(update, context):
    user_id = update.effective_user.id
    if user_id in PREMIUM_USERS:
        keyboard = [
            [InlineKeyboardButton("🎨 Criar Sticker", callback_data='create')],
            [InlineKeyboardButton("💎 Premium", callback_data='premium')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(
            "🎉 Bem-vindo Premium! Escolha uma opção:",
            reply_markup=reply_markup
        )
    else:
        keyboard = [
            [InlineKeyboardButton("🎨 Criar Sticker", callback_data='create')],
            [InlineKeyboardButton("💎 Upgrade Premium", callback_data='premium')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(
            "👋 Bem-vindo! Escolha uma opção:",
            reply_markup=reply_markup
        )

def button(update, context):
    query = update.callback_query
    query.answer()
    
    user_id = query.from_user.id
    is_premium = user_id in PREMIUM_USERS
    
    if query.data == 'create':
        if is_premium:
            query.edit_message_text("✨ Envie uma imagem para criar seu sticker premium!")
        else:
            query.edit_message_text("🎨 Envie uma imagem para criar seu sticker gratuito!")
    
    elif query.data == 'premium':
        if is_premium:
            query.edit_message_text("💎 Você já é Premium! Aproveite todos os recursos ilimitados!")
        else:
            query.edit_message_text("💎 Versão Premium: R$ 9,90/mês\n• Criação ilimitada\n• Stickers HD\n• Suporte prioritário")

def handle_photo(update, context):
    user_id = update.effective_user.id
    is_premium = user_id in PREMIUM_USERS
    
    if is_premium:
        update.message.reply_text("✨ Sticker Premium criado com sucesso! 🎉")
    else:
        update.message.reply_text("🎨 Sticker gratuito criado! (Limite: 3/dia)")

def main():
    TOKEN = "7836447953:AAEzA8BEsKTjaa-DDeqa3fhOIfknTB__Bzs"
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))

    updater.start_polling()
    print("Bot iniciado com sucesso!")
    updater.idle()

if __name__ == '__main__':
    main()