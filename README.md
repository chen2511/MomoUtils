# Momo's Utils

>   For Python Utils

功能说明：包括`json`、`日志`、`视频写入`工具包

### 1.JsonUtils

1.1 从文件中读取json格式数据到字典

1.2 写入字典到json格式文件

1.3 根据路径创建文件夹



### 2.Logger

日志记录器：既可以输出日志到终端，还可以写入日志文件。

可以设置日志保存的路径，还可以设置日志输出的模块。



### 3.CVUtils

没啥要紧的。。。



# 构建自己的`Python`包教程

## 1.项目准备

项目文件夹里面就是你要发布的所有内容。

```
/项目文件夹
    __init__.py
    helloworld.py
/setup.py
```



## 2.setup.py

setup.py是setuptools的构建脚本。它告诉setuptools你的包（例如名称和版本）以及要包含的代码文件。

关键是你的`name`和`packages`参数。

这个文件放在和你的packages同级目录即可。

```py
# setup.py
from setuptools import setup
setup(name='MomoUtils',
    version='0.1',
    description='Testing installation of Package',
    url='#',
    author='MomoChen',
    author_email='1514300203@qq.com',
    license='MIT',
    packages=['MomoUtils'],
    zip_safe=False)
```

运行：`python setup.py sdist`，生成目标文件

>   dist/
>
>     MomoUtils-0.1.tar.gz

最后`pip install ***` 即可











