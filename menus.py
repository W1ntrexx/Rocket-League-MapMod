import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import shutil
from tkinter import filedialog
import sys
import psutil

SETTINGS_LINE_AUTOMATIC_SEARCH = 5
SETTINGS_LINE_PATH = 6
SETTINGS_LINE_INTERVAL = 7

buttonColor = "#131524"
dropDownColor = "#1B1B35"
borderColor= "#24242E"
bgColor = "#0b0f22"
columnColor = "#101531"

COMBOBOX_SETTINGS = {       #verwende mit .configure(**COMBOBOX_SETTINGS) / wichtig sind die Sterne!
    "border_color": borderColor,
    "fg_color": buttonColor,
    "dropdown_fg_color": dropDownColor,
    "button_color": borderColor
}



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
        # Ensure each written setting ends with a newline to avoid concatenation
        lines[index] = str(content) + "\n"
        with open("settings.txt", "w") as settings:
            settings.writelines(lines)

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
        if os.path.exists(cache_path) and curStatus == "offline":
            shutil.rmtree(cache_path)
            messagebox.showinfo("Success", "Cache has been deleted.")
        elif curStatus() == "online":
            messagebox.showwarning("Warning", "Please close Rocket League before clearing the cache.")
            pass
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
        if curStatus() == "online":
            if not messagebox.askyesno("Hold on", "It seems that an instance of Rocket League or Epic Games is running. Modifying files currently could cause unwanted behaviour. Wish to continue?"):
                return 
        else:
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
        text_color="white"
    )
    
    presetCamCombobox = ctk.CTkComboBox(
        tweaksFrame,
        width=120,
        text_color="white"
    )

    controlsLabel = ctk.CTkLabel(
        tweaksFrame,
        text="Controller Presets:",
        bg_color=columnColor,
        text_color="white"
    )

    presetConCombox = ctk.CTkComboBox(
        tweaksFrame,
        width=120,
        text_color="white"
    )

    IncludeBindsCheckbox = ctk.CTkCheckBox(
        tweaksFrame,
        text="Include binds",
        text_color="white"
    )

    confirmPresetsButton = ctk.CTkButton(
        tweaksFrame,
        text="Confirm choices",
        width=120,
        text_color="white"
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
        fg_color=columnColor,
        text_color="white"
    )

    createBackupButton = ctk.CTkButton(
        tweaksFrame,
        text="Create Backup",
        width=120,
        text_color="white"
    )

    createBackupEntry = ctk.CTkEntry(
        tweaksFrame,
        placeholder_text="Backup Name",
        width=200,
        text_color="white"
    )

    applyBackupButton = ctk.CTkButton(
        tweaksFrame,
        text="Apply Backup",
        width=120,
        text_color="white"
    )

    applyBackupCombobox = ctk.CTkComboBox(
        tweaksFrame,
        width=200,
        values=readBackups(),
        text_color="white"
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
        fg_color=columnColor,
        text_color="white"
    )

    clearCacheButton = ctk.CTkButton(
        tweaksFrame,
        text="Clear Cache",
        width=100,
        text_color="white"
    )

    bakkesButton = ctk.CTkButton(
        tweaksFrame,
        text="BM Textures",
        width=100,
        text_color="white"
    )

    startupEntry = ctk.CTkEntry(
        tweaksFrame,
        placeholder_text="Startup Options",
        width=245,
        text_color="white"
    )

    launchButton = ctk.CTkButton(
        tweaksFrame,
        text="Launch",
        width=100,
        text_color="white"
    )
    
    tweaksFrame.place(x=200, y=0)

    presetsFrame.place(relx=0.5, rely=0, x=0, y=0, anchor="n")

    cameraLabel.place(relx=0.7, rely=0, x=0, y=0, anchor="n")

    presetCamCombobox.place(relx=0.74, rely=0, x=0, y=35, anchor="n")
    presetCamCombobox.configure(**COMBOBOX_SETTINGS)

    controlsLabel.place(relx=0.20, rely=0, x=0, y=0, anchor="n")

    presetConCombox.place(relx=0.23, rely=0, x=0, y=35, anchor="n")
    presetConCombox.configure(**COMBOBOX_SETTINGS)

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
    applyBackupCombobox.configure(**COMBOBOX_SETTINGS)
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
        print(f"Checkbox-state {current_state} has been saved.")
    

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
        if os.path.exists(os.path.join(newPath, "TAGame", "CookedPCConsole")):
            editSettings(SETTINGS_LINE_PATH, newPath)
            pass
        else:  
            pathEntry.configure(state="normal")
            pathEntry.delete(0, "end")      
            pathEntry.configure(state="readonly")    
            messagebox.showerror("Uh oh...", "The chosen path does not seem to be correct. Please choose the folder that contains the TAGame folder.")
    
    def resetApp():
        if messagebox.askyesno("You fr?", "Are you sure you want to reset the app?"):
            if os.path.exists("settings.txt"):
                os.remove("settings.txt")
            if os.path.exists("firstTimeRun.txt"):
                os.remove("firstTimeRun.txt")
            if os.path.exists("backups"):
                shutil.rmtree("backups")
            os.execl(sys.executable, sys.executable, *sys.argv)
        
    def programmPath():
        
        if getattr(sys, 'frozen', False):
            app_path = os.path.dirname(sys.executable)
        else:
            app_path = os.path.dirname(os.path.abspath(__file__))
        
        try:
            os.startfile(app_path)
        except Exception as e:
            print(f"Konnte den Ordner nicht öffnen: {e}")

    def RLPath():
        if determinePath(rl_path, editSettings(SETTINGS_LINE_AUTOMATIC_SEARCH)) == "":
            messagebox.showwarning("Uh oh...", "There is no path...")
            pass
        else:
            os.startfile(determinePath(rl_path, editSettings(SETTINGS_LINE_AUTOMATIC_SEARCH)))


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
        fg_color=columnColor,
        text_color="white"
    )

    pathEntry = ctk.CTkEntry(
        settingsFrame,
        width=270,
        text_color="white"
    )

    pathSearchButton = ctk.CTkButton(
        settingsFrame,
        width=100,
        text="Path",
        text_color="white"
    )

    automaticSearchCheckbox = ctk.CTkCheckBox(
        settingsFrame,
        text="Automatic search",
        command=on_checkbox_toggle,
        text_color="white"
    )

    QoLFrame = ctk.CTkFrame(
        settingsFrame,
        width = 400, height = 30,
        fg_color=columnColor,
        corner_radius=0
    )

    QoLLabel = ctk.CTkLabel(
        settingsFrame,
        text="Quality of Life settings:",
        fg_color=columnColor,
        text_color="white"
    )

    intervalSlider = ctk.CTkSlider(
        settingsFrame,
        width=200,
        from_=1, to=10,
        number_of_steps=9,
        command=lambda value: editSettings(SETTINGS_LINE_INTERVAL, str(value)) #speichert den Wert des Sliders in Zeile 8 der settings.txt
    )

    intervalLabel = ctk.CTkLabel(
        settingsFrame,
        text="Status refreshing Interval: ",
        fg_color=bgColor,
        text_color="white"
    )

    aSecondLabel = ctk.CTkLabel(
        settingsFrame,
        text="1",
        fg_color=bgColor,
        text_color="white"
    )

    tenSecondLabel = ctk.CTkLabel(
        settingsFrame,
        text="10 Seconds",
        fg_color=bgColor,
        text_color="white"
    )

    resetButton = ctk.CTkButton(
        settingsFrame,
        text="Reset App",  
        text_color="White",
        fg_color="#991414",
        hover_color="#630C0C",
        width=100,
        command=resetApp
    )

    goPathButton = ctk.CTkButton(
        settingsFrame,
        text="App Path",
        width = 100,
        command=programmPath
    )

    goRLButton = ctk.CTkButton(
        settingsFrame,
        text="RL Path",
        width=100,
        command=RLPath
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

    QoLFrame.place(relx=0.5, rely=0.32, x=0, y=0, anchor="n")

    QoLLabel.place(relx=0.23, rely=0.32, x=0, y=0, anchor="n")

    intervalSlider.place(relx=0.5, rely=0.48, x=0, y=0, anchor="n")
    intervalSlider.set(5)

    intervalLabel.place(relx=0.5, rely=0.41, x=0, y=0, anchor="n")

    aSecondLabel.place(relx=0.24, rely=0.468, x=0, y=0, anchor="n")

    tenSecondLabel.place(relx=0.83, rely=0.466, x=0, y=0, anchor="n")

    resetButton.place(relx=0.2, rely=0.87, x=0, y=0, anchor="n")

    goPathButton.place(relx=0.5, rely=0.87, x=0, y=0, anchor="n")

    goRLButton.place(relx=0.8, rely=0.87, x=0, y=0, anchor="n")

    return settingsFrame


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

    maps = get_custom_maps()
    print("Maps found:", maps)

    def open_swap_popup(custom_map_name):
        popup = tk.Toplevel(window)
        popup.title("Swap Map")
        popup.geometry("300x150")
        popup.configure(bg="#0b0f22")
        label = tk.Label(popup, text=f"swapping in {custom_map_name}?", bg="#0b0f22", fg="white", font=("Arial", 10))
        label.pack(pady=20)

        freeplayMaps = get_freeplay_maps(rl_path)
        mapDropdown = ctk.CTkComboBox(
            popup,
            values=freeplayMaps,
            width=200,
            text_color="white"
        )
        mapDropdown.configure(**COMBOBOX_SETTINGS)
        mapDropdown.set("Select Freeplay Map...")
        mapDropdown.pack(pady=10)

        confirmButton = ctk.CTkButton(
            popup,
            text = "Confirm Swap",
            command = lambda: swap_maps(custom_map_name, mapDropdown.get(), popup),
            text_color="white"
        )
        confirmButton.pack(pady=10)


    for i, map_name in enumerate(maps):
        row = i //3
        col = i % 3

        mapButton = ctk.CTkButton(
            mapScrollFrame,
            text=map_name,
            width=110, height=150,
            command = lambda m=map_name: open_swap_popup(m),
            text_color="white"
        )
        mapButton.grid(row=row, column=col, padx=5, pady=5)


    return mapChangerFrame

def get_boosts(rl_path):
    folder = os.path.join(rl_path, "TAGame", "CookedPCConsole")
    boosts = []
    
    if not os.path.exists(folder):
        return boosts
    
    for file in os.listdir(folder):
        lower = file.lower()
        if lower.startswith("boost_") and lower.endswith("_sf.upk") and not lower.endswith("_t_sf.upk"):
            name = file[len("boost_"):-len("_SF.upk")]
            if name not in boosts:
                boosts.append(name)
    
    return boosts

def showSkinsChanger(window, rl_path):
    skinsChangerFrame = ctk.CTkFrame(
        window,
        width=400, height=400,
        fg_color="#0b0f22", 
        corner_radius=0,
    )
    skinsChangerFrame.place(x=200, y=0)

    boosts = get_boosts(rl_path)

    boostLabel = ctk.CTkLabel(
        skinsChangerFrame,
        text="Boosts:",
    )
    boostLabel.place(relx=0.5, rely=0.02, anchor="n")

    swapToBoost = ctk.CTkComboBox(
        skinsChangerFrame,
        values=boosts,
        width=150,
    )
    swapToBoost.set("Swap to...")
    swapToBoost.place(relx=0.05, rely=0.08, anchor="nw")

    swapFromBoost = ctk.CTkComboBox(
        skinsChangerFrame,
        values=boosts,
        width=150,
    )
    swapFromBoost.set("Swap from...")
    swapFromBoost.place(relx=0.95, rely=0.08, anchor="ne")

    confirmBoostButton = ctk.CTkButton(
        skinsChangerFrame,
        text="Confirm",
        width=120,
    )
    confirmBoostButton.place(relx=0.5, rely=0.16, anchor="n")

    return skinsChangerFrame

  
   



