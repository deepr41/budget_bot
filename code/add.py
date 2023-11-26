import helper
import logging
from telebot import types
from datetime import datetime

option = {}

# === Documentation of add.py ===
supported_currencies = ["USD", "INR", "EUR", "GBP"]

def run(message, bot):
    helper.read_json()
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    chat_id = message.chat.id
    expense_history = helper.getUserHistory(chat_id)
    for c in helper.getTransactionTypes()[:-1]:
        markup.add(c)
    if expense_history:
        markup.add(helper.getTransactionTypes()[-1])
        # recur_msg = bot.send_message(chat_id,"You have previously recorded expenses. Do you want to repeat one of these expenses?(Y/N)")
        # bot.register_next_step_handler(recur_msg, record_expense, bot, expense_history)
    msg = bot.reply_to(message, "Add type", reply_markup=markup)
    bot.register_next_step_handler(msg, post_transaction_selection, bot, expense_history)

def post_transaction_selection(message, bot, expense_history):
    """
    """
    transaction_type = message.text
    bot.reply_to(message, transaction_type)
    if(transaction_type not in helper.getTransactionTypes()):
        helper.throw_exception("Unable to find the type of transaction.")
    if(transaction_type == "New"):
        date_of_entry = datetime.today().strftime(helper.getDateFormat())
        new_expense(message, bot, date_of_entry)
    elif(transaction_type == "Old"):
        old_expense_day(message, bot)
    else:
        date_of_entry = datetime.today().strftime(helper.getDateFormat())
        record_expense(message, bot, expense_history, date_of_entry)

def new_expense(message, bot, date_of_entry):
    """
    run(message, bot): This is the main function used to implement the add feature.
    It pop ups a menu on the bot asking the user to choose their expense category,
    after which control is given to post_category_selection(message, bot) for further proccessing.
    It takes 2 arguments for processing - message which is the message from the user,
    and bot which is the telegram bot object from the main code.py function.
    """
    helper.read_json()
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    for c in helper.getSpendCategories():
        markup.add(c)
    markup.add("Add new category")
    msg = bot.reply_to(message, "Select Category", reply_markup=markup)
    bot.register_next_step_handler(msg, post_category_selection, bot, date_of_entry)

def old_expense_day(message, bot):
    """
    When adding an old expense
    """
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2

    days_list = helper.getDaysList()

    for c in days_list:
        markup.add(c)
    
    msg = bot.reply_to(message, "Select Day", reply_markup=markup)
    bot.register_next_step_handler(msg, old_expense_month, bot)

def old_expense_month(message, bot):
    """
    When adding an old expense
    """
    date =  message.text
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2

    months_list = helper.getMonthsList()

    for c in months_list:
        markup.add(c)
    
    msg = bot.reply_to(message, "Select Month", reply_markup=markup)
    bot.register_next_step_handler(msg, old_expense_year, bot, date)

def old_expense_year(message, bot, date):
    """
    When adding an old expense
    """
    month = message.text

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2

    year_list = helper.getYearList()

    for c in year_list:
        markup.add(c)
    
    msg = bot.reply_to(message, "Select Year", reply_markup=markup)
    bot.register_next_step_handler(msg, post_old_date_selection, bot, date, month)

def post_old_date_selection(message, bot, date, month):
    year = message.text

    date_of_entry = f'{date}-{month}-{year}'
    new_expense(message, bot, date_of_entry)

def post_append_spend(message, bot, date_of_entry):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    selected_category = message.text
    chat_id = message.chat.id
    allocated_categories = helper.getCategoryBudget(chat_id)
    if selected_category not in allocated_categories.keys():
        helper.updateBudgetCategory(chat_id,selected_category)
    helper.spend_categories.insert(0,selected_category)
    for c in helper.getSpendCategories():
        markup.add(c)
    msg = bot.reply_to(message, "Select Category", reply_markup=markup)
    bot.register_next_step_handler(msg, post_category_selection, bot, date_of_entry)

def post_category_selection(message, bot, date_of_entry):
    """
    post_category_selection(message, bot): It takes 2 arguments for processing -
    message which is the message from the user, and bot which is the telegram bot object
    from the run(message, bot): function in the add.py file. It requests the user to enter the amount
    they have spent on the expense category chosen and then passes control to
    post_amount_input(message, bot): for further processing.
    """
    try:
        chat_id = message.chat.id
        selected_category = message.text
        if selected_category == "Add new category":
            message1 = bot.send_message(chat_id, "Please enter your category")
            bot.register_next_step_handler(message1, post_append_spend, bot, date_of_entry)
        else:
            if selected_category not in helper.getSpendCategories():
                bot.send_message(
                    chat_id, "Invalid", reply_markup=types.ReplyKeyboardRemove()
                )
                raise Exception(
                    'Sorry, I don\'t recognise this category "{}"!'.format(selected_category)
                )
           # Prompt the user to choose a currency
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            markup.row_width = 2
            for currency in supported_currencies:
                markup.add(currency)
            
            msg = bot.reply_to(message, "Select Currency", reply_markup=markup)
            bot.register_next_step_handler(msg, post_currency_selection, bot, selected_category, date_of_entry)

    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oh no! " + str(e))
        display_text = ""
        commands = helper.getCommands()
        for c in commands:  
            # generate help text out of the commands dictionary defined at the top
            display_text += "/" + c + ": "
            display_text += commands[c] + "\n"
        bot.send_message(chat_id, "Please select a menu option from below:")
        bot.send_message(chat_id, display_text)

def post_currency_selection(message, bot, selected_category, date_of_entry):
    try:
        chat_id = message.chat.id
        selected_currency = message.text

        if selected_currency not in supported_currencies:
            bot.send_message(
                chat_id, "Invalid", reply_markup=types.ReplyKeyboardRemove()
            )
            raise Exception(
                'Sorry, I don\'t recognise this currency "{}"!'.format(selected_currency)
            )

        option[chat_id] = selected_category
        # Now, proceed with asking the user for the amount
        message = bot.send_message(
            chat_id, "How much did you spend on {} in {}? \n(Numeric values only)".format(str(option[chat_id]), selected_currency)
        )
        bot.register_next_step_handler(message, post_amount_input, bot, selected_category, selected_currency, date_of_entry)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oh no! " + str(e))
        display_text = ""
        commands = helper.getCommands()
        for c in commands:  
            # generate help text out of the commands dictionary defined at the top
            display_text += "/" + c + ": "
            display_text += commands[c] + "\n"
        bot.send_message(chat_id, "Please select a menu option from below:")
        bot.send_message(chat_id, display_text)

def record_expense(message, bot, previous_expenses, date_of_entry):
    print("In function to record expense")
    selection = message.text
    print(selection)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    if selection == "Y" or selection == "y":
        for record in previous_expenses:
            markup.add(record)
        msg = bot.reply_to(message, "Select the expense you want to repeat", reply_markup=markup)
        bot.register_next_step_handler(msg, post_expense_selection, bot, date_of_entry)
    else:
        for c in helper.getSpendCategories():
            markup.add(c)
        markup.add("Add new category")
        msg = bot.reply_to(message, "Select Category", reply_markup=markup)
        bot.register_next_step_handler(msg, post_category_selection, bot, date_of_entry)

def post_expense_selection(message,bot,date_of_entry):
    chat_id = message.chat.id
    expense_record = message.text
    expense_data = expense_record.split(",")
    amount = expense_data[2]
    category = expense_data[1]
    currency = expense_data[3]
    print(amount)
    amount_value = helper.validate_entered_amount(amount)  # validate
    try:
        if amount_value == 0:  # cannot be $0 spending
            raise Exception("Spent amount has to be a non-zero number.")
        date_str, category_str, amount_str = (
            str(date_of_entry),
            str(category),
            str(amount_value),
        )
        helper.write_json(
            add_user_record(
                chat_id, "{},{},{}".format(date_str, category_str, amount_str, currency)
            )
        )
        bot.send_message(
            chat_id,
            "The following expenditure has been recorded: You have spent {} {} for {} on {}".format(
                currency, amount_str, category_str, date_str
            ),
        )
        helper.display_remaining_budget(message, bot, category)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oh no. " + str(e))

def post_amount_input(message, bot, selected_category, selected_currency, date_of_entry):
    """
    post_amount_input(message, bot): It takes 2 arguments for processing -
    message which is the message from the user, and bot which is the telegram bot
    object from the post_category_selection(message, bot): function in the add.py file.
    It takes the amount entered by the user, validates it with helper.validate() and then
    calls add_user_record to store it.
    """
    try:
        print("---------------------------------------------------")
        chat_id = message.chat.id
        print(chat_id)
        amount_entered = message.text
        print("0000000000000000000000000000000000000000000000000")
        print(amount_entered)
        print(selected_category)
        amount_value = helper.validate_entered_amount(amount_entered)  # validate
        if amount_value == 0:  # cannot be $0 spending
            raise Exception("Spent amount has to be a non-zero number.")
        date_str, category_str, amount_str = (
            str(date_of_entry),
            str(option[chat_id]),
            str(amount_value),
        )
        helper.write_json(
            add_user_record(
                chat_id, "{},{},{},{}".format(date_str, category_str, amount_str, selected_currency)
            )
        )
        bot.send_message(
            chat_id,
            "The following expenditure has been recorded: You have spent {} {} for {} on {}".format(
                selected_currency,amount_str, category_str, date_str
            ),
        )
        # TODO: @Deepak Post adding expense metrics
        # helper.display_remaining_budget(message, bot, selected_category)
    except Exception as e:
        logging.exception(str(e))
        bot.reply_to(message, "Oh no. " + str(e))

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

    user_list[str(chat_id)]["data"].append(f"{record_to_be_added}")
    print("!" * 5)
    print("after")
    print(user_list)
    print("!" * 5)
    return user_list
