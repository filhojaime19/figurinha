from telegram.ext import Updater, CommandHandler

# Lista de usuários premium
PREMIUM_USERS = [1195062240]

def start(update, context):
    user_id = update.effective_user.id
    if user_id in PREMIUM_USERS:
        update.message.reply_text("🎉 Bem-vindo à versão Premium do Creating My Stickers Bot!")
    else:
        update.message.reply_text("👋 Olá! Este é o Creating My Stickers Bot. Versão gratuita disponível.")

def create_sticker(update, context):
    user_id = update.effective_user.id
    if user_id in PREMIUM_USERS:
        update.message.reply_text("✨ Criando sticker premium...")
    else:
        update.message.reply_text("🎨 Criando sticker gratuito...")

def premium(update, context):
    update.message.reply_text("💎 Versão Premium desbloqueia recursos exclusivos! Contate o suporte para upgrade.")

def ajuda(update, context):
    update.message.reply_text("""
Comandos disponíveis:
/start - Iniciar o bot
/create - Criar sticker
/premium - Informações sobre versão Premium
/ajuda - Mostrar esta ajuda
""")

def main():
    TOKEN = "7836447953:AAEzA8BEsKTjaa-DDeqa3fhOIfknTB__Bzs"
    updater = Updater(TOKEN, use_context=True)
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("create", create_sticker))
    dp.add_handler(CommandHandler("premium", premium))
    dp.add_handler(CommandHandler("ajuda", ajuda))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
