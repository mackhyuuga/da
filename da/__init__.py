import os 
import sys 
import json
from tabnanny import filename_only 
import pathvalidate


def __join_the_words():
    pass 

        
def current_dir():
    return os.getcwd()

def change_to_a_directory(new_directory):
    os.chdir(new_directory)


def create_folders(folders, base_directory = ""):
    """This function is responsible to create the folders

    Args:
        folders (list): name of the folders 
        base_directory (str, optional): name of the directory 
        from which the actions will take place. Defaults to "".
    """

    base_directory = pathvalidate.sanitize_filename(base_directory)
    
    if not isinstance(folders, list):
        folders = (folders, "")

    for folder in folders:
        folder_name = os.path.join(base_directory, folder)
        try:
            os.mkdir(folder_name, mode=0o777)
        except:
            pass

def rename_folder():
    pass

def move_file():
    pass 

def copy_file():
    pass



class File():
    def __init__(self, file_name, extension = "txt", path = ""):
        self.file_name = file_name
        self.extension = extension
        self.full_file_name = self.file_name + "." + self.extension
        self.path = path


    def create(self, content = None):
        with open(os.path.join(self.path, self.full_file_name), "w+") as file:
            if content != None:
                file.write(content)
            file.close
            

    def rename_file(self, new_name, extension = None):
        self.extension = self.extension if extension == None else extension
        os.rename(self.full_file_name, new_name + '.' + self.extension)


    def rename_for_standard(self):
        new_name = self.file_name.replace(' ', '_')
        os.rename(self.full_file_name, new_name + '.' + self.extension)
        

    def write(self, content):
        with open(os.path.join(self.path, self.full_file_name), "a+") as file:
            file.write(content)
            file.close
    
    def get_content(self, format = "default", referential = (0,0)):
        with open(os.path.join(self.path, self.full_file_name), "r") as file:
            file.seek(referential[0], referential[1])
            if format == "default":
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


    def delete_file(self):
        os.remove(os.path.join(self.path, self.full_file_name))



if __name__ == "__main__":
    f = File("abc","txt")
    f.create("allison asd\nEduardo")
    f.write("\nbonfim")
    print(f.get_content("line_by_line"))
    f.delete_file()
