import graphing
import helper
import logging
import os

# === Documentation of budget_view.py ===

def run(message, bot):
    """
    run(message, bot): This is the main function used to implement the budget feature.
    It takes 2 arguments for processing - message which is the message from the user, and bot which
    is the telegram bot object from the main code.py function. Depending on whether the user has configured
    an overall budget or a category-wise budget, this functions checks for either case using the helper
    module's isOverallBudgetAvailable and isCategoryBudgetAvailable functions and passes control on the
    respective functions(listed below). If there is no budget configured an exception is raised and the user
    is given a message indicating that there is no budget configured.
    """
    try:
        print("here")
        chat_id = message.chat.id
        if helper.isOverallBudgetAvailable(chat_id) or helper.isCategoryBudgetAvailable(chat_id):
            display_overall_budget(message, bot)
            display_category_budget(message, bot)
        else:
            raise Exception(
                "Budget does not exist. Use " + helper.getBudgetOptions()["update"] + " option to add/update the budget"
            )
    except Exception as e:
        helper.throw_exception(e, message, bot, logging)

def display_overall_budget(message, bot):
    """
    display_overall_budget(message, bot): It takes 2 arguments for processing -
    message which is the message from the user, and bot which is the telegram bot
    object from the run(message, bot): in the same file. It gets the budget for the
    user based on their chat ID using the helper module and returns the same through the bot to the Telegram UI.
    """
    chat_id = message.chat.id
    data, currency = helper.getOverallBudget(chat_id)
    bot.send_message(chat_id, f"Overall Budget: {currency} " + data)

def display_category_budget(message, bot):
    """
    display_category_budget(message, bot): It takes 2 arguments for processing -
    message which is the message from the user, and bot which is the telegram bot object
    from the run(message, bot): in the same file. It gets the category-wise budget for the
    user based on their chat ID using the helper module.It then processes it into a string
    format suitable for display, and returns the same through the bot to the Telegram UI.
    """
    chat_id = message.chat.id
    if helper.isCategoryBudgetAvailable(chat_id):
        data = helper.getCategoryBudget(chat_id)
        graphing.viewBudget(data)
        bot.send_photo(chat_id, photo=open("budget.png", "rb"))
        os.remove("budget.png")
    else:
        bot.send_message(chat_id, "You are yet to set your budget for different categories.")