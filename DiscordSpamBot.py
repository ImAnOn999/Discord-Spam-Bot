import requests
import time

authorizationCodes = ["MTAwNjM0Mzc3Mjg1NjEzNTgyMg.GiDOnk.SDu7DJ0flOLKxCrfrtdo-4Z3pf_BXgPIZmn1tY","OTc5Mzk4NDIwNTYzMzY1OTkw.G96Yrp.IHHTdRy8aSCPpYvA6FPlc4_PnpemFiHP2hZr-M"]#Add authorization codes for accounts you want to use here
spamMessages = ["test","test2"]#Add messages you want to send here

messagesSent = 0

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
