Feature: Removing friends from Mina Vänner
  As a user of Mina Vänner
  I want to remove friends from my list
  So that I can manage my contacts

  Background:
    Given I am on the Mina Vänner main page
    When I click "Ny Vän" and add "Test Friend" with email "test@example.com"
    And I try to save the friend
    And I go to "Vänlista"

  Scenario: Removing a friend from the list
    When I remove "Test Friend" from the friend list
    Then I should not see "Test Friend" in the friends list