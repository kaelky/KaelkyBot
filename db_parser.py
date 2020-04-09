from telegram.ext import CallbackContext

def parse_user_db(context: CallbackContext):
    return context.user_data.setdefault('user_account', {})

def parse_bot_db(context: CallbackContext):
    return context.bot_data.setdefault('bot_account', {})

def parse_user_ids_manager_in_bot_db(context: CallbackContext):
    return parse_bot_db(context).setdefault('ids', {})