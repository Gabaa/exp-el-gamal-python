import random


class Group:
    """Defines a q-order subgroup of the multiplicative group of integers modulo p."""

    def __init__(self, p: int, q: int):
        self.p = p
        self.q = q

    def find_generator(self):
        h = random.randrange(1, self.p)
        while True:
            g = pow(h, 2, self.p)
            if g != 1:
                break
        return g


class PublicKey:
    """Defines an El Gamal public key."""

    def __init__(self, alpha: int, beta: int):
        self.alpha = alpha
        self.beta = beta


class SecretKey:
    """Defines an El Gamal secret key."""

    def __init__(self, a: int):
        self.a = a


def key_gen(group: Group) -> "tuple[PublicKey, SecretKey]":
    alpha = group.find_generator()
    a = random.randrange(1, group.q)
    beta = pow(alpha, a, group.p)
    return PublicKey(alpha, beta), SecretKey(a)


def encrypt(group: Group, pk: PublicKey, message: int) -> "tuple[int, int]":
    r = random.randint(0, group.q - 1)
    return pow(pk.alpha, r, group.p), (pow(pk.beta, r, group.p) * message) % group.p


def decrypt(group: Group, sk: SecretKey, c: int, d: int) -> int:
    return (pow(c, -sk.a, group.p) * d) % group.p
