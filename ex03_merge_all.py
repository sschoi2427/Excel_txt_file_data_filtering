  # -*- coding: utf-8 -*-

"""
ex03_merge_all.py

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
"""
WORK_PATH = "D:/파이썬"
DATA_PATH = WORK_PATH + "/data"
RESULT_PATH = DATA_PATH + "/result"
RESULT1_PATH = RESULT_PATH + "/2003"
RESULT2_PATH = RESULT_PATH + "/2008"
RESULT3_PATH = RESULT_PATH + "/2013"


def main():
    """
    ************************************************************************
    f파일로 읽아서 g파일(text0)로 쓰는 프로그램
    각 연도파일별 합할 파일 갯수를 차례대로 입력    
    ************************************************************************
    """
    
    #연도별 텍스트 파일 갯수
    amount = [(2003,221), (2008,219), (2013,120)] 
   
    for (year,num) in amount:
        g = open(RESULT_PATH + "/{}/text0.txt".format(year), 'a', encoding = "utf-8")
        
        tot = num + 1
        for i in range(1,tot):
            f = open(RESULT_PATH + "/{0}/text{1}.txt".format(year,i), 'r', encoding = "utf-8")
            line = f.readlines()            
#            for word in line:
#                g.write(word)
            g.writelines(line)    
            g.write("\n")
            f.close()
    
        print(" {0} 처리 파일수는 {1}개,".format(year,i))
        g.close()          
                                                                                     

main()
