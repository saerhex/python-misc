from __future__ import annotations
from typing import Callable
import matplotlib.pyplot as plt
import numpy as np
from logical_encoding import *


class Encoder:

    def __init__(self, string, encoding_method: Callable[[list], None] = None):
        self.string = string
        self.bitseq = self.get_bits()
        self.methods = {}
        if encoding_method:
            self.methods.setdefault(encoding_method.__name__, encoding_method)
        else:
            self.methods.setdefault("nrz", nrz)

    def get_bits(self):
        codes = (format(enc, '8b') for enc in self.string.encode('cp1251'))
        return list(map(int, ''.join(codes)))

    def encode_seq(self):
        data = {}
        for method, func in self.methods.items():
            data.setdefault(method, func(self.bitseq))
        return data


class Plotter:

    def __init__(self, x_axis: int, base_bits: list, rows, cols):
        self.X = np.arange(x_axis)
        self.base_bits = base_bits
        self.rows = rows
        self.cols = cols

    def make_plot(self, bits: list, i: int, title: str):
        plt.subplot(self.rows, self.cols, i)
        plt.step(self.X, bits, where="post", color='black', linewidth='3')
        min_y, max_y = min(bits), max(bits) + 0.4

        for tbit, bit in enumerate(self.base_bits):
            plt.text(tbit, max_y - 0.2, str(bit))

        keys = ['top', 'bottom', 'right']

        for key in keys:
            plt.gca().spines[key].set_visible(False)
        plt.axhline(y=0, xmin=0, xmax=1, color='gray', linewidth='.5')

        plt.ylim((min_y, max_y))
        plt.xticks([])
        plt.title(title)

    def show_plot(self, data: dict[str, list]):
        plt.figure(figsize=(len(self.X)/2, 2 * self.rows))
        i = 1
        for title, bits in data.items():
            self.make_plot(bits, i, title)
            i += 1
        plt.tight_layout()
        plt.show()


class Producer:

    def __init__(self, string: str, x_axis_len: int, encoder_meth, rows=2, cols=1):
        self.encoder = Encoder(string, encoder_meth)
        self.plotter = Plotter(x_axis_len, self.encoder.bitseq, rows, cols)

    def produce_plot(self):
        produced_data = self.encoder.encode_seq()
        self.plotter.show_plot(produced_data)

    def add_method(self, method: Callable[[list], None]):
        self.encoder.methods.setdefault(method.__name__, method)

    def change_string(self, new_string: str):
        self.encoder.string = new_string


if __name__ == '__main__':
    data = input("Input your data to be encoded:")
    producer = Producer(data, len(data) * 8, nrzi, rows=2)
    producer.add_method(enc_2b1q)
    producer.produce_plot()
