from PIL import Image


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
    image_raw = Image.new(mode="RGB", size=(600, 600))
    image = image_raw.load()
    for y_coord in range(0, 600):
        for x_coord in range(0, 600):
            x = x_coord/300.0 - 1.5
            y = y_coord/300.0 - 1
            value = mandelbrot_point((x,y),2.0,255)
            image[x_coord, y_coord] = (value, value, value)
    image_raw.show()

    
def main():
    mandelbrot_matrix()

    
if __name__ == "__main__":
    main()
