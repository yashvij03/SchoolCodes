def csvcreate():
    import csv
    f=open("data.csv",'w')
    L=[["Adm No.",'Name','Class','Sec','Marks']]
    ans="y"
    while ans== "y" or ans=="Y":
        adno=int(input("Enter admission number:"))
        na=input("Enter Name:")
        cla=int(input("Enter class:"))
        sec=input("Enter section:")
        mar=float(input("Enter marks:"))
        ans=input("Do you wish to enter more entries(y/n)?")
        lis=[adno,na,cla,sec,mar]
        L.append(lis)
    print(L)
    csvwriter=csv.writer(f)
    csvwriter.writerows(L)
    f.close() 

def addcsv():
    import csv
    f=open("data.csv",'a')
    write=csv.writer(f)
    ans="y"
    L=[]
    while ans=="y" or ans=="Y":
        adno=int(input("Enter admission number:"))
        na=input("Enter Name:")
        cla=int(input("Enter class:"))
        sec=input("Enter section:")
        mar=float(input("Enter marks:"))
        lis=[adno,na,cla,sec,mar]
        L.append(lis)
        ans=input("Do you wish to enter more entries(y/n)?")
    print(L)
    write.writerows(L)
    f.close()

def searchcsv():
    import csv
    f=open("data.csv",'r')
    adm=int(input("Enter admission number:"))
    found=False
    k=0
    data=csv.reader(f)
    next(f)
    for entry in data:
        if int(entry[0])==adm:
            print (entry)
            found=True
    if found==False:
        print("Data entry not found")

def productcsv():
    import csv
    f=open("products.csv",'w')
    L=[]
    head=['Prod. Id','Name','Price']
    ans="y"
    L.append(head)
    while ans=="y" or ans=="Y":
        p_id=input("Enter product id:")
        p_name=input("Enter product name:")
        p_price=float(input("Enter price:"))
        item=[p_id,p_name,p_price]
        L.append(item)
        ans=input("Do u wanna enter more items?")
    writer=csv.writer(f)
    writer.writerows(L)
    f.close()

def addproduct():
    import csv
    f=open("products.csv",'a')
    write=csv.writer(f)
    ans="y"
    L=[]
    while ans=="y" or ans=="Y":
        p_id=input("Enter product id:")
        p_name=input("Enter product name:")
        p_price=float(input("Enter price:"))
        item=[p_id,p_name,p_price]
        L.append(item)
        ans=input("Do u wanna enter more items?")
    write.writerows(L)
    f.close()

def searchprod():
    import csv
    f=open("products.csv",'r')
    items=csv.reader(f)
    next(f)
    for item in items:
        if  float(item[0])>=float(500):
            print (item)

def push():
    play={'Kohli':78,'Dhoni':36,'Pant':63,'Rohit':50}
    players={}
    ans="y"
    while ans=="y" or ans=="Y":
        name=input("Enter player name:")
        run=int(input("Enter player runs:"))
        players[name]=run
        ans=input("do you wish to enter more records?")
    L1=play.keys()
    Stack=[]
    for i in L1:
        if play[i]>50:
            Stack.append(i)
    return Stack
 
def pop(Stack):
    print("Contents in the stack are:")
    for i in range(len(Stack)):
        if len(Stack)==0:
           print("Underflow")
           print("Stack is empty")
        else:
            print(Stack.pop())

N=[12,15,55,6,72,80,99,10,69,5]

def div5(N):
    stack=[]
    for i in N:
        if i%5==0:
            stack.append(i)
    return stack


def POP(stk):
    print("Contents in the stack are:")
    for i in range(len(stk)):
        if len(stk)==0:
           print("Underflow")
           print("Stack is empty")
        else:
            print(stk.pop())

            
