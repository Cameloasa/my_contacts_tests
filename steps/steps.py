from behave import given, when, then
from pages.friends_page import FriendsPage

# Add Friend
@given(u'I am on the Mina Vänner main page')
def step_given_main_page(context):
    context.page.goto(context.base_urls["main"])
    context.friends_page = FriendsPage(context.page)
    assert "my-contacts" in context.page.url

@when(u'I click "Ny Vän" and add "{name}" with email "{email}"')
def step_when_add_friend(context, name, email):
    context.friends_page.click_new_friend()
    context.friends_page.fill_name(name)
    context.friends_page.fill_email(email)

@when(u'I try to save the friend')
def step_when_try_to_save(context):
    try:
        context.friends_page.click_save()
    except ValueError as e:
        context.error_message = str(e)

# Edit Friend
@when(u'I edit "Test Friend" to have name "{new_name}" and email "{new_email}"')
def step_when_edit_friend(context, new_name, new_email):
    context.friends_page.edit_friend("Test Friend", new_name, new_email)

# Remove Friend
@when(u'I remove "Test Friend" from the friend list')
def step_when_remove_friend(context):
    context.friends_page.remove_friend("Test Friend", "test@example.com")

# Common Steps
@when(u'I go to "Vänlista"')
def step_when_go_to_friend_list(context):
    context.friends_page.go_to_friend_list()

@then(u'I should see "{name}" with email "{email}" in the friends list')
def step_then_see_friend(context, name, email):
    assert context.friends_page.is_friend_visible(name, email), f"{name} with {email} not found"

@then(u'I should not see "Test Friend" in the friends list')
def step_then_not_see_friend(context):
    assert not context.friends_page.is_friend_visible("Test Friend", "test@example.com"), "Test Friend is still visible"

@then(u'I should only see "Test Friend" if "{new_name}" is "Test Friend"')
def step_then_conditional_friend(context, new_name):
    if new_name == "Test Friend":
        assert context.friends_page.is_friend_visible("Test Friend"), "Test Friend should be visible"
    else:
        assert not context.friends_page.is_friend_visible("Test Friend"), "Test Friend should not be visible"

@then(u'I should see the error message "Fyll i båda fälten för att lägga till din vän."')
def step_then_see_error_message(context):
    error_message = context.page.locator("p.error").inner_text()
    expected_message = "Fyll i båda fälten för att lägga till din vän."
    assert error_message == expected_message, f"Expected '{expected_message}', but got '{error_message}'"

# Search
@when(u'I search for "{search_term}"')
def step_when_search_friend(context,search_term):
    context.friends_page.search_friend(search_term)


