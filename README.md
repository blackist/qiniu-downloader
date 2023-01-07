## qiniu-downloader

### Features

- 下载文件：file_download.py
- 删除文件：file_delete.py

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

