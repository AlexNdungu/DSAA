# Create a data structure that can store 100mil users. You can also insert, update and search the list

class User:
    #Add a constructor methos 
    def __init__(self, username,name,email):
        
        #Create the attributes
        self.username = username
        self.name = name
        self.email = email
        #print('User Created')

#Also we want create a CRUD fuctionality

class UserDataBase:

    def __init__(self):
        self.users = []

    def insert(self,user):
        
        i = 0

        while i < len(self.users):

            if self.users[i].username > user.username:

                break
            i+=1

        self.users.insert(i, user)

    def find(self,username):
        
        for user in self.users:

            if user.username == username:

                return user

    def update(self,user):
        
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users 

#Now we create a new object
alex = User('theAlex','Alex','alex@gmail.com')
meta = User('theMehta','Meta','meta@gmail.com')
ndungu = User('theNdungu','Wilson Ndungu','wilson@gmail.com')
joyce = User('theJoyce','Joyce Waruguru','joyce@gmail.com')
muniu = User('theMuniu','Karuga Muniu','muniu@gmail.com')

#Now we store the users
users = [alex,meta,ndungu,joyce,muniu]

#instanciate database
database = UserDataBase()

#Insert to database
database.insert(alex)
database.insert(meta)
database.insert(ndungu)

#Find a user
user = database.find('theAlex')
#print(user.name)

#Now we update data
database.update(User(username='theAlex', name='Nie Meta', email='alexM@gmail.com'))

user = database.find('theAlex')
#print(user.name)

#List
database.list_all()


#Lets create key value pair tree using the users data
from keyValue import BSTNode, insert, find, update

# tree = BSTNode(joyce.username, joyce)

# print(tree.key, tree.value)

# # Lets go to the left side
# tree.left = BSTNode(alex.username, alex)
# tree.left.parent = tree
# tree.right = BSTNode(muniu.username, muniu)
# tree.right.parent = tree

# Lest use the insert fuction

#Since there is no existing tree, use None for the variable node
tree = insert(None, joyce.username, joyce)

# insert the rest
insert(tree, alex.username, alex)
insert(tree, meta.username,meta)
insert(tree, ndungu.username, ndungu)
insert(tree, muniu.username, muniu)

#Lets find elements
find_value = find(tree, 'theAlex')

print(find_value.value.email)

#Now lets update the key

update(tree, 'theAlex', User('theAlex','new alex','newalex@gmail.com'))

find_value = find(tree, 'theAlex')

print(find_value.value.email)