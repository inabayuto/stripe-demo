import stripe
from stripe import PaymentIntent

def create_and_confirm_payment_intent(
    amount: int,
    currency: str,
    customer_id: str,
    payment_method_id: str
) -> PaymentIntent:
    """
    Creates and immediately confirms a PaymentIntent.

    Args:
        amount: The amount to charge in the smallest currency unit (e.g., cents).
        currency: The currency (e.g., "jpy", "usd").
        customer_id: The ID of the customer.
        payment_method_id: The ID of the PaymentMethod to use.

    Returns:
        The created and confirmed PaymentIntent object.
    """
    payment_intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        payment_method=payment_method_id,
        customer=customer_id,
        confirm=True,
        # 3Dセキュアなどのリダイレクト設定を省略するために下記を設定 (テスト環境向け)
        automatic_payment_methods={"enabled": True, "allow_redirects": "never"},
    )
    return payment_intent
