import os
import shutil

os.makedirs(os.path.join('my_project', 'templates'), exist_ok=True)
shutil.copytree(os.path.join('my_project', 'mainapp', 'templates'),
                os.path.join('my_project', 'templates'), dirs_exist_ok=True)
shutil.copytree(os.path.join('my_project', 'authapp', 'templates'),
                os.path.join('my_project', 'templates'), dirs_exist_ok=True)
