# CSC 470 Machine Learning Project 2
# find_s.py

# Returns true if an example attribute is consistent with the hypothesis constraint
# Otherwise returns false
def is_consistent(hyp_constraint,example_attr):
	if (hyp_constraint == '?'):
		return True
	elif (hyp_constraint == example_attr):
		return True
	else:
		return False

# Returns the next most general attribute that will make h consistent with the training example
# If constraint is 0, return the attribute 
# If constraint is a single attribute, return a ?
def next_most_general_constraint(constraint,example_attr):
	if (constraint == '0'):
		return example_attr
	else:
		return '?'
	

if __name__ == '__main__':
	
	#Find-S Algorithm pseudo-code
	# 1. Initialize h to the most specific hypothesis in H

	h = ['0','0','0','0','0','0']

	# Create training examples
	num_attrs = 7
	training_examples = []

	training_examples.append(['Sunny','Warm','Normal','Strong','Warm','Same','Yes'])
	training_examples.append(['Sunny','Warm','High','Strong','Warm','Same','Yes'])
	training_examples.append(['Rainy','Cold','High','Strong','Warm','Change','No'])
	training_examples.append(['Sunny','Warm','High','Strong','Cool','Change','Yes'])

	"""
	2. For each positive training instance x: 
		For each attribute constraint a_i in h:
			if the constraint a_i is satisfied by x:
				do nothing
			else replace a_i in h by the next most general constraint that is satisfied by x
	"""

	for example in training_examples:
		if (example[-1] == 'No'):
			continue

		for i in range(num_attrs-1):
			if (not is_consistent(h[i],example[i])):
				h[i] = next_most_general_constraint(h[i],example[i]) # Replace by the next most general constraint


	# 3. Output hypothesis h
	print(h)


