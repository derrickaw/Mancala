








class Pebble:
	def __init__(self,starting,number):
		self.startingSpot = starting
		self.pebbleNum    = number


def createPebbles():
	gameArray = []
	for i in range(14):
		gameArray.append([])
		if ((i + 1) % 7) != 0:
			for j in range(4):
				gameArray[i].append(Pebble(i,j))
	return gameArray


def main():
	game = createPebbles()
	print (game)




if __name__=='__main__':
    main()