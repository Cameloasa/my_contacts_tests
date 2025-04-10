Feature: Editing friends in Mina Vänner
  As a user of Mina Vänner
  I want to edit my friends details
  So that I can keep my contacts up to date

  Background:
    Given I am on the Mina Vänner main page
    When I click "Ny Vän" and add "Test Friend" with email "test@example.com"
    And I try to save the friend
    And I go to "Vänlista"

  Scenario Outline: Changing friend details
    When I edit "Test Friend" to have name "<new_name>" and email "<new_email>"
    Then I should see "<new_name>" with email "<new_email>" in the friends list
    And I should only see "Test Friend" if "<new_name>" is "Test Friend"
    Examples:
        | new_name       | new_email           |
        | Updated Friend | test@example.com    |
        | Test Friend    | updated@example.com |