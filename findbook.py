import re

book_dict=dict()

book_dict['안드로이드앱개발'] = {'author': '최전산' ,'company': 'PCB' ,'price': '25000' ,'year': '2017'}
book_dict['파이썬'] = {'author': '강수라' ,'company': '연두' ,'price': '22000' ,'year': '2019'}
book_dict['자바스크립트'] = {'author': '박정식' ,'company': 'SSS' ,'price': '23000' ,'year': '2018'}
book_dict['HTML5'] = {'author': '주환' ,'company': '대한' ,'price': '27500' ,'year': '2012'}
book_dict['컴파일러'] = {'author': '장진웅' ,'company': 'PCB' ,'price': '19500' ,'year': '2011'}
book_dict['C언어'] = {'author': '홍말숙' ,'company': '한국' ,'price': '22000' ,'year': '2010'}
book_dict['프로그래밍언어'] = {'author': '현정숙' ,'company': '연두 ','price': '15000' ,'year': '2019'}

def printBook(bookName):
    print('제목: {}'.format(bookName))
    print('저자: {}'.format(book_dict[bookName]['author']))
    print('출판사: {}'.format(book_dict[bookName]['company']))
    print('가격: {}'.format(book_dict[bookName]['price']))
    print()


while(True):
    info='도서검색키워드\n1. 도서명\n2. 저자명\n3. 출판사명\n선택(1,2,3) : '
    n=int(input(info))
    
    if n==1:
        key=input('제목 >>> ')
        
        cnt=0
        for name in book_dict:
            regex=re.compile(key)
            mo=regex.search(name)
            if mo != None:
                printBook(name)
                cnt+=1
        if cnt==0:
            print('검색한 도서가 없습니다.\n')

    elif n==2:
        key=input('저자 >>> ')
        
        cnt=0
        for name in book_dict:
            regex=re.compile(key)
            mo=regex.search(book_dict[name]['author'])
            if mo != None:
                printBook(name)
                cnt+=1

        if cnt==0:
            print('검색한 도서가 없습니다.\n')

        
    elif n==3:
        key=input('출판사 >>> ')        
        
        cnt=0
        for name in book_dict:
            regex=re.compile(key)
            mo=regex.search(book_dict[name]['company'])
            if mo != None:
                printBook(name)
                cnt+=1

        if cnt==0:
            print('검색한 도서가 없습니다.\n')
            
        
    elif n==0:
        print('종료합니다.\n')
        break
    else:
        print('잘못된 입력입니다.\n')
