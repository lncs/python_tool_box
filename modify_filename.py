import os


def modify_filename(new_filename, suffix, path='./modify_filename/'):
    """
    :param new_filename: 目标文件名模式
    :param path: 存放需要修改文件名的文件夹
    :return:
    """
    # 列出当前路径下的所有文件
    files = os.listdir(path)
    # print(files)
    i = 0
    for filename in files:
        # print(filename)
        i = i + 1
        portion = os.path.splitext(filename)
        if suffix == portion[1]:
            # print("文件名:{},文件后缀名:{}".format(portion[0], portion[1]))
            new_name = new_filename + str(i) + portion[1]
            os.rename(path + filename, path + new_name)


if __name__ == '__main__':
    modify_filename('test', '.uftfunction')
