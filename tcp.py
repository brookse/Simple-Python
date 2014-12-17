# coding=utf-8
# cs2910-lab02-brookse.farrowc.py Lab 2 -- UDP/TCP send/receive
# Team members: Lyzzi Brooks (brookse), Chris Farrow (farrowc)

# import the "socket" module -- not using "from socket import *" in order to selectively use items with "socket." prefix
import socket;
import time;

# Port number definitions
# (May have to be adjusted if they collide with ports in use by other programs/services.)
UDP_PORT = 12000
TCP_PORT = 12100

# Host address when acting as "receiver" ("server").
# The address '' means accept any connection for our "receive" port from any network interface
# on this system (including 'localhost' loopback connection).
LISTEN_FOR_HOST = ''

# Address of the "other" ("server") host that should be connected to for "send" operations.
# When connecting on one system, use 'localhost'
OTHER_HOST = '155.92.64.179'
# When "sending" to another system, use its IP address (or DNS name if there it has one)
#OTHER_HOST = '155.92.x.x'
	
def main():
	# Get chosen operation from the user.
	action = raw_input('Select "(1-TS) tcpsend", or "(2-TR) tcpreceive":')
	# Execute the chosen operation.
	if action in ['1','TS','ts','tcpsend']:
		tcp_send(OTHER_HOST,TCP_PORT,'TCP test message');
	elif action in ['2','TR','tr','tcpreceive']:
		tcp_receive(TCP_PORT);
	else:
		print "Unknown action: '{0}'".format(action)

# Send a TCP message to a designated host/port.
# Receive a one-character response from the "server".
# Print the received response.
# Close the socket
# Return
# Written by Chris Farrow
def tcp_send(server_host,server_port,message):
	print "tcp_send: dst_host='{0}', dst_port={1}, message='{2}'".format(server_host,server_port,message)
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect((server_host,server_port))

	# Send a TCP message to a designated host/port.
	sock.send(message)

	# Receive a one-character response from the "server".
	received_message = sock.recv(4096)

	# Print the received response.
	print(received_message)

	# Close the socket
	sock.close()

# Listen for a TCP connection on a designated "listening" port
# Accept the connection, creating a connection socket
# Print the address and port of the sender
# Receive the message string (one "socket.recv" call is sufficient for now)
# Print the message length and message string
# Send a single-character response (e.g., "Y") back to the sender
# Close the connection socket
# Close the listening socket
# Return
# Written by Lyzzi Brooks
def tcp_receive(listen_port):
	print "tcp_receive (server): listen_port={0}".format(listen_port)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Listen for a TCP connection on a designated "listening" port
	sock.bind(("0.0.0.0", TCP_PORT))
	print "bound"
	sock.listen(1)
	# Accept the connection, creating a connection socket
	connection, addr = sock.accept()
	# Print the address and port of the sender
	print "Address: ", addr
	# Receive the message string (one "socket.recv" call is sufficient for now)
	end = "x"
	message = ""
	while(end != "Q"):
		end = connection.recv(1)
		print end
		message += end
		time.sleep(.01)
	
	# Print the message length and message string
	print "Message: ", message, " | Message length: ", len(message)
	# Send a single-character response (e.g., "Y") back to the sender
	connection.send("O")
	# Close the connection socket
	connection.close()
	# Close the listening socket
	sock.close()
	# Return
	return

# Invoke the main method to run the program.	
main()

####################################################################################
# Comments
# Functionality: On the receive side, we opened a socket based on the TCP port. 
#   After listening on that, we waited for a message from the sender, accepted 
#	and printed that message, and then sent a return message back.
#	On the send side, we opened a socket, listened to the receiving socket, sent
#	a message, and then received a message back from the receiver.
# Results of testing: We were able to see both messages sent in Wireshark, 
#	specifically we could see our actual message contents in the packet.
# Comments on experience: We really didn't have any issues besides realizing we
#	had to create an instance of a socket instead of using just socket. We also
#	realized we had to create a connection socket in order to receive from and send 
#	a message back to the sender.
####################################################################################