from PIL import Image
import matplotlib.pyplot as plt
from math import log


def mandelbrot_point(c ,threshold,iterations):
    (x, y) = c
    z_re = 0.0
    z_img = 0.0
    for i in range(0, iterations):
        z_re_old = z_re
        z_re = (z_re * z_re) - (z_img * z_img) + x
        z_img = 2 * (z_re_old * z_img) + y
        if (z_re * z_re) + (z_img * z_img) > (threshold * threshold):
            return i
    return 0


def mandelbrot_matrix():
    histogram = [0] * 256
    image_raw = Image.new(mode="RGB", size=(1000, 1000))
    image = image_raw.load()
    for y_coord in range(0, 1000):
        for x_coord in range(0, 1000):
            x = x_coord/500.0 - 1.5
            y = y_coord/500.0 - 1
            value = mandelbrot_point((x,y),2.0, 255)
            # intensity 0..255
            #if intensity > 1:
            #    histogram[intensity] += 1
            
            # RGB Value
            rgb = (0,0,0)
            if value < 256:
                # 0 - 255
                rgb = (0,0,value)
            elif 255 < value < 511:
                # 255 < value < 511 
                rgb = (0, (value - 256), 255 - (value - 256))
            else:
                rgb = ((value - 511), 255 - (value - 511), 255 - (value - 511))
            image[x_coord, y_coord] = rgb
    image_raw.show()

def plot_log_histogram_fct(histogram):
    for idx in range(0, 255):
        if histogram[idx] > 0:
            histogram[idx] = log(histogram[idx])
    plt.plot(histogram)
    plt.show()

    
def main():
    mandelbrot_matrix()

    
if __name__ == "__main__":
    main()
