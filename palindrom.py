def Palindrome(x):
	return x == x[::-1]

print("Enter the word:")
x = input()
ans = Palindrome(x)

if ans:
	print("Yes")
else:
	print("No")