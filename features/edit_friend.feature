Feature: Editing friends in Mina Vänner
  As a user of Mina Vänner
  I want to edit my friends details
  So that I can keep my contacts up to date

  Background:
    Given I am on the Mina Vänner main page

  Scenario Outline: Changing friend details
    When I click "Ny Vän" and add "<original_name>" with email "<original_email>"
    And I try to save the friend
    And I go to "Vänlista"
    When I edit "<original_name>" to have name "<new_name>" and email "<new_email>"
    Then I should see "<new_name>" with email "<new_email>" in the friends list
    And I should only see "<original_name>" if "<new_name>" is "<original_name>"
    Examples:
      | original_name | original_email   | new_name       | new_email           |
      | Test Friend   | test@example.com | Updated Friend | test@example.com    |
      | Test Friend   | test@example.com | Test Friend    | updated@example.com |