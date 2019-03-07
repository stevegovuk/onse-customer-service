Feature: Get the customer based on id
  As a service I want to get the customer details so that I can check whether they exist.

#  Scenario: Fetching existing customer
#    Given customer "Nicole Forsgren" with ID "12345" exists
#    When I fetch customer "12345"
#    Then I should see customer "Nicole Forsgren"
#
#  Scenario: Fetching customer which doesn't exist
#    Given there is no customer with ID "99999"
#    When I fetch customer "99999"
#    Then I should get a not found response
#
#  Scenario: Changing customer name
#    Given I fetch customer "1"
#    When I update the customer name to be "Fred Bloggs"
#    Then I fetch customer "1"
#    And the customer name is "Fred Bloggs"

  Scenario: Changing customer name
    Given customer "Ted Blobs" with ID "1" exists
    When I update the customer name to be "Fred Bloggs"
    When I fetch customer "1"
    Then I should see customer "Fred Bloggs"
