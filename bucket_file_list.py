import json

import jsonpath
from qiniu import Auth, BucketManager


def bucket_list():
    # 七牛的秘钥对
    access_key = ''
    secret_key = ''
    # 存储空间的名称
    bucket_name = ''

    q_auth = Auth(access_key, secret_key)
    bucket = BucketManager(q_auth)
    # 前缀
    prefix = None
    # 列举条目
    limit = 1000
    # 列举出除'/'的所有文件以及以'/'为分隔的所有前缀
    delimiter = None
    # 标记
    marker = None
    ret, eof, info = bucket.list(bucket_name, prefix, marker, limit, delimiter)
    # 格式化获取的Json文件列表
    print(json.dumps(ret, sort_keys=True, indent=2))
    # 使用JsonPath提取图片文件名称
    images_keys = jsonpath.jsonpath(ret, '$..key')
    # 显示图片名称、数量
    print(images_keys)

    return images_keys


if __name__ == "__main__":
    # clean model emission item
    bucket_list()
