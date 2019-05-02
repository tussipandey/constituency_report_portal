from tkinter import *
import sys;
import subprocess
from collections import defaultdict
new_dict={}
new_list=[]
dict={}
fh=open("area.txt","r+")
for i in fh:
    c=i.split("$")
    for i in c:
        if (i==''):
            continue
        x=i.split("|")
        dict[x[0]]=x[1:]
print(dict)
fh.close()        
user_input=0
area=""
state=""


def ex():
    sys.exit()
    
        #selection sort code
    
def ssort(A):
    for i in range(len(A)): 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
        A[i], A[min_idx] = A[min_idx], A[i] 
    print(A)    
    return (A) 

        #Binary Search Code
    
    
def bina(l,key):
    i=0
    j=len(l)-1
    while(i<=j):
        mid=(i+j)//2
        if(l[mid]==key):
            return 1
        elif(l[mid]>key):
            j=mid-1
        else:
            i=mid+1
    return -1            
    
    
    
            #admin window function
    
def admin():
    
    window4=Tk()
    window4.geometry("500x300")
        #window = Toplevel(top)
    window4.configure(background='blue')    
    window4.title("Admin Panel")
    L7= Label(window4, text = "Data Entry",font='Helvetica 18 bold')
    L7.pack( side = TOP)
    L8 = Label(window4, text = "Enter the politician name")
    L8.place( x=10,y=95)
    E10 = Entry(window4, bd = 5)
    #E1.pack(side = RIGHT)
    E10.place(x = 180,y = 95)
    
    L9 = Label(window4, text = "Enter the area name")
    L9.place( x=10,y=125)
    E11 = Entry(window4, bd = 5)
    #E1.pack(side = RIGHT)
    E11.place(x = 180,y = 125)
    
     
    L10 = Label(window4, text = "Enter the party name")
    L10.place( x=10,y=155)
    E12 = Entry(window4, bd = 5)
    #E1.pack(side = RIGHT)
    E12.place(x = 180,y = 155)
    
    
    L12 = Label(window4, text = "Enter the state name")
    L12.place( x=10,y=185)
    E14 = Entry(window4, bd = 5)
    #E1.pack(side = RIGHT)
    E14.place(x = 180,y = 185)
    
    L11 = Label(window4, text = "Enter the Win Status 1/0")
    L11.place( x=10,y=215)
    E13 = Entry(window4, bd = 5)
    #E1.pack(side = RIGHT)
    E13.place(x = 180,y = 215)
    
                #function called on inserting data
    def l():
        global area
        global dict
        pol=E10.get()
        area=E11.get()
        party=E12.get()
        status=E13.get()
        global state
        state=E14.get()
        l=[]
        il=[]
        f=open("politician.txt","r")
        for lines in f:
            line=lines.split("$")
            #print(line)
            for k in line:
                if (k==''):
                    continue
                d=k.rstrip().split("|")
                l.append([d[0],d[2]])
                il.append(int(d[0]))
        if state not in dict:
            dict[state]=[area]
        elif(area in dict[state]):
            print("area in dic")
        else:
            dict[state].append(area)
        print(dict)   
        open('area.txt', 'w').close()
        fh=open("area.txt","a")
        for i in dict:
            x=dict[i]
            s=x[0]+"|"
            for j in range(1,len(x)):
                s+=x[j]+"|"
            s=s[:len(s)-1]    
                
            new_area=i+"|"+s+"$"
            fh.write(new_area)
                
        flag=0    
        for i in l:
            if i[1]==area:
                cid=i[0]
                flag=1
                break
        if(flag==0):  
            cid=(max(il))+1
        g=open("politician.txt","r+")
        z=g.readlines()
        if status=="1":
            x=open("k.txt","a")

            c=g.tell()
            v=area+"|"+str(c)+"$"
            x.write(v)
        ln=str(cid)+"|"+pol+"|"+area+"|"+party+"|"+status+"$"
        g.write(ln)

        ms="Record added"
        msg = messagebox.showinfo( "Response Message", ms)
                

        
    print("hello")
    def d():
            window4.destroy()
            mainm()    
    B12 = Button(window4, text = "Insert Data", command = l,activeforeground="Grey",activebackground="Green",relief=RAISED)
    B12.place(x = 10,y = 245)    
    B13 = Button(window4, text = "Main Menu",command=d,activeforeground="Grey",activebackground="Green",relief=RAISED)
    B13.place(x = 175,y = 245)
    
        
    B14 = Button(window4, text = "Exit",command=ex,activeforeground="Grey",activebackground="Green",relief=RAISED)
    B14.place(x = 370,y = 245)
    
    
def admin2():
    
    
    
    
    
    window6=Tk()
    window6.geometry("500x200")
        #window = Toplevel(top)
    window6.title("admin")
    
    
    def verify():
        ids=E1.get()
        
        def dm():
            window6.destroy()
            admin()
        passw=E2.get()
        if(ids=="admin" and passw=="123456"):
            ms="ADMIN LOGIN SUCCESSFULL"
            msg = messagebox.showinfo( "Response Message", ms)
            dm()
        else:
            ms1="WRONG CREDINTALS"
            msg1 = messagebox.showwarning( "Warning Message", ms1)
            
            
    L5= Label(window6, text = "ADMIN LOGIN",font='Helvetica 18 bold')
    L5.pack( side = TOP)
    
    L1 = Label(window6, text = "Enter your login id")
    L1.place( x=10,y=75)
    E1 = Entry(window6, bd = 5)
    #E1.pack(side = RIGHT)
    E1.place(x = 180,y = 75)
    
    L2 = Label(window6, text = "Enter the password")
    L2.place( x=10,y=105)
    E2 = Entry(window6, bd = 5)
    #E1.pack(side = RIGHT)
    E2.place(x = 180,y = 105)
    B = Button(window6, text = "Login", command = verify,activeforeground="Grey",activebackground="Green",relief=RAISED)
    B.place(x = 10,y = 170)
    def d():
        window6.destroy()
        mainm()
    B3 = Button(window6, text = "Main Menu",command=d,activeforeground="Grey",activebackground="Green",relief=RAISED)
    B3.place(x = 175,y = 170)
    
        # report window starts here
    
def  helloCallBack2():
    window3=Tk()
    window3.geometry("500x300")
        #window = Toplevel(top)
    window3.title("Username Entry")
    window3.configure(background='Grey')    
    L5= Label(window3, text = "FEEDBACK RETRIEVAL",font='Helvetica 18 bold')
    L5.pack( side = TOP)
    global dict  
    def update_options(*args):
        countries = dict[variable_a.get()]
        variable_b.set(countries[0])
        menu = y['menu']
        menu.delete(0, 'end')
        for country in countries:
            menu.add_command(label=country, command=lambda nation=country: variable_b.set(nation))
                    
    variable_a= StringVar(window3)
    variable_a.set('UP') # default value

    variable_b = StringVar(window3)

    variable_a.trace('w', update_options)

    L2 = Label(window3, text = "Select your State",font='Helvetica 12 bold')
    L2.place( x=70,y=85)

    w = OptionMenu(window3, variable_a, *dict.keys())
    w.place(x=240,y=85)

    L3 = Label(window3, text = "Enter your Place",font='Helvetica 12 bold')
    L3.place( x=70,y=155)
            
    y= OptionMenu(window3, variable_b, '')
    y.place(x=240,y=155)

    

            #function called on clicking get feedback button
        
    def lm():
        st=variable_a.get()
        ar=str(variable_b.get())
        print ("value of state is", variable_a.get())
        print ("value of place is", variable_b.get())
        subprocess.call(" python feed2.py 1", shell=True)
        
        
        
        #indexing operation
        
        
        
        
        x=open("k.txt","r")
        arid=""
        for i in x:
            c=i.split("$")
            for h in c:
                if h=='':
                    continue
                d=h.rstrip().split("|")
                #print(d)
                if d[0]==ar:
                    s=int(d[1])
                    b=open("politician.txt","r+")
                    b.seek(s)
                   # print(b.read(2))
                    arid=b.read(2)
    
            print(arid)     
            k=open("reports2.txt","r")   
            flag=0
            for lines in k:
                line=lines.split("$")
                for h in line:
                    if h=='':
                        continue
                    d=h.rstrip().split("|")
                  #  print(d[0],arid)
                    if(d[0]==arid and len(arid)>0):
                        print("he")
                        medr=d[1]
                        roadr=d[2]
                        overr=d[3]
                        no=d[4]
                        flag=1
                        break
            if(flag==0):
                ms="Ratings not available for the area yet"
                msg1 = messagebox.showwarning( "Response Message", ms)
                
                
            print("Rating for Healthcare = ",medr)
            print("Rating for infrastructure = ",roadr)
            print("Rating for other parameters = ",overr)
            print("No of reviews = ",no)
            
            
           
            fh=open("politician.txt","r+")
            k=defaultdict(list)
            wk=defaultdict(list)
            for i in fh:
                line=i.split("$")
                for h in line:
                    if h=='':
                        continue
                    d=h.rstrip().split("|")
                    if d[4]=='0':
                        k[d[0]].append([d[1],d[3]])
                    else:
                        wk[d[0]].append([d[1],d[3]])
            c=k[arid]    
            wc=wk[arid]
            rparty=wc[0][1]
            rleader=wc[0][0]
            print(wc)
            print("LOSER GROUP")
            
            def response(c,rparty,rleader,medr,roadr,overr,no,ar):
                window5=Tk()
                window5.geometry("1500x1300")
                    #window = Toplevel(top)
                window5.configure(background='Skyblue')    
                window5.title("Report")
                rar=(((int(medr)*int(no))+(int(roadr)*int(no))+(int(overr)*int(no))))
               
                print(rar)
                rara=(rar/(int(no)*10*3))*100
                print(rara)
                rara=round(rara)
                L8= Label(window5, text = "-----------------REPORT CARD--------------------",font='Helvetica 18 bold')
                L8.pack(side=TOP)
                L19= Label(window5, text = ar,font='Helvetica 18 bold')
                L19.place(x=550,y=70)
                L15= Label(window5, text = "PARAMETERS      RATING       COUNT",font='Helvetica 16 bold')
                L15.place(x=100,y=120) 
                L9= Label(window5, text = "HEALTHCARE                             "+medr+"                         "+no,font='Helvetica 12 ')
                L9.place(x=100,y=180)
                L10= Label(window5, text = "INFRASTRUCTURE                       "+roadr+"                       "+no,font='Helvetica 12 ')
                L10.place(x=100,y=240)
                L11= Label(window5, text = "OVERALL                                       "+overr+"                      "+no,font='Helvetica 12 ')
                L11.place(x=100,y=290)
                L19= Label(window5, text = "PERCENTAGE SCORE OF LEADER               "+str(rara),font='Helvetica 14 bold')
                L19.place(x=100,y=350)
                L12= Label(window5, text = "---RULING CANDIDATE----",font='Helvetica 18 bold')
                L12.place(x=800,y=120)
                L13= Label(window5, text = "NAME                                                      PARTY\n\n",font='Helvetica 14 bold')
                L13.place( x=800,y=180)
                
                #L13= Label(window5, text = "NAME                 PARTY",font='Helvetica 18 bold')
                #L13.place( x=100,y=450)
                L14= Label(window5, text = rleader+"                                   "+rparty,font='Helvetica 12')
                L14.place( x=800,y=220)
                L16= Label(window5, text = "---CONTENDER CANDIDATE---",font='Helvetica 18 bold')
                L16.place(x=100,y=450)
                ms1=""
                for i in c:
                    ms1+=i[0]+"\t\t"+i[1]+"\n"
                print(ms1)     
                L18= Label(window5, text = "NAME                                PARTY\n\n",font='Helvetica 14 bold')
                L18.place( x=150,y=500)
                L17= Label(window5, text = ms1,font='Helvetica 12 ')
              #  L17= Label(window5, text = "NAME                  PARTY\n\n"+ms1,font='Helvetica 14 bold ')
               
                L17.place( x=150,y=530)
                
                def f():
                    window5.destroy()
                    helloCallBack2()
                def fr():
                    window5.destroy()
                    mainm()    
                B14 = Button(window5, text = "Back", command =f,activeforeground="Grey",activebackground="Green",relief=RAISED)  
                B14.place(x = 550,y =650)
                B19 = Button(window5, text = "Main Menu", command =fr,activeforeground="Grey",activebackground="Green",relief=RAISED)  
                B19.place(x = 700,y =650)
                B18 = Button(window5, text = "Exit",command=ex,activeforeground="Grey",activebackground="Green",relief=RAISED)
                B18.place(x = 850,y =650)
               # ms1="Other candidates are"+"\n"+"CANDIDATE-------PARTY"+"\n"
       
                
                
                
                
            def recl():
                window3.destroy()
                response(c,rparty,rleader,medr,roadr,overr,no,ar)
            recl()    
            
        
            ms1="Other candidates are"+"\n"+"CANDIDATE-------PARTY"+"\n"
            for i in c:
                ms1+=i[0]+"\t\t"+i[1]+"\n"
                print("the candidate is "+i[0]+" "+"party is "+i[1])


            
          #  ms="Ruling party is"+" "+wc[0][1]+"\n"+"Ruling Leader is"+" "+wc[0][0]+"\n"+"Rating for Healthcare = "+medr+"\n"+"Rating for infrastructure = "+roadr+"\n"+"Rating for other parameters = "+overr+"\n"+"No of reviews = "+no
           # msg1 = messagebox.showinfo( "Response Message", ms)
        
            #msg2 = messagebox.showinfo( "Response Message", ms1)
             
                 
    
    def d():
        window3.destroy()
        mainm()
        
    B11 = Button(window3, text = "Get Feedback", command = lm,activeforeground="Grey",activebackground="Green",relief=RAISED)
    B11.place(x = 10,y = 250)    
    B9 = Button(window3, text = "Main Menu",command=d,activeforeground="Grey",activebackground="Green",relief=RAISED)
    B9.place(x = 175,y = 250)
    
        
    B10 = Button(window3, text = "Exit",command=ex,activeforeground="Grey",activebackground="Green",relief=RAISED)
    B10.place(x = 370,y = 250)
    
    
    
    

from tkinter import messagebox

                            # main window starts here

def mainm():

    top = Tk()
    top.geometry("600x400")
    top.configure(background='blue')
    L= Label(top, text = "Constituency Feedback System",font='Helvetica 18 bold')
    L.pack( side = TOP)
    
    L19= Label(top, text = "Welcome to the portal.Select the options to continue !!",font='Helvetica 12 bold')
    L19.place(x=100,y=90)
    
                            #function called when rating button is clicked
        
    def helloCallBack():
        
        window=Tk()
        window.geometry("500x300")
        window.configure(background='Sky blue')
        #window = Toplevel(top)
        window.title("Username Entry")

        L= Label(window, text = "REGISTER AND LOGIN",font='Helvetica 18 bold')
        L.pack( side = TOP)
               
                  #function called when login button is clicked
                
        def lmsg():
                global user_input
                user_input = E1.get()  
                f=open("voter2.txt","r")
                l=[]
                global new_dict
                global new_list
                for lines in f:
                    line=lines.split("$")
                    for h in line:
                        if h=='':
                            continue
                        d=h.rstrip().split("|")
                        new_dict[d[0]]=d[1:]
                        l.append(d[0])        
                new_list=ssort(l)        
                flag=bina(new_list,user_input)
                print(flag)

                if(user_input==""):
                    ms="Please Enter Your Aadhar"
                    msg = messagebox.showinfo( "Response Message", ms)
                    
                elif(flag==-1):
                    ms="LOGIN SUCCESSFULL"+" "+user_input
                    msg = messagebox.showinfo( "Response Message", ms)
                    getinput()
                else:
                    ms="Aadhar Already Exist"+" "+user_input
                    msg = messagebox.showwarning( "Warning Message", ms)
                    
                    #function called on successfull login
                    
                    
        def getinput():
            user_input = E1.get()
            print(user_input)


            window.destroy()
            window2 = Tk()
            window2.title("Username Entry")


            L0= Label(window2, text = "Enter the Ratings",font='Helvetica 18 bold')
            L0.pack( side = TOP)
            window2.geometry("600x600")
            window2.configure(background='blue')
            
            def getdata2():
                print("You selected the option " + str(var.get()))
                
            def getdata3():
                print("You selected the option " + str(var2.get()))  
                
            def getdata4():
                print("You selected the option " + str(var3.get()))    
    
    
                                #function for rating submission 
        
            def getdata():
                flag=0
                ar=""


                user_name = E2.get()
                vot=str(user_name)
                print(user_name)
                medr=str(var.get())
                roadr=str(var2.get())
                overr=str(var3.get())
                st=variable_a.get()
                ar=variable_b.get()
                if( user_name =="" or vot=="" or medr=="0" or roadr=="0" or overr=="0" or st=="" or ar==""):
                    
                    ms="Please fill all the fields"
                    msg = messagebox.showwarning( "Response Message", ms)
                else:    
                    
                    ms="Thankyou for your response"+" "+user_name
                    msg = messagebox.showinfo( "Response Message", ms)

                    print("You selected the option " + str(var.get()))
                    print("You selected the option " + str(var2.get()))
                    print("You selected the option " + str(var3.get()))


                    print ("value of state is", variable_a.get())
                    print ("value of place is", variable_b.get())

                    global new_dict
                    global new_list
                    global user_input


                    new_dict[user_input]=[vot,st,ar]
                    new_list.append(user_input)
                    newww=[]
                    for i in new_list:
                        newww.append(int(i))    
                    new_list=[]  
                    ne=ssort(newww)
                    for i in ne:
                        new_list.append(str(i))

       
                    open('voter2.txt', 'w').close()
                    fh=open("voter2.txt","a")
                    print(new_list)
                    for i in new_list:
                        d_val=new_dict[i]
                        x=i+"|"+d_val[0]+"|"+d_val[1]+"|"+d_val[2]+"$"
                        fh.write(x)




                    k=open("politician.txt","r")
                    for lines in k:
                        line=lines.split("$")
                        for h in line:
                            if h=='':
                                continue
                            d=h.rstrip().split("|")
                            if(d[2]==ar and len(ar)>0):
                                print("haio")
                                arid=d[0]
                                flag=1
                                break

                    if(flag==0):
                        ms="Ratings not available for the area yet"
                        msg1 = messagebox.showwarning( "Response Message", ms)            
               #     
                    else:
                        print("THANK YOU! YOUR RESPONSE HAS BEEN RECORDED \n ")
                        #cid=int(line[0])
                        g=open("rating2.txt","a")
                        ln=arid+"|"+medr+"|"+roadr+"|"+overr+"|"+"1"+"|"+user_input+"$"
                        g.write(ln)  
                        
                        
                        # Rating window starts here
                        
            L1 = Label(window2, text = "Enter your name")
            L1.place( x=10,y=105)
            E2 = Entry(window2, bd = 5)
   
            E2.place(x = 150,y = 105)
        
           
            global dict    
            
            
            def update_options2(*args):
                print(variable_b.get())
                are=variable_b.get()
                print(are)
                fpp=open("politician.txt","r")
                for lines in fpp:
                    line=lines.split("$")
                    #print(line)
                    for k in line:
                        #print(k)
                        if (k==''):
                            continue
                        d=k.rstrip().split("|")
                        #print(d)
                        if(d[2]==are and d[4]=="1"):
                            winn=d[1]
                L21 = Label(window2, text = "Rating for \n"+winn,font='Helvetica 14 bold')
                L21.place( x=350,y=155)            
                
                
                
                
            """              
            def update_options2(*args):
               # print(variable_a.get())
                 are=variable_b.get()
                f=open("politician.txt","r")
                for lines in f:
                    line=lines.split("$")
            #print(line)
                for k in line:
                    if (k==''):
                        continue
                d=k.rstrip().split("|")
                if(d[2]==ar):
                    print(d[1])
             """        
            
            def update_options(*args):
              #  print(variable_a.get())
             #   print(variable_b.get())
                countries = dict[variable_a.get()]
              #  variable_b.set(countries[0])
                menu = y['menu']
                menu.delete(0, 'end')
                for country in countries:
                    menu.add_command(label=country, command=lambda nation=country: variable_b.set(nation))
            
            
            def getl(value):
                print(value)
            
            
            
            variable_a= StringVar(window2)
            variable_a.set('UP') # default value

            variable_b = StringVar(window2)

            variable_a.trace('w', update_options)
            variable_b.trace('w', update_options2)


            L2 = Label(window2, text = "Enter your State")
            L2.place( x=10,y=145)

            w = OptionMenu(window2, variable_a, *dict.keys())
            w.place(x=150,y=145)

            L3 = Label(window2, text = "Enter your Place")
            L3.place( x=10,y=195)
            
            y= OptionMenu(window2, variable_b, '')
            y.place(x=150,y=195)

            
      
            L15 = Label(window2, text = "Enter the ratings")
            L15.place( x=10,y=230)
            
            L5 = Label(window2, text = "Healthcare and Medicines")
            L5.place( x=10,y=260)
            
            
            var = IntVar()
            
            R1 = Radiobutton(window2, text = "1", variable = var, value = 1,
                              command = getdata2)
            R1.place(x=170,y=260)
            #R1.pack( anchor = W )

            R2 = Radiobutton(window2, text = "2", variable = var, value = 2,
                              command = getdata2)
            R2.place(x=210,y=260)
            #R2.pack( anchor = W )

            R3 = Radiobutton(window2, text = "3", variable = var, value = 3,
                              command = getdata2)
            R3.place(x=250,y=260)

            R4 = Radiobutton(window2, text = "4", variable = var, value = 4,
                              command = getdata2)
            R4.place(x=290,y=260)

            R5= Radiobutton(window2, text = "5", variable = var, value = 5,
                              command = getdata2)
            R5.place(x=330,y=260)

            R6 = Radiobutton(window2, text = "6", variable = var, value = 6,
                              command = getdata2)
            R6.place(x=370,y=260)

            R7 = Radiobutton(window2, text = "7", variable = var, value = 7,
                              command = getdata2)
            R7.place(x=410,y=260)

            R8 = Radiobutton(window2, text = "8", variable = var, value = 8,
                              command = getdata2)
            R8.place(x=450,y=260)
            R9 = Radiobutton(window2, text = "9", variable = var, value = 9,
                              command = getdata2)
            R9.place(x=490,y=260)

            R10 = Radiobutton(window2, text = "10", variable = var, value = 10,
                              command = getdata2)
            R10.place(x=530,y=260)

            
    
            L6 = Label(window2, text = "Roads and infrastructure")
            L6.place( x=10,y=300)
            
            
            var2 = IntVar()
            
            R11 = Radiobutton(window2, text = "1", variable = var2, value = 1,
                              command = getdata3)
            R11.place(x=170,y=300)
            #R1.pack( anchor = W )

            R12 = Radiobutton(window2, text = "2", variable = var2, value = 2,
                              command = getdata3)
            R12.place(x=210,y=300)
            #R2.pack( anchor = W )

            R13 = Radiobutton(window2, text = "3", variable = var2, value = 3,
                              command = getdata3)
            R13.place(x=250,y=300)

            R14 = Radiobutton(window2, text = "4", variable = var2, value = 4,
                              command = getdata3)
            R14.place(x=290,y=300)

            R15= Radiobutton(window2, text = "5", variable = var2, value = 5,
                              command = getdata3)
            R15.place(x=330,y=300)

            R16 = Radiobutton(window2, text = "6", variable = var2, value = 6,
                              command = getdata3)
            R16.place(x=370,y=300)

            R17 = Radiobutton(window2, text = "7", variable = var2, value = 7,
                              command = getdata3)
            R17.place(x=410,y=300)

            R18 = Radiobutton(window2, text = "8", variable = var2, value = 8,
                              command = getdata3)
            R18.place(x=450,y=300)
            R19 = Radiobutton(window2, text = "9", variable = var2, value = 9,
                              command = getdata3)
            R19.place(x=490,y=300)

            R20 = Radiobutton(window2, text = "10", variable = var2, value = 10,
                              command = getdata3)
            R20.place(x=530,y=300)


            L7 = Label(window2, text = "Overall Rating ")
            L7.place( x=10,y=330)
            
            
            var3 = IntVar()
            
            R21 = Radiobutton(window2, text = "1", variable = var3, value = 1,
                              command = getdata4)
            R21.place(x=170,y=330)
            #R1.pack( anchor = W )

            R22 = Radiobutton(window2, text = "2", variable = var3, value = 2,
                              command = getdata4)
            R22.place(x=210,y=330)
            #R2.pack( anchor = W )

            R23 = Radiobutton(window2, text = "3", variable = var3, value = 3,
                              command = getdata4)
            R23.place(x=250,y=330)

            R24 = Radiobutton(window2, text = "4", variable = var3, value = 4,
                              command = getdata4)
            R24.place(x=290,y=330)

            R25= Radiobutton(window2, text = "5", variable = var3, value = 5,
                              command = getdata4)
            R25.place(x=330,y=330)

            R26 = Radiobutton(window2, text = "6", variable = var3, value = 6,
                              command = getdata4)
            R26.place(x=370,y=330)

            R27 = Radiobutton(window2, text = "7", variable = var3, value = 7,
                              command = getdata4)
            R27.place(x=410,y=330)

            R28 = Radiobutton(window2, text = "8", variable = var3, value = 8,
                              command = getdata4)
            R28.place(x=450,y=330)
            R29 = Radiobutton(window2, text = "9", variable = var3, value = 9,
                              command = getdata4)
            R29.place(x=490,y=330)

            R30 = Radiobutton(window2, text = "10", variable = var3, value = 10,
                              command = getdata4)
            R30.place(x=530,y=330)
     
            def cl():
                
                getdata()
                window2.destroy()
                mainm()
                          

     
            
            B1 = Button(window2, text = "SUBMIT", command = cl,activeforeground="Grey",activebackground="Green",relief=RAISED)
            B1.place(x = 10,y = 375)
            def f():
                window2.destroy()
                helloCallBack()
            B4 = Button(window2, text = "Back", command =f,activeforeground="Grey",activebackground="Green",relief=RAISED)  
            B4.place(x = 150,y =375)
            B8 = Button(window2, text = "Exit",command=ex,activeforeground="Grey",activebackground="Green",relief=RAISED)
            B8.place(x = 300,y =375 )
            window2.mainloop()


                #Login window buttons and options

        L1 = Label(window, text = "Enter your Aadhar no")
        L1.place( x=10,y=155)
        E1 = Entry(window, bd = 5)
    #E1.pack(side = RIGHT)
        E1.place(x = 180,y = 155)
        B = Button(window, text = "Register and Login", command = lmsg,activeforeground="Grey",activebackground="Green",relief=RAISED)
        B.place(x = 10,y = 200)
        def d():
            window.destroy()
            mainm()
        B3 = Button(window, text = "Main Menu",command=d,activeforeground="Grey",activebackground="Green",relief=RAISED)
        B3.place(x = 175,y = 200)
    
        
        B6 = Button(window, text = "Exit",command=ex,activeforeground="Grey",activebackground="Green",relief=RAISED)
        B6.place(x = 370,y = 200)

        window.mainloop()

    def new():
        top.destroy()
        helloCallBack()
    def ne():
        top.destroy()
        helloCallBack2()
        
        
                                 # main window button and options 
            
    B = Button(top, text = "Rate", command =new,activeforeground="Brown",activebackground="Grey",relief=RAISED)
    B.place(x = 150,y = 150)

    B = Button(top, text = "Report", command = ne,activeforeground="Brown",activebackground="Grey",relief=RAISED)
    B.place(x = 300,y = 150)  
    
    B7= Button(top, text = "Exit",command=ex,activeforeground="Brown",activebackground="Grey",relief=RAISED)
    B7.place(x = 450,y = 350)
    
    def adm():
        top.destroy()
        admin2()
    B11 = Button(top, text = "Admin", command = adm,activeforeground="Red",activebackground="Grey",relief=RAISED)
    B11.place(x = 450,y = 150)  
    
    top.mainloop()
    
                                           # main functiom call   
mainm()    
