import csv
import glob
import sys
import re
from collections import defaultdict



if len(sys.argv) == 1:
    print("Usage: python run.py <dir>")
    sys.exit(1)

directory = sys.argv[1]
files = glob.glob(directory + '/*')

total_dict = defaultdict(set)
name_dict = defaultdict(str)
for fn in files:
    split_fn = re.split('/', fn)
    filename = split_fn[-1]
    mailmagazine_name = filename[:-4]

    address_dict = {}
    with open(fn) as fp:
        reader = csv.reader(fp)
        for row in reader:
            name = row[0]
            address = row[1]

            total_dict[address].add(mailmagazine_name)
            name_dict[address] = name

for address in total_dict.keys():
    mm_string = '・'.join(total_dict[address])
    print(f'{name_dict[address]},{address},{mm_string}')
