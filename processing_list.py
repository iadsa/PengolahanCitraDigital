from PIL import Image, ImageOps
import math
import numpy as np
import random


def ImgNegative(img_input, coldepth):
    # solusi 1
    # img_output=ImageOps.invert(img_input)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    img_output = Image.new("RGB", (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            pixels[i, j] = (255 - r, 255 - g, 255 - b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# membuat fungsi rotate
def ImgRotate(img_input, coldepth, deg, direction):
    # solusi 1
    # img_output=img_input.rotate(deg)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    img_output = Image.new("RGB", (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if direction == "C":
                r, g, b = img_input.getpixel((j, img_output.size[0] - i - 1))
            elif direction == "180":
                r, g, b = img_input.getpixel(
                    (img_input.size[0] - i - 1, img_input.size[1] - j - 1)
                )
            elif direction == "CCW":
                r, g, b = img_input.getpixel((img_input.size[1] - j - 1, i))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
    return img_output


# membuat fungsi Brightness


def Brightness(img_input, coldepth, tingkat_brightness):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    img_output = Image.new("RGB", img_input.size)
    pixels_output = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            tingkat_r = max(0, min(255, r + tingkat_brightness))
            tingkat_g = max(0, min(255, g + tingkat_brightness))
            tingkat_b = max(0, min(255, b + tingkat_brightness))
            pixels_output[i, j] = (int(tingkat_r), int(tingkat_g), int(tingkat_b))

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output

    # membuat fungsi Blending


def blending(input_image, color_depth, input_image2, color_depth2, alpha, alpha2):
    if color_depth != 24:
        input_image = input_image.convert("RGB")
    if color_depth2 != 24:
        input_image2 = input_image2.convert("RGB")

    input_image2 = input_image2.resize(input_image.size)

    output_image = Image.new("RGB", input_image.size)
    output_pixels = output_image.load()

    for i in range(output_image.size[0]):
        for j in range(output_image.size[1]):
            color1 = input_image.getpixel((i, j))
            color2 = input_image2.getpixel((i, j))
            r = int(color1[0] * alpha + color2[0] * alpha2)
            g = int(color1[1] * alpha + color2[1] * alpha2)
            b = int(color1[2] * alpha + color2[2] * alpha2)
            output_pixels[i, j] = (r, g, b)

    return output_image


# membuat fungsi Flip
def ImgFlip(img_input, coldepth, flip):

    if coldepth != 24:
        img_input = img_input.convert("RGB")

    img_output = Image.new("RGB", img_input.size)
    pixels = img_output.load()

    if flip == "vertical":
        for i in range(img_input.size[0]):
            for j in range(img_input.size[1]):

                pixels[i, j] = img_input.getpixel((i, img_input.size[1] - j - 1))
    elif flip == "horizontal":
        for i in range(img_input.size[0]):
            for j in range(img_input.size[1]):

                pixels[i, j] = img_input.getpixel((img_input.size[0] - i - 1, j))
    elif flip == "horizontal-vertical":
        for i in range(img_input.size[0]):
            for j in range(img_input.size[1]):

                pixels[i, j] = img_input.getpixel(
                    (img_input.size[0] - i - 1, img_input.size[1] - j - 1)
                )

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")

    return img_output


def ImgThreholding(img_input, coldepth, value):
    if coldepth != 24:
        img_input = img_input.convert("RGB")
    T = value

    img_output = Image.new("RGB", (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            if r < T or g < T or b < T:
                pixels[i, j] = (0, 0, 0)
            else:
                pixels[i, j] = (255, 255, 255)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# fungsi Logaritmik
def Logarithmic(img_input, coldepth, C):
    # rumusnya = S = C*log10(1+r)

    if coldepth != 24:
        img_input = img_input.convert("RGB")

    img_output = Image.new("RGB", img_input.size)
    pixels_output = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))
            pixels_output[i, j] = (
                int(C * math.log10(1 + r)),
                int(C * math.log10(1 + g)),
                int(C * math.log10(1 + b)),
            )

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def TraslationX(
    img_input,
    coldepth,
    sumbu_x,
):
    # rumusnya = B(i,j) = A(i,j+n) sumbu x

    if coldepth != 24:
        img_input = img_input.convert("RGB")

    img_output = Image.new("RGB", img_input.size)

    img_output = Image.new("RGB", (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            # sumbu x itu  kolom = 1
            tx = i - sumbu_x
            if 0 < tx < img_input.size[1]:
                r, g, b = img_input.getpixel((tx, j))
                pixels[i, j] = (r, g, b)
            else:
                pixels[i, j] = (0, 0, 0)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def TraslationY(
    img_input,
    coldepth,
    sumbu_y,
):

    # rumusnya = B(i,j) = A(i+m,j) sumbu y

    if coldepth != 24:
        img_input = img_input.convert("RGB")

    img_output = Image.new("RGB", img_input.size)

    img_output = Image.new("RGB", (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            # sumbu y itu  kolom = 1
            ty = j - sumbu_y
            if 0 < ty < img_input.size[1]:
                r, g, b = img_input.getpixel((i, ty))
                pixels[i, j] = (r, g, b)
            else:
                pixels[i, j] = (0, 0, 0)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def TraslationXY(
    img_input,
    coldepth,
    sumbu_y,
    sumbu_x,
):

    # rumusnya = B(i,j) = A(i+m,j+n)

    if coldepth != 24:
        img_input = img_input.convert("RGB")

    img_output = Image.new("RGB", img_input.size)

    img_output = Image.new("RGB", (img_input.size[1], img_input.size[0]))
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            # sumbu y itu  kolom = 0
            # sumbu x itu  kolom = 1

            ty = j - sumbu_y
            tx = i - sumbu_x

            if 0 < tx < img_input.size[1] and 0 < ty < img_input.size[0]:
                r, g, b = img_input.getpixel((tx, ty))
                pixels[i, j] = (r, g, b)
            else:
                pixels[i, j] = (0, 0, 0)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def Shrinking(img_input, coldepth, scaling):
    # skema
    # row in  div n
    # col in div n
    # i * n j * n

    if coldepth != 24:
        img_input = img_input.convert("RGB")

    img_output = Image.new("RGB", img_input.size)

    img_output = Image.new(
        "RGB", (int(img_input.size[1] / scaling), int(img_input.size[0] / scaling))
    )
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i * scaling, j * scaling))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def ZoomIn(img_input, coldepth, scaling):
    # skema
    # row in  * n
    # col in * n
    # i div n j div n

    if coldepth != 24:
        img_input = img_input.convert("RGB")

    img_output = Image.new("RGB", img_input.size)

    img_output = Image.new(
        "RGB", (int(img_input.size[1] * scaling), int(img_input.size[0] * scaling))
    )
    pixels = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i // scaling, j // scaling))
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# median
def median(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    img_output = Image.new("RGB", img_input.size)
    pixels = img_output.load()

    for i in range(1, img_input.size[0] - 1):
        for j in range(1, img_input.size[1] - 1):
            mask = [
                img_input.getpixel((i - 1, j - 1)),
                img_input.getpixel((i, j - 1)),
                img_input.getpixel((i + 1, j - 1)),
                img_input.getpixel((i - 1, j)),
                img_input.getpixel((i, j)),
                img_input.getpixel((i + 1, j)),
                img_input.getpixel((i - 1, j + 1)),
                img_input.getpixel((i, j + 1)),
                img_input.getpixel((i + 1, j + 1)),
            ]

            mask.sort()
            pixels[i, j] = mask[4]

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# mean
def mean(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

        kernel = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]

        offset = len(kernel) // 2

    img_output = Image.new("RGB", img_input.size)
    pixels = img_output.load()

    for i in range(1, img_input.size[0] - 1 - offset):
        for j in range(1, img_input.size[1] - 1 - offset):
            mask = [
                img_input.getpixel((i - 1, j - 1)),
                img_input.getpixel((i, j - 1)),
                img_input.getpixel((i + 1, j - 1)),
                img_input.getpixel((i - 1, j)),
                img_input.getpixel((i, j)),
                img_input.getpixel((i + 1, j)),
                img_input.getpixel((i - 1, j + 1)),
                img_input.getpixel((i, j + 1)),
                img_input.getpixel((i + 1, j + 1)),
            ]

            r, g, b = (0, 0, 0)
            for k in range(9):
                _r, _g, _b = mask[k]
                _r, _g, _b = round(_r / 9), round(_g / 9), round(_b / 9)
                r, g, b = r + _r, g + _g, b + _b
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# power law transform
def PowerLawoperasion(img_input, coldepth, C, gamma):
    if coldepth != 24:
        img_input = img_input.convert("RGB")
    # rumusnya = S = C*(r**gamma)
    img_output = Image.new("RGB", img_input.size)
    pixels_output = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            r, g, b = img_input.getpixel((i, j))

            r_norm = r / 255.0
            g_norm = g / 255.0
            b_norm = b / 255.0

            _r = int(C * (r_norm**gamma) * 255.0)
            _g = int(C * (g_norm**gamma) * 255.0)
            _b = int(C * (b_norm**gamma) * 255.0)

            _r = max(0, min(255, _r))
            _g = max(0, min(255, _g))
            _b = max(0, min(255, _b))
            pixels_output[i, j] = (_r, _g, _b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# img_neg & flip


# citra kamera 256 256 terus
# dengan output negatif atasnya
# bagian kiri rotate 90
# bagain kanan di flip Vertikal
#
# citra output 512  x 512
#
#
#


# ZOOM_NEGATIF_ROTATE_FLIP_BLENDING
def ZNRFB(img_input, coldepth, scaling):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    neg_img = ImgNegative(img_input, coldepth)

    zoomed_neg_img = ZoomIn(neg_img, coldepth, scaling)

    rotated_img = ImgRotate(img_input, coldepth, 90, "C")

    flipped_img = ImgFlip(img_input, coldepth, flip="horizontal")

    output_image = Image.new("RGB", (512, 512))

    for i in range(512):
        for j in range(256):
            output_image.putpixel((i, j), zoomed_neg_img.getpixel((i, j)))

    blended_rotated_img = blending(img_input, coldepth, rotated_img, coldepth, 0.0, 0.5)
    for i in range(256):
        for j in range(256):
            output_image.putpixel((i, j + 256), blended_rotated_img.getpixel((i, j)))

    blended_flipped_img = blending(img_input, coldepth, flipped_img, coldepth, 0.0, 0.5)
    for i in range(256):
        for j in range(256):
            output_image.putpixel(
                (i + 256, j + 256), blended_flipped_img.getpixel((i, j))
            )

    if coldepth == 1:
        output_image = output_image.convert("1")
    elif coldepth == 8:
        output_image = output_image.convert("L")

    return output_image


# Materi  edge detector


def gradien1(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    gx_kernel = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1],
    ]

    gy_kernel = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1],
    ]

    offset = len(gx_kernel) // 2

    img_output = Image.new("RGB", img_input.size)
    pixels = img_output.load()

    width, height = img_input.size
    for i in range(offset, width - offset):
        for j in range(offset, height - offset):
            gx = 0
            gy = 0

            for m in range(-offset, offset + 1):
                for n in range(-offset, offset + 1):
                    pixel = img_input.getpixel((i + m, j + n))
                    intensity = sum(pixel) / 3

                    gx += gx_kernel[m + offset][n + offset] * intensity
                    gy += gy_kernel[m + offset][n + offset] * intensity

            magnitude = int(math.sqrt(gx**2 + gy**2))
            magnitude = min(255, max(0, magnitude))
            pixels[i, j] = (magnitude, magnitude, magnitude)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# sobel gx
def sobel_gx(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    gx_kernel = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1],
    ]

    offset = len(gx_kernel) // 2
    img_output = Image.new("L", img_input.size)
    pixels = img_output.load()
    width, height = img_input.size

    for i in range(offset, width - offset):
        for j in range(offset, height - offset):
            gx = 0
            for k in range(len(gx_kernel)):
                for l in range(len(gx_kernel[k])):
                    pixel = img_input.getpixel((i + k - offset, j + l - offset))
                    intensity = sum(pixel) / 3
                    gx += intensity * gx_kernel[k][l]
            gx = int(min(255, max(0, gx)))
            pixels[i, j] = gx

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# sobel_gy
def sobel_gy(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    gy_kernel = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1],
    ]

    offset = len(gy_kernel) // 2
    img_output = Image.new("L", img_input.size)
    pixels = img_output.load()
    width, height = img_input.size

    for i in range(offset, width - offset):
        for j in range(offset, height - offset):
            gy = 0
            for k in range(len(gy_kernel)):
                for l in range(len(gy_kernel[k])):
                    pixel = img_input.getpixel((i + k - offset, j + l - offset))
                    intensity = sum(pixel) / 3
                    gy += intensity * gy_kernel[k][l]
            gy = int(min(255, max(0, gy)))
            pixels[i, j] = gy

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


def sobel(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert("RGB")
    gx_kernel = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1],
    ]

    gy_kernel = [
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1],
    ]

    offset = len(gx_kernel) // 2
    img_output = Image.new("L", img_input.size)
    pixels = img_output.load()
    width, height = img_input.size

    for i in range(offset, width - offset):
        for j in range(offset, height - offset):
            gx = 0
            gy = 0
            for k in range(len(gx_kernel)):
                for l in range(len(gx_kernel[k])):
                    pixel = img_input.getpixel((i + k - offset, j + l - offset))
                    intensity = sum(pixel) / 3
                    gx += intensity * gx_kernel[k][l]
                    gy += intensity * gy_kernel[k][l]
            magnitude = int(math.sqrt(gx**2 + gy**2))
            magnitude = min(255, max(0, magnitude))
            pixels[i, j] = magnitude

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# prewitt
def prewitt_gx(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    gx_kernel = [
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1],
    ]

    offset = len(gx_kernel) // 2
    img_output = Image.new("L", img_input.size)
    pixels = img_output.load()
    width, height = img_input.size

    for i in range(offset, width - offset):
        for j in range(offset, height - offset):
            gx = 0
            for k in range(len(gx_kernel)):
                for l in range(len(gx_kernel[k])):
                    pixel = img_input.getpixel((i + k - offset, j + l - offset))
                    intensity = sum(pixel) / 3
                    gx += intensity * gx_kernel[k][l]
            gx = int(min(255, max(0, gx)))
            pixels[i, j] = gx

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# prewitt
def prewitt_gy(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    gy_kernel = [
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1],
    ]

    offset = len(gy_kernel) // 2
    img_output = Image.new("L", img_input.size)
    pixels = img_output.load()
    width, height = img_input.size

    for i in range(offset, width - offset):
        for j in range(offset, height - offset):
            gy = 0
            for k in range(len(gy_kernel)):
                for l in range(len(gy_kernel[k])):
                    pixel = img_input.getpixel((i + k - offset, j + l - offset))
                    intensity = sum(pixel) / 3
                    gy += intensity * gy_kernel[k][l]
            gy = int(min(255, max(0, gy)))
            pixels[i, j] = gy

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# prewitt_edge
def prewitt_edge(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    gx_kernel = [
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1],
    ]

    gy_kernel = [
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1],
    ]

    offset = len(gx_kernel) // 2
    img_output = Image.new("L", img_input.size)
    pixels = img_output.load()
    width, height = img_input.size

    for i in range(offset, width - offset):
        for j in range(offset, height - offset):
            gx = 0
            gy = 0
            for k in range(len(gx_kernel)):
                for l in range(len(gx_kernel[k])):
                    pixel = img_input.getpixel((i + k - offset, j + l - offset))
                    intensity = sum(pixel) / 3
                    gx += intensity * gx_kernel[k][l]
                    gy += intensity * gy_kernel[k][l]
            magnitude = int(math.sqrt(gx**2 + gy**2))
            magnitude = min(255, max(0, magnitude))
            pixels[i, j] = magnitude

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


##Robert operator


# GX
def robert_operator_gx(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    gx_kernel = [
        [-1, 0],  # Membalik arah gradien gx
        [0, 1],
    ]

    width, height = img_input.size
    img_output = Image.new("L", (width, height))
    pixels_output = img_output.load()
    pixels_input = img_input.load()

    for i in range(width - 1):
        for j in range(height - 1):
            gx = 0

            for m in range(2):
                for n in range(2):
                    pixel = pixels_input[i + m, j + n]
                    intensity = sum(pixel) / 3
                    gx += gx_kernel[m][n] * intensity

            gx = int(abs(gx))
            gx = min(255, max(0, gx))
            pixels_output[i, j] = gx

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# GY
def robert_operator_gy(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    gy_kernel = [
        [0, 1],
        [-1, 0],
    ]

    width, height = img_input.size
    img_output = Image.new("L", (width, height))
    pixels_output = img_output.load()
    pixels_input = img_input.load()

    for i in range(0, width - 1):
        for j in range(0, height - 1):
            gy = 0

            for m in range(2):
                for n in range(2):
                    pixel = pixels_input[i + m, j + n]
                    intensity = sum(pixel) / 3  # Rata-rata intensitas untuk grayscale
                    gy += gy_kernel[m][n] * intensity

            gy = int(abs(gy))
            gy = min(255, max(0, gy))
            pixels_output[i, j] = gy

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# robert
def robert(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    gx_kernel = [
        [1, 0],
        [0, -1],
    ]

    gy_kernel = [
        [0, 1],
        [-1, 0],
    ]

    width, height = img_input.size
    img_output = Image.new("RGB", (width, height))
    pixels_output = img_output.load()

    for i in range(1, width - 1):
        for j in range(1, height - 1):
            gx = 0
            gy = 0

            for m in range(2):
                for n in range(2):
                    pixel = img_input.getpixel((i + m - 1, j + n - 1))
                    intensity = sum(pixel) / 3
                    gx += gx_kernel[m][n] * intensity
                    gy += gy_kernel[m][n] * intensity

            magnitude = int(math.sqrt(gx**2 + gy**2))
            magnitude = min(255, max(0, magnitude))

            pixels_output[i, j] = (magnitude, magnitude, magnitude)

    # Konversi gambar output sesuai dengan kedalaman warna yang diinginkan
    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# Laplacian Operator


def laplacian(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    laplacian_kernels = [
        [
            [0, 1, 0],
            [1, -4, 1],
            [0, 1, 0],
        ],
        [
            [1, 1, 1],
            [1, -8, 1],
            [1, 1, 1],
        ],
        [
            [1, -2, 1],
            [-2, 4, -2],
            [1, -2, 1],
        ],
    ]

    width, height = img_input.size
    img_output = Image.new("RGB", (width, height))
    pixels_output = img_output.load()

    for i in range(1, width - 1):
        for j in range(1, height - 1):
            laplacian_total = 0

            for kernel in laplacian_kernels:
                laplacian_value = 0
                for m in range(3):
                    for n in range(3):
                        pixel = img_input.getpixel((i + m - 1, j + n - 1))
                        intensity = sum(pixel) / 3
                        laplacian_value += kernel[m][n] * intensity

                laplacian_total += abs(laplacian_value)

            laplacian = int(laplacian_total / len(laplacian_kernels))
            laplacian = min(255, max(0, laplacian))
            pixels_output[i, j] = (laplacian, laplacian, laplacian)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


from PIL import Image


def kompas(img_input, coldepth):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    compass_kernels = [
        [
            [-1, -1, -1],
            [1, 1, 1],
            [0, 0, 0],
        ],  # North
        [
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1],
        ],  # North-East (modified)
        [
            [0, 1, 1],
            [-1, 0, 1],
            [-1, -1, 0],
        ],  # East
        [
            [1, 1, 1],
            [0, 0, 0],
            [-1, -1, -1],
        ],  # South-East
        [
            [1, 0, -1],
            [1, 0, -1],
            [1, 0, -1],
        ],  # South
        [
            [0, 0, 0],
            [-1, -1, -1],
            [1, 1, 1],
        ],  # South-West
        [
            [0, -1, -1],
            [1, 0, -1],
            [1, 1, 0],
        ],  # West
        [
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1],
        ],  # North-West
    ]

    width, height = img_input.size
    img_output = Image.new("RGB", (width, height))
    pixels_output = img_output.load()

    for i in range(1, width - 1):
        for j in range(1, height - 1):
            max_gradient = 0

            for kernel in compass_kernels:
                gradient = 0
                for m in range(3):
                    for n in range(3):
                        pixel = img_input.getpixel((i + m - 1, j + n - 1))
                        intensity = sum(pixel) / 3
                        gradient += kernel[m][n] * intensity

                max_gradient = max(max_gradient, abs(gradient))

            max_gradient = int(max_gradient)
            max_gradient = min(255, max(0, max_gradient))
            pixels_output[i, j] = (max_gradient, max_gradient, max_gradient)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# Noise Graussian (scaling)
def add_gaussian_noise(img_input, mean=0, std_dev=25, coldepth=24):
    if coldepth != 24 and coldepth != 8 and coldepth != 1:
        raise ValueError(
            "Unsupported coldepth. Use 24 for RGB, 8 for grayscale, or 1 for binary images."
        )

    img_input = img_input.convert("RGB") if coldepth == 24 else img_input.convert("L")
    img_output = img_input.copy()
    pixels_output = img_output.load()

    for i in range(img_output.size[0]):
        for j in range(img_output.size[1]):
            if coldepth == 24:
                r, g, b = img_input.getpixel((i, j))

                noise_r = int(random.gauss(mean, std_dev))
                noise_g = int(random.gauss(mean, std_dev))
                noise_b = int(random.gauss(mean, std_dev))

                _r = max(0, min(255, r + noise_r))
                _g = max(0, min(255, g + noise_g))
                _b = max(0, min(255, b + noise_b))

                pixels_output[i, j] = (_r, _g, _b)
            else:
                gray = img_input.getpixel((i, j))

                noise_gray = int(random.gauss(mean, std_dev))

                _gray = max(0, min(255, gray + noise_gray))

                pixels_output[i, j] = _gray

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# Noise Salt and pepper (scalling)
# Salt
def add_salt_noise(img_input, salt_prob=0.02, coldepth=24):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    img_output = img_input.copy()
    pixels_output = img_output.load()
    if img_output.mode == "L":  # Grayscale
        for i in range(img_output.size[0]):
            for j in range(img_output.size[1]):
                if random.random() < salt_prob:
                    pixels_output[i, j] = 255
    else:
        for i in range(img_output.size[0]):
            for j in range(img_output.size[1]):
                if random.random() < salt_prob:
                    pixels_output[i, j] = (255, 255, 255)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# Pepper
def add_pepper_noise(img_input, pepper_prob=0.02, coldepth=24):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    img_output = img_input.copy()
    pixels_output = img_output.load()
    if img_output.mode == "L":  # Grayscale
        for i in range(img_output.size[0]):
            for j in range(img_output.size[1]):
                if random.random() < pepper_prob:
                    pixels_output[i, j] = 0
    else:  # RGB or other modes
        for i in range(img_output.size[0]):
            for j in range(img_output.size[1]):
                if random.random() < pepper_prob:
                    pixels_output[i, j] = (0, 0, 0)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# Salt and pepper
def add_salt_and_pepper_noise(img_input, salt_prob=0.02, pepper_prob=0.02, coldepth=24):
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    img_output = img_input.copy()
    pixels_output = img_output.load()
    if img_output.mode == "L":  # Grayscale
        for i in range(img_output.size[0]):
            for j in range(img_output.size[1]):
                rand_num = random.random()
                if rand_num < salt_prob:
                    pixels_output[i, j] = 255
                elif rand_num < salt_prob + pepper_prob:
                    pixels_output[i, j] = 0
    else:  # RGB or other modes
        for i in range(img_output.size[0]):
            for j in range(img_output.size[1]):
                rand_num = random.random()
                if rand_num < salt_prob:
                    pixels_output[i, j] = (255, 255, 255)
                elif rand_num < salt_prob + pepper_prob:
                    pixels_output[i, j] = (0, 0, 0)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")

    return img_output


# getfixel
def get_pixel(img_input, x, y, default=0):
    width, height = img_input.size
    if x < 0 or y < 0 or x >= width or y >= height:
        return default
    return img_input.getpixel((x, y))


# mean filter
def mean_filter(img_input, kernel_size):
    coldepth = img_input.mode
    if coldepth != "RGB":
        img_input = img_input.convert("RGB")

    img_output = img_input.copy()
    pixels_output = img_output.load()
    offset = kernel_size // 2

    for i in range(img_input.width):
        for j in range(img_input.height):
            mask = []
            for k in range(-offset, offset + 1):
                for l in range(-offset, offset + 1):
                    mask.append(get_pixel(img_input, i + k, j + l, default=(0, 0, 0)))
            pixels_output[i, j] = tuple(
                int(sum(channel) / len(channel)) for channel in zip(*mask)
            )

    if coldepth == "1":
        img_output = img_output.convert("1")
    elif coldepth == "L":
        img_output = img_output.convert("L")

    return img_output


# median filter
def median_filter(img_input, kernel_size):
    coldepth = img_input.mode
    if coldepth != "RGB":
        img_input = img_input.convert("RGB")

    img_output = img_input.copy()
    pixels_output = img_output.load()
    offset = kernel_size // 2

    for i in range(img_input.width):
        for j in range(img_input.height):
            mask = []
            for k in range(-offset, offset + 1):
                for l in range(-offset, offset + 1):
                    mask.append(get_pixel(img_input, i + k, j + l, default=(0, 0, 0)))
            pixels_output[i, j] = tuple(
                int(np.median(channel)) for channel in zip(*mask)
            )

    if coldepth == "1":
        img_output = img_output.convert("1")
    elif coldepth == "L":
        img_output = img_output.convert("L")

    return img_output


# Gaussian filter
def gaussian_filter(img_input, kernel_size):
    coldepth = img_input.mode
    if coldepth != "RGB":
        img_input = img_input.convert("RGB")

    def gaussian(x, y, sigma=1.0):
        return (1.0 / (2.0 * np.pi * sigma**2)) * np.exp(
            -(x**2 + y**2) / (2 * sigma**2)
        )

    img_output = img_input.copy()
    pixels_output = img_output.load()
    offset = kernel_size // 2

    # Create Gaussian kernel
    kernel = np.zeros((kernel_size, kernel_size))
    for x in range(-offset, offset + 1):
        for y in range(-offset, offset + 1):
            kernel[x + offset, y + offset] = gaussian(x, y)
    kernel /= np.sum(kernel)

    for i in range(img_input.width):
        for j in range(img_input.height):
            mask = []
            for k in range(-offset, offset + 1):
                for l in range(-offset, offset + 1):
                    mask.append(get_pixel(img_input, i + k, j + l, default=(0, 0, 0)))
            pixels_output[i, j] = tuple(
                int(np.sum(np.array(channel) * kernel.flatten()))
                for channel in zip(*mask)
            )

    if coldepth == "1":
        img_output = img_output.convert("1")
    elif coldepth == "L":
        img_output = img_output.convert("L")

    return img_output


# loop 3x3 filter
def loop_3x3_filter(img_input, filter_func, iterations):
    img_output = img_input
    for _ in range(iterations):
        img_output = filter_func(img_output, 3)
    return img_output


# Fungsi Min Filter
def min_filter(img_input):
    coldepth = img_input.mode
    if coldepth != "RGB":
        img_input = img_input.convert("RGB")

    width, height = img_input.size
    pixels_input = img_input.load()
    img_output = Image.new("RGB", (width, height))
    pixels_output = img_output.load()

    for i in range(1, width - 1):
        for j in range(1, height - 1):
            mask = [
                img_input.getpixel((i - 1, j - 1)),
                img_input.getpixel((i, j - 1)),
                img_input.getpixel((i + 1, j - 1)),
                img_input.getpixel((i - 1, j)),
                img_input.getpixel((i, j)),
                img_input.getpixel((i + 1, j)),
                img_input.getpixel((i - 1, j + 1)),
                img_input.getpixel((i, j + 1)),
                img_input.getpixel((i + 1, j + 1)),
            ]
            min_r = min(mask, key=lambda x: x[0])[0]
            min_g = min(mask, key=lambda x: x[1])[1]
            min_b = min(mask, key=lambda x: x[2])[2]
            pixels_output[i, j] = (min_r, min_g, min_b)

    if coldepth == "1":
        img_output = img_output.convert("1")
    elif coldepth == "L":
        img_output = img_output.convert("L")

    return img_output


# Fungsi Max Filter
def max_filter(img_input):
    coldepth = img_input.mode
    if coldepth != "RGB":
        img_input = img_input.convert("RGB")

    width, height = img_input.size
    pixels_input = img_input.load()
    img_output = Image.new("RGB", (width, height))
    pixels_output = img_output.load()

    for i in range(1, width - 1):
        for j in range(1, height - 1):
            mask = [
                img_input.getpixel((i - 1, j - 1)),
                img_input.getpixel((i, j - 1)),
                img_input.getpixel((i + 1, j - 1)),
                img_input.getpixel((i - 1, j)),
                img_input.getpixel((i, j)),
                img_input.getpixel((i + 1, j)),
                img_input.getpixel((i - 1, j + 1)),
                img_input.getpixel((i, j + 1)),
                img_input.getpixel((i + 1, j + 1)),
            ]
            max_r = max(mask, key=lambda x: x[0])[0]
            max_g = max(mask, key=lambda x: x[1])[1]
            max_b = max(mask, key=lambda x: x[2])[2]
            pixels_output[i, j] = (max_r, max_g, max_b)

    if coldepth == "1":
        img_output = img_output.convert("1")
    elif coldepth == "L":
        img_output = img_output.convert("L")

    return img_output


# Fungsi Erosi
# penipisan objek( putih) hitam menebal
# mengikuti kernel
# 𝐴⊖𝐵
def erosi(img_input):
    return min_filter(img_input)


# Fungsi Dilasi
# penebalan objek (putih)
# 𝐴 ⊕ 𝐵
def dilasi(img_input):
    return max_filter(img_input)


# Fungsi Opening
# turunan pertama
# citra masukan dikenakan erosi dilanjutkan dilasi
# 𝐴⊖𝐵⨁𝐵 (max)
def opening(img_input):
    eroded = erosi(img_input)
    opened = dilasi(eroded)
    return opened


# Fungsi Closing
# citra masukan dikenakan dilasi dilanjutkan erosi
# 𝐴⊕𝐵⊖𝐵 (min)
def closing(img_input):
    dilated = dilasi(img_input)
    closed = erosi(dilated)
    return closed


# Fungsi White Top Hat
# A + B - Opening
def white_top_hat(img_input):
    coldepth = img_input.mode
    if coldepth != "RGB":
        img_input = img_input.convert("RGB")

    opened = opening(img_input)
    pixels_input = img_input.load()
    pixels_opened = opened.load()
    img_output = Image.new(img_input.mode, img_input.size)
    pixels_output = img_output.load()

    for i in range(img_input.width):
        for j in range(img_input.height):
            if coldepth == "1" or coldepth == "L":
                r = pixels_input[i, j]
                ro = pixels_opened[i, j]
                pixels_output[i, j] = max(0, r - ro)
            else:
                r, g, b = pixels_input[i, j]
                ro, go, bo = pixels_opened[i, j]
                pixels_output[i, j] = (max(0, r - ro), max(0, g - go), max(0, b - bo))

    if coldepth == "1":
        img_output = img_output.convert("1")
    elif coldepth == "L":
        img_output = img_output.convert("L")

    return img_output


# Fungsi Black Top Hat
# Citra hasil Clossing - Citra masukan (A + B)
def black_top_hat(img_input):
    coldepth = img_input.mode
    if coldepth != "RGB":
        img_input = img_input.convert("RGB")

    closed = closing(img_input)
    pixels_input = img_input.load()
    pixels_closed = closed.load()
    img_output = Image.new(img_input.mode, img_input.size)
    pixels_output = img_output.load()

    for i in range(img_input.width):
        for j in range(img_input.height):
            if coldepth == "1" or coldepth == "L":
                r = pixels_input[i, j]
                rc = pixels_closed[i, j]
                pixels_output[i, j] = max(0, rc - r)
            else:
                r, g, b = pixels_input[i, j]
                rc, gc, bc = pixels_closed[i, j]
                pixels_output[i, j] = (max(0, rc - r), max(0, gc - g), max(0, bc - b))

    if coldepth == "1":
        img_output = img_output.convert("1")
    elif coldepth == "L":
        img_output = img_output.convert("L")

    return img_output


# sceletonisation
