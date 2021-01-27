class Solution:
	def displayTable(self, orders: [[str]]) -> [[str]]:
		loggedFood = set()
		loggedTables = set()
		for order in orders:
			if order[2] not in loggedFood:
				loggedFood.add(order[2])
			if order[1] not in loggedTables:
				loggedTables.add(int(order[1]))

		foodItems = list(loggedFood)
		foodItems.sort()
		foodToColDict = {}
		for i, item in enumerate(foodItems):
			foodToColDict[item] = i

		tableOrder = {}
		for order in orders:
			tableNum = int(order[1])
			food = order[2]
			foodNum = foodToColDict[food]
			if tableNum in tableOrder:
				tableOrder[tableNum][foodNum] = str(int(tableOrder[tableNum][foodNum]) + 1)
			else:
				tableOrder[tableNum] = ["0"] * len(foodItems)
				tableOrder[tableNum][foodNum] = str(int(tableOrder[tableNum][foodNum]) + 1)

		retArr = []
		tables = list(loggedTables)
		tables.sort()
		retArr.append(['Table'] + foodItems)
		for index in tables:
			retArr.append([str(index)] + tableOrder[index])

		return retArr
