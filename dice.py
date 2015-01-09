__author__ = 'Kibur'

import sys
import random

class Dice:
    d20 = [
        [1, 7, 19, 17],
        [3, 2, 12, 18],
        [15, 5, 16, 10],
        [8, 4, 11, 13],
        [6, 9, 14, 20]
    ]

    d6 = [
        [1, 6, 2],
        [5, 3, 4]
    ]

    d4 = [
        [3, 4, 2],
        [4, 1, 2],
        [1, 3, 2],
        [3, 4, 1]
    ]

    d12 = [
        [1, 6, 5, 3, 2, 4],
        [12, 8, 7, 9, 11, 10]
    ]

    d8 = [
        [1, 3, 5, 7],
        [4, 6, 8, 2]
    ]

    d10 = [
        [1, 9, 5, 3, 7],
        [6, 2, 8, 0, 4]
    ]

    def __init__(self, sides=6):
        self.name = 'd6'
        self.dice = self.d6

        if sides is not 0 or sides is not 6:
            if sides is 20:
                self.name = 'd' + str(sides)
                self.dice = self.d20
            elif sides is 4:
                self.name = 'd' + str(sides)
                self.dice = self.d4
            elif sides is 12:
                self.name = 'd' + str(sides)
                self.dice = self.d12
            elif sides is 8:
                self.name = 'd' + str(sides)
                self.dice = self.d8
            elif sides is 10:
                self.name = 'd' + str(sides)
                self.dice = self.d10

    def roll(self):
        row = self.dice[random.randint(0, len(self.dice) - 1)]
        return row[random.randint(0, len(row) - 1)]

    def getName(self):
        return self.name

class UI:
	def __init__(self):
		if len(sys.argv) < 2:
			print 'Usage dice.py <dice>'
			sys.exit('More info --help')
		elif len(sys.argv) == 2:
			if sys.argv[1] == '--help':
				print 'Usage dice.py <dice>'
				sys.exit('List all available dices: --show-dices')
			elif sys.argv[1] == '--show-dices':
				print 'Available dices:'
				print 'd4, d6, d8, d10, d12, d20'
				print 'Example:'
				sys.exit('dice.py d20')
			else:
				arg = sys.argv[1]
				num = arg[1:]
				d = Dice(int(num))

				print 'You rolled %i with a %s' % (d.roll(), d.getName())
				sys.exit(0)

if __name__ == '__main__':
	ui = UI()
