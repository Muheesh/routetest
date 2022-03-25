import sqlite3
from prettytable import PrettyTable
data = sqlite3.connect("routes.db")
table = data.execute("select name from sqlite_master where type='table' and name='flight'").fetchall()
if table!=[]:
    print("Table already created.")
else:
    data.execute('''create table flight(
                        airline text,
                        price integer,
                        time integer,
                        destination text);''')
print("Table created")

while True:
        print("1.Add Route")
        print("2.View all route")
        print("3.View cheapest flight")
        print("4.Search destination")
        print("5.View Costliest flight")
        print("6.Exit")

        a = int(input("Enter the choice to be executed"))

        if a==1:
            getAir = input("Enter the airline name:")
            getPrice = input("Enter the price:")
            getTime = input("Enter the time:")
            getDes = input("Enter the destination:")
            data.execute("insert into flight(airline,price,time,destination)values('"+getAir+"',"+getPrice+","+getTime+",'"+getDes+"')")
            data.commit()
            print("route added")
        elif a==2:
            result=data.execute("select * from flight")
            table = PrettyTable(["Airlinename","Price","Time","Destination"])
            for i in result:
                print(i[0],i[1],i[2],i[3])
        elif a==3:
            result=data.execute("select max(price) as price from flight")
            for i in result:
                print("Price",i[0])
        elif a==4:
            getDes=input("Enter the destination:")
            result=data.execute("select * from flight where destination like '"+getDes+"%'")
            for i in result:
                print("Destination",i[0])
        elif a==5:
            result=data.execute("select max(price) as price from flight")
            for i in result:
                print("Flight:",i[0])
        elif a==6:
            print("Exited")
            break
        else:
            print("Invalid selection")

