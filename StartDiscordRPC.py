import rpc
import time
from time import mktime

from Layouts import LayoutRun


def StartDiscordRPC(displayDetail, displayState):
    client_id = '783396264431452190'
    rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)

    LayoutRun(displayDetail, displayState)

    time.sleep(5)
    start_time = mktime(time.localtime())
    while True:
        activity = {
            "state": displayState,
            "details": displayDetail,  # anything you like
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "ADZU🦅",  # anything you like
                "small_image": "adzu_bird",  # must match the image key
                "large_text": "Ateneo de Zoom University🦅",  # anything you like
                "large_image": "adzu"  # must match the image key
            }
        }
        rpc_obj.set_activity(activity)
        time.sleep(30)
