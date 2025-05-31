import stripe
from stripe import Customer


def create_stripe_customer(email: str, name: str) -> Customer:
    """
    Creates a new Stripe customer.

    Args:
        email: The customer's email address.
        name: The customer's name.

    Returns:
        The created Stripe Customer object.
    """

    customer: Customer = stripe.Customer.create(
        email=email,
        name=name
    )
    return customer.id

def get_customer(customer_id: str) -> Customer:
    """
    Retrieves an existing Stripe customer by ID.

    Args:
        customer_id: The ID of the customer to retrieve.

    Returns:
        The Stripe Customer object.
    """
    customer: Customer = stripe.Customer.retrieve(customer_id)
    return customer