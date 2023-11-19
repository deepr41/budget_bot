import helper
import logging
import budget_view
from telebot import types

# === Documentation of budget_update.py ===
default_currency = "$"
supported_currencies = [default_currency, "Rs", "Pounds", "Dirham"]

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
            update_overall_budget(message, chat_id, bot)
        elif op == options["category"]:
            update_category_budget(message, bot)
    except Exception as e:
        helper.throw_exception(e, message, bot, logging)

def update_overall_budget(message, chat_id, bot):
    """
    update_overall_budget(message, bot): It takes 2 arguments for processing - message which is the
    message from the user, and bot which is the telegram bot object. This function is called when the
    user wants to either create a new overall budget or update an existing one. It checks if there is an
    existing budget through the helper module's isOverallBudgetAvailable function and if so, displays this
    along with the prompt for the new (to be updated) budget, or just asks for the new budget. It passes control
    to the post_overall_amount_input function in the same file.
    """
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.row_width = 2
    for currency in supported_currencies:
        markup.add(currency)

    if helper.isOverallBudgetAvailable(chat_id):
        currentBudget = helper.getOverallBudget(chat_id)
        msg_string = "Current Budget is ${}\n\nHow much is your new monthly budget? \n(Enter numeric values only)"
        message = bot.send_message(chat_id, msg_string.format(currentBudget))
    else:
        message = bot.reply_to(message, "Select Currency", reply_markup=markup)
        
    bot.register_next_step_handler(message, post_budget_currency_selection, bot)

def post_budget_currency_selection(message, bot):
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

        # Now, proceed with asking the user for the amount
        message = bot.send_message(
            chat_id, "How much is your monthly budget? \n(Enter numeric values only)"
        )
        bot.register_next_step_handler(message, post_overall_amount_input, bot, selected_currency)
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

def post_overall_amount_input(message, bot, selected_currency):
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
        user_list[str(chat_id)]["budget"]["overall"] = amount_value
        total_budget = 0
        if helper.isCategoryBudgetAvailable(chat_id):
            for c in helper.getCategoryBudget(chat_id).values():
                total_budget += float(c)
            if total_budget > float(amount_value):
                raise Exception("Overall budget cannot be less than " + str(total_budget))
        uncategorized_budget = helper.get_uncategorized_amount(chat_id, amount_value)
        if float(uncategorized_budget) > 0:
            if user_list[str(chat_id)]["budget"]["category"] is None:
                user_list[str(chat_id)]["budget"]["category"] = {}
            user_list[str(chat_id)]["budget"]["category"]["uncategorized"] = uncategorized_budget
        helper.write_json(user_list)
        bot.send_message(chat_id, "Budget Updated!")
        budget_view.display_overall_budget(message, bot, selected_currency)
        print(user_list)
        return user_list
    except Exception as e:
        helper.throw_exception(e, message, bot, logging)


def update_category_budget(message, bot):
    """
    update_category_budget(message, bot): It takes 2 arguments for processing -
    message which is the message from the user, and bot which is the telegram bot object.
    This function is called in case the user decides to choose category-wise budgest in the run or
    post_type_selection stages. It gets the spend categories from the helper module's getSpendCategories
    and displays them to the user. It then passes control on to the post_category_selection function.
    """
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    categories = helper.getSpendCategories()
    markup.row_width = 2
    for c in categories:
        markup.add(c)
    markup.add("Add new category")
    msg = bot.reply_to(message, "Select Category", reply_markup=markup)
    bot.register_next_step_handler(msg, post_category_selection, bot)


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
        selected_category = message.text
        if selected_category == "Add new category":
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
                msg_string = "Current monthly budget for {} is {}\n\nEnter monthly budget for {}\n(Enter numeric values only)"
                message = bot.send_message(
                    chat_id,
                    msg_string.format(selected_category, currentBudget, selected_category),
                )
            else:
                message = bot.send_message(
                    chat_id,
                    "Enter monthly budget for " + selected_category + "\n(Enter numeric values only)",
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
        amount_value = helper.validate_entered_amount(message.text)
        if amount_value == 0:
            raise Exception("Invalid amount.")
        user_list = helper.read_json()
        if str(chat_id) not in user_list:
            user_list[str(chat_id)] = helper.createNewUserRecord()
        if user_list[str(chat_id)]["budget"]["category"] is None:
            user_list[str(chat_id)]["budget"]["category"] = {}
        user_list[str(chat_id)]["budget"]["category"][category] = amount_value
        message = bot.send_message(
            chat_id, "Budget for " + category + " is now: $" + amount_value
        )
        if helper.isCategoryBudgetByCategoryAvailable(chat_id, category):
                currentBudget = helper.getCategoryBudgetByCategory(chat_id, category)
                amount_value = str(float(amount_value) - float(currentBudget))
        if(user_list[str(chat_id)]["budget"]["overall"]) and user_list[str(chat_id)]["budget"]["overall"] != '0':
            if 'uncategorized' in user_list[str(chat_id)]["budget"]["category"].keys():
                if round(float(user_list[str(chat_id)]["budget"]["category"]["uncategorized"]) - float(amount_value),2) > 0:
                    user_list[str(chat_id)]["budget"]["category"]["uncategorized"] = str(round(float(user_list[str(chat_id)]["budget"]["category"]["uncategorized"]) - float(amount_value),2))
                else:
                    user_list[str(chat_id)]["budget"]["category"]["uncategorized"] = str(0)
            helper.write_json(user_list)
            total_budget = 0
            for c in helper.getCategoryBudget(chat_id).values():
                total_budget += float(c)
            print(total_budget)
            user_list[str(chat_id)]["budget"]["overall"] = str(total_budget)
        else:
            user_list[str(chat_id)]["budget"]["overall"] = amount_value
        helper.write_json(user_list)
        budget_view.display_overall_budget(message, bot)
        print(user_list)
        post_category_add(message, bot)

    except Exception as e:
        helper.throw_exception(e, message, bot, logging)


def post_category_add(message, bot):
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
    bot.register_next_step_handler(msg, post_option_selection, bot)

def post_option_selection(message, bot):
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
        update_category_budget(message, bot)