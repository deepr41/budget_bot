# About MyDollarBot's /helper class
The helper file contains a set of functions that are commonly used for repeated tasks in the various features of MyDollarBot. Since these come up often, we have put them all up here in a separate file for reusability.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/deepr41/budget_bot/blob/main/code/helper.py)

# Code Description
## Functions

1. read_json():
Function to load .json expense record data

2. write_json(user_list):
Stores data into the datastore of the bot.

3. validate_entered_amount(amount_entered):
Takes 1 argument, **amount_entered**. It validates this amount's format to see if it has been correctly entered by the user.

4. getUserHistory(chat_id):
Takes 1 argument **chat_id** and uses this to get the relevant user's historical data.

4. getUserHistoryByCategory(chat_id,category):
Takes 2 arguments **chat_id** and **category** and returns the expenses from a specific category for a given chat id.

5. getUserData(chat_id):
This function gives all the data related to a user from the chat_id. Includes budgets and expenses.

6. throw_exception(e, message, bot, logging):
Used for error handling in bot code. Throws exception if any is thrown by another part of code.

7. createNewUserRecord():
Creates a new record for a newly registered user

8. getOverallBudget(chatId):
Returns overall budget value for given user

9. getCategoryBudget(chatId):
Returns category-wise budget split for given user

10. getCategoryBudgetByCategory(chatId, cat):
Returns specific category's budget allocation

11. isOverallBudgetAvailable(chatId):
Checks whether overall budget is initialized or not

12. isCategoryBudgetAvailable(chatId):
Checks whether category wise budget is initialized or not

13. isCategoryBudgetByCategoryAvailable(chatId, cat):
Checks whether specified category's budget is initialized or not

14. get_uncategorized_amount(chatId, amount):
Calculates the portion of the budget that is not assigned to any specific category

15. display_remaining_budget(message, bot, cat):
Displays remaining budget

16. display_remaining_overall_budget(message, bot):
Displays overall budget after recorded expenses

17. calculateRemainingOverallBudget(chat_id):
Calculate remaining overall budget after recorded expenses

18. calculate_total_spendings(queryResult):
Calculate total spendings of the user

19. display_remaining_category_budget(message, bot, cat):
Display remaining category budget for a specific category

20. calculateRemainingCategoryBudget(chat_id, cat):
Calculate remaining category budget after recorded expenses in the specific category

21. calculateRemainingCateogryBudgetPercent(chat_id, cat):
Calculate percentage of spent money on a particular category against its budget.

22. calculate_total_spendings_for_category(queryResult, cat):
Calculate total spending of the user within a specific category

23. updateBudgetCategory(chatId, category):
initializes the specific budget category 

24. getAvailableCategories(history):
Get available categories from history data

25. getCategoryWiseSpendings(available_categories, history):
Get category wise spending details

26. getFormattedPredictions(category_predictions):
Format predictions into readable format from dictionary into string in order to send message to the user.

27. getSpendCategories():
This functions returns the spend categories used in the bot. These are defined the same file.

28. getSpendDisplayOptions():
This functions returns the spend display options used in the bot. These are defined the same file.

29. getCommands():
This functions returns the command options used in the bot. These are defined the same file.

30. def getDateFormat():
This functions returns the date format used in the bot. 

31. def getTimeFormat():
This functions returns the time format used in the bot. 

32. def getMonthFormat():
This functions returns the month format used in the bot. 

33. getBudgetOptions():
This function returns the budget options used by the bot. These are defined in the same file.

34. getBudgetTypes():
This function returns the types of budgets that can be set up by users. These are defined in the same file.

35. getUpdateOptions():
This function returns the update options used by the bot. These are defined in the same file.

36. getAnalyticsOptions():
This function returns the analytics options used by the bot. These are defined in the same file.

# How to run this feature?
This file is not a feature and cannot be run per se. Its functions are used all over by the other files as it provides helper functions for various functionalities and features.
