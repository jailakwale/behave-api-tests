
import requests
from behave import given, when, then

@given('the API endpoint is "{url}"')
def step_impl(context, url):
    context.url = url

@when("I send a GET request")
def step_impl(context):
    context.response = requests.get(context.url)

@then("the response code should be {status_code:d}")
def step_impl(context, status_code):
    assert context.response.status_code == status_code

@then('the response should contain "{key}"')
def step_impl(context, key):
    assert key in context.response.text
