class Card:
    def __init__(self, value, suit) -> None:
        self.value = value
        self. suit = suit
    def __str__(self) -> str:
        value = self.value
        faceDict = {
            11 :'Jack',
            12 : 'Queen',
            13 : 'King',
            14 : 'Ace'
        }
        if value in faceDict:
            return f'{faceDict[value]} of {self.suit}'
        else:
            return f'{value} of {self.suit}'
        
    def __repr__(self):
        return str(self)
