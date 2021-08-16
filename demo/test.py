import coconutmonkey
coconutmonkey.fileName = "phonebook.txt"
coconutmonkey.init()

name, phoneNumber = input("Enter the name: "), input("Enter the phone number: ")

coconutmonkey.addOrSetItem(name, phoneNumber)

wannaGet = input("Do you want to get a phone number? [Y/N]").lower() == "y" 

if (wannaGet):
    try: print(coconutmonkey.getItem(input("Enter the person's name: ")))
    except: print("they don't exist")
else:
    print("ok sure")