# About MyDollarBot's budget_view module
The budget_view module contains all the functions required to implement the display budget feature. In essence, all operations involved in displaying a budget are taken care of in this module and are implemented here. 

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/deep41/budget_bot/blob/main/code/budget_view.py)

# Code Description
## Functions

1. run(message, bot):
This is the main function used to implement the budget feature. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function. Depending on whether the user has configured an overall budget or a category-wise budget, this functions checks for either case using the helper module's isOverallBudgetAvailable and isCategoryBudgetAvailable functions and passes control on the respective functions(listed below). If there is no budget configured an exception is raised and the user is given a message indicating that there is no budget configured.

2. display_overall_budget(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the run(message, bot): in the same file. It gets the budget for the user based on their chat ID using the helper module and returns the same through the bot to the Telegram UI.

3. display_category_budget(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the run(message, bot): in the same file. It gets the category-wise budget for the user based on their chat ID using the helper module.It then processes it into a string format suitable for display, and returns the same through the bot to the Telegram UI.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /budget into the telegram bot. Create a budget, and then type /budget again, and choose the option to view your budget.
