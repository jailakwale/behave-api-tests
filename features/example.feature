
Feature: API testing with reqres.in

  Scenario: Get user details
    Given the API endpoint is "https://reqres.in/api/users/2"
    When I send a GET request
    Then the response code should be 200
    And the response should contain "Janet"



    
