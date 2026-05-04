import pandas as pd
import pymysql

# 连接数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='dcy2251958',
    database='travelAnalysis',
    charset='utf8mb4'
)

df = pd.read_sql('SELECT * FROM travel_travelinfo', conn)
print(f"读取数据：{len(df)} 条")

def save_to_db(df_result, table_name):
    cursor = conn.cursor()
    df_result = df_result.where(pd.notnull(df_result), None)
    cols = ', '.join([f'`{c}` VARCHAR(255)' for c in df_result.columns])
    cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
    cursor.execute(f'CREATE TABLE {table_name} ({cols}) CHARACTER SET utf8mb4')
    for _, row in df_result.iterrows():
        vals = tuple(str(v) if v is not None else None for v in row)
        placeholders = ', '.join(['%s'] * len(vals))
        cursor.execute(f'INSERT INTO {table_name} VALUES ({placeholders})', vals)
    conn.commit()
    cursor.close()
    print(f"{table_name} 保存成功，共 {len(df_result)} 条")

# part1: 评分分布
part1 = df.groupby(pd.cut(df['rating'], bins=[0,2,3,4,4.5,5], 
    labels=['0-2','2-3','3-4','4-4.5','4.5-5'])).size().reset_index()
part1.columns = ['评分区间', '数量']
save_to_db(part1, 'part1')

# part2: 各省份景点数量
part2 = df.groupby('province').size().reset_index()
part2.columns = ['省份', '景点数量']
part2 = part2.sort_values('景点数量', ascending=False).head(20)
save_to_db(part2, 'part2')

# part3: 评论数排行前20
part3 = df[['name','city','comment_count']].sort_values(
    'comment_count', ascending=False).head(20)
part3.columns = ['景点名称', '城市', '评论数量']
save_to_db(part3, 'part3')

# part4: 各城市热门景点（评分最高前15城市）
part4 = df.groupby('city')['rating'].mean().reset_index()
part4.columns = ['城市', '平均评分']
part4 = part4.sort_values('平均评分', ascending=False).head(15)
save_to_db(part4, 'part4')

# part5: 票价区间分布
part5 = df.groupby(pd.cut(df['price'], bins=[-1,0,50,100,200,1000],
    labels=['免费','0-50','50-100','100-200','200以上'])).size().reset_index()
part5.columns = ['票价区间', '数量']
save_to_db(part5, 'part5')

# part6: 各省份景点地图数据
part6 = df.groupby('province').size().reset_index()
part6.columns = ['name', 'value']
save_to_db(part6, 'part6')

# part7: 热度评分排行前20
part7 = df[['name','city','rating']].sort_values(
    'rating', ascending=False).head(20)
part7.columns = ['景点名称', '城市', '评分']
save_to_db(part7, 'part7')

# part8: 各省份平均评分
part8 = df.groupby('province')['rating'].mean().round(2).reset_index()
part8.columns = ['省份', '平均评分']
part8 = part8.sort_values('平均评分', ascending=False)
save_to_db(part8, 'part8')

conn.close()
print("\n所有分析完成！")