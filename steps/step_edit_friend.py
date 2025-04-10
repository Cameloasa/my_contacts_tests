from behave import given, when, then


@when(u'I edit "Test Friend" to have name "{new_name}" and email "{new_email}"')
def step_when_edit_friend(context,new_name, new_email):
    context.friends_page.edit_friend("Test Friend",new_name,new_email)


@then(u'I should only see "Test Friend" if "{new_name}" is "Test Friend"')
def step_then_conditional_friend(context, new_name):
    if new_name == "Test Friend":
        assert context.friends_page.is_friend_visible("Test Friend"), "Test Friend should be visible"
    else:
        assert not context.friends_page.is_friend_visible("Test Friend"), "Test Friend should not be visible"

