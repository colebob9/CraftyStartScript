"""
CraftyStartScript
v0.1.1
Written by colebob9
Python 3 Code - Released under MIT License

Psuedocode:
Start server
Keep in restart loop until recieving signal to stop the server.

Maybe put in separate standalone script
On timer, start backup process
    `save-off`
    `save-all`
    Put all world and plugin data and put both in their respective .ZIP archives.
    `save-on`


To-Do:
* Backups
* Add Spigot command

"""
print("CraftyStartScript v0.1.1")

# Configure this before using script.

# Java Launch Options
minMem = "512M"
maxMem = "512M"
jarName = "minecraft_server.1.11.2.jar"
extraOptions = " -XX:+UseConcMarkSweepGC" # add space before if adding anything

# Script Options
exitTimer = 15      # in seconds

# Config End.

import shlex
import subprocess
import time
import sys

while True:
    # Launch
    print("\nLaunching server using command:\njava -Xms%s -Xmx%s%s -jar %s" % (minMem, maxMem, extraOptions, jarName))
    subprocess.call(shlex.split("java -Xms%s -Xmx%s%s -jar %s" % (minMem, maxMem, extraOptions, jarName)))
    
    # Timer with countdown to ask for exit.
    print("\nTo exit the script, use CTRL-C in the next %d seconds..." % (exitTimer))
    for i in range(exitTimer):
        time.sleep(1)
        sys.stdout.write(str(i)+' ')
        sys.stdout.flush()

    
