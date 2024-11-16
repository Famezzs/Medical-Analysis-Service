from flask import Flask, request, jsonify
from module.controller.UserController import UserController
from module.controller.AuthenticationController import AuthenticationController
from module.controller.IllnessController import IllnessController
from module.static.Configuration import Configuration
from module.helper.IllnessesToArrayConverter import IllnessesToArrayConverter

app = Flask(__name__)

# Register endpoint
@app.route('/api/v1/register', methods=['POST'])
def register():
    try:
        json_data = request.get_json()
        user = UserController.parse_json_user(json_data.get('user'))
        authentication_controller = AuthenticationController(Configuration)
        login_details = authentication_controller.parse_json_login_details(json_data.get('login_details'), True)
        authentication_controller.register_user(user, login_details)
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Login endpoint
@app.route('/api/v1/login', methods=['POST'])
def login():
    try:
        json_data = request.get_json()
        authentication_controller = AuthenticationController(Configuration)
        login_details = authentication_controller.parse_json_login_details(json_data.get('login_details'))
        authentication_controller.authenticate_user(login_details)
        return jsonify({"message": "Logged in successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Logout endpoint
@app.route('/api/v1/logout', methods=['POST'])
def logout():
    try:
        authentication_controller = AuthenticationController(Configuration)
        authentication_controller.logout_user()
        return jsonify({"message": "Logged out successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Conduct analysis endpoint
@app.route('/api/v1/analysis', methods=['POST'])
def conduct_analysis():
    try:
        json_data = request.get_json()
        illness_controller = IllnessController(Configuration)
        requested_illnesses = illness_controller.get_illnesses_from_list(json_data.get('illnesses_list'))
        illness_to_array_converter = IllnessesToArrayConverter()
        return jsonify({"analysis": illness_to_array_converter.convert(requested_illnesses)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get illnesses endpoint
@app.route('/api/v1/illnesses', methods=['GET'])
def get_illnesses():
    try:
        illness_controller = IllnessController(Configuration); illnesses = illness_controller.get_illnesses()
        illness_to_array_converter = IllnessesToArrayConverter()
        return jsonify({"illnesses": illness_to_array_converter.convert(illnesses)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Create illness endpoint
@app.route('/api/v1/illness', methods=['POST'])
def create_illness():
    try:
        json_data = request.get_json()
        illness_controller = IllnessController(Configuration)
        illness = illness_controller.parse_json_illness(json_data.get('illness'), True, False)
        illness_controller.create_illness(illness)
        return jsonify({"message": "Illness created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Update illness endpoint
@app.route('/api/v1/illness', methods=['PUT'])
def update_illness():
    try:
        json_data = request.get_json()
        illness_controller = IllnessController(Configuration)
        illness = illness_controller.parse_json_illness(json_data.get('illness'), False, True)
        illness_controller.update_illness(illness)
        return jsonify({"message": "Illness updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
