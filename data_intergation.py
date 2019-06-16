import csv,re

def read_csv(file):
   with open(file,'rt')as f:
      data = csv.DictReader(f)
      return list(data)

location=read_csv('3451632_1367546816_OfficeLocations.csv')
services=read_csv('3451633_1242974339_OfficeServices.csv')
office=read_csv('3451634_544425036_offices.csv')

#merging data with respect to foreign key officeid
for row in services:
	for off_row in office:
		if row['OfficeID']==off_row['OfficeID']:
			row.update(off_row)
	for loc_row in location:
		if loc_row['officeID']== row['OfficeID']:
			row.update(loc_row)

merged_data = services
#writing merged_csv file


def modify_phone(phone):
    str=phone.replace(' ','')
    str=str.replace(')','')
    str=str.replace('(','')
    str=str.replace('+','')
    #print(str ,len(str))
    if True: 
       if len(str)== 8:
          str='6107'+str
       if len(str)==9:
          str='61'+str
       if len(str)==10:
          str ='61'+str
       if len(str)==11:
          str= '0'+str
       if len(str)==13:
          str= str[1:13]
       if len(str) ==12:
          first=str[:2]
          second = str[2:4]
          third = str[4:12]
          int_str= int(str)
          return '(+'+first+') '+second+' '+third
       else:
          print(str ,len(str))
          return False      
    else:
       return False

def not_ok(dict):
    phone =dict['Phone Number']
    mod_phone= modify_phone(phone)
    #print(mod_phone)
    if mod_phone != False:
       dict['Phone Number'] = mod_phone
       return dict
    else :
       return False
#cleaning data:
i=0

for row in merged_data:
    i=i+1
    new_data =not_ok(row)
    if new_data==False:
       merged_data.pop(i-1)
       print('removing ..... ',row)
    else:
       row = new_data

csv_file = 'office_service_locations.csv'
csv_columns= merged_data[0].keys()
for row in merged_data[0:30]:
	print(row.values())
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in merged_data:
            #print(row)
            writer.writerow(data)

except IOError:
    print("I/O error") 


