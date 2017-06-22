


import os
import numpy as np
import matplotlib.pyplot as plt


def test_a():
    a = np.loadtxt(fname=os.path.dirname(os.path.abspath(__file__)) + "/datavalues/a MG_10_15_20_25b_1p8A_th100keV", unpack=True)
    b = np.loadtxt(fname=os.path.dirname(os.path.abspath(__file__)) + "/datavalues/a mg10.txt", unpack=True)
    c = np.loadtxt(fname=os.path.dirname(os.path.abspath(__file__)) + "/datavalues/a mg15.txt", unpack=True)

    plt.plot(a[0],a[1], label='fra 10')
    plt.plot(b[0],b[1], label='alv 10')

    plt.plot(a[0],a[2], label='fra 15')
    plt.plot(c[0],c[1],label='alv 15')

    '''
    plt.plot(a[0],a[3])
    plt.plot(a[0],a[4])
    '''
    plt.legend()
    plt.show()

def test_b():
    a = np.loadtxt(fname=os.path.dirname(os.path.abspath(__file__)) + "/datavalues/b MG_10_15_20b_1um_th100keV", unpack=True)
    b = np.loadtxt(fname=os.path.dirname(os.path.abspath(__file__)) + "/datavalues/b mg10.txt", unpack=True)
   # c = np.loadtxt(fname=os.path.dirname(os.path.abspath(__file__)) + "/datavalues/a mg15.txt", unpack=True)
    '''
    plt.plot(a[0],a[1])
    plt.plot(b[0],b[1])
    '''

    plt.plot(a[0],a[1])
    plt.plot(b[0], b[1], label='alv 10')
   # plt.plot(c[0],c[1])

    '''
    plt.plot(a[0],a[3])
    plt.plot(a[0],a[4])
    '''
    plt.legend()
    plt.show()


def test_c():
    a = np.loadtxt(fname=os.path.dirname(os.path.abspath(__file__)) + "/datavalues/c MG_15b_lambda1_1p8_2p5_4_10A_1um_th100keV",
                   unpack=True)
    plt.plot(a[0], a[1])
    plt.legend()
    plt.show()


def test_d():
    a = np.loadtxt(fname=os.path.dirname(os.path.abspath(__file__)) + "/datavalues/d MGopt_10_15_20b_th100keV_ploteffdetVSlambda",
                   unpack=True)
    b = np.loadtxt(fname=os.path.dirname(os.path.abspath(__file__)) + "/datavalues/d 10.txt",
                   unpack=True)
    plt.plot(a[0], a[1])
    plt.plot(b[0], b[1])
    plt.legend()
    plt.show()


def test_e():
    a = np.loadtxt(fname=os.path.dirname(os.path.abspath(__file__)) + "/datavalues/e MGopt_10_15_20b_th100keV_ploteffindepth_10A",
                   unpack=True)
    b = np.loadtxt(fname=os.path.dirname(os.path.abspath(__file__)) + "/datavalues/e 10.txt",
                   unpack=True)
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    plt.plot(l, a[0], 'o')
    plt.plot(b[0], b[1]/100, 'o', label='alv')
    plt.legend()
    plt.show()


def test_f():
    a = np.loadtxt(fname=os.path.dirname(os.path.abspath(__file__)) + "/datavalues/f MGopt_10_15_20b_th100keV_plotthickindepth_10A",
                   unpack=True)
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    b = np.loadtxt(fname=os.path.dirname(os.path.abspath(__file__)) + "/datavalues/f 10",
                   unpack=True)
    c = np.loadtxt(fname=os.path.dirname(os.path.abspath(__file__)) + "/datavalues/f 15",
                   unpack=True)
    d = np.loadtxt(fname=os.path.dirname(os.path.abspath(__file__)) + "/datavalues/f 20",
                   unpack=True)
    plt.plot(l, a[0], 'o', label='fra 10')
    plt.plot(l, a[1], 'o', label='fra 15')
    plt.plot(l, a[2], 'o', label='fra 20')
    plt.plot(b[0], b[1], 'o', label='alv 10')
    plt.plot(c[0], c[1], 'o', label='alv 15')
    plt.plot(d[0], d[1], 'o', label='alv 20')

   # plt.plot(l, a[1], 'o')
    #plt.plot(l, a[2], 'o')
    plt.legend()
    plt.show()


if __name__=='__main__':

   # test_a()
   # test_b()
    #test_c()
    #test_d()
    #test_e()
    test_f()