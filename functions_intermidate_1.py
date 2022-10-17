#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
#Change the last_name of the first student from 'Jordan' to 'Bryant'
#In the sports_directory, change 'Messi' to 'Andres'
#Change the value 20 in z to 30



x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def change(x):
    x = [ [5,2,3], [10,8,9]]
    x[1][0] = 15
    return x
print(change(x))

def change(dictionary):
    students = [
     {'first_name':  'Michael',
    'last_name' : 'Jordan'},
     {'first_name' : 'John', 
     'last_name' : 'Rosales'}
     ]
    students[0]['last_name']='Brian'
    return students
print(change(students))

def changesoccer(dict):
    sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']}
    sports_directory['soccer'][0]='Andres'
    return sports_directory

print(changesoccer(dict))

def changevalue(z):
    z = [ {'x': 10, 'y': 20} ]
    z[0]['y']=30 
    return z
print(changevalue(z))

#Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

def iterateDictionary(students):
    students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}]
    for i in range(len(students)):
        print('first name -', students[i]['first_name'] , 'last name -' , students[i]['last_name'])

iterateDictionary(students)

#Get Values From a List of Dictionaries
def iterateDictionary2(students):
    students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}]
    for i in range(len(students)):
        print(students[i]['first_name'])
iterateDictionary2(students)

def iterateDictionary2(students):
    students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}]
    for i in range(len(students)):
        print(students[i]['last_name'])
iterateDictionary2(students)

#Iterate Through a Dictionary with List Values

def printInfo():
    dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
   }
    print(len(dojo['locations']), "Locations")
    for location in dojo['locations']:
        print(location)
    print(len(dojo['instructors']), "Instructors")
    for location in dojo['instructors']:
        print(location)

printInfo()



    