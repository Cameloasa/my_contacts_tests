Feature: Searching friends in Mina Vänner
  Background:
    Given I am on the Mina Vänner main page

  Scenario Outline: Searching for a friend
    When I click "Ny Vän" and add "<name>" with email "<email>"
    And I try to save the friend
    And I go to "Vänlista"
    When I search for "<search_term>"
    Then I should see "<expected_name>" with email "<expected_email>" in the friends list
    Examples:
      | name        | email            | search_term       | expected_name | expected_email    |
      | Test Friend | test@example.com | Test Friend       | Test Friend   | test@example.com  |
      | Test Friend | test@example.com | test@example.com  | Test Friend   | test@example.com  |