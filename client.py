import zmq # import ZeroMQ

def main():
    # set up the context so we can create sockets
    context = zmq.Context()

    # set up the socket to recieve messages, REQ is the request socket
    socket = context.socket(zmq.REQ)

    # connect to the same localhost at the server
    socket.connect("tcp://localhost:5100")

    # send the correct string
    socket.send_string("This is a message from CS361")

    # Get the reply from the server
    message = socket.recv()

    # Print the message that was sent back
    print(f"Server sent back: {message.decode()}")

if __name__ == "__main__":
    main()