'''
    작성일 : 2023년 09월 20일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : 선택문 if
           성적을 입력받아 60점 이상이면 "합격입니다"를 출력
'''

# 1. 성적을 입력 받는다. -> 입력 받아(문자) 정수로 변환하여 변수에 저장.

score = int(input("성적 입력 : "))

# 2. 만약에 성적이 60점 이상이면 "합격" 출력.

if score >= 60 :
    print("합격입니다.")

'''
자동차의 속도를 입력받아 속도를 출력하고 속도가 30km/h이면 "과속입니다. 속도를 줄이세요."를 출력하고,
속도와 상관 없이 "안전 운전 하세요"를 출력 
'''
# 1. 속도 입력 받는다. -> 정수로 입력 받는다.
speed = int(input("현재 속도를 입력하세요 : "))

# 2. 현재 속도 출력
print("현재 속도 : {} km/h" .format(speed))
print(f"현재 속도 : {speed}km/h")

# 3. 판단. 속도가 30 이상인가?
if speed >= 30 :
    print("과속입니다. 속도를 줄이세요.")

print("안전 운전 하세요.")
