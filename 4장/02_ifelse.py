'''
    작성일 : 2023년 09월 20일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 선택문 if~else
           정수를 입력받아 짝수인지 홀수인지 판단
'''
# 1. 정수를 입력받는다.
i = int(input("정수를 입력하세요 : "))

# 2. 판단. 판단의 기준은 ?
if i % 2 == 0 :
    print(i, "는(은) 짝수입니다")
else :
    print(i, "는(은) 홀수입니다")