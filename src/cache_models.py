'''
Fetches and caches the NMT models
'''

from easynmt import EasyNMT


def get_models():
    model = EasyNMT('mbart50_m2en')
    model.translate("traduccion para que haga cache", target_lang='en')

    return model


if __name__ == "__main__":
    get_models()
