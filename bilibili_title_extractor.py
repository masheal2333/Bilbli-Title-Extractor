import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox,
    QStatusBar
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QIcon

# 导入title_parser模块的功能
try:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from title_parser import get_video_parts
except ImportError as e:
    # 如果导入失败，尝试直接从当前目录导入
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        if os.path.exists(os.path.join(current_dir, "title_parser.py")):
            sys.path.append(current_dir)
        elif os.path.exists(os.path.join(current_dir, "Frameworks", "title_parser.py")):
            sys.path.append(os.path.join(current_dir, "Frameworks"))
        from title_parser import get_video_parts
    except ImportError:
        # 如果仍然无法导入，我们将在运行时通知用户
        def get_video_parts(bvid):
            raise ImportError("无法导入title_parser模块")

class TitleExtractorThread(QThread):
    """处理标题提取的线程，防止UI卡死"""
    # 定义信号
    finished = pyqtSignal(list)
    error = pyqtSignal(str)
    
    def __init__(self, bvid):
        super().__init__()
        self.bvid = bvid
        
    def run(self):
        try:
            titles = get_video_parts(self.bvid)
            if titles:
                self.finished.emit(titles)
            else:
                self.error.emit("未能获取到任何标题，请检查视频链接是否正确")
        except Exception as e:
            import traceback
            error_msg = str(e)
            if "requests" in error_msg and "module" in error_msg:
                self.error.emit("缺少requests模块，请安装：pip install requests")
            else:
                trace = traceback.format_exc()
                self.error.emit(f"提取标题时出错: {error_msg}\n{trace}")

class BilibiliTitleExtractor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # 设置窗口基本属性
        self.setWindowTitle('哔哩哔哩标题提取器')
        self.setGeometry(300, 300, 650, 500)
        
        # 创建中心部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)
        
        # 设置字体
        title_font = QFont('微软雅黑', 12, QFont.Bold)
        normal_font = QFont('微软雅黑', 10)
        
        # 标题标签
        header_label = QLabel('哔哩哔哩视频标题提取')
        header_label.setFont(QFont('微软雅黑', 16, QFont.Bold))
        header_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header_label)
        
        # 输入区域
        input_label = QLabel('请输入B站视频链接或BV号:')
        input_label.setFont(title_font)
        main_layout.addWidget(input_label)
        
        self.url_input = QLineEdit()
        self.url_input.setFont(normal_font)
        self.url_input.setPlaceholderText('例如: https://www.bilibili.com/video/BV1JV411t7ow 或 BV1JV411t7ow')
        main_layout.addWidget(self.url_input)
        
        # 按钮区域
        button_layout = QHBoxLayout()
        
        self.extract_button = QPushButton('获取标题')
        self.extract_button.setFont(title_font)
        self.extract_button.setMinimumHeight(36)
        self.extract_button.clicked.connect(self.extract_titles)
        button_layout.addWidget(self.extract_button)
        
        self.clear_button = QPushButton('清空')
        self.clear_button.setFont(normal_font)
        self.clear_button.setMinimumHeight(36)
        self.clear_button.clicked.connect(self.clear_fields)
        button_layout.addWidget(self.clear_button)
        
        button_layout.setStretch(0, 3)
        button_layout.setStretch(1, 1)
        main_layout.addLayout(button_layout)
        
        # 输出区域
        output_label = QLabel('提取的标题:')
        output_label.setFont(title_font)
        main_layout.addWidget(output_label)
        
        self.output_text = QTextEdit()
        self.output_text.setFont(normal_font)
        self.output_text.setReadOnly(True)
        main_layout.addWidget(self.output_text)
        
        # 添加状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('准备就绪')
        
        # 设置样式
        self.setStyleSheet('''
            QMainWindow {
                background-color: #f5f5f5;
            }
            QLabel {
                color: #333333;
            }
            QLineEdit, QTextEdit {
                border: 1px solid #cccccc;
                border-radius: 4px;
                padding: 6px;
                background-color: #ffffff;
            }
            QPushButton {
                background-color: #4e9ef5;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #3d8ee6;
            }
            QPushButton:pressed {
                background-color: #2d7dd6;
            }
            QPushButton#clear_button {
                background-color: #f0f0f0;
                color: #333333;
                border: 1px solid #cccccc;
            }
            QPushButton#clear_button:hover {
                background-color: #e0e0e0;
            }
            QStatusBar {
                background-color: #f0f0f0;
                color: #606060;
            }
        ''')
        
        # 设置按钮ID用于样式表
        self.clear_button.setObjectName('clear_button')
        
    def extract_titles(self):
        url = self.url_input.text().strip()
        if not url:
            QMessageBox.warning(self, '警告', '请输入视频链接或BV号')
            return
        
        # 提取BV号
        bv_match = None
        if "bilibili.com/video/" in url:
            try:
                bv_match = url.split("bilibili.com/video/")[1].split("?")[0].split("/")[0]
            except Exception:
                QMessageBox.warning(self, '警告', '无法从URL中提取BV号，请检查链接格式')
                return
        elif url.startswith("BV"):
            bv_match = url
        else:
            QMessageBox.warning(self, '警告', '无效的链接格式，请输入正确的B站视频链接或BV号')
            return
            
        # 禁用按钮，显示加载状态
        self.extract_button.setEnabled(False)
        self.statusBar.showMessage('正在提取标题...')
        
        # 启动线程提取标题
        self.thread = TitleExtractorThread(bv_match)
        self.thread.finished.connect(self.on_extraction_finished)
        self.thread.error.connect(self.on_extraction_error)
        self.thread.start()
    
    def on_extraction_finished(self, titles):
        if titles:
            # 显示标题到文本框
            self.output_text.clear()
            for i, title in enumerate(titles, 1):
                self.output_text.append(f"{i}. {title}")
            
            # 更新状态栏
            self.statusBar.showMessage(f'已提取 {len(titles)} 个标题')
        else:
            self.output_text.clear()
            self.output_text.append("未能获取到任何标题")
            self.statusBar.showMessage('提取失败: 未找到标题')
            
        # 恢复按钮状态
        self.extract_button.setEnabled(True)
    
    def on_extraction_error(self, error_msg):
        QMessageBox.critical(self, '错误', f'提取标题时出错: {error_msg}')
        self.statusBar.showMessage('提取失败')
        self.extract_button.setEnabled(True)
        
        # 在文本框中也显示错误信息
        self.output_text.clear()
        self.output_text.append(f"错误: {error_msg}")
        
        # 如果是缺少requests模块的错误，提供更详细的指导
        if "requests" in error_msg and "module" in error_msg:
            self.output_text.append("\n解决方法:")
            self.output_text.append("1. 请在终端中运行: pip install requests")
            self.output_text.append("2. 或者重新下载完整版本的应用")
    
    def clear_fields(self):
        self.url_input.clear()
        self.output_text.clear()
        self.statusBar.showMessage('准备就绪')

def main():
    # 设置异常钩子，确保未捕获的异常不会导致程序崩溃
    def exception_hook(exctype, value, traceback):
        print(f"未捕获的异常: {exctype}, {value}")
        sys.__excepthook__(exctype, value, traceback)
    
    sys.excepthook = exception_hook
    
    app = QApplication(sys.argv)
    window = BilibiliTitleExtractor()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
