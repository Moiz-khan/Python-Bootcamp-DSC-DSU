import os

#input from user
folder_path = input()
os.chdir(folder_path)
files_list = os.listdir(folder_path)
files_data = []

#storing files name and sizes in list
for i in range(len(files_list)):
    files_stat = os.stat(files_list[i])
    files = [files_list[i], files_stat.st_size/1024*2]
    files_data.append(files)

#bubble sort
for i in range(0,len(files_data)-1):
        for j in range(0,len(files_data)-i-1):
            if files_data[j][1] < files_data[j+1][1]:
                files_data[j], files_data[j+1] = files_data[j+1], files_data[j]
                
print('\n',files_data)