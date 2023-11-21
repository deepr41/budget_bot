import helper
import logging
import budget_view
from telebot import types
from datetime import datetime
import add

# === Documentation of budget_update.py ===

def run(message, bot):
    """
    run(message, bot): This is the main function used to implement the budget add/update features.
    It takes 2 arguments for processing - message which is the message from the user, and bot which
    is the telegram bot object from the main code.py function.
    """
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    options = helper.getBudgetTypes()
    markup.row_width = 2
    for c in options.values():
        markup.add(c)
    msg = bot.reply_to(message, "Select Budget Type", reply_markup=markup)
    bot.register_next_step_handler(msg, post_type_selection, bot)

def post_type_selection(message, bot):
    """
    post_type_selection(message, bot): It takes 2 arguments for processing - message
    which is the message from the user, and bot which is the telegram bot object.
    This function takes input from the user, making them choose which type of budget they
    would like to create - category-wise or overall, and then calls the corresponding functions for further processing.
    """
    try:
        chat_id = message.chat.id
        op = message.text
        options = helper.getBudgetTypes()
        if op not in options.values():
            bot.send_message(
                chat_id, "Invalid", reply_markup=types.ReplyKeyboardRemove()
            )
            raise Exception('Sorry I don\'t recognise this operation "{}"!'.format(op))
        if op == options["overall"]:
            update_overall_budget(chat_id, bot)
        elif op == options["goal"]:
            update_category_budget(message, bot, "goal")
        elif op == options["recurrent"]:
            update_category_budget(message, bot, "recurrent")
    except Exception as e:
        helper.throw_exception(e, message, bot, logging)

def update_overall_budget(chat_id, bot):
    """
    update_overall_budget(message, bot): It takes 2 arguments for processing - message which is the
    message from the user, and bot which is the telegram bot object. This function is called when the
    user wants to either create a new overall budget or update an existing one. It checks if there is an
    existing budget through the helper module's isOverallBudgetAvailable function and if so, displays this
    along with the prompt for the new (to be updated) budget, or just asks for the new budget. It passes control
    to the post_overall_amount_input function in the same file.
    """
    val = helper.read_json()
    print("=======================")
    print(val)
    if helper.isOverallBudgetAvailable(chat_id):
        currentBudget = helper.getOverallBudget(chat_id)
        msg_string = "Current Budget is ${}\n\nHow much is your new monthly budget? \n(Enter numeric values only)"
        message = bot.send_message(chat_id, msg_string.format(currentBudget))
    else:
        message = bot.send_message(
            chat_id, "How much is your monthly budget? \n(Enter numeric values only)"
        )
    bot.register_next_step_handler(message, post_overall_amount_input, bot)

def post_overall_amount_input(message, bot):
    """
    update_overall_budget(message, bot): It takes 2 arguments for processing -
    message which is the message from the user, and bot which is the telegram bot object.
    This function is called when the user wants to either create a new overall budget or
    update an existing one. It checks if there is an existing budget through the helper module's
    isOverallBudgetAvailable function and if so, displays this along with the prompt for the new
    (to be updated) budget, or just asks for the new budget. It passes control to the post_overall_amount_input
    function in the same file.
    """
    try:
        chat_id = message.chat.id
        amount_value = helper.validate_entered_amount(message.text)
        if amount_value == 0:
            raise Exception("Invalid amount.")
        user_list = helper.read_json()
        if str(chat_id) not in user_list:
            user_list[str(chat_id)] = helper.createNewUserRecord()
        user_list[str(chat_id)]["budget"]["budget"] = amount_value
        total_budget = 0
        if helper.isCategoryBudgetAvailable(chat_id):
            for c in helper.getCategoryBudget(chat_id).values():
                total_budget += float(c)
            if total_budget > float(amount_value):
                raise Exception("Overall budget cannot be less than " + str(total_budget))
        # uncategorized_budget = helper.get_uncategorized_amount(chat_id, amount_value)
        # if float(uncategorized_budget) > 0:
        #     if user_list[str(chat_id)]["budget"]["goal"] is None:
        #         user_list[str(chat_id)]["budget"]["goal"] = {}
            # user_list[str(chat_id)]["budget"]["goal"]["uncategorized"] = uncategorized_budget
        helper.write_json(user_list)
        bot.send_message(chat_id, "Budget Updated!")
        budget_view.display_overall_budget(message, bot)
        print(user_list)
        return user_list
    except Exception as e:
        helper.throw_exception(e, message, bot, logging)


def update_category_budget(message, bot, op):
    """
    update_category_budget(message, bot): It takes 2 arguments for processing -
    message which is the message from the user, and bot which is the telegram bot object.
    This function is called in case the user decides to choose category-wise budgest in the run or
    post_type_selection stages. It gets the spend categories from the helper module's getSpendCategories
    and displays them to the user. It then passes control on to the post_category_selection function.
    """
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    categories = helper.getSpendCategories() if op == "goal" else helper.getRecurrentCategories()
    markup.row_width = 2
    for c in categories:
        markup.add(c)
    if op == "goal":
        markup.add("Add new goal")
        msg = bot.reply_to(message, "Select Goal", reply_markup=markup)
        bot.register_next_step_handler(msg, post_category_selection, bot)
    elif op == "recurrent":
        markup.add("Add new recurrent spending")
        msg = bot.reply_to(message, "Select Spending", reply_markup=markup)
        bot.register_next_step_handler(msg, add_recurrent_spendings, bot)


def post_category_selection(message, bot):
    """
    post_category_selection(message, bot): It takes 2 arguments for processing -
    message which is the message from the user, and bot which is the telegram bot object.
    Based on the category chosen by the user, the bot checks if these are part of the pre-defined
    categories in helper.getSpendCategories(), else it throws an exception. If there is a budget
    already existing for the category, it identifies this case through helper.isCategoryBudgetByCategoryAvailable
    and shares this information with the user. If not, it simply proceeds. In either case, it then asks for the
    new/updated budget amount. It passes control onto post_category_amount_input.
    """
    try:
        chat_id = message.chat.id
        if helper.getOverallBudget == '0':
            message = bot.send_message(
                    chat_id,
                    "No Budget Available",
                )
        else:
            selected_category = message.text
            if selected_category == "Add new goal":
                message1 = bot.send_message(chat_id, "Please enter your category")
                bot.register_next_step_handler(message1, add_new_category, bot)
            else:
                categories = helper.getSpendCategories()
                if selected_category not in categories:
                    bot.send_message(
                        chat_id, "Invalid", reply_markup=types.ReplyKeyboardRemove()
                    )
                    raise Exception(
                        'Sorry I don\'t recognise this category "{}"!'.format(selected_category)
                    )
                if helper.isCategoryBudgetByCategoryAvailable(chat_id, selected_category):
                    currentBudget = helper.getCategoryBudgetByCategory(
                        chat_id, selected_category
                    )
                    msg_string = "Current goal for {} is {}\n\nEnter goal for {}\n(Enter numeric values only)"
                    message = bot.send_message(
                        chat_id,
                        msg_string.format(selected_category, currentBudget, selected_category),
                    )
                else:
                    message = bot.send_message(
                        chat_id,
                        "Enter new goal amount for " + selected_category + "\n(Enter numeric values only)",
                    )
                bot.register_next_step_handler(
                    message, post_category_amount_input, bot, selected_category
                )
    except Exception as e:
        helper.throw_exception(e, message, bot, logging)

def add_new_category(message,bot):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    new_category = message.text
    helper.spend_categories.append(new_category)
    for c in helper.getSpendCategories():
        markup.add(c)
    msg = bot.reply_to(message, "Select Category", reply_markup=markup)
    bot.register_next_step_handler(msg, post_category_selection, bot)

def post_category_amount_input(message, bot, category):
    """
    post_category_amount_input(message, bot, category): It takes 2 arguments for
    processing - message which is the message from the user, and bot which is the telegram
    bot object, and the category chosen by the user.
    """
    try:
        chat_id = message.chat.id
        budget_currency = helper.getOverallCurrency(chat_id)
        amount_value = helper.validate_entered_amount(message.text)
        if amount_value == 0:
            raise Exception("Invalid amount.")
        user_list = helper.read_json()
        if str(chat_id) not in user_list:
            user_list[str(chat_id)] = helper.createNewUserRecord()
        user_list[str(chat_id)]["budget"]["goal"][category] = amount_value
        message = bot.send_message(
            chat_id, "Goal for " + category + f" is now: {budget_currency} " + amount_value
        )
        helper.write_json(user_list)
        post_category_add(message, bot, "goal")

    except Exception as e:
        helper.throw_exception(e, message, bot, logging)

def add_new_spending(message,bot):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    new_category = message.text
    helper.spend_categories.append(new_category)
    for c in helper.getRecurrentCategories():
        markup.add(c)
    msg = bot.reply_to(message, "Select Category", reply_markup=markup)
    bot.register_next_step_handler(msg, add_recurrent_spendings, bot)


def add_recurrent_spendings(message, bot):
    """
    """
    try:
        chat_id = message.chat.id   
        selected_category = message.text
        if selected_category == "Add new recurrent spending":
            message1 = bot.send_message(chat_id, "Please enter your category")
            bot.register_next_step_handler(message1, add_new_spending, bot)
        else:
            categories = helper.getRecurrentCategories()
            if selected_category not in categories:
                bot.send_message(
                    chat_id, "Invalid", reply_markup=types.ReplyKeyboardRemove()
                )
                raise Exception(
                    'Sorry I don\'t recognise this category "{}"!'.format(selected_category)
                )
            if helper.isRecurrentBudgetByCategoryAvailable(chat_id, selected_category):
                currentBudget = helper.getRecurrentBudgetByCategory(
                    chat_id, selected_category
                )
                msg_string = "Current recurrent spending for {} is {}\n\nEnter spending for {}\n(Enter numeric values only)"
                message = bot.send_message(
                    chat_id,
                    msg_string.format(selected_category, currentBudget, selected_category),
                )
            else:
                message = bot.send_message(
                    chat_id,
                    "Enter new recurrent spending amount for " + selected_category + "\n(Enter numeric values only)",
                )
            bot.register_next_step_handler(
                message, post_recurrent_amount_input, bot, selected_category
            )
    except Exception as e:
        helper.throw_exception(e, message, bot, logging)


def post_recurrent_amount_input(message, bot, category):
    """
    post_category_amount_input(message, bot, category): It takes 2 arguments for
    processing - message which is the message from the user, and bot which is the telegram
    bot object, and the category chosen by the user.
    """
    try:
        chat_id = message.chat.id
        budget_currency = helper.getOverallCurrency(chat_id)
        amount_value = helper.validate_entered_amount(message.text)
        if amount_value == 0:
            raise Exception("Invalid amount.")
        user_list = helper.read_json()
        if str(chat_id) not in user_list:
            user_list[str(chat_id)] = helper.createNewUserRecord()
        user_list[str(chat_id)]["budget"]["recurrent"][category] = amount_value
        message = bot.send_message(
            chat_id, "Recurrent amount for " + category + f" is now: {budget_currency} " + amount_value
        )
        helper.write_json(user_list)

        date_of_entry = datetime.today().strftime(helper.getDateFormat())

        date_str, category_str, amount_str = (
            str(date_of_entry),
            str(category),
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

        post_category_add(message, bot, "recurrent")

    except Exception as e:
        helper.throw_exception(e, message, bot, logging)


def post_category_add(message, bot, option):
    """
    post_category_add(message, bot): It takes 2 arguments for processing -
    message which is the message from the user, and bot which is the telegram bot object.
    This exists in case the user wants to add a category-wise budget to another category after adding
    it for one category. It prompts the user to choose an option from helper.getUpdateOptions().values() and
    passes control to post_option_selection to either continue or exit the add/update feature.
    """
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    options = helper.getUpdateOptions().values()
    markup.row_width = 2
    for c in options:
        markup.add(c)
    msg = bot.reply_to(message, "Select Option", reply_markup=markup)
    bot.register_next_step_handler(msg, post_option_selection, bot, option)

def post_option_selection(message, bot, option):
    """
    post_option_selection(message, bot): It takes 2 arguments for processing -
    message which is the message from the user, and bot which is the telegram bot object.
    It takes the category chosen by the user from the message object. If the message is "continue",
    then it runs update_category_budget (above) allowing the user to get into the add/update process again.
    Otherwise, it exits the feature.
    """
    print("here")
    selected_option = message.text
    options = helper.getUpdateOptions()
    print("here")
    if selected_option == options["continue"]:
        if option == "goal":
            update_category_budget(message, bot)
        elif option == "recurrent":
            add_recurrent_spendings(message, bot)