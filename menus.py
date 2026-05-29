import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

def showTweaks(window):
    global tweaksFrame, mapChangerFrame, skinChangerFrame
    
    tweaksFrame = ctk.CTkFrame(
        window,
        width=400, height=400,
        fg_color="#2b2b2b",
        corner_radius=0,
    )
    tweaksFrame.place(x=200, y=0)



