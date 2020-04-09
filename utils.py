from functools import wraps
from telegram import ChatAction
from db_parser import parse_user_ids_manager_in_bot_db, parse_bot_db
import os

LIST_OF_ADMINS = [
    os.getenv("RICKY_USER_ID"),
    os.getenv("WINDI_USER_ID"),
]


def send_typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(
            chat_id=update.effective_message.chat_id, action=ChatAction.TYPING)
        return func(update, context,  *args, **kwargs)

    return command_func


def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(update, context, *args, **kwargs)
    return wrapped


def is_ricky(update):
    if (update.effective_user.id) == LIST_OF_ADMINS[0]:
        return True
    return False


def force_get_id_handler(update, context):
    ids_manager = parse_user_ids_manager_in_bot_db(context)
    if (update.message.from_user['id'] not in ids_manager):
        ids_manager[update.message.from_user['id']] = "{} {}".format(update.message.from_user['first_name'], update.message.from_user['last_name'])

@restricted
@send_typing_action
def read_ids(update, context):
    ids_manager = parse_user_ids_manager_in_bot_db(context)
    update.message.reply_text(ids_manager)