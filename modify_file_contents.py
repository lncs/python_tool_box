import os
import re


def modify_contents(old_str, new_str, suffix, path='./modify_contents/'):
    """
    :param old_str: 原内容
    :param new_str: 目标内容
    :param suffix: 文件后缀
    :param path: 文件所在文件夹
    :return:
    """
    files_list = os.listdir(path)
    for filename in files_list:
        if filename.endswith(suffix):
            filename_bak = filename + '.bak'
            with open(path + filename, 'r', encoding='utf-8') as f1, open(path + filename_bak, 'w', encoding='utf-8') as f2:
                for line in f1:
                    if old_str in line:
                        line = line.replace(old_str, new_str)
                    f2.write(line)

            os.remove(path + filename)
            os.rename(path + filename_bak, path + filename)
        else:
            print(filename + '不参与此次内容修改')


def modify_contents_re(pattern_str, new_str, suffix, path='./modify_contents/'):
    """
    :param pattern_str: 模式串，使用正则表达式
    :param new_str: 目标内容,为空代表删除匹配到的该行数据
    :param suffix: 文件后缀
    :param path: 文件所在文件夹
    :return:
    """
    files_list = os.listdir(path)
    pattern1 = re.compile(pattern_str)
    for filename in files_list:
        if filename.endswith(suffix):
            filename_bak = filename + '.bak'
            with open(path + filename, 'r', encoding='utf-8') as f1, open(path + filename_bak, 'w', encoding='utf-8') as f2:
                for line in f1:
                    # print(type(line))
                    # print(line)
                    matcher1 = re.search(pattern1, line)
                    # re.search()
                    if (None != matcher1):
                        if ('' != new_str):
                            old_str = matcher1.group(0)
                            # print(old_str)
                            line = line.replace(old_str, new_str)
                        else:
                            # new_str 为空，代表删除匹配到的该行数据
                            continue
                    f2.write(line)

            os.remove(path + filename)
            os.rename(path + filename_bak, path + filename)
        else:
            print(filename + '不参与此次内容修改')


if __name__ == '__main__':
    # 精确替换字符串
    # modify_contents('[事务处理结束]', '111', 'uftfunction')

    # 正则匹配事务处理** 替换为空（删除事务处理**）
    modify_contents_re('\[事务处理\w+]( +| ?)(&#xD;)?', '', 'uftfunction')
