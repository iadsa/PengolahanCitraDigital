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


# membuat gambar rotate
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
            else:
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
