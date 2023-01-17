from phonenumbers import carrier
from flask import Flask, request
import phonenumbers

app = Flask(__name__)

@app.route('/phonenumber_carrier', methods=['POST'])
def get_phonenumber_carrier():
    request_data = request.get_json()
    # Get the phone number from the request
    phone_number = request_data['phone_number']

    # Parse the phone number using the phonenumbers library
    parsed_number = phonenumbers.parse(phone_number)
    
    # Use the phonenumbers library to get the carrier for the parsed phone number
    carrier_name = carrier.name_for_number(parsed_number, "en")
    
    # Return the carrier name
    return carrier_name

if __name__ == '_main_':
    app.run()


