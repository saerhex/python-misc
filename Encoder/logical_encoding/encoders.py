def nrz(bitseq: list) -> list:
    """
    Simple encoding method. Zero means low-level voltage,
    One means high-level voltage.

    :param bitseq: list of bits to be encoded.
    :return: list of encoded bits.
    """
    res = [bit for bit in bitseq]
    return res


def nrzi(bitseq: list) -> list:
    """
    NRZI encoding method.
    Iterate throw all bit sequence and if 1 occures - reverse
    current value of bits, for example, 1 reverse to 0, 0 to 1 etc.

    :param bitseq: list of bits to be encoded.
    :return: list of encoded bits.
    """
    res = []
    cur_val = 0
    for bit in bitseq:
        if bit == 1:
            cur_val ^= 1
        res.append(cur_val)
    return res


def enc_2b1q(bitseq: list):
    """
    2B1Q encoding method.
    Every 2 bits of sequence refer to specific value in this Quaternary table:
    ___________
    | 00 | -3 |
    |____|____|
    | 01 | -1 |
    |____|____|
    | 11 |  1 |
    |____|____|
    | 10 |  3 |
    |____|____|

    :param bitseq: list of bits to be encoded.
    :return: list of encoded bits.
    """
    res = []
    quadras = {
        "00": -3,
        "01": -1,
        "11": 1,
        "10": 3,
    }
    doubles = [bitseq[i * 2:i*2 + 2] for i in range(len(bitseq)//2)]
    for double in doubles:
        str_double = ''.join(map(str, double))
        val = quadras.get(str_double)
        res.extend([val, val])
    return res