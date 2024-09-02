def find_v():
   
        var=int(input("enter the value:"))
        match var:
            case 1: return "good"
            case 2:return "average"
            case 3:return "bad"
            case _:return "invalid"
print(find_v())