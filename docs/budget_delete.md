# About BudgetBot's budget_delete module
The budget_delete module incorporates the functionality to remove an existing budget entered by the user. It essentially resets all the factors associated with the budget to their initial empty values. In summary, this module manages and implements all the operations related to the removal and deletion of a budget.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/deepr41/budget_bot/blob/main/code/budget_delete.py)

# Code Description
## Functions

1. run(message, bot):
This serves as the primary function for executing the budget deletion feature. It requires two arguments for processing: message, representing the user's message, and bot, the Telegram bot object from the main code.py function. The function extracts the user's chat ID from the message object and retrieves all user data using the read_json method from the helper module. Subsequently, it proceeds to clear the budget data for the specific user, based on the provided user ID from the UI. The function then returns a straightforward message indicating the completion of this operation to the UI.


# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /budget into the telegram bot. Add a budget and then type /budget again. Please choose the option for deleting a budget.
