from random import randint as rdi


class Player():
    def __init__(self, name):
        if name == 'easy':
            self.name = 'Oswald'
        elif name == 'medium':
            self.name = 'Peter'
        elif name == 'hard':
            self.name = 'Simon'
        else:
            self.name = name

        self.score = 0
        self.turn = 0
        self.roll = 0
        self.last_roll = 0

    def take_turn(self):
        self.roll = rdi(1, 6)
        if self.roll == 1:
            self.last_roll = self.roll
            self.roll = 0
            self.turn = 0
            return 0
        else:
            self.turn += self.roll
            self.last_roll = self.roll
            self.roll = 0
            return self.last_roll

    def hold(self):
        self.score += self.turn
        self.turn = 0
