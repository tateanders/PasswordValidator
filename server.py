import time
import zmq # import ZeroMQ

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Create an array (list) of users
users = [
    User("alice", "P@ssw0rd123"),
    User("bob", "helloWorld!"),
    User("carol", "secure*456"),
    User("dave", "admin2024!"),
    User("eve", "myPassword$"),
    User("frank", "Qwerty#789"),
    User("grace", "Summer2025!"),
    User("heidi", "LetMeIn@1"),
    User("ivan", "Dragon$Rider"),
    User("judy", "ILovePython3"),
    User("mallory", "N0Access!"),
    User("oscar", "BlueSky#42"),
    User("peggy", "CoffeeTime!"),
    User("trent", "ToTheMoon99"),
    User("victor", "H@ckMeIfYouCan"),
    User("wendy", "1234Secure!"),
    User("yasmine", "Night0wl$"),
    User("zach", "ButterFly88"),
    User("nina", "OpenSesame@"),
    User("leo", "Pa$$word2025")
]

def main():

    # set up the context so we can create sockets
    context = zmq.Context()

    # set up the socket to recieve messages, REP is the reply socket
    socket = context.socket(zmq.REP)

    # address to listed from and send to
    socket.bind("tcp://*:5100")

    # run the program until it recieves the correct message
    while True:
        # set this variable to whatever the server recieves from the client
        parts = socket.recv_multipart()
        username = parts[0].decode()
        password = parts[1].decode()
        wasGood = 0

        # if the server recieves the correct message, send it back and break the while loop
        for user in users:
            if user.username == username and user.password == password:
                socket.send_string("valid")
                wasGood = 1
        if wasGood == 0:
            socket.send_string("invalid")

        time.sleep(2) #let the program rest for a few senonds if it has not recieved the correct message

        # destroy context and exit the program
        context.destroy()

if __name__ == "__main__":
    main()
