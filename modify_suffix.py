import os


def modify_suffix(old_suffix, new_suffix, path='./suffix_files/'):
    """
    :param old_suffix: 原后缀
    :param new_suffix: 目标后缀
    :param path: 保存需要修改后缀名文件的文件夹
    :return:
    """
    # 列出当前路径下的所有文件
    files = os.listdir(path)
    # print(files)
    for filename in files:
        # print(filename)
        portion = os.path.splitext(filename)
        # print("文件名:{},文件后缀名:{}".format(portion[0], portion[1]))
        if old_suffix == portion[1]:
            new_name = portion[0] + new_suffix
            os.rename(path + filename, path + new_name)
            pass


if __name__ == '__main__':
    # 修改原子函数
    # modify_suffix('.uftfunction', '.uftatomfunction', )
    # 修改原子服务
    # modify_suffix('.uftfunction', '.uftatomservice', )
    modify_suffix('.uftatomservice', '.uftfunction', )
    pass
