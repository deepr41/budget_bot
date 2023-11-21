#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import telebot
import time
import helper
import edit
import history
import pdf
import display
import estimate
import delete
import add
import budget
import analytics
import predict
import schedule
from datetime import datetime
from jproperties import Properties

configs = Properties()

with open("user.properties", "rb") as read_prop:
    configs.load(read_prop)

api_token = str(configs.get("api_token").data)

bot = telebot.TeleBot(api_token)

telebot.logger.setLevel(logging.INFO)

option = {}

# === Documentation of code.py ===

# Define listener for requests by user
def listener(user_requests):
    """
    listener(user_requests): Takes 1 argument user_requests and logs all user
    interaction with the bot including all bot commands run and any other issue logs.
    """
    for req in user_requests:
        if req.content_type == "text":
            print(
                "{} name:{} chat_id:{} \nmessage: {}\n".format(
                    str(datetime.now()),
                    str(req.chat.first_name),
                    str(req.chat.id),
                    str(req.text),
                )
            )

    message = (
        ("Sorry, I can't understand messages yet :/\n"
         "I can only understand commands that start with /. \n\n"
         "Type /faq or /help if you are stuck.")
    )

    try:
        helper.read_json()
        global user_list
        chat_id = user_requests[0].chat.id

        if user_requests[0].text[0] != "/":
            bot.send_message(chat_id, message)
    except Exception:
        pass

bot.set_update_listener(listener)

custom_commands = [
    ("/menu", "Show the main menu"),
    ("/add", "Add an expense"),
    ("/pdf", "Generate a PDF report"),
    ("/history", "View expenditure history"),
    ("/edit", "Edit a transaction"),
    ("/display", "Display total expenditure"),
    ("/estimate", "Estimate future expenditure"),
    ("/delete", "Delete a transaction"),
    ("/budget", "Manage your budget"),
    ("/analytics", "View analytics"),
    ("/predict", "Predict future budget"),
    ("/help", "Show available commands"),
    ("/faq", "Frequently Asked Questions"),
]

# Convert custom commands to BotCommand objects
commands = [telebot.types.BotCommand(command, description) for command, description in custom_commands]

# Set the bot's commands
bot.set_my_commands(commands)


@bot.message_handler(commands=["help"])
def help(m):

    helper.read_json()
    global user_list
    chat_id = m.chat.id

    message = "Here are the commands you can use: \n"
    commands = helper.getCommands()
    for c in commands:
        message += "/" + c + ", "
    message += "\nUse /menu for detailed instructions about these commands."
    bot.send_message(chat_id, message)

@bot.message_handler(commands=["faq"])
def faq(m):

    helper.read_json()
    global user_list
    chat_id = m.chat.id

    faq_message = (
        ('"What does this bot do?"\n'
         ">> DollarBot lets you manage your expenses so you can always stay on top of them! \n\n"
         '"How can I add an epxense?" \n'
         ">> Type /add, then select a category to type the expense. \n\n"
         '"Can I see history of my expenses?" \n'
         ">> Yes! Use /analytics to get a graphical display, or /history to view detailed summary.\n\n"
         '"I added an incorrect expense. How can I edit it?"\n'
         ">> Use /edit command. \n\n"
         '"Can I check if my expenses have exceeded budget?"\n'
         ">> Yes! Use /budget and then select the view category. \n\n")
    )
    bot.send_message(chat_id, faq_message)

# defines how the /start and /help commands have to be handled/processed
@bot.message_handler(commands=["start", "menu"])
def start_and_menu_command(m):
    """
    start_and_menu_command(m): Prints out the the main menu displaying the features that the
    bot offers and the corresponding commands to be run from the Telegram UI to use these features.
    Commands used to run this: commands=['start', 'menu']
    """
    helper.read_json()
    global user_list
    chat_id = m.chat.id

    text_intro = (
        ("Welcome to the Dollar Bot! \n"
         "DollarBot can track all your expenses with simple and easy to use commands :) \n"
         "Here is the complete menu. \n\n")
    )

    commands = helper.getCommands()
    for c in commands:  
        # generate help text out of the commands dictionary defined at the top
        text_intro += "/" + c + ": "
        text_intro += commands[c] + "\n\n"
    bot.send_message(chat_id, text_intro)
    return True

# defines how the /add command has to be handled/processed
@bot.message_handler(commands=["add"])
def command_add(message):
    """
    command_add(message) Takes 1 argument message which contains the message from
    the user along with the chat ID of the user chat. It then calls add.py to run to execute
    the add functionality. Commands used to run this: commands=['add']
    """
    add.run(message, bot)

# handles pdf command
@bot.message_handler(commands=["pdf"])
def command_pdf(message):
    """
    command_history(message): Takes 1 argument message which contains the message from
    the user along with the chat ID of the user chat. It then calls pdf.py to run to execute
    the add functionality. Commands used to run this: commands=['pdf']
    """
    pdf.run(message, bot)

# function to fetch expenditure history of the user
@bot.message_handler(commands=["history"])
def command_history(message):
    """
    command_history(message): Takes 1 argument message which contains the message from
    the user along with the chat ID of the user chat. It then calls history.py to run to execute
    the add functionality. Commands used to run this: commands=['history']
    """
    history.run(message, bot)

# function to edit date, category or cost of a transaction
@bot.message_handler(commands=["edit"])
def command_edit(message):
    """
    command_edit(message): Takes 1 argument message which contains the message from
    the user along with the chat ID of the user chat. It then calls edit.py to run to execute
    the add functionality. Commands used to run this: commands=['edit']
    """
    edit.run(message, bot)

# function to display total expenditure
@bot.message_handler(commands=["display"])
def command_display(message):
    """
    command_display(message): Takes 1 argument message which contains the message from the user
    along with the chat ID of the user chat. It then calls display.py to run to execute the add functionality.
    Commands used to run this: commands=['display']
    """
    display.run(message, bot)

# function to estimate future expenditure
@bot.message_handler(commands=["estimate"])
def command_estimate(message):
    estimate.run(message, bot)

# handles "/delete" command
@bot.message_handler(commands=["delete"])
def command_delete(message):
    """
    command_delete(message): Takes 1 argument message which contains the message from the user
    along with the chat ID of the user chat. It then calls delete.py to run to execute the add functionality.
    Commands used to run this: commands=['display']
    """
    delete.run(message, bot)

# handles budget command
@bot.message_handler(commands=["budget"])
def command_budget(message):
    budget.run(message, bot)

# handles analytics command
@bot.message_handler(commands=["analytics"])
def command_analytics(message):
    """
    command_analytics(message): Take an argument message with content and chat ID. Calls analytics to 
    run analytics. Commands to run this commands=["analytics"]
    """
    analytics.run(message, bot)

# handles predict command
@bot.message_handler(commands=["predict"])
def command_predict(message):
    """
    command_predict(message): Take an argument message with content and chat ID. Calls predict to 
    analyze budget and spending trends and suggest a future budget. Commands to run this commands=["predict"]
    """
    predict.run(message, bot)

def addUserHistory(chat_id, user_record):
    global user_list
    if not (str(chat_id) in user_list):
        user_list[str(chat_id)] = []
    user_list[str(chat_id)].append(user_record)
    return user_list



def monthly_recurrent_expense():
    categories = helper.getRecurrentCategories()
    data = helper.read_json()
    chat_id = list(data.keys())[0]
    for cat in categories:
        date_of_entry = datetime.today().strftime(helper.getDateFormat())  
        amount_value = helper.recurrent_spend_categories[cat]

        date_str, category_str, amount_str = (
            str(date_of_entry),
            str(chat_id),
            str(amount_value),
        )

        helper.write_json(
            add.add_user_record(
                chat_id, "{},{},{}".format(date_str, category_str, amount_str)
            )
        )
        bot.send_message(
            chat_id,
            "The following expenditure has been recorded: You have spent {} {} for {} on {}".format(
                helper.getOverallCurrency(chat_id), amount_str, category_str, date_str
            ),
        )

# Schedule the function to run on the 1st of every month
schedule.every().month.at("00:00").do(monthly_recurrent_expense)

def main():
    """
    main() The entire bot's execution begins here. It ensure the bot variable begins
    polling and actively listening for requests from telegram.
    """
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logging.exception(str(e))
        time.sleep(3)
        print("Connection Timeout")

if __name__ == "__main__":
    main()