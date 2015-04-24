import os


def get_content(name):
    f = open('./Articles/' + str(name) + '.txt')
    content = f.read()
    return content

print(get_content('name1'))
