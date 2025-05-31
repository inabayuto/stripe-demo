from customer import create_stripe_customer, get_customer
from payment_method import attach_payment_method_to_customer, list_customer_payment_methods
from payment_intent import create_and_confirm_payment_intent
import sys; sys.path.insert(0, '..')
from utils.setup import setup_stripe

import os
import stripe

if __name__ == "__main__":
    # Stripeのセットアップ
    setup_stripe()

    customer_email = "test@test.com"
    customer_name = "John Doe from python code"
    
    # customer_id = create_stripe_customer(customer_email, customer_name)

    customer_id = "cus_SPcSptHlmw9f32"
    try:
        customer = get_customer(customer_id)
        print(f"created with ID: {customer.id}")
    except stripe.error.InvalidRequestError as e:
        print(f"Error retrieving customer {customer}: {e}")
    

    payment_method_id = "pm_card_visa"
    try:
        pm =  attach_payment_method_to_customer(payment_method_id, 
                                                customer_id)
        payment_methods = list_customer_payment_methods(customer_id)

        print(f"PaymentMethod {pm.id} successfully attached.")
    except stripe.error.StripeError as e:
         print(f"Could not attach PaymentMethod {customer_id}: {e}")

    pm_id = payment_methods.data[0]["id"]
    amount = 2000
    currency = "jpy"

    try:
        payment_intent = create_and_confirm_payment_intent(
            amount,
            currency,
            customer_id,
            pm_id
        )
        print("success payment")
    except stripe.error as e:
        print("An error occurred during payment processing")
