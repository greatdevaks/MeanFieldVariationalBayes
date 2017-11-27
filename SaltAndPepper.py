import numpy
import matplotlib.pyplot
from scipy.misc import imread

def addGaussianNoise(im, prop, varSigma):
    print("Here")
    N = int(numpy.round(numpy.prod(im.shape) * prop))
    index = numpy.unravel_index(numpy.random.permutation(numpy.prod(im.shape))[1:N], im.shape)
    e = varSigma * numpy.random.randn(numpy.prod(im.shape)).reshape(im.shape)
    im2 = numpy.copy(im)
    im2[index] += e[index]
    return im2

def addSaltAndPepperNoise(im, prop):
    print("Now here")
    N = int(numpy.round(numpy.prod(im.shape) * prop))
    index = numpy.unravel_index(numpy.random.permutation(numpy.prod(im.shape))[1:N], im.shape)
    im2 = numpy.copy(im)
    im2[index] += 1 - im2[index]
    return im2

#proportion of pixels to alter...
prop = 0.7

varSigma = 0.1

matplotlib.pyplot.ion()
im = imread('test.jpg')
im = im / 255
fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(131)
ax.imshow(im, cmap = 'gray')

im2 = addGaussianNoise(im, prop, varSigma)
ax2 = fig.add_subplot(132)
ax2.imshow(im2, cmap = 'gray')
im2 = addSaltAndPepperNoise(im, prop)
ax3 = fig.add_subplot(133)
ax3.imshow(im2, cmap= 'gray')



