
import json
import os.path

#returns contents of JSON file
def getFromJSON(filePathName):
	with open(filePathName,'r') as fp:
		return json.load(fp)

#returns dictionary of userID if existing
def inJSON(filePathName, userID):
	
	#checks if file exist
	if(os.path.isfile(filePathName)):
		data = getFromJSON(filePathName)
	else:
		return

	#checks if user exists
	if(userID in data):
		return data.get(userID);
	else:
		return
	
	
	
	
path = '../../'
fileName = 'PantryUsers'

#parameters for function
filePathName = path + '/' + fileName + '.json'
userID = 'McNug001'

userData = inJSON(filePathName, userID)

#checks if empty
if (userData):
	print (userData["firstName"])
	print (userData["userSS"])
	print (userData["userNumber"])
else:
	print("Unable to find person")



userID = 'Block011'

userData = inJSON(filePathName, userID)

#checks if empty
if (userData):
	print (userData["firstName"])
	print (userData["userSS"])
	print (userData["userNumber"])
else:
	print("Unable to find person")



#non-existing user
userID = 'Empty404'

userData = inJSON(filePathName, userID)

#checks if empty
if (userData):
	print (userData["firstName"])
	print (userData["userSS"])
	print (userData["userNumber"])
else:
	print("Unable to find ", userID)





