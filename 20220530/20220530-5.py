#設計一個函數返回給定文件名的後綴名

def get_suffix(filename, has_dot=False):
    """
    獲取文件名的後綴名

    :param filename: 文件名
    :param has_dot: 返回的後綴名是否需要帶點
    :return: 文件的後綴名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''