import csv

header=['id','name','address','department']
data=[
    ['E001','surithika','chennai','it'],
    ['E002','anil','chennai','admin'],
    ['E003','sreeram','chennai','hr'],
]
with open('employee_details.csv','w',encoding='utf8',newline='')as f:
    writer=csv.writer(f)
    
    writer.writerow(header)
    
    writer.writerows(data)
    
    print("data saved")