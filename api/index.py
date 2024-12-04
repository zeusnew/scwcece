from flask import Flask, request, jsonify
from truecallerpy import search_phonenumber

app = Flask(__name__)

# Truecaller API Key
API_KEY = "YOUR_TRUECALLER_API_KEY"

@app.route('/lookup', methods=['POST'])
def lookup_number():
    data = request.json
    phone_number = data.get('phone_number')
    try:
        response = search_phonenumber(phone_number, "IN", API_KEY)
        if "data" in response and len(response["data"]) > 0:
            return jsonify({'success': True, 'data': response["data"][0]})
        else:
            return jsonify({'success': False, 'message': 'No data found.'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == "__main__":
    app.run()
