Feature: Removing friends from Mina Vänner
  Background:
    Given I am on the Mina Vänner main page
    And I go to "Vänlista"
    And I remove any existing "Test Friend" with all matches
    When I click "Ny Vän" and add "Test Friend" with email "test@example.com"
    And I try to save the friend
    And I go to "Vänlista"