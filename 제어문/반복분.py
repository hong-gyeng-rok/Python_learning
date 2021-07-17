#-------------------while 반복문
#tree_hit = 0
#
#while tree_hit < 10:
#    tree_hit = tree_hit +1
#    massage = f"나무를 {tree_hit}번 찍었습니다."
#    print(massage)
#    if tree_hit == 10:
#        print("넘~어~간~다~~")

#coffee = 10
#money = 300
#
#while money:
#    money = money -10
#    print("돈 받았습니다.\n 커피 드리겠습니다.\n")
#    coffee = coffee -1
#    massage = f"남은 커피는 {coffee}잔 입니다.\n"
#    잔고 = f"잔고는 {money}원 입니다."
#    print(massage,잔고)
#    if not coffee:
#        print("커피가 다 떨어졌습니다. \n 감사합니다.")
#        break
#    elif money < 100 :
#        print("잔고가 부족합니다.")
#        break   

# if 나머지가 0일 경우 while문 다시 시작 if 나머지가 있을 경우 print(a)
#a = 0
#
#while a < 10:
#    a = a+1
#    if a % 2 == 0:
#        continue
#    print(a)




#-------------------for 반복분

#기본형
#test_list = ['one', 'two', 'three']
#
#for i in test_list:
#    print(i)

# 문제 :60 점 이상이면 합격
#mark = [("국어", 90), ("수학", 25), ("영어", 67), ("과학", 45), ("사회", 80)]
#
#for (first, last) in mark:
#    if last >= 60:
#        print(first,": 합격")
#    else:
#        print(first,": 불합격")

# 구구단
#for i in range(2, 10):
#    print(f"------------{i}단------------")
#    for j in range(1, 10):
#        multiply = i * j
#        print(i,"X", j, "=", multiply)
#        print("-----------")
#    print(' ')
