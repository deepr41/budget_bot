# About MyDollarBot's /delete Feature
This feature enables the user to delete all of their saved records till date in their expense tracker.

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/deepr41/budget_bot/blob/main/code/delete.py)

# Code Description
## Functions

1. run(message, bot):
This is the main function used to implement the delete feature. It takes 2 arguments for processing - **message** which is the message from the user, and **bot** which is the telegram bot object from the main code.py function. It calls helper to get the user history i.e chat ids of all user in the application, and if the user requesting a delete has their data saved in myDollarBot i.e their chat ID has been logged before, run calls the deleteHistory(chat_id): to remove it. Then it ensures this removal is saved in the datastore.

2. deleteHistory(chat_id):
It takes 1 argument for processing - **chat_id** which is the chat_id of the user whose data is to deleted from the user list. It removes this entry from the user list.

# How to run this feature?
Once the project is running(please follow the instructions given in the main README.md for this), please type /add into the telegram bot.
