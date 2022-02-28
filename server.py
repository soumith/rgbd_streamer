# saved as greeting-server.py
import Pyro4
import numpy as np
from data_compression import jpg_encode
Pyro4.config.SERIALIZER = "pickle"
Pyro4.config.SERIALIZERS_ACCEPTED.add("pickle")
Pyro4.config.PICKLE_PROTOCOL_VERSION=4

@Pyro4.expose
class RGBDStreamer(object):
    def get_rgb(self):
        return jpg_encode(np.zeros((640, 480, 3)))

if __name__ == "__main__":
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(RGBDStreamer)
    ns.register("RGBDStreamer", uri)
    
    print("Ready.")
    daemon.requestLoop()          
