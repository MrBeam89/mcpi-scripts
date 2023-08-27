#!/usr/bin/env python3
# MCPI Spy+
# By MrBeam89_
# Enhanced version of the original MCPI Spy
# Requires Minecraft Pi Addons by Bigjango13 : https://github.com/Bigjango13/MCPI-Addons
# Spy on other players by manipulating the camera
# Can also break/place blocks in Normal mode

from tkinter import *
from sys import exit

# Check if MCPI-Addons is installed
try:
    from mcpi_addons.minecraft import Minecraft
except ModuleNotFoundError:
    print("[FATAL ERROR] MCPI-Addons isn't installed, see https://github.com/Bigjango13/MCPI-Addons to install it")
    exit()

WINDOW_WIDTH = 240
WINDOW_HEIGHT = 400
RESIZABLE_WIDTH = False
RESIZABLE_HEIGHT = False

print("MCPI Spy+ by MrBeam89_")

# Attempts to establish connection with Minecraft, fails and exits if no client is running
try:
    mc = Minecraft.create()
    print("[INFO] Successfully connected")
    usernames = mc.getUsernames()
except ConnectionRefusedError:
    print("[FATAL ERROR] Minecraft client isn't connected")
    exit()

# Updates list of all player usernames
def refresh():
    listbox.delete(0, listbox.size())
    usernames = mc.getUsernames()
    for elementIndex in range(0, len(usernames)):
        listbox.insert(elementIndex, usernames[elementIndex])
    print("[INFO] Refreshed usernames list")

# The core program
def spy():
    selected = listbox.curselection()
    try:
        if selected_camera_mode.get() == "Normal":
            mc.camera.setNormal(mc.getPlayerEntityId(usernames[selected[0]]))
        if selected_camera_mode.get() == "Fixed":
            # Get coordinates
            x = x_textbox.get()
            y = y_textbox.get()
            z = z_textbox.get()
            # Check if coordinates are valid
            try:
                x = float(x)
                y = float(y)
                z = float(z)
                mc.camera.setNormal(mc.getPlayerEntityId(usernames[0])) # Fix for Fixed mode not working after selecting Follow mode
                mc.camera.setPos(x,y,z)
                print(f"[INFO] Spying coordinates X: {x} Y: {y} Z: {z}")
                
            except ValueError:
                print("[ERROR] Invalid coordinates")
        if selected_camera_mode.get() == "Follow":
            mc.camera.setFollow(mc.getPlayerEntityId(usernames[selected[0]]))
            
        if selected_camera_mode.get() in ["Normal", "Follow"]:
            print(f'[INFO] Spying {usernames[selected[0]]} in {selected_camera_mode.get()} mode')
        if selected_camera_mode.get() == "Follow":
            print("[INFO] Unable to place/break blocks in Follow mode")
        if not selected_camera_mode.get():
            print("[INFO] No camera mode selected")

    except:
        print(f'[ERROR] No name selected / No player found with chosen name')
        

# Main window, text and list of all player usernames
root = Tk()
root.title("MCPi Spy+")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(width=RESIZABLE_WIDTH, height=RESIZABLE_HEIGHT)
frame = Frame(root)
title = Label(root, text="MCPi Spy+", font=("Arial", 15))
subtitle = Label(root, text="By MrBeam89_", font=("Arial", 10))
listbox = Listbox(root)

frame.pack()
title.pack()
subtitle.pack()
listbox.pack(pady=5)

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

# Regular buttons to refresh and spy
button_frame = Frame(root)
update_btn = Button(button_frame, text="Refresh", command=refresh)
spy_btn = Button(button_frame, text="Spy", command=spy)

button_frame.pack(side="right", padx=10)
update_btn.pack()
spy_btn.pack()

# Textboxes for specific X, Y and Z coords
textbox_frame = Frame(root)
x_label = Label(textbox_frame, text="X:")
x_textbox = Entry(textbox_frame, width=4)
y_label = Label(textbox_frame, text="Y:")
y_textbox = Entry(textbox_frame, width=4)
z_label = Label(textbox_frame, text="Z:")
z_textbox = Entry(textbox_frame, width=4)

textbox_frame.pack(pady=5)
x_label.pack()
x_textbox.pack()
y_label.pack()
y_textbox.pack()
z_label.pack()
z_textbox.pack()

# Start the program
refresh()
root.mainloop()
