class Solution:
	def simplifyPath(self, path: str) -> str:
		if len(path) == 0:
			return ""

		i = 1
		commandList = []

		while i < len(path):
			command = ''
			while i < len(path) and path[i] != '/':
				command += path[i]
				i += 1

			if len(command):
				if command == "..":
					if len(commandList):
						commandList.pop()
				else:
					if command != ".":
						commandList.append(command)
			i += 1

		retVal = ""
		for command in commandList:
			retVal += "/" + command

		retVal = "/" if not len(retVal) else retVal

		return retVal
