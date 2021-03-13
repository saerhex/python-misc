def nrz(bitseq: list):
    res = [bit for bit in bitseq]
    return res


def nrzi(bitseq: list):
    res = []
    cur_val = 0
    for bit in bitseq:
        if bit == 1:
            cur_val ^= 1
        res.append(cur_val)
    return res


def enc_2b1q(bitseq: list):
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