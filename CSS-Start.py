"""
CraftyStartScript
v0.2
Written by colebob9
Python 3 Code - Released under MIT License

TODO:
Launch options for Vanilla, Spigot/Bukkit, Forge, etc.
Detect if new file
Download extra scripts (listed below) if needed.
Integration with CraftyPluginOrganizer for predetermined plugin installs.
Integration with AutoBuildTools to build Spigot if needed. 
Custom command


"""
print("CraftyStartScript v0.2")

# Config

# Simple Java Launch Options
useSimpleCommand = True

serverType = "vanilla"  # "vanilla", "spigot"

minMem = "512M" # -Xms
maxMem = "512M" # -Xmx
jarName = "minecraft_server.1.11.2.jar"
#extraOptions = "-XX:+UseConcMarkSweepGC"
extraOptions = ""

# Custom Launch Command
useCustomCommand = False
customCommand = "java -Xmx512M -Xms512M -jar minecraft_server.1.11.2.jar nogui"

# Script Options
exitTimer = 15      # in seconds

# Config End.

import shlex
import subprocess
import time
import sys



while True:
    if useCustomCommand:
        launchCommand = customCommand
    elif useSimpleCommand:
        if serverType == "vanilla":
            simpleCommandEnding = " nogui"
        elif serverType == "spigot":
            simpleCommandEnding = " -o true"
        
        if not extraOptions == "" or None:
            extraOptions = extraOptions + " "
        launchCommand = "java " + "-Xms" + minMem + " -Xmx" + maxMem + " -jar " + extraOptions + jarName + simpleCommandEnding
    
    print("\nLaunching server using command:\n" + launchCommand)
    subprocess.call(shlex.split(launchCommand))
    
    
    # Timer with countdown to ask for exit.
    print("\nTo exit the script, use CTRL-C in the next %d seconds..." % (exitTimer))
    for i in range(exitTimer):
        time.sleep(1)
        sys.stdout.write(str(exitTimer - i)+' ')
        sys.stdout.flush()
