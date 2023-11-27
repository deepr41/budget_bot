import helper
from datetime import datetime
from telebot import types


option = {}

def run(message, bot):
    chat_id = message.chat.id
    option[chat_id]=message.text
    msg = bot.send_message(
            chat_id, "Add source name  \n"
        )

    bot.register_next_step_handler(msg, post_income_selection, bot)

def post_income_selection(message, bot):
    source_entered = message.text
    print("sourceName:",source_entered)
    chat_id = message.chat.id
    option[chat_id]=message.text
    message = bot.send_message(
            chat_id, "Income Value {}? \n(Numeric values only)".format(str(option[chat_id]))
        )
    bot.register_next_step_handler(message, post_source_name, bot,source_entered)
    

def post_source_name(message, bot,source_entered):
    chat_id = message.chat.id
    amount_entered = message.text
    print("income amount:",amount_entered)
    date_of_entry = datetime.today().strftime(helper.getDateFormat())

    date_str, incomename_str, amount_str = (
            str(date_of_entry),
            str(source_entered),
            str(amount_entered),
        )

    helper.write_json(
            add_user_record(
                chat_id, "{},{},{}".format(date_str, incomename_str, amount_str)
            )
        )
    bot.register_next_step_handler(message, updateOverallBudget, bot,amount_entered)


def updateOverallBudget(message, bot,amount_entered):
    chat_id = message.chat.id
    print("updating overall budget after income")
    user_list = helper.read_json()
    if str(chat_id) not in user_list:
            user_list[str(chat_id)] = helper.createNewUserRecord()
    overall=user_list[str(chat_id)]["budget"]["budget"]
    user_list[str(chat_id)]["budget"]["budget"] = float(overall)+amount_entered
    helper.write_json(user_list)
    bot.send_message(chat_id, "Overall Budget Updated!")

def add_user_record(chat_id, record_to_be_added):
    """
    add_user_record(chat_id, record_to_be_added): Takes 2 arguments -
    chat_id or the chat_id of the user's chat, and record_to_be_added which
    is the expense record to be added to the store. It then stores this expense record in the store.
    """
    user_list = helper.read_json()
    print("!" * 5)
    print("before")
    print(user_list)
    print("!" * 5)
    if str(chat_id) not in user_list:
        user_list[str(chat_id)] = helper.createNewUserRecord()

    user_list[str(chat_id)]["income"].append(f"{record_to_be_added}")
    print("!" * 5)
    print("after")
    print(user_list)
    print("!" * 5)
    return user_list