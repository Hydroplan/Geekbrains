import os

os.makedirs('my_project', exist_ok=True)
os.makedirs(os.path.join('my_project', 'settings'), exist_ok=True)
os.makedirs(os.path.join('my_project', 'mainapp'), exist_ok=True)
os.makedirs(os.path.join('my_project', 'adminapp'), exist_ok=True)
os.makedirs(os.path.join('my_project', 'authapp'), exist_ok=True)
