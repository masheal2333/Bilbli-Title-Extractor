# B站标题提取器

这是一个简单的GUI应用程序，用于从B站视频链接中提取视频标题。

## 功能

- 输入B站视频链接或BV号
- 提取视频所有选集的标题
- 显示标题列表
- 自动保存标题到文件

## 使用方法

1. 双击`dist/B站标题提取器.app`启动应用，或运行`./start.sh`脚本
2. 在输入框中粘贴B站视频链接或BV号（例如：BV1JV411t7ow）
3. 点击【获取标题】按钮
4. 提取的标题将显示在下方文本框中，并自动保存至`bilibili_titles.txt`文件

## 技术说明

- 使用PyQt5构建GUI界面
- 使用requests库获取网页内容
- 使用正则表达式提取标题信息
- 使用PyInstaller打包为.app应用

## 解决常见问题

如果启动应用时遇到问题，请尝试以下解决方法：
1. 确保已安装所需的依赖库：`pip install PyQt5 requests`
2. 如果应用无法启动，可能是缺少必要的依赖项。请使用以下命令重新打包：
   ```bash
   cd Bilibili/Bilbli_Title_Extractor
   pyinstaller bilibili_app.spec
   ```

## 打包方法

如需重新打包应用，可以使用以下命令：

```bash
cd Bilbli_Title_Extractor
pyinstaller bilibili_app.spec
```

打包后的应用会生成在`dist/B站标题提取器.app`目录下。 