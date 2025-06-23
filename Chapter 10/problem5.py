# Can you change the self parameter inside a class to something else(say "harry"). 
# Try changing self to "slf" or "harry" and see the effect.


'''  Output intact. just it's a god practise to write (self).'''

from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo    # changed self -> slf ''' output intact''' 

    def book(harry, fro, to):
        print(f"Ticket is booked in train no: {harry.trainNo} from {fro} to {to}")  #changed self to harry

    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time.")


    def getfare(self, fro, to):
        print(f"Ticket fare for train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(12399)

t.book("Rampur", "Delhi")
t.getstatus()
t.getfare("Rampur", "Delhi")
