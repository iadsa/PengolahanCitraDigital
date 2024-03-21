import PySimpleGUI as sg
import os.path
from PIL import Image, ImageOps
from processing_list import *

# Kolom Area No 1: Area open folder and select image
file_list_column = [
    [
        sg.Text("Open Image Folder :"),
    ],
    [
        sg.In(size=(20, 1), enable_events=True, key="ImgFolder"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("Choose an image from list :"),
    ],
    [sg.Listbox(values=[], enable_events=True, size=(18, 10), key="ImgList")],
]

# Kolom Area No 2: Area viewer image input
image_viewer_column = [
    [sg.Text("Image Input :")],
    [sg.Text(size=(40, 1), key="FilepathImgInput")],
    [sg.Image(key="ImgInputViewer")],
]


# Kolom Area No 3: Area Image info dan Tombol list of processing
list_processing = [
    [
        sg.Text("Image Information:"),
    ],
    [
        sg.Text(size=(20, 1), key="ImgSize"),
    ],
    [
        sg.Text(size=(20, 1), key="ImgColorDepth"),
    ],
    [
        sg.Text("List of Processing:"),
    ],
    [
        sg.Button("Image Negative", size=(20, 1), key="ImgNegative"),
    ],
    [
        sg.Button("Image Rotate", size=(20, 1), key="ImgRotate"),
    ],
    [
        sg.Button("Image Brightness", size=(20, 1), key="ImgBrightness"),
    ],
]

list_processing_output = [
    [
        sg.Text("Image Information Output:"),
    ],
    [
        sg.Text(size=(20, 1), key="ImgSize_output"),
    ],
    [
        sg.Text(size=(20, 1), key="ImgColorDepth_output"),
    ],
]


# Kolom Area No 4: Area viewer image output
image_viewer_column2 = [
    [sg.Text("Image Processing output:")],
    [sg.Text(size=(40, 1), key="ImgProcessingType")],
    [sg.Image(key="ImgOutputViewer")],
]


# Gabung Full layout
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(list_processing_output),
        sg.VSeperator(),
        sg.Column(image_viewer_column2),  # tukar posisi
        sg.VSeperator(),
        sg.Column(list_processing),
        sg.VSeperator(),
        sg.Column(image_viewer_column),  # tukar posisi
    ]
]

window = sg.Window("Mini Image Editor", layout)


# Run the Event Loop
# nama image file temporary setiap kali processing output
filename_out = "out.png"
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    # Folder name was filled in, make a list of files in the folder
    if event == "ImgFolder":
        folder = values["ImgFolder"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["ImgList"].update(fnames)

    elif event == "ImgList":  # A file was chosen from the listbox
        try:
            filename = os.path.join(values["ImgFolder"], values["ImgList"][0])
            window["FilepathImgInput"].update(filename)
            window["ImgInputViewer"].update(filename=filename)
            window["ImgProcessingType"].update(filename)
            window["ImgOutputViewer"].update(filename=filename)
            img_input = Image.open(filename)
            img_output = Image.open(filename)
            # img_input.show()
            # Size
            img_width, img_height = img_input.size
            window["ImgSize"].update(
                "Image Size : " + str(img_width) + " x " + str(img_height)
            )

            # Color depth
            mode_to_coldepth = {
                "1": 1,
                "L": 8,
                "P": 8,
                "RGB": 24,
                "RGBA": 32,
                "CMYK": 32,
                "YCbCr": 24,
                "LAB": 24,
                "HSV": 24,
                "I": 32,
                "F": 32,
            }
            coldepth = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth"].update("Color Depth : " + str(coldepth))

        except:
            pass

    elif event == "ImgRotate":  # A file was chosen from the listbox
        try:
            filename = os.path.join(values["ImgFolder"], values["ImgList"][0])
            window["FilepathImgInput"].update(filename)
            window["ImgInputViewer"].update(filename=filename)
            window["ImgProcessingType"].update(filename)
            window["ImgOutputViewer"].update(filename=filename)
            img_input = Image.open(filename)
            img_output = Image.open(filename)

            angle = 90
            img_output = img_input.rotate(angle, expand=True)

            # Update informasi ukuran gambar input
            img_width, img_height = img_input.size
            window["ImgSize"].update(
                "Image Size : " + str(img_width) + " x " + str(img_height)
            )

            # Update informasi kedalaman warna gambar input
            mode_to_coldepth = {
                "1": 1,
                "L": 8,
                "P": 8,
                "RGB": 24,
                "RGBA": 32,
                "CMYK": 32,
                "YCbCr": 24,
                "LAB": 24,
                "HSV": 24,
                "I": 32,
                "F": 32,
            }
            coldepth = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth"].update("Color Depth : " + str(coldepth))

            # Update informasi ukuran gambar output
            img_width, img_height = img_output.size
            window["ImgSize_output"].update(
                "Image Size : " + str(img_width) + " x " + str(img_height)
            )

            # Update informasi kedalaman warna gambar output
            coldepth = mode_to_coldepth[img_output.mode]
            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

    # memanggil fungsi image negatif
    elif event == "ImgNegative":
        try:
            window["ImgProcessingType"].update("Image Negative")
            img_output = ImgNegative(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass
    # memanggil fungsi image rotate
    elif event == "ImgRotate":
        try:
            window["ImgProcessingType"].update("Image Rotate")
            img_output = ImgRotate(img_input, coldepth, 90, "C")
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass

    elif event == "ImgBrightness":
        try:
            window["ImgProcessingType"].update("Image Brightness Adjustment")
            brightness_factor = 1.5
            img_output = ImgBrightness(img_input, brightness_factor)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
        except:
            pass


# menambahkan informasi untuk image output
# grafik logaritma di excel
# input 2 citra untuk blending
# membuat brightness dan menurunkan brightness ajust + - slider, menggunakan citra negatif


window.close()
