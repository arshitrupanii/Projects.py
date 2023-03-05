import os

print("Please Enter after path this '\\' ")
path = input("Enter your PC path --> ")
ext = input("Enter extension Ex.. .jpg, .py, .png  ")
path= path.replace('\\','/')

def rename():
    i = 1
    for files in os.listdir(path):
        new_file = path + str(i) + ext
        old_file = path + files
        os.rename(old_file,new_file)
        i+=1

rename()