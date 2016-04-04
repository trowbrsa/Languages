class Spaceship:

    def __init__(self):
        self.thirst = 50
        self.work = 50
        self.horde = 50
        self.hunger = 50
        self.receipts = 50
        self.stable = True
        self.total = 0

    def drink(self):
        self.thirst -= 10
        self.work += 2

    def deliver(self):
        self.work += 8
        self.receipts += 4

    def steal(self):
        self.horde += 10
        self.work += 7

    def eat(self):
        self.hunger -= 10
        self.work += 2

    def account(self):
        self.receipts -= 10
        self.horde -= 10

    def score(self):
        if self.thirst < 60:
            self.total += 7
        elif self.thirst >= 60:
            self.total -= 7

        if self.work < 70:
            self.total += 1
        elif self.work >= 70:
            self.total -= 1

        if self.horde > 80:
            self.total += 5
        elif self.horde <= 80:
            self.total -= 1

        if self.receipts > 70:
            self.total += 3
        elif self.receipts <= 70:
            self.total -= 3

        return self.total

    def stable(self):
        if any( [self.thirst > 99, self.work > 99, self.horde < 1, self.hunger > 99, self.receipts < 1] ):
            return False
        else:
            return True

    def check(self):
        self.alert()
        if self.stable:
            return True
        else:
            return False
            print "You lose! Try again!"

    def alert(self):
        if any( [self.thirst > 60, self.work > 60, self.horde > 60, self.hunger > 60, self.receipts > 60] ):
            print "Uh oh! Your ship is about to sink. Here's your current status of the boat. Remember, if any value reaches 100, you're DOOMED!"
            self.thirst
            print "Current thirst level: "
            print self.thirst
            print "Current work level:"
            print self.work
            print "Current hording level: "
            print self.horde
            print "Current hunger level: "
            print self.hunger
            print "Current receipt level: "
            print self.receipts

def playGame():
    ship = Spaceship()

playGame
