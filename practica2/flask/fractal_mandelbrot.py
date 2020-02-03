# Mandelbrot fractal 
# FB - 201003254 
from PIL import Image

# max iterations allowed 
maxIt = 255

# return: un objeto de la clase Image con el fractal
def fractal_mandelbrot(xa=-2.0, ya=-1.5, xb=1.0, yb=1.5, size=256):
    imgx = imgy = size
    image = Image.new("RGB", (imgx, imgy)) 
    
    for y in range(imgy): 
        zy = y * (yb - ya) / (imgy - 1) + ya 
        for x in range(imgx): 
            zx = x * (xb - xa) / (imgx - 1) + xa 
            z = zx + zy * 1j
            c = z 
            for i in range(maxIt): 
                if abs(z) > 2.0: break
                z = z * z + c 
            image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))
    
    return image
    