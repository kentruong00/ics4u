from cat import Cat
from cat import ScratchPost

post = ScratchPost()
cat1 = Cat('Timothy', 'Bengal', 'orange')
print(cat1)
if cat1.wantToScratch:
    cat1.scratch(post)
