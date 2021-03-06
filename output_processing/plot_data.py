import scipy
import matplotlib.pyplot as plt
import os.path

from constants import DATA_PATH


def generate_plot(filepath):
    '''
    Make a basic plot of the binary output data (from gnuradio)
    '''
    dataLen = 1000
    data = scipy.fromfile(open(filepath), dtype=scipy.complex64, count=dataLen)
    plt.figure()
    plt.plot(data)
    plt.show()


def main():
    path = os.path.join(DATA_PATH, "ch0.cfile")
    generate_plot(path)


if __name__ == "__main__":
    main()



