#!/usr/bin/env python3

import asyncio
import http.client
import sys
import json
import urllib.request
import urllib.parse

from pprint import pprint


def do_headers(**kwargs):
    _headers = {"User-Agent": "MozillaMozilla! x64"}
    if kwargs:
        for k, v in kwargs.items():
            if "_" in k:
                k = k.replace("_", "-")
            _headers.update({k: v})
    return _headers


async def get_caller(
    url: str,
    method: str = "GET",
    headers: dict = None,
    query_params: dict = None,
    **kwargs,
):

    if not method.casefold() in {"get", "head"}:
        raise SystemExit("...wat")

    if not headers:
        headers = do_headers()

    if query_params:
        use_params = urllib.parse.urlencode(query_params)
    else:
        use_params = None

    request = urllib.request.Request(url=url, headers=headers, method=method, **kwargs)
    try:
        with urllib.request.urlopen(request, timeout=10) as r:
            response = r.read().decode("utf-8")
            return json.loads(response)
    except urllib.error.HTTPError as err:
        print(f"Error: {err.status} -- {err.reason}")
    except urllib.error.URLError as err:
        print(f"Error: {err}")
    except http.client.RemoteDisconnected as wtf:
        print(f"Error: {wtf}")
    except TimeoutError:
        print("Request timed out")
    return


async def dancedance(us: list):
    for i, u in enumerate(us):
        response = await get_caller(u)
        print(i, response)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        asyncio.run(dancedance(sys.argv[1:]))
    else:
        print("urls expected")
