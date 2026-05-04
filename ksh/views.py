from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import pymysql
import json

def get_data(table):
    conn = pymysql.connect(
        host='localhost', user='root',
        password='dcy2251958',
        database='travelAnalysis', charset='utf8mb4'
    )
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    rows = cursor.fetchall()
    cols = [d[0] for d in cursor.description]
    conn.close()
    return [dict(zip(cols, r)) for r in rows]

@login_required
def index(request):
    part1 = get_data('part1')
    part2 = get_data('part2')
    part3 = get_data('part3')
    part4 = get_data('part4')
    part5 = get_data('part5')
    part7 = get_data('part7')
    part8 = get_data('part8')

    return render(request, 'ksh.html', {
        'part1': json.dumps(part1, ensure_ascii=False),
        'part2': json.dumps(part2, ensure_ascii=False),
        'part3': json.dumps(part3, ensure_ascii=False),
        'part4': json.dumps(part4, ensure_ascii=False),
        'part5': json.dumps(part5, ensure_ascii=False),
        'part7': json.dumps(part7, ensure_ascii=False),
        'part8': json.dumps(part8, ensure_ascii=False),
    })