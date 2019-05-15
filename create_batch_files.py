import os


def create_files(file_count, file_name_pattern='', suffix='.txt', path='./create_files/'):

    if not os.path.exists(path):
        os.mkdir(path)
    for i in range(file_count):
        i_str = str(i + 1)
        filename = file_name_pattern + i_str + suffix
        f = open(path + filename, 'w', encoding='utf-8')
        f.close()


if __name__ == '__main__':
    create_files(2, 'test')
