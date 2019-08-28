# -*- coding: utf-8 -*-
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
text0의 초록에서 한줄 + 원본excel파일에서 날짜  읽어와서
새로운 excel에 쓰기
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import xlrd
import xlwt

WORK_PATH = "C:/Users/User/Desktop/file"
DATA_PATH = WORK_PATH + "/data"
RESULT_PATH = DATA_PATH + "/result"


def main():
    
    #새롭게 저장할 엑셀 객체 생성
    wb_n = xlwt.Workbook()
    ws_n = wb_n.add_sheet('First Sheet',cell_overwrite_ok=True)  # 시트 이름 정해주기  cell_overwrite_ok=True 필수!
    
    #메모장 불러오기
    f = open(RESULT_PATH+'/new_text0.txt', 'r+', encoding = "utf-8") 
    data = f.readlines() #readlines 리스트로 리턴
    
    #메모장에서 초록 추출해서 쓰기
    for i in range(len(data)):   #리스트 길이만큼 반복문 수행
        row = data[i].split('\n')  #text0의 '\n'를 기준으로 한줄씩 잘라내기
        ws_n.write(i, 1, row)  # .write(행, 열, 값)
    f.close()

    
    #엑셀원본 불러오기
    input_file_name = DATA_PATH + "/data_560.xlsx"
    
    wb = xlrd.open_workbook(input_file_name)
    ws = wb.sheet_by_index(0)
    
    #엑셀원본에서 날짜 추출해서 쓰기 
    nrow = ws.nrows #ws.nrows 행 수
    for i in range(1,nrow):  #2번쨰 행부터 추출하기 위해  (1,nrow)
        ymd=ws.col_values(2)[i]         
        print(ymd)
        ws_n.write(i-1,0,ymd) # .write(행, 열, 값)
            
   
    wb_n.save('new_data.xls')
    
    


main()