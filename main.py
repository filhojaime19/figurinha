from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Lista de usuários premium (adicione IDs de teste aqui)
PREMIUM_USERS = [1195062240]  # Substitua pelos IDs reais dos usuários premium

# Comando /start
def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id in PREMIUM_USERS:
        update.message.reply_text("🎉 Bem-vindo à versão Premium do bot!")
    else:
        update.message.reply_text("👋 Olá! Este é o Creating My Stickers Bot. Versão gratuita disponível.")

# Comando /create (exemplo de criação de sticker)
def create_sticker(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id in PREMIUM_USERS:
        update.message.reply_text("✨ Criando sticker premium...")
    else:
        update.message.reply_text("🎨 Criando sticker gratuito...")

# Comando /premium
def premium(update: Update, context: CallbackContext):
    update.message.reply_text("💎 Para acessar a versão Premium, entre em contato com o suporte.")

# Função principal
def main():
    # Substitua 'SEU_TOKEN_AQUI' pelo token do seu bot
    updater = Updater("7836447953:AAEzA8BEsKTjaa-DDeqa3fhOIfknTB__Bzs", use_context=True)

    # Adiciona os comandos ao bot
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("create", create_sticker))
    dp.add_handler(CommandHandler("premium", premium))

    # Inicia o bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
