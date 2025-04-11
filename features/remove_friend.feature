Feature: Removing friends from Mina Vänner
  As a user of Mina Vänner
  I want to remove friends from my list
  So that I can manage my contacts

  Background:
    Given I am on the Mina Vänner main page

  Scenario Outline: Removing a friend from the list
    When I click "Ny Vän" and add "<name>" with email "<email>"
    And I try to save the friend
    And I go to "Vänlista"
    When I remove "<name>" from the friend list
    Then I should not see "<name>" in the friends list
    Examples:
      | name        | email            |
      | Test Friend | test@example.com |