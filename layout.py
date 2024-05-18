import PySimpleGUI as sg

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
        sg.Text("Image Information Img 1:"),
    ],
    [
        sg.Text(size=(18, 1), key="ImgSize"),
    ],
    [
        sg.Text(size=(18, 1), key="ImgColorDepth"),
    ],
    [
        sg.Text("Image Information Img 2:"),
    ],
    [
        sg.Text(size=(18, 1), key="ImgSize2"),
    ],
    [
        sg.Text(size=(18, 1), key="ImgColorDepth2"),
    ],
    [],
    [
        sg.Text(" "),
        sg.Text("List of Processing:"),
    ],
    [
        sg.Button("Negative", size=(10, 1), key="ImgNegative"),
    ],
    [
        sg.Text("Img Rotate"),
        sg.Button("90", size=(4, 1), key="ImgRotate90"),
        sg.Button("180", size=(4, 1), key="ImgRotate180"),
        sg.Button("270", size=(4, 1), key="ImgRotate270"),
    ],
    [
        sg.Text("Brightness:"),
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
        sg.Text("Img Blending: "),
    ],
    [
        sg.Text("Value Img Alpha 1: "),
        sg.Slider(
            range=(0.0, 2),
            default_value=0,
            size=(15, 10),
            orientation="horizontal",
            key="Alpha1",
            enable_events=True,
            resolution=0.01,
        ),
    ],
    [
        sg.Text("Value Img Alpha 2: "),
        sg.Slider(
            range=(0.0, 2),
            default_value=0,
            size=(15, 10),
            orientation="horizontal",
            key="Alpha2",
            enable_events=True,
            resolution=0.01,
        ),
    ],
    [
        sg.Text("Flip"),
        sg.Button("H", size=(4, 1), key="horizontal"),
        sg.Button("V", size=(4, 1), key="vertical"),
        sg.Button("H-V", size=(5, 1), key="horizontal-vertical"),
    ],
    [
        sg.Text("Thresholding: "),
        sg.Slider(
            range=(0, 255),
            default_value=0,
            size=(15, 10),
            orientation="horizontal",
            key="ImgThresholding",
            enable_events=True,
        ),
    ],
    [
        sg.Text("Logarithmic: "),
        sg.Slider(
            range=(0, 255),
            default_value=0,
            size=(15, 10),
            orientation="horizontal",
            key="ImgLog",
            enable_events=True,
        ),
    ],
    [
        sg.Text("Img Translation "),
        sg.Button("TX", size=(5, 1), key="ImgTranslationX"),
        sg.Button("TY", size=(5, 1), key="ImgTranslationY"),
        sg.Button("TXY", size=(5, 1), key="ImgTranslationXY"),
    ],
    [
        sg.Text("Zoom In: "),
        sg.Slider(
            range=(0.0, 4),
            default_value=0,
            size=(15, 10),
            orientation="horizontal",
            key="ZoomIn",
            enable_events=True,
        ),
    ],
    [
        sg.Text("Shrinking: "),
        sg.Slider(
            range=(0.0, 6),
            default_value=0,
            size=(15, 10),
            orientation="horizontal",
            key="ShrinkingImg",
            enable_events=True,
        ),
    ],
    [
        sg.Button("median", size=(8, 1), key="Median"),
        sg.Button("mean", size=(6, 1), key="Mean"),
    ],
    [
        sg.Button("powerlaw", size=(8, 1), key="PowerLaw"),
    ],
    [
        sg.Button(
            "ZNRFB",
            size=(10, 1),
            key="ZoomNegativeRotateFlipBlend",
        ),
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
