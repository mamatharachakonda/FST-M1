import pandas
from pandas import ExcelFile
from pandas import ExcelWriter
data={
    "FirstName":["Mamatha","RUthwika","prakash"],
    "LastName":["rach","nara","Rath"],
    "Email":["satshah@example.com","avinashk@example.com","lahri.rath@example.com"],
    "PhoneNumber":[4537829158,5892184058,4528727830]
}
dt=pandas.DataFrame(data)
writer=ExcelWriter('User.xlsx')
dt.to_excel(writer,'Sheet1',index=False)
writer.save()