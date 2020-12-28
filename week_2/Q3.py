
import requests
base_link = requests.get("https://directory.ntschools.net/api/System/GetAllSchools")
print(base_link.content)

import json
import csv
parse_data = json.loads(base_link.content)
parse_data

api_link = "https://directory.ntschools.net/api/System/GetSchool?itSchoolCode="

school_code = []
for i in parse_data:
    school_code.append(i["itSchoolCode"])    

nested_list = []

for i in range(50):
    school_data = requests.get(api_link + school_code[i])
    data = json.loads(school_data.content)

    single_sch_data = []

    single_sch_data.append(data['name'])
    single_sch_data.append(data['physicalAddress']['displayAddress'])
    single_sch_data.append(data['schoolManagement'][0]['firstName'] + data['schoolManagement'][0]['lastName'])
    single_sch_data.append(data['schoolManagement'][0]['position'])
    single_sch_data.append(data['schoolManagement'][0]['email'])
    single_sch_data.append(data['telephoneNumber'])
    nested_list.append(single_sch_data)


with open("school_data.csv", "w") as file:
    file_writer = csv.writer(file, delimiter=',')

    head_list = ["Name", "Address", "Principal/Admin Name", "Principal/Admin Position", "Principal/Admin E-mail", "TelePhone"]
    file_writer.writerow(head_list)

    for i in range(len(nested_list)):
        file_writer.writerow(nested_list[i])




