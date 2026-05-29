import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

tweaksFrame = None
mapChangerFrame = None
skinChangerFrame = None

def setup(window):
    global tweaksFrame, mapChangerFrame, skinChangerFrame
    
    tweaksFrame = ctk.CTkFrame(
        window,
        width=400, height=400,
        fg_color="#2b2b2b",
        corner_radius=0,
    )
    tweaksFrame.place(x=200, y=0)

    mapChangerFrame = ctk.CTkFrame(
        window,
        width=400, height=400,
        fg_color="#2b2b2b",
        corner_radius=0,
    )
    mapChangerFrame.place(x=200, y=0)

    skinChangerFrame = ctk.CTkFrame(
        window,
        width=400, height=400,
        fg_color="#2b2b2b",
        corner_radius=0,
    )
    skinChangerFrame.place(x=200, y=0)

def showTweaks(e):
    tweaksFrame.lift()

def showMapChanger(e):
    mapChangerFrame.lift()

def showSkinChanger(e):
    skinChangerFrame.lift()