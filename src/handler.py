import os
import time
from typing import Any

import runpod  # type: ignore

sleep_time = int(os.environ.get("SLEEP_TIME", 3))


# load your model(s) into vram here


def handler(event: Any) -> str:
    print(event)
    time_slept = 0
    while time_slept < sleep_time:
        print("working, I promise")
        time_slept += 1
        time.sleep(1)
    # do the things

    return "Hello World"


runpod.serverless.start({"handler": handler})
