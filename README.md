[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
![Issues Open](https://img.shields.io/github/issues/deepr41/budget_bot)
[![Issues Closed](https://img.shields.io/github/issues-closed/deepr41/budget_bot)](https://github.com/deepr41/budget_bot/)
![GitHub last commit](https://img.shields.io/github/last-commit/deepr41/budget_bot/:main)
![Lines of code](https://tokei.rs/b1/github/deepr41/wolfjobs)
[![Repo-size](https://img.shields.io/github/repo-size/deepr41/budget_bot)](https://github.com/deepr41/budget_bot/)
[![file_count](https://img.shields.io/github/directory-file-count/deepr41/budget_bot)](https://github.com/deepr41/budget_bot/)
[![language_count](https://img.shields.io/github/languages/count/deepr41/budget_bot)](https://github.com/deepr41/budget_bot/)
[![Downloads](https://img.shields.io/github/downloads/deepr41/budget_bot/total)](https://github.com/deepr41/budget_bot/)
[![Top Language](https://img.shields.io/github/languages/top/deepr41/budget_bot)](https://github.com/deepr41/budget_bot/)
[![Release](https://img.shields.io/github/v/release/deepr41/budget_bot)](https://gitHub.com/deepr41/budget_bot)
![Codecov](https://img.shields.io/codecov/c/gh/deepr41/budget_bot)

# 💲 Budget Bot 💲

<!--![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/deepr41/budget_bot/.github/workflows/python-app.yml)-->

<!-- TABLE OF CONTENTS -->
- [What is Budget Bot?](#what-is-budget-bot)
- [Why use Budget Bot?](#why-use-budget-bot)
- [Demo](#demo)
- [What's new in this version?](#whats-new)
- [Installation and Setup](#installation-and-setup)
- [How to use?](#how-to-use)
- [Contributors](#contributors)
- [Future Scope](#future-scope)
- [Acknowledgements](#acknowledgements)


## Are you a developer? 💻
<a href="https://github.com/deepr41/budget_bot/Developer_ReadMe.md">Detailed Documentation For Developers and Future Contributors</a>
<br></br>


## What is Budget Bot?

BudgetBot💲 is a user-friendly Telegram bot designed to simplify your budgeting process and help you manage your finances. <br>
With intuitive in-chat commands, BudgetBot allows you to effortlessly set and customize your budget, track expenses, add income from various sources, and even predict your next month's budget based on _current_ spending trends.
<br>
<br>
<a href="https://www.canva.com/design/DAFxwU4ABIg/LqMkLeGUBhC__JmWmdkFiQ/watch?utm_content=DAFxwU4ABIg&utm_campaign=designshare&utm_medium=link&utm_source=editor">Click here for a video overview!!</a>

## Why use Budget Bot?

- **Easy Budgeting💼:** Set and update your budget with simple commands tailored to your financial preferences
- **Expense Tracking 📅:** Record and categorize your expenses, providing a detailed summary of your spending history
- **Income Management💵:** Add income from different sources and monitor your financial inflow effortlessly
- **Graphical Analytics📈**: Visualize your spending trends through expressive graphs, gaining insights into your financial habits
- **Budget Prediction🔮:** Utilize the bot's analytical capabilities to predict your future budget, ensuring financial planning accuracy
- **PDF Reports📄:** Generate clear and informative PDF reports of your spending history and analytics for easy reference
- **Recurring Expenses🔁:** Seamlessly add recurring expenses to enhance the accuracy of your budgeting
- **Goal Setting🎯:** Set savings goals for specific categories, fostering a proactive approach to financial planning

## Demo

Demo Video -> [https://www.youtube.com/watch?v=XlndmRhr9Lc]

## What's new?

![Enhancements](https://github.com/deepr41/budget_bot/blob/main/docs/Enhancements.png)

We've considerably extended this project to make using Budget Bot easy and engaging.
- Expressive Graphs📊: Engaging visual representations of your financial data for better understanding.
- Budget Prediction🤑: Anticipate your budget for the upcoming month based on your current expenditure patterns.
- Clearer PDF Reports📈: Improved documentation with more detailed and informative PDF reports for effective analysis.
- Recurring Expenses🔁: Now you can effortlessly add recurring expenses, ensuring a more comprehensive budget.
- Enhanced Budget Creation🔄: Updated features for creating, updating, and deleting budgets, providing greater flexibility.
- Integrated OpenAI API🚀: Receive tips on efficient expense management and enhanced analysis from an AI Advisor.

Check [this documentation out](https://github.com/deepr41/budget_bot/blob/main/docs/whats-new.md) for an in-depth depiction of our changes. :)

## Installation and Setup

### Pre-requisite: The Telegram Desktop App

Since Budget Bot is built on top of Telegram, you'll first need:
1. Download the Telegram Desktop Application <a href="https://desktop.telegram.org/">```https://desktop.telegram.org/```</a>

2. Create a Telegram account or Sign in.

Open up your terminal and let's get started:

### MacOS / Ubuntu Users

1. Clone this repository to your local system. 
```
   git clone https://github.com/deepr41/budget_bot
```
2. Start a terminal session in the directory where the project has been cloned. Run the following commands and follow the instructions on-screen to complete the installation.
```
  chmod a+x setup.sh
  bash setup.sh
```
There, all done!

The installation is easy for MacOS or on UNIX terminals. 

### Windows

With Windows, you'll need to use a platform to execute UNIX-like commands in order to execute the setup.sh bash script. Once in the platform, use the steps in the MacOS/Unix Section above to setup Budget Bot.

We've used <a href="https://www.cygwin.com/">Cygwin,</a> but there are more options like WSL that you can explore.

Additionally, find more hints on Cygwin installation <a href="https://stackoverflow.com/questions/6413377/is-there-a-way-to-run-bash-scripts-on-windows">here.</a>

## Running Budget Bot:

Once you've executed setup.sh, and all dependencies have been installed, you can start running Budget Bot by following these instructions.

1. Open the Telegram Desktop Application and sign in. Once inside Telegram, search for "BotFather". Click on "Start", and enter the following command:
```
  /newbot
```
2. Follow the instructions on screen and choose a name for your bot (e.g., `budgetbot`). After this, select a UNIQUE username for your bot that ends with "bot", for example: `budgetbot_<your_nickname>`.

3. BotFather will now confirm the creation of your bot and provide a TOKEN to access the HTTP API - copy and save this token for future use. Make sure you save this token– don't lose it!

4. In the repo directory (where you cloned it), run these commands.

(a) grant execution access to a bash script
  ```
  chmod a+x run.sh
  ```

(b) execute the run.sh bash script to start Budget Bot
   
###### MacOS / Unix
```
   bash run.sh
```
###### Windows
```
   ./run.sh
```

```Note```: It will ask you to paste the API token you received from Telegram while creating your bot (Step 3), so keep that handy.
A successful run will generate a message on your terminal that says "TeleBot: Started polling." 

5. In the Telegram app, search for your newly created bot by entering your UNIQUE username and open the bot you created.

6. Now, on Telegram, enter the "/start" or "menu" command, and you are all set to track your expenses!

### Run Automatically at Startup

To run the script automatically at startup / reboot, simply add the `.run_forever.sh` script to your `.bashrc` file, which executes whenever you reboot your system.
<a href="https://stackoverflow.com/questions/49083789/how-to-add-new-line-in-bashrc-file-in-ubuntu">Click here for help adding to .bashrc files.</a>

## How to Use

Here's a quick overview of how each of the commands work. Simply enter /<command_name> into the Telegram chat and watch as the magic happens! 

#### /menu: Display commands with their descriptions.

#### /help: Display the list of commands.

#### /pdf: Save history as PDF.

#### /add: This option is for adding your expenses        
 1. It will give you the list of categories to choose from.        
 2. You will be prompted to enter the amount corresponding to your spending        
 3. The message will be prompted to notify the addition of your expense with the amount,date, time and category 

#### /analytics: This option gives user a graphical representation of their expenditures         
 You will get an option to choose the type of data you want to see.

#### /predict: This option analyzes your recorded spendings and gives you a budget that will accommodate for them.

#### /history: This option is to give you the detailed summary of your expenditure with Date, time ,category and amount. A quick lookup into your spendings

#### /delete: This option is to Clear/Erase all your records

#### /edit: This option helps you to go back and correct/update the missing details         
 1. It will give you the list of your expenses you wish to edit         
 2. It will let you change the specific field based on your requirements like amount/date/category

#### /budget: This option is to set/update/delete the budget.         
 1. The Add/update category is to set the new budget or update the existing budget         
 2. The view category gives the detail if budget is exceeding or in limit with the difference amount         
 3. The delete category allows to delete the budget and start afresh!

## Future Scope

- Sharing expenses
- Windows specific setup scripts
- Adding notes section while recording expenses
- Incorporating Machine Learning insights into the Analytics Feature
- Making Budget Bot respond to casual conversation like 'Hi' and 'Bye'

## Acknowledgements

- We extend our heartfelt gratitude to Prof. Dr. Timothy Menzie for affording us the invaluable opportunity to delve into the realm of software building, fostering new skills, and navigating the development process throughout the project.

- A warm and appreciative thank you is extended to the Teaching Assistants for their unwavering support.

- Our sincere thanks are also extended to the [previous team](https://github.com/aditikilledar/dollar_bot_SE23) for providing a comprehensive ReadMe and detailed documentation, which has proven instrumental in our understanding and progress 😊.

- Lastly, a special acknowledgment goes to the Telegram bot, accessible at [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot), for its major contribution to our project.

## Contributors

  <table>
  <tr>
    <td align="center"><a href="https://github.com/deepr41"><img src="https://avatars.githubusercontent.com/deepr41" width="100px;" alt=""/><br /><b>Deepak Rajendran</b></a></td>
    <td align="center"><a href="https://github.com/shafa112"><img src="https://avatars.githubusercontent.com/shafa112" width="100px;" alt=""/><br /><b>Shafa Hassan</b></a><br /></td>
    <td align="center"><a href="https://github.com/Janhavi-23"><img src="https://avatars.githubusercontent.com/Janhavi-23" width="100px;" alt=""/><br /><b>Janhavi Pendse</b></a><br /></td>
    <td align="center"><a href="https://github.com/deepp2905"><img src="https://avatars.githubusercontent.com/deepp2905" width="100px;" alt=""/><br /><b>Deep Patel</b></a><br /></td>
  </tr>
</table>

