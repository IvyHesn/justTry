import os


def get_content(name):
    f = open('./Articles/' + str(name) + '.txt')
    content = f.read()
    return content

# print(get_content('name1'))


def main():
    from models import Blog
    for name in os.listdir('./Articles'):
        n = name.split('.')
        if len(n) < 2:
            continue
        if n[1] == 'txt':
            content = get_content(n[0])
            Blog.objects.create(name=n[0], content=content)


if __name__ == "__main__":
    main()
    print('Done!')
