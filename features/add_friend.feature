Feature: Managing my friends
  As a user of Mina Vänner
  I want to add friends to my list
  So that I can keep track of them

  Background:
    Given I am on the Mina Vänner main page

  Scenario: Adding a single friend and checking the list
    When I click "Ny Vän" and add "Ana" with email "ana@example.com"
    And I go to "Vänlista"
    Then I should see "Ana" in the friends list