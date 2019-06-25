
def compute(a,b):
	return a+b

def output(a,b):
	print("{0} + {1} = {2} ".format(a,b,compute(a,b)))

def main():
	print("Addition of 2 no.s: ")
	a=input("Enter the 1st no. : ")
	b=input("Enter the 2nd no. : ")
	output(a,b)

main()

