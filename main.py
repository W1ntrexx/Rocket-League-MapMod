import winreg
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import webbrowser
import menus
import json

main = ctk.CTk()
main.geometry("600x400")
main.title("RocketLeague MapMod - RLMM")
main.resizable(False, False)

if not os.path.exists("settings.png") or not os.path.exists("RLmmBG.png"):
    messagebox.showerror("Error", "Missing required image files.")
    main.destroy()

if not os.path.exists("firstTimeRun.txt"):
    messagebox.showinfo("Warning", "This program is in early development and may contain bugs. Please report any issues to the developer.\nFurthermore, hes not resposible for any damage")
    with open("firstTimeRun.txt", "w") as f:
        pass

def find_RL_epic():
    possible_paths = [
        r"SOFTWARE\Epic Games\EpicGamesLauncher",                  # 64-Bit Ort
        r"SOFTWARE\WOW6432Node\Epic Games\EpicGamesLauncher"
    ]
    for path in possible_paths:
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
            data_path = winreg.QueryValueEx(key, "AppDataPath")[0]
            winreg.CloseKey(key)
            print(data_path)
            
        
        except FileNotFoundError:
            continue
    if not data_path:
        print("Epic Games Launcher not found in registry.")

    manifest_path = os.path.join(data_path, "Manifests")
    if os.path.exists(manifest_path):
        for file in os.listdir(manifest_path):
            if file.endswith(".item"):
                with open(os.path.join(manifest_path, file), "r") as f:
                    content = f.read()
                    if "Rocket League" in content:
                        print("Rocket League found in Epic Games Launcher.")
                        
                with open(os.path.join(manifest_path, file), "r") as f:
                    daten = json.load(f)

                    displayName = daten.get("InstallLocation","")
                    if daten.get:
                        print("Path found: " + displayName)
                        break
                                                 
                
def find_RL_steam():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Valve\Steam")
        data_path = winreg.QueryValueEx(key, "SteamPath")[0]
        winreg.CloseKey(key)
        print(data_path)
    
    except FileNotFoundError:
        return None
    
find_RL_epic()


menuColour= "#131b28"

menu_frame = ctk.CTkFrame(
main, 
width=200, 
height=400,
fg_color=menuColour,
corner_radius=0
)

info_image_raw = Image.open("InfoIcon.png").resize((45, 30))
info_image = ImageTk.PhotoImage(info_image_raw)

infoLabel = tk.Label(
main,
image=info_image, 
bg="#04050b",
)

def infoBox():
    messagebox.showinfo("Info", "This Programm works by switching files. If you encounter any issues while launching the game, verify the integrity of your game files in the epic games launcher or steam. This method is not bannable but use at your own risk.")

infoLabel.configure(cursor="hand2")
infoLabel.bind("<Button-1>", lambda e: infoBox())

homeButton = ctk.CTkButton(
main,
width=200,
height=70,
fg_color=menuColour,
corner_radius=0,
text="Home",
font=("Arial", 20, "bold"),
)

homeButton.configure(cursor="hand2")
homeButton.bind("<Button-1>", ) #missing command

changerMapButton = ctk.CTkButton(
main,
width=200,
height=70,
fg_color=menuColour,
corner_radius=0,
text="Change Map",
font=("Arial", 20, "bold"),
)

changerMapButton.configure(cursor="hand2")
changerMapButton.bind("<Button-1>", ) #missing command

changerSkinsButton = ctk.CTkButton(
main,
width=200,
height=70,
fg_color=menuColour,
corner_radius=0,
text="Change Skins",
font=("Arial", 20, "bold"),
)

changerSkinsButton.configure(cursor="hand2")
changerSkinsButton.bind("<Button-1>", ) #missing command

tweaksButton = ctk.CTkButton(
main,
width=200,
height=70,
fg_color=menuColour,
corner_radius=0,
text="Tweaks",
font=("Arial", 20, "bold"),
)

tweaksButton.configure(cursor="hand2")
tweaksButton.bind("<Button-1>", lambda e: menus.showTweaks(main))

creditsButton = ctk.CTkButton(
main,
width=200,
height=70,
fg_color=menuColour,
corner_radius=0,
text="Credits",
font=("Arial", 20, "bold"),
)

creditsButton.configure(cursor="hand2")
creditsButton.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/W1ntrexx/Rocket-League-MapMod"))

statusColor = "#06090D"

status_frame = ctk.CTkFrame(
main,
width=200,
height=50,
fg_color=statusColor,
corner_radius=0
)

sett_image_raw = Image.open("settings.png").resize((30, 30))
sett_image = ImageTk.PhotoImage(sett_image_raw)

settLabel = tk.Label(
main,
image=sett_image, 
bg="#030409",
)

bg_Image = ctk.CTkImage(
    light_image=Image.open("RLmmBG.png"),
    dark_image=Image.open("RLmmBG.png"),
    size=(600, 400)
)

bg_Label = ctk.CTkLabel(
main,
image=bg_Image, 
text="",
fg_color="transparent",
bg_color="black",
)

statusLabel = ctk.CTkLabel(
    main,
    text="Status: ",
    font=("Arial", 20, "bold"),
    fg_color="transparent",  
    bg_color=statusColor,
    text_color="white"
)

curStatus = "online" # idle, online, offline

if(curStatus == "idle"):
    textColor = "white"
    statText = "Idling"
elif(curStatus == "online"):
    textColor = "green"
    statText = "Running"
else:
    textColor = "red"
    statText = "Offline"

curStatusLabel = ctk.CTkLabel(
    main,
    text=statText,
    font=("Arial", 20, "bold"),
    fg_color="transparent",  
    bg_color=statusColor,
    text_color=textColor
)


bg_Label.place(x=0, y=0, relwidth=1, relheight=1)
bg_Label.lower()

menu_frame.place(x=0, y=0, relheight=1)

homeButton.place(x=0, y=0)
changerMapButton.place(x=0, y=70)
changerSkinsButton.place(x=0, y=140)
tweaksButton.place(x=0, y=210)
creditsButton.place(x=0, y=280)

status_frame.place(relx=1.0, rely=1.0, x=-400, y=-0, anchor="se")

infoLabel.place(relx=1.0, y=10, x=-50, anchor="ne")

settLabel.place(relx=1.0, y=10, x=-10, anchor="ne")
settLabel.configure(cursor="hand2")
settLabel.bind("<Button-1>", ) #missing command

statusLabel.place(rely=1.0, x=10, y=-12, anchor="sw")
curStatusLabel.place(rely=1.0, x=90, y=-12, anchor="sw")

main.mainloop()