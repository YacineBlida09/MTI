# File: python/tp/tp6/ex1.py
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock: # thread wa7d y9dr y acceder l class en meme temps
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    def __copy__(self):
        raise Exception("mamnou3 copiage")
    def __deepcopy__(self, memo):
        raise Exception("mamnou3 copiage")


s1 = Singleton()
s2 = Singleton()
bool = s1 != s2
print(bool)