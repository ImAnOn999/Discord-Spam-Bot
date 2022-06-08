import requests
import time

authorizationCodes = [""]#Add authorization codes for accounts you want to use here
spamMessages = [""]#Add messages you want to send here

currentId = 0
currentMessage = 0
messagesSent = 0

header = {
    'authorization': authorizationCodes[0]
}

payload = {
    'content': spamMessages[0]
}

id = input("Insert id of channel or user you want to spam: ")
timer = int(input("Insert time until attack (In Seconds): "))
messages = int(input("Insert number of messages you want to send: "))
delay = float(input("Insert delay between messages (In Seconds): "))

input("Press ENTER to begin")

def changeId(currentId, authorizationCodes, currentMessage, spamMessages):
    currentId += 1
    if currentId >= len(authorizationCodes):
        currentId = 0
        changeMessage(currentMessage, spamMessages)
    header["authorization"] = authorizationCodes[currentId]

def changeMessage(currentMessage, spamMessages):
    currentMessage += 1
    if currentMessage >= len(spamMessages):
        currentMessage = 0
    payload["content"] = spamMessages[currentMessage]

while timer > 0:
    print("T-" + str(timer))
    timer -= 1
    time.sleep(1)

while messages > 0:
    changeId(currentId, authorizationCodes, currentMessage, spamMessages)
    requests.post('https://discord.com/api/v9/channels/' + id + '/messages', headers = header, data = payload)
    messages -= 1
    time.sleep(delay)

print("Command Executed")
