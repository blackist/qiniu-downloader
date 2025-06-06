## qiniu-downloader

由于域名备案、https 证书付费问题，我把博客的文件存储迁移到了 [Cloudflare 的 R2 存储](https://cloudflare.com/)。

文件迁移采取先备份再上传的方式，使用脚本批量下载文件。

迁移完成后，删除七牛云的 Bucket 需要清空对象，使用脚本批量删除；不过，批量删除后七牛云有缓存，删除 Bucket 校验文件对象仍非空，需要等待较长时间才能执行删除操作。

### Features

- 下载文件：file_download.py
- 删除文件：file_delete.py

### python lib

``` bash 
pip3 install qiniu
pip3 install configparser
```

### 配置文件

在根目录创建 config.ini 文件：

``` 
[qiniu]
AK = KF***li
SK = VZ***hp
BucketName = my-image


[download]
SavePath = /Users/black/Downloads/my-image-bak
BaseURL = http://image.blackist.org/

```

- AK: 七牛云 access key
- SK: 七牛云 secret key
- BucketName: 需要操作的 bucket name
- SavePath: 下载文件的保存路径
- BaseURL: 文件的外链域名（七牛云公开文件需要绑定域名才可以访问、下载）

