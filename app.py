from flask import Flask, request, abort
import hmac
import hashlib
import json
import os
import time

app = Flask(__name__)

# Replace 'your_secret_key' with the actual secret key provided by YaYa Wallet
SECRET_KEY = 'your_secret_key'

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Step 1: Get the raw data from the request
        data = request.get_data(as_text=True)

        # Step 2: Verify the signature to ensure the request is from YaYa Wallet
        verify_signature(request.headers.get('YAYA-SIGNATURE'), data)

        # Step 3: Process the JSON payload
        payload = json.loads(data)
        process_webhook(payload)

        # Step 4: Respond with a success message
        return 'Webhook received successfully', 200

    except Exception as e:
        # Handle any exceptions during processing
        print(f"Error processing webhook: {str(e)}")
        abort(400)

def verify_signature(signature, data):
    # Step 1: Ensure YAYA-SIGNATURE header is present
    if not signature:
        abort(400)

    # Step 2: Prepare the signed_payload by concatenating values from the payload
    signed_payload = ''.join([str(value) for value in json.loads(data).values()])

    # Step 3: Compute the expected signature using HMAC SHA256
    expected_signature = hmac.new(bytes(SECRET_KEY, 'latin-1'), msg=bytes(signed_payload, 'latin-1'), digestmod=hashlib.sha256).hexdigest()

    # Step 4: Compare the computed signature with the received signature
    if not hmac.compare_digest(expected_signature, signature):
        # If signatures don't match, reject the request
        abort(401)

def process_webhook(payload):
    # Step 1: Your custom processing logic goes here
    print(f"Received webhook data: {json.dumps(payload)}")

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)





