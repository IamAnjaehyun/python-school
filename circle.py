import math #pi값을 사용하기 위하여 import math 사용

#class 지정
class Circle:  #원의 넓이와 좌표에 관한 클래스
    radius=0 # 반지름 초기값 0
    cx=0 #x 좌표 초기값 0
    cy=0 #y 좌표 초기값 0

    def __init__(self, radius, cx, cy):  #원에 정보에 관한 생성자
        self.radius = radius  #입력받은 radius 원의 반지름
        self.cx = cx #입력받은 x좌표값이 원의 x좌표 
        self.cy = cy #입력받은 y좌표값이 원의 y좌표 
        
    def area(self):  #원의 넓이를 구해주는 예약어
        return self.radius*self.radius*math.pi # 반지름*반지름*pi값 , pi값은 import math 안에 내장되어있음.
    def center(self):  #원의 좌표를 알려주는 예약어
        return self.cx,self.cy #입력받은 x,y 값이 각각 cx,cy값이다.
    

def main():  #main 예약어
    radius=0 # 반지름 초기값 0
    cx=0 #x 좌표 초기값 0
    cy=0 #y 좌표 초기값 0
    
    print("정보를 입력하세요")
    radius=int(input("반지름:"))  #반지름 값 입력
    cx=int(input("x좌표:"))  #x좌표 값 입력
    cy=int(input("y좌표:"))  #y좌표 값 입력
    circle = Circle(radius,cx,cy)  #원에 관한 정보

    #함수호출
    print("원의 넓이: "+str(circle.area()))  #class 안의 area(원의 넓이) 예약어 호출
    print("중심좌표: "+str(circle.center()))  #class 안의 center(좌표값) 예약어 호출
 

if  __name__ == "__main__":  #시작점, main()예약어 호출해서 시작
    main()
