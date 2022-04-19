

print("-" * 40)                              #1
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic4 = {}
dic4.update(dic1)
print(f"dic4 :{dic4}")
dic4.update(dic2)
dic4.update(dic3)
print(f"dic4 :{dic4}")



print("-" * 40)                               #2
d1 = {1: 10, 2 :20, 3 :30}
def is_presented (x):
    if x in d1:
        print("key presented")
    else:
        print("not printed")
is_presented(5)

print("-" * 40)                                                       #3
a={'name':'suresh','college':'jntuk','branch':'mech','passOut':'2021'}
for i in a.items():
    print(i)


print("-" * 40)                                #4
n = 6
dict = dict()
for i in range (1, n+1):
    dict[i] = i*i
print(f"dict : {dict}")
print(len(dict))


print("-" * 40)                               #7
a=[1,2,3,4,5,6]
print(a[::-1])

print("-" * 40)                               #9
a=[1,2,3,4,5,6,7]
sum=0
for i in a:
    sum+=i
print('sum of the elements in list a is:',sum)




print("-" * 40)                               #10
list = [10, 20, 45, 80, 10, 60, 50, 55]
list.sort()
print(list[-2])


print("-" * 40)                                   #14
a=[1,2,3,4,5]
b=[4,5,1,6,7]
print("the common elements in both lists are:")
for i in a:
    for j in b:
        if i==j:
            print(i,end=',')

print("-" * 40)                               #15
# def list_count(list_a):
#     return len(list_a)
#
# list_a = [[1, 3], [5, 7], [9, 11], [13,15,17]]
# print(list_count(list_a))
#
# def dec.begin_end(f1):
#     def inner():
#         print("we will win the soccor wc {a} {b}")
#         return
#     return inner
#
# def dwa.starstop(f2):
#     def inner():
#         print("Happy sunday fun3 {x} {y} {z}")
#         return
#     return inner


