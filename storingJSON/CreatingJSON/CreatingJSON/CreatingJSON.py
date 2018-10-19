

import json
import os.path


#returns contents of JSON file
def getFromJSON(filePathName):
	with open(filePathName, 'r') as fp:
		return json.load(fp)


#inserts User to JSON file
def bumpToJSON( path, fileName, newUser):

	filePathName = path + '/' + fileName + '.json'

	if (os.path.isfile(filePathName)):
		oldData = getFromJSON(filePathName)
	else:
		oldData = {}
	#grabs data if file exists

	updatedData = {**oldData, **newUser}
	#combines data

	with open(filePathName, 'w') as fp:
		json.dump(updatedData,fp)
		#updates data in file

	return;

#Takes data and created dictionary
def insertData(userID, userName, userSS, userNumber):
	path = '../../'
	fileName = 'PantryUsers'
	#These are default filenames and directories
	#Can be changed if code gets more complex

	data = {}
	data['firstName'] = userName
	data['userSS'] = userSS
	data['userNumber'] = userNumber
	#dictionary of data for the User
	User = {}
	User[userID] = data
	#Key to find user

	bumpToJSON(path, fileName, User)



#MAIN////

userID = 'Block011'
name = 'Alex'
userSS = '617 77 5485'
number = '9518378334'
insertData(userID, name,userSS, number)

userID = 'McNug001'
name = 'Juestro'
userSS = '616 44 8241'
number = '6194485854'
insertData(userID, name,userSS, number)

userID = 'Smith140'
name = 'Matt'
userSS = '448 92 4215'
number = '7601145467'
insertData(userID, name,userSS, number)

userID = 'arang008'
name = 'Crasher'
userSS = '487 74 7495'
number = '9093768481'
insertData(userID, name,userSS, number)


