import os


def rename_files():
	#Get file names from a folder

	file_list = os.listdir("./prank")
        # print(file_list)
        saved_path = os.getcwd()
    # saved_path = os.getcwd()
        print("Current Working Directory is"+saved_path)
        os.chdir("./prank")	
     
    #for each file, rename filename


        for file_name in file_list:
    #	print ("Old Name - "+file_name)
    #	print ("New Name -"+file_name.translate(None,"0123456789"))
            os.rename(file_name, file_name.translate(None,'0123456789'))


        os.chdir(saved_path)
rename_files()
