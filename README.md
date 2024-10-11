# Machineory
Games made with Python, with tutorials in bilibili

## 介绍

## 库

### 使用的Python库
* PyGame

### 安装指令
```
pip install pygame
```

#### 快速安装

在指令后加上
```
-i https://mirrors.aliyun.com/pypi/simple/
```

## 打包

### 使用pyinstaller打包。

* 先要安装requests

```
pip install requests
```

* 获得requirements.txt

```
pip freeze > requirements.txt
```

* 安装pyinstaller

```
pip install pyinstaller
```

### 打包

#### 测试打包

```
pyinstaller -F run.py -n Machineory -i .\assets\images\icons\icon.ico
```

#### 正式打包

```
pyinstaller -F run.py -n Machineory -w -i .\assets\images\icons\icon.ico
```
