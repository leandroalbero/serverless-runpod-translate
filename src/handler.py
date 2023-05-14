from typing import Any

import runpod  # type: ignore
from easynmt import EasyNMT  # type: ignore

model = EasyNMT("opus-mt")


def handler(event: Any) -> dict:
    src_lang = event["input"]["src_lang"] if "src_lang" in event["input"] else "es"
    target_lang = (
        event["input"]["target_lang"] if "target_lang" in event["input"] else "en"
    )
    translated = model.translate(
        event["input"]["input_text"], target_lang=target_lang, source_lang=src_lang
    )
    return {
        "result": translated,
        "debug": model.device,
    }


runpod.serverless.start({"handler": handler})
