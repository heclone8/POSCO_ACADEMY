#!/usr/bin/env python
# coding: utf-8

# In[91]:


import sys

def show(data):  # 헤더가 있는 출력
    data.sort(reverse=True, key=lambda x: x[4])  # 평균 기준 내림차순 정렬
    
    header = ("Student", "Name", "Midterm", "Final", "Average", "Grade")
    
    # 각 열의 최대 너비 계산 (추가 공간 포함)
    padding = 2
    widths = [max(len(str(item)) for item in col) + padding for col in zip(header, *data)]
    
    # 헤더 출력
    print(" ".join(f"{header[i]:^{widths[i]}}" if i != 1 else f"{header[i]:>{widths[i]}}" for i in range(len(header))))
    print("-" * (sum(widths) + len(widths) - 1))
    
    # 데이터 출력
    for row in data:
        print(" ".join(f"{str(row[i]):^{widths[i]}}" if i != 1 else f"{str(row[i]):>{widths[i]}}" for i in range(len(row))))

def show_no_header(data):  # 헤더가 없는 출력
    data.sort(reverse=True, key=lambda x: x[4])  # 평균 기준 내림차순 정렬

    # 각 열의 최대 너비 계산 (추가 공간 포함)
    padding = 2
    widths = [max(len(str(item)) for item in col) + padding for col in zip(*data)]

    # 데이터 출력
    for row in data:
        print(" ".join(f"{str(row[i]):^{widths[i]}}" if i != 1 else f"{str(row[i]):>{widths[i]}}" for i in range(len(row))))

        
def search(data): #구현 완료
    all_stu_id = [i[0] for i in data]
    stu_id = input("Studeit ID: ")
    if stu_id in all_stu_id:
        attempt = 0
        for i in data:
            if i[0] == stu_id:
                break
            else:
                attempt += 1
        single_data = [i]
        show(single_data)
    else:
        print("NO SUCH PERSON.")
    
def changescore(data): #구현 완료
    all_stu_id = [i[0] for i in data]
    stu_id = input("Studeit ID: ")
    if stu_id not in all_stu_id:
        print("NO SUCH PERSON.")
        return
    attempt = 0
    for i in data:
        if i[0] == stu_id:
            break
        else:
            attempt += 1
    mf = input("Mid/Final? ").upper()
    if mf == 'MID':
        input_score = int(input("Input new score: "))
        if (input_score >= 0) & (input_score <= 100):
            single_data = [data[attempt]]
            show(single_data)
            data[attempt][2] = input_score
            data[attempt][4] = (data[attempt][2] + data[attempt][3]) / 2
            if data[attempt][4] >= 90:
                data[attempt][5] = 'A'
            elif data[attempt][4] >= 80:
                data[attempt][5] = 'B'
            elif data[attempt][4] >= 70:
                data[attempt][5] = 'C'
            elif data[attempt][4] >= 60:
                data[attempt][5] = 'D'
            else:
                data[attempt][5] = 'F'
            print("Score changed.")
            show_no_header(single_data)
        else:
            print("0~100사이 숫자를 넣으십시오")
    elif mf == 'FINAL':
        input_score = int(input("Input new score: "))
        if (input_score >= 0) & (input_score <= 100):
            single_data = [data[attempt]]
            show(single_data)
            data[attempt][3] = input_score
            data[attempt][4] = (data[attempt][2] + data[attempt][3]) / 2
            if data[attempt][4] >= 90:
                data[attempt][5] = 'A'
            elif data[attempt][4] >= 80:
                data[attempt][5] = 'B'
            elif data[attempt][4] >= 70:
                data[attempt][5] = 'C'
            elif data[attempt][4] >= 60:
                data[attempt][5] = 'D'
            else:
                data[attempt][5] = 'F'
            print("Score changed.")
            show_no_header(single_data)
        else:
            print("0~100사이 숫자를 넣으십시오")
    else:
        print("잘못 입력하였습니다.")
        return
    
def add(data): #구현 완료
    all_stu_id = [i[0] for i in data]
    stu_id = input("Student ID: ")
    if stu_id in all_stu_id:
        print("ALREADY EXISTS.")
        return
    name = input("Name :")
    mid_score = int(input("Midterm Score:"))
    if not((mid_score >= 0) & (mid_score <= 100)): #내가 추가한 내용(보고서 작성)
        print("Wrong Value")
        return
    final_score = int(input("Final Score:"))
    if not((final_score >= 0) & (final_score <= 100)): #내가 추가한 내용(보고서 작성)
        print("Wrong Value")
        return
    average = (mid_score + final_score) / 2
    grade = 'F'
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    new_std = [stu_id, name, mid_score, final_score, average, grade]
    data.append(new_std)
    print("Student added.")
            
def searchgrade(data):#구현 완료
    input_grade = input("Grade to search: ").upper()
    all_std_grade = [i[-1] for i in data]
    correct_input = ['A', 'B', 'C', 'D', 'F']
    if input_grade not in correct_input:
        print("Wrong input!") #내가 구현함(보고서 작성)
        return
    if input_grade in all_std_grade:
        result_data = []
        for i in data:
            if i[5] == input_grade:
                result_data.append(i)
        show(result_data)
    else:
        print("NO RESULTS.")


def remove(data): #구현 완료
    if len(data) == 0:
        print("List is empty.")
        return
    
    std_id = input("Student ID: ")
    id_list = []
    for i in data:
        id_list.append(i[0])
    if std_id in id_list:
        data[:] = [i for i in data if i[0] != std_id]
        print("Student removed.")
    else:
        print("NO SUCH PERSON.")
        return
    
    
    
def quit(data, select): # 구현은 완료하였으나 txt파일을 아름답게 정리는 방법은 추후에 구현
    if select == 'YES':
        file_name = input('File name: ')
        data.sort(reverse = True, key = lambda x : x[4])
        columns_to_save = [0, 1, 2, 3]
                        
        with open(file_name, 'w', encoding='utf-8') as f:
            for row in data:
                filtered_row = [row[i] for i in columns_to_save]
                line = '\t'.join(map(str, filtered_row))
                f.write(line + "\n")
    else:
        return
#-----------------------------------------------------------------------------------------------------------------------------------------    
data = [] #모든 학생 데이터는 이 전역변수로 생성된 data에 저장되어 관리된다.
if len(sys.argv) >= 2:
    with open(sys.argv[1], 'r') as f:
        for line in f:
            now = line
            now = now.replace('\t', ' ')
            now = now.replace('\n', ' ')
            now = now.split(' ')
            now.pop()

            now[1] = now[1] + " " + now[2] # Student Name
            del now[2]

            now[2] = int(now[2]) #Midterm Score
            now[3] = int(now[3]) #Final Score
            now.append((now[2] + now[3]) / 2) # Average

            if now[4] >= 90: # Grade
                now.append('A')
            elif now[4] >= 80:
                now.append('B')
            elif now[4] >= 70:
                now.append('C')
            elif now[4] >= 60:
                now.append('D')
            else:
                now.append('F')
            data.append(now)
    show(data) #show는 현재의 데이터(data)를 평균 기준 내림차순 정렬하여 보여준다
else:
    with open("students.txt", 'r') as f:
        for line in f:
            now = line
            now = now.replace('\t', ' ')
            now = now.replace('\n', ' ')
            now = now.split(' ')
            now.pop()

            now[1] = now[1] + " " + now[2] # Student Name
            del now[2]

            now[2] = int(now[2]) #Midterm Score
            now[3] = int(now[3]) #Final Score
            now.append((now[2] + now[3]) / 2) # Average

            if now[4] >= 90: # Grade
                now.append('A')
            elif now[4] >= 80:
                now.append('B')
            elif now[4] >= 70:
                now.append('C')
            elif now[4] >= 60:
                now.append('D')
            else:
                now.append('F')
            data.append(now)
    show(data) #show는 현재의 데이터(data)를 평균 기준 내림차순 정렬하여 보여준다

while True: #사용자로부터 입력값을 받는다.
    print()
    print("[CMD]: show, search, changescore, add, searchgrade, remove, quit")# 내가 추가함(보고서에 작성)
    command = input("# ")
    if command == 'show':
        show(data)
    elif command == 'search':
        search(data)
    elif command == 'changescore':
        changescore(data)
    elif command == 'add':
        add(data)
    elif command == 'searchgrade':
        searchgrade(data)
    elif command == 'remove':
        remove(data)
    elif command == 'quit':
        select = input("Save data?[yes/no] ").upper()
        if select == 'YES':
            quit(data, select)
            break
        elif select == 'NO':
            break
        else:
            print("잘못 입력하셨습니다.")
    else:
        print("잘못된 입력입니다. 다시 입력하십시오.") #내가 추가한 내용(보고서에 작성)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




