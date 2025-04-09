from behave import given, when, then

from pages.friends_page import click_new_friend, fill_name, fill_email, click_save, go_to_friend_list

@given(u'I am on the Mina Vänner main page')
def step_given_main_page(context):
    context.page.goto(context.base_urls["main"])
    assert "my-contacts" in context.page.url, "Not on Mina Vänner main page"

@when(u'I click "Ny Vän" and add "Ana" with email "ana@example.com"')
def step_when_add_friend(context):
    # Click on "Ny Vän" să open the form
    click_new_friend(context.page)
    # Fill input Namn and E-post
    fill_name(context.page, "Ana") # input: Namn
    fill_email(context.page, "ana@example.com") #input: E-post
    # Click on button "Spara" to save
    click_save(context.page)

@when(u'I go to "Vänlista"')
def step_when_go_to_friend_list(context):
    #Click button "Vänlista"
    go_to_friend_list(context.page)

@then(u'I should see "Ana" in the friends list')
def step_then_see_friend_in_list(context):
    assert context.page.get_by_text("Ana", exact= True).is_visible(), "Ana not found in friends list"
