from django.db import models

class TravelInfo(models.Model):
    name = models.CharField(max_length=200,verbose_name="景点名称")
    area = models.CharField(max_length=100,verbose_name="所在区域",null=True, blank=True)
    city = models.CharField(max_length=200,verbose_name="城市")
    province = models.CharField(max_length=200,verbose_name="省份",null=True, blank=True)
    address = models.CharField(max_length=500,verbose_name="地址",null=True, blank=True)
    phone = models.CharField(max_length=100,verbose_name="电话",null=True, blank=True)
    rating = models.FloatField(verbose_name="评分",null=True, blank=True)
    longitude = models.FloatField(verbose_name="经度",null=True, blank=True)
    latitude = models.FloatField(verbose_name="纬度",null=True, blank=True)
    tags = models.CharField(max_length=500,verbose_name="标签",null=True, blank=True)
    image_url = models.CharField(max_length=500,verbose_name="图片链接",null=True, blank=True)
    hot_score = models.FloatField(verbose_name="热度评分",null=True, blank=True)
    comment_count = models.IntegerField(verbose_name="评论数量",null=True, blank=True)
    price = models.FloatField(verbose_name="票价",null=True, blank=True)

    class Meta:      #Meta = 配置这个模型在“数据库 + 后台界面”的行为和显示方式
        db_table = 'travel_travelinfo'  # 指定数据库表名
        verbose_name = "景点信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
