import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import shutil

def showTweaks(window, rl_path, curStatus):

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
            try:
                shutil.rmtree(savedPath)
                messagebox.showinfo("Success", "Saved has been deleted.")
            except:
                messagebox.showerror("Error", "Unable to delete Saved.")
                print("Permission error: Programm was denied access.")
        
        

    def createBackup():
        if not os.path.exists("backups"):
            os.mkdir("backups")
        if createBackupEntry.get().strip() == "":
            messagebox.showwarning("Warning", "Cannot save with empty name.")
            return
        backupName = createBackupEntry.get().strip()
        
        saveDataPath = os.path.expanduser(r"~\Documents\My Games\Rocket League\TAGame\SaveDataEpic\DBE_Production")
        
        try:  #versucht zu copy pasten, ansonsten Fehlerausgabe
            shutil.copytree(saveDataPath, fr"backups\{backupName}")
            messagebox.showinfo("Saved.", f"Successfully saved backup under {backupName}")
            applyBackupCombobox.configure(values=readBackups()) #aktualisiert applyBackupCombobox
        except:
            messagebox.showerror("Error", "Unable to make backup file.")

    def readBackups():
        backupList = []

        if os.path.exists("backups"):
            for eintrag in os.listdir("backups"):
                backupList.append(str(eintrag))

        return backupList
    
    def applyBackup(chosenBackup):
        if not os.path.exists("backups"):
            messagebox.showwarning("Uh oh...", "No backup folder has been found.")
            return
        if chosenBackup == "Select backup...":
            messagebox.showwarning("Uh oh...", "You have not selected a backup.")
            return
        sourcePath = os.path.join("backups/", chosenBackup)
        saveDataPath = os.path.expanduser(r"~\Documents\My Games\Rocket League\TAGame\SaveDataEpic\DBE_Production")
        print(sourcePath)
        if curStatus == "online":
            if messagebox.askyesno("Hold on", "It seems that an instance of Rocket League or Epic Games is running. Modifying files currently could cause unwanted behaviour. Wish to continue?"):
                try:
                    shutil.copytree(sourcePath, saveDataPath, dirs_exist_ok=True)
                    messagebox.showinfo("Horray", "Successfully applied backup")
                except:
                    messagebox.showerror("Uh oh...", "Unable to apply backup.")
        
                
    def installBakkesTextures():
        texture_path = os.path.expanduser(r"~\AppData\Roaming\bakkesmod\bakkesmod\data\acplugin\Decals")
        if not os.path.exists(texture_path):
            messagebox.showerror("Uh oh...", "Please install BakkesMod and AlphaConsole first.")
            return
        if messagebox.askyesno("BakkesMod Textures", "Do you wish to install the V1.0 BakkesMod Textures?"):
            if curStatus == "online":
                if messagebox.askyesno("Hold on", "It seems that an instance of Rocket League or Epic Games is running. Modifying files currently could cause unwanted behaviour. Wish to continue?"):
                    try:
                        shutil.copytree("textures", texture_path, dirs_exist_ok=True)
                        messagebox.showinfo("Horray", "Successfully applied textures")
                    except:
                        messagebox.showerror("Uh oh...", "Unable to apply textures.")
        

    




            
    
    
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
        width=200,
        values=readBackups()
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
    createBackupButton.bind("<Button-1>", lambda e: createBackup())

    createBackupEntry.place(relx=1, rely=0.49, x=-370, y=0, anchor="w")
    createBackupEntry.configure(border_color=borderColor, fg_color= buttonColor)

    applyBackupButton.place(relx=1, rely=0.60, x=-140, y=0, anchor="w")
    applyBackupButton.bind("<Button-1>", lambda e:applyBackup(applyBackupCombobox.get().strip()))

    applyBackupCombobox.place(relx=1, rely=0.60, x=-370, y=0, anchor="w")
    applyBackupCombobox.configure(border_color=borderColor, fg_color= buttonColor, dropdown_fg_color=dropDownColor, button_color=borderColor)
    applyBackupCombobox.set("Select backup...")

    miscFrame.place(relx=0.5, rely=0.67, x=0, y=0, anchor="n")

    miscLabel.place(relx=0.2, rely=0.67, x=0, y=0, anchor="n")

    clearCacheButton.place(relx=0.2, rely= 0.78, x=0, y=0, anchor="n")
    clearCacheButton.bind("<Button-1>", lambda e:clearCache())

    bakkesButton.place(relx=0.5, rely= 0.78, x=0, y=0, anchor="n")
    bakkesButton.bind("<Button-1>", lambda e:installBakkesTextures())

    startupEntry.place(relx=0.38, rely= 0.89, x=0, y=0, anchor="n")
    startupEntry.configure(border_color=borderColor, fg_color= buttonColor)

    launchButton.place(relx=0.8, rely=0.89, x=0, y=0, anchor="n")
    
    return tweaksFrame


def get_custom_maps():  
    folder = "custom_maps"
    maps = []

    if not os.path.exists(folder):
        os.mkdir(folder)
        return maps
    
    for file in os.listdir(folder):
        if file.endswith(".upk"):
            name=file.replace(".upk", "")
            maps.append(name)

    return maps

def get_freeplay_maps(rl_path):
    folder = os.path.join(rl_path, "TAGame", "CookedPCConsole")
    maps = []

    if not os.path.exists(folder):
        return maps

    for file in os.listdir(folder):
        if file.lower().endswith("_p.upk"):
            name=file.replace("_p.upk", "")
            maps.append(name)

    return maps



def showMapChanger(window, rl_path):
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

    maps = get_custom_maps()
    print("Maps found:", maps)

    def open_swap_popup(custom_map_name):
        popup = tk.Toplevel(window)
        popup.title("Swap Map")
        popup.geometry("300x150")
        popup.configure(bg="#0b0f22")
        label = tk.Label(popup, text=f"swapping in {custom_map_name}?", bg="#0b0f22", fg="white")
        label.pack(pady=20)

        freeplayMaps = get_freeplay_maps(rl_path)
        mapDropdown = ctk.CTkComboBox(
            popup,
            values=freeplayMaps,
            width=200,
        )
        mapDropdown.set("Select Freeplay Map...")
        mapDropdown.pack(pady=10)

        confirmButton = ctk.CTkButton(
            popup,
            text = "Confirm Swap",
            command = lambda: swap_maps(custom_map_name, mapDropdown.get(), popup),   #swap_maps muss noch definiert werden um die actual files zu swappen, mach ich demnächst
        )
        confirmButton.pack(pady=10)


    for i, map_name in enumerate(maps):
        row = i //3
        col = i % 3

        mapButton = ctk.CTkButton(
            mapScrollFrame,
            text=map_name,
            width=110, height=150,
            command = lambda m=map_name: open_swap_popup(m)
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

  
   



