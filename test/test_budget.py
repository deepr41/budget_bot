from mock import ANY
import mock
from mock.mock import patch
from telebot import types
from code import goal as budget


@patch("telebot.telebot")
def test_run(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.reply_to.return_value = True
    message = create_message("hello from test run!")
    budget.run(message, mc)
    assert mc.reply_to.called
    # assert mc.reply_to.called_with(ANY, "Select Operation", ANY)


@patch("telebot.telebot")
def test_post_operation_selection_failing_case(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True

    mocker.patch.object(budget, "helper")
    budget.helper.getBudgetOptions.return_value = {}

    message = create_message("hello from budget test run!")
    budget.post_operation_selection(message, mc)
    mc.send_message.assert_called_with(11, "Invalid", reply_markup=mock.ANY)


@patch("telebot.telebot")
def test_post_operation_selection_update_case(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True

    mocker.patch.object(budget, "budget_update")
    budget.budget_update.run.return_value = True

    mocker.patch.object(budget, "helper")
    budget.helper.getBudgetOptions.return_value = {
        "update": "Add/Update",
        "view": "View",
        "delete": "Delete",
    }

    message = create_message("Add/Update")
    budget.post_operation_selection(message, mc)
    assert budget.budget_update.run.called


@patch("telebot.telebot")
def test_post_operation_selection_view_case(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True

    mocker.patch.object(budget, "budget_view")
    budget.budget_view.run.return_value = True

    mocker.patch.object(budget, "helper")
    budget.helper.getBudgetOptions.return_value = {
        "update": "Add/Update",
        "view": "View",
        "delete": "Delete",
    }

    message = create_message("View")
    budget.post_operation_selection(message, mc)
    assert budget.budget_view.run.called


@patch("telebot.telebot")
def test_post_operation_selection_delete_case(mock_telebot, mocker):
    mc = mock_telebot.return_value
    mc.send_message.return_value = True

    mocker.patch.object(budget, "budget_delete")
    budget.budget_delete.run.return_value = True

    mocker.patch.object(budget, "helper")
    budget.helper.getBudgetOptions.return_value = {
        "update": "Add/Update",
        "view": "View",
        "delete": "Delete",
    }

    message = create_message("Delete")
    budget.post_operation_selection(message, mc)
    assert budget.budget_delete.run.called


def create_message(text):
    params = {"messagebody": text}
    chat = types.User(11, False, "test")
    message = types.Message(1, None, None, chat, "text", params, "")
    message.text = text
    return message
