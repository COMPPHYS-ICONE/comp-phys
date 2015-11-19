import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
#from skimage import feature

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-order', type = float)
parser.add_argument('--no-norm', dest='norm',  action='store_false') 
parser.add_argument('-zeroth', dest = 'no_zeroth',  action='store_false') 
parser.set_defaults(no_zeroth=True, norm=True)
args = parser.parse_args()
order = args.order
no_norm = args.norm
zeroth = args.no_zeroth

print order, type(order)
print no_norm, type(no_norm)
print zeroth, type(zeroth)


def extract_shape(im_file, blowup = 1., plot_img = False, plot_contour = False, plot_contour_pts = False):
    x_arr = []
    y_arr = []
    im = mpimg.imread(im_file)
    if len(im.shape) > 2:
        im = im[:, :, 0]
    
    if plot_img:
        plt.figure()
        plt.title('Original Shape')
        plt.imshow(im, cmap = plt.cm.gray)
    x = np.arange(im.shape[1])*blowup  
    y = np.arange(im.shape[0])*blowup
    y = y[::-1]

    X, Y = np.meshgrid(x, y)
    
    plt.figure()
    plt.title('Contours')
    CS = plt.contour(X, Y, im, 1)
    levels = CS.levels
    print 'contour level', levels
    if not plot_contour:
        plt.close()

    cs_paths = CS.collections[0].get_paths()

    print 'number of contour path', len(cs_paths)

    for i in range(0, len(cs_paths)):
        v = cs_paths[i].vertices
        x_arr.append(v[:,0])
        y_arr.append(v[:,1])

    if plot_contour_pts:
        plt.figure()
        plt.title("Verify the contour points are correct")
        for i in range(0, len(cs_paths)):
            plt.scatter(x_arr[i], y_arr[i])

    return x_arr, y_arr, cs_paths

def FD(x, y, plot_FD = False, y_lim = None):
    N = len(x)
    n = np.arange(N)
    z = x + y*1j
    Z = np.fft.fft(z)
    if plot_FD:
        plt.figure()
        plt.title('FD real and imag')
        plt.plot(Z.real, 'b-')
        plt.plot(Z.imag, 'g-')
        if y_lim != None:
            plt.ylim([-y_lim, y_lim])
    return Z
    
def filt_FD(Z, n_keep, no_zeroth = True):
    N = len(Z)
    n = np.arange(len(Z))
    print 'Nyquist index', N/2
    # in case I want the centroid position.
    filt0 = n > 0 if no_zeroth else 1
    filt1 = filt0*(n <= n_keep)
    
    filt2 = (n > ((N-1) - n_keep))
    print 'Number of components from both sides:', filt1.sum(), filt2.sum()
    filt = filt1 + filt2
    #print Z.real[N/2]
    return Z*filt
    
def get_FD_abs(x, y, order, norm = no_norm, no_zeroth = zeroth):
    '''Finds the Fourier Descriptors and the recovered x and y for a shape.'''
    Z = []
    fd_mag = []
    x_rec = []
    y_rec = []
    for conts in range(0, len(cs_paths)):
        Z = FD(x[conts], y[conts])
        print 'len(Z)', len(Z)
        print 'Shape of Z', Z.shape

        Z_filt = filt_FD(Z, order, no_zeroth=zeroth)
        if norm:
            print type(Z_filt)
            print Z_filt.shape
            Z_filt = size_norm(Z_filt)
        print 'len(Z_filt)', len(Z_filt)
        x_recover, y_recover = recover_shape(Z_filt)
        x_rec.append(x_recover)
        y_rec.append(y_recover)

        # throw away zero terms
        fd_mag.append(np.abs(Z_filt[Z_filt != 0]))
    #     fd_mag = fd_mag[fd_mag > 0]
    
    return fd_mag, x_rec, y_rec

def recover_shape(Z):
    z_rec = np.fft.ifft(Z)
    x_rec = z_rec.real
    y_rec = z_rec.imag
    return x_rec, y_rec
    
def size_norm(Z):
    return Z/np.sqrt(np.abs(Z[1])*np.abs(Z[-1]))
    
def plot_shape(x, y, new_plot = False, showit = False, save = False):
    if new_plot == True:
        plt.figure()
    try:
        xlen = len(x)
    except:
        plt.plot(x, y)
    else:
        for i in range(xlen):
            plt.plot(x[i], y[i])
    if save == True:
        pass
    
plt.figure()
plt.title('Numbers Recovered from FDs')
x1, y1, cs_paths = extract_shape('number1.png')
fd_mag, x_rec, y_rec = get_FD_abs(x1,y1,order)
plot_shape(x_rec, y_rec)
x2, y2, cs_paths = extract_shape('number2.png')
fd_mag2, x_rec2, y_rec2 = get_FD_abs(x2,y2,order)
plot_shape(x_rec2, y_rec2)
x3, y3, cs_paths = extract_shape('number6.png', .1)
fd_mag3, x_rec3, y_rec3 = get_FD_abs(x3,y3,order)
plot_shape(x_rec3, y_rec3)
plt.savefig("rec_numbers126.pdf") 
plt.show()


plt.figure()
plt.title('Magnitudes of FDs for 1,2 and 6')
plt.plot(fd_mag[0], 'bo')
plt.plot(fd_mag2[0], 'gx')
for i in range(0, len(cs_paths)):
    plt.plot(fd_mag3[i], 'r8')
plt.savefig("FourierDescriptor_numbers126.pdf") 
plt.show()