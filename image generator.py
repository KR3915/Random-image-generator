import numpy as np
import matplotlib.pyplot as plt
def make_img(#height, width, channel
        ):
    rnd_arr = np.random.rand(35, 35, 3)
    return rnd_arr
def display_img(array):
    plt.imshow(array)
    plt.show()
def main():
    display_img(array=make_img())


