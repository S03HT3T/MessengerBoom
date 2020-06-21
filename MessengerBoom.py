import fbchat
from fbchat import Client
from fbchat.models import*

Purple="\033[0;35m"
c = "\033[036m"
Red="\033[0;31m"
BBlue="\033[1;34m"
Green="\033[0;32m"

print("""
	{}##############################
	#      Messenger Boom :v     #
	#         version 1.0        #
	#                            #
	#                By SO3HT3T  #
	##############################{}
""".format(Purple,Green))

print("\nPlease Login Your account first.Thank You.\n")
user = input("{}Enter Your Gmail or Phonenumber : {}".format(c,Green))
password = input("{}Enter Your Password : {}".format(c,Green))

client = Client(user,password)

target = input("{}\nEnter Your Target Name : {}".format(c,Green))
info = client.searchForUsers(target)
info = info[0]
print("{}\nTarget : ".format(Red),info.url,"\n")

target = info.uid
message = input("{}Enter Your Message : {}".format(c,Green))
a = int(input("{}Numbers of Message : {}".format(c,Green)))

for i in range(a):
	client.send(fbchat.models.Message(message),target)

print("{}\nDone!   Thanks for using My Tool!\nGood Bye.".format(BBlue))