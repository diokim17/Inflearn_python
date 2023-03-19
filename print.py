# Chapter 01_1
# 파이썬 완전 기초
# print에 대해
# 참조 https://www.python-course.eu/python3_formattered_output.php

## 기본 출력
print('python start')  # 주로 많이 사용
print("python start")  # 주로 많이 사용
print('''python start''')
print("""python start""")
# line 7 ~ 10 동일한 결과 값 : python start

print()  # 줄 바꿈으로 활용

## separator 옵션
# 인수 즉 파라미터를 sep 옵션을 이용해 연결해줌
print('p', 'y', 't', 'h', 'o', 'n', sep='')   # python
print('p', 'y', 't', 'h', 'o', 'n', sep=',')  # p,y,t,h,o,n
print('p', 'y', 't', 'h', 'o', 'n', sep='|')  # p|y|t|h|o|n
print('dykim335', 'gmail.com', sep='@')      # dykim335@gmail.com

print()

## end 옵션
# print문은 자동으로 줄 바꿈을 해주지만, end 옵션을 이용하면 줄 바꿈이 아니라 end=''의 ''안에 있는 문자로 이어짐
print('welcome to', end='')
print('IT News')
# welcome toIT News

print("Hello", end=' ')
print("I'm", end=' ')
print("Dio")
# Hello I'm Dio

print('dykim335', end='@')
print('gmail.com')
# dykim335@gmail.com

print()

## file 옵션
# 현재 이 내용을 내가 외부에 어떤 특정한 파일을 사용할 떄 사용
import sys

print("Learn Python", file=sys.stdout) # sys.stdout 콘솔 아웃을 의미
# Learn Python

print()

## format (d, s, f ...)
# d=정수(digit), s=문자열(string), f=실수(float)
print("%s %s" %("one", "two")) # 문자열 대체 가능 즉, 첫번째 %s 자리에 one, 두번째 %S 자리에 two
# one two

print("{} {}" .format("one", "two")) # print("{} {}") -> 암묵적으로 {0} {1}이므로 생략해서 적은 것
# one two
# line 52, 55 동일한 결과 값
# 52번은 오직 문자열 왜냐하면, %s로 지정을 해줬기 때문
# 55번은 상관없이 정수, 실수도 가능 {}알아서 매핑해줌

print("{1} {0}" .format("one", "two")) # 컴퓨터는 0부터 시작 즉, 자리 수가 0,1,2,... 이렇게 진행
# 따라서 format("0", "1")의 자리이므로 {1}의 자리에 1이 들어가게 됨, {0}의 자리에 0이 들어가게 됨
# two one

# %s
print("%10s" %("python")) # 10 의미: 10개의 자리수
# (    python)
# 10개의 자리 중 python의 6개 자리는 출력하고 남은 자리는 왼쪽에서 부터 공백으로 채움

print("{:>10}" .format("python"))  # 10 자리 중 왼쪽에서 공백을 채움
# (    python)

print("%-10s" %("python")) 
print("{:10}" .format("python"))  
# (python    )

print("{:->10}" .format("python")) # 왼쪽 공백을 -로 채움
# (----python)

print("{:^10}" .format("python"))  # 10자리에서 중앙 정렬
# (  python  )

print("%5s" %("python"))   # 5자리 지정을 해도 문자가 5글자 이상이면 그냥 입력한 문자로 출력
# python
print("%.5s" %("python"))  # 5자리만 출력
# pytho

