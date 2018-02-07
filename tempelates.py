import os

"""
/abc/ad/file.txt
\hi\this\is\a\file.txt

open("\hi\this\is\a\file.txt").read()

open("/abc/ad/file.txt").read()
"""
#os.path.join() cwd-current working directory
def get_template_path(path):
    file_path = os.path.join(os.getcwd(),path)  
    if not os.path.isfile(file_path):
        return Exception ("This is not a valid template path %s"% (file_path))
    return file_path

def get_template(path):
    file_path = get_template_path(path)
    return open(file_path).read()

def render_context(template_string,context):
    return template_string.format(**context)

file_ = 'tempelates/email_message.txt'
template = get_template(file_)
context = {
    "name": "Zeel",
    "date": None,
    "total": None
}
print(render_context(template,context))