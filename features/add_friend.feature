Feature: Managing my friends
  As a user of Mina Vänner
  I want to add friends to my list
  So that I can keep track of them

  Background:
    Given I am on the Mina Vänner main page

  Scenario Outline: Adding a friend and checking the list
    When I click "Ny Vän" and add "<name>" with email "<email>"
    And I go to "Vänlista"
    Then I should see "<name>" in the friends list

    Examples:
      | name | email            |
      | Ana  | ana@example.com  |
      | Bob  | bob@example.com  |

  Scenario: trying to add a friend with missing fields
     When I click "Ny Vän" and add "" with email "test@example.com"
     Then I should see the error message "Fyll i båda fälten för att lägga till din vän"
