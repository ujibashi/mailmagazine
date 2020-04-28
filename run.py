# coding: UTF-8
import csv
import glob
import sys
import re
from collections import defaultdict

# check arguments
if len(sys.argv) == 1:
    print("Usage: python run.py <dir>")
    sys.exit(1)

# get the file list in the given directory
directory = sys.argv[1]
files = glob.glob(directory + '/*')

# the dictionary of mail magazines, sur name, given name having the mail address as the keys
total_dict = defaultdict(set)
sur_name_dict = defaultdict(str)
given_name_dict = defaultdict(str)

for fn in files:
    # extract the mail magazine name
    split_fn = re.split('/', fn)
    filename = split_fn[-1]
    mailmagazine_name = filename[:-4]

    # read each csv file and store the infos. into the dictionaries
    with open(fn) as fp:
        reader = csv.reader(fp)
        for row in reader:
            sur_name = row[0]
            given_name = row[1]
            address = row[2]

            total_dict[address].add(mailmagazine_name)
            sur_name_dict[address] = sur_name
            given_name_dict[address] = given_name

# output
output_file = directory + '/main.csv'
with open(output_file, 'w') as out:
    for address in total_dict.keys():
        mm_string = ''.join(total_dict[address])
        print(f'{sur_name_dict[address]},{given_name_dict[address]},{address},{mm_string}', file=out)
