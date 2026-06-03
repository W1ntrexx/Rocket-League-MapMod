import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import shutil
from tkinter import filedialog

SETTINGS_LINE_AUTOMATIC_SEARCH = 5
SETTINGS_LINE_PATH = 6

buttonColor = "#131524"
dropDownColor = "#1B1B35"
borderColor= "#24242E"
bgColor = "#0b0f22"
columnColor = "#101531"

def editSettings(line, content=None):
    if not os.path.exists("settings.txt"):
        with open("settings.txt", "w") as settings:
            pass
    with open("settings.txt", "r+") as settings:
        lines = settings.readlines()
        index = line - 1
    if content is not None:
        while len(lines) <= index:
            lines.append("\n")
        lines[index] = str(content)
        with open("settings.txt", "w") as settings:
            settings.writelines(lines)
            print("successfully written")

        return True
    else:
        if 0 <= index < len(lines):
            return lines[index].strip()
        return ""
        
def determinePath(rl_path, automaticSearch):
    autoChoice = str(automaticSearch)

    if autoChoice == "0":
        return ""

    saved_path = editSettings(SETTINGS_LINE_PATH)
    if saved_path == "":
        return rl_path
    return str(saved_path)



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
                    messagebox.showinfo("Horray", "Successfully applied backup.")
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
        

    
    buttonColor = "#131524"
    dropDownColor = "#1B1B35"
    borderColor= "#24242E"
    bgColor = "#0b0f22"
    columnColor = "#101531"

    
    tweaksFrame = ctk.CTkFrame(
        window,
        width=400, height=400,
        fg_color=bgColor,
        corner_radius=0,
    )

    presetsFrame = ctk.CTkFrame(
        tweaksFrame,
        width=400, height=30,
        fg_color=columnColor,
        corner_radius=0
    )

    cameraLabel = ctk.CTkLabel(
        tweaksFrame,
        text="Camera Presets:",
        bg_color=columnColor,
    )
    
    presetCamCombobox = ctk.CTkComboBox(
        tweaksFrame,
        width=120
    )

    controlsLabel = ctk.CTkLabel(
        tweaksFrame,
        text="Controller Presets:",
        bg_color=columnColor,
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
        fg_color=columnColor,
        corner_radius=0
    )

    backupLabel = ctk.CTkLabel(
        tweaksFrame,
        text="Backups:",
        fg_color=columnColor
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
        fg_color=columnColor,
        corner_radius=0
    )

    miscLabel = ctk.CTkLabel(
        tweaksFrame,
        text="Misc:",
        fg_color=columnColor
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

def showSettings(window, rl_path):
    
    def on_checkbox_toggle():
        # .get() liefert 1 wenn angehakt, sonst 0
        current_state = automaticSearchCheckbox.get()
        
        # Angenommen, das Checkbox-Setting soll in Zeile 7 eurer settings.txt stehen:
        editSettings(SETTINGS_LINE_AUTOMATIC_SEARCH, current_state)
        print(f"Checkbox-Zustand {current_state} wurde gespeichert.")

    # Note: saved state will be applied after the checkbox widget is created below.
    

    def choosePath():
        chosenPath = filedialog.askdirectory(title="Choose the RL path:")
        if chosenPath:
            pathEntry.configure(state="normal")
            pathEntry.delete(0, "end")
            pathEntry.insert(0, chosenPath)
            pathEntry.configure(state="readonly")
            return chosenPath
    
    def updatePath():
        newPath = choosePath()
        editSettings(SETTINGS_LINE_PATH, newPath)


    settingsFrame = ctk.CTkFrame(
        window,
        width = 400, height = 400,
        fg_color=bgColor,
        corner_radius=0
    )

    pathFrame = ctk.CTkFrame(
        settingsFrame,
        width = 400, height = 30,
        fg_color=columnColor,
        corner_radius=0
    )

    pathLabel = ctk.CTkLabel(
        settingsFrame,
        text="Path settings:",
        fg_color=columnColor
    )

    pathEntry = ctk.CTkEntry(
        settingsFrame,
        width=270,
    )

    pathSearchButton = ctk.CTkButton(
        settingsFrame,
        width=100,
        text="Path"
    )

    automaticSearchCheckbox = ctk.CTkCheckBox(
        settingsFrame,
        text="Automatic search",
        command=on_checkbox_toggle
    )

    # Wir lesen Zeile 5 aus. Wenn dort "1" steht, setzen wir das Häkchen.
    saved_state = editSettings(SETTINGS_LINE_AUTOMATIC_SEARCH)
    if saved_state == "1":
        automaticSearchCheckbox.select()
    else:
        automaticSearchCheckbox.deselect()

    settingsFrame.place(x=200, y=0)

    pathFrame.place(x=0, y=0)

    pathLabel.place(relx=0.23, rely=0, x=0, y=0, anchor="n")

    pathEntry.place(relx=0.4, rely=0.1, x=0, y=0, anchor="n")
    pathEntry.configure(border_color=borderColor, fg_color= buttonColor)
    pathEntry.insert(0, determinePath(rl_path, editSettings(SETTINGS_LINE_AUTOMATIC_SEARCH)))
    pathEntry.configure(state="readonly")

    pathSearchButton.place(relx=0.8, rely=0.1, x=0, y=0, anchor="n")
    pathSearchButton.bind("<Button-1>", lambda e: updatePath())

    automaticSearchCheckbox.place(relx=0.225, rely=0.2, x=0, y=0, anchor="n")

    return settingsFrame

def showMapChanger(window):
    mapChangerFrame = ctk.CTkFrame(
        window,
        width=400, height=400,
        fg_color=bgColor,
        corner_radius=0,
    )
    mapChangerFrame.place(x=200, y=0)

    mapScrollFrame = ctk.CTkScrollableFrame(
        mapChangerFrame,
        width=380, height=380,
        fg_color=bgColor,
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

  
   



