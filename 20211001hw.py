select, answer, num1, num2 = 0, 0, 0, 0

print("==============================")
print("MENU")
print("==============================")
print("1. 덧셈")
print("2. 뺄셈")
print("3. 곱셈")
print("4. 나눗셈")
print("5. 나머지")


select=int(input("원하는 메뉴를 선택하시오  : "))
if select == 1 :
    num1=int(input("숫자1: "))
    num2=int(input("숫자2: "))
    answer=num1+num2
    print("연산결과: ",num1,"+",num2,+"=",answer)
    y=(string(input("계속하려면 y를 누르세요: "))
    if(y=="y")
       continue

elif select == 2:
    num1=int(input("숫자1: "))
    num2=int(input("숫자2: "))
    answer=num1-num2
    print("연산결과: ",num1,"-",num2,+"=",answer)
    y=(string(input("계속하려면 y를 누르세요: "))
    if(y=="y")
       continue

elif select == 3:
    num1=int(input("숫자1: "))
    num2=int(input("숫자2: "))
    answer=num1*num2
    print("연산결과: ",num1,"*",num2,+"=",answer)
    y=(string(input("계속하려면 y를 누르세요: "))
    if(y=="y")
       continue

elif select == 4:
    num1=int(input("숫자1: "))
    num2=int(input("숫자2: "))
    answer=num1/num2
    print("연산결과: ",num1,"/",num2,+"=",answer)
    y=(string(input("계속하려면 y를 누르세요: "))
    if(y=="y")
       continue

elif select == 5:
    num1=int(input("숫자1: "))
    num2=int(input("숫자2: "))
    answer=num1%num2
    print("연산결과: ",num1,"%",num2,+"=",answer)
    y=(string(input("계속하려면 y를 누르세요: "))
    if(y=="y")
       continue

else
    print("1또는 2만 입력해야합니다.")
    break;
