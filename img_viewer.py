import os.path
from PIL import Image, ImageOps
from processing_list import *
from layout import *


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
    ):  # A file was chosen from the blending image listbox
        try:
            filename_input2 = os.path.join(
                values["ImgFolderBlending"], values["ImgListBlending"][0]
            )
            window["FilepathImgInput2"].update(filename_input2)
            window["ImgInputViewer2"].update(filename=filename_input2)

            img_input2 = Image.open(filename_input2)
            img_output2 = Image.open(filename_input2)
            img_width2, img_height2 = img_input2.size
            window["ImgSize2"].update(
                "Image Size : " + str(img_width2) + " x " + str(img_height2)
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

            coldepth2 = mode_to_coldepth[img_input2.mode]
            window["ImgColorDepth2"].update("Color Depth : " + str(coldepth2))
        except:
            pass

    elif event == "ImgFolderBlending":
        folder_blending = values["ImgFolderBlending"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder_blending)
        except:
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

            img_width, img_height = img_input.size
            window["ImgSize"].update(
                "Image Size : " + str(img_width) + " x " + str(img_height)
            )

            img_width_output, img_height_output = img_output.size
            window["ImgSize_output"].update(
                "Image Size : " + str(img_width_output) + " x " + str(img_height_output)
            )

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
    ]:
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

            img_width, img_height = img_input.size
            window["ImgSize"].update(
                "Image Size : " + str(img_width) + " x " + str(img_height)
            )

            img_width_output, img_height_output = img_output.size
            window["ImgSize_output"].update(
                "Image Size : " + str(img_width_output) + " x " + str(img_height_output)
            )

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

            img_width, img_height = img_input.size
            window["ImgSize"].update(
                "Image Size : " + str(img_width) + " x " + str(img_height)
            )

            img_width_output, img_height_output = img_output.size
            window["ImgSize_output"].update(
                "Image Size : " + str(img_width_output) + " x " + str(img_height_output)
            )

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

    # memanggil fungsi blending
    elif event in [
        "Alpha1",
        "Alpha2",
    ]:
        try:
            if values["ImgListBlending"]:
                filename_blending = os.path.join(
                    values["ImgFolderBlending"], values["ImgListBlending"][0]
                )
                input_image2 = Image.open(filename_blending)

                window["ImgProcessingType"].update("Image Blending")
                alpha = values["Alpha1"]
                alpha2 = values["Alpha2"]
                output_image = blending(
                    img_input, coldepth, input_image2, coldepth, alpha, alpha2
                )  # nilai alpha menjadi 0.5
                output_image.save(filename_out)
                window["ImgOutputViewer"].update(filename=filename_out)

                img_width_output, img_height_output = output_image.size
                window["ImgSize_output"].update(
                    "Image Size : "
                    + str(img_width_output)
                    + " x "
                    + str(img_height_output)
                )

                coldepth_output = mode_to_coldepth[output_image.mode]
                window["ImgColorDepth_output"].update(
                    "Color Depth : " + str(coldepth_output)
                )
            else:
                print("tidak ada file yang diblending.")
        except:
            pass

    # memanggil fungsi imgflip

    elif event in [
        "vertical",
        "horizontal",
        "horizontal-vertical",
    ]:  # A file was chosen from the listbox
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

            window["ImgProcessingType"].update(filename)
            window["ImgOutputViewer"].update(filename=filename)
            img_input = Image.open(filename)

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

            if event == "vertical":
                flip_type = "vertical"
            elif event == "horizontal":
                flip_type = "horizontal"
            elif event == "horizontal-vertical":
                flip_type = "horizontal-vertical"

            window["ImgProcessingType"].update("Image Flip: " + flip_type)
            img_output = ImgFlip(
                img_input, mode_to_coldepth[img_input.mode], 0, flip_type
            )

            filename_out = filename.replace(".", "_output.")
            img_output.save(filename_out)

            window["ImgOutputViewer"].update(filename=filename_out)

            img_width, img_height = img_input.size
            window["ImgSize"].update(
                "Image Size : " + str(img_width) + " x " + str(img_height)
            )

            img_width_output, img_height_output = img_output.size
            window["ImgSize_output"].update(
                "Image Size : " + str(img_width_output) + " x " + str(img_height_output)
            )

            coldepth_output = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth_output"].update(
                "Color Depth : " + str(coldepth_output)
            )

        except:
            pass

    # memanggil fungsi Thresholding
    elif event == "ImgThresholding":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

            window["ImgProcessingType"].update(filename)
            window["ImgOutputViewer"].update(filename=filename)
            img_input = Image.open(filename)
            img_output = Image.open(filename)

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

            window["ImgProcessingType"].update("Thresholding diatur")

            value = values["ImgThresholding"]
            img_output = ImgThreholding(img_input, coldepth, value)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            img_width, img_height = img_input.size
            window["ImgSize"].update(
                "Image Size : " + str(img_width) + " x " + str(img_height)
            )

            img_width_output, img_height_output = img_output.size
            window["ImgSize_output"].update(
                "Image Size : " + str(img_width_output) + " x " + str(img_height_output)
            )

            coldepth_output = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth_output"].update(
                "Color Depth : " + str(coldepth_output)
            )

        except:

            pass

    elif event == "ImgLog":
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
            C = values["ImgLog"]
            img_output = Brightness(img_input, coldepth, C)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            img_width, img_height = img_input.size
            window["ImgSize"].update(
                "Image Size : " + str(img_width) + " x " + str(img_height)
            )

            img_width_output, img_height_output = img_output.size
            window["ImgSize_output"].update(
                "Image Size : " + str(img_width_output) + " x " + str(img_height_output)
            )

            coldepth_output = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth_output"].update(
                "Color Depth : " + str(coldepth_output)
            )

        except:
            pass

    # memanggil fungsi imagetranslasi
    elif event == "ImgTranslationX":
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

            window["ImgProcessingType"].update("Translasi X: ")
            sumbu_x = 50
            img_output = TraslationX(
                img_input,
                coldepth,
                sumbu_x,
            )
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
            img_output.save(filename_out)

            window["ImgOutputViewer"].update(filename=filename_out)

            img_width, img_height = img_input.size
            window["ImgSize"].update(
                "Image Size : " + str(img_width) + " x " + str(img_height)
            )

            img_width_output, img_height_output = img_output.size
            window["ImgSize_output"].update(
                "Image Size : " + str(img_width_output) + " x " + str(img_height_output)
            )

            coldepth_output = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth_output"].update(
                "Color Depth : " + str(coldepth_output)
            )

        except:
            pass

    elif event == "ImgTranslationY":
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

            window["ImgProcessingType"].update("Translasi Y: ")
            sumbu_y = 50

            img_output = TraslationY(
                img_input,
                coldepth,
                sumbu_y,
            )
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
            img_output.save(filename_out)

            window["ImgOutputViewer"].update(filename=filename_out)

            img_width, img_height = img_input.size
            window["ImgSize"].update(
                "Image Size : " + str(img_width) + " x " + str(img_height)
            )

            img_width_output, img_height_output = img_output.size
            window["ImgSize_output"].update(
                "Image Size : " + str(img_width_output) + " x " + str(img_height_output)
            )

            coldepth_output = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth_output"].update(
                "Color Depth : " + str(coldepth_output)
            )

        except:
            pass

    # XY

    elif event == "ImgTranslationXY":
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

            window["ImgProcessingType"].update("Translasi XY: ")
            sumbu_y = 50
            sumbu_x = 10

            img_output = TraslationXY(img_input, coldepth, sumbu_y, sumbu_x)
            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)
            img_output.save(filename_out)

            window["ImgOutputViewer"].update(filename=filename_out)

            img_width, img_height = img_input.size
            window["ImgSize"].update(
                "Image Size : " + str(img_width) + " x " + str(img_height)
            )

            img_width_output, img_height_output = img_output.size
            window["ImgSize_output"].update(
                "Image Size : " + str(img_width_output) + " x " + str(img_height_output)
            )

            coldepth_output = mode_to_coldepth[img_input.mode]
            window["ImgColorDepth_output"].update(
                "Color Depth : " + str(coldepth_output)
            )

        except:
            pass
