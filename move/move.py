import os
import shutil
for name in os.listdir('./Articles'):
    n = name.split('.')
    if len(n) < 2:
        continue
    if n[1] == 'txt':
        print(name)
        print('./Articles/' + name)
        print('./Articles/Done/')
        shutil.copyfile('./Articles/' + name, './Articles/Done/' + name)
        os.remove('./Articles/' + name)
