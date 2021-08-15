import coconutmonkey

coconutmonkey.init()

name = input("Enter name")
new = input(f"Hello {name}! Are you new? ") == "Y"

if new:
    n, pn = input("Enter your name: "), input("Enter your phone number: ") 
    coconutmonkey.addOrSetItem(key = n, item = pn)
    print('Added!')
else:
    try:
        print(coconutmonkey.getItem(name))
    except:
        print("Looks like you are new!")
