def print_num(n):
	if n == 1:
		return 1
	return str(print_num(n-1)) + ' ' + str(n)

print(print_num(4))
