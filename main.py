import random
import elgamal
import expelgamal


def main():
    test_exp_el_gamal_homomorphism()


def test_exp_el_gamal_homomorphism():
    group = elgamal.Group(1907, 953)
    pk, sk = expelgamal.key_gen(group)

    m1 = random.randint(0, 1)
    (c1, d1) = expelgamal.encrypt(group, pk, m1)
    m2 = random.randint(0, 1)
    (c2, d2) = expelgamal.encrypt(group, pk, m2)
    print(f"m1 = {m1}")
    print(f"m2 = {m2}")

    c, d = (c1 * c2) % group.p, (d1 * d2) % group.p

    dec = elgamal.decrypt(group, sk, c, d)

    if dec == 1:
        print("0 and 0")
    elif dec == pk.g:
        print("1 and 0 or 0 and 1")
    else:
        print("1 and 1")


def test_enc_dec(msg):
    group = elgamal.Group(1907, 953)
    pk, sk = elgamal.key_gen(group)
    enc = elgamal.encrypt(group, pk, msg)
    dec = elgamal.decrypt(group, sk, *enc)
    assert dec == msg, f"Got {dec}, expected {msg}"


if __name__ == "__main__":
    main()
