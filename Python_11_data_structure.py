# data strucure

# list
# dictionary
# tuple 
# sets 
# frozensets

# list fruit names
listname = ["apple", "banana", "papaya"]
print(type(listname)) # <class 'list'>
listname[1] ="kiwi"
print(listname[1]) #banana


# tuples
listname = ("apple", "banana", "papaya")
print(type(listname)) # <class 'tuple'>
# listname[1] ="kiwi"
print(listname[1]) #banana
print(len(listname)) #3


# set 
setdata = {"apple", "banana", "papaya", "papaya"}
print(setdata)

# dictionary
dictdata = {
    "make": "Maruti",
    "Model" : "800",
    "year": 1990
}
print(type(dictdata))#<class 'dict'>
print(dictdata) # {'make': 'Maruti', 'Model': '800', 'year': 1990}
print(dictdata["Model"]) #800

print(len(dictdata)) #3