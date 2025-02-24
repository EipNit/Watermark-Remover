# Watermark Remover

## 项目简介

Watermark Remover 是一个用于从图像中去除水印的小型工具。它使用 Python 和一些常用的图像处理库来处理 PNG 格式的图像。

## 功能描述

1. **从图像中去除水印**：工具会将输入目录中的所有 PNG 图像读取并处理，将处理后的无水印图像保存在输出目录中。

## 项目结构
Watermark_Remover/
│
├── main.py
├── image/ # 存放待处理的图片
└── out/ # 存放处理后的图片

## 安装说明

1. 克隆项目：
    ```sh
    git clone https://github.com/你的用户名/Watermark_Remover.git
    cd Watermark_Remover
    ```

2. 安装依赖：
    ```sh
    pip install -r requirements.txt
    ```

3. 创建所需的目录结构：
    ```sh
    mkdir image out
    ```

## 使用方法

1. 将要处理的 PNG 图片放到 `image` 目录中。

2. 运行 `main.py`：
    ```sh
    python main.py
    ```

3. 处理后的图片会保存在 `out` 目录中，并附加 `_no_watermark` 后缀。

## 代码概述

`main.py` 文件主要包含以下几个部分：

1. 设置输入和输出目录。
2. 定义从图像中去除水印的函数 `remove_watermark`。
3. 遍历输入目录中的所有 PNG 图片，调用 `remove_watermark` 函数处理每个图片，并将处理后的图片保存到输出目录。
4. 列出输出目录中的所有处理后文件以验证处理结果。

## 依赖

- Python 3
- PIL (Pillow)
- numpy
