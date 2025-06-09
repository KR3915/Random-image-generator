import numpy as np
import matplotlib.pyplot as plt

def make_img():
    rnd_arr = np.random.rand(35, 35, 3)
    return rnd_arr

def display_img(array):
    
    plt.imshow(array)
    plt.show()

def main():
    for i in range(10):
        display_img(array=make_img())
if __name__ == "__main__":
    main()