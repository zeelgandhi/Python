import os

"""
/abc/ad/file.txt
\hi\this\is\a\file.txt

open("\hi\this\is\a\file.txt").read()

open("/abc/ad/file.txt").read()
"""
#os.path.join()
def get_template_path(path):
    file_path = os.path.join(os.getcwd(),path)  #cwd-current working directory 
    return file_path

file_ = 'this/is/a/file.txt'
print(get_template_path(file_))