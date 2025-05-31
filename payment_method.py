import stripe
from stripe import PaymentMethod, ListObject

def attach_payment_method_to_customer(payment_method_id: str, customer_id: str) -> PaymentMethod:
    """
    Attaches a PaymentMethod to a Stripe customer.

    Args:
        payment_method_id: The ID of the PaymentMethod to attach.
        customer_id: The ID of the customer to attach the PaymentMethod to.

    Returns:
        The attached PaymentMethod object.
    """
    # setup_stripe()
    pm: PaymentMethod = stripe.PaymentMethod.attach(
        payment_method_id,
        customer=customer_id,
    )
    return pm


def list_customer_payment_methods(customer_id: str, type: str = "card") -> ListObject[PaymentMethod]:
    """
    Lists PaymentMethods for a given customer.

    Args:
        customer_id: The ID of the customer.
        type: The type of PaymentMethods to list (e.g., "card", "sepa_debit"). Defaults to "card".

    Returns:
        A ListObject containing PaymentMethod objects.
    """
    payment_methods: ListObject[PaymentMethod] = stripe.PaymentMethod.list(
        customer=customer_id,
        type=type,
    )
    return payment_methods
