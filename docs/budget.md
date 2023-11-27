# /budget Feature of BudgetBot
This functionality allows users to add/update, delete, or view a budget within their expense tracker. Users can opt for an all-encompassing expense tracker, which tallies every expenditure against the budget. Alternatively, they can select a category-specific expense tracker, which only considers expenses within a designated category for that category's budget. Users also have the option to allocate a recurring amount for fixed monthly expenditures or contribute to monthly savings they wish to set aside.

The user can choose a category and add the amount for the budget to be stored in the expense tracker.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/deepr41/budget_bot/tree/main/code)

# Code Description
## Functions

1. run(message, bot):
This serves as the primary function for executing the budget functionality. It triggers a menu on the bot interface, prompting the user to select options such as adding, deleting, or displaying a budget. Following this, control is handed over to the post_operation_selection(message, bot) function for additional processing. It requires two parameters for processing: message, representing the user's message, and bot, which is the Telegram bot object derived from the main code.py function.

2. post_operation_selection(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the run(message, bot): function in the budget.py file. Depending on the action chosen by the user, it passes on control to the corresponding functions which are all located in different files such as budget_view.py, budget_update.py, budget_delete.py


# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /budget into the telegram bot.
