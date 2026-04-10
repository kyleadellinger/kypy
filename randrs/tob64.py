#!/usr/bin/env python3

import base64
import fileinput
import getpass
import sys

def passwords(s: str=None):
    if s:
        p = s
    else:
        p = getpass.getpass("Enter value to be converted to base64: ")

    bp = bytes(p, "utf-8")
    encoded_pass = base64.b64encode(bp)

    return encoded_pass.decode("utf-8")


if __name__ == "__main__":
    try:
        print(passwords())
    except KeyboardInterrupt:
        sys.exit("\nKeyboard interrupt detected.\n")

