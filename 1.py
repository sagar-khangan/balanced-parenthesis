import sys

opening_brackets = ["(","{","["]
closing_brackets = [")","}","]"]
bracket_mapping = {"(":")","{":"}","[":"]"}

# input_list = list("([})")
input_list = list(sys.argv[1])

def check(input_list):
	try:
		queue = []
		for i in input_list:
			if i in opening_brackets:
				queue.append(bracket_mapping[i])
			elif i in closing_brackets:
				if not queue or i != queue.pop():
					return (False)
		return(not queue)
	except Exception as e:
		print(e)
		
print(check(input_list))