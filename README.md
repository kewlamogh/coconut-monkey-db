# CoconutMonkey
# A simple to use, beginner-friendly, Python persistance database.

# Gist
CoconutMonkey can be thought of as a magical dictionary - so the structure is like a dictionary:
```
key: value
```
Items will be set and added using keys.

#  How to use
## Setup
First, download the `CoconutMonkey` source file from Github [here](https://github.com/kewlamogh/coconut-monkey-db) (the central source file is `coconutmonkey.py`). I haven't published it to the PyPi yet, so you need to have the library stored in your project.

Now, you want to import `coconutmonkey`:
```py
import coconutmonkey
```
> CoconutMonkey's core revolves around `.txt` files, so you can name the database's `txt` file by typing `coconutmonkey.fileName = "file_name_here"`. You must add `".txt"` to the end. 

Next type:
```py
# you can also put the custom filename BEFORE the `init` function
# something like this:
# coconutmonkey.fileName = "newtextfile.txt"
coconutmonkey.init()
```

> Note: CoconutMonkey auto-creates the text file if it does not exist.

## Functions
### `addOrSetItem(key -> str, value -> any)`

`addOrSetItem` adds an item to the database, with the item's key as `key` and it's value is the parameter `value`. If the provided key already exists in the database, then the `value` overrides the previous value under the key `key`. 

### `deleteItem(key -> str)`
Deletes the item associated with `key` from the database. If no such item exists, then nothing happens.

### `getItem(key -> str)`
Get the item whose key is `key`, if no such item exists, it throws an `IndexError`.

### `init()`
`init` creates (if it doesn't exist already) the databases's core text file. `init` should be at the top of every `CoconutMonkey` program, regardless of the number of times the program has executed.

### `fileName`
The variable `fileName` can be changed BEFORE calling the `init` function. By default, the text file that is created is called `db.txt`, but if you edit `fileName` you can change it.

### `getKeys()`
Returns a list of all keys.

# Demo/Tutorial
A basic, persistant, phonebook program. First, we have to import the central library and do some setup:
```py
import coconutmonkey
coconutmonkey.fileName = "phonebook.txt"
coconutmonkey.init()
```
Now we need to get the necessary data to make a person in the phonebook and add that to the database.
```py
name, phoneNumber = input("Enter the name: "), input("Enter the phone number: ")

coconutmonkey.addOrSetItem(name, phoneNumber)

wannaGet = input("Do you want to get a phone number? [Y/N]").lower() == "y" 

if (wannaGet):
    try: print(coconutmonkey.getItem(input("Enter the person's name: ")))
    except: print("they don't exist")
else:
    print("ok sure")
```
> I couldn't find a way to add the `deleteItem` function into the tutorial/demo.

To find the source code for the finished demo, go to `demo/test.py` or click [here](https://github.com/kewlamogh/coconut-monkey-db/blob/main/demo/test.py).

# License:

Copyright (c) 2021 DaCool1

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
