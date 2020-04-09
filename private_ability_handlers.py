import os
import telegram

from telegram import ParseMode

from utils import restricted, send_typing_action
from db_parser import parse_bot_db, parse_user_db, parse_user_ids_manager_in_bot_db

@restricted
@send_typing_action
def tell_basic_handler(update, context):
    parameter_list = " ".join(context.args)
    context.bot.send_message(chat_id=os.getenv("BASIC_WW_GROUP_CHAT_ID"), text=parameter_list)

@restricted
@send_typing_action
def mention_all_fetched_ids_users(update, context):
    ids_manager = parse_user_ids_manager_in_bot_db(context)
    if len(ids_manager) != 0:
        users = []
        for i in ids_manager:
            users.append("[{}](tg://user?id={})".format(ids_manager[i], i))
        for user in users:
            context.bot.send_message(chat_id=os.getenv("BASIC_WW_GROUP_CHAT_ID"), text=users[user], parse_mode=telegram.ParseMode.MARKDOWN_V2)
        return