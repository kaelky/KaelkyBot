import telegram
import telegram.ext

from utils import send_typing_action, restricted
from random import seed, randint
from telegram.ext import CallbackContext

@send_typing_action
def which_handler(update, context):
    parameter_list = " ".join(context.args).split(" or ")

    if (len(parameter_list) >= 1):
        value = randint(0, len(parameter_list)-1)
        update.message.reply_text(parameter_list[value])


@send_typing_action
def roll_handler(update, context):
    parameter_list = " ".join(context.args).split(" ")
    if (len(parameter_list) == 2):
        try:
            first_num = int(parameter_list[0])
            last_num = int(parameter_list[1])
            value = randint(first_num, last_num)
            update.message.reply_text(value)
        except:
            update.message.reply_text(
                "Something went wrong. The command is /roll <lower bound> <upper bound>")
    else:
        value = randint(1, 6)
        update.message.reply_text(value)

@restricted
@send_typing_action
def say_handler(update, context):
    parameter_list = " ".join(context.args)
    update.message.reply_text(parameter_list)