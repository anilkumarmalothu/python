import json

data={"hello":"gshad","hdhd":"jaghdad","jdhahd":"dhhd"}

with open("sample.json","w") as f1:
    write=json.dump(data,f1,indent=4)
with open("sample.json","r") as f1:    
    read1=json.load(f1)
print(read1)    
    
    