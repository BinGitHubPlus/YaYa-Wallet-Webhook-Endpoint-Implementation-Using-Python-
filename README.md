# YaYa-Wallet-Webhook-Endpoint-Implementation-Using-Python

## Introduction

This project implements a webhook endpoint for YaYa Wallet to notify partner systems about transactions.

## Assumptions

- The incoming data is in JSON format.
- The processing logic is a placeholder and needs to be customized based on actual requirements.

## Prerequisites

- Python 3.x
- Flask library

## How to Test

1. Clone the repository.
2. Activate the virtual environment (`source venv/bin/activate`).
3. Install Flask (`pip install Flask`).
4. Run the Flask app by executing `python app.py`.
5. Use a tool like Postman to send a POST request to `http://localhost:5000/webhook` with sample JSON data.

## Problem-solving Approach

1. Implemented a basic Flask app to handle incoming webhook notifications.
2. Processed the JSON data and provided a placeholder for custom processing logic.
3. Handled exceptions and provided appropriate error responses.
4. Included a simple logging mechanism for received webhook notifications.

## Webhook Integration Guidelines by YaYa Wallet

### Structure of a Webhook Payload

The following example payload shows webhook update information at the end of a transaction:

```json
{
  "id": "1dd2854e-3a79-4548-ae36-97e4a18ebf81",
  "amount": 100,
  "currency": "ETB",
  "created_at_time": 1673381836,
  "timestamp": 1701272333,
  "cause": "Testing",
  "full_name": "Abebe Kebede",
  "account_name": "abebekebede1",
  "invoice_url": "https://yayawallet.com/en/invoice/xxxx"
}



