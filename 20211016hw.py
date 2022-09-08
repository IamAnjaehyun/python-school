b1= {'bookname': 안드로이드앱개발 , 'author': 최전산 ,'company': PCB ,'price': 25000 ,'year': 2017}
b2= {'bookname': 파이썬 , 'author': 강수라 ,'company': 연두 ,'price': 22000 ,'year': 2019}
b3= {'bookname': 자바스크립트 , 'author': 박정식 ,'company': SSS ,'price': 23000 ,'year': 2018}
b4= {'bookname': HTML5 , 'author': 주환 ,'company': 대한 ,'price': 27500 ,'year': 2012}
b5= {'bookname': 컴파일러' , author': 장진웅 ,'company': PCB ,'price': 19500 ,'year': 2011}
b6= {'bookname': C언어 , 'author': 홍말숙 ,'company': 한국 ,'price': 22000 ,'year': 2010}
b7= {'bookname': 프로그래밍언어 , 'author': 현정숙 ,'company': 연두 ,'price': 15000 ,'year': 2019}
b8= {'bookname': Core파이썬 , 'author': 두더쥐 ,'company': 용설 ,'price': 27000 ,'year': 2021 }
b9= {'bookname': 자바자바 , 'author': 강수라 ,'company': 연두 ,'price': 18000 ,'year': 2018}

def printBook(bookName):
    print('제목: {}'.format(bookName))
    print('저자: {}'.format(d[bookName]['author']))
    print('출판사: {}'.format(d[bookName]['company']))
    print('가격: {}'.format(d[bookName]['price']))
    print()

while(True):
    info='도서검색키워드\n1. 도서명\n2. 저자명\n3. 출판사명\n선택(1,2,3) : '
    n=int(input(info))
    
    if n==1:
        key=input('제목 >>> ')
        #key='파이썬'
        cnt=0
        for name in dict():
           
        
                cnt+=1

        if cnt==0:
            print('검색한 도서가 없습니다.')
