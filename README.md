本仓库借用与openlab的mmsegmentation代码，应用于学习和科研作用。
改写了mmsegmentation的数据接口，目前采用如下的数据接口。
参数导入方式为传入一个txt文件，数据和标签的格式如下：
图片路径  标签路径
图片路径  标签路径
图片路径  标签路径
图片路径  标签路径
图片路径  标签路径
图片路径  标签路径

通过这个办法简化了mmsegmentation的数据接口，方便所有人简单上手使用。


This repository borrows the mmsegmentation code from openlab and is used for learning and scientific research.
The data interface of mmsegmentation has been rewritten, and the following data interface is currently used.
The parameter import method is to pass in a txt file, and the format of the data and labels is as follows:
imagepath labelpath
imagepath labelpath
imagepath labelpath
imagepath labelpath
imagepath labelpath
imagepath labelpath

This method simplifies the data interface of mmsegmentation, making it easy for everyone to get started.
