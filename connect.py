import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['BankDB']
# print("database are",myclient.list_database_names())
# print("collection are",mydb.list_collection_names())
# paras
colList= mydb.list_collection_names()


collection = mydb['account']

#Count number of record in collection
total= collection.count()
print("toal record is :" ,total)
#Function for increment 1 value in id column in collection
def sequence(id):
    data=total
    data += 1
    return data
#end of increment function


#Check colletion name 'account' is exists or not
if "account" in colList:
    print("collection already exists")
else:
    myTable = mydb['account']

# Display diferent message in promt
print("0. Exit")
print("1. Insert")
print("2. Update")
print("3. Display")
print("4. Delete")
print("5. Withdraw")
print("6. Diposit")

# Function for fetch all the record from 'account' collection
def getAllData():
    for x in collection.find():

        print(x)

# Function for insert data into 'account' collection
def insert_data(func,name,amount,withdraw,diposit):
    try:
        data = func(id)
        # curs = collection.find().sort([("id", -1)]).limit(1)
        # print("curs :",curs)
        # for document in curs:
        #     print("doc :",document)
        #     document['id'] = str(int(document['id']) + 1)
        #     print("id : ",document['id'])
        myDict = {'id': data, 'name': name, 'amount': amount, 'withdraw': withdraw, 'diposit': diposit}
        collection.insert_one(myDict)
    except Exception as e:
        print(e)

# Function for Delete record
def delete_data(id):
    myquery = {'id': id}
    delete = collection.delete_one(myquery)
    if delete:
        print("Delete successfully")
    else:
        print("Error")

# Function for Update record
def update_data(id):
    print(id)
    name = input("Enter name")
    # myquery = {"id": id}
    # newvalues = {"$set": {"name": name}}
    # collection.update_one(myquery,newvalues)
    collection.update_one({'id':id},{'$set':{'name':name}})


# Function for withdrawl money
def withdraw(id):
    money = int(input("Withdrawal amount"))
    data = collection.find_one({"id":id})
    amount = data['amount']
    amount -= money
    collection.update_one({'id': id}, {'$set': {'amount': amount,'withdraw':money}})
    updated_data=collection.find_one({"id": id})
    print(updated_data)

# Funtion for diposit money
def diposit(id):
    money = int(input("Withdrawal amount"))
    data = collection.find_one({"id": id})
    amount = data['amount']
    amount += money
    collection.update_one({'id': id}, {'$set': {'amount': amount, 'diposit': money}})
    updated_data = collection.find_one({"id": id})
    print(updated_data)

# Code for different choices. It's break when user enter zero.
choice = 1
while choice > 0:
    choice = int(input("Enter Your Choice"))
    if choice == 1:

        name = input("Enter your name")
        amount = int(input("Enter Bank balance"))
        withdraw = 0
        diposit = 0
        insert_data(sequence,name,amount,withdraw,diposit)
    elif choice == 2:
        id = int(input("Enter Id"))
        update_data(id)
        getAllData()
    elif choice == 3:
        getAllData()
    elif choice == 4:
        id = int(input("Enter a customer id To delete record"))
        delete_data(id)
        getAllData()
    elif choice == 5:
        id = int(input("Enter a customer id withdrawal amount : "))
        withdraw(id)
    elif choice== 6:
        id = int(input("Enter a customer id withdrawal amount : "))
        diposit(id)
    elif choice == 0:
        break
    else:
        print("Plese Enter valid choice")
else:
    print("Invalid input")

