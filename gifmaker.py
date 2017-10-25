import imageio

images = []
images.append(imageio.imread('maps/until1920_text.png'))
images.append(imageio.imread('maps/1921-1929_text.png'))
images.append(imageio.imread('maps/1930-1939_text.png'))
images.append(imageio.imread('maps/1940-1949_text.png'))
images.append(imageio.imread('maps/1950-1959_text.png'))
images.append(imageio.imread('maps/1960-1969_text.png'))
images.append(imageio.imread('maps/1970-1979_text.png'))
images.append(imageio.imread('maps/1980-1989_text.png'))
images.append(imageio.imread('maps/1990-1999_text.png'))
images.append(imageio.imread('maps/2000-2009_text.png'))
images.append(imageio.imread('maps/2010-2016_text.png'))
images.append(imageio.imread('maps/total_text.png'))

imageio.mimsave('timeline.gif', images,  duration=2)
