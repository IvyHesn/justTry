import os
import shutil
import sys
sys.path.append('../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_web.settings")

import django
if django.VERSION >= (1, 7):
    django.setup()


def get_content(name):
    f = open('./Articles/' + str(name) + '.txt')
    content = f.read()
    return content

# print(get_content('name1'))


def main():
    from blog.models import Article
    for name in os.listdir('./Articles'):
        n = name.split('.')
        if len(n) < 2:
            continue
        if n[1] == 'txt':
            print(name)
            content = get_content(n[0])
            Article.objects.create(name=n[0], content=content)
            print('./Articles/' + name)
            print('./Articles/Done/')
            shutil.copyfile('./Articles/' + name, './Articles/Done/' + name)
            os.remove('./Articles/' + name)

if __name__ == "__main__":
    main()
    print('Done!')
