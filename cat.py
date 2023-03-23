from random import choice

class Cat:
    def __init__(self, name, breed, colour): # self is a keyboard to reference the class that you are working
        self.name = name
        self.breed = breed
        self.colour = colour
        # created three attributes and assigned them to the arguments from the __init__ method
        self.isHungry = choice([True, False])
        self.wantToScratch = choice([True, False])
        self.fat = False
    def __str__(self):
        return f'{self.name} is a(n) {self.colour} {self.breed} cat'
    def hungryCheck(self):
        if self.isHungry:
            print(f'{self.name} is starving to death')
        else:
            print(f'{self.name} could probably go another few days')
    def eat(self, foodName):
        if self.isHungry:
            print(f'{self.name} ate {foodName}')
            print(f'{self.name} won\'t die now!!!! W cat owner!!!')
            self.isHungry = False
        else:
            print(f'{self.name} ate {foodName}')
            print(f'{self.name} is now fat as fuck')
            self.fat = True
    def starve(self):
        print(f'{self.name} is now starving to death')
        self.isHungry = True
    def vehicularManslaughter(self, vehicle):
        if choice([True, False]):
            print(f'{self.name} was hit by a(n) {vehicle}')
        else:
            print(f'{vehicle} nearly missed {self.name}')
    def scratch(self, post):
        if self.wantToScratch:
            post.use()
            print(f'{self.name} scratched {post}')

class ScratchPost:
    def __init__(self): # if 
        self.health = 10
    def __str__(self):
        return f'a scratching post, {self.health} health remaining'
    def use(self):
        if self.health <= 0:
            print('the scratch post is broken')
            return False
        else:
            self.health -= 1
            return True
        