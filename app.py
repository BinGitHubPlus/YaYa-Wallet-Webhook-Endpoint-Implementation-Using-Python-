from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()

        # Process the data as needed
        # Example: Log the transaction details
        print("Received Webhook Notification:")
        print(data)

        # Implement verification and replay handling as needed

        return jsonify({"status": "success"}), 200

    except Exception as e:
        print(f"Error processing webhook: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
