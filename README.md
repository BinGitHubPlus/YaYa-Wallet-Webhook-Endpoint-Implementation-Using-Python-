# YaYa-Wallet-Webhook-Endpoint-Implementation-Using-Python


## Introduction
This project implements a webhook endpoint for YaYa Wallet to notify partner systems about transactions.

## Assumptions
- The incoming data is in JSON format.
- The processing logic is a placeholder and needs to be customized based on actual requirements.

## How to Test
1. Clone the repository.
2. Activate the virtual environment (`source venv/bin/activate`).
3. Install Flask (`pip install Flask`).
4. Run the Flask app by executing `python app.py`.
5. Use a tool like [Postman](https://www.postman.com/) to send a POST request to `http://localhost:5000/webhook` with sample JSON data.

## Problem-solving Approach
- Implemented a basic Flask app to handle incoming webhook notifications.
- Processed the JSON data and provided a placeholder for custom processing logic.
- Handled exceptions and provided appropriate error responses.
- Included a simple logging mechanism for received webhook notifications.




