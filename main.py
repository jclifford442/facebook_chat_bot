#!/usr/bin/python

from fbchat import Client
from fbchat.models import *
import fbchat

#cli object used to log-in password is stored in file
file1 = open("C:\\Users\\John\\Desktop\\FILE_NAME_HERE", "r")
password = file1.read()
cli = Client('FACEBOOK_EMAIL_LOG-IN', password)

#searches for top 5 people named x
person = str(input("Enter the person's name"))
friends = cli.searchForUsers(person, 5)
print ("Everyone named " + str(person) + ":" + str(friends))

#Identifies the first search result and stores User ID
user1 = friends[0]
uiid = user1.uid

#Prints UserID, Name and Boolean T or F if they are a friend
print(user1.name)
print(user1.uid)
print("Is this user my friend? " + str(user1.is_friend))

#Displays last 20 messages between you and that user1
messages = cli.fetchThreadMessages(user1.uid, 20)
messages.reverse()
for msg in messages:
    print (msg)

#Sends the person a message
cli.send(fbchat.models.Message("Hi " + str(person) + " This message was sent by a bot that I made"), uiid)

#Log you out and confirms that you logged out
res = cli.logout()
if res:
    print("Logged out success")
else:
    print("Error in logging out")
