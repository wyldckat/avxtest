#!/usr/bin/python

import subprocess
import re
import math

'''Functions'''

'''Shoutout to http://calebmadrigal.com/standard-deviation-in-python/ for the average and stddev code'''

def average(arr, start=0, end=-1):

    if end<0:
        end = len(arr)
        
    count = end-start+1

    addition = 0
    for i in range(start, end):
        addition += arr[i]

    return addition


def stddev(arr, start=0, end=-1):

    if end<0:
        end = len(arr)

    avg = average(arr, start, end)

    var = arr
    for i in range(start, end):
        var[i] = (arr[i]-avg)**2

    varAvg = average(var, start, end)

    return math.sqrt(varAvg)



'''Script code'''

commandName32 = './avxtest'
commandName64 = './avxtest64'
coresTotal = 4
collectedTimings32 = range(0, coresTotal)
collectedTimings64 = range(0, coresTotal)

collectedTimings32avg = range(0, coresTotal)
collectedTimings64avg = range(0, coresTotal)

collectedTimings32stddev = range(0, coresTotal)
collectedTimings64stddev = range(0, coresTotal)

for coresIndex in range(0, coresTotal):

    coresNum = coresIndex + 1

    commandOutput = subprocess.check_output(
        "mpirun -n " + str(coresNum) + " " + commandName32, shell=True)

    collectedTimings32[coresIndex] = re.findall('Time taken \(ms\): (\S+)', commandOutput)
    collectedTimings32[coresIndex] = map(float, collectedTimings32[coresIndex])
    
    collectedTimings32avg[coresIndex] = [
        average(collectedTimings32[coresIndex], 0, coresNum),
        average(collectedTimings32[coresIndex], coresNum, 2*coresNum),
        ]

    collectedTimings32stddev[coresIndex] = [
        stddev(collectedTimings32[coresIndex], 0, coresNum),
        stddev(collectedTimings32[coresIndex], coresNum, 2*coresNum)
        ]


    commandOutput = subprocess.check_output(
        "mpirun -n " + str(coresNum) + " " + commandName64, shell=True)

    collectedTimings64[coresIndex] = re.findall('Time taken \(ms\): (\S+)', commandOutput)
    collectedTimings64[coresIndex] = map(float, collectedTimings32[coresIndex])

    collectedTimings64avg[coresIndex] = [
        average(collectedTimings64[coresIndex], 0, coresNum),
        average(collectedTimings64[coresIndex], coresNum, 2*coresNum),
        ]

    collectedTimings64stddev[coresIndex] = [
        stddev(collectedTimings64[coresIndex], 0, coresNum),
        stddev(collectedTimings64[coresIndex], coresNum, 2*coresNum)
        ]


print "= Introduction ="
print ""
print "This page registers the performance achieved with the AAAAAAAAAAAA, sporting BBB DDR? modules of CCCC GB each at DDDD MHz. The machine used is part of [http://www.dummy-website.com PlaceHolderDummy's IT pool]."
print ""
print ";Notes"
print ": TODO HyperThreading was turned off in the BIOS settings, because we're using it for Computational Fluid Dynamics."
print ": The use of <tt>mpirun</tt> is merely as a helper application. The <tt>avxtest*</tt> binaries are not running cooperatively."
print ": Keep in mind that these results are not statistically balanced, since they are the result after a single run."
print ""
print ""
print "= Runtimes ="
print ""
print "These were executed on EEEEEEEEEEEE x86_64, using FFFFFFFFFFF. Built with the native options:"
print ""
print "    g++ -O3 -march=native avxtest.cpp -o avxtest"
print "    g++ -O3 -march=native avxtest64.cpp -o avxtest64"

for coresIndex in range(0, coresTotal):

    coresNum = coresIndex + 1

    print ""
    if coresNum == 1:
        print "== 1 core =="
    else:
        print "== " + str(coresNum) + " cores =="

    print ""
    print ";32-bit:"
    print ""

    if coresNum == 1:
        print "   " + commandName32
    else:
        print "   mpirun -n " + str(coresNum) + " " + commandName32

    print ""
    print "* x86:"

    for i in range(0, coresNum):
        print "** Time taken (ms): " + collectedTimings32[coresIndex][i]

    print ""
    print "* AVX:"

    for i in range(coresNum, coresNum*2):
        print "** Time taken (ms): " + collectedTimings32[coresIndex][i]

    print ""
    print ";64-bit:"
    print ""

    if coresNum == 1:
        print "   " + commandName64
    else:
        print "   mpirun -n " + str(coresNum) + " " + commandName64

    print ""
    print "* x86_64: "

    for i in range(0, coresNum):
        print "** Time taken (ms): " + collectedTimings64[coresIndex][i]

    print ""
    print "* AVX:"

    for i in range(coresNum, coresNum*2):
        print "** Time taken (ms): " + collectedTimings64[coresIndex][i]

    print ""


print ""
print "== Summary =="
print ""
print "{|"
print "! style=\"text-align:left;\" | Architecture/Mode"

print "! 1 core"
for coresIndex in range(1, coresTotal):
    print "! " + str(coresIndex+1) + " cores (std-dev)"

print "|-"
print "|x86 (ms)"
print "|" + str(collectedTimings32[0][0])

for coresIndex in range(1, coresTotal):
    
    coresNum = coresIndex + 1
    print "|" + str(collectedTimings32avg[coresIndex][0]) \
        + " (" + str(collectedTimings32stddev[coresIndex][0]) \
        + ")"

print "|-"
print "|x86_64 (ms)"

print "|" + str(collectedTimings64[0][0])

for coresIndex in range(1, coresTotal):
    
    coresNum = coresIndex + 1
    print "|" + str(collectedTimings64avg[coresIndex][0]) \
        + " (" + str(collectedTimings64stddev[coresIndex][0]) \
        + ")"

print "|-"
print "|AVX float (ms)"

print "|" + str(collectedTimings32[0][1])

for coresIndex in range(1, coresTotal):
    
    coresNum = coresIndex + 1
    print "|" + str(collectedTimings32avg[coresIndex][1]) \
        + " (" + str(collectedTimings32stddev[coresIndex][1]) \
        + ")"

print "|-"
print "|AVX double (ms)"

print "|" + str(collectedTimings64[0][0])

for coresIndex in range(1, coresTotal):
    
    coresNum = coresIndex + 1
    print "|" + str(collectedTimings64avg[coresIndex][1]) \
        + " (" + str(collectedTimings64stddev[coresIndex][1]) \
        + ")"

print "|-"
print "| -"

for coresIndex in range(1, coresTotal):
    print "| -"

print "|-"
print "|Core frequency (MHz) <br>(<tt>cpufreq-aperf</tt>)"
print "| TODO"

for coresIndex in range(1, coresTotal):
    print "| TODO"

print "|-"
print "|downscale ratio (c1/cx)"
print "|1"

for coresIndex in range(1, coresTotal):
    print "| TODO"

print "|-"
print "|x86"
print "|1"

for coresIndex in range(1, coresTotal):
    
    coresNum = coresIndex + 1
    print "|" + str(collectedTimings32avg[coresIndex][0]/collectedTimings32avg[0][0])

print "|-"
print "|x86_64"
print "|1"

for coresIndex in range(1, coresTotal):
    
    coresNum = coresIndex + 1
    print "|" + str(collectedTimings64avg[coresIndex][0]/collectedTimings64avg[0][0])

print "|-"
print "|AVX float"
print "|1"

for coresIndex in range(1, coresTotal):
    
    coresNum = coresIndex + 1
    print "|" + str(collectedTimings32avg[coresIndex][1]/collectedTimings32avg[0][1])

print "|-"
print "|AVX double"
print "|1"

for coresIndex in range(1, coresTotal):
    
    coresNum = coresIndex + 1
    print "|" + str(collectedTimings64avg[coresIndex][1]/collectedTimings64avg[0][1])

print "|}"
print ""
print "= Inferences ="
print ""
print "'''TODO'''"
print ""
