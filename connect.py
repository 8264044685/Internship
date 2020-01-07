import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['BankDB']
# print("database are",myclient.list_database_names())
# print("collection are",mydb.list_collection_names())

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

def getAllData():
    for x in collection.find():
        print(x)
def insert_data(name,amount,withdraw,diposit):
    try:
        curs = collection.find().sort([("_id", -1)]).limit(1)
        for document in curs:
            document['_id'] = str(int(document['_id']) + 1)
        myDict = {'_id': document['_id'], 'name': name, 'amount': amount, 'withdraw': withdraw, 'diposit': diposit}
        collection.insert_one(myDict)
    except Exception as e:
        print(e)
def delete_data(id):
    myquery = {'_id': id}
    delete = collection.delete_one(myquery)
    if delete:
        print("Delete successfully")
    else:
        print("Error")

def update_data(id):
    print(id)
    name = input("Enter name")
    # myquery = {"_id": id}
    # newvalues = {"$set": {"name": name}}
    # collection.update_one(myquery,newvalues)
    collection.update_one({'_id':id},{'$set':{'name':name}})

def withdraw(id):
    money = int(input("Withdrawal amount"))
    data = collection.find_one({"_id":id})
    amount = data['amount']
    amount -= money
    collection.update_one({'_id': id}, {'$set': {'amount': amount,'withdraw':money}})
    updated_data=collection.find_one({"_id": id})
    print(updated_data)
def diposit(id):
    money = int(input("Withdrawal amount"))
    data = collection.find_one({"_id": id})
    amount = data['amount']
    amount += money
    collection.update_one({'_id': id}, {'$set': {'amount': amount, 'diposit': money}})
    updated_data = collection.find_one({"_id": id})
    print(updated_data)

choice = 1
while choice > 0:
    choice = int(input("Enter Your Choice"))
    if choice == 1:
        name = input("Enter your name")
        amount = int(input("Enter Bank balance"))
        withdraw = 0
        diposit = 0
        insert_data(name,amount,withdraw,diposit)
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

