# Returns snap when divisible by 3 (or contains 3),
# crackle when divisible by 7 (or contains 7),
# and snap crackle when divisible by 3 and 7 (or contains 3 and 7)
def snapCrackle(n: int) -> str:
	retStr = str(n) + " "
	numsIn = checkChar(n)
	if n%3 == 0 or 3 in numsIn:
		retStr += "snap "
	if n%7 == 0 or 7 in numsIn:
		retStr += "crackle"
	return retStr

# Returns a set, which contains number that appeared
def checkChar(n: int) -> set():
	numsIn = set()
	while n != 0:
		numsIn.add(int(n%10))
		n = int(n/10)
	return numsIn

if __name__ == '__main__':
	for i in range(100):
		print(snapCrackle(i+1))