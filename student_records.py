student1={"Name":"Raju","Class":4,"Perccentage":88.54}
student2={"Name":"Apple","Class":4,"Perccentage":33.54}
student3={"Name":"Anju","Class":4,"Perccentage":45}
student5={"Name":"Yash","Class":4,"Perccentage":82}
student6={"Name":"Soundarya","Class":4,"Perccentage":95}
student4={"Name":"Rose","Class":4,"Perccentage":54}

print(student2["Name"])
print(student3.keys())

# Adding a new key-value pair
student3["Result"]="Third Class"

# Updating an existing value
student4["Name"]="Rosey"
print("Updated an existing value of student4:",student4)

# Using del 
del student6["Name"]
print(student6)

# Using pop() 
val = student5.pop("Perccentage")
print(val)

# Using popitem()
key, val = student3.popitem()
print(f"Key: {key}, Value: {val}")

# Using clear()
student4.clear()
print(student4)


#Loop through dictionary
loop={1:'if',4:'else',3:'for',2:'while'}

for key in loop:
    print('Key:',key)
for value in loop.values():
    print('Value:',value)
for value,key in loop.items():
    print(f"{key}:{value}")

#Convert dictionary to JSON
import json
rec={
    "student1":{"Name":"Raju","Class":4,"Perccentage":88.54},
    "student2":{"Name":"Apple","Class":4,"Perccentage":33.54},
    "student3":{"Name":"Anju","Class":4,"Perccentage":45},
    "student5":{"Name":"Yash","Class":4,"Perccentage":82},
    "student6":{"Name":"Soundarya","Class":4,"Perccentage":95},
    "student4":{"Name":"Rose","Class":4,"Perccentage":54},
}
print(json.dumps(rec, indent=5))
print(json.dumps(rec, sort_keys=True))
print(json.dumps(rec, ensure_ascii=False)) 
print(json.dumps([{k: rec[k]} for k in rec]))

#saving json
out_file = open("student_records.json", "w") 
json.dump(rec, out_file, indent = 6) 
out_file.close() 
#Read JSON back into Python

with open('student_records.json', 'r') as file:
    data = json.load(file)

print(json.dumps(data, indent=4))
#formatted output
print("\n" + "-" * 50)
print(f"{'Student ID':<12} | {'Name':<12} | {'Class':<8} | {'Perccentage'}")
print("-" * 50)


for student_id, details in data.items():
    name = details["Name"]
    cls = details["Class"]
    per = details["Perccentage"]
    
    print(f"{student_id:<12} | {name:<12} | {cls:<8} | {per}%")

print("-" * 50)