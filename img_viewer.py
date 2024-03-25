import PySimpleGUI as sg
import os.path
from PIL import Image, ImageOps
from processing_list import *

background_color = "#F5EEE6"

# Kolom Area No 1: Area membuka folder dan memilih gambar
file_list_column = [
    [
        sg.Text("Buka Folder :"),
    ],
    [
        sg.In(size=(10, 1), enable_events=True, key="ImgFolder"),
        sg.FolderBrowse("pilih"),
    ],
    [
        sg.Text("Pilih Gambar:"),
    ],
    [sg.Listbox(values=[], enable_events=True, size=(10, 5), key="ImgList")],
]

file_list_column_blending = [
    [
        sg.Text("Buka Folder :"),
    ],
    [
        sg.In(size=(10, 1), enable_events=True, key="ImgFolderBlending"),
        sg.FolderBrowse("pilih"),
    ],
    [
        sg.Text("Pilih Gambar Blending:"),
    ],
    [sg.Listbox(values=[], enable_events=True, size=(10, 5), key="ImgListBlending")],
]

# Kolom Area No 2: menampilkan input gambar
image_viewer_column = [
    [sg.Text("Image Input :")],
    [sg.Text(size=(15, 1), key="FilepathImgInput")],
    [sg.Image(key="ImgInputViewer")],
]

image_viewer_column_input2 = [
    [sg.Text("Image Input 2:")],
    [sg.Text(size=(15, 1), key="FilepathImgInput2")],
    [sg.Image(key="ImgInputViewer2")],
]


# Kolom Area No 3: informasi gambar untuk kolom input
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
        sg.Button("Image Negative", size=(15, 1), key="ImgNegative"),
    ],
    [
        sg.Button("Image Rotate 90", size=(15, 1), key="ImgRotate90"),
    ],
    [
        sg.Button("Image Rotate 180", size=(15, 1), key="ImgRotate180"),
    ],
    [
        sg.Button("Image Rotate 270", size=(15, 1), key="ImgRotate270"),
    ],
    [
        sg.Text("Atur Brightness: "),
        sg.Slider(
            range=(-255, 255),
            default_value=0,
            size=(15, 10),
            orientation="horizontal",
            key="BrightnessSlider",
            enable_events=True,
        ),
    ],
    [
        sg.Button(
            "Image Blending",
            size=(15, 1),
            key="ImgBlending",
        )
    ],
]


# Kolom Area No 4: Area viewer image output
image_viewer_column2 = [
    [sg.Text("Image Processing output:")],
    [sg.Text(size=(15, 1), key="ImgProcessingType")],
    [sg.Image(key="ImgOutputViewer")],
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

# Gabung Full layout tata letak setiap colom
layout = [
    [
        sg.Column(
            [[sg.Column(file_list_column)], [sg.Column(file_list_column_blending)]]
        ),
        sg.VSeperator(),
        sg.Column(image_viewer_column2),
        sg.VSeperator(),
        sg.Column(list_processing),
        sg.VSeperator(),
        sg.Column(
            [[sg.Column(image_viewer_column)], [sg.Column(image_viewer_column_input2)]]
        ),
    ],
]

window = sg.Window("Mini Image Editor", layout, background_color=background_color)


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

    elif (
        event == "ImgListBlending"
    ):  # A file was chosen from the listbox for Input Image 2
        try:
            filename_input2 = os.path.join(
                values["ImgFolderBlending"], values["ImgListBlending"][0]
            )
            window["FilepathImgInput2"].update(filename_input2)
            window["ImgInputViewer2"].update(filename=filename_input2)
        except:
            pass

    elif event == "ImgFolderBlending":
        folder_blending = values["ImgFolderBlending"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder_blending)
        except Exception as e:
            print("Error:", e)
            file_list = []

        fnamesblending = [
            fb
            for fb in file_list
            if os.path.isfile(os.path.join(folder_blending, fb))
            and fb.lower().endswith((".png", ".gif"))
        ]
        window["ImgListBlending"].update(fnamesblending)

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

    # memanggil fungsi image negatif
    elif event == "ImgNegative":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

            window["ImgProcessingType"].update(filename)
            window["ImgOutputViewer"].update(filename=filename)
            img_input = Image.open(filename)
            img_output = Image.open(filename)

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

            window["ImgProcessingType"].update("Image Negative")
            img_output = ImgNegative(img_input, coldepth)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            # Update informasi ukuran gambar input
            img_width, img_height = img_input.size
            window["ImgSize"].update(
                "Image Size : " + str(img_width) + " x " + str(img_height)
            )

            # Update informasi ukuran gambar output
            img_width_output, img_height_output = img_output.size
            window["ImgSize_output"].update(
                "Image Size : " + str(img_width_output) + " x " + str(img_height_output)
            )

            # Update informasi kedalaman warna gambar output
            coldepth_output = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth_output"].update(
                "Color Depth : " + str(coldepth_output)
            )

        except:
            pass

    # memanggil fungsi image rotate dan ukuran sesuai rotate
    elif event in [
        "ImgRotate90",
        "ImgRotate180",
        "ImgRotate270",
    ]:  # A file was chosen from the listbox
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

            window["ImgProcessingType"].update(filename)
            window["ImgOutputViewer"].update(filename=filename)
            img_input = Image.open(filename)
            img_output = Image.open(filename)

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

            rotation_angle = (
                90
                if event == "ImgRotate90"
                else (180 if event == "ImgRotate180" else 270)
            )
            rotation_direction = (
                "C"
                if event == "ImgRotate90"
                else ("180" if event == "ImgRotate180" else "CCW")
            )

            window["ImgProcessingType"].update("Image Rotate")
            img_output = ImgRotate(
                img_input, coldepth, rotation_angle, rotation_direction
            )
            window["ImgOutputViewer"].update(filename=filename_out)
            img_output.save(filename_out)

            window["ImgOutputViewer"].update(filename=filename_out)

            # Update informasi ukuran gambar input
            img_width, img_height = img_input.size
            window["ImgSize"].update(
                "Image Size : " + str(img_width) + " x " + str(img_height)
            )

            # Update informasi ukuran gambar output
            img_width_output, img_height_output = img_output.size
            window["ImgSize_output"].update(
                "Image Size : " + str(img_width_output) + " x " + str(img_height_output)
            )

            # Update informasi kedalaman warna gambar output
            coldepth_output = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth_output"].update(
                "Color Depth : " + str(coldepth_output)
            )

        except:
            pass

    # memanggil fungsi brightness
    elif event == "BrightnessSlider":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

            window["ImgProcessingType"].update(filename)
            window["ImgOutputViewer"].update(filename=filename)
            img_input = Image.open(filename)
            img_output = Image.open(filename)

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

            window["ImgProcessingType"].update("Brightness diatur")
            tingkat_brightness = values["BrightnessSlider"]
            img_output = Brightness(img_input, coldepth, tingkat_brightness)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            # Update informasi ukuran gambar input
            img_width, img_height = img_input.size
            window["ImgSize"].update(
                "Image Size : " + str(img_width) + " x " + str(img_height)
            )

            # Update informasi ukuran gambar output
            img_width_output, img_height_output = img_output.size
            window["ImgSize_output"].update(
                "Image Size : " + str(img_width_output) + " x " + str(img_height_output)
            )

            # Update informasi kedalaman warna gambar output
            coldepth_output = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth_output"].update(
                "Color Depth : " + str(coldepth_output)
            )

        except:
            pass

    # membuat folder untuk blending

    elif event == "ImgFolderBlending":
        folder_blending = values["ImgFolderBlending"]
        try:
            file_list = os.listdir(folder_blending)
        except Exception as e:
            print("Error:", e)
            file_list = []

        fnamesblending = [
            fb
            for fb in file_list
            if os.path.isfile(os.path.join(folder_blending, fb))
            and fb.lower().endswith((".png", ".gif"))
        ]
        window["ImgListBlending"].update(fnamesblending)

    elif event == "ImgBlending":
        try:
            if values["ImgListBlending"]:
                filename_blending = os.path.join(
                    values["ImgFolderBlending"], values["ImgListBlending"][0]
                )
                input_image2 = Image.open(filename_blending)

                window["ImgProcessingType"].update("Image Blending")
                output_image = blending(
                    img_input, coldepth, input_image2, coldepth, 0.5, 0.5
                )  # nilai alpha menjadi 0.5
                output_image.save(filename_out)
                window["ImgOutputViewer"].update(filename=filename_out)

                # Update informasi ukuran gambar output blending
                img_width_output, img_height_output = output_image.size
                window["ImgSize_output"].update(
                    "Image Size : "
                    + str(img_width_output)
                    + " x "
                    + str(img_height_output)
                )

                # Update informasi kedalaman warna gambar output blending
                coldepth_output = mode_to_coldepth[output_image.mode]
                window["ImgColorDepth_output"].update(
                    "Color Depth : " + str(coldepth_output)
                )
            else:
                print("tidak ada file yang diblending.")
        except:
            pass
