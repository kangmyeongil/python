'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 201995004 강명일
    설명 : lab 7-5 함수는 튜플을 돌려줄 수 있다.
        반지름을 입력받아 원의 넓이와 둘레를 계산하시오.
        넓이와 둘레를 계산하는 함수를 작성하시오.
        함수는 넓이와 둘레를 함께 돌려줍니다.(return)

        [함수]
            3. 반지름을 받아서 매개변수에 저장한다.
            4. 넓이와 둘레를 계산한다.
            5. 넓이와 둘레를 돌려준다.(함수를 호출한 곳으로)
                return 넓이, 둘레
        [메인]
            1. 반지름을 입력받는다.
            2. 함수 호출 -> 반지름을 가지고 호출한다.
            6. 돌려받은 넓이와 둘레를 튜플로 저장한다.
                (넓이, 둘레)
            7. 출력한다.
'''
import math # 파이값 가져오기 위해 import
# 반지름이 radius인 원의 넓이, 둘레 반환하는 함수(area, circum)
def circle(radius):
    area = radius**2*math.pi # 넓이 계산
    circum = radius*2*math.pi # 둘레 계산
    return area, circum # 넓이와 둘레의 값을 튜플로 반환함

radius = float(input("반지름을 입력하세요 : "))
(a,c) = circle(radius)

print(f"원의 반지름 : {radius}, 원의 넓이 : {a:.2f}, 원의 둘레 : {c:.2f}")

# 변수 하나에도 저장해서 출력할수 있다
circle = circle(radius)
print(f"원의 반지름 : {radius}, 원의 넓이 : {circle[0]:.2f}, 원의 둘레 : {circle[1]:.2f}")