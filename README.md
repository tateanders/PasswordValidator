# PasswordValidator
# Requesting Data
To request data all you have to do is connect to the ZMQ socket at "tcp://localhost:5100"
and then send a username and password like this in python:
socket.send_multipart([username.encode(), password.encode()])
# Recieving Data
To recieve data you just set up a python line like this:
message = socket.recv()
The microservide will return "valid" if the username and password exists and "invalid" if it does not.
