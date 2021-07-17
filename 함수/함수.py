#Function 

#my_list = [1,2,3]
#print(my_list.append(4))
#print(my_list)
#print(my_list.pop())

#def sum_many(*args):
#    sum = 0
#    for i in args:
#        sum = sum + i
#    return sum
#print(sum_many(1,2,3,24))

#def print_kwargs(**kwargs):
#    for k in kwargs.keys():
#        if(k == "name"):
#            print("당신의 이름은:" + k)
#
#print(print_kwargs(name="조수", b="2"))

#def sum_and_mul(a,b):
#    return a+b,a*b
#    
#print(sum_and_mul(1,2)[1])

#def say_myself(name, old, man = True):
#    print(f"나의 이름은 {name}입니다")
#    print(f"나의 나이는 {old}입니다")
#    if man:
#        print("나는 남자입니다.")
#    else:
#        print("나는 여자입니다.")
#say_myself(name = "홍경록",old = "19")

##변수
#a = 1
##a = 독립된 변수 = 함수 안에서만 쓰임 = 함수 안에서만 영향을 끼침
#def vartest(a):
#    a = a + 1
#    
#vartest(a)


##lambda 미사용
#def add(a,b):
#    return a+b
#    
##lambda 사용
#
#add = lambda a, b: a+b
#my_list = [lambda a, b:a+b, lambda a, b: a-b,lambda a, b: a*b,lambda a, b: a%b]
#print(my_list[3](1,2))

#f = open("새파일.txt", 'w', encoding="UTF-8")
#for i in range(1, 11):
#    data = "%d번째 줄입니다.\n" %i
#    f.write(data)
#f.close()

#f = open("새파일.txt", 'r', encoding="UTF-8")
#while True:
#    line = f.readline()
#    if not line: break
#    print(line)
#f.close