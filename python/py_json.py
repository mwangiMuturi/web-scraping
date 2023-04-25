# parseing json into a python dictionary
# module called json
import json

# sample json
userJson='{"fname":"John","sname":"Doe","age":31}'

# parse to a dictionary
user=json.loads(userJson) 
print(user)

# parse a dictionary into json
car={'make':'ford','model':'mustang','year':1970}
myFile=open('myFile.txt','w')
dic={}
carJson=json.dump(car,fp=dic)
print(dic)