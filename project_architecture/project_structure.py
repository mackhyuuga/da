import os 
import sys 
import json
from tabnanny import filename_only 
import pathvalidate

class Architecture():
    def __init__(self, base_directory = "") -> None:
        self.base_directory = base_directory
        
    @staticmethod
    def current_dir():
        return os.getcwd()

    @staticmethod
    def change_dir(new_directory):
        os.chdir(new_directory)


    def create_folders(self, folders):
        """This function is responsible to create the folders

        Args:
            folders (list): name of the folders 
            base_directory (str, optional): name of the directory 
            from which the actions will take place. Defaults to "".
        """
        self.base_directory = pathvalidate.sanitize_filename(self.base_directory)

        for folder in folders:
            folder_name = os.path.join(self.base_directory, folder)
            try:
                os.makedirs(folder_name, mode=0o777)
            except:
                pass

    def move_file():
        pass 

    def copy_file():
            pass




class File(Architecture):
    def __init__(self, file_mame, path = ""):
        self.file_mame = file_mame
        self.path = path

    def create(self, content = None):
        file = open(os.path.join(self.path, self.file_mame), "w+")
        if content != None:
            file.write(content)
        file.close
    
    def get_content(self, format = "standard"):
        file = open(os.path.join(self.path, self.file_mame), "r")
        file.seek(0,0)
        if format == "standard":
            file_content = file.read()
            return file_content
        
        elif format == "line_by_line":
            file_content_list = file.readlines()
            file_content_dictionary = {}
            for i in range(1, len(file_content_list)+1):
                if i < len(file_content_list):
                    file_content_dictionary[i] = file_content_list[i-1][:-1]
                else:
                    file_content_dictionary[i] = file_content_list[i-1]
            file.close
            return file_content_dictionary
        file.close



f = File("abc.txt")
# f.create("allison asd\nEduardo")
print(f.get_content("line_by_line"))