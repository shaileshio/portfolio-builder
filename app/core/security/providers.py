from .hashing import Argon2Hasher


def get_hasher() -> Argon2Hasher:
    return Argon2Hasher()
