from WeiboUser.models import User
from rest_framework import serializers
class WeiboUserSerializer(serializers.Serializer):
    id=serializers.CharField(max_length=20)
    screen_name=serializers.CharField(max_length=30)
    gender=serializers.CharField(max_length=10)
    statuses_count=serializers.IntegerField(required=False)
    followers_count=serializers.IntegerField(required=False)
    follow_count=serializers.IntegerField(required=False)
    registration_time=serializers.CharField(max_length=20,allow_blank=True, required=False)
    sunshine=serializers.CharField(max_length=20,allow_blank=True, required=False)
    birthday=serializers.CharField(max_length=40,allow_blank=True, required=False)
    location=serializers.CharField(max_length=200,allow_blank=True, required=False)
    education=serializers.CharField(max_length=200,allow_blank=True, required=False)
    company=serializers.CharField(max_length=200,allow_blank=True, required=False)
    description=serializers.CharField(max_length=140,allow_blank=True, required=False)
    profile_url=serializers.CharField(max_length=200,allow_blank=True, required=False)
    profile_image_url=serializers.CharField(max_length=200,allow_blank=True, required=False)
    avatar_hd=serializers.CharField(max_length=200,allow_blank=True, required=False)
    urank=serializers.IntegerField(required=False)
    mbrank=serializers.IntegerField(required=False)
    verified=serializers.BooleanField(required=False)
    verified_type=serializers.IntegerField(required=False)
    verified_reason=serializers.CharField(max_length=140,allow_blank=True, required=False)
    def create(self, validated_data):
        """
        新建 create
        validated_data内置参数
        被序列化器中的save()调用的  通过两个参数不同来判断是create()还是update()
        :return 模型类对象
        """
        return User.objects.create(**validated_data)  #此处指明create方法,如果出错,数据将存不到数据库

    def update(self,instance,validated_data):
        """
        更新
        :param instance: 要更新的实例化模型类对象
        :param validated_data:
        :return: 更新后的数据
        """
        instance.id = validated_data.get('id',instance.id)
        instance.screen_name = validated_data.get('screen_name',instance.screen_name)
        instance.gender = validated_data.get('gender',instance.gender)
        instance.statuses_count = validated_data.get('statuses_count',instance.statuses_count)
        instance.followers_count = validated_data.get('followers_count',instance.followers_count)
        instance.follow_count = validated_data.get('follow_count',instance.follow_count)
        instance.registration_time = validated_data.get('registration_time',instance.registration_time)
        instance.sunshine = validated_data.get('sunshine',instance.sunshine)
        instance.birthday = validated_data.get('birthday',instance.birthday)
        instance.location = validated_data.get('location',instance.location)
        instance.education = validated_data.get('education',instance.education)
        instance.company = validated_data.get('company',instance.company)
        instance.description = validated_data.get('description',instance.description)
        instance.profile_url = validated_data.get('profile_url',instance.profile_url)
        instance.profile_image_url = validated_data.get('profile_image_url',instance.profile_image_url)
        instance.avatar_hd = validated_data.get('avatar_hd',instance.avatar_hd)
        instance.urank = validated_data.get('urank',instance.urank)
        instance.mbrank = validated_data.get('mbrank',instance.mbrank)
        instance.verified = validated_data.get('verified',instance.verified)
        instance.verified_type = validated_data.get('verified_type',verified_type)
        instance.verified_reason = validated_data.get('verified_reason',instance.verified_reason)

        instance.save()    #在返回对象时,把数据保存在数据库中
        return instance
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data['education']:
            data['education'] = ""
        if not data['company']:
            data['company'] = ""
        if not data['description']:
            data['description'] = ""
        if not data['verified_reason']:
            data['verified_reason'] = ""
        return data