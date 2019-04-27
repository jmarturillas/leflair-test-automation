*** Settings ***
Documentation       Successful Customer Checkout
Library             Checkout.py

*** Test Cases ***
Validate that the response code is equal to 200
    [Tags]  positive
    Given a user wants to place an order
    When a request with correct payload was made
    Then response code should be    code=200

Validate that the response contains order code in presence of "code" key
    [Tags]  positive
    Given a user wants to place an order
    When a request with correct payload was made
    Then response body should contain key named     contains="code"

Validate that the response contains order total amount in presence of "total" key
    [Tags]  positive
    Given a user wants to place an order
    When a request with correct payload was made
    Then response body should contain key named     contains="total"

Validate the the response schema is correct
    [Tags]  positive
    Given a user wants to place an order
    When a request with correct payload was made
    Then response schema should be correct