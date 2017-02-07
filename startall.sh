#!/bin/bash

# Simple script to start every Minecraft server on PC.

# Example
echo Starting Server1!
screen -dm -S test1
screen -S test1 -p 0 -X stuff "cd /home/cabox/workspace/CCNetwork/Server1/\n"
screen -S test1 -p 0 -X stuff "python3 CSS-Start.py\n"
