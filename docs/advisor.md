# /advisor of BudgetBot
This documentation outlines the finance advisor functionality of the bot, detailing the actions available to users (Advice, Analyse, Tips) 
and the corresponding processes for each action. Additionally, it explains the interaction flow between the user and the AI model for
generating finance-related advice and tips.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/deepr41/budget_bot/tree/main/code)

# Code Description
## Functions

1. run(message, bot): Initiates the finance advisor bot and prompts the user to select an action (Advice, Analyse, Tips)
   
2.  post_advisor_type(message, bot): Processes the user's selected action and directs the flow accordingly

3.  post_advisor_category(message, bot): Prompts the user to select a specific finance advice category

4.  post_advisor_prompting(message, bot): Processes the user-selected finance advice category and requests additional information.
    It then generates an AI response based on the user's input.

5.  analyse_bot(message, bot): Initiates the financial analysis process by gathering user data and generating an AI analysis.

6.  tips_message(message, bot): Generates a finance-related tip using AI


# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /advisor into the telegram bot.
