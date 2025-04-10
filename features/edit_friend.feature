Feature: Editing friend in Mina Vänner
    As a user in Mina >Vänner
    I want to edit my friends details
    So that I kan keep my contacts up to date

    Background:
        Given I am on Mina Vänner main page
        When I click "Ny vän" and add "Test Friend" with example "test@example.com"
        And I try to save the friend
        And I go to "Vänlista"

    Scenario outline: Changing a friends details
        When I edit "Test Friend" to have name "<new_name>" and email "<new_email>"
        Then I should see "<new_name>" in the friends list
        And I should not see "Test Friend" in the friends list
        Examples:
        | new_name       | new_email           |
        | Updated Friend | test@example.com    |
        | Test Friend    | updated@example.com |