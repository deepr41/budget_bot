# /analytics Feature OF BudgetBot
This feature allows users to view graphical insights about their budgeting and expenses.

There are four types of graphs that can be viewed.
1. View split of the overall budget goal category-wise
2. View split of current spending category-wise
3. View the remaining budget category-wise
4. View a time-series plot of the spending history

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/deepr41/budget_bot/blob/main/code/analytics.py)

# Code Description
## Functions

1. run(message, bot):
This is the main function used to implement the analytics feature. It pop ups a menu on the bot asking the user to choose type of analysis to display after which control is given to post_operation_selection(message, bot) for further proccessing. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function.

2. post_operation_selection(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the run(message, bot): function in the analytics.py file. Depending on the action chosen by the user, it passes on control to the corresponding functions which are all located in different files.   

[Learn about the graph implementation here](https://github.com/deepr41/budget_bot/blob/main/docs/graphing.md)

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /analytics into the telegram bot.
