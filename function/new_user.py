from common.database import Database

Database.initialize()
user = Database.find_one('users', {"Name": "Jack"})

print(user)
