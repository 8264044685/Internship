import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['BankDB']
# print("database are",myclient.list_database_names())
# print("collection are",mydb.list_collection_names())

colList= mydb.list_collection_names()
collection = mydb['account']

#Function for increment 1 value in id column in collection
count = 0
for total1 in collection.find():
    count +=1


def sequence(id):
    data=count

    data +=1
    return data


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
        print("Id :",x['id'])
        print("Name :",x['name'])
        print("Amount :",x['amount'])
        print("*" * 40)



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
    id1 = collection.find_one({"id": id})
    if id == id1['id']:

        myquery = {'id': id}
        delete = collection.delete_one(myquery)
        if delete:
            print("Delete successfully")
        else:
            print("Error")
    else:
        print("Id not found")

# Function for Update record
def update_data(id):
    # print("update id is ",id)
    id1 = collection.find_one({"id": id})
    # print("find id is :",id1['id'])
    if id == id1['id']:
        name = input("Enter name")
        # myquery = {"id": id}
        # newvalues = {"$set": {"name": name}}
        # collection.update_one(myquery,newvalues)
        collection.update_one({'id':id},{'$set':{'name':name}})
    else:
        print("ID account not found")

# Function for withdrawl money
def withdraw(id):

    data = collection.find_one({"id":id})
    if data == id:
        money = int(input("Withdrawal amount"))
        amount = data['amount']
        if money <= 0:
           print("Please Enter valid amount")
        elif amount >= money:
            updated_data = collection.find_one({"id": id})
            amount -= money
            collection.update_one({'id': id}, {'$set': {'amount': amount,'withdraw':money}})
            print('ID : ',updated_data['id'])
            print("Name :", updated_data['name'])
            print("Amount :",updated_data['amount'])
            print("*" * 40)
        else:
            print("\n Insufficient balance  ")
    else:
        print("Id account is not found")
# Funtion for diposit money
def diposit(id):
    updated_data = collection.find_one({"id": id})

    if update_data == id:

        money = int(input("Enter an amount : "))

        data = collection.find_one({"id": id})
        amount = data['amount']
        if money <= 0:
            print("Please enter valid balance ")
        else :
            amount += money
            collection.update_one({'id': id}, {'$set': {'amount': amount, 'diposit': money}})

            print('ID : ', updated_data['id'])
            print("Name :", updated_data['name'])
            print("Amount :", updated_data['amount'])
            print("*" * 40)
    else:
        print("Id account not found")

# Code for different choices. It's break when user enter zero.
choice = 1
while choice > 0:
    choice = int(input("Enter Your Choice : "))
    if choice == 1:

        name = input("Enter your name : ")
        amount = int(input("Enter Bank balance : "))
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
        id = int(input("Enter a customer id :"))
        delete_data(id)
        getAllData()
    elif choice == 5:
        id = int(input("Enter a customer id : "))
        withdraw(id)
    elif choice== 6:
        id = int(input("Enter a customer id  : "))
        diposit(id)
    elif choice == 0:
        break
    else:
        print("Plese Enter valid choice")
else:
    print("Invalid input")

