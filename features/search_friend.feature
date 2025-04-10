Feature: Searching friends in Mina Vänner
  As a user of Mina Vänner
  I want to search for friends by name or email
  So that I can find them quickly

  Background:
    Given I am on the Mina Vänner main page
    When I click "Ny Vän" and add "Test Friend" with email "test@example.com"
    And I try to save the friend
    And I go to "Vänlista"

  Scenario Outline: Searching for a friend
    When I search for "<search_term>"
    Then I should see "<expected_name>" in the friends list
    Examples:
      | search_term       | expected_name |
      | Test Friend       | Test Friend   |
      | test@example.com  | Test Friend   |