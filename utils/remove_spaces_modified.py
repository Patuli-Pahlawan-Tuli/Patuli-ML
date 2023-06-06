import sys
import os
import glob
import argparse

# this script will load class_list.txt and find class names with spaces
# then replace spaces with delimiters inside ground-truth/ and predicted/

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--delimiter', type=str, help="delimiter to replace space (default: '-')", default='-')
parser.add_argument('-y', '--yes', action='store_true', help="force yes confirmation on yes/no query (default: False)", default=False)
args = parser.parse_args()

def rename_class(current_class_name, new_class_name):
  # get list of txt files
  file_list = glob.glob('*.txt')
  file_list.sort()
  # iterate through the txt files
  for txt_file in file_list:
    class_found = False
    # open txt file lines to a list
    with open(txt_file) as f:
      content = f.readlines()
    # remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    new_content = []
    # go through each line of eache file
    for line in content:
      #class_name = line.split()[0]
      if current_class_name in line:
        class_found = True
        line = line.replace(current_class_name, new_class_name)
      new_content.append(line)
    if class_found:
      # rewrite file
      with open(txt_file, 'w') as new_f:
        for line in new_content:
          new_f.write("%s\n" % line)

with open('classes.txt') as f:
    base_dir = os.getcwd()
    for line in f:
        current_class_name = line.rstrip("\n")
        new_class_name = line.replace(' ', args.delimiter).rstrip("\n")
        if current_class_name == new_class_name:
            continue

        os.chdir(base_dir + "/mAP/input/ground-truth")
        rename_class(current_class_name, new_class_name)
        os.chdir(base_dir + "/mAP/input/detection-results")
        rename_class(current_class_name, new_class_name)

print('Done!')