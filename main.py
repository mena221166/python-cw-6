person={
    "name":'mena',
    "age":17,
    "hobbies":['drawing','writing','swimming','coding']
}
print(person['name'])
print(person['age'])

person['age']=18
person['country']='japan'
print(person)
print(len(person['hobbies']))
person["hobbies"].append('gaming')
print(person)
def check_hobbies(person):
    if len(person['hobbies'])>=3:
        print("wow you are amazing")
check_hobbies(person)