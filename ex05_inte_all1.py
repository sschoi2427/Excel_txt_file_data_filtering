# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 15:29:39 2019

@author: sec

Title :  데이터 통합
"""
WORK_PATH = "D:/파이썬"
DATA_PATH = WORK_PATH + "/data"
RESULT_PATH = WORK_PATH + "/result"

year = [2003, 2008, 2013]
def main():
    for i in year:
        
        f = open(RESULT_PATH + "{}/text0.txt".format(i), 'r', encoding="UTF-8")
        g = open(RESULT_PATH + "new_text0.txt", 'a', encoding="UTF-8")
        
        line = f.readlines()
        g.writelines(line)
        g.write("\n")
        
        f.close()
        g.close()
        
main()