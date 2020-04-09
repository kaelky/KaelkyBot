import logging
import os
import random
import sys
import traceback
import telegram.ext

from telegram.ext import Updater, CommandHandler, CallbackContext, PicklePersistence, Filters, MessageHandler
from telegram.utils.helpers import mention_html

from utils import send_typing_action, force_get_id_handler, read_ids
from private_ability_handlers import tell_basic_handler, mention_all_fetched_ids_users
from calculator_handlers import add_handler, subtract_handler, multiply_handler, divide_handler
from helper_handlers import roll_handler, which_handler, say_handler

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

persistence = PicklePersistence('./db')

MODE = os.getenv("MODE", "dev")
TOKEN = os.getenv("TOKEN")
if MODE == "dev":
    def run(updater):
        updater.start_polling()
elif MODE == "prod":
    def run(updater):
        PORT = int(os.environ.get("PORT", "8443"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN)
        updater.bot.set_webhook(
            "https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))
else:
    logger.error("No MODE specified!")
    sys.exit(1)


@send_typing_action
def start_handler(update, context):
    update.message.reply_text("Hello, {}! I'm KaelkyBot ready to help you!".format(
        update.message.from_user.first_name))
    print(update.effective_message.chat_id)

if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True, persistence=persistence)
    job_queue = updater.job_queue
    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(CommandHandler("add", add_handler))
    updater.dispatcher.add_handler(
        CommandHandler("subtract", subtract_handler))
    updater.dispatcher.add_handler(
        CommandHandler("multiply", multiply_handler))
    updater.dispatcher.add_handler(CommandHandler("divide", divide_handler))
    updater.dispatcher.add_handler(CommandHandler("roll", roll_handler))
    updater.dispatcher.add_handler(CommandHandler("which", which_handler))
    updater.dispatcher.add_handler(CommandHandler("say", say_handler))
    updater.dispatcher.add_handler(CommandHandler("tell_basic", tell_basic_handler))
    updater.dispatcher.add_handler(CommandHandler("secrets", read_ids))
    # updater.dispatcher.add_handler(CommandHandler("everyones", mention_all_fetched_ids_users))
    updater.dispatcher.add_handler(MessageHandler(Filters.all, force_get_id_handler))
    run(updater)
