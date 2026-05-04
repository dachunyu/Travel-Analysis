import requests
import pandas as pd
import time

API_KEY = 'b97256df45364fa35d4828b519db85eb'

CITIES = [
    '北京', '上海', '广州', '深圳', '成都', '杭州', '西安', '南京',
    '武汉', '重庆', '苏州', '丽江', '桂林', '厦门', '青岛', '大连',
    '哈尔滨', '长沙', '昆明', '贵阳', '三亚', '乌鲁木齐', '拉萨',
    '西宁', '兰州', '银川', '呼和浩特', '沈阳', '长春', '济南',
    '郑州', '太原', '石家庄', '合肥', '福州', '南昌', '海口',
    '南宁', '天津', '宁波', '温州', '扬州', '无锡', '常州',
    '黄山', '张家界', '敦煌', '大理', '香格里拉'
]

def get_attractions(city, page=1):
    url = 'https://restapi.amap.com/v3/place/text'
    params = {
        'key': API_KEY,
        'keywords': '景点',
        'types': '110000',
        'city': city,
        'citylimit': 'true',
        'offset': 25,
        'page': page,
        'extensions': 'all'
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        if data['status'] == '1':
            return data['pois']
        return []
    except Exception as e:
        print(f"请求失败: {e}")
        return []

all_data = []

for city in CITIES:
    print(f"正在获取 {city} 的景点数据...")
    for page in range(1, 5):  # 每个城市爬4页
        pois = get_attractions(city, page)
        if not pois:
            break
        for poi in pois:
            location = poi.get('location', ',').split(',')
            item = {
                '景点名称': poi.get('name', ''),
                '所在区域': poi.get('adname', ''),
                '城市名称': city,
                '省份': poi.get('pname', ''),
                '地址': poi.get('address', ''),
                '电话': poi.get('tel', ''),
                '评分': poi.get('biz_ext', {}).get('rating', ''),
                '经度': location[0] if len(location) > 1 else '',
                '纬度': location[1] if len(location) > 1 else '',
                '标签': poi.get('type', ''),
                '图片链接': '',
                '票价': poi.get('biz_ext', {}).get('cost', ''),
                '热度评分': poi.get('biz_ext', {}).get('rating', ''),
                '评论数量': poi.get('biz_ext', {}).get('rating_count', ''),
            }
            all_data.append(item)
        time.sleep(0.5)  # 避免请求太快
    print(f"{city} 完成，当前共 {len(all_data)} 条数据")

# 保存原始数据
df = pd.DataFrame(all_data)
df.to_csv('data.csv', index=False, encoding='utf-8-sig')
print(f"\n爬取完成！共 {len(df)} 条数据，已保存到 data/data.csv")