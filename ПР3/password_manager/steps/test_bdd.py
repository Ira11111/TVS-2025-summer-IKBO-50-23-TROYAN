import os
import sys
from behave import given, when, then

# Добавляем родительскую директорию в Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pass_manager import PasswordManager


@given('Пароль для сервиса "{service}" с именем пользователя "{username}" еще не сохранен')
def step_clean_state(context, service, username):
    context.pm = PasswordManager('test_bdd_passwords.enc')
    # Убедимся, что пароль не существует
    try:
        context.pm.delete_password(service, username)
    except:
        pass


@given('Пароль "{password}" сохранен для сервиса "{service}" и пользователя "{username}"')
def step_save_initial_password(context, password, service, username):
    context.pm = PasswordManager('test_bdd_passwords.enc')
    context.pm.save_password(service, username, password)


@when('Я сохраняю пароль "{password}" для сервиса "{service}" и пользователя "{username}"')
def step_save_password(context, password, service, username):
    context.save_result = context.pm.save_password(service, username, password)


@when('Я запрашиваю пароль для сервиса "{service}" и пользователя "{username}"')
def step_get_password(context, service, username):
    try:
        context.retrieved_password = context.pm.get_password(service, username)
        context.password_error = None
    except Exception as e:
        context.password_error = str(e)
        context.retrieved_password = None


@when('Я обновляю пароль на "{new_password}" для сервиса "{service}" и пользователя "{username}"')
def step_update_password(context, new_password, service, username):
    context.update_result = context.pm.update_password(service, username, new_password)


@when('Я удаляю пароль для сервиса "{service}" и пользователя "{username}"')
def step_delete_password(context, service, username):
    context.delete_result = context.pm.delete_password(service, username)


@then('Пароль должен быть успешно сохранен')
def step_check_save_success(context):
    assert context.save_result is True


@then('Я должен получить пароль "{expected_password}"')
def step_check_retrieved_password(context, expected_password):
    assert context.retrieved_password == expected_password


@then('Пароль должен быть успешно обновлен')
def step_check_update_success(context):
    assert context.update_result is True


@then('Пароль должен быть успешно удален')
def step_check_delete_success(context):
    assert context.delete_result is True


@then('Я должен получить ошибку "{expected_error}"')
def step_check_error(context, expected_error):
    assert context.password_error is not None
    assert expected_error in context.password_error
