import os


def change_charset(path, suffix='.txt', dest_charset='utf8'):
    """
    :param path: 存放需要转换编码格式文件的文件夹名
    :param suffix: 文件后缀名，默认为 .txt
    :param dest_charset: 目标编码，默认为 utf8
    :return:
    """
    files = (file for file in os.listdir(path) if file.endswith(suffix))
    os.chdir(path)
    for file in files:
        print('修改 {} 编码格式为：{}'.format(file, dest_charset))
        try:
            # print('尝试以gbk格式打开文件，目标编码：{}'.format(dest_charset))
            with open(file, encoding='gbk') as f1, open('temp.txt', 'w', encoding=dest_charset) as f2:
                f2.write(f1.read())
            # 删除原文件，并重命名临时文件为原文件名
            os.remove(file)
            os.rename('temp.txt', file)
        except:
            # 如果以gbk格式打开文件失败，以utf8格式打开
            # print('以gbk格式打开文件失败，以utf8格式打开，目标编码：{}'.format(dest_charset))
            with open(file, encoding='utf8') as f1, open('temp.txt', 'w', encoding=dest_charset) as f2:
                f2.write(f1.read())
            # 删除原文件，并重命名临时文件为原文件名
            os.remove(file)
            os.rename('temp.txt', file)


if __name__ == '__main__':
    change_charset('./change_charset', '.xml', 'utf8')
