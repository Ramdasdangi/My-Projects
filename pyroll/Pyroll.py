
import mysql.connector
import datetime
from tabulate import tabulate

db=input("enter name of your database : ")

mydb=mysql.connector.connect(host='localhost',
                             user='root',
                             passwd='raaz123',
                             auth_plugin="mysql_native_password"
                             )
mycursor=mydb.cursor()

sql="create database if not exists %s"%(db,)
mycursor.execute(sql)
print("databses created successfully ")
mycursor=mydb.cursor()
mycursor.execute("use "+db)
Tablename=input("name of table to be created : ")
query="create table if not exists "+Tablename+"\
(empno int primary key,\
name varchar(15) not null,\
job varchar(15),\
Basicsalary int ,\
DA float,\
HRA float ,\
Gross_Salary float,\
Tax float ,\
NetSalary float)"

print("table "+ Tablename +" created successfully...." )
mycursor.execute(query)


while True :
    print('\n\n\n')
    print("*"*95 )
    print('\t\t\tMain Menu '  )
    print( "*"*95 )
    print( '\t1. Adding Employee records')
    print( '\t2. For Displaying Record of all the Employees ' )
    print( '\t3. For Displaying Record of a particular Employee ' )
    print( '\t4. For deleting  Records of all the Employees ' )
    print( '\t5. For Deleting a  Record of a particular Employee'  )
    print( '\t6. For Modification in a record '  )
    print( '\t7. For Displaying payroll'  )
    print( '\t8. For Displaying Salary Slip of all the Employees '  )
    print( '\t9. For Displaying Salary Slip of a particular the Employee ' )
    print( '\t10.For Exit ' )
    print('enter choice...',end='')
    choice=int(input())
    if choice==1 :
        try :
            print("enter employee information......")
            mempno=int(input("enter employee no : "))
            mname=input("enter employee name : ")
            mjob=input("enter employee job :")
            mbasic=float(input("enter basic salary : "))
            if mjob.upper()=='OFFICER':
                mda=mbasic*0.5
                mhra=mbasic*0.35
                mtax=mbasic*0.2
            elif mjob.upper()=='MANAGER':
                mda=mbasic*0.45
                mhra=mbasic*0.30
                mtax=mbasic*0.15
            else :
                mda=mbasic*0.40
                mhra=mbasic*0.25
                mtax=mbasic*0.10
            mgross=mbasic+mda+mhra
            mnet=mgross-mtax
            rec=(mempno,mname,mjob,mbasic,mda,mhra,mgross,mtax,mnet)
            querry="insert into "+Tablename+" values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"   
            mycursor.execute(querry,rec)
            mydb.commit()
            print("record added successfully..........")
        except :
            print("something went wrong ")

    elif choice==2:
        try :
            querry="select*from "+Tablename
            mycursor.execute(querry)
            print(tabulate(mycursor,headers=["empno","name","jon","basic salary","DA","HRA","Gross Salry","Tax","Net salary"],tablefmt='fancy_grid'))
            '''myrecords=mycursor.fetchall()
            for rec in myrecords :
                print(rec)'''
        except :
            print("something went wrong ")

    elif choice==3:
        try:
            en=input("enter employee no. of the record to be displayed ..: ")
            querry="select * from "+Tablename+" where empno ="+ en
            mycursor.execute(querry)
            myrecord=mycursor.fetchone()
            print("\n\nRecord of employee no. : "+en)
            
            ch=mycursor.rowcount
            print(100*'-')
            print('%-8s %-15s %-15s %-10s %-10s %-10s %-10s %-10s %-10s'%myrecord)
            print(100*'-')
            if ch==-1:
                print("nothing to display ")
        except :
            print("something went wrong ")

    elif choice==4:
        try:
            ch=input("do you want to delete all the records (y/n)")
            if ch.upper()=="Y":
                mycursor.execute("delete from "+ Tablename)
                mydb.commit()
                print("all the records are deleted .... ")
        except:
            print("something went wrong ")

    elif choice==5:
        try :
            en+input("enter employee no. of the record to br deleted ...")
            querry="delete from "+Tablename+" where empno="+en
            mycursor.execute(querry)
            mydb.commit()
            c=mycursor.rowcount
            if c>0:
                print("deletion done ")
            else :
                print("employee no ",en," not found ")
        except :
            print("something went wrong ")

    elif choice==6:
        try :
            en=input("enter employee no. of the record to be modified ...")
            querry="select * from "+Tablename+" where empno="+en
            mycursor.execute(querry)
            myrecord=mycursor.fetchone()
            c = mycursor.rowcount
            
            if c==-1 :
                print("empno "+en+" does not exist ")
            else :
                print("......ok..........")
                print(myrecord[3])
                mname=myrecord[1]
                print('yes')
                mjob=myrecord[2]
                mbasic=myrecord[3]
                
                print("empno    :",myrecord[0])
                print("name     :",myrecord[1])
                print("job      :",myrecord[2])
                print("basic    :",myrecord[3])
                print("DA       :",myrecord[4])
                print("HRA      :",myrecord[5])
                print("gross    :",myrecord[7])
                print("net      :",myrecord[8])
                print("-------------------------")
                print("type value to modify below or just press enter for no change ")
                x=input("enter name ")
                if len(x)>0:
                    mname=x
                x=input("enter job ")
                if len(x)>0:
                    mjob=x
                x=input('enter Basic Salary ')
                if len(x)>0:

                    mbasic=int(x)
                    
                querry="update "+Tablename+" set name ="+'"'+mname+'"'+','+"job="+'"'+mjob+'"'+','+"Basicsalary="+str(mbasic)+ " where empno="+en
                print(querry)
                mycursor.execute(querry)
                
                mydb.commit()
                print("record modified ")
        except Exception as e:
            print("error  = " , e)

    elif choice==7:
        try :
            querry="select * from "+Tablename
            mycursor.execute(querry)
            myrecords=mycursor.fetchall()
            print("\n\n\n")
            print(100*'-')
            print("employee payroll ")
            print(100*'-')
            now=datetime.datetime.now()
            print(now)
            print("current Date and Time : " , now ,end=" ")
            print(now.strftime("%y-%m-%d %H:%M:%S"))
            print()
            print(100*'-')
            print("%-8s %-15s %-15s %-10s %-10s %-10s %-10s %-10s %-10s"\
                  %("empno","name","job","Basic","DA","HRA","Gross","Tax","Net"))
            print(100*'-')
            for rec in myrecords :
                print("%-8s %-15s %-15s %-10s %-10s %-10s %-10s %-10s %-10s"%rec)#'%4d %-15s &-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f'%rec........see from yyt
            print(100*'-')
        except :
            print("something went wrong ")

    elif choice==8:
        try :
            querry="select * from "+Tablename
            mycursor.execute(querry)
            now=datetime.datetime.now()
            print("\n\n\n")
            print("-"*100)
            print("\t\t\t\tSalary Slip ")
            print(100*'-')
            print("current Date and Time :",end=" " )
            print(now.strftime("%Y=%m-%d %H:%M:%S"))
            myrecords=mycursor.fetchall()
            for rec in myrecords :
                print('%-8s %-15s %-15s %-10s %-10s %-10s %-10s %-10s %-10s'%rec) #%4d %-15s %-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f
        except :
            print("something went wrong ")

    elif choice==9:
        try :
            en=input("enter employee number whose pay slip you want retrieve : ")
            querry="select * from "+Tablename +" where empno="+en
            mycursor.execute(querry )
            now=datetime.datetime.now()
            print("\n\n\n\t\t\t\tSalary Slip ")
            print("current Date and Time :",end=" " )
            print(now.strftime("%Y=%m-%d %H:%M:%S"))
            print(tabulate(mycursor,headers=["empno","name","jon","basic salary","DA","HRA","Gross Salry","Tax","Net salary"],tablefmt="fancy_grid"))
        except exceptions as e :
            print("something went wrong ",e)


    elif choice==10 :
        break
    else :
        print("wrong choice ....")