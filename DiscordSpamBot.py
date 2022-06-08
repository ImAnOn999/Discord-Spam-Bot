import requests#References "requests" module, we need this to send fake http requests to discord servers
import time#References "time" module, we need this for the timer/delay

authorizationCodes = ["OTc5Mzk4NDIwNTYzMzY1OTkw.G7dloB.DLzf_1oW-2LZFJEAJGG7-62jifkan95qKDkoQQ"]#Creates array of authorization codes, these are needed to send fake http requests
spamMessages = ["test"]#Creates array of spam messages

currentId = 0#Sets the currentId to 0, this id will be used as an index to find the authorization code to be used in a request from the array authorizationCodes
currentMessage = 0#Sets the currentMessage to 0, this id will be used as an index to find the payload(message) to be used in a request from the array spamMessages

header = {#"header" is one of the data that is sent during an http request, we create a dictionary to store the header data we want sent during the request
    'authorization': authorizationCodes[0]#Defines the "authorization" element of the header as the first element from the authorizationCodes array
}

payload = {#"payload" is another data that is sent during an http request, we use another dictionary to store the payload data we want
    'content': spamMessages[0]#Defines the "content" element of the header as the first element from the spamMessages array
}

id = int(input("Insert id of channel or user you want to spam: "))#Gets integer input for ID of channel/user to attack (discord uses this format https://discord.com/channels/(@me for DMs or serverId for server attacks)/(channelId))
timer = int(input("Insert time until attack (In Seconds): "))#Gets integer input for time until attack occurs
messages = int(input("Insert number of messages you want to send: "))#Gets integer input for number of messages the user wants to send, this script will repeat sending fake http requests until we reach that number
delay = float(input("Insert delay between messages (In Seconds): "))#Gets float input for delay between requests (Usually between 5 seconds and 2 minutes), using multiple accounts will allow you to set a lower delay

input("Press ENTER to begin")#As soon as user presses "ENTER", everything below will run

def changeId(currentId, authorizationCodes, currentMessage, spamMessages):#Defines a function to change the authorization code, requires these parameters
    currentId += 1#Adds 1 to the currentId
    if currentId >= len(authorizationCodes):#Checks if the currentId is past the number of ids in the array
        currentId = 0#If it is, resets the currentId at 0
        changeMessage(currentMessage, spamMessages)#Fires function to change the message with the currentMessage and the array of spamMessages as parameters
    header["authorization"] = authorizationCodes[currentId]#Sets the authorization code that will be used when firing a request to the item from the array authorizationCodes with the index of the currentId

def changeMessage(currentMessage, spamMessages):#Defines a function to change the current message, requires these parameters
    currentMessage += 1#Adds 1 to the currentMessage
    if currentMessage >= len(spamMessages):#Checks if the currentMessage is past the number of messages in the array
        currentMessage = 0#If it is, resets the currentMessage at 0
    payload["content"] = spamMessages[currentMessage]#Sets the message that will be used when firing a request to the item from the array spamMessages with index of currentMessage

while timer > 0:#While the timer is greater than 0, it will continue firing this function
    print("T-" + str(timer))#Prints the time remaining until the attack
    timer -= 1#Subtracts 1 from the timer
    time.sleep(1)#Waits for 1 second before continuing

while messages > 0:#While the messages remaining are greater than 0, it will continue firing this function
    changeId(currentId, authorizationCodes, currentMessage, spamMessages)#Fires the changeId function every time
    requests.post('https://discord.com/api/v9/channels/' + str(id) + '/messages', headers = header, data = payload)#Sends the fake http request to discord
    messages -= 1#Subtracts 1 from the remaining messages to be sent 
    time.sleep(delay)#Waits for the delay set by the user

print("Command Executed")#Prints "Command Executed" to the console once there are no messages remaining
