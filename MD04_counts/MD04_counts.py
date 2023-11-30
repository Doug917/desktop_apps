import os, sys
'''
Parses through MD04 table for part number and counts
deliveries, deliveries blocked (CusOrd) and planned receipts.
Permits one data file in .txt per run.
Get data file:
-----------------------------------------------------------------
MD04 (enter part number) >> List >> Variable Print >> Unconverted
-----------------------------------------------------------------
Run Code:
-----------------------------------------------------------------
in terminal >> python3 MD04_counts.py
outputs the counts of different MRP elements
from MD04 screen into console.
-----------------------------------------------------------------
'''

CusOrd_counts = 0
Delvry_counts = 0
IndReq_counts = 0
files = os.listdir()
if len(files)==1:
    print("Please download MD04 data.")
    sys.exit()
for file in files:
    if file.split(".")[1] == "txt":
        filename = file
        

with open(filename, "r") as data_file:
    content = data_file.readlines()
    for row in content:
        test = row.find("CusOrd")
        if test != -1:
            #entry found.  now, find quantity in qty column.
            test2 = row.find("-")
            CusOrd_counts += int(row[test2-4:test2])
        test = row.find("Delvry")
        if test != -1:
            #entry found.  now, find quantity in qty column.
            test2 = row.find("-")
            Delvry_counts += int(row[test2-4:test2])
        test = row.find("IndReq")
        if test != -1:
            #entry found.  now, find quantity in qty column.
            test2 = row.find("-")
            IndReq_counts += int(row[test2-4:test2])
  
f = filename.split(".")[0]
print(f"Part Number: {f}")   
print(f"CusOrd: {CusOrd_counts}")
print(f"Delvry: {Delvry_counts}")
print(f"IndReq: {IndReq_counts}")

os.remove(filename)

     