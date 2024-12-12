from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
	data = request.get_json()
	height = data.get('height')
	weight = data.get('weight')
	if height is None or weight is None:
		return jsonify({'error': 'Les paramètres "height" et "weight" sont requis.'}),
	try:
		bmi_value = calculate_bmi(height, weight)
		return jsonify({'bmi': bmi_value}), 200
	except ValueError as e:
		return jsonify({'error': str(e)}), 400

@app.route('/bmr', methods=['POST'])
def bmr():
	data = request.get_json()
	height = data.get('height')
	weight = data.get('weight')
	age = data.get('age')
	gender = data.get('gender')
	if None in [height, weight, age, gender]:
		return jsonify({'error': 'The parameters "height, "weight", "age" and "gender" are required.'}), 400
	if gender not in ['male', 'female']:
		return jsonify({'error': 'The parameter "gender" must be "male" or "female".'}), 400 

	try:
		bmr_value = calculate_bmr(height, weight, age, gender)
		return jsonify({'bmr': bmr_value}), 200
	except ValueError as e:
		return jsonify({'error': str(e)}), 400

if __name__ == '__main__' :
	app.run(debug=True)
