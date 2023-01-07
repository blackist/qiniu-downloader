import sys
from urllib.parse import urlsplit

import requests

import bucket_file_key


def download_progressbar(bucket_file_url, base_path):
    """
    下载文件及进度显示
    :param file_url: 文件url
    :param base_path: 本地目录，用于保存文件
    """

    response = requests.get(bucket_file_url, stream=True, verify=False)
    # 获取文件大小
    total_size = int(response.headers['Content-Length'])
    temp_size = 0
    with open(base_path + urlsplit(bucket_file_url).path, "wb") as f:
        # 每次写入大小，文件较大时，防止内存不足，分次写入
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                temp_size += len(chunk)
                f.write(chunk)
                f.flush()
                done = int(50 * temp_size / total_size)
                # 显示 已下载大小，总大小，进度条，百分比
                sys.stdout.write("\r%d:%d [%s%s] %d%%" % (
                    total_size, temp_size, '█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                sys.stdout.flush()
    print()


if __name__ == "__main__":

    config = bucket_file_key.build_config()

    base_url = repr(config['download']['BaseURL'])
    base_save = repr(config['download']['SavePath'])

    print(base_url)
    print(base_save)

    bucket_name, file_keys = bucket_file_key.get_file_keys()
    skip_file_keys = []

    index = 0

    for file_key in file_keys:

        print(index)
        index += 1
        if file_key in skip_file_keys:
            continue

        file_url = base_url + file_key
        print(file_key)
        download_progressbar(file_url, base_save)
