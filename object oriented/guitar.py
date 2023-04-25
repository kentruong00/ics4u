from random import choice

class Guitar:
    '''
    A class that represents an electric guitar 

    Attributes
        model: The model of the guitar, eg Stratocaster, Les Paul
        year: The year of the guitar
        colour: The colour or finish of the guitar, eg sea foam green, three tone sunburst
        tuned: Whether or not the guitar is in tune, True or False
        amp: The amp that the guitar is plugged into
    Methods:
    getModel, getYear, getColour, setTone, tune, plug, play
    '''
    def __init__(self, model, year, colour) -> None:
        self.__model = model 
        self.__year = year 
        self.__colour = colour 
        self.tuned = choice([True, False])
        self.amp = None 
    #Getter methods
    def getModel(self):
        return self.__model
    def getYear(self):
        return self.__year
    def getColour(self):
        return self.__colour
    # Base overrides
    def __str__(self) -> str:
        return f'A {self.__year} {self.__model} in {self.__colour}'
    def __repr__(self) -> str:
        return self.__str__()
    def tune(self): # Method to tune the guitar, if the guitar is already tuned, let the user know, and if the guitar is not tuned, the set tuned to True and tell the user.
        if self.tuned:
            print('The guitar is already tuned')
        else:
            self.tuned = True
            print('The guitar is now in tune')
    def plug(self, amp): # Method to plug into an amp, with an Amplifier object as the parameter. It sets the amp attribute to an Amplifier object and prints a string.
        self.amp = amp
        print(f'The guitar is now plugged into a(n) {amp.name}')

    def play(self): # A Method to play the guitar. The guitar is only playable if it is in tune and plugged into an amp. The method uses sound method from the amp class, and prints a string.
        if self.amp and self.tuned:
            sound = self.amp.sound()
            print(f'Played {self.__str__()} out of a {self.amp.name}. It sounds {sound[0]} and {sound[1]}')
        else:
            if not self.amp:
                print('Must be plugged in to play')
            if not self.tuned:
                print('Guitar must be in tune to play')


class Amp:
    '''
    A class that represents a guitar amplifier
    Attributes
        name: name and model of the amp
        gain: value of the amp's gain knob
        treble: value of the amp's treble knob
        bass: value of the amp's bass knob
    
    Methods
        sound
    '''
    def __init__(self, name, gain, treble, bass):
        self.name = name
        self.gain = gain
        self.treble = treble
        self.bass = bass
    #Base overrides for printing
    def __str__(self) -> str:
        return f'A {self.name} with gain set to {self.gain}, treble set to {self.treble} and bass set to {self.bass}.'
    def __repr__(self) -> str:
        return self.__str__()
    def sound(self): # Uses the gain, treble and bass parameters to define the sound of the guitar when played
        gain = ''
        tone = ''
        if self.gain > 6:
            gain = 'distorted'
        else:
            gain = 'clean'
        if self.treble > self.bass:
            tone = 'bright'
        elif self.treble == self.bass:
            tone = 'neutral'
        else: 
            tone = 'dark'
        return [gain, tone]

guitar1 = Guitar('Stratocaster', 1995, 'Three Tone Sunburst')
print(guitar1)
print(guitar1.getModel())
guitar1.tune()

amp1 = Amp('Vox 40', 7 , 8, 5)
print(amp1)
guitar1.plug(amp1)
guitar1.play()

amp1.gain = 5
amp1.treble = 4
print(amp1)
guitar1.play()