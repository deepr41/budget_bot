# About MyDollarBot's budget_view module
The budget_view module contains all the functions required to implement the display add and update features. In essence, all operations involved in addition of a new budget and updating an existing budget are taken care of in this module and are implemented here. 

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/deepr41/budget_bot/blob/main/code/budget_update.py)

# Code Description
## Functions

1. run(message, bot):
This is the main function used to implement the budget add/update features. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function. 

Depending on whether the user has configured an overall budget or a category-wise budget, this functions checks for either case using the helper module's isOverallBudgetAvailable and isCategoryBudgetAvailable functions and passes control on the respective functions(listed below). If there is no budget configured, the function provides prompts to nudge the user to create a new budget depending on their preferences, through the post_type_selection function in the same module.

2. post_type_selection(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object. This function takes input from the user, making them choose which type of budget they would like to create - category-wise or overall, and then calls the corresponding functions for further processing.

3. update_overall_budget(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object. This function is called when the user wants to either create a new overall budget or update an existing one. 
It checks if there is an existing budget through the helper module's isOverallBudgetAvailable function and if so, displays this along with the prompt for the new (to be updated) budget, or just asks for the new budget. It passes control to the  post_overall_amount_input function in the same file.

4. post_overall_amount_input(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot . This function takes over from the update_overall_budget, and asks the user to enter the new/updated budget amount. 
As long as this amount is not zero(in which case it throws an exception), it continues processing. It reads the current user data through helper module's read_json function and adds the new budget information onto it, writing back with the helper module's write_json function. 

5. update_category_budget(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object. This function is called in case the user decides to choose category-wise budgest in the run or post_type_selection stages. 
It gets the spend categories from the helper module's getSpendCategories and displays them to the user. It then passes control on to the post_category_selection function.

6. post_category_selection(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object. Based on the category chosen by the user, the bot checks if these are part of the pre-defined categories in helper.getSpendCategories(), else it throws an exception. 
If there is a budget already existing for the category, it identifies this case through helper.isCategoryBudgetByCategoryAvailable and shares this information with the user. If not, it simply proceeds. In either case, it then asks for the new/updated budget amount. It passes control onto post_category_amount_input.

7. post_category_amount_input(message, bot, category):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object, and the category chosen by the user. 

It gets the amount entered by the user and validates it. As long as this amount is not zero(in which case it throws an exception), it continues processing. It reads the current user data through helper module's read_json function and adds the new budget information onto it, writing back with the helper module's write_json function. It passes control to post_category_add.

8. post_category_add(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object. This exists in case the user wants to add a category-wise budget to another category after adding it for one category. It prompts the user to choose an option from  helper.getUpdateOptions().values() and passes control to post_option_selection to either continue or exit the add/update feature.

9. post_option_selection(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object.
It takes the category chosen by the user from the message object. If the message is "continue", then it runs update_category_budget (above) allowing the user to get into the add/update process again.
Otherwise, it exits the feature.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /budget into the telegram bot. Please follow the prompts on the screen to create a new budget.
