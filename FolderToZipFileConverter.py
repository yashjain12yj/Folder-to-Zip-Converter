import os
import shutil
# Open a file
path = input("Enter the path of the folder : ")
folder_name=input("Enter the folder name : ")
os.chdir(path)
if os.path.isdir(folder_name):
	#If the selected file is a folder
	print("Creating...")
	shutil.make_archive(folder_name, "zip", folder_name)
	#(Jis naam se banega, type , jiska banana hai)
	print("Zip file Created!!")
else:
	print(folder_name+" is not a folder, hence it can not be zipped.")
