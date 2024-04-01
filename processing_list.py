from PIL import Image, ImageOps


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
            tingkat_r = max(0, min(255, r + tingkat_brightness * (r / 255)))
            tingkat_g = max(0, min(255, g + tingkat_brightness * (g / 255)))
            tingkat_b = max(0, min(255, b + tingkat_brightness * (b / 255)))
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
    elif color_depth2 != 24:
        input_image2 = input_image2.convert("RGB")

    # Resize input_image2 to match the size of input_image
    input_image2 = input_image2.resize(input_image.size)

    output_image = Image.new("RGB", input_image.size)
    output_pixels = output_image.load()

    for i in range(output_image.size[0]):
        for j in range(output_image.size[1]):
            color1 = input_image.getpixel((i, j))
            color2 = input_image2.getpixel((i, j))
            r = int(color1[0] * alpha) + int(color2[0] * alpha2)
            g = int(color1[1] * alpha) + int(color2[1] * alpha2)
            b = int(color1[2] * alpha) + int(color2[2] * alpha2)
            output_pixels[i, j] = (r, g, b)

    if color_depth == 1:
        output_image = output_image.convert("1")
    elif color_depth == 8:
        output_image = output_image.convert("L")
    else:
        output_image = output_image.convert("RGB")

    return output_image


# membuat fungsi Flip
def ImgFlip(img_input, coldepth, deg, flip):
    # solusi 1
    # img_output=img_input.flip(deg)

    # solusi 2
    if coldepth != 24:
        img_input = img_input.convert("RGB")

    img_output = Image.new("RGB", (img_input.size[0], img_input.size[1]))
    pixels = img_output.load()
    for i in range(img_input.size[0]):
        for j in range(img_input.size[1]):
            if flip == "vertical":
                r, g, b = img_input.getpixel((i, img_input.size[1] - j - 1))
            elif flip == "horizontal":
                r, g, b = img_input.getpixel((img_input.size[0] - i - 1, j))
            elif flip == "horizontal-vertical":
                r, g, b = img_input.getpixel(
                    (img_input.size[0] - i - 1, img_input.size[1] - j - 1)
                )
            pixels[i, j] = (r, g, b)

    if coldepth == 1:
        img_output = img_output.convert("1")
    elif coldepth == 8:
        img_output = img_output.convert("L")
    else:
        img_output = img_output.convert("RGB")
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
