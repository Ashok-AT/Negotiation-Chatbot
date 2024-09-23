# Negotiation Chatbot

This project is a Negotiation Chatbot built using Flask and the pretrained model GPT-2 API from Hugging Face's Transformers library. The chatbot is designed to negotiate with users based on their offers and provide persuasive responses.

## Features

- Negotiate, Accepts or Decline customer offer and context.
- Provides acceptance, counteroffers, or reasons for rejection.
- Built using Flask and GPT-2.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ashok-AT/Negotiation-Chatbot.git
   cd Negotiation-Chatbot

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:
   ```bash
   pip install -r requirements.txt

## Usage

1. Run the application:
   ```bash
   python app.py
   
2. Send a POST request to the /negotiate endpoint with a JSON payload on cmd:
   ```bash 
   curl -X POST http://127.0.0.1:5000/negotiate -H "Content-Type: application/json" -d "{\"message\": \"40, Im a regular customer, make discount.\"}"

## Disadvantages

- The bot uses the GPT-2 API from Hugging Face, which is an older pre-trained model and struggles to understand user inputs, leading to irrelevant responses.

- Advanced models like GPT-3, GPT-3.5, GPT-4, and Gemini require paid subscriptions, which I cannot afford.
