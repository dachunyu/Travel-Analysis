from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import TravelInfo

@login_required
def travel_list(request):
    city = request.GET.get('city', '')
    province = request.GET.get('province', '')
    keyword = request.GET.get('keyword', '')

    queryset = TravelInfo.objects.all()
    if city:
        queryset = queryset.filter(city=city)
    if province:
        queryset = queryset.filter(province=province)
    if keyword:
        queryset = queryset.filter(name__icontains=keyword)

    paginator = Paginator(queryset, 12)
    page = request.GET.get('page', 1)
    travels = paginator.get_page(page)

    cities = TravelInfo.objects.values_list('city', flat=True).distinct()
    provinces = TravelInfo.objects.values_list('province', flat=True).distinct()

    return render(request, 'travel_list.html', {
        'travels': travels,
        'cities': cities,
        'provinces': provinces,
        'city': city,
        'province': province,
        'keyword': keyword,
    })

@login_required
def travel_detail(request, pk): 
    travel = get_object_or_404(TravelInfo, pk=pk)
    return render(request, 'travel_detail.html', {'travel': travel})


@login_required
def ai_recommend(request):
    return render(request, 'ai_recommend.html')

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI

@csrf_exempt
@login_required
def ai_generate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        city = data.get('city', '')
        season = data.get('season', '')
        days = data.get('days', '')
        budget = data.get('budget', '')

        client = OpenAI(
            api_key='sk-096c46a3ac6d48449276f24665077b16',
            base_url='https://api.deepseek.com'
        )

        prompt = f"""
        请为我规划一个详细的旅游路线，要求如下：
        - 目标城市：{city}
        - 旅游季节：{season}
        - 行程天数：{days}
        - 预算：{budget}

        请按照以下格式输出：
        1. 行程概览
        2. 每天详细安排（包含景点、餐饮、交通建议）
        3. 费用预算分配
        4. 注意事项和小贴士

        请结合当地特色景点和美食，给出实用的建议。
        """

        try:
            response = client.chat.completions.create(
                model='deepseek-chat',
                messages=[
                    {'role': 'system', 'content': '你是一个专业的旅游规划师，熟悉中国各地景点、美食和文化。'},
                    {'role': 'user', 'content': prompt}
                ],
                max_tokens=2000
            )
            result = response.choices[0].message.content
            return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'result': f'生成失败：{str(e)}'})

    return JsonResponse({'result': '请求方式错误'})
