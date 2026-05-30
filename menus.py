import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

def showTweaks(window):
    
    tweaksFrame = ctk.CTkFrame(
        window,
        width=400, height=400,
        fg_color="#2b2b2b",
        corner_radius=0,
    )
    
    presetCombobox = ctk.CTkComboBox(
        tweaksFrame,
        width=10
    )
    
    tweaksFrame.place(x=200, y=0)
    presetCombobox.place(x=220, y=50)

    return tweaksFrame



def showMapChanger(window):
    mapChangerFrame = ctk.CTkFrame(
        window,
        width=400, height=400,
        fg_color="#2b2b2b",
        corner_radius=0,
    )
    mapChangerFrame.place(x=200, y=0)

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

  
    return tweaksFrame



