from behave import when, then

@when(u'I remove "Test Friend" from the friend list')
def step_when_remove_friend(context):
    context.friends_page.remove_friend("Test Friend", "test@example.com")

@then(u'I should not see "Test Friend" in the friends list')
def step_then_not_see_friend(context):
    assert not context.friends_page.is_friend_visible("Test Friend", "test@example.com"), "Test Friend is still visible"