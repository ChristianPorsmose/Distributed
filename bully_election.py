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
        if receivedMessage[0] == Message.CORDINATE:
            return (Message.NOPE, self.id)
        
        match receivedMessage[0]:
            case Message.OK:
                return (Message.NOPE, self.id)
            case Message.ELECTION:
                print(receivedMessage)
                if receivedMessage[1] < self.id:
                    self.inform()
                    self.respond(receivedMessage[1])
                return (Message.NOPE, self.id)
            case Message.CORDINATE:
                print(receivedMessage[1])
                self.leaderID = receivedMessage[1]
                

    def inform(self):
        #for alle id'er højere end mig selv, send en election.
        for connection in connections[self.id:]:
            receivemes = connection.receive( (Message.ELECTION, self.id) )
            if receivemes[0] != Message.NOPE:
                return
        self.coordinate()


    def respond(self,id ):
        connections[id].receive( (Message.OK, self.id))
        
    def coordinate(self):
        for connection in connections:
            connection.receive((Message.CORDINATE, self.id))

connections = [Node(i) for i in range(10)]
    
def run():
    connections[4].receive( (Message.ELECTION, -1))


run()






