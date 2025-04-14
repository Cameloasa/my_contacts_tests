Feature: Searching friends in Mina Vänner

  Background:
    Given I am on the Mina Vänner main page
    And I go to "Vänlista"
    And I remove any existing "Test Friend"
    When I click "Ny Vän" and add "Test Friend" with email "test@example.com"
    And I try to save the friend
    And I go to "Vänlista"

  Scenario Outline: Searching for a friend
    When I search for "<search_term>"
    Then I should see "<expected_name>" with email "<expected_email>" in the friends list
    Examples:
      | search_term       | expected_name | expected_email    |
      | Test Friend       | Test Friend   | test@example.com  |
      | test@example.com  | Test Friend   | test@example.com  |