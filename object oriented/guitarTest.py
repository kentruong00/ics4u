from guitar import Guitar
from guitar import Amp

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