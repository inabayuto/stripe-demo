from stripe import StripeClient
from stripe import Customer
import stripe
import os
from dotenv import load_dotenv

load_dotenv()


def setup_stripe():
    # 環境変数からシークレットキーを取得し、Stripeに設定
    stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
    
    # APIキーが取得できたか確認（任意）
    if not stripe.api_key:
        raise ValueError("STRIPE_SECRET_KEY not found in environment variables or .env file")
    
