import requests
import time

authorizationCodes = [""]#Add authorization codes for accounts you want to use here
spamMessages = [""]#Add messages you want to send here

id = input("Insert id of channel or user you want to spam: ")
timer = int(input("Insert time until attack (In Seconds): "))
messages = int(input("Insert number of messages you want to send: "))
delay = float(input("Insert delay between messages (In Seconds): "))

input("Press ENTER to begin")

while messages > 0:
    for message in spamMessages:
        payload = {
            'content': message
        }
        for code in authorizationCodes:
            header = {
                'authorization': code
            }
            requests.post('https://discord.com/api/v9/channels/' + id + '/messages', headers = header, data = payload)
        messages -= 1
    time.sleep(delay)

print("Command Executed")
