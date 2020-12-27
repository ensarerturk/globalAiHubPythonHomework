import sys
print("If you don't know the name you need to enter to boot the system, please read ""README.txt""."
      "\nBecause if you enter wrong 3 times, the system will shut down.\n")

name=input("Please enter a name :").upper()
surname=input("Please enter a surname :").upper()

tinfo=["ENSAR","ERTURK"]
tryin=0

#Control is done. If the entered name and the registered name do not match, 
#it is requested to enter it again. If it is entered incorrectly 3 times, the system shuts down
if tinfo[0]!=name or tinfo[1]!=surname:
    while 1:
            
        print("try again")
        name=input("Please enter a name :").upper()
        surname=input("Please enter a surname :").upper()
        tryin+=1
        if tryin==3:
            print("Please try again later")
            sys.exit()
        elif tinfo[0]==name and tinfo[1]==surname:
            
            break

## Part of the lesson selected. courses are listed and you are given the option to choose or exit the course. 

def lessons():
    lesson=[]
    courses=["Turkish","Math","Geometry","Physics","Chemistry","Biology","Social Studies","Physical education","Music","Art"]
    while 1:
        a=0
        for i in courses:
            print("{} -> {}".format(a,i))
            a=a+1
            
        sec=int(input("\nChoose Process :\n1-Add Course :\n2-Exit :\n="))
        #Courses taken are removed from the list in order not to be taken again.
        if sec==1:
            les=int(input("\nEnter the number of the lecture you want to add :\n="))
            lesson.append(courses[les])
            courses.pop(les)
      
        elif sec==2:
            print("Course selection is over\nBelow are the lessons you took.\n")
            break
          
    # If he / she chooses less than 3 or more than 5 courses, 
    # the message he / she failed the course is displayed on the screen.
    if len(lesson)<3 or len(lesson)>5:
        print("You failed in class")
        sys.exit()
    
    exam(lesson)   
    
#the method where exam grades are dictionary
def exam(lesson):
    exa={"midterm":0,"final":0,"project":0}
    a=0
    for e in lesson:
        print(f"{a} -> {e}")
        a+=1
    
    ex=int(input("please chose a lesson number : "))
    
    print("{} lesson selected ".format(lesson[ex]))
    midterm=int(input("Midterm Note :"))
    exa["midterm"]=midterm
    final=int(input("Final Note :"))
    exa["final"]=final
    proje=int(input("Project Note :"))
    exa["project"]=proje
    
    for key,value in exa.items():
        print("\n{} : {}".format(key,value))

    grade(midterm,final,proje)
   
##The method that the query is passed or failed    
def grade(midterm,final,proje):
    
    finalNote = midterm*0.3 + final*0.5 + proje*0.5
    
    if finalNote > 90:
        print("\nYour grade AA - passed")
    elif 70 < finalNote < 90:
        print("\nYour grade BB - passed")
    elif 50 < finalNote < 70:
        print("\nYour grade CC - passed")
    elif 30 < finalNote < 50:
        print("\nYour grade DD - passed")
    elif finalNote< 30:
        print("\nYour grade FF - failure")
                

## main method
#This is the place that returns the name entered into the system with the welcome text.
def main():
    print("\nWelcome {} {}\nYou can see the courses you can take below.".format(name,surname))
    lessons()

main()
        