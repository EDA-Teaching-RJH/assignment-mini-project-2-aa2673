class Archetypes:
    def __init__(self,name,off,vit,agl):
        self.name = name
        self.off = off
        self.vit = vit
        self.agl = agl

class Barbarian(Archetypes):
    def __init__(self,name,off,vit,agl):
        super().__init__(name, off=15, vit=5, agl = agl)
        self.classAbility = "Undying Fury"

class Rogue(Archetypes):
    def __init__(self,name,off,vit,agl):
        super().__init__(name, off=5, vit = vit, agl=15)
        self.classAbility = "Flash Step"


class Tank(Archetypes):
    def __init__(self,name,off,vit,agl):
        super().__init__(name, off=5, vit=15, agl=agl)
        self.classAbility = "Iron Physique"
        



    