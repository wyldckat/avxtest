#!/bin/sh

#this is just and example of sourcing the correct shell environment to be used
#for the custom GCC that was used
source /opt/OpenFOAM/OpenFOAM-2.4.x/etc/bashrc

#Run the testing utility
./noavxtest64
