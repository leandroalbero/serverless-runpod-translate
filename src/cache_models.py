"""
Fetches and caches the NMT models
"""

from easynmt import EasyNMT


def get_models():
    model = EasyNMT("m2m_100_418m")

    # Translate so it downloads the models
    model.translate("a", source_lang="es", target_lang="en")
    model.translate("a", source_lang="fr", target_lang="en")
    model.translate("a", source_lang="pt", target_lang="en")

    return model


if __name__ == "__main__":
    get_models()
