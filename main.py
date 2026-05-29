import customtkinter as ctk
import tkinter as tk
from PIL import Image

main = ctk.CTk()
main.geometry("600x400")
main.title("RocketLeague MapMod - RLMM")
main.resizable(False, False)

bg_Image = ctk.CTkImage(
    light_image=Image.open("RLmmBG.png"),
    dark_image=Image.open("RLmmBG.png"),
    size=(600, 400)
)

bg_Label = ctk.CTkLabel(
main,
image=bg_Image, 
text=""
)

statusLabel = ctk.CTkLabel(
    main,
    text="Status: ",
    font=("Arial", 20, "bold"),
    fg_color="transparent",  
    bg_color="black",
    text_color="white"
)

textColor = "white"

curStatusLabel = ctk.CTkLabel(
    main,
    text="Idle",
    font=("Arial", 20, "bold"),
    fg_color="transparent",  
    bg_color="black",
    text_color=textColor
)


bg_Label.place(x=0, y=0, relwidth=1, relheight=1)
statusLabel.place(rely=1.0, x=10, y=-10, anchor="sw")
curStatusLabel.place(rely=1.0, x=90, y=-10, anchor="sw")



main.mainloop()