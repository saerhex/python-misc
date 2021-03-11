from __future__ import annotations

from typing import Callable

import matplotlib.pyplot as plt
import numpy as np


X = np.arange(32)


class Encoder:

    def __init__(self, string, encoding_method=None):
        self.string = string
        self.bitseq = self.get_bits()
        if encoding_method:
            self.encoding_method = encoding_method
        else:
            self.encoding_method = nrz

    def get_bits(self):
        codes = (format(enc, '8b') for enc in self.string.encode('cp1251'))
        return list(map(int, ''.join(codes)))

    def encode_seq(self):
        return self.encoding_method(self.bitseq)


class Plotter:

    def show_plot(self, bits: list, base_bits: list):
        plt.figure(pltsize=(10, 2))
        plt.step(X, bits, where="post", color='black', linewidth='3')

        for tbit, bit in enumerate(base_bits):
            plt.text(tbit + 0.2, 1.3, str(bit))

        keys = ['top', 'bottom', 'right']

        for key in keys:
            plt.gca().spines[key].set_visible(False)
        plt.axhline(y=0, xmin=0, xmax=1, color='gray', linewidth='.5')
        plt.xticks([])


class Producer:

    def __init__(self, string, encoder_meth):
        self.encoder = Encoder(string, encoder_meth)
        self.plotter = Plotter()

    def produce_plot(self):
        produced = self.encoder.encode_seq()
        self.plotter.show_plot(produced, self.encoder.bitseq)

    def change_method(self, method: Callable[[list], None]):
        self.encoder.encoding_method = method

    def change_string(self, new_string: str):
        self.encoder.string = new_string


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


if __name__ == '__main__':
    producer = Producer("СЕРГ", enc_2b1q)
    producer.produce_plot()
