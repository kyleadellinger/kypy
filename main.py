#!/usr/bin/env python3

import argparse

import aserv

def prog_entry():
    parser = argparse.ArgumentParser(prog="kypy")
    parser.add_argument("-d", "--debug", help="Enable arbitrary debug printing", action="store_true", default=False)

    subcommands = parser.add_subparsers(help="subcommand help", dest="subcommand")

    passer = subcommands.add_parser("kpass", help="Prompt/obtain secrets")
    passer.add_argument("-p", "--prompt", help="Override default prompt", default="Secret: ")
    passer.add_argument("-n", "--no-newline", help="Don't include a newline character with provided secret. May not actually be necessary anyway", action="store_true", default=False)

    asocks = subcommands.add_parser("asock", help="Async sockets things")
    asocks.add_argument("subc", choices=("serve", "client"))
    asocks.add_argument("-p", "--port", help="Listen port on 'serve'; Target port on 'client'", type=int, default=8888)
    asocks.add_argument("-i", "--ip", help="Listen IP on 'serve'; Target IP on 'client'", default="0.0.0.0")

    args = parser.parse_args()

    def debug_printer(x) -> None:
        """learn decorators though"""
        if args.debug:
            print("Info Print: ", x)

    debug_printer(vars(args))

    match args.subcommand:
        case "asock":
            if args.subc == "serve":
                debug_printer(f"start async server -> {args.ip = } | {args.port = }") # note: do validation
                try:
                    aserv.main(handler=aserv.handle_echo, ipaddr=args.ip, port=args.port)
                except KeyboardInterrupt:
                    return
        case "passer":


        case _:
            parser.print_usage()
            return 11

if __name__ == "__main__":
    prog_entry()
    
