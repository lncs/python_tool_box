### 批量修改文件后缀

import os


def modify_suffix(old_suffix, new_suffix, path='./suffix_files/'):
    # 列出当前路径下的所有文件
    files = os.listdir(path)
    print(files)
    for filename in files:
        # print(filename)
        portion = os.path.splitext(filename)
        print("文件名:{},文件后缀名:{}".format(portion[0], portion[1]))
        if old_suffix == portion[1]:
            newname = portion[0] + new_suffix
            os.rename(path+filename, path+newname)
            pass


if __name__ == '__main__':
    # 修改原子函数
    # modify_suffix('.uftfunction', '.uftatomfunction', )
    # 修改原子服务
    modify_suffix('.uftatomservice', '.uftfunction', )
    pass