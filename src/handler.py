from typing import Any
from time import time

import runpod  # type: ignore
from easynmt import EasyNMT  # type: ignore

model = EasyNMT("m2m_100_418m")


def handler(event: Any) -> dict:
    start_time = time()
    src_lang = event["input"]["src_lang"] if "src_lang" in event["input"] else None
    target_lang = (
        event["input"]["target_lang"] if "target_lang" in event["input"] else "en"
    )

    translated_text = model.translate(
        event["input"]["input_text"], target_lang=target_lang, source_lang=src_lang
    )

    translation_time = time() - start_time
    print(f"Translated in {translation_time} seconds")

    return {
        "translated_text": translated_text,
        "translation_time": translation_time,
    }


runpod.serverless.start({"handler": handler})
