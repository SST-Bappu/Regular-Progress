class Robot:
    def __init__(self,givenName,givenColor,givenWeight): #Constructor
        self.name= givenName
        self.color=givenColor
        self.weight=givenWeight
    def introduce_self(self):
        print(f"My name is {self.name}")
class person:
    def __init__(self,n,p,i):
        self.name= n
        self.personality=p
        self.is_sitting=i
    def sit_down(self):
        self.is_sitting=True
    def stand_up(self):
        self.is_sitting=False

if __name__=="__main__":
    '''r1 = Robot()
    r1.name="Tom"
    r1.color="Red"
    r1.weight=30
    r1.introduce_self()'''
    r1=Robot("Tom","Red",30)
    r2=Robot("Jerry","Blue",50)
    r1.introduce_self()
    r2.introduce_self()

    p1 = person("Rahim","Aggressive",False)
    p2 = person("Karim","Talkative",True)
    p1.robot_owned=r1
    p2.robot_owned=r2
    p1.robot_owned.introduce_self()
    p2.robot_owned.introduce_self()

