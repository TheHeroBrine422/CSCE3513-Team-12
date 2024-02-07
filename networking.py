# This is just a workspace for caleb to mess around with udp in python
# generally i am just trying to write some rough pseudoish code for what the networking should look like in the final product.
# none of this has actually been tested yet and will be done in the future.
# py udp tutorial: https://www.binarytides.com/programming-udp-sockets-in-python/
# socket documentation: https://docs.python.org/3/library/socket.html
# socket broadcast tutorial: https://en.ittrip.xyz/python/python-udp-broadcast

import socket

BROADCAST_PORT = 7500
RECV_PORT = 7501

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(("", RECV_PORT))

def send_broadcast(msg):
	s.sendto(msg, ("255.255.255.255", BROADCAST_PORT))

gameEndCount = 0

gameState = "starting"

while True:
    data, addr = s.recvfrom(1024)
    if gameState == "starting":
        send_broadcast("202")
        gameEndCount = 0
        gameState = "inprogress"
    elif gameState == "finished" and gameEndCount < 3:
        send_broadcast("221")
        gameEndCount += 1
    else:
        # still need to deal with red and blue team bases. not entirely sure how their data will look like.
        data = data.split(":")
        sendingEquipID = data[0]
        hitEquipID = data[1]
        if sendingEquipID.team == hitEquipID.team:
            send_broadcast(sendingEquipID)
        else:
             send_broadcast(hitEquipID)
