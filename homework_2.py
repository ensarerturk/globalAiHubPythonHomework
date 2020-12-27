#first asked how many users to add.The process will continue until the specified number.
i=int(input("kaç kullanıcı ekleyeceksiniz :"))
liste=list()

while 0<i:
    fname=input("Please send the first name :")
    lname=input("Please sen the last name :")
    age=int(input("Please sen the age :"))
    birt=int(input("Please send the date of birt(year) :"))
    
    #Values received from the user are added to the list
    liste.append(fname)
    liste.append(lname)
    liste.append(age)
    liste.append(birt)    
   
    #the list is printed on the screen
    for x in liste:
        print(x)
    
    #Control is made according to the age taken from the user.
    if age<18:
        print("You can't go out cause it's too dangerous")
    else:
        print("You can go out to the street")
        
    i+=1
    
    a=2020-int(liste[3])
    print(a)
    
    
    