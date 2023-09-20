'''
    작성일 : 2023년 09월 20일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 선택문 if~else
           년도를 입력 받아 윤년인지 아닌지 판단하는 프로그램.

           윤년? 
           연도를 4로 나누어 떨어지면 윤년.
           4로 나누어 떨어져도 100으로 나누어 떨어지면 평년.
           400으로 나누어 떨어지면 무조건 윤년.
'''

year = int(input("현재 년도를 입력하세요. : "))

# ver1.
if year % 4 == 0 :
    if  year % 100 == 0 and year % 400 != 0 :
        print(year, "년도는 윤년이 아닙니다.")
    else :
        print(year, "년도는 윤년입니다.")
else :
    print(year, "년도는 윤년이 아닙니다.")

# ver2.
if ((year % 4 == 0) and year % 100 != 0) or (year % 400 == 0) :
    print(year, "년도는 윤년입니다.")
else :
    print(year, "년도는 윤년이 아닙니다.")
