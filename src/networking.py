# py udp tutorial: https://www.binarytides.com/programming-udp-sockets-in-python/
# socket documentation: https://docs.python.org/3/library/socket.html
# socket broadcast tutorial: https://en.ittrip.xyz/python/python-udp-broadcast
# strother's udp: https://github.com/jstrother123/photon-main/tree/main/udp_files

import socket

class NetworkingManager():
    BROADCAST_PORT = 7500
    RECV_PORT = 7501
    LOCAL_ADDRESS = "127.0.0.1"
    BROADCAST_ADDRESS = "127.0.0.1"

    def __init__(self, gameState):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.s.bind((self.LOCAL_ADDRESS, self.RECV_PORT))
        self.gameEndCount = 0
        self.gameState = gameState

    def send_broadcast(self, msg):
        self.s.sendto(str.encode(msg), (self.BROADCAST_ADDRESS, self.BROADCAST_PORT))



    def tick(self):
        if self.gameState["stage"] == "starting":
            self.send_broadcast("202")
            self.gameEndCount = 0
        elif gameState["stage"] == "finished" and self.gameEndCount < 3:
            self.send_broadcast("221")
            self.gameEndCount += 1
        else:
            data, addr = self.s.recvfrom(1024) # check how this function actually returns data, cause it might be a problem depending on how it works.

            data = data.split(":")
            sendingEquipID = data[0]
            hitEquipID = data[1]
            if hitEquipID == "53" or hitEquipID == "43":
                pass
                # todo: deal with bases
            elif sendingEquipID.team == hitEquipID.team: # todo figure out actually where team data will be located and grab it from there.
                self.send_broadcast(sendingEquipID)
            else:
                self.send_broadcast(hitEquipID)

