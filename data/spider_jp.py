import requests
import pandas as pd
import time
import os

GOOGLE_API_KEY = 'AIzaSyBW-jxCypvmCEsi0qWCW-PQGoe8qlOuJeU'


CITIES = [
    
    '奈良', '金沢', '鎌倉', '日光', '箱根', '熊本', '那覇',
    '伊勢', '姫路', '岡山', '倉敷', '別府', '湯布院', '阿蘇',
    '函館', '小樽', '長野', '松本', '高山', '軽井沢', '草津',
    
    '広島', '福岡', '神戸', '横浜', '名古屋', '仙台', '長崎', '札幌',
    
    '沖縄', '北海道', '京都', '大阪', '東京', '富士山'
]

def get_attractions(city, max_results=20):
    """获取景点数据，支持分页"""
    results = []
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'query': f'{city} 観光スポット',
        'language': 'ja',
        'key': GOOGLE_API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        data = response.json()

        if data.get('status') == 'OK':
            for place in data.get('results', [])[:max_results]:
                loc = place.get('geometry', {}).get('location', {})
                item = {
                    '景点名称': place.get('name', ''),
                    '所在区域': '',
                    '城市名称': city,
                    '省份': '',
                    '地址': place.get('formatted_address', ''),
                    '电话': '',
                    '评分': place.get('rating', ''),
                    '经度': loc.get('lng', ''),
                    '纬度': loc.get('lat', ''),
                    '标签': '|'.join(place.get('types', [])),
                    '图片链接': '',
                    '票价': 0,
                    '热度评分': place.get('rating', ''),
                    '评论数量': place.get('user_ratings_total', 0),
                }
                results.append(item)
        elif data.get('status') == 'OVER_QUERY_LIMIT':
            print(f"{city} API配额已用完，请稍后再试")
        elif data.get('status') == 'REQUEST_DENIED':
            print(f"{city} 请求被拒绝，请检查API密钥")
        else:
            print(f"{city} 状态: {data.get('status')}")

    except Exception as e:
        print(f"{city} 请求失败: {e}")

    return results


if os.path.exists('data_jp.csv'):
    existing_df = pd.read_csv('data_jp.csv', encoding='utf-8-sig')
    all_data = existing_df.to_dict('records')
    crawled_cities = set(existing_df['城市名称'].unique())
    print(f"已加载现有数据：{len(all_data)} 条，已爬取城市：{crawled_cities}")
else:
    all_data = []
    crawled_cities = set()


for i, city in enumerate(CITIES, 1):
    if city in crawled_cities:
        print(f"[{i}/{len(CITIES)}] {city} 已爬取，跳过")
        continue

    print(f"🔄 [{i}/{len(CITIES)}] 正在获取 {city} 的景点数据...")
    pois = get_attractions(city, max_results=20)

    if pois:
        all_data.extend(pois)
        print(f"{city} 完成，获取 {len(pois)} 条，当前共 {len(all_data)} 条")

       
        df = pd.DataFrame(all_data)
        df.to_csv('data_jp.csv', index=False, encoding='utf-8-sig')
    else:
        print(f"{city} 未获取到数据")

    if city in ['東京', '大阪', '京都']:
        delay = 3  
    else:
        delay = 1.5

    print(f"等待 {delay} 秒...")
    time.sleep(delay)

print(f"\n爬取完成！共 {len(all_data)} 条数据，已保存到 data_jp.csv")
