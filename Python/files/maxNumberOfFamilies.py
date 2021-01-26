class Solution:
	def maxNumberOfFamilies(self, n: int, reservedSeats: [[int]]) -> int:
		firstPossComb = set([2,3,4,5])
		secondPossComb = set([6,7,8,9])
		thirdPossComb = set([4,5,6,7])
		reservationIndex = 0
		maxGrouping = 0
		reservedSeats.sort()

		for rowNum in range(n):
			firstPoss = True
			secondPoss = True
			thirdPoss = True

			while reservationIndex < len(reservedSeats) and (reservedSeats[reservationIndex][0] == (rowNum+1)):
				firstPoss = firstPoss and not(reservedSeats[reservationIndex][1] in firstPossComb)
				secondPoss = secondPoss and not(reservedSeats[reservationIndex][1] in secondPossComb)
				thirdPoss = thirdPoss and not(reservedSeats[reservationIndex][1] in thirdPossComb)
				reservationIndex += 1

			if firstPoss and secondPoss:
				maxGrouping += 2
			elif firstPoss or secondPoss or thirdPoss:
				maxGrouping += 1

		return maxGrouping

	def maxNumberOfFamiliesEff(self, n: int, reservedSeats: [[int]]) -> int:
		firstPossComb = set([2,3,4,5])
		secondPossComb = set([6,7,8,9])
		thirdPossComb = set([4,5,6,7])
		maxGrouping = 0

		organizedReservedSeats = {}

		for reservation in reservedSeats:
			if reservation[0] not in organizedReservedSeats:
				organizedReservedSeats[reservation[0]] = [True and not(reservation[1] in firstPossComb), \
															True and not(reservation[1] in secondPossComb), \
															True and not(reservation[1] in thirdPossComb)]
			else:
				if reservation[1] in firstPossComb:
					organizedReservedSeats[reservation[0]][0] = False
				if reservation[1] in secondPossComb:
					organizedReservedSeats[reservation[0]][1] = False
				if reservation[1] in thirdPossComb:
					organizedReservedSeats[reservation[0]][2] = False

		maxGrouping = 2*n
		maxGrouping -= 2*len(organizedReservedSeats)

		for reservationRow in organizedReservedSeats.values():
			if reservationRow[0] and reservationRow[1]:
				maxGrouping += 2
			elif reservationRow[0] or reservationRow[1] or reservationRow[2]:
				maxGrouping += 1

		return maxGrouping
