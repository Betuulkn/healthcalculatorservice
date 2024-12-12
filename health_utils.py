def calculate_bmi(height, weight):
if height <= O:
	raise ValueError
return weight / (height ** 2)

def calculate_bmr(height, weight, age, gender): 
if gender == 'male':
	bmr = 66.5 + (13.75 * weight) + (5.003 * height) - (6.75 * age)
elif gender == 'female':
	bmr = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
else:
	raise ValueError("The gender must be 'male' or 'female'.")
return bmr
