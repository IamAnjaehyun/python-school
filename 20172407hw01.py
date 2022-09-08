select, answer, num1, num2 = 0, 0, 0, 0
def menu():
    print("==============================")
    print("MENU")
    print("==============================")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 나눗셈")
    print("5. 나머지")

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

def remainer(num1,num2):
    return num1%num2

while True:
    menu()
    select=int(input("원하는 메뉴를 선택하시오(1-5) : "))
    if select == 1 :
        num1=int(input("숫자1: "))
        num2=int(input("숫자2: "))
        print("연산결과: ",num1,"+",num2,"=",add(num1,num2))
        y=input("계속하려면 y를 누르세요: ")
        if(y=='y'):
            continue
        else:
            break

        
    elif select == 2:
        num1=int(input("숫자1: "))
        num2=int(input("숫자2: "))
        print("연산결과: ",num1,"-",num2,"=",sub(num1,num2))
        y=input("계속하려면 y를 누르세요: ")
        if(y=='y'):
            continue
        else:
            break


    elif select == 3:
        num1=int(input("숫자1: "))
        num2=int(input("숫자2: "))
        print("연산결과: ",num1,"*",num2,"=",mul(num1,num2))
        y=input("계속하려면 y를 누르세요: ")
        if(y=='y'):
            continue
        else:
            break


    elif select == 4:
        num1=int(input("숫자1: "))
        num2=int(input("숫자2: "))
        print("연산결과: ",num1,"/",num2,"=",div(num1,num2))
        y=input("계속하려면 y를 누르세요: ")
        if(y=='y'):
            continue
        else:
            break


    elif select == 5:
        num1=int(input("숫자1: "))
        num2=int(input("숫자2: "))
        print("연산결과: ",num1,"%",num2,"=",remainer(num1,num2))
        y=input("계속하려면 y를 누르세요: ")
        if(y=='y'):
            continue
        else:
            break


    else:
        print("1~4만 입력해야합니다. 처음으로 돌아갑니다.")
        continue
