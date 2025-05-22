import time
import zmq # import ZeroMQ

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
        ClientMessage = socket.recv()

        # define the message we want to send and recieve
        Message = "This is a message from CS361"

        # print the message recieved from the client
        print(f"Message from client: {ClientMessage.decode()}")

        # if the server recieves the correct message, send it back and break the while loop
        if ClientMessage.decode() == Message:
            print(f"Sending back: {Message}")
            socket.send_string(Message)
            break

        time.sleep(2) #let the program rest for a few senonds if it has not recieved the correct message

    # destroy context and exit the program
    context.destroy()

if __name__ == "__main__":
    main()