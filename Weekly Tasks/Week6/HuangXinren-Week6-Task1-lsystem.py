# Give inital object for the lsystem
initial = "AB"

# Give rules for lsystem
# A is assigned to AB, B is assigned to A
rules = {
	"A": "AB",
	"B": "A"
}

def l_system(initial, rules, generation):
	current = initial
	# Copy the inital state into variable current 

	for _ in range(0, generation):
		# Decide how many generation you want
		result = ""
		# Set an empty string as the variable 

		for state in current:
			# Current will have the value of last generation 
			result += rules.get(state, state)
			# If there's not C as a key in the dictionary, return C

		current = result
		# Assign the result string to current

	return current

for i in range(0, 10):
	print( "{}: {}".format(i, l_system(initial, rules, i)) )
	# String formatting
	# i is correspond to the first {}, l_system(initial, rules, i) is correspond to the second {}
	# i is generation
