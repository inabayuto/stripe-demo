from flask import Flask, request, jsonify, send_file
import stripe
import os
from dotenv import load_dotenv
import json # Add json import for potential future use, although jsonify handles most cases

app = Flask(__name__)

# .envファイルを読み込む
load_dotenv()

# 環境変数からシークレットキーを取得し、Stripeに設定
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

# APIキーが取得できたか確認（任意）
if not stripe.api_key:
    raise ValueError("STRIPE_SECRET_KEY not found in environment variables or .env file")

# 簡単のため、サーバー起動時にデモ用の顧客を作成し、そのIDを使用します。
# 実際のアプリケーションでは、ユーザー認証と連携して顧客を管理します。
try:
    # Check if a customer ID is already saved (e.g., in a simple file or DB in a real app)
    # For this simple example, we'll just create one every time the server starts
    customer = stripe.Customer.create(
        email="demo-web-user@example.com",
        name="Demo Web User"
    )
    customer_ID = customer.id
    print(f"Created demo customer with ID: {customer_ID}")

except stripe.error.StripeError as e:
    print(f"Error creating demo customer: {e}")
    # If customer creation fails critically, you might want to exit
    customer_ID = None # Ensure ID is None if creation failed

@app.route('/')
def index():
    # index.html ファイルを配信します
    # {{.PublishableKey}} を実際の公開可能キーに置き換える必要があります
    # 簡単のため、ここではファイルを直接読み込み、キーを置き換えて返します。
    # 本来はFlaskのテンプレート機能 (Jinja2など) を使うべきです。
    publishable_key = os.getenv("STRIPE_PUBLISHABLE_KEY")
    if not publishable_key:
         return "Stripe Publishable Key not set in environment variables.", 500

    try:
        with open('index.html', 'r') as f:
            html_content = f.read()
            # Place the publishable key into the HTML (simple string replace for demo)
            html_content = html_content.replace('{{.PublishableKey}}', publishable_key)
            return html_content, 200, {'Content-Type': 'text/html'}
    except FileNotFoundError:
        return "index.html not found.", 404


@app.route('/save-payment-method', methods=['POST'])
def save_payment_method():
    # 顧客IDが利用可能か確認
    if customer_ID is None:
        return jsonify({"success": False, "error": "Demo customer ID not available."}), 500

    # リクエストボディからPaymentMethod IDを取得
    data = request.get_json()
    payment_method_id = data.get('paymentMethodId')

    if not payment_method_id:
        return jsonify({"success": False, "error": "paymentMethodId not provided."}), 400

    print(f"Received PaymentMethod ID: {payment_method_id} for Customer ID: {customer_ID}")

    try:
        # PaymentMethodを顧客にアタッチする
        stripe.PaymentMethod.attach(
            payment_method_id,
            customer=customer_ID,
        )
        print(f"PaymentMethod {payment_method_id} successfully attached to customer {customer_ID}")

        return jsonify({
            "success": True,
            "customerId": customer_ID,
            "message": "Payment method attached successfully."
        }), 200

    except stripe.error.StripeError as e:
        print(f"Stripe API Error: {e}")
        return jsonify({"success": False, "error": str(e)}), 500
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"success": False, "error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # サーバー起動
    port = int(os.environ.get("PORT", 5000)) # デフォルトポートを5000に設定
    app.run(port=port, debug=True) # debug=True は開発用です
