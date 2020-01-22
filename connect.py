import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['BankDB']
colList= mydb.list_collection_names()
collection = mydb['account']

if "account" in colList:
    print("collection already exists")
else:
    myTable = mydb['account']

print("0. Exit")
print("1. Insert")
print("2. Update")
print("3. Display")
print("4. Delete")
print("5. Withdraw")
print("6. Diposit")
print("7. MY Info")

def myInfo(id):
    print("my info----")
    data = collection.find_one({"id": id})
    print("Id :", data['id'])
    print("Id :", data['name'])
    print("Id :", data['amount'])
    print("*" * 40)

def getAllData():
    if collection.find():
        for x in collection.find():
            print("Id :",x['id'])
            print("Name :",x['name'])
            print("Amount :",x['amount'])
            print("*" * 40)
    else:
        print("Acccount not created at")

def insert_data(func,name,amount,withdraw,diposit):
    try:
        data = func(id)
        myDict = {'id': data, 'name': name, 'amount': amount, 'withdraw': withdraw, 'diposit': diposit}
        collection.insert_one(myDict)
	print("Your Id : {}, \nName    : {}, \nAmount  : {}".format(data,name,amount))
    except Exception as e:
        print(e)

def delete_data(id):
    if collection.find_one({"id": id}):
        # print("success")
        myquery = {'id': id}
        delete = collection.delete_one(myquery)
        if delete:
            print("Delete successfully")
        else:
            print("Error")

    else:
        print("Id not found")

def update_data(id):
    if collection.find_one({"id": id}):
        name = input("Enter name")
        collection.update_one({'id':id},{'$set':{'name':name}})
    else:
        print("ID account not found")

def withdraw(id):
    data_id = collection.find_one({"id": id})

    if collection.find_one({"id": id}):
        data = collection.find_one({"id": id})
        money = float(input("Withdrawal amount"))
        amount = data['amount']
        if money <= 0:
           print("Please Enter valid amount")
        elif amount >= money:
            amount -= money
            collection.update_one({'id': id}, {'$set': {'amount': amount,'withdraw':money}})
            updated_data = collection.find_one({"id": id})
            print('ID : ',updated_data['id'])
            print("Name :", updated_data['name'])
            print("Amount :",updated_data['amount'])
            print("*" * 40)
        else:
            print("\n Insufficient balance  ")

    else:
        print("Id account is not found")

def diposit(id):

    if collection.find_one({"id": id}):
        data = collection.find_one({"id": id})
        
        money = float(input("Enter an amount : "))
        amount = data['amount']
        if money <= 0:
            print("Please enter valid balance ")
        else :
            amount += money
            collection.update_one({'id': id}, {'$set': {'amount': amount, 'diposit': money}})
            data_updated = collection.find_one({"id": id})
            print('ID : ', data_updated['id'])
            print("Name :", data_updated['name'])
            print("Amount :", data_updated['amount'])
            print("*" * 40)
    else:
        print("Id account not found")

choice = 1
while choice > 0:

    choice = int(input("Enter Your Choice : "))
    if choice == 1:

        count = 0
        for total1 in collection.find():
            count += 1
        # print("count = ", count)

        def sequence(id):
            data = count

            data += 1
            return data

        name = input("Enter your name : ")
        amount = int(input("Enter Bank balance : "))
        withdraw = 0
        diposit = 0
        insert_data(sequence,name,amount,withdraw,diposit)
    elif choice == 2:
        try:

            id =float(input("Enter Id : "))
            id = round(id)
            # print("id :",type(id),id)
            update_data(id)
            getAllData()
        except Exception as e:
            print("Warning : ",error)
    elif choice == 3:
        getAllData()
    elif choice == 4:
        try:

            id = float(input("Enter Id : "))
            id = round(id)
            delete_data(id)
            getAllData()
        except Exception as error:
            print("Warning : ",error)
    elif choice == 5:
        try:
            id = int(input("Enter Id : "))
            print("---",id)
        # id = round(id)
            withdraw(id)
        except Exception as error:
            print("Warning : Please ener valid id")
    elif choice== 6:
        try:
            id = float(input("Enter Id : "))
            id = round(id)
            diposit(id)
        except Exception as error:
            print("Warning :",error)
    elif choice == 7:
        try:
            id = int(input("Enter Id : "))
            # print("---", type(id))
            # id = round(id)
            myInfo(id)
        except Exception as error:
            print("Warning : Please ener valid id")
            print(str(error))
    elif choice == 0:
        break
    else:
        print("Plese Enter valid choice")
else:
    print("Invalid input")
