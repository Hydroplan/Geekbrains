import yaml
import os

new_file = open('config.yaml')
configuration = yaml.load(new_file, Loader=yaml.FullLoader)
new_file.close()

for key in configuration:
    os.makedirs(key, exist_ok=True)
    for keys in configuration[key]:
        os.makedirs(os.path.join(key, keys), exist_ok=True)
        for file in configuration[key][keys]:
            if isinstance(file, str):
                new_file = open(os.path.join(key, keys, file), 'w')
            else:
                for file2 in file:
                    os.makedirs(os.path.join(key, keys, file2), exist_ok=True)

                    for file3 in file[file2]:
                        os.makedirs(os.path.join(key, keys, file2, file3), exist_ok=True)
                        for file4 in file[file2][file3]:
                            new_file = open(os.path.join(key, keys, file2, file3, file4), 'w')
new_file.close()
