# CSC 470 Machine Learning Project 2
#Random training example generator 
#generator.py
import random 

def generate(num, attr1_vals,attr2_vals,attr3_vals,attr4_vals,attr5_vals,attr6_vals ):
	training_examples = []
	i = 0	
	while i < num:
		training_examples.append([attr1_vals[random.randint(0,2)], attr2_vals[random.randint(0,1)],attr3_vals[random.randint(0,1)],
		attr4_vals[random.randint(0,1)], attr5_vals[random.randint(0,1)], attr6_vals[random.randint(0,1)], 'classify'])
		i+=1

	return training_examples

def classify(training_examples, target):
	
	for i in training_examples:
		passing = 0
		for k in range(0,6):
			if target[k] == '?':
				passing +=1
			elif target[k] == i[k]:
				passing +=1
		if passing == 6:
			i[6] = 'Yes'
		else:
			i[6] = 'No'

	return training_examples		
			
if __name__ == '__main__':

	target = ['Sunny', 'Warm', '?', '?', '?', '?']
	sky = ['Sunny', 'Rainy', 'Cloudy']
	temp = ['Warm', 'Cold']
	humidity = ['High', 'Normal']
	wind = ['Strong', 'Weak']
	water = ['Sunny', 'Rainy']
	forecast = ['Same', 'Change']

	random_examples = generate(100, sky, temp, humidity, wind, water, forecast)
	classified = classify(random_examples, target)

	for i in classified:
		print(i)
