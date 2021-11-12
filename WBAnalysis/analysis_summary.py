# from django.http import HttpResponse
from django.http.response import JsonResponse
from django.db import models
import time
import datetime
import numpy as np
import operator
from math import log
from WeiboUser.models import User
from . import weibo_spider
from WeiboEntity.models import Weibo
def summary(Userid):
    lists=analysis(Userid)
    # print(len(lists))
    print("用户属性方面的关注比（关注数/粉丝数）水军指数为：",lists[0])
    print("非原创微博数在总微博数占比  该用户发布微博非原创的指数为:",lists[1])
    print("用户微博的删除率指数为：",lists[2])
    print("同一天发微博数十条  该用户发布聚集性发布微博的指数为：",lists[3])
    lists.append(get_zhishu(Userid))
    print("用户微博的微博关键词分析指数为：",lists[4])
    sum_score=sum(lists)/len(lists)
    print("用户的可疑水军总指数为:",sum_score)
    data={}
    if lists[4]==0:
        error='该用户在最近一段时间没有任何微博发出，分析结果无参考价值'
        data={
            "userid": str(Userid),
            "username": User.objects.get(id=str(Userid)).screen_name,
            "total_mark": sum_score,
            "largest_mark": 5.0,
            "error_info": error,
            "details":[
                {
                    "item": "关注比",
                    "mark": lists[0],
                    "largest_mark": 5.0,
                    "describe": "关注数/粉丝数"
                },
                {
                    "item": "非原创微博指数",
                    "mark": lists[1],
                    "largest_mark": 5.0,
                    "describe": "非原创微博数在总微博数占比"
                },
                {
                    "item": "删除率",
                    "mark": lists[2],
                    "largest_mark": 5.0,
                    "describe": "水军可能经常删除微博"
                },
                {
                    "item": "聚集性发布微博指数",
                    "mark": lists[3],
                    "largest_mark": 5.0,
                    "describe": "水军经常聚集性发布微博"
                },
                {
                    "item": "关键词分析指数",
                    "mark": lists[4],
                    "largest_mark": 5.0,
                    "describe": "对其微博的文本进行分析"
                }
            ]
        }
    else:
        data={
            "userid": str(Userid),
            "username": User.objects.get(id=str(Userid)).screen_name,
            "total_mark": sum_score,
            "largest_mark": 5.0,
            "details":[
                {
                    "item": "关注比",
                    "mark": lists[0],
                    "largest_mark": 5.0,
                    "describe": "关注数/粉丝数"
                },
                {
                    "item": "非原创微博指数",
                    "mark": lists[1],
                    "largest_mark": 5.0,
                    "describe": "非原创微博数在总微博数占比"
                },
                {
                    "item": "删除率",
                    "mark": lists[2],
                    "largest_mark": 5.0,
                    "describe": "水军可能经常删除微博"
                },
                {
                    "item": "聚集性发布微博指数",
                    "mark": lists[3],
                    "largest_mark": 5.0,
                    "describe": "水军经常聚集性发布微博"
                },
                {
                    "item": "关键词分析指数",
                    "mark": lists[4],
                    "largest_mark": 5.0,
                    "describe": "对其微博的文本进行分析"
                }
            ]
        }
    return data

def analysis(ID):
    #创建一个游标对象
    '''cursor = db.cursor()
    sql1 = "SELECT * FROM user where id = " + str(ID) + ";"'''
    
    all_count=0 #所有微博数
    returns=[]
    try:
        '''cursor.execute(sql1)            #使用游标的execute()方法执行sql1语句
        results = cursor.fetchall()    #使用fetchall()获取全部数据'''
        results=User.objects.get(id=ID)
        
        all_count=results.statuses_count
        followers_count = results.followers_count
        follow_count = results.follow_count
        Bi_lv=(follow_count+1)/(followers_count+1)#关注/粉丝(+1为修正)
        Feng_guang=int(log(Bi_lv,1.5)+0.5)/2#用户属性方面的关注比（关注数/粉丝数）水军指数
        if(Feng_guang<0):#修正
            Feng_guang=0
        elif(Feng_guang>5):
            Feng_guang=5
        print ('debug_用户属性方面的关注比（关注数/粉丝数）水军指数为：',Feng_guang)
        # print(type(Feng_guang))
        returns.append(Feng_guang)
    except Exception as e:
        print("Error while analyzing debug_用户属性方面的关注比:",e)

    # sql2 = "SELECT * FROM weibo where user_id = " + str(ID) + ";"
    try:
        '''cursor.execute(sql2)            #使用游标的execute()方法执行sql1语句
        results = cursor.fetchall()    #使用fetchall()获取全部数据 
        lines=list(results)'''
        lines=Weibo.objects.filter(user_id=str(ID))
        or_count=0 #原创微博数
        created_at=[]
        for i in lines:
            created_at.append(i.created_at)
            if(i.retweet_id ==''):
                or_count+=1
        now_count=len(created_at)
        if now_count==0:
            Zhuang_fa=0
        else:
            Zhuang_fa=int((1-or_count/now_count)*10)/2 #非原创指数
        print("debug_非原创微博数在总微博数占比  该用户发布微博非原创的指数为:",str(Zhuang_fa))
        returns.append(Zhuang_fa)
        if all_count==0:
            del_lv=0 #删除率
        else:
            del_lv=int((1-now_count/all_count)*10)/2
        print("debug_用户微博的删除率指数为：",del_lv)
        returns.append(del_lv)

        #对用户发布微博时间进行整理分析
        t=0
        dt=[]     #创建空列表存放日期（年月日）编码
        for i in lines:
            # struct_time = time.strptime(created_at[i], "%Y-%m-%d %H:%M:%S") #strptime()函数根据指定的格式把一个时间字符串解析为时间元组
            #%H:%M
            created_at=i.created_at
            year=created_at.year
            mon=created_at.month
            day=created_at.day
            '''year=struct_time.tm_year
            mon=struct_time.tm_mon
            day=struct_time.tm_mday'''
            tt=100000*year+100*mon+day    #为日期设置编码
            dt.append(tt)                 #日期编码存入dt列表
            '''
            hour=struct_time.tm_hour
            if hour>=2 and hour<5:
                t=t+1
            '''
        dt = sorted(dt)  #对日期的列表进行排序
        unique_data = np.unique(dt)  #统计出现的日期有哪些
        #统计发布微博不正常日期的发布微博的总次数
        cou=0    
        for k in unique_data:
            if dt.count(k)>10:
                cou=cou+dt.count(k)
        if(len(lines)==0):
            Time_jujixin=0
        else:
            Time_jujixin=int(cou/len(lines)*10)/2
        
        print("debug_同一天发微博数十条  该用户发布聚集性发布微博的指数为：",Time_jujixin)
        returns.append(Time_jujixin)
        
    except Exception as e:
         print("Error while analyzing debug_同一天发微博数十条:",e)
    return returns

from . import jieba
from jieba import analyse
from optparse import OptionParser
import numpy as np
from math import log

#导入字典
jieba.load_userdict('./WBAnalysis/userdict.txt')
analyse.set_stop_words("./WBAnalysis/stop_words.txt")
analyse.set_idf_path("./WBAnalysis/idf.txt.big")

def key_words(user_id):
    '''
    输入用户账号,从数据库中读取所发的微博,提取关键词,
    关键词个数==微博条数 *2 
    指数为所有关键词的权值分布方差相关
    '''
    #创建一个游标对象
    '''cursor = db.cursor()
    sql1 = "SELECT text FROM weibo where user_id = " + str(user_id) + ";"'''
    
    try:
        '''cursor.execute(sql1)            #使用游标的execute()方法执行sql1语句
        results = cursor.fetchall()    #使用fetchall()获取全部数据
        alist=list(results)'''
        alist=Weibo.objects.filter(user_id=str(user_id)).values('text')
        # print(alist)
        weibo_count=len(alist)
        with open ("_text_.txt",'w',encoding='utf-8') as f:
            for line in alist:#一条记录
                print(line['text'])
                f.write(line['text'])
                f.write("\n")
        
        tags=get_key("_text_.txt",topK=weibo_count)
        
    except Exception as e:
        # cursor.rollback()
        print("Error while analyzing key_words:",e)
    #关闭游标连接
    return tags

def analysis_tag(tags):
    arr=[]
    try:
        for tag in tags:
            arr.append(tag[1])
        tags_var=np.var(arr)#方差
        tags_std=np.std(arr,ddof=1)
        Zhi_shu=int(log(0.1/tags_var,2)*2)/2#关键词提取的指数结果
        if(Zhi_shu>5):
            Zhi_shu=5
        elif(Zhi_shu<0):
            Zhi_shu=0
    except Exception as e:
        Zhi_shu=0
    return  Zhi_shu


def get_key(file_name, withWeight=True,topK=20):# 得到用于判读的水军数据集

    # 数据txt文件
    content = open(file_name, 'r',encoding='utf-8').read()
    tags = analyse.extract_tags(content, topK=topK, withWeight=withWeight)
    results=[]
    if withWeight is True:
        for tag in tags:#将权值输出为4位小数
            line=[]
            line=list(tag)
            line[1]=round(tag[1],4)
            results.append(line)            
    '''
    基于 TF-IDF 算法的关键词抽取
    jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=()) 
    sentence 为待提取的文本
    topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
    withWeight 为是否一并返回关键词权重值，默认值为 False
    allowPOS 仅包括指定词性的词，默认值为空，即不筛选
'''
    return results #结果

def get_zhishu(Userid):# 返回关键词分析指数
    tags=key_words(Userid)
    return analysis_tag(tags)


def get_summary(request):
    id = request.GET.get("id")
    print("get id:"+str(id))
    if User.objects.filter(id=str(id)).exists()==False:
        print('not exist')
        weibo_spider.go_spider([str(id)])
    data=summary(id)
    return JsonResponse(data)
