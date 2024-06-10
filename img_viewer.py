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
    elif event in ["Alpha1", "Alpha2"]:
        try:
            if values["ImgListBlending"]:
                filename_blending = os.path.join(
                    values["ImgFolderBlending"], values["ImgListBlending"][0]
                )
                input_image2 = Image.open(filename_blending)

                window["ImgProcessingType"].update("Image Blending")

                try:
                    alpha = float(values["Alpha1"])
                    alpha2 = float(values["Alpha2"])
                except ValueError:
                    print("Alpha values must be numbers.")
                    continue

                output_image = blending(
                    img_input, coldepth, input_image2, coldepth, alpha, alpha2
                )
                filename_out = os.path.join(
                    values["ImgFolderBlending"], ".", "_output."
                )
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
                print("No files selected for blending.")
        except Exception as e:
            print(f"An error occurred: {e}")

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
            img_output = ImgFlip(img_input, mode_to_coldepth[img_input.mode], flip_type)

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

            window["ImgProcessingType"].update("Img Log")
            C = values["ImgLog"]
            img_output = Logarithmic(img_input, coldepth, C)
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

    # memanggil fungsi image translasi
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
            sumbu_x = 30

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

        # img scaliing // shrinking

    elif event == "ShrinkingImg":
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

            window["ImgProcessingType"].update("Shrinking diatur ")
            scaling = values["ShrinkingImg"]
            img_output = Shrinking(img_input, coldepth, scaling)
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

    elif event == "ZoomIn":
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

            window["ImgProcessingType"].update("Zoom In diatur")
            scaling = values["ZoomIn"]
            img_output = ZoomIn(img_input, coldepth, scaling)
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

    # median filter
    elif event == "Median":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

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

            window["ImgProcessingType"].update("Median diatur")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = median(img_input, coldepth)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

        # median filter

    elif event == "Mean":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

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

            window["ImgProcessingType"].update("Mean diatur")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = mean(img_input, coldepth)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

    elif event == "PowerLaw":
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

            window["ImgProcessingType"].update("Power Law")
            img_output = PowerLawoperasion(img_input, coldepth, C=1, gamma=0.5)
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

    # ZoomNegativeRotateFlipBlend
    elif event == "ZoomNegativeRotateFlipBlend":
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

            window["ImgProcessingType"].update("ZNRFB")
            scaling = 2

            # mengatur nilai output processing
            img_output = ZNRFB(img_input, mode_to_coldepth[img_input.mode], scaling)
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

        except Exception as e:
            print("An error occurred:", e)

    elif event == "gradien1":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

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

            window["ImgProcessingType"].update("edge detector gradient")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = gradien1(img_input, coldepth)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

    elif event == "gx_sobel":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

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

            window["ImgProcessingType"].update("sobel_gx")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = sobel_gx(img_input, coldepth)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

    elif event == "gy_sobel":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

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

            window["ImgProcessingType"].update("sobel_gycl")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = sobel_gy(img_input, coldepth)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

    elif event == "gx_sobel":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

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

            window["ImgProcessingType"].update("sobel_gy")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = sobel_gx(img_input, coldepth)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

    elif event == "sobel":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

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

            window["ImgProcessingType"].update("sobel")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = sobel(img_input, coldepth)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

    ### PREWITT

    elif event == "gx_prewitt":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

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

            window["ImgProcessingType"].update("gx_prewitt")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = prewitt_gx(img_input, coldepth)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

    elif event == "gy_prewitt":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

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

            window["ImgProcessingType"].update("gy_prewitt")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = prewitt_gy(img_input, coldepth)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

    elif event == "prewitt":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

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

            window["ImgProcessingType"].update("prewitt")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = prewitt_edge(img_input, coldepth)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

    elif event == "gx_robert":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

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

            window["ImgProcessingType"].update("gx_robert")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = robert_operator_gx(img_input, coldepth)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

    elif event == "gy_robert":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

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

            window["ImgProcessingType"].update("gy_robert")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = robert_operator_gy(img_input, coldepth)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

    elif event == "robert":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

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

            window["ImgProcessingType"].update("robert")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = robert(img_input, coldepth)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

    # Laplacian

    elif event == "Laplacian":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

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

            window["ImgProcessingType"].update("laplacian")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = laplacian(img_input, coldepth)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

    # KOMPAS
    elif event == "kompas":
        try:
            window["FilepathImgInput"].update(filename)

            window["ImgInputViewer"].update(filename=filename)

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

            window["ImgProcessingType"].update("kompas")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = kompas(img_input, coldepth)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

    # noise

    elif event in ["GaussianNoise", "SaltNoise", "PepperNoise", "SaltAndPepperNoise"]:
        try:
            window["FilepathImgInput"].update(filename)
            window["ImgInputViewer"].update(filename=filename)

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

            window["ImgProcessingType"].update(event)
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = img_input.copy()
            if event == "GaussianNoise":
                std_dev = values["GaussianNoise"]
                img_output = add_gaussian_noise(img_output, mean=0, std_dev=std_dev)
            elif event == "SaltNoise":
                salt_prob = values["SaltNoise"] / 100.0
                img_output = add_salt_noise(img_output, salt_prob=salt_prob)
            elif event == "PepperNoise":
                pepper_prob = values["PepperNoise"] / 100.0
                img_output = add_pepper_noise(img_output, pepper_prob=pepper_prob)
            elif event == "SaltAndPepperNoise":
                salt_and_pepper_prob = values["SaltAndPepperNoise"] / 100.0
                img_output = add_salt_and_pepper_noise(
                    img_output,
                    salt_prob=salt_and_pepper_prob,
                    pepper_prob=salt_and_pepper_prob,
                )

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except:
            pass

    if event in [
        "median_3x3",
        "median_5x5",
        "median_7x7",
        "median_9x9",
        "median_loop_3x3",
        "gaussian_3x3",
        "gaussian_5x5",
        "gaussian_7x7",
        "gaussian_9x9",
        "gaussian_loop_3x3",
        "mean_3x3",
        "mean_5x5",
        "mean_7x7",
        "mean_9x9",
        "mean_loop_3x3",
    ]:
        try:
            window["FilepathImgInput"].update(filename)
            window["ImgInputViewer"].update(filename=filename)

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

            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            if event.startswith("median"):
                if "3x3" in event:
                    kernel_size = 3
                elif "5x5" in event:
                    kernel_size = 5
                elif "7x7" in event:
                    kernel_size = 7
                elif "9x9" in event:
                    kernel_size = 9
                if "loop" in event:
                    img_output = loop_3x3_filter(img_input, median_filter, 3)
                else:
                    img_output = median_filter(img_input, kernel_size)
            elif event.startswith("gaussian"):
                if "3x3" in event:
                    kernel_size = 3
                elif "5x5" in event:
                    kernel_size = 5
                elif "7x7" in event:
                    kernel_size = 7
                elif "9x9" in event:
                    kernel_size = 9
                if "loop" in event:
                    img_output = loop_3x3_filter(img_input, gaussian_filter, 3)
                else:
                    img_output = gaussian_filter(img_input, kernel_size)
            elif event.startswith("mean"):
                if "3x3" in event:
                    kernel_size = 3
                elif "5x5" in event:
                    kernel_size = 5
                elif "7x7" in event:
                    kernel_size = 7
                elif "9x9" in event:
                    kernel_size = 9
                if "loop" in event:
                    img_output = loop_3x3_filter(img_input, mean_filter, 3)
                else:
                    img_output = mean_filter(img_input, kernel_size)

            img_output.save(filename_out)
            window["ImgOutputViewer"].update(filename=filename_out)

            img_width, img_height = img_input.size
            window["ImgSize"].update(f"Image Size: {img_width} x {img_height}")

            img_width_output, img_height_output = img_output.size
            window["ImgSize_output"].update(
                f"Output Image Size: {img_width_output} x {img_height_output}"
            )

            window["ImgColorDepth"].update(f"Color Depth: {coldepth}")
            window["ImgColorDepth_output"].update(f"Output Color Depth: {coldepth}")

        except Exception as e:
            sg.popup_error(f"Error processing image: {e}")

    elif event == "MaxFilter":
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

            window["ImgProcessingType"].update("MaxFilter")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = max_filter(img_input)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except Exception as e:
            print(f"Error: {e}")

    elif event == "MinFilter":
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

            window["ImgProcessingType"].update("MinFilter")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = min_filter(img_input)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except Exception as e:
            print(f"Error: {e}")

    elif event == "Erosi":
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

            window["ImgProcessingType"].update("Erosi")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = erosi(img_input)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except Exception as e:
            print(f"Error: {e}")

    elif event == "Dilasi":
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

            window["ImgProcessingType"].update("Dilasi")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = dilasi(img_input)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except Exception as e:
            print(f"Error: {e}")

    elif event == "White top hat":
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

            window["ImgProcessingType"].update("White top head")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = white_top_hat(img_input)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except Exception as e:
            print(f"Error: {e}")

    elif event == "Black top head":
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

            window["ImgProcessingType"].update("Black top head")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = black_top_hat(img_input)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except Exception as e:
            print(f"Error: {e}")

    elif event == "Closing":
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

            window["ImgProcessingType"].update("Closing")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = closing(img_input)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except Exception as e:
            print(f"Error: {e}")

    elif event == "Opening":
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

            window["ImgProcessingType"].update("Opening")
            img_input = Image.open(filename)
            coldepth = mode_to_coldepth[img_input.mode]

            img_output = opening(img_input)

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

            window["ImgColorDepth_output"].update("Color Depth : " + str(coldepth))

        except Exception as e:
            print(f"Error: {e}")
