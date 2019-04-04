# CSC 470 Machine Learning Project 2
#Random training example generator 
#generator.py
import random 
import find_s

def generate(num, attr1_vals,attr2_vals,attr3_vals,attr4_vals,attr5_vals,attr6_vals ):
	training_examples = []
	i = 0	
	while i < num:
		training_examples.append([attr1_vals[random.randint(0,2)], attr2_vals[random.randint(0,1)],attr3_vals[random.randint(0,1)],
		attr4_vals[random.randint(0,1)], attr5_vals[random.randint(0,1)], attr6_vals[random.randint(0,1)], 'classify'])
		i+=1

	return training_examples

def generate_one_example(attr1_vals,attr2_vals,attr3_vals,attr4_vals,attr5_vals,attr6_vals ):
	return [attr1_vals[random.randint(0,2)], attr2_vals[random.randint(0,1)],attr3_vals[random.randint(0,1)],
		attr4_vals[random.randint(0,1)], attr5_vals[random.randint(0,1)], attr6_vals[random.randint(0,1)], 'classify']

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

	#for i in classified:
		#print(i)


	# Task 3 
	"""'
	For 100 experiments
		set learned hypothesis to null
		create an empty set of training examples

		while the learned hypothesis is not the target hyothesis
			generate a random training example
			increment counter of training examples
			run find_s on the set of training examples so far and update the learned hypothesis

		add the experiment results to the array of results
	
	"""	
	experiment_results = [] # create an array to track experiment results

	for i in range(100):
		learned_hypothesis = ['0','0','0','0','0','0']
		training_examples = []
		num_examples = 0

		while (learned_hypothesis != target):
			random_example = generate_one_example(sky, temp, humidity, wind, water, forecast)
			training_examples.append(random_example)
			classified_training_examples = classify(training_examples,target)
			num_examples += 1
			learned_hypothesis = find_s.find_s_algorithm(classified_training_examples,7)

		experiment_results.append(num_examples)

	print(experiment_results) # Prints out the number of training examples needed for our 100 experiments

