import json

rows=[{
'id':1,
'name':'anil',
'address':'chennai',
'department':'admin'
},{
'id':2,
'name':'bala',
'address':'chennai',
'department':'admin'
},
{
'id':3,
'name':'sreeram',
'address':'chennai',
'department':'admin'
}]


with open("employeedata.json","w") as write_file:
    json.dump(rows,write_file,indent=4)
    print("data saved")
with open("employeedata.json","r") as read_file:
    emp_data=json.load(read_file)
    print(emp_data)    
    