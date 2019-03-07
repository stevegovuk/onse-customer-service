def get_customer(customer_id, customer_repository):
    return customer_repository.fetch_by_id(customer_id)


def create_customer(customer, customer_repository):
    customer_repository.store(customer)


def update_customer_name(customer_id, firstName, surname, customer_repository):
    print("firstName " + firstName )
    customer = customer_repository.fetch_by_id(customer_id)
    customer.first_name = firstName
    customer.surname = surname
    print("Cust firstname " + customer.first_name )

    customer_repository.store(customer)
