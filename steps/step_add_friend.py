from behave import given, when, then

@given(u'I am on the Mina Vänner main page')
def step_given_main_page(context):
    assert "my-contacts" in context.page.url, "Not on Mina Vänner main page"

@when(u'I click "Ny Vän" and add "Ana" with email "ana@example.com"')
def step_when_add_friend(context):
    # Click on "Ny Vän" să open the form
    context.page.get_by_text("Ny Vän").click()
    # Waiting form to appear
    context.page.wait_for_selector("section.form", timeout=10000)
    # Fill input Namn and E-post
    form = context.page.locator("section.form")
    form.locator("input").nth(0).fill("Ana")  # input: Namn
    form.locator("input").nth(1).fill("ana@example.com")  #input: E-post
    # Click on button "Spara" to save
    context.page.get_by_text("Spara").click()

@when(u'I go to "Vänlista"')
def step_when_go_to_friend_list(context):
    #Click button "Vänlista"
    context.page.get_by_text("Vänlista").click()

@then(u'I should see "Ana" in the friends list')
def step_then_see_friend_in_list(context):
    assert context.page.get_by_text("Ana", exact= True).is_visible(), "Ana not found in friends list"
