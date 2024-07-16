file = open("myFile.txt","a")
data = "\n{'data':'Ujjwal Srivastava','marks':{'EN':20,'MTS':30}}"
print(f"Lets Write : {len(data)}")
file.write(data)
file.close()
file = open("myFile.txt","r")
lst = file.readlines()
# print(lst)
# for i in lst:
#     print(i)
file.close()
