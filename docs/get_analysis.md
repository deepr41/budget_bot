# /Get-Analysis of BudgetBot
This code section defines functions for visualizing and displaying financial insights to Telegram bot users, including overall budget distribution, 
spending breakdown by category, remaining budget percentages, and a time series of spending history. It utilizes the helper and graphing modules 
to extract and graph relevant data, providing users with informative visual summaries of their financial activity.
The user can choose a category and add the amount for the budget to be stored in the expense tracker.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/deepr41/budget_bot/tree/main/code)

# Code Description
## Functions

1. viewOverallBudget(chat_id, bot):
   This function displays an overall split of the budget
    across different spending categories for a user. It retrieves the category budgets using
    helper.getCategoryBudget(chat_id) and iterates through each category to obtain the individual
    budget values. The graphing.overall_split() function is then called to visualize this data,
    and the resulting graph is sent to the user through the Telegram bot.
   
2.  viewSpendWise(chat_id, bot): This function displays a breakdown of spending across different categories
    for a user. It retrieves the user's expense data using helper.getUserData(chat_id), extracts the category
    and amount information, and calculates the total spending for each category. The graphing.spend_wise_split()
    function is then called to visualize this data, and the resulting graph is sent to the user through the Telegram bot.

3. viewRemaining(chat_id, bot): This function displays the remaining budget percentage for each spending
    category based on the user's defined category budgets. It iterates through the predefined spending
    categories and calculates the remaining budget percentage using helper.calculateRemainingCateogryBudgetPercent().
    The graphing.remaining() function is then called to visualize this data, and the resulting graph is sent
    to the user through the Telegram bot.
   
5. viewHistory(chat_id, bot): This function displays a time series graph of the user's spending history.
    It retrieves the user's spending data using helper.getUserHistoryDateExpense(chat_id) and creates a
    dictionary mapping dates to total expenses for each date. The graphing.time_series() function is then
    called to visualize this data, and the resulting graph is sent to the user through the Telegram bot. 

# How to run this feature?

