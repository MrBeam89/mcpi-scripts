#!/usr/bin/env python3
# MCPI Spy
# By MrBeam89_
# "Spies" on other players by manipulating the camera
# Can also break/place blocks in Normal mode

from tkinter import *
from mcpi.minecraft import Minecraft
from sys import exit

# Attempts to establish connection with Minecraft, fails and exits if no client is running
try:
    mc = Minecraft.create()
    entityIds = mc.getPlayerEntityIds()
except ConnectionRefusedError:
    print("[ERROR] Minecraft client isn't connected")
    exit()

# Updates list of all player IDs
def update():
    listbox.delete(0, listbox.size())
    entityIds = mc.getPlayerEntityIds()
    for elementIndex in range(0, len(entityIds)):
        listbox.insert(elementIndex, entityIds[elementIndex])
    print("[INFO] Updated player IDs list")

# The core program
def spy():
    selected = listbox.curselection()
    try:
        if selected_camera_mode.get() == "Normal":
            mc.camera.setNormal(entityIds[selected[0]])
        if selected_camera_mode.get() == "Fixed":
            mc.camera.setFixed()
        if selected_camera_mode.get() == "Follow":
            mc.camera.setFollow(entityIds[selected[0]])
            
        if selected_camera_mode.get():
            print(f'[INFO] Spying player with ID {entityIds[selected[0]]} in {selected_camera_mode.get()} mode')
        else:
            print("[INFO] No camera mode selected")
        
        if selected_camera_mode.get() in ["Follow", "Fixed"]:
            print("[INFO] Unable to place/break blocks in Fixed/Follow mode")

    except:
        print(f'[ERROR] No player found with ID {entityIds[selected[0]]}')

# Main window, text and list of all player IDs
root = Tk()
root.title("MCPi Spy")
root.geometry("200x320")
frame = Frame(root)
title = Label(root, text="MCPi Spy", font=("Arial", 15))
subtitle = Label(root, text="By MrBeam89_", font=("Arial", 10))
listbox = Listbox(root)

frame.pack()
title.pack()
subtitle.pack()
listbox.pack()

# Radio buttons for selecting camera mode
radio_frame = Frame(root)
selected_camera_mode = StringVar()
normal_camera_radio = Radiobutton(radio_frame, text="Normal", variable=selected_camera_mode, value="Normal")
fixed_camera_radio = Radiobutton(radio_frame, text="Fixed", variable=selected_camera_mode, value="Fixed")
follow_camera_radio = Radiobutton(radio_frame, text="Follow", variable=selected_camera_mode, value="Follow")

radio_frame.pack(side="left", padx=10)
normal_camera_radio.pack(anchor="w")
fixed_camera_radio.pack(anchor="w")
follow_camera_radio.pack(anchor="w")

# Regular buttons to update and spy
button_frame = Frame(root)
update_btn = Button(button_frame, text="Update", command=update)
spy_btn = Button(button_frame, text="Spy", command=spy)

button_frame.pack(side="right", padx=10)
update_btn.pack()
spy_btn.pack()
selected = None

update()
root.mainloop()
