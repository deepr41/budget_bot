# About MyDollarBot's /estimate Feature
This feature enables the user to estimate their expenses for the next month or next day. The option to choose next month or next day pops up on the screen and they can choose their preference to be displayed.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/aditikilledar/dollar_bot_SE23/blob/main/code/estimate.py)

# Code Description
## Functions

1. run(message, bot):
This is the main function used to implement the estimate feature. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function. 

It gets the options for the estimate period from the helper.py file's getSpendEstimateOptions() method and then makes the Telegram bot display them for the user to choose along with a message indicating this. It then passes control to the estimate_total() function for further processing.

2. estimate_total(message, bot):
It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the  run(message, bot): function in the same file. This function loads the user's data using the helper file's getUserHistory(chat_id) method. After this, depending on the option user has chosen on the UI, it calls the  calculate_estimate(queryResult, days_to_estimate): to process the queried data to return to the user after which it finally passes the data to the UI for the user to view.

3. calculate_estimate(queryResult, days_to_estimate):
Takes 2 arguments for processing - **queryResult** which is the query result from the estimate total function in the same file. It parses the query result and turns it into a form suitable for display on the UI by the user. **days_to_estimate** is a variable that tells the function to calculate the estimate for a specified period like a day or month.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /estimate into the telegram bot.

