import pandas as pd
import pymysql

# 读取日本景点数据
df = pd.read_csv('data_jp.csv', encoding='utf-8-sig')
print(f"读取日本景点数据：{len(df)} 条")

# 数据清洗
df = df.drop_duplicates(subset=['景点名称', '城市名称'])
df['评分'] = pd.to_numeric(df['评分'], errors='coerce')
df['经度'] = pd.to_numeric(df['经度'], errors='coerce')
df['纬度'] = pd.to_numeric(df['纬度'], errors='coerce')
df['评论数量'] = pd.to_numeric(df['评论数量'], errors='coerce').fillna(0).astype(int)
df['票价'] = pd.to_numeric(df['票价'], errors='coerce').fillna(0)

print(f"清洗后数据：{len(df)} 条")

# 连接数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='dcy2251958',
    database='travelAnalysis',
    charset='utf8mb4'
)

cursor = conn.cursor()

# 插入数据
success_count = 0
error_count = 0

for _, row in df.iterrows():
    try:
        sql = """
        INSERT INTO travel_travelinfo
        (name, area, city, province, address, phone, rating, longitude, latitude,
         tags, image_url, hot_score, comment_count, price)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            row['景点名称'],
            row['所在区域'] if pd.notna(row['所在区域']) else '',
            row['城市名称'],
            row['省份'] if pd.notna(row['省份']) else '日本',
            row['地址'] if pd.notna(row['地址']) else '',
            row['电话'] if pd.notna(row['电话']) else '',
            row['评分'] if pd.notna(row['评分']) else None,
            row['经度'] if pd.notna(row['经度']) else None,
            row['纬度'] if pd.notna(row['纬度']) else None,
            row['标签'] if pd.notna(row['标签']) else '',
            row['图片链接'] if pd.notna(row['图片链接']) else '',
            row['热度评分'] if pd.notna(row['热度评分']) else None,
            int(row['评论数量']) if pd.notna(row['评论数量']) else 0,
            float(row['票价']) if pd.notna(row['票价']) else 0
        )
        cursor.execute(sql, values)
        success_count += 1
    except Exception as e:
        error_count += 1
        print(f"插入失败：{row['景点名称']} - {e}")

conn.commit()
cursor.close()
conn.close()

print(f"\n导入完成！")
print(f"成功：{success_count} 条")
print(f"失败：{error_count} 条")
