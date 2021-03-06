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

    def thirst_level(self):
        if self.thirst < 50:
            self.total += 7
        elif self.thirst >= 60:
            self.total -= 7

    def horde_level(self):
        if self.horde > 80:
            self.total += 5
        elif self.horde <= 80:
            self.total -= 1

    def work_level(self):
        if self.work < 70:
            self.total += 1
        elif self.work >= 70:
            self.total -= 1

    def hunger_level(self):
        if self.hunger > 60:
            self.total -= 1
        elif self.hunger <= 60:
            self.total -= 1

    def receipt_level(self):
        if self.receipts > 70:
            self.total += 3
        elif self.receipts <= 70:
            self.total -= 3

    def total_score(self):
        self.thirst_level
        self.horde_level
        self.work_level
        self.receipt_level
        self.hunger_level
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
        if any( [self.thirst > 90, self.work > 90, self.horde > 90, self.hunger > 90, self.receipts > 90] ):
            print "Uh oh! Your ship is about to sink. Here's what you need to watch out for. Remember, if any value reaches 100, you're DOOMED!"
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
    game = Spaceship()

    print "All Aboard the Planet Express!"
    print "What would you like to do?"
    print "Keep track of your score by typing \"score\" at any time."
    print "You can also type 'bye' at any time to leave this game :(."

    stop = False

    while stop != True:
        print "What would you like to do aboard the ship?"
        action = raw_input("You can type 'eat', 'drink', 'accounting', 'deliver', or 'steal'. ")
        if action == "bye":
            stop = True
            print "Laterz."
        else:
            if action == "eat":
                game.eat()
                print "You ate something! Your belly is fuller, but it required work!"
            elif action == "drink":
                game.drink()
                print "You drank something! You're less thirsty, but it required some work!"
            elif action == "accounting":
                game.account()
                print "You did some accounting! Boring! That was a lot of work!"
            elif action == "deliver":
                print "You did some work for once! That required some work!"
            elif action == "steal":
                game.steal()
                print "You stole some stuff! That's awkward."
            elif action == "score":
                print "Your total score is: "
                print game.total_score()
            else:
                "I don't understand that command! Try again!"
        game.check()

playGame()
