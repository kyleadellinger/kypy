#!/usr/bin/env python3

import shlex
import subprocess
import sys

def run_subprocess(cmd, *args, **kwargs) -> None:
    """
    run subprocess wrapper
    """
    if isinstance(cmd, str):
        cmd = shlex.split(cmd)
    elif isinstance(cmd, list):
        pass
    else:
        raise SystemExit("Invalid command provided")

    try:
        _timeout = kwargs.pop("timeout")
    except KeyError:
        _timeout = 15

    proc = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=_timeout,
        *args,
        **kwargs,
    )

    if proc.returncode != 0:
        print(
            f"Warning: unexpected exit code: {proc.returncode}: cmd: {cmd}")
    return

def _main():
    #import argparse
    from shutil import which

    

    #parser = argparse.ArgumentParser()
    #parser.add_argument("cmd", help="Run arbitrary command")

    #args = parser.parse_args()
    #print(vars(args))


if __name__ == "__main__":
    _main()