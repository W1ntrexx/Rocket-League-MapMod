import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

def showTweaks(window):
    
    tweaksFrame = ctk.CTkFrame(
        window,
        width=400, height=400,
        fg_color="#0b0f22",
        corner_radius=0,
    )

    presetsFrame = ctk.CTkFrame(
        tweaksFrame,
        width=400, height=30,
        fg_color="#101531",
        corner_radius=0
    )

    cameraLabel = ctk.CTkLabel(
        tweaksFrame,
        text="Camera Presets:",
        bg_color="#101531",
    )
    
    presetCamCombobox = ctk.CTkComboBox(
        tweaksFrame,
        width=120
    )

    controlsLabel = ctk.CTkLabel(
        tweaksFrame,
        text="Controller Presets:",
        bg_color="#101531",
    )

    presetConCombox = ctk.CTkComboBox(
        tweaksFrame,
        width=120
    )

    IncludeBindsCheckbox = ctk.CTkCheckBox(
        tweaksFrame,
        text="Include binds"
    )
    
    tweaksFrame.place(x=200, y=0)
    presetsFrame.place(relx=0.5, rely=0, x=0, y=0, anchor="n")
    cameraLabel.place(relx=0.20, rely=0, x=0, y=0, anchor="n")
    presetCamCombobox.place(relx=0.23, rely=0, x=0, y=35, anchor="n")
    controlsLabel.place(relx=0.7, rely=0, x=0, y=0, anchor="n")
    presetConCombox.place(relx=0.72, rely=0, x=0, y=35, anchor="n")
    IncludeBindsCheckbox.place(relx=0.70, rely=0, x=0, y=70, anchor="n")
    
    
    return tweaksFrame



def showMapChanger(window):
    mapChangerFrame = ctk.CTkFrame(
        window,
        width=400, height=400,
        fg_color="#0b0f22",
        corner_radius=0,
    )
    mapChangerFrame.place(x=200, y=0)

    mapScrollFrame = ctk.CTkScrollableFrame(
        mapChangerFrame,
        width=380, height=380,
        fg_color="#0b0f22",
        corner_radius=0,
    )
    mapScrollFrame.place(x=0, y=0)

    maps = ["Map A", "Map B", "Map C", "Map D", "Map E", "Map F", "Map G", "Map H", "Map I", "Map J"]

    for i, map_name in enumerate(maps):
        row = i //3
        col = i % 3

        mapButton = ctk.CTkButton(
            mapScrollFrame,
            width=100, height=80,
        )
        mapButton.grid(row=row, column=col, padx=5, pady=5)

    return mapChangerFrame

def showSkinsChanger(window):
    skinsChangerFrame = ctk.CTkFrame(
        window,
        width=400, height=400,
        fg_color="#2b2b2b",
        corner_radius=0,
    )
    skinsChangerFrame.place(x=200, y=0)

    return skinsChangerFrame

  
   



