import re
import sys

#Handle user input.

limit = int(input("Limit number of search results to: "))
count = 0
query = input("Enter phrase: ")
#load in ASV txt.
file = open("asv.txt", "r")
for line in file.readlines():
    if re.search(query, line.lower()):
        #print line containing query.
        print(line)
        count += 1
        if (count > limit - 1):
            file.close()
            break
if count < limit:
    print(f"Total # of results: {count}")
file.close()