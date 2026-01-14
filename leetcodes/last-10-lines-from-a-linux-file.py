# ---------------------------------

# File          : last-10-lines-from-a-linux-file.py
# Author        : Anup Jacob
# Version       : v1.0
# Created Date  : 14/01/2026
# Modified Date : 14/01/2026
# Description   :
# Licensing     : Anup Jacob, DevOps
# ----------------------------------

#For small files
def print_last_10_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

#Without slicing
        for i in range(len(lines) - 10, len(lines)):
            print(lines[i], end=" -> ")
'''
#With Slicing
    for line in lines[-10:]:
        print(line, end=" -> ")
'''


if __name__ == '__main__':
    file_path = "D:\GIT Repo\Git Main\Python_Development\leetcodes\Youtubescriptsample.txt"
    print_last_10_lines(file_path)
