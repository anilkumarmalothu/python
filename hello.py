import csv


header=["name","roll","class"]
rows=[
    ["anil","10","6"],
    ["sreeram","7","6"],
    ["shobidh","8","6"]
]
with open("hello.csv","w",encoding="UTF8")as f1:
    writer=csv.writer(f1)
    writer.writerow(header)
    writer.writerows(rows)
print("data saved")    