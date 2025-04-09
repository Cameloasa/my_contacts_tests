from behave import given, when, then
from pages.friends_page import click_new_friend, fill_name, fill_email, click_save, go_to_friend_list


@given(u'I am on the Mina Vänner main page')
def step_given_main_page(context):
    context.page.goto(context.base_urls["main"])
    assert "my-contacts" in context.page.url, "Not on Mina Vänner main page"

@when(u'I click "Ny Vän" and add "{name}" with email "{email}"')
def step_when_add_friend(context,name,email):
    # Click on "Ny Vän" să open the form
    click_new_friend(context.page)
    # Fill input Namn and E-post
    fill_name(context.page, name) # input: Namn
    fill_email(context.page, email) #input: E-post

@when(u'I try to save the friend')
def step_when_try_to_save(context):
    try:
        click_save(context.page)
    except ValueError as e:
        context.error_message = str(e)

@then(u'I should see the error message "Fyll i båda fälten för att lägga till din vän"')
def step_then_see_error_message(context):
    error_message = context.page.locator("p.error").inner_text()
    expected_message = "Fyll i båda fälten för att lägga till din vän."
    print(f"Got: '{error_message}'")
    print(f"Expected: '{expected_message}'")
    assert error_message == expected_message, f"Expected '{expected_message}', but got '{error_message}'"

@when(u'I go to "Vänlista"')
def step_when_go_to_friend_list(context):
    #Click button "Vänlista"
    go_to_friend_list(context.page)

@then(u'I should see "{name}" in the friends list')
def step_then_see_friend_in_list(context,name):
    assert context.page.get_by_text(name, exact= True).is_visible(), "Ana not found in friends list"




