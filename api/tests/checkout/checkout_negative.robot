*** Settings ***
Documentation       Failed Customer Checkout
Library             Checkout.py

*** Test Cases ***
Validate that the response code is equal to 400 when malformed payload is passed
    [Tags]  negative
    Given a user wants to place an order
    When a request with incorrect payload was made
    Then response code should be    code=400

Validate that the response code is equal to 500 when server ecounters error
    [Tags]  negative
    Given a user wants to place an order
    When a request with correct payload was made  # Use cases of 500 depends on the status of the server's health
    Then response code should contain 5 in the beginning
