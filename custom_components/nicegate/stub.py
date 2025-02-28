import asyncio
import xml.etree.ElementTree as ET

import requests
from requests.auth import HTTPBasicAuth

from custom_components.nicegate import NiceGateApi

def callback(val):
    print(f"callback: {val}")

def sync_wait(future):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(future)


def main():
    nice = NiceGateApi('192.168.0.29', '00:0B:6C:73:E3:46', 'hass_nicegate', None)
    nice.set_update_callback(callback)
    pwd = sync_wait(nice.pair('001-63-622'))
    print(f"paring: {pwd}")
    if pwd is not None:
        # nice.setPassword(pwd)
        nice = NiceGateApi('192.168.0.29', '00:0B:6C:73:E3:46', 'hass_nicegate', pwd)
        print(f"Connected: {sync_wait(nice.connect())}")
        # print(f"Check: {sync_wait(nice.verify_connect())}")

        print (f"Info: {sync_wait(nice.info())}")
        sync_wait(nice.disconnect())

if __name__ == "__main__":
    main()