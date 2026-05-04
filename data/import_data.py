import pandas as pd
import pymysql

df = pd.read_csv('clean.csv')
print(f"准备导入 {len(df)} 条数据...")

def clean_val(v):
    if pd.isna(v):
        return None
    return v

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='dcy2251958',
    database='travelAnalysis',
    charset='utf8mb4'
)
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS travel_travelinfo;')
cursor.execute('''
    CREATE TABLE travel_travelinfo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(200),
        area VARCHAR(100),
        city VARCHAR(100),
        province VARCHAR(100),
        address VARCHAR(500),
        phone VARCHAR(100),
        rating FLOAT,
        longitude FLOAT,
        latitude FLOAT,
        tags VARCHAR(500),
        image_url VARCHAR(500),
        price FLOAT,
        hot_score FLOAT,
        comment_count INT
    ) CHARACTER SET utf8mb4;
''')

success = 0
for _, row in df.iterrows():
    try:
        cursor.execute('''
            INSERT INTO travel_travelinfo 
            (name, area, city, province, address, phone, rating, 
             longitude, latitude, tags, image_url, price, hot_score, comment_count)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''', (
            clean_val(row['景点名称']), clean_val(row['所在区域']),
            clean_val(row['城市名称']), clean_val(row['省份']),
            clean_val(row['地址']), clean_val(row['电话']),
            clean_val(row['评分']), clean_val(row['经度']),
            clean_val(row['纬度']), clean_val(row['标签']),
            clean_val(row['图片链接']), clean_val(row['票价']),
            clean_val(row['热度评分']), clean_val(row['评论数量'])
        ))
        success += 1
    except Exception as e:
        print(f"插入失败: {e}")
        break

conn.commit()
cursor.close()
conn.close()
print(f"导入完成！成功插入 {success} 条数据")