# About MyDollarBot's code.py file
code.py is the main file from where calls to the corresponding .py files for all features are sent. It contains a number of endpoints which redirect to function calls in the corresponding files. 

# Location of Code for this Feature
The code that implements this feature can be found [here](https://github.com/deepr41/budget_bot/blob/main/code/code.py)

# Code Description
## Functions

1. main()
The entire bot's execution begins here. It ensure the **bot** variable begins polling and actively listening for requests from telegram.

2. listener(user_requests):
Takes 1 argument **user_requests** and logs all user interaction with the bot including all bot commands run and any other issue logs.

3. faq(m):
Prints out the frequently asked questions for users to understand some common doubts. Commands used to run this: command=['faq']

4. help(m):
Provides a succinct list of commands the user can use. Command used to run this: command=['help']

5. start_and_menu_command(m):
Prints out the the main menu displaying the features that the bot offers and the corresponding commands to be run from the Telegram UI to use these features. Commands used to run this: commands=['start', 'menu']

6. command_add(message)
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls add.py to run the add functionality. Commands used to run this: command=['add']

7. command_history(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls history.py to execute the history functionality. Commands used to run this: command=['history']

8. command_pdf(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls pdf.py to run to execute the pdf functionality. Commands used to run this: command=['pdf']

9. command_analytics(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls analytics.py which leverages get_analysis.py and graphing.py to perform the analytics. Commands used to run this: command=['analytics']

10. command_edit(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls edit.py to run the edit functionality. Commands used to run this: command=['edit']

11. command_budget(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls budget.py to execute the budget functionality. Commands used to run this: command=['budget']

12. command_predict(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls predict.py to execute the predict functionality. Commands used to run this: command=['predict']

13. command_display(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls display.py to run to execute the add functionality. Commands used to run this: command=['display']

14. command_delete(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls delete.py to run to execute the add functionality. Commands used to run this: command=['delete']

15. command_income(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls income.py to run to execute the add functionality. Commands used to run this: command=['income']

16. command_savings(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls savings.py to run to execute the add functionality. Commands used to run this: command=['saving']

17. command_advisor(message):
Takes 1 argument **message** which contains the message from the user along with the chat ID of the user chat. It then calls advisor.py to run to execute the add functionality. Commands used to run this: command=['advisor']

18. monthly_recurrent_expense
It iterates through all recurrent payments stored and creates corresponsing expenses for them and this function is scheduled to run every 1st of the month

# How to run this feature?
This file contains information on the main code.py file from where all features are run. Instructions to run this are the same as instructions to run the project and can be found in README.md.
