from django.shortcuts import render
from django.http import HttpResponse
from .models import ball
from django.core import serializers

# Create your views here.

def home(request):
    allBall = ball.objects.all()
    context = {
        'allBall': allBall,
    }
    return render(request,'homepage01.html',context)

def detail(request,idxx):
    ballDetail = ball.objects.filter(idx=idxx)
    context = {
        'iball': ballDetail,
    }
    return render(request,'detail01.html',context)


# Ajax GET 提交数据
def ajax_get(request):
    idxs = request.GET.dict()
    for idxm in idxs:
        print('sssssssssssssssssssssssssssssssss',idxm)
        ballQ = ball.objects.filter(idx=idxm) # 主商品
        for ballm in ballQ:
            ball_same_type = ball.objects.filter(type=ballm.type) # 所有同类商品
            priceMax = 0
            priceMin = 10000
            sizeMax = 0
            sizeMin = 10
            result = []
            for st in ball_same_type:
                if (st.price>priceMax): priceMax = st.price
                if (st.price<priceMin): priceMin = st.price
                if (st.sizeNum > sizeMax): sizeMax = st.sizeNum
                if (st.sizeNum < sizeMin): sizeMin = st.sizeNum
            if (sizeMax==sizeMin): sizeMin = 0
            mPrice = ballm.price
            mSizeNum = ballm.sizeNum
            orderResult = ball.objects.filter(type=ballm.type).extra(
                select={"new_order": "select SQRT( POWER(ABS(price-%s)/(%s-%s),2)+ POWER(ABS(sizeNum-%s)/(%s-%s),2) )"
                                     "where idx != %s"},
                select_params=(mPrice, priceMax, priceMin, mSizeNum, sizeMax, sizeMin, ballm.idx)
            ).extra(order_by=['new_order'])[1:13]
        ball_same_type = serializers.serialize('json', orderResult)

    return HttpResponse(ball_same_type,content_type="application/json")

