#!/usr/bin/python

import sys
import re
from glob import glob

word_list = []
word_dic = {}
def parse_word_from_file(filename):
    f = open(filename, 'r')
    lines = f.readlines() 
    for line in lines:
        #print line
        #words = line.split()
        words = re.split('\W+', line)
        #print words
        for word in words:
            #print word
            if word.lower() not in word_dic:
                #print "not in the dic!"
                word_dic[word.lower()] = 1
            else:
                #print "in the dic!"
                word_dic[word.lower()] += 1
    f.close()
    outfile = filename.split('.')[0] + "_word.txt"
    f = open(outfile, 'w')

    #print sorted(word_dic, key=lambda k : word_dic[k], reverse=True)
    out = sorted(word_dic.items(), key=lambda t: t[1], reverse=True)
    print out
    for o in out:
        outline = o[0] + " : " + str(o[1]) + "\n"
        f.write(outline)
    f.close()
    #print word_dic
    #for word in word_dic:
    #    print word
    #f.write(word_dic)


        


if __name__ == "__main__":
    if sys.argv[1]:
        filenames = glob(sys.argv[1])
        for filename in filenames:
            print filename
            parse_word_from_file(filename)

