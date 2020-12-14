# ----------------------------------------------------------------
# Clean SOCC files.
#
# (C) 2020 Laurens Bosman, Discourse Processing Lab, SFU
# Released under GNU General Public License (GPL)
# email lbosman@sfu.ca
# ----------------------------------------------------------------

import os
import re

def main(corpusFolder):
    os.mkdir('./SOCC_clean/')
    for file in os.listdir(corpusFolder):
        with open('./SOCC_clean/' + file, 'w') as output:
            with open(corpusFolder + file, 'r') as inputFile:
                for line in inputFile:
                    first = re.sub(r'<.{1,3}>', '', line)
                    second = re.sub(r'_{4,100}', '', first)
                    third = re.sub(r'-{4,100}', '', second)
                    fourth = re.sub(r'~{4,100}', '', third)
                    output.write(fourth)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description='remove artifacts from data collection process')
	parser.add_argument('corpusPath', type=str, help='the path to the corpus folder')
	args = parser.parse_args()
	main(args.corpusPath) 
