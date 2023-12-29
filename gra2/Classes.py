class Enemy:
    def __init__(self, name, hitPoints, attack, defence, expDrop):
        self.name = name;
        self.hitPoints = hitPoints;
        self.attack = attack;
        self.defence = defence;
        self.expDrop = expDrop;

class Character:
    def __init__(self,name, hitPoints, attack, defence, level,exp):
        self.name = name;
        self.hitPoints = hitPoints;
        self.attack = attack;
        self.defence = defence;
        self.level =  level;
        self.exp = exp;

class Location:
    name: str = "newName";
    enemyId: int = [];



