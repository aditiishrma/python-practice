# finally keyword is used along with try...except..else block
# it is basically a conclusion of a program with a delighful msg
def func1() :
 try :
    a=[1,4,7,2] # indexes are assigned & on their basis the output is generated
    i=int(input("Enter the index : "))
    print(a[i])
    return 1
 except :
    print("Some error occurred")
    return 0
# finally :
#     print("I'm always executed bachhaa !")
print("I'm always executed bachhaa !")
x = func1()
print(x)