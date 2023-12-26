# hardener
Linux加固程序

```text
django==4.2.8
pytest==7.4.3
```

# 使最小化安装的系统符合加固要求

```shell
echo "hd_admin ALL=(ALL) NOPASSWD:ALL" > /etc/sudoer.d/hd_admin

```