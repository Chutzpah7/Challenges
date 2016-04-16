import sys
import math
rad = True
ans = None
while True:
	stack = []
	for string in raw_input().split(" "):
		try:
			stack.append(float(string))
		except ValueError:
			if string == "ans":
				stack.append(ans)
			elif string in ["*","x"]:
				stack.append(stack.pop()*stack.pop()) # Multiply top two values
			elif string == "+":
				stack.append(stack.pop()+stack.pop()) # Add top two values
			elif string == "/":
				stack.append(1/stack.pop()*stack.pop()) # Subtract top two values
			elif string == "-":
				stack.append(-(stack.pop()-stack.pop()))
			elif string == "^":
				a = stack.pop()
				b = stack.pop()
				stack.append(b**a)
			elif string == "e":
				stack.append(math.e)
			elif string == "pi":
				stack.append(math.pi)
			elif string == "sin":
				if rad:
					stack.append(math.sin(stack.pop()))
				else:
					stack.append(math.sin(stack.pop()*math.pi/180.0))
			elif string == "cos":
				if rad:
					stack.append(math.cos(stack.pop()))
				else:
					stack.append(math.cos(stack.pop()*math.pi/180.0))
			elif string == "tan":
				if rad:
					stack.append(math.tan(stack.pop()))
				else:
					stack.append(math.tan(stack.pop()*math.pi/180.0))
			elif string == "rad":
				rad = True
			elif string == "deg":
				rad = False
			elif string is "abs":
				stack.append(math.fabs(stack.pop()))
			elif string == "exit":
				sys.exit()
			else:
				print "unknown symbol"
				break
	if len(stack) is 1:
		ans = stack.pop()
		print int(ans) if ans.is_integer() else ans
	else:
		print "invalid number of operators"