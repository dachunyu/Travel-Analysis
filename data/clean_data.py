import pandas as pd

# 读取原始数据
df = pd.read_csv('data.csv')
print(f"原始数据：{len(df)} 条")

# 1. 去除重复数据（基于景点名称+城市）
before = len(df)
df = df.drop_duplicates(subset=['景点名称', '城市名称'])
print(f"去重：删除 {before - len(df)} 条，剩余 {len(df)} 条")

# 2. 去除景点名称为空的行
df = df.dropna(subset=['景点名称'])

# 3. 处理评分字段
df['评分'] = pd.to_numeric(df['评分'], errors='coerce')
df['评分'] = df['评分'].fillna(df['评分'].mean().round(1))

# 4. 处理票价字段（提取数字，无票价填0）
df['票价'] = df['票价'].astype(str).str.extract(r'(\d+\.?\d*)')
df['票价'] = pd.to_numeric(df['票价'], errors='coerce').fillna(0)

# 5. 处理评论数量
df['评论数量'] = pd.to_numeric(df['评论数量'], errors='coerce').fillna(0).astype(int)

# 6. 处理热度评分
df['热度评分'] = pd.to_numeric(df['热度评分'], errors='coerce')
df['热度评分'] = df['热度评分'].fillna(df['热度评分'].mean().round(1))

# 7. 清理经纬度（去除无效坐标）
df['经度'] = pd.to_numeric(df['经度'], errors='coerce')
df['纬度'] = pd.to_numeric(df['纬度'], errors='coerce')
df = df.dropna(subset=['经度', '纬度'])

# 8. 清理标签字段
df['标签'] = df['标签'].str.strip()

print(f"清洗完成！最终 {len(df)} 条数据")
print(df[['景点名称', '城市名称', '评分', '票价', '经度', '纬度']].head(10))

# 保存清洗后数据
df.to_csv('clean.csv', index=False, encoding='utf-8-sig')
print("已保存到 data/clean.csv")