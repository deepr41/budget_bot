# /add Feature of BugetBot
This feature enables the user to add a new expense to their expense tracker.
User can also add old expense or repeat add in existing monthly expense.
Currently we have the following expense categories set by default:

- Food
- Groceries
- Utilities
- Transport
- Shopping
- Miscellaneous

The user has the flexibility to select a category and input the amount spent, which will then be saved in the expense tracker. 
Additionally, the user can opt to create a new category and log an expense under it. 
Furthermore, the user is empowered to replicate any expense recorded earlier, including recurring expenditures like rent and utilities.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/deepr41/budget_bot/blob/main/code/add.py)

# Code Description
## Functions

1. run(message, bot):
This serves as the primary function for executing the "add" feature. It provides the user with the choice to either replicate a previously logged expense, record a new one, or add a fresh expense. A menu is triggered on the bot interface, prompting the user to select their expense category. Subsequently, control is transferred to the "post_category_selection(message, bot)" function for additional processing. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function.

2. post_transaction_selection(message, bot, expense_history):
This function takes 3 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the run and **expense history** from run(message,bot) function in add.py file. Depending on the type of transaction user has selected, the control will then be transferred to new_expense(message, bot, date_of_entry) or old_expense(message, bot, date_of_entry) or record_expense(message, bot, expense_history, date_of_entry) for additional processing. As per the transaction type user is then prompted to selected the category through function post_category_selection(message, bot).

4. post_category_selection(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the run(message, bot): function in the add.py file. If the user wants to add a new category, passes control to post_append_spend(message,bot): to update the categories. Otherwise, it requests the user to enter the amount they have spent on the expense category chosen and then passes control to post_amount_input(message, bot): for further processing.

5. post_append_spend(message,bot):
This function adds the user defined category to the list of options available to record expenses, and then asks the user to pick the category for which they want to record an expense. The control passes back to post_category_selection(message, bot) once the user has selected the category to add an expense.

6. record_expense(message, bot, previous_expenses):
This function takes **previous expenses** as an argument, which is the list of previously recorded expenses that users can choose to repeat. After the user selects the expense they want to repeat, it calls post_expense_selection(message,bot): to update and store the information.

7. post_expense_selection(message,bot):
This function is called to record the previously recorded expense with the date updated to the current date.  

8. post_amount_input(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the post_category_selection(message, bot): function in the add.py file. It takes the amount entered by the user, validates it with helper.validate() and then calls add_user_record to store it.

9. add_user_record(chat_id, record_to_be_added):
 Takes 2 arguments - **chat_id** or the chat_id of the user's chat, and **record_to_be_added** which is the expense record to be added to the store. It then stores this expense record in the store.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /add into the telegram bot.
