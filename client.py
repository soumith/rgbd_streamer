import time
import numpy as np
from data_compression import jpg_decode

import Pyro4
Pyro4.config.SERIALIZER = "pickle"
Pyro4.config.SERIALIZERS_ACCEPTED.add("pickle")
Pyro4.config.PICKLE_PROTOCOL_VERSION=2


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Pass in server device IP")
    parser.add_argument(
        "--ip",
        help="Server device (robot) IP",
        type=str,
        default="0.0.0.0",
    )

    args = parser.parse_args()

    
    bot = Pyro4.Proxy("PYRONAME:RGBDStreamer@" + args.ip)
    tm = time.time()
    rgb = jpg_decode(bot.get_rgb())
    print(time.time() - tm)
