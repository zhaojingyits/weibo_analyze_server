from WeiboEntity.models import Weibo
from rest_framework import serializers
class WeiboEntitySerializer(serializers.Serializer):
    id=serializers.CharField(max_length=20, required=False)#
    bid=serializers.CharField(max_length=12,allow_blank=True, required=False)
    user_id=serializers.CharField(max_length=20,allow_blank=True, required=False)##传结构体时为空
    screen_name=serializers.CharField(max_length=30,allow_blank=True, required=False)##传结构体时为空
    text=serializers.CharField(allow_blank=True, required=False)
    topics=serializers.CharField(max_length=200,allow_blank=True, required=False)
    at_users=serializers.CharField(allow_blank=True, required=False)
    pics=serializers.CharField(allow_blank=True, required=False)
    video_url=serializers.CharField(allow_blank=True, required=False)
    location=serializers.CharField(max_length=100,allow_blank=True, required=False)
    created_at=serializers.DateField(required=False)
    source=serializers.CharField(max_length=30,allow_blank=True, required=False)
    attitudes_count=serializers.IntegerField(required=False)
    comments_count=serializers.IntegerField(required=False)
    reposts_count=serializers.IntegerField(required=False)
    retweet_id=serializers.CharField(max_length=20,allow_blank=True, required=False)

    def create(self, validated_data):
        """
        新建 create
        validated_data内置参数
        被序列化器中的save()调用的  通过两个参数不同来判断是create()还是update()
        :return 模型类对象
        """
        s=Weibo.objects.create(**validated_data)
        # print('id='+str(s.id)+'text='+str(s.text))
        return s  #此处指明create方法,如果出错,数据将存不到数据库

    def update(self,instance,validated_data):
        """
        更新
        :param instance: 要更新的实例化模型类对象
        :param validated_data:
        :return: 更新后的数据
        """
        instance.id = validated_data.get('id',instance.id)
        instance.bid = validated_data.get('bid',instance.bid)
        instance.user_id = validated_data.get('user_id',instance.user_id)
        instance.screen_name = validated_data.get('screen_name',instance.screen_name)
        instance.text = validated_data.get('text',instance.text)
        instance.topics = validated_data.get('topics',instance.topics)
        instance.at_users = validated_data.get('at_users',instance.at_users)
        instance.pics = validated_data.get('pics',instance.pics)
        instance.video_url = validated_data.get('video_url',instance.video_url)
        instance.location = validated_data.get('location',instance.location)
        instance.created_at = validated_data.get('created_at',instance.created_at)
        instance.source = validated_data.get('source',instance.source)
        instance.attitudes_count = validated_data.get('attitudes_count',instance.attitudes_count)
        instance.comments_count = validated_data.get('comments_count',instance.comments_count)
        instance.reposts_count = validated_data.get('reposts_count',instance.reposts_count)
        instance.retweet_id = validated_data.get('retweet_id',retweet_id)

        instance.save()    #在返回对象时,把数据保存在数据库中
        return instance
