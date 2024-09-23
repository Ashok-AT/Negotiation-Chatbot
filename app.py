from flask import Flask, request, jsonify
from transformers import pipeline, set_seed
import warnings

# Suppress FutureWarning from transformers library
warnings.filterwarnings("ignore", category=FutureWarning)

app = Flask(__name__)

# Initialize the GPT-2 generator
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

# Pricing logic
BASE_PRICE = 100
ACCEPTANCE_THRESHOLD = 50  # Price range to accept user offer

@app.route('/negotiate', methods=['POST'])
def negotiate():
    user_message = request.json.get('message')

    if user_message is None:
        return jsonify({'error': 'Message not provided'}), 400

    # Extract price and context from user message
    try:
        price_context = user_message.split(',')
        user_price = float(price_context[0].strip())
        context = price_context[1].strip() if len(price_context) > 1 else ""
    except Exception:
        return jsonify({'error': 'Invalid message format. Provide a price and context separated by a comma.'}), 400

    # Generate a response using the GPT-2 model
    response_text = generate_response(user_price, context)

    return jsonify({'response': response_text})

def generate_response(user_price, context):
    # Check if user price is within acceptable range
    if user_price >= BASE_PRICE - ACCEPTANCE_THRESHOLD:
        return f"I accept your offer of ${user_price}."

    # Create the prompt for negotiation
    prompt = (
        f"User's offer: ${user_price}\n"
        f"Context: {context}\n"
        "You are a seller. Respond to the user's offer with either acceptance, a counteroffer, or a reason for rejection. "
        "Make sure to be persuasive and directly address the user's context."
    )

    # Call GPT-2 to generate a response
    results = generator(
        prompt,
        max_length=60,
        num_return_sequences=1,
        truncation=True,
        pad_token_id=50256,
        clean_up_tokenization_spaces=True
    )

    # Extract the generated text from the results
    bot_reply = results[0]['generated_text']

    # Identify where the prompt ends and the response begins
    response_start_index = len(prompt)
    bot_reply = bot_reply[response_start_index:].strip()  # Slice the response correctly

    return bot_reply if bot_reply else "I'm not sure how to respond to that."

if __name__ == '__main__':
    app.run(debug=True)
