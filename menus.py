import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import shutil

def showTweaks(window, rl_path):

    def clearCache():
        cache_path = os.path.expanduser(r"~\Documents\My Games\Rocket League\TAGame\Cache")
        if os.path.exists(cache_path):
            shutil.rmtree(cache_path)
            messagebox.showinfo("Success", "Cache has been deleted.")
        else:
            messagebox.showwarning("Warning", "Cache has not been found.")

        answer = messagebox.askyesno("Delete Saved?", "Would you like to delete .\AppData\Local\EpicGamesLauncher\Saved? (only neccessary if youre having issues starting up RL)")
        savedPath = os.path.expanduser(r"~\AppData\Local\EpicGamesLauncher\Saved")
        if answer and os.path.exists(savedPath):
            messagebox.showwarning("Warning", "Epic Games must be closed and stopped (even in tray)")
            shutil.rmtree(savedPath)
            messagebox.showinfo("Success", "Saved has been deleted.")
        else:
            messagebox.showerror("Error", "Unable to delete Saved.")


        
        
    
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

    confirmPresetsButton = ctk.CTkButton(
        tweaksFrame,
        text="Confirm choices",
        width=120
    )

    backupFrame = ctk.CTkFrame(
        tweaksFrame,
        width=400, height=30,
        fg_color="#101531",
        corner_radius=0
    )

    backupLabel = ctk.CTkLabel(
        tweaksFrame,
        text="Backups:",
        fg_color="#101531"
    )

    createBackupButton = ctk.CTkButton(
        tweaksFrame,
        text="Create Backup",
        width=120
    )

    createBackupEntry = ctk.CTkEntry(
        tweaksFrame,
        placeholder_text="Backup Name",
        width=200
    )

    applyBackupButton = ctk.CTkButton(
        tweaksFrame,
        text="Apply Backup",
        width=120
    )

    applyBackupCombobox = ctk.CTkComboBox(
        tweaksFrame,
        width=200
    )

    miscFrame = ctk.CTkFrame(
        tweaksFrame,
        width=400, height=30,
        fg_color="#101531",
        corner_radius=0
    )

    miscLabel = ctk.CTkLabel(
        tweaksFrame,
        text="Misc:",
        fg_color="#101531"
    )

    clearCacheButton = ctk.CTkButton(
        tweaksFrame,
        text="Clear Cache",
        width=100,
    )

    bakkesButton = ctk.CTkButton(
        tweaksFrame,
        text="BM Textures",
        width=100
    )

    startupEntry = ctk.CTkEntry(
        tweaksFrame,
        placeholder_text="Startup Options",
        width=245
    )

    launchButton = ctk.CTkButton(
        tweaksFrame,
        text="Launch",
        width=100
    )

    buttonColor = "#131524"
    dropDownColor = "#1B1B35"
    borderColor= "#24242E"
    
    tweaksFrame.place(x=200, y=0)

    presetsFrame.place(relx=0.5, rely=0, x=0, y=0, anchor="n")

    cameraLabel.place(relx=0.7, rely=0, x=0, y=0, anchor="n")

    presetCamCombobox.place(relx=0.74, rely=0, x=0, y=35, anchor="n")
    presetCamCombobox.configure(border_color=borderColor, fg_color=buttonColor, dropdown_fg_color=dropDownColor, button_color=borderColor)

    controlsLabel.place(relx=0.20, rely=0, x=0, y=0, anchor="n")

    presetConCombox.place(relx=0.23, rely=0, x=0, y=35, anchor="n")
    presetConCombox.configure(border_color=borderColor, fg_color= buttonColor, dropdown_fg_color=dropDownColor, button_color=borderColor)

    IncludeBindsCheckbox.place(relx=0.215, rely=0, x=0, y=70, anchor="n")
    IncludeBindsCheckbox.configure(border_color = borderColor)

    confirmPresetsButton.place(relx=1, rely=0.28, x=-140, y=0, anchor="w")

    backupFrame.place(relx=0.5, rely=0.35, x=0, y=0, anchor="n")
    
    backupLabel.place(relx=0.2, rely=0.35, x=0, y=0, anchor="n")

    createBackupButton.place(relx=1, rely=0.49, x=-140, y=0, anchor="w")

    createBackupEntry.place(relx=1, rely=0.49, x=-370, y=0, anchor="w")
    createBackupEntry.configure(border_color=borderColor, fg_color= buttonColor)

    applyBackupButton.place(relx=1, rely=0.60, x=-140, y=0, anchor="w")

    applyBackupCombobox.place(relx=1, rely=0.60, x=-370, y=0, anchor="w")
    applyBackupCombobox.configure(border_color=borderColor, fg_color= buttonColor, dropdown_fg_color=dropDownColor, button_color=borderColor)

    miscFrame.place(relx=0.5, rely=0.67, x=0, y=0, anchor="n")

    miscLabel.place(relx=0.2, rely=0.67, x=0, y=0, anchor="n")

    clearCacheButton.place(relx=0.2, rely= 0.78, x=0, y=0, anchor="n")
    clearCacheButton.bind("<Button-1>", lambda e:clearCache())

    bakkesButton.place(relx=0.5, rely= 0.78, x=0, y=0, anchor="n")

    startupEntry.place(relx=0.38, rely= 0.89, x=0, y=0, anchor="n")
    startupEntry.configure(border_color=borderColor, fg_color= buttonColor)

    launchButton.place(relx=0.8, rely=0.89, x=0, y=0, anchor="n")
    
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
        fg_color="#0b0f22", 
        corner_radius=0,
    )
    skinsChangerFrame.place(x=200, y=0)

    return skinsChangerFrame

  
   



