# /savings of BudgetBot
This part of code allows users to add savings to their budget through this bot. It prompts users to enter a numerical savings amount, updates the budget and savings accordingly, and notifies the user of the successful budget update.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/deepr41/budget_bot/tree/main/code)

# Code Description
## Functions

1. run(message, bot): Initiates the process of adding savings for a user. 
    Displays the current budget and savings amounts and prompts the user to enter 
    the savings amount. The function registers the next step to post_overall_savings_input() 
    for further processing.
   
2. post_overall_savings_input(message, bot): Processes the user-inputted savings amount, 
    updates the overall budget and savings, and writes the changes to the user's record. 
    Handles exceptions if the savings amount exceeds the budget.

# How to run this feature?
