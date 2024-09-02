import csv
import json


data_dic={}

with open("employee_details.csv","r",encoding="UTF_8") as csv_filehandler:
    csv_reader=csv.DictReader(csv_filehandler)
      
    for rows in csv_reader:
        keys=rows['id']
        data_dic[keys]=rows
        
with open("data.json","w",encoding="UTF_8") as json_f:
    json_f.write(json.dumps(data_dic,indent=4))
    print("it is converted") 
  
        
    

           
            
    
