from behave import when, then

from features.steps.get_customer import fetch_customer


@given(u'I fetch customer "{custid}"')
def i_fetch_cust(context, custid):
    context.custid = custid
    context.first_name = fetch_customer(context, custid).first_name


@when(u'I update the customer name to be "{custname}"')
def i_update_cust(context,custname):

    print("update_custb " + custname)
    (first_name, surname) = custname.split(' ', 2)

    response = context.web_client.put(
        '/customers/' + context.custid,
        json={'firstName': first_name, 'surname': surname})

    assert response.status_code == 201, response.status_code
    # context.customer_id = response.get_json()['customerId']


@then(u'I fetch customer "{custid}"')
def i_fetch_cust(context, custid):
    context.custid = custid
    context.customer = fetch_customer(context,custid)
    print("got cust " + str(context.custid))

@then(u'the customer name is "{expected_name}"')
def assert_customer(context, expected_name):
    print("Start")
    response = context.response
    customer = context.customer
    print(customer)
    # assert response.status_code == 200, response.status_code
    # assert response.is_json
    customer.first_name
    body = response.get_json()
    print("body " + str(body))
    assert customer.first_name + " " + customer.surname == expected_name
