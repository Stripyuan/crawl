#一个scrapy小应用  



---------  
###安装python环境  
1.下载Python for windows
废话不说，直接上网址：https://www.python.org/ftp/python/3.5.1/python-3.5.1.exe  
2.安装Python for windows（不得不说Python 在 Windows平台下的安装比傻瓜式还傻瓜式，直接点击Install Now，Python就直接被装到你的C盘了。）  

---------  
##安装scrapy  
1、`pip install scrapy`  
>命令安装，提示 
`Failed building wheel for Twisted
Microsoft Visual C++ 14.0 is required...`  

1、直接使用pip install scrapy安装不成功可以安装whl格式的包

首先下载scrapy的whl包，[点这里下载](http://www.lfd.uci.edu/~gohlke/pythonlibs/)  

2、安装whl格式包需要安装wheel库  
3、scrapy依赖twiste，同样使用whl格式的包进行安装
>[在这里](http://www.lfd.uci.edu/~gohlke/pythonlibs/)，在网页中搜索twisted找到其对应的whl包并下载

Twisted‑17.1.0‑cp36‑cp36m‑win_amd64.whl
根据你的Python的版本选择合适的包，名称中间的cp36是python3.6的意思，amd64是python的位数   
下载完成后使用cmd打开windows的命令行窗口，进入whl包所在的文件夹执行如下命令

`pip install [whl]`
例如：`pip install Twisted-17.1.0-cp36-cp36m-win_amd64.whl`  
Scrapy-1.3.3-py2.py3-none-any.whl包使用同样的方式安装，只是应该等到其所有依赖的包安装完成后才能进行安装，现在还不能安装  
4、scrapy依赖lxml包，需要先安装lxml包，lxml包依赖libxml2，libxml2-devel，所以安装lxmllibxml2， libxml2-devel。幸运的是之前我之前已经安装过lxml  
5、所有准备工作做完，终于可以安装scrapy包了，进入Scrapy-1.3.3-py2.py3-none-any.whl所在的目录  
`pip install Scrapy-1.3.3-py2.py3-none-any.whl  `  
Successfully ! 先别急着撒花，是否真的安装成功了，还需要验证，输入scrapy -h，显示scrapy的相关信息，大功告成...
--------
##运行项目
1、先将项目git clone 到本地（也就是自己的电脑上）  
2、通过命令行进入到你下载的目录，嗯，就是那个黑框（命令行）
3、直接输入命令`python main.py`就OK，好了，大功告成，好好欣赏妹子呦，也注意身体哈。。。
