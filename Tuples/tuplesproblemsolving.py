# convert dictionary into json format
# dumps method converts python data into json format
import json
Student_data={"name":"David","age":13,"marks":87}
print(type(Student_data))
data=json.dumps(Student_data)
print(data)
print(type(data))

# acces value of age from the data
# loads converts into python object
Student_data='{"name":"David","age":13,"marks":87}'
data=json.loads(Student_data)
print(data["age"])

# pretty print following JSON data.

Student_data={"name":"David","age":13,"marks":87}
data=json.dumps(Student_data,indent=4,separators=(",","="))
print(data)

# sort the following json keys and write them into a file
Student_data={"name":"David","age":13,"marks":87}
f=open("demo.json","w")
data=json.dumps(Student_data,indent=4,sort_keys=True)
f.write(data)
print("data has been added to the file")

#access the nested key marks from the following nested data
Student_data="""{"student":
{"grade":
{"name":"David","age":13,"marks":87}
}
}"""
data=json.loads(Student_data)
print(data["student"]["grade"]["marks"])



