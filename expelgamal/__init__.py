import elgamal


class PublicKey:
    def __init__(self, pk: elgamal.PublicKey, g: int) -> None:
        self.inner_pk = pk
        self.g = g


def key_gen(group: elgamal.Group):
    pk, sk = elgamal.key_gen(group)
    g = group.find_generator()
    return PublicKey(pk, g), sk


def encrypt(group: elgamal.Group, pk: PublicKey, message: int) -> "tuple[int, int]":
    assert message.bit_length() <= 1
    m = pow(pk.g, message, group.p)
    return elgamal.encrypt(group, pk.inner_pk, m)


def decrypt(group: elgamal.Group, sk: elgamal.SecretKey, c: int, d: int) -> int:
    m = elgamal.decrypt(group, sk, c, d)
    return 0 if m == 1 else 1
