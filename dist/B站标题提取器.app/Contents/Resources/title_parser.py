import requests
import json
import re
import sys

def get_video_parts(bvid):
    """获取B站视频分集标题"""
    url = f"https://www.bilibili.com/video/{bvid}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.bilibili.com/"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # 使用正则表达式从页面提取窗口.__INITIAL_STATE__中的JSON数据
        pattern = r'window\.__INITIAL_STATE__=(.*?);\(function'
        match = re.search(pattern, response.text)
        
        if match:
            initial_state = json.loads(match.group(1))
            
            # 获取分集标题
            titles = []
            
            # 处理合集视频
            if 'ugcSeason' in initial_state and initial_state['ugcSeason'] and 'sections' in initial_state['ugcSeason']:
                for section in initial_state['ugcSeason']['sections']:
                    for episode in section['episodes']:
                        titles.append(episode['title'])
            # 处理普通多P视频
            elif 'videoData' in initial_state and 'pages' in initial_state['videoData'] and len(initial_state['videoData']['pages']) > 1:
                titles = [page['part'] for page in initial_state['videoData']['pages']]
            # 单个视频
            elif 'videoData' in initial_state:
                titles = [initial_state['videoData']['title']]
            
            return titles
        else:
            # 如果无法获取__INITIAL_STATE__数据，尝试直接从HTML提取标题
            title_pattern = r'<span class="video-episode-card__info-title">(.*?)</span>'
            titles = re.findall(title_pattern, response.text)
            
            if not titles:
                # 尝试其他方式获取标题
                title_pattern = r'<span class="ep-title">(.*?)</span>'
                titles = re.findall(title_pattern, response.text)
            
            if not titles:
                # 尝试获取主标题
                title_pattern = r'<h1[^>]*>(.*?)</h1>'
                main_title = re.search(title_pattern, response.text)
                if main_title:
                    titles = [main_title.group(1)]
            
            return titles
    
    except Exception as e:
        print(f"获取视频信息时出错: {e}")
        raise e  # 向上抛出异常，让GUI程序处理 