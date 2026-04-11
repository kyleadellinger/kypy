#!/usr/bin/env python3

import argparse
import socket
import sys

from pathlib import Path

def tcp_sockerman(host: str, port: int, msg: str):
    if msg.endswith("\n"):
        pass
    else:
        msg = msg + "\n"
    bmsg = bytes(msg, "utf-8")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(bmsg)
            response = s.recv(4096)
            r = response.decode("utf-8")
        return f"Responding: {host} says -> : {r}"
    except KeyboardInterrupt:
        sys.exit(0)        
    except ConnectionRefusedError:
        print("Remote connection refused")
        sys.exit(0)
    except TimeoutError:
        print("Connection timeout")
        sys.exit(0)
    except socket.gaierror as se:
        sys.exit(se)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="sockit")
    parser.add_argument("target_host", help="Target Host")
    parser.add_argument("-p", "--port", help="Override port. Default 9002", default="9002")
    parser.add_argument("-m", "--message", help="Override message. Default is 'GET QUEUE LENGTH\\n'", default="GET QUEUE LENGTH\n")

    args = parser.parse_args()
    pint = int(args.port)
    targets = args.target_host.split(",")    

    for t in targets:
        print(tcp_sockerman(t, pint, args.message))
