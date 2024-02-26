from Profile import *
from ds_client import send

profile = Profile()
profile.load_profile("/Users/nicolekwan/Workspace/journal.dsu")
server = "168.235.86.101"
while True:
    msg = input("Enter msg: ")

    args = msg.split()
    new_post = args[::]

    message = (" ").join(new_post)
    print(profile.username)
    print(profile.password)
    print(message)


    if profile.dsuserver == "":
        server = input("Enter server name: ")

    send(server, 3021, profile.username, profile.password, message)