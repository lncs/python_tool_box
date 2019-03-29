"""
批量修改文件内容
"""

import os
import re


def modify_contents(old_str, new_str, suffix, path='./modify_contents/'):
    files_list = os.listdir(path)
    print(files_list)
    for filename in files_list:
        if filename.endswith(suffix):
            filename_bak = filename + '.bak'
            with open(path + filename, 'r', encoding='utf-8') as f1, open(path + filename_bak, 'w', encoding='utf-8') as f2:
                for line in f1:
                    if old_str in line:
                        line = line.replace(old_str, new_str)
                        print(line)
                    f2.write(line)

            os.remove(path + filename)
            os.rename(path + filename_bak, path + filename)
        else:
            print(filename + '不参与此次内容修改')
    pass


def modify_contents_re(pattern_str, new_str, suffix, path='./modify_contents/'):
    files_list = os.listdir(path)
    print(files_list)
    pattern1 = re.compile(pattern_str)
    for filename in files_list:
        if filename.endswith(suffix):
            filename_bak = filename + '.bak'
            with open(path + filename, 'r', encoding='utf-8') as f1, open(path + filename_bak, 'w', encoding='utf-8') as f2:
                for line in f1:
                    print(111)
                    print(type(line))
                    print(line)
                    matcher1 = re.search(pattern1, line)
                    # re.search()
                    if (None != matcher1):
                        continue
                        old_str = matcher1.group(0)
                        # print(old_str)
                        line = line.replace(old_str, new_str)
                    f2.write(line)

            os.remove(path + filename)
            os.rename(path + filename_bak, path + filename)
        else:
            print(filename + '不参与此次内容修改')
    pass


if __name__ == '__main__':
    # # modify_contents('[事务处理结束]', '', 'uftfunction')
    modify_contents_re('\[事务处理\w+]( +| ?)(&#xD;)?', '', 'uftfunction')
    # s = 'af_delete_feedetailhs_feehs.uftfunction:[事务 处理结束]'
    # key = '\[事务处理\w+]( +| ?)(&#xD;)?'
    # pattern = re.compile(key)
    #
    # matcher = re.search(pattern, s)
    # if (None == matcher):
    #     print('matcher is null')
    # print(matcher.group())

    pass
