from enum import Enum



class Message(Enum):
    OK = 0
    ELECTION = 1
    CORDINATE = 2
    NOPE = 3



class Node:
    id = 0
    leaderID = 0
    def __init__(self, id):
        self.id = id
    

    def receive(self,receivedMessage):
        match receivedMessage[0]:
            case Message.OK:
                return (Message.NOPE, self.id)
            case Message.ELECTION:
               
                if receivedMessage[1] < self.id:
                    self.inform()
                    
                    return ( (Message.OK,self.id) )
        
                return (Message.NOPE, self.id)
            case Message.CORDINATE:
                print(receivedMessage)
                self.leaderID = receivedMessage[1]
        
                

    def inform(self):
        #for alle id'er højere end mig selv, send en election.
        answered = False
        for connection in connections[self.id+1:]:
            receivemes = connection.receive( (Message.ELECTION, self.id) )
            self.receive(receivemes)
            if receivemes[0] != Message.NOPE:
                answered = True
        if not answered:
            self.coordinate()
        
    def coordinate(self):
        for connection in connections:
            connection.receive((Message.CORDINATE, self.id))

connections = [Node(i) for i in range(10)]
    
def run():
    connections[4].receive( (Message.ELECTION, -1))


run()






