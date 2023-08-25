#!/usr/bin/env python3
# Entity Tracker
# By MrBeam89_
from mcpi.minecraft import Minecraft
from time import sleep
import os
from sys import exit
os.system("clear")
try:
    mc = Minecraft.create()
except ConnectionRefusedError:
    print("[ERROR] Minecraft client isn't connected")
while True:
    entityIds = mc.getPlayerEntityIds()
    print("Entity tracker")
    print("-" * 14)
    for x in entityIds:
        try:
            print("ID :",x,"| Pos:",mc.entity.getPos(x))
        except KeyboardInterrupt:
            exit()
        except:
            pass
    sleep(1)
    os.system("clear")
