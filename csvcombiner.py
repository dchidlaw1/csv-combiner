#!/usr/bin/env python3

import csv
from fileinput import filename
import sys
import os
import pandas as pd

def main():
    #writes the name of the columns to standard output
    writer = csv.writer(sys.stdout, delimiter=',', quotechar='"', 
    quoting=csv.QUOTE_ALL)
    try:
        rowNames = writeCols(sys.argv[1], writer)
        #go through each file and add print them to stdout
        for i in range(1, len(sys.argv)):
            readFile(sys.argv[i], rowNames)
    except Exception as e:
        print("File: " + str(e) + " does not exist" )

def writeCols(readFile, writer):
    """
    Writes the first row of the given file to the given writer

    readFile is the file being read from, writer is the file being output
    to
    """
    try:
        #get the first row of the file and output as the header
        with open(readFile, newline='') as file:
            reader = csv.reader(file, delimiter=",")
            row = next(reader)
            row.append("filename")
            rowNames = row
            writer.writerow(row)
            file.close()
            return rowNames
    except OSError as e:
        raise Exception(readFile)


def readFile(read, rowNames):
    """
    Reads the given file and outputs it to stdout with a new column that
    shows the file name

    read is the name of the file being read from, rowNames is the name
    of the rows for the output file
    """
    try:
        printFileName = os.path.basename(read)
        #get data in chunks to improve performance
        reader = pd.read_csv(read, escapechar="\\", chunksize=1000)
        for rd in reader:
            rd["filename"] = printFileName
            data = pd.DataFrame(rd, columns=rowNames)
            data.to_csv(sys.stdout, header=False, index=False, sep=",", mode="w", quoting=csv.QUOTE_ALL, escapechar="\\")
    except OSError as e:
        raise Exception(read)

            
if __name__ == '__main__':
    main()

