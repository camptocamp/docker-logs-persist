#!/usr/bin/python3

from datetime import date
from os import listdir, environ
from os.path import isfile, join
import re

yesterday = date.fromordinal(date.today().toordinal() - 1)

inputLogPath=environ.get("INPUT_LOG_PATH")
outputLogPath=environ.get("OUTPUT_LOG_PATH")
outputLogFile=join(outputLogPath, "%s.log" % yesterday)
label="filter-log"
labelValue="yes"

def processFile(infile, outfile):
    input = open(infile)
    output = open(outfile, "a")
    i = 0
    line = input.readline()
    while len(line) > 0:
        match = re.search(r"(.*)\s+###IMAGE(.*)###LABELS:map\[[^\]]*%s:%s[^\]]*\]" % (label, labelValue), line)
        if match is None:
            return 0
        output.write("%s\n" % match.group(1))
        i = i+1
        line = input.readline()
    input.close()
    output.close()
    return i

yesterdayLogsDir = join(inputLogPath, str(yesterday))
print("Input log dir : %s" % yesterdayLogsDir)
print("Output log file : %s" % outputLogFile)

logfiles = [f for f in listdir(yesterdayLogsDir) if isfile(join(yesterdayLogsDir, f))]

for file in logfiles:
    if not re.search(".*\.gz", file):
        nbLine = processFile(join(yesterdayLogsDir, file), outputLogFile)
        print("Write %s from %s " % (nbLine, file))

# sed -r 's/io\.rancher\.service\.hash/filter-log:yes io.rancher.service.hash/g'
