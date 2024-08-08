class Hero:
    def __init__(self, phrase, clas, stats):
        self.phrase = phrase
        self.clas = clas
        self.stats = stats


class Swordsman(Hero):
    def speak(self):
        return self.phrase


    def pr_stats(self):
        return self.stats.items()


class Magician(Hero):
    def speak(self):
        return self.phrase


    def pr_stats(self):
        return self.stats.items()


#hero1 = Swordsman('i am swordsman and i am here', 'sword', {'stg': 10, 'dxt': 4, 'itl': 1})
#hero2 = Magician('magic... mAgIc.. MAGIC!!!', 'magic', {'stg': 1, 'dxt': 6, 'itl': 10})
#print(hero1.pr_stats())
