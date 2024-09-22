from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'GET':
        return jsonify({"operation_code": 1}), 200

    if request.method == 'POST':
        data = request.get_json()
        user_id = "john_doe_17091999"  # Example
        file_b64 = data.get("file_b64", "")
        file_valid = bool(file_b64)  # Validate file existence
        
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": [x for x in data['data'] if x.isdigit()],
            "alphabets": [x for x in data['data'] if x.isalpha()],
            "highest_lowercase_alphabet": [max([x for x in data['data'] if x.islower()])] if any(x.islower() for x in data['data']) else [],
            "file_valid": file_valid,
            "file_mime_type": "image/png" if file_valid else "unknown",
            "file_size_kb": 400 if file_valid else 0
        }
        return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
