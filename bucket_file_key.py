import json
import jsonpath
import configparser
from qiniu import Auth, BucketManager


def build_config():
    config = configparser.ConfigParser()
    config.read('config.ini')

    return config


def build_bucket():
    # 七牛的秘钥对
    config = build_config()
    access_key = config['qiniu']['AK']
    secret_key = config['qiniu']['SK']

    qiniu_auth = Auth(access_key, secret_key)
    bucket = BucketManager(qiniu_auth)

    return bucket


def get_file_keys():
    # 前缀
    prefix = None
    # 列举条目
    limit = 1000
    # 列举出除'/'的所有文件以及以'/'为分隔的所有前缀
    delimiter = None
    # 标记
    marker = None

    bucket = build_bucket()
    # 存储空间的名称
    config = build_config()
    bucket_name = config['qiniu']['BucketName']

    # list files
    ret, eof, info = bucket.list(bucket_name, prefix, marker, limit, delimiter)

    # 格式化获取的Json文件列表
    # print(json.dumps(ret, sort_keys=True, indent=2))
    # 使用JsonPath提取文件名称
    files_keys = jsonpath.jsonpath(ret, '$..key')
    # 显示文件名称、数量
    print(files_keys)

    return bucket_name, files_keys


if __name__ == "__main__":
    # clean model emission item
    get_file_keys()
