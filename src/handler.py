from typing import Any

import runpod  # type: ignore
from easynmt import EasyNMT  # type: ignore

model = EasyNMT("mbart50_m2en")


def handler(event: Any) -> str:
    src_lang = event["input"]["src_lang"] if "src_lang" in event["input"] else None
    target_lang = (
        event["input"]["target_lang"] if "target_lang" in event["input"] else "en"
    )

    return model.translate(
        event["input"]["input_text"], target_lang=target_lang, source_lang=src_lang
    )


runpod.serverless.start({"handler": handler})
