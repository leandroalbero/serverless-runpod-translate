from typing import Any

import runpod  # type: ignore

# load your model(s) into vram here
from easynmt import EasyNMT  # type: ignore

model = EasyNMT("opus-mt")


def handler(event: Any) -> str:
    return model.translate(event["input"]["input_text"], target_lang="en")


runpod.serverless.start({"handler": handler})
