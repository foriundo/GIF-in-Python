import imageio.v3 as iio

filenames = ['nyan-cat1.png','nyan-cat2.png','nyan-cat3.png']
images =[]

for f in filenames:
    images.append(iio.imread(f))
iio.imwrite('nyan.gif', images, duration = 500, loop = 0)