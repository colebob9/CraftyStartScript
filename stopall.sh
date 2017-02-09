#!/bin/bash

# Sends command to stop all Minecraft servers at once.

# Example
echo Stopping Server1!
screen -S test1 -p 0 -X stuff "stop\n"
sleep 8s
# Sends keyboardinterupt to script
screen -S test1 -p 0 -X stuff "^C" 
sleep 1s
screen -X -S test1 quit
