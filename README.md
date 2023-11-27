# 💰 Budget Bot 💰

<!-- TABLE OF CONTENTS -->
<b><h3>Table of Contents</h3></b>
  <ol>
    <li><a href="#whats-budgetbot">What's BudgetBot?
    <li><a href="#why-use-dollarbot">Why use BudgetBot?</a></li>
    <li><a href="#demo">Demo</a></li>
    <li><a href="#whats-new">What's new in this version?</a></li>
    <li><a href="#installation-and-setup">Installation and Setup</a></li>
   <li><a href="#how-to-use">How to use?</a></li>
   <li><a href="#contributors">Contributors</a></li>
   <li><a href="#future-work">Future Work</a></li>
   <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>

Are you a developer? <a href="https://github.com/deepr41/budget_bot/blob/main/Developer_ReadMe.md">Click here: For Developers and Future Contributors</a>

![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
[![Platform](https://img.shields.io/badge/Platform-Telegram-blue)](https://desktop.telegram.org/)
![GitHub](https://img.shields.io/badge/Language-Python-blue.svg)
[![GitHub contributors](https://img.shields.io/github/contributors/aditikilledar/dollar_bot_SE23)](https://github.com/deepr41/budget_bot/graphs/contributors)
[![DOI](https://zenodo.org/badge/691334031.svg)](https://zenodo.org/doi/10.5281/zenodo.10023639)
[![Build Status](https://app.travis-ci.com/usmanwardag/dollar_bot.svg?branch=main)](https://app.travis-ci.com/usmanwardag/dollar_bot)
[![codecov](https://codecov.io/gh/aditikilledar/dollar_bot_SE23/graph/badge.svg?token=23RW1XPB3P)](https://codecov.io/gh/aditikilledar/dollar_bot_SE23)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/aditikilledar/dollar_bot_SE23)](https://github.com/aditikilledar/dollar_bot_SE23/issues?q=is%3Aissue+is%3Aclosed)
<!-- [![GitHub closed issues](https://img.shields.io/github/issues-closed/sak007/MyDollarBot-BOTGo)](https://github.com/sak007/MyDollarBot-BOTGo/issues?q=is%3Aissue+is%3Aclosed) -->

<hr>

## What's BudgetBot?

BudgetBot is a handy little bot built on top of Telegram, to help you with daily expense tracking and analytics on your past spends. 

It's easy to setup, run and use on a daily basis!

<a href="https://www.canva.com/design/DAFxwU4ABIg/LqMkLeGUBhC__JmWmdkFiQ/watch?utm_content=DAFxwU4ABIg&utm_campaign=designshare&utm_medium=link&utm_source=editor">Click here for a video overview!!</a>

## Why use BudgetBot?

With simple in-chat commands, this bot helps you:
- Set your own customized budget
- Add/Record new spendings
- Add your income from different sources
- Add recurrant spendings
- Add your monthly savings
- Add your goals categorywise
- Display your spending trends through engaging graphs
- Predict your next month's budget based on your current expenditure
- Display your spending history
- Clear/Erase all your records
- Edit/Change any spending details if you wish to
- View Analytics and export as a pdf
- Use OpenAI tools for analysis and tips on expense management

## Demo

Demo Video -> [https://www.youtube.com/watch?v=XlndmRhr9Lc]

## What's new?

We've considerably extended this project to make using BudgetBot easy and engaging.
![alt text](https://github.com/deepr41/budget_bot/blob/main/docs/Enhancements.png)

Check [this documentation out](https://github.com/deepr41/budget_bot/blob/main/docs/whats-new.md) for an in-depth depiction of our changes. :)

## Installation and Setup

### Pre-requisite: The Telegram Desktop App

Since BudgetBot is built on top of Telegram, you'll first need:
1. Download the Telegram Desktop Application <a href="https://desktop.telegram.org/">here.</a>
```https://desktop.telegram.org/```
2. Create a Telegram account or Sign in.

Open up your terminal and let's get started:

### MacOS / Ubuntu Users

1. Clone this repository to your local system. 
```
   git clone https://github.com/deepr41/budget_bot/
```
2. Start a terminal session in the directory where the project has been cloned. Run the following commands and follow the instructions on-screen to complete the installation.
```
  chmod a+x setup.sh
  bash setup.sh
```
There, all done!

The installation is easy for MacOS or on UNIX terminals. 

### Windows

With Windows, you'll need to use a platform to execute UNIX-like commands in order to execute the setup.sh bash script. Once in the platform, use the steps in the MacOS/Unix Section above to setup BudgetBot.

We've used <a href="https://www.cygwin.com/">Cygwin,</a> but there are more options like WSL that you can explore.

Additionally, find more hints on Cygwin installation <a href="https://stackoverflow.com/questions/6413377/is-there-a-way-to-run-bash-scripts-on-windows">here.</a>

## Running BudgetBot:

Once you've executed setup.sh, and all dependencies have been installed, you can start running BudgetBot by following these instructions.

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

(b) execute the run.sh bash script to start BudgetBot
   
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
 3.The message will be prompted to notify the addition of your expense with the amount,date, time and category 

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

#### /income: This option is to provide income from different sources.

#### /Monthly savings: This option comes under budget type and lets you set a savings goal for a month.

#### / JANHAVI'S GOALS AND RECURRANT SPENDINGS INFORMARION NEEDS TO BE ADDED HERE ------ TODO 

## Contributors
<table>
  <tr>
    <td align="center"><a href="https://github.com/deepr41"><img src="https://avatars.githubusercontent.com/u/22258487?v=4" width="75px;" alt=""/><br /><sub><b>Deepak Rajendran</b></sub></a></td>
    <td align="center"><a href="https://github.com/shafa112"><img src="https://avatars.githubusercontent.com/u/39904345?v=4" width="75px;" alt=""/><br /><sub><b>Shafa Hassan</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Janhavi-23"><img src="https://avatars.githubusercontent.com/u/71866252?v=4" width="75px;" alt=""/><br /><sub><b> Janhavi Pendse</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/deepp2905"><img src="https://avatars.githubusercontent.com/u/62642211?v=4" width="75px;" alt=""/><br /><sub><b>Deep Patel</b></sub></a><br /></td>
  </tr>
</table>

## Future Work

- Sharing expenses
- Windows specific setup scripts
- Adding notes section while recording expenses
- Making BudgetBot respond to casual conversation like 'Hi' and 'Bye'
- Add budget items through OpenAI API

## Acknowledgements

- We would like to express our gratitude 🙏🏻 and a big thank you 😇 to Prof. Dr. Timothy Menzie for giving us the opportunity to get into the shoes of software building and learning new skills and development process throught the project building.
- A big thank you 😊 to the Teaching Assistants for their support.
- Thank you to the previous team 😊 for a thorough ReadMe and deatiled documentation.[MyDollarBot](https://github.com/sak007/MyDollarBot-BOTGo)
- Thank you to the ⭐️[Telegram bot](https://github.com/python-telegram-bot/python-telegram-bot)
