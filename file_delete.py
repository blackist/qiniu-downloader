# -*- coding: utf-8 -*-

import bucket_file_key


def delete_files():
    bucket = bucket_file_key.build_bucket()

    bucket_name, file_keys = bucket_file_key.get_file_keys()

    for key in file_keys:
        print(key)
        # delete files
        ret, info = bucket.delete(bucket_name, key)

        print(ret)
        print(info)


if __name__ == "__main__":
    # clean model emission item
    delete_files()
