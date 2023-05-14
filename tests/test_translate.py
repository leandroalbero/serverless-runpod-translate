import pytest as pytest
from easynmt import EasyNMT  # type: ignore

model = EasyNMT("opus-mt")


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("Hola, cómo estás?", ["Hey, how are you?", "Hello, how are you?"]),
    ],
)
def test_translate_es_en(input_text: str, expected: list[str]) -> None:
    assert model.translate(input_text, target_lang="en") in expected
