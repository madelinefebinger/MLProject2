# CSC 470 Machine Learning Project 2
#Random training example generator 
#generator.py
import random 

def generate(num, attr1_vals,attr2_vals,attr3_vals,attr4_vals,attr5_vals,attr6_vals ):
	training_examples = []
	i = 0	
	while i < num:
		training_examples.append([attr1_vals[random.randint(0,4)], attr2_vals[random.randint(0,3)],attr3_vals[random.randint(0,3)],
		attr4_vals[random.randint(0,3)], attr5_vals[random.randint(0,3)], attr6_vals[random.randint(0,3)], 'classify'])
		i+=1

	return training_examples

def classify(training_examples, target):
	
	for i in training_examples:
		passing = 0
		for k in range(0,6):
			if target[k] == '?':
				passing +=1
			elif i[k] == '0':
				i[6] = 'No'
				break
			elif target[k] == i[k]:
				passing +=1
		if passing == 6:
			i[6] = 'Yes'
		else:
			i[6] = 'No'

	return training_examples		
			
if __name__ == '__main__':

	target = ['Sunny', 'Warm', '?', '?', '?', '?']
	sky = ['0', '?', 'Sunny', 'Rainy', 'Cloudy']
	temp = ['0', '?', 'Warm', 'Cold']
	humidity = ['0', '?', 'High', 'Normal']
	wind = ['0', '?', 'Strong', 'Weak']
	water = ['0', '?', 'Sunny', 'Rainy']
	forecast = ['0', '?', 'Same', 'Change']

	random_examples = generate(100, sky, temp, humidity, wind, water, forecast)
	classified = classify(random_examples, target)

	for i in classified:
		print(i)
