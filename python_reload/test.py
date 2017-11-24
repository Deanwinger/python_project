import os

def dir_list():
    dir_list = []
    root = "/home/ubuntu/alan/gitlab/LS-API"
    for i in os.walk(root):
        print(i[0])
        for s in i[2]:
            abth_path = str(i[0]) + '/' + str(s)
            dir_list.append(abth_path)
            print(abth_path)
    # print(os.walk(root))

def find_file_info():
    filename = "/home/ubuntu/alan/python_related/python_fundemental/banks.txt"
    print(os.stat(filename))
    print(os.stat(filename).st_mtime)

if __name__ == '__main__':
    # dir_list()
    find_file_info()


# ('/home/ubuntu/alan/alan_blog', ['app', '.git'], ['README.md'])
# ('/home/ubuntu/alan/alan_blog/app', ['resources', 'common'], ['app.py', '__init__.py'])
# ('/home/ubuntu/alan/alan_blog/app/resources', [], ['users.py'])
# ('/home/ubuntu/alan/alan_blog/app/common', [], ['__init__.py', 'util.py'])
# ('/home/ubuntu/alan/alan_blog/.git', ['objects', 'branches', 'info', 'logs', 'refs', 'hooks'], ['COMMIT_EDITMSG', 'ORIG_HEAD', 'config', 'HEAD', 'description', 'FETCH_HEAD', 'index'])
# ('/home/ubuntu/alan/alan_blog/.git/objects', ['0b', '31', '2f', 'df', '2a', '0a', 'pack', '6c', '86', '32', 'e6', 'fa', 'ae', 'a1', 'info', 'd0', '61', '22', '03'], [])
# ('/home/ubuntu/alan/alan_blog/.git/objects/0b', [], ['d231018ce0deca883e5799f19ebed3cf6398f9'])
# ('/home/ubuntu/alan/alan_blog/.git/objects/31', [], ['6a20fc7cd54b381a47f009f8923ffd296e501a'])
# ('/home/ubuntu/alan/alan_blog/.git/objects/2f', [], ['1b0f67b5060b5997248f25d06e2af89d4bdb7e'])
# ('/home/ubuntu/alan/alan_blog/.git/objects/df', [], ['7ec033856eaf3fb840d25fd3f5ea7fc66ef766'])
# ('/home/ubuntu/alan/alan_blog/.git/objects/2a', [], ['1a2e227a1e65efbbf285dfb5348f7fe5dc9606'])
# ('/home/ubuntu/alan/alan_blog/.git/objects/0a', [], ['df4dd7c6d60b832e59859ff91a73a0c4dd5347'])
