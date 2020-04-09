from utils import send_typing_action


@send_typing_action
def add_handler(update, context):
    parameter_list = " ".join(context.args).split(" ")
    counter = 0

    for i in parameter_list:
        try:
            i = float(i)
            counter += i
        except:
            update.message.reply_text("Please don't put non-number item(s)")
            return

    counter = '{:,.2f}'.format(counter)
    update.message.reply_text(counter)


@send_typing_action
def multiply_handler(update, context):
    parameter_list = " ".join(context.args).split(" ")
    counter = 1.0

    for i in parameter_list:
        try:
            i = float(i)
            counter *= i
        except:
            update.message.reply_text("Please don't put non-number item(s)")
            return

    counter = '{:,.2f}'.format(counter)
    update.message.reply_text(counter)


@send_typing_action
def divide_handler(update, context):
    parameter_list = " ".join(context.args).split(" ")
    counter = 1.0

    try:
        counter = float(parameter_list[0])
    except:
        update.message.reply_text("Please don't put non-number item(s)")
        return

    for i in range(1, len(parameter_list)):
        try:
            temp = float(parameter_list[i])
            counter /= temp
        except:
            update.message.reply_text("Please don't put non-number item(s)")
            return

    counter = '{:,.2f}'.format(counter)
    update.message.reply_text(counter)


@send_typing_action
def subtract_handler(update, context):
    parameter_list = " ".join(context.args).split(" ")

    if (len(parameter_list) == 1):
        try:
            update.message.reply_text(float(parameter_list[0]))
            return
        except:
            update.message.reply_text("Please don't put non-number item(s)")
            return

    else:
        try:
            counter = float(parameter_list[0])
        except:
            update.message.reply_text("Please don't put non-number item(s)")
            return

        for i in range(1, len(parameter_list)):
            try:
                temp = float(parameter_list[i])
                counter -= temp
            except:
                update.message.reply_text(
                    "Please don't put non-number item(s)")
                return
        counter = '{:,.2f}'.format(counter)
        update.message.reply_text(counter)
