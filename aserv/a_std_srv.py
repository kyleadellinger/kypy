#!/usr/bin/env python3

import asyncio


async def handle_echo(reader, writer):
    """simple socket echo handler"""
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info("peername")
    print(f"{message = } - {addr = }")

    writer.write(data)
    await writer.drain()

    writer.close()
    await writer.wait_closed()


async def srv_main(handler_func, listen_ip, listen_port):
    server = await asyncio.start_server(handler_func, listen_ip, listen_port)

    # addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)

    async with server:
        await server.serve_forever()


def run(handler, ipaddr, port):
    asyncio.run(srv_main(handler_func=handler, listen_ip=ipaddr, listen_port=port))


if __name__ == "__main__":
    #    asyncio.run(main())
    try:
        run(handler=handle_echo, ipaddr="0.0.0.0", port=8888)
    except KeyboardInterrupt:
        pass
