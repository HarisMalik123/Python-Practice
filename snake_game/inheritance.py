
class Human:
    def __init__(self):
        self.eyes=2
        
    def speak(self):
        print("Speaking")


class MetaHuman(Human):
    def __init__(self):
        super().__init__()
        self.power=100
    def speak(self):
        print("Meta Human can not speak")
        return super().speak()

metu=MetaHuman()

metu.speak()