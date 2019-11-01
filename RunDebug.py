# coding=utf-8
import datetime
import math
import asyncio
import random
from time import sleep


def get_ceil(total, per):
    """

    :param total:
    :param per:
    :return:
    """
    return math.ceil(total / per)


def get_between_month(start, end):
    """
    获取两个时间段的每一个月
    :param start:
    :param end:
    :return:
    """
    start = datetime.datetime.strptime(start, '%Y-%m-%d')
    end = datetime.datetime.strptime(end, '%Y-%m-%d')
    start_year, start_month = start.year, start.month
    end_year, end_month = end.year, end.month
    diff_months = (end_year - start_year) * 12 + end_month - start_month
    month_range = []
    year, month = start_year, start_month
    for i in range(diff_months + 1):
        if (start_month + i) % 12 == 1:
            year += 1
            month = 1
        month_range.append("{}-{}".format(year, "0{}".format(month) if month < 10 else month))
        month += 1

    return month_range


class Potatoes(object):
    @classmethod
    def make(cls, num, *args, **kwargs):
        """

        :param num:
        :param args:
        :param kwargs:
        :return:
        """
        potatoes = [cls.__new__(cls, *args, **kwargs) for n in range(num)]
        return potatoes


total_potatoes = Potatoes.make(5)


async def buy_potatoes():
    """
    购买
    :return:
    """
    bucket = []
    i = 1
    async for p in take_potatoes(50):
        bucket.append(p)
        print(i, f"Got potato {id(p)}...")
        i += 1


async def take_potatoes(num):
    """
    获取
    :param num:
    :return:
    """
    count = 0
    while True:
        if len(total_potatoes) == 0:
            await ask_for_potato()
        else:
            potatoes = total_potatoes.pop()
            yield potatoes
            count += 1
            if count == num:
                break


async def ask_for_potato():
    """
    请求
    :return:
    """
    await asyncio.sleep(random.random())
    total_potatoes.extend(Potatoes.make(random.randint(1, 10)))


def run():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(buy_potatoes())
    loop.close()


# if __name__ == '__main__':
#     run()
import time

x = [i * 5 for i in range(5000)]


def get_start(l, n):
    if n < l[0]:
        return l[0]
    elif n > l[-1]:
        return l[-1]
    else:
        length = len(l)
        for i in range(length):
            if l[i] >= n:
                return l[i]


def get_end(l, n):
    if n < l[0]:
        return l[0]
    elif n > l[-1]:
        return l[-1]
    else:
        length = len(l)
        for i in range(length):
            if l[i] == n:
                return l[i]
            if l[i] > n:
                return l[i]


def get_max(li, start, end):
    l = li.copy()
    t = time.time()
    s = get_start(l, start)
    e = get_end(l, end)
    result = max(s, e)
    return result, time.time() - t


# print(get_max(x, -2, -1))
# print(get_max(x, 0, 9997))
# print(get_max(x, 4999, 9997))
# print(get_max(x, 4999, 4999))
# print(get_max(x, 2, 4))
# print(get_max(x, 9997, 100001))
# print(get_max(x, 100001, 100003))


def get_max2(li, start, end):
    t = time.time()
    l = li.copy()
    if end < l[0] or start > l[-1]:
        return 0
    l.append(start)
    l.append(end)
    l.sort()
    if l.index(start) + 1 == l.index(end) or l.index(start) == l.index(end):
        return 0

    if l.count(start) == 1:
        start_index = l.index(start) + 1
    else:
        start_index = l.index(start)

    if l.count(end) == 1:
        end_index = l.index(end) - 1
    else:
        end_index = l.index(end)

    result = max(l[start_index: end_index]) if start_index != end_index else l[start_index]
    return result, time.time() - t


# print("\n", "#" * 20)
# print(get_max2(x, -2, -1))
# print(get_max2(x, -1, 9998))
# print(get_max2(x, 4999, 9998))
# print(get_max2(x, 2, 4))
# print(get_max2(x, 9997, 100001))
# print(get_max2(x, 100001, 100002))

div = '''
<html class="expanded screen-max"><head><script type="text/javascript" async="" src="https://pos.baidu.com/auto_dup?psi=0651d7b2101ed8bf46b6e0ca32548db2&amp;di=0&amp;dri=0&amp;dis=0&amp;dai=0&amp;ps=0&amp;enu=encoding&amp;exps=110011&amp;dcb=___baidu_union_callback_&amp;dtm=AUTO_JSONP&amp;dvi=0.0&amp;dci=-1&amp;dpt=none&amp;tsr=0&amp;tpr=1571283662127&amp;ti=%E6%B6%89%E5%AF%86%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%AE%A1%E7%90&amp;ari=2&amp;dbv=2&amp;drs=4&amp;pcs=1261x952&amp;pss=1268x5335&amp;cfv=0&amp;cpl=3&amp;chi=1&amp;cce=true&amp;cec=GBK&amp;tlm=1571283662&amp;prot=2&amp;rw=969&amp;ltu=https%3A%2F%2Fwenku.baidu.com%2Fview%2Fe167fbacae45b307e87101f69e3143323968f5cc.html%3Frec_flag%3Ddefault%26sxts%3D1571282613997&amp;ecd=1&amp;uc=1920x1040&amp;pis=-1x-1&amp;sr=1920x1080&amp;tcn=1571283662&amp;dc=4"></script><style id="wk-style-10">.reader-txt-layer a.keyword {color:#19a97b;text-decoration:none;}.reader-txt-layer a.keyword:hover {text-decoration:none;border-bottom: 15px solid#19a97b;}.reader-txt-layer span.keyword-span-wrap {color:#19a97b;}.reader-txt-layer span.keyword-span-wrap:hover {text-decoration:none;cursor:pointer;border-bottom: 15px solid#19a97b;}</style><style id="reader-render-style">.reader-word-s1-5,.reader-word-s1-6,.reader-word-s1-7,.reader-word-s1-8,.reader-word-s1-9,.reader-word-s1-10,.reader-word-s1-11,.reader-word-s1-12,.reader-word-s1-13,.reader-word-s1-14,.reader-word-s1-0{ font-size:224px;} .reader-word-s1-0,.reader-word-s1-2,.reader-word-s1-3,.reader-word-s1-4,.reader-word-s1-5,.reader-word-s1-6,.reader-word-s1-7,.reader-word-s1-8,.reader-word-s1-9,.reader-word-s1-10,.reader-word-s1-11,.reader-word-s1-12,.reader-word-s1-13,.reader-word-s1-14,.reader-word-s1-1{ color:#000000;} .reader-word-s1-2{ font-size:351px;} .reader-word-s1-3{ font-family:'微软雅黑 Bold','383e8336c281e53a5802ff9e0030001','微软雅黑 Bold';} .reader-word-s1-2,.reader-word-s1-3,.reader-word-s1-4{ font-weight:600;} .reader-word-s1-8,.reader-word-s1-9,.reader-word-s1-10,.reader-word-s1-11,.reader-word-s1-12,.reader-word-s1-13,.reader-word-s1-14,.reader-word-s1-5{ font-family:'微软雅黑','383e8336c281e53a5802ff9e0060001','微软雅黑';} .reader-word-s1-13,.reader-word-s1-6{ letter-spacing:-0.71px;} .reader-word-s1-7{ font-family:'微软雅黑','383e8336c281e53a5802ff9e0070001','微软雅黑';} .reader-word-s1-8{ letter-spacing:-0.68px;} .reader-word-s1-9{ letter-spacing:-0.74px;} .reader-word-s1-10{ letter-spacing:-0.63px;} .reader-word-s1-11{ letter-spacing:-0.66px;} .reader-word-s1-12{ letter-spacing:-0.5800000000000001px;} .reader-word-s1-13{ letter-spacing:-0.71px;} .reader-word-s1-14{ letter-spacing:-0.75px;} #pageNo-1 .reader-parent{visibility:visible;}.reader-word-s2-1,.reader-word-s2-2,.reader-word-s2-3,.reader-word-s2-4,.reader-word-s2-5,.reader-word-s2-6,.reader-word-s2-7,.reader-word-s2-8,.reader-word-s2-9,.reader-word-s2-10,.reader-word-s2-11,.reader-word-s2-12,.reader-word-s2-13,.reader-word-s2-14,.reader-word-s2-15,.reader-word-s2-0{ color:#000000;font-size:224px;} .reader-word-s2-2,.reader-word-s2-4,.reader-word-s2-5,.reader-word-s2-6,.reader-word-s2-8,.reader-word-s2-9,.reader-word-s2-10,.reader-word-s2-11,.reader-word-s2-12,.reader-word-s2-13,.reader-word-s2-14,.reader-word-s2-15,.reader-word-s2-1{ font-family:'微软雅黑','383e8336c281e53a5802ff9e0060002','微软雅黑';} .reader-word-s2-2{ letter-spacing:-0.51px;} .reader-word-s2-3{ font-family:'微软雅黑','383e8336c281e53a5802ff9e0070002','微软雅黑';} .reader-word-s2-4{ letter-spacing:-0.63px;} .reader-word-s2-5{ letter-spacing:-0.56px;} .reader-word-s2-6{ letter-spacing:-0.42000000000000004px;} .reader-word-s2-6,.reader-word-s2-7{ letter-spacing:-0.42000000000000004px;} .reader-word-s2-8{ letter-spacing:-0.47px;} .reader-word-s2-9{ letter-spacing:-0.73px;} .reader-word-s2-10{ letter-spacing:-0.71px;} .reader-word-s2-11{ letter-spacing:-0.72px;} .reader-word-s2-12{ letter-spacing:-0.75px;} .reader-word-s2-13{ letter-spacing:-3.07px;} .reader-word-s2-14{ letter-spacing:-0.37px;} .reader-word-s2-15{ letter-spacing:-3.29px;} #pageNo-2 .reader-parent{visibility:visible;}.reader-word-s3-1,.reader-word-s3-2,.reader-word-s3-3,.reader-word-s3-4,.reader-word-s3-5,.reader-word-s3-6,.reader-word-s3-7,.reader-word-s3-8,.reader-word-s3-0{ color:#000000;font-size:224px;} .reader-word-s3-3,.reader-word-s3-4,.reader-word-s3-5,.reader-word-s3-6,.reader-word-s3-7,.reader-word-s3-8,.reader-word-s3-1{ font-family:'微软雅黑','383e8336c281e53a5802ff9e0060003','微软雅黑';} .reader-word-s3-2{ font-family:'微软雅黑','383e8336c281e53a5802ff9e0070003','微软雅黑';} .reader-word-s3-3{ letter-spacing:-0.68px;} .reader-word-s3-4{ letter-spacing:-0.66px;} .reader-word-s3-5{ letter-spacing:0.67px;} .reader-word-s3-6{ letter-spacing:-0.31px;} .reader-word-s3-7{ letter-spacing:-0.63px;} .reader-word-s3-8{ letter-spacing:-0.94px;} #pageNo-3 .reader-parent{visibility:visible;}.reader-word-s4-1,.reader-word-s4-2,.reader-word-s4-3,.reader-word-s4-4,.reader-word-s4-5,.reader-word-s4-6,.reader-word-s4-7,.reader-word-s4-0{ color:#000000;font-size:224px;} .reader-word-s4-2,.reader-word-s4-4,.reader-word-s4-5,.reader-word-s4-6,.reader-word-s4-7,.reader-word-s4-1{ font-family:'微软雅黑','383e8336c281e53a5802ff9e0060004','微软雅黑';} .reader-word-s4-2{ letter-spacing:-0.5800000000000001px;} .reader-word-s4-3{ font-family:'微软雅黑','383e8336c281e53a5802ff9e0070004','微软雅黑';} .reader-word-s4-4{ letter-spacing:-0.71px;} .reader-word-s4-5{ letter-spacing:-0.68px;} .reader-word-s4-6{ letter-spacing:-0.63px;} .reader-word-s4-7{ letter-spacing:-0.75px;} #pageNo-4 .reader-parent{visibility:visible;}.reader-word-s6-1,.reader-word-s6-2,.reader-word-s6-3,.reader-word-s6-4,.reader-word-s6-5,.reader-word-s6-0{ color:#000000;font-size:224px;} .reader-word-s6-2,.reader-word-s6-4,.reader-word-s6-5,.reader-word-s6-1{ font-family:'微软雅黑','383e8336c281e53a5802ff9e0060006','微软雅黑';} .reader-word-s6-2{ letter-spacing:-0.63px;} .reader-word-s6-3{ font-family:'微软雅黑','383e8336c281e53a5802ff9e0070006','微软雅黑';} .reader-word-s6-4{ letter-spacing:-0.47px;} .reader-word-s6-5{ letter-spacing:-0.65px;} #pageNo-6 .reader-parent{visibility:visible;}.reader-word-s5-1,.reader-word-s5-2,.reader-word-s5-3,.reader-word-s5-4,.reader-word-s5-5,.reader-word-s5-6,.reader-word-s5-0{ color:#000000;font-size:224px;} .reader-word-s5-1{ font-family:'微软雅黑','383e8336c281e53a5802ff9e0070005','微软雅黑';} .reader-word-s5-3,.reader-word-s5-4,.reader-word-s5-5,.reader-word-s5-6,.reader-word-s5-2{ font-family:'微软雅黑','383e8336c281e53a5802ff9e0060005','微软雅黑';} .reader-word-s5-3{ letter-spacing:-0.47px;} .reader-word-s5-4{ letter-spacing:-0.63px;} .reader-word-s5-5{ letter-spacing:-0.68px;} .reader-word-s5-6{ letter-spacing:-0.66px;} #pageNo-5 .reader-parent{visibility:visible;}</style><style id="wk-style-8">.reader-txt-layer a.keycard {color:#000;text-decoration:none;border-bottom: 15px solid #19a979;}</style><style id="reader-other-style"></style><style id="reader-font-style"></style>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312">
<meta http-equiv="X-UA-Compatible" content="IE=Edge">
<link rel="shortcut icon" href="https://www.baidu.com/cache/icon/favicon.ico" type="image/x-icon">
<link rel="icon" sizes="any" href="https://www.baidu.com/cache/icon/favicon.svg">



<title>涉密计算机管理制度&nbsp;- 百度文库</title>

<script async="" src="https://fex.bdstatic.com/hunter/alog/dp.csp.min.js?v=140804"></script><script async="" src="https://fex.bdstatic.com/hunter/alog/dp.min.js?v=-18187-18187"></script><script async="" src="https://fex.bdstatic.com/hunter/alog/alog.min.js?v=-18187-18187"></script><script>
    // 性能优化：打点标识title
    window.viewTime = {
        t: new Date().getTime()
    };
    // 性能优化：打点标识title end
    window.alogObjectConfig = {
        sample: '0.2',
 
        product: '112',
        page: '112_5',
        monkey_page: 'wenku-view',
        speed_page: '',
        speed: {
            sample: '0.1'
        },
 
        monkey: {
            sample: '0.1'
        },
 
        exception: { 
            sample: '0.1'
        },
 
        feature: {
            sample: '0.1'
        },
 
        cus: {
            sample: '0.1'
        },
 
        csp: {
            sample: '0.2',
            'default-src': [
                {match: '*bae.baidu.com', target: 'Accept,Warn'},
                {match: '*.baidu.com,*.bdstatic.com,*.baidustatic.com,*.baiduimg.com,*.bdimg.com,localhost,*.hao123.com,*.hao123img.com', target: 'Accept'},
                {match: /^(127|172|192|10)(\.\d+){3}$/, target: 'Accept'},
                {match: '*', target: 'Accept,Warn'}
            ]
        }
    };
    void function(a,b,c,d,e,f,g){a.alogObjectName=e,a[e]=a[e]||function(){(a[e].q=a[e].q||[]).push(arguments)},a[e].l=a[e].l||+new Date,d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d;var h=!0;if(a.alogObjectConfig&&a.alogObjectConfig.sample){var i=Math.random();a.alogObjectConfig.rand=i,i>a.alogObjectConfig.sample&&(h=!1)}h&&(f=b.createElement(c),f.async=!0,f.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),g=b.getElementsByTagName(c)[0],g.parentNode.insertBefore(f,g))}(window,document,"script","/hunter/alog/alog.min.js","alog"),void function(){function a(){}window.PDC={mark:function(a,b){alog("speed.set",a,b||+new Date),alog.fire&&alog.fire("mark")},init:function(a){alog("speed.set","options",a)},view_start:a,tti:a,page_ready:a}}();
    void function(n){var o=!1;n.onerror=function(n,e,t,c){var i=!0;return!e&&/^script error/i.test(n)&&(o?i=!1:o=!0),i&&alog("exception.send","exception",{msg:n,js:e,ln:t,col:c}),!1},alog("exception.on","catch",function(n){alog("exception.send","exception",{msg:n.msg,js:n.path,ln:n.ln,method:n.method,flag:"catch"})})}(window);
</script>


<script type="text/javascript">
    var PLAYER_LOAD_START = (new Date()).getTime();
</script>
<noscript>
<style type="text/css">
        .no-script {
            background-color: #ffffe1;
            color: #333;
            font-size: 14px;
            line-height: 20px;
            padding: 10px 0 10px 121px;
            margin-bottom: 10px;
            border-bottom: 1px solid #f1f1f1;
        }
        .no-script>a {
                text-align: center;
                width: 100%;
                text-decoration: underline;
                color: #333;
            }
        }
    </style>
<div class="no-script">
您的浏览器Javascript被禁用，需开启后体验完整功能，<a style=""
            target="_blank" class="link-to-enable-js"
            href="https://wenku.baidu.com/go/help_js">
请单击此处查询如何开启</a>
<img style="display: none;" src="https://wkctj.baidu.com/click.gif?pid=1&bid=1&fr=4&act_id=101711">
</div>
</noscript><script>
            (function(){
                var root = document.documentElement,
                        screenClassName = +screen.width > 1024 ? 'max' : 'min';
                root.className += ' screen-' + screenClassName;
            })();
        </script>
<script>
            // 事业部seo监控
            window.seoMonitorConf = {
                mode: 'wenku_pc'
            };
            var seoSrc = 'https://edu-wenku.bdimg.com/v1/usergrowth/seo.online.js?t=' + new Date().getTime();
            var script = document.createElement('script');
            script.src = seoSrc;
            setTimeout(function () {
                try {
                    document.body.appendChild(script);
                    setTimeout(function () {
                        document.body.removeChild(script);
                    }, 1000);
                }
                catch (e) {

                }
            }, 2000);
            // 事业部seo监控 end
        </script>



<meta name="description" content="在线互动式文档分享平台，在这里，您可以和千万网友分享自己手中的文档，全文阅读其他用户的文档，同时，也可以利用分享文档获取的积分下载文档 ">

<script type="text/javascript">!function(n){var t={},i={};i._data=t,i.get=function(n){return t[n]},i.set=function(n,i){if("string"==typeof n)t[n]=i;else for(var r in n)n.hasOwnProperty(r)&&(t[r]=n[r])},n.__fisData=i}(window);</script>
<link rel="stylesheet" type="text/css" href="//wkstatic.bdimg.com/static/wkcommon/widget/ui/css_core/ui/core_v3/core_v3_d429a2e.css"><link rel="stylesheet" type="text/css" href="//wkstatic.bdimg.com/static/wkcommon/pkg/pkg_wkcommon_base_00b3e20.css"><link rel="stylesheet" type="text/css" href="//wkstatic.bdimg.com/static/wkview/pkg/viewcommon_8b36725.css"><link rel="stylesheet" type="text/css" href="//wkstatic.bdimg.com/static/wkview/pkg/pkg_wkview_npm_ce517f8.css"><link rel="stylesheet" type="text/css" href="//wkstatic.bdimg.com/static/wkview/pkg/toctoolbar_63e2fff.css"><link rel="stylesheet" type="text/css" href="//wkstatic.bdimg.com/static/wkview/widget/common_toc_reader/reader_xreader/index_b81abc3.css"><link rel="stylesheet" type="text/css" href="//wkstatic.bdimg.com/static/wkcommon/pkg/pkg_wkcommon_htmlReader_a8ba29d.css"><link rel="stylesheet" type="text/css" href="//wkstatic.bdimg.com/static/wkcommon/pkg/pkg_wkcommon_pay_f7322bb.css"><link rel="stylesheet" type="text/css" href="//wkstatic.bdimg.com/static/wkview/widget/common_toc/common/style/main_82a8131.css"><script> alog('speed.set', 'ht', +new Date); </script><style type="text/css">.fc-ad-line{position:relative}.fc-ad-line:after{display:block;content:"";position:absolute;left:-50%;bottom:0;width:200%;height:1px;background:#e5e5e5;-webkit-transform:scale(.5);transform:scale(.5);pointer-events:none}</style><style type="text/css">.fc-parallax-scrolling{height:88px;position:relative;overflow:hidden;width:100%;min-width:560px}.fc-parallax-scrolling a{text-decoration:none;color:#fff}.fc-parallax-scrolling .fc-parallax-scrolling-wrapper{width:100%;position:absolute;top:-88px}.fc-parallax-scrolling .fc-parallax-scrolling-wrapper .fc-parallax-scrolling-run{display:block;width:100%;height:88px;margin:0;padding:0}.fc-parallax-scrolling-d9b779{background-color:#d9b779}.fc-parallax-scrolling-25ae84{background:#25ae84}.fc-parallax-scrolling-25ae84 .fc-parallax-scrolling-bogus{color:#f8e71c}.fc-parallax-scrolling .fc-parallax-scrolling-without-image .fc-parallax-scrolling-text{padding-left:6.8%}.fc-parallax-scrolling-text-line{overflow:hidden;text-overflow:ellipsis;-ms-text-overflow:ellipsis;-o-text-overflow:ellipsis;white-space:nowrap}.fc-parallax-scrolling .fc-parallax-scrolling-text .fc-parallax-scrolling-title{width:78%;font-size:24px;height:24px;line-height:24px;padding:19px 0 13px}.fc-parallax-scrolling .fc-parallax-scrolling-text .fc-parallax-scrolling-content{width:100%;height:14px;font-size:14px;line-height:14px}.fc-parallax-scrolling .fc-parallax-scrolling-text .fc-parallax-scrolling-content .fc-parallax-scrolling-content-left{width:100%;float:left}.fc-parallax-scrolling .fc-parallax-scrolling-text .fc-parallax-scrolling-sub{max-width:55%;display:inline-block}.fc-parallax-scrolling .fc-parallax-scrolling-text .fc-parallax-scrolling-tag{display:inline-block;font-size:12px;border:1px solid #fff;border-radius:2px;margin-right:6px;vertical-align:top}.fc-parallax-scrolling .fc-parallax-scrolling-text .fc-parallax-scrolling-bogus{display:inline-block;margin-left:13px;vertical-align:top}.fc-parallax-scrolling .fc-parallax-scrolling-wrapper .fc-parallax-scrolling-with-image .fc-parallax-scrolling-text{float:left;width:100%;margin-left:-268px}.fc-parallax-scrolling .fc-parallax-scrolling-wrapper .fc-parallax-scrolling-with-image .fc-parallax-scrolling-text-inner{margin-left:268px;padding-left:2.3%}.fc-parallax-scrolling .fc-parallax-scrolling-image{float:right;width:268px;background-color:#fff}.fc-parallax-scrolling .fc-parallax-scrolling-image ul{list-style:none;margin:0;padding:0}.fc-parallax-scrolling .fc-parallax-scrolling-image li{float:left}.fc-parallax-scrolling .fc-parallax-scrolling-image li div{width:88px;height:88px;background-repeat:no-repeat;background-size:cover;background-position:center center}.fc-parallax-scrolling .fc-parallax-scrolling-image .fc-parallax-scrolling-second-image{margin:0 2px}.fc-parallax-scrolling .fc-parallax-scrolling-without-image .fc-parallax-scrolling-text .fc-parallax-scrolling-bogus{float:none}@media (min-width:900px) and (max-width:1200px){.fc-parallax-scrolling .fc-parallax-scrolling-with-image .fc-parallax-scrolling-text .fc-parallax-scrolling-sub{width:90%}}@media (min-width:700px) and (max-width:900px){.fc-parallax-scrolling .fc-parallax-scrolling-with-image .fc-parallax-scrolling-text .fc-parallax-scrolling-sub{max-width:67%}}@media (min-width:600px) and (max-width:700px){.fc-parallax-scrolling .fc-parallax-scrolling-with-image .fc-parallax-scrolling-text .fc-parallax-scrolling-sub{max-width:59%}}</style><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkcommon/pkg/pkg_wkcommon_htmlReader_5998cf0.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkcommon/pkg/pkg_wkcommon_pay_90be412.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkview/widget/common_toc/reader_html/page_body/main_ca25087.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkcommon/widget/ui/lib/async_widget/async_widget_e8d6637.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkview/widget/common_toc/common/main_3e09e8a.js"></script><link rel="stylesheet" href="https://edu-wenku.bdimg.com/v1/pc/bdshare/static/api/css/share_style0_16.css?v=6aba13f0.css"><link rel="stylesheet" type="text/css" href="//wkretype.bdimg.com/retype/pipe/383e8336c281e53a5802ff9e?pn=1&amp;t=ttf&amp;rn=1&amp;v=6&amp;md5sum=eca395b49edb00ad238df924ac49504b&amp;range=0-100457&amp;sign=190fc0dc96&amp;a=1"><link rel="stylesheet" type="text/css" href="//wkretype.bdimg.com/retype/pipe/383e8336c281e53a5802ff9e?pn=2&amp;t=ttf&amp;rn=1&amp;v=6&amp;md5sum=eca395b49edb00ad238df924ac49504b&amp;range=100458-204795&amp;sign=190fc0dc96&amp;a=1"><link rel="stylesheet" type="text/css" href="//wkretype.bdimg.com/retype/pipe/383e8336c281e53a5802ff9e?pn=3&amp;t=ttf&amp;rn=1&amp;v=6&amp;md5sum=eca395b49edb00ad238df924ac49504b&amp;range=204796-282690&amp;sign=190fc0dc96&amp;a=1"><script>(function(win){win.ecom = win.ecom || {};win.ecom.pl = win.ecom.pl || {};win.ecom.pl.imTimesign = parseInt("87" || 0, 10);win.ecom.pl.searchId = "00059512fc7cefd1";})(window);(function(a){function b(d){var c=location.href.match("debug=1");var g=window.jQuery||{};if(!c){try{d(a.pl,g)}catch(f){}}else{d(a.pl,g)}}a.pl.run=function(d,c){if(c||arguments.length==1){bds.ready(function(){b(d)})}else{b(d)}};a.pl.q=function(f,g){g=g||document;if(g.getElementsByClassName){return g.getElementsByClassName(f)}else{var d=[];var c=g.all||g.getElementsByTagName("*");var e=c.length;f=f.replace(/\-/g,"\\-");var h=new RegExp("(^|\\s)"+f+"(\\s|$)");while(--e>=0){if(h.test(c[e].className)){d.push(c[e])}}return d}}})(window.ecom);(function(v){var h=undefined,g=undefined;var l=0,k=0;var e=0;var o=0;var i=0;var d=0;var m=0;var b=0;var t=0;var r=/link\?url\=([^\&]+)/;var n=/\?url\=([^\.]+)\./;function s(){var y=t.href;var x=r.exec(y)||n.exec(y);return x?x[1]:false}function u(z){var x=s();if(x!==false){var y=q(x,z);p(y)}}function p(z){var x="&ck="+[z,e,b,l,k,h,g,m].join(".");if(t.href){var y=t.href;if(y.indexOf("&ck=")==-1){t.href+=x}else{t.href=y.replace(/&ck=[\d.]*/,x)}}}function q(A,C){var B=0;for(var z=0;z<(((e*C)%99)+9);z++){var y=A.length<20?A.length:20;B+=A.charCodeAt((b*z)%A.length)}return B}function w(x){x=x||window.event;e++;if(h===undefined){h=x.clientX}if(g===undefined){g=x.clientY}o=new Date().getTime()}function f(y,x){y=y||window.event;t=y.target||y.srcElement;while(t&&t.tagName!="A"){t=t.parentNode}i=new Date().getTime();b=9999;l=y.clientX;k=y.clientY;if(o===0){m=0}else{m=i-o}u(x)}function j(y,x){d=new Date().getTime();b=d-i;u(x)}function c(C,z,B){var A,x,y;for(y in z){A=z[y];x=B[y];if(window.attachEvent){C.attachEvent("on"+A,x)}else{C.addEventListener(A,x,false)}}}function a(x){return[function(y){w(y)},function(y){f(y,x)},function(y){j(y,x)}]}v.ck=function(B,A){if(B.length===undefined){B=[B]}var x=B.length;var y=0;var z=a(A);for(;y<x;y++){c(B[y],["mouseover","mousedown","mouseup"],z)}}})(window.ecom.pl);window.ecom.pl.run(function(c){var e=c.q("KNkTOH");for(var b=0;b<e.length;b++){var a=e[b];var d=a.getElementsByTagName("A");c.ck(d,window.ecom.pl.imTimesign)}},false);</script><link rel="stylesheet" type="text/css" href="//wkretype.bdimg.com/retype/pipe/383e8336c281e53a5802ff9e?pn=4&amp;t=ttf&amp;rn=1&amp;v=6&amp;md5sum=eca395b49edb00ad238df924ac49504b&amp;range=282691-356753&amp;sign=190fc0dc96&amp;a=1"><link rel="stylesheet" type="text/css" href="//wkretype.bdimg.com/retype/pipe/383e8336c281e53a5802ff9e?pn=6&amp;t=ttf&amp;rn=1&amp;v=6&amp;md5sum=eca395b49edb00ad238df924ac49504b&amp;range=425668-&amp;sign=190fc0dc96&amp;a=1"><link rel="stylesheet" type="text/css" href="//wkretype.bdimg.com/retype/pipe/383e8336c281e53a5802ff9e?pn=5&amp;t=ttf&amp;rn=1&amp;v=6&amp;md5sum=eca395b49edb00ad238df924ac49504b&amp;range=356754-425667&amp;sign=190fc0dc96&amp;a=1"></head>



<body class="sf-2111 newTools" style=""><div id="WkDialogDownDoc" class="hide" style="display: none;"><div class="dialog-ad dialog-ad-miti"><div class="dialog-ad-hd"><span class="dialog-ad-logo"></span><h4 class="dialog-ad-title" style="font-size: px"></h4><a target="_blank" href="//wenku.baidu.com/miti" class="dialog-ad-more log-xsend" data-logxsend="[1, 100448]">免费安装&gt;&gt;</a></div><div class="dialog-container"><div class="close-btn"></div><div class="dialog-left-greenbar"></div><div class="dialog-top"><p class="doc-title">涉密计算机管理制度</p><p class="doc-size doc-size-1">19.3</p></div><div class="dialog-inner"><p class="ticket-num-msg msg1"></p><p class="ticket-detail-msg msg2"></p><div class="wealth-5-container hide"><a href="javascript:;" class="wealth-5-btn-use-down-load-ticket btn-gray btn-m">使用下载券下载</a><a href="javascript:;" class="wealth-5-btn-use-free btn-green btn-m"><i class="btn-ico"></i><span>免下载券下载</span></a></div><div class="ticket-no-wealth-container hide"><div class="ticket-btn-container ticket-btn-container-vip"><a href="javascript:;" class="btn-green btn-m ticket-exchange-btn">兑换后下载</a><a href="javascript:;" class="btn-gray btn-m ticket-user-free-download-btn">免下载券下载</a></div><div class="clear"></div><div class="ticket-raido-container hidden"><div class="ticket-raido-bg"><span class="ticket-radio-tips">您共有<i>100</i>积分，可兑换：</span><ul><li class="disable"><span class="sel-option" data-value="3"></span>3下载券</li><li class="disable"><span class="sel-option" data-value="5"></span>5下载券</li><li class="disable"><span class="sel-option" data-value="10"></span>10下载券</li><li class="disable"><span class="sel-option" data-value="30"></span>30下载券</li><li class="disable"><span class="sel-option" data-value="50"></span>50下载券</li><li class="other"><span class="sel-option"></span><input type="text" placeholder="其他" class="other-input">下载券</li></ul><div class="ticket-tips"><div class="ticket-tips-item w6 ticket-num">兑换后获得：<em></em>下载券<span class="ticket_gift_tips">+赠3下载券</span></div><div class="ticket-tips-item w4">共消耗：<em class="ticket-wealth"></em>积分</div><div class="tikcet-tips-notice w4">下载券有效期：<em>30天</em></div></div></div><a class="btn-green btn-l ticket-exchange-download-btn                         'ticket-exchange-download-btn-disable" href="javascript:;">兑换并下载</a></div></div><div class="vip-getback hide"><a href="javascript:;" class="ui-bz-btn-senior btn-vip-ticket-download"><b class="ui-bz-btn-p-16 ui-bz-btc">花费下载券下载</b></a><a href="###" class="ui-bz-btn"><b class="ui-bz-btn-p-16 ui-bz-btc">续费VIP<i>/赠5次下载特权</i></b></a></div><div class="user-dialog-download-btn-center hide"><a class="dialog-down-load-btn btn-green btn-l" href="javascript:void(0);">续费VIP</a><a class="btn-orange btn-l ml24" href="/user/mydocs?check_new_user_gift=1"><b class="gift-icon"></b>领取新手礼包</a></div><div class="dialog-down-load-btn-center"><a class="dialog-down-load-btn btn-green btn-l" href="javascript:void(0);">续费VIP</a></div><div class="vcode-box vcode-disable"><input type="text" class="vcode-ipt"><img src=""><span class="vcode-change">换一换</span><b class="vcode-right"></b><p class="error-tip"><b class="vcode-error"></b><span>请输入正确的验证码！</span></p></div><div class="download-btn-others"><a href="/cashier/browse/dispatch?doc_id=' + docId + '" target="_blank" class="download-btn-tip">续费3月即送下载特权</a></div></div><div class="dialog-bottom"><p id="bottom-btn" class="bottom-btn">使用下载券下载</p><p id="price10-bottom-btn" class="price10-bottom-btn hide" style="text-decoration: none;">由于文档价格较高，建议您使用<span style="text-decoration: underline; color: #139f72;">下载特权</span>下载</p><p class="bottom-msg">因本次下载而产生的财富将由百度文库以一定方式转交版权人</p></div></div></div></div><iframe class="dialog-container-iframe" allowtransparency="true" src="" frameborder="0" scrolling="no"></iframe>





<script>
(function(Data) {

		var smallFlowContent = [];
					smallFlowContent.push('xll_search_download' + '=' + '1');
					smallFlowContent.push('xll_view_newviewtpl' + '=' + '0');
					smallFlowContent.push('viewPageChangeOnePPT' + '=' + '1');
					smallFlowContent.push('viewPageChangeOneXreader' + '=' + '1');
					smallFlowContent.push('not_hit_dump_doc' + '=' + '0');
					smallFlowContent.push('isBaiduWiseGuideSmallFlow' + '=' + '0');
					smallFlowContent.push('isBaiduWiseGuideValid' + '=' + '0');
					smallFlowContent.push('isBaiduWiseGuideVipSmallFlow' + '=' + '0');
					smallFlowContent.push('isBaiduWiseGuideVipValid' + '=' + '0');
				
		Data.set('smallFlowContent', smallFlowContent);

}(window.__fisData));
</script>

<script>
	(function(Data) {
		var WkInfo = Data.get("WkInfo") || {};
		var isLogin="1";WkInfo.PageInfo={isLogin:!!isLogin,copyright:"1",tpl:"wk_info",docTypeList:[["none",""],["doc","Word\u6587\u6863"],["xls","Excel\u8868\u683c"],["ppt","PPT\u6587\u7a3f"],["doc","Word\u6587\u6863"],["xls","Excel\u8868\u683c"],["ppt","PPT\u6587\u7a3f"],["pdf","pdf\u6587\u6863"],["txt","txt\u6587\u6863"],["wps","Word\uff08\u91d1\u5c71\uff09"],["et","Excel\uff08\u91d1\u5c71\uff09"],["dps","PPT\uff08\u91d1\u5c71\uff09"],["vsd","Visio\u7ed8\u56fe"],["rtf","rtf\u6587\u6863"],["pot","PPT\u6a21\u677f"],["pps","PPT\u653e\u6620"],["epub","ePub\u6587\u6863"],["dwg","CAD\u6587\u4ef6"]]};
;
				var isCreater="",isLimit="",isNoUsername="",isAdmin="";WkInfo.UserInfo={wealth:"0",payed:!1,userName:"小虫很酷",userGradeNum:"1",isCreater:!!isCreater,isLimit:!!isLimit,isNoUsername:!!isNoUsername,isAdmin:!!isAdmin},WkInfo.errMsg={0:"\u63d0\u4ea4\u6210\u529f",1:"\u7cfb\u7edf\u9519\u8bef",2:"\u7528\u6237\u672a\u767b\u9646",5:"\u64cd\u4f5c\u9891\u7387\u592a\u5feb",11:"\u63d0\u4ea4\u53c2\u6570\u975e\u6cd5"};
;
				Data.set("WkInfo",WkInfo);
	}(window.__fisData));
</script>

<div class="wk-other-new-cntent">
<a href="//wenku.baidu.com" class="wkLogo"></a>
<div class="user-bar user-bar-new" style="left: 914px;">
<ul class="inner">
<li><a href="https://www.baidu.com/" class="logSend baidu-home" data-logsend="{&quot;send&quot;:[&quot;general&quot;,&quot;bdindex&quot;,{&quot;login&quot;:1}]}" alog-action="userbar.loginbdhome">百度首页</a></li>
<li><a href="//wenku.baidu.com/" class="wenku-home">文库首页</a></li>
<li class="mn-lk-w member-icon" id="user-bar-uname">
<a id="userNameCon" href="/user/mydocs" target="_blank" class="uname mn-lk user-my-name log-xsend user-bar-home-link" data-logxsend="[1, 100795]">
<span class="text-dec-under">
小虫很酷
</span>
<span id="wk-user-icon-home"><span class="iconfont ic-not-vip"></span></span>
</a>
<div class="user-my-name-tip user-mn-tip">
<ul class="user-mn-tip-inner">
<li class="user-info-wrap">
<div class="user-image" style="background-image:url(https://gss0.bdstatic.com/7Ls0a8Sm1A5BphGlnYG/sys/portraitn/item/wenku.1.77c38886.XftyCgxYBqZM-LwMActxfQ.jpg)"></div>
<div class="user-tip-info">
<a class="user-name log-xsend" href="/user/mydocs" target="_blank" data-logxsend="[1, 101969, {&quot;index&quot;:&quot;name&quot;}]">
小虫很酷
<div class="tip-vip-ico"><span class="iconfont ic-not-vip"></span></div>
</a>
<div class="vip-info">
<span class="tip-vip-status">您还未开通VIP</span>
<a class="tip-vip-btn" href="/ndcashier/browse/jiaoyuvipcashier?cashier_code=idcard_kt" target="_blank">立即开通</a>
</div>
</div>
<a href="https://passport.baidu.com/?logout&amp;aid=7&amp;u=https%3A//wenku.baidu.com/view/e167fbacae45b307e87101f69e3143323968f5cc.html%3Frec_flag%3Ddefault%26sxts%3D1571282613997" id="logout" class="logSend tip-logout" data-logsend="{&quot;send&quot;:[&quot;general&quot;,&quot;logout&quot;]}">退出</a>
</li>
<li class="card-info">
<a class="card-item log-xsend" href="/user/mydocs" target="_blank" data-logxsend="[1, 101969, {&quot;index&quot;:&quot;user&quot;}]">
<span class="card-ico"><i class="user-card"></i></span>
个人中心</a>
<a class="card-item log-xsend" href="/ndvipmember/browse/index" target="_blank" data-logxsend="[1, 101969, {&quot;index&quot;:&quot;vip&quot;}]">
<span class="card-ico"><i class="vipmember-card"></i></span>
会员中心</a>
<a class="card-item log-xsend" href="/user/task?fr=status" target="_blank" alog-action="userbar.mytask" data-logxsend="[1, 101969, {&quot;index&quot;:&quot;task&quot;}]">
<span class="card-ico"><i class="task-card"></i></span>
我的任务</a>
<a class="card-item log-xsend" href="/wenkuverify?from=3" target="_blank" data-logxsend="[1, 100135]">
<span class="card-ico"><i class="auth-card"></i></span>
申请认证</a>
</li>
</ul>
</div>
</li>
<li style="position: relative;"><a href="/cashier/browse/dispatch?dqStatCode=topnav_joinvip_new" target="_blank" title="" style="height: auto;" id="my-wkHome-vip-tips" class="log-xsend" data-logxsend="[1, 101547, {'index':0, 'pptChuileiView': undefined}]"><span class="s-vip-text">加入VIP</span></a><div class="vip-tips-hover-div clearfix" style="width: 180px;"><div class="vip-tips-hover-div-content"><ul><li class="icon-pro-doc">享VIP专享文档下载特权</li><li class="icon-share-doc">赠共享文档下载特权</li><li class="icon-free-doc">100w优质文档免费下载</li><li class="icon-yuedu-vip">赠百度阅读VIP精品版</li></ul><a target="_blank" class="log-xsend vip-tips-hover-gotocashier ljkt-btn-gold vip-tips-hover-to-cashier" data-logxsend="[1, 101547, {'index': 0,'pptChuileiView': undefined}]" href="/cashier/browse/dispatch?dqStatCode=topnav_joinvip_new">立即开通</a></div></div></li>
<li class="user-my-class-new" id="user-my-class"><a href="/user/mymessage" class="my-notice">消息<span class="my-notice" title="消息" alog-action="userbar.mynotice"></span></a></li>
<li class="fankui fankui-hide"><a class="help-feedback">意见反馈</a></li>
<li id="mywenku" class="mn-lk-w user-my-wenku"><a href="javascript:void(0);" class="mn-lk logSend">更多</a>
<div class="mn-tip user-my-wenku-tip" style=" width:93px; right: -8px;">
<div class="mn-tip-inner">
<ul class="mn clearfix mn-tip-shadow">
<li class="fankui-li-item"><a class="help-feedback" title="意见反馈">意见反馈</a></li>
<li><a href="/apps?fr=1011" target="_blank" alog-action="userbar.loginapp" title="下载客户端">下载客户端</a></li>
<li><a href="http://passport.baidu.com/center" class="logSend" data-logsend="{&quot;send&quot;:[&quot;general&quot;,&quot;userinfo&quot;]}" target="_blank" alog-action="userbar.mysetting">百度帐号设置</a></li>
<li class="vip-fankui"><a href="https://wenku.baidu.com/portal/browse/help#help/12" target="_blank" title="VIP专属客服">VIP专属客服</a></li>
</ul>
<i class="mn-tip-icon"></i>
</div>
</div>
</li>
</ul>
</div>
<div class="s_tab" alog-group="switch.productline">
<a data-href="http://www.baidu.com" href="http://www.baidu.com/s?wd=word&amp;fr=wenku" class="logSend " data-logsend="{&quot;send&quot;:[&quot;general&quot;,&quot;toptablink&quot;,{&quot;to&quot;:&quot;webpage&quot;}]}" wdfield="wd" onmousedown="setHeadUrl(this)">网页</a>
<a data-href="http://news.baidu.com" href="http://news.baidu.com/ns?word=word&amp;tn=news&amp;cl=2&amp;rn=20&amp;ct=1&amp;fr=wenku" class="logSend" data-logsend="{&quot;send&quot;:[&quot;general&quot;, &quot;toptablink&quot;,{&quot;to&quot;:&quot;news&quot;}]}" wdfield="word" onmousedown="setHeadUrl(this)">资讯</a>
<a data-href="http://v.baidu.com" href="//www.baidu.com/sf/vsearch?pd=video&amp;tn=vsearch&amp;word=word&amp;rsv_spt=15" class="logSend " data-logsend="{&quot;send&quot;:[&quot;general&quot;,&quot;toptablink&quot;,{&quot;to&quot;:&quot;video&quot;}]}" wdfield="word" onmousedown="setHeadUrl(this)">视频</a>
<a data-href="http://image.baidu.com" href="http://image.baidu.com/i?ct=201326592&amp;cl=2&amp;nc=1&amp;lm=-1&amp;st=-1&amp;tn=baiduimage&amp;istype=2&amp;fm=&amp;pv=&amp;z=0&amp;word=word&amp;fr=wenku" class="logSend " data-logsend="{&quot;send&quot;:[&quot;general&quot;,&quot;toptablink&quot;,{&quot;to&quot;:&quot;image&quot;}]}" wdfield="word" onmousedown="setHeadUrl(this)">图片</a>
<a data-href="http://zhidao.baidu.com" href="http://zhidao.baidu.com/q?word=word&amp;ct=17&amp;pn=0&amp;tn=ikaslist&amp;rn=10&amp;lm=0&amp;fr=wenku" class="logSend" data-logsend="{&quot;send&quot;:[&quot;general&quot;,&quot;toptablink&quot;,{&quot;to&quot;:&quot;zhidao&quot;}]}" wdfield="word" onmousedown="setHeadUrl(this)">知道</a>
<b>文库</b>
<a data-href="http://tieba.baidu.com" href="http://tieba.baidu.com/f?kw=word&amp;fr=wenku" class="logSend " data-logsend="{&quot;send&quot;:[&quot;general&quot;,&quot;toptablink&quot;,{&quot;to&quot;:&quot;tieba&quot;}]}" wdfield="kw" onmousedown="setHeadUrl(this)">贴吧</a>
<a data-href="https://b2b.baidu.com" href="https://b2b.baidu.com/s?&amp;fr=wenku&amp;key=word" class="logSend " data-logsend="{&quot;send&quot;:[&quot;general&quot;,&quot;toptablink&quot;,{&quot;to&quot;:&quot;b2b&quot;}]}" wdfield="key" onmousedown="setHeadUrl(this)">采购</a>
<a data-href="http://map.baidu.com" href="http://map.baidu.com/?newmap=1&amp;ie=utf-8&amp;s=s&amp;wd=word&amp;fr=wenku" class="logSend" data-logsend="{&quot;send&quot;:[&quot;general&quot;,&quot;toptablink&quot;,{&quot;to&quot;:&quot;map&quot;}]}" wdfield="wd" onmousedown="setHeadUrl(this)">地图</a>
<b class="wk-right-line">|</b>
</div>
</div>
<div id="vip-cms-doc-list" style="display:none;"></div>

<div id="doc" class="page" style="width: auto;">
<div id="hd">

<style type="text/css">
/*
    @require wkview:widget/down_doc/down_doc.less
    @require wkview:widget/ui/panel/panel.less
*/
</style>

<script type="text/javascript">
    (function (Data) {
        Data.set('isHitVipDocLimited', +'');
        Data.set('verticalDocType', +'0');
        var WkInfo = Data.get('WkInfo') || {};
        // RD文库阅读页异步操作重构
        WkInfo.Urls = {
            'submitPriceUpdate': '\/doc\/submit\/priceUpdate' || '/submit', // 修改标价
            'submitClassUpdate': '\/doc\/submit\/classUpdate' || '/submit', // 修改分类
            'submitValue': '\/doc\/submit\/value' || '/submit', // 评分
            'submitDownload': '\/user\/submit\/download' || '/submit', // 下载
            'submitCollect': '\/user\/submit\/collect' || '/submit', // 收藏
            'interfaceGetFoldSon': '\/user\/interface\/getFoldSon' || '/roomasync', // 获取文件夹结构
            'interfaceGetViewFoldInfo': '\/user\/interface\/getViewFoldInfo' || '/roomasync', // 外链的文件夹结构
            'submitFoldCreate': '\/user\/submit\/foldCreate' || '/roomasync', // 文件夹创建
            'submitDocMove': '\/user\/submit\/docMove' || '/roomasync', // 移动
            'submitBookmark': '\/user\/submit\/bookmark' || '/submit', // 书签
            'interfaceGetRepeatDown': '\/user\/interface\/getRepeatDown' || '/async'//重复文档检查
        };
        WkInfo.transType = JSON.parse('[]');
        WkInfo.DocInfo = {
            'player': 'html',
            'creater': '%CE%C4%BF%E2%D0%C2%C8%CB', // 贡献者
            'createUserId': '2467037678',
            'commentStar': '', // 文档已评论的星级
            'isPayDocAndCommented': '0', // 文档是否已经评论（付费文档）
            'title': '涉密计算机管理制度', // 文档标题
            'docId': 'e167fbacae45b307e87101f69e3143323968f5cc', // 文档id
            'editorDocId': '', // html编辑器docid
            'docType': 'doc', // 文档格式
            'docTypeNum': '4', // 文档格式号
            'flag': '25',
            'can_dump': '1', // 文档是否可以转存网盘	
            'cats': '3-63-162-0' || '0-0-0-0', // 文档分类
            'cid1': '3', // 文档分类
            'cid2': '63', // 文档分类
            'cid3': '162', // 文档分类
            'cid4': '0', // 文档分类
            'price': '5', // 文档价格
            'size': '19851', // 文档价格
            'rateNum': '0', // 文档评分
            'totalPageNum': '6', // 文档评分
            'catal': '0',
            'relateDoc': '0',
            'otherLikeDoc': '0',
            'relateAlblum': '0',
            'sameSeriesDoc': '4',
            'isInRoom': '0',
            'freeDoc': '',
            'freeMoney': '',
            'readerType': 'xreader',
            'payPrice': +'0', // 文档价格
            'isPaymentDoc': +'0', // 是否为付费文档
            'freepagenum': +'', // 免费阅读页数
            'ispaied': +'', // 是否已经购买
            'writername': '', // 付费文档作者名称
            'isdownloaded': +'', // 是否允许下载
            'isPrivate': !!'', // 是否为私有文档
            'vip_free_buy': +'0',
            'is_vip_free_doc': +'0',
            'is_only_vip_doc': +'',
            'vip_price': + '',
            'vip_type': +'0',
            // tianzheng 教育会员 明哲让我加的
            'is_edu_doc': +'',
            'edu_vip_type': +'0',
            'jiaoyu_vip_type': +'0',
            'docTicket':+'2',
            'JOINVIP_URL': '/vip/privilege',
            'is_discount_doc': +'0',
            'isInRoomButDeletedByCreater':!!'', // 
            'goodsPayStatus': 'notPaymentDoc',
            'price_supported_devices_info': '',
            'confirm_price': +'',
            'wk2yd': '0',
            'docDesc': '',
            'hasImage': '' || 0,
            // 机构文档第二篇打折，必须数据
            'org_discount_status':+'-1',
            'org_discount_price':'',
            'org_title':'',
            'org_engName': '' || '',
            'isOrgDoc': '0' || 0,
            'is_exam_link': '0',
            'professionalDoc': '', // VIP专享文档
            'isRepeatDown': +'', // 付费文档是否已下载
            'isPickDoc': +'0', // 收纳文档
            'readerVersion': (function () {
                var version = '3';
                if (version != 1 && version != 2 && version != 3) {
                    version = 1;
                }
                return version;
            })(),
            'isPartnerDoc': +'' || 0,
            // 行业报告定制
            'hangyebaogao_customized': +'' || 0,
            'vipHuixueConvert': {
                is_open: +'1'
            }
        };

        WkInfo.PaceInfo = {
            'rate': '30'
        };
        // 小流量下掉阅读页猜你喜欢广告位
        var randomNum = Math.random();
        WkInfo.WkAdInfo = {
            'blockStatus': +'',
            'offAdSmallFlow': randomNum
        };
        WkInfo.smallFlowContent = {
            'not_hit_dump_doc': '0'
        };
        if (WkInfo.VipInfo) {
            WkInfo.VipInfo.flag = '0';
            WkInfo.VipInfo.professionalDocDownloadTicket = '';
        }
        else {
            WkInfo.VipInfo = {
                'flag': '0', // 专业会员
                'professionalDocDownloadTicket': '' // 专业特权
            }
        }
        if (WkInfo.UserInfo) {
            WkInfo.UserInfo.smallFlowProfessionalDoc = '1'; // VIP专享文档小流量
            WkInfo.UserInfo.isBGC = '0';
            WkInfo.UserInfo.isLogin = '1';
            WkInfo.UserInfo.sf_svip = '2111'; // 会员升级小流量
        }
        else {
            WkInfo.UserInfo = {
                'smallFlowProfessionalDoc': '1', // VIP专享文档小流量
                'sf_svip': '2111' // 会员升级小流量
            }
        }
        WkInfo.docType = {
            '0': '',
            '1': 'doc',
            '2': 'xls',
            '3': 'ppt',
            '4': 'docx',
            '5': 'xlsx',
            '6': 'pptx',
            '7': 'pdf',
            '8': 'txt',
            '9': 'wps',
            '10': 'et',
            '11': 'dps',
            '12': 'vsd',
            '13': 'rtf',
            '14': 'pot',
            '15': 'pps',
            '16': 'epub'
        };

        // 协同推荐数据，暂时供下载后推荐使用
        WkInfo.otherLikeDocRec = [];

        
        // 判断是否使用Bcs请求的地址
        WkInfo.htmlBcs = +'1';
        // htmlBcs迁移请求地址
        WkInfo.htmlUrls = '{\x22ttf\x22:[{\x22pageIndex\x22:1,\x22param\x22:\x22&md5sum=eca395b49edb00ad238df924ac49504b&range=0-100457&sign=190fc0dc96\x22},{\x22pageIndex\x22:2,\x22param\x22:\x22&md5sum=eca395b49edb00ad238df924ac49504b&range=100458-204795&sign=190fc0dc96\x22},{\x22pageIndex\x22:3,\x22param\x22:\x22&md5sum=eca395b49edb00ad238df924ac49504b&range=204796-282690&sign=190fc0dc96\x22},{\x22pageIndex\x22:4,\x22param\x22:\x22&md5sum=eca395b49edb00ad238df924ac49504b&range=282691-356753&sign=190fc0dc96\x22},{\x22pageIndex\x22:5,\x22param\x22:\x22&md5sum=eca395b49edb00ad238df924ac49504b&range=356754-425667&sign=190fc0dc96\x22},{\x22pageIndex\x22:6,\x22param\x22:\x22&md5sum=eca395b49edb00ad238df924ac49504b&range=425668-&sign=190fc0dc96\x22}],\x22json\x22:[{\x22pageIndex\x22:1,\x22pageLoadUrl\x22:\x22https:\\\/\\\/wkbjcloudbos.bdimg.com\\\/v1\\\/docconvert9104\\\/wk\\\/eca395b49edb00ad238df924ac49504b\\\/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sun%2C%2001%20Dec%202019%2011%3A40%3A57%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2019-10-17T03%3A40%3A57Z%2F3600%2Fhost%2Fbbb7a797ea9bd57341c0bfb9f5bda00bccccf02884007c3017b7f78c09b823ae&x-bce-range=0-11751&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3MTI4NzI1NywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.CHWLp%2ByjGlvs%2B%2BplswsZsr96EwzBAqOwKSXtR%2Bi9O0o%3D.1571287257\x22},{\x22pageIndex\x22:2,\x22pageLoadUrl\x22:\x22https:\\\/\\\/wkbjcloudbos.bdimg.com\\\/v1\\\/docconvert9104\\\/wk\\\/eca395b49edb00ad238df924ac49504b\\\/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sun%2C%2001%20Dec%202019%2011%3A40%3A57%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2019-10-17T03%3A40%3A57Z%2F3600%2Fhost%2Fbbb7a797ea9bd57341c0bfb9f5bda00bccccf02884007c3017b7f78c09b823ae&x-bce-range=11752-24038&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3MTI4NzI1NywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.dGde%2FJCzJmFsQ%2BCqoqmkPgTs3UffdV3AKJHjsnXLfxc%3D.1571287257\x22},{\x22pageIndex\x22:3,\x22pageLoadUrl\x22:\x22https:\\\/\\\/wkbjcloudbos.bdimg.com\\\/v1\\\/docconvert9104\\\/wk\\\/eca395b49edb00ad238df924ac49504b\\\/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sun%2C%2001%20Dec%202019%2011%3A40%3A57%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2019-10-17T03%3A40%3A57Z%2F3600%2Fhost%2Fbbb7a797ea9bd57341c0bfb9f5bda00bccccf02884007c3017b7f78c09b823ae&x-bce-range=24039-35817&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3MTI4NzI1NywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.Y15n1bl94dzoN4io3%2BmF3LAuBfBBRUTIbyUxYYe3MeE%3D.1571287257\x22},{\x22pageIndex\x22:4,\x22pageLoadUrl\x22:\x22https:\\\/\\\/wkbjcloudbos.bdimg.com\\\/v1\\\/docconvert9104\\\/wk\\\/eca395b49edb00ad238df924ac49504b\\\/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sun%2C%2001%20Dec%202019%2011%3A40%3A57%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2019-10-17T03%3A40%3A57Z%2F3600%2Fhost%2Fbbb7a797ea9bd57341c0bfb9f5bda00bccccf02884007c3017b7f78c09b823ae&x-bce-range=35818-47363&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3MTI4NzI1NywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.l9kcUkNhUbpAeuFLp7lquY%2Fogs0fQ5Hr0FkMO2ew0is%3D.1571287257\x22},{\x22pageIndex\x22:5,\x22pageLoadUrl\x22:\x22https:\\\/\\\/wkbjcloudbos.bdimg.com\\\/v1\\\/docconvert9104\\\/wk\\\/eca395b49edb00ad238df924ac49504b\\\/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sun%2C%2001%20Dec%202019%2011%3A40%3A57%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2019-10-17T03%3A40%3A57Z%2F3600%2Fhost%2Fbbb7a797ea9bd57341c0bfb9f5bda00bccccf02884007c3017b7f78c09b823ae&x-bce-range=47364-59116&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3MTI4NzI1NywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.4lFOwf84AdKqXUtgaL%2BRjNPMt1YZdSD4fLH226W%2BQtg%3D.1571287257\x22},{\x22pageIndex\x22:6,\x22pageLoadUrl\x22:\x22https:\\\/\\\/wkbjcloudbos.bdimg.com\\\/v1\\\/docconvert9104\\\/wk\\\/eca395b49edb00ad238df924ac49504b\\\/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sun%2C%2001%20Dec%202019%2011%3A40%3A57%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2019-10-17T03%3A40%3A57Z%2F3600%2Fhost%2Fbbb7a797ea9bd57341c0bfb9f5bda00bccccf02884007c3017b7f78c09b823ae&x-bce-range=59117-&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3MTI4NzI1NywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.P3D3EdyH9n0FVmcRsGS3r7%2F%2BojkcmM%2FvopEiKIbz6g8%3D.1571287257\x22}],\x22png\x22:[]}';
        WkInfo.verify_user_info ='';
        WkInfo.isUgcTest = Boolean('');
        WkInfo.isRealName = +('1' + '0' + '0');
        WkInfo.is_tianyancha_doc ='';
        WkInfo.OrgInfo = {
            'uid': ''
        };
        Data.set('WkInfo', WkInfo);
        +'1724948680' && Data.set('userFlowGroup', +'1');
        Data.set('mitidialogtitle', '');
        Data.set('mitidialogfontsize', '');
        Data.set('isDialogCashier', '');
        Data.set('isBGC', '0');
    })(window.__fisData);
</script>
<div class="header-wrap">

<div class="box top-search-box  " style="width: 1200px;">
<div class="media media-new-150">

<a href="/?fr=logo" alog-action="wk.logo">
<span class="wk-logo-icon"></span>
</a>
</div>
<span id="h-hide" style="display: none;"></span>
<div class="content" id="adbg">
<div class="s_nav s_nav-new">
</div>

</div>
<a class="page-banner page-banner-new log-xsend" id="banurl" data-logxsend="[1, 101282, {index: 4}]" href="https://eduad.baidu.com/click/wenku_post_json?p=eZqDpQFRaaIX9lcjfAotSXFhjYMiKaBF3nrSRQF9dn8RBdiFNJ9OP99lJC8KCrjrmGVgxxRD7voBMthTpjEhunG0hqkcPb-sHnHwNZ5A5YSFj-bgUBfSvFm2pA1cU8ZmDHe_rzgspAr_LqN1DvJ9t1FRsheeLleUr7la8SM4UCFZPomkJZmSRp78oH9jFC3fWAAni9UF0LVkFjuI2e_wCNH5gQ9fYyWOzo0LNGrwLJNa-wQoEPH2jE2rr_He7ip0RV9CLfEghU2y0DWCf8tQgA0urM9XUsC__Ytm-0K3CH0TDOcdxqW9n_DXQmfLjYaPCWHz6CORDDhN5pdJOBrE3GhIeaKCqrcOfpdnVp7H1tUBz2-6MNWQyQyzxyS5ObBY2mkUXw3m30iMTI9TGCyMyf9ojRuMz7AhIY-JC5Q27ffbkeU_eLs0Fp1ycB6SUlJFXwgfIaQqgs0qWqK85ga-s6cp9jrSGcCWVp2wVkhLqGNUN8ck3HMVr6wdUE4Uh0MllUtJcN3C-jHRp5xmpibJG9mHD9Wwy99XxPjW3SkY9tjw26Ol6xZBhNWS7SfGGg24B_1FKJ4bz4RNc1bsJg6aIZh49ct0UqkPX4jfNSyn28NkUW0TEcaLML9nwothejPWRTLAATB6XQk7llqicpgzpltEGznO_FseTybq3ZJX0Vu8HOTyWccIVdlcFpppK62wg_uyN9VqIgBut9lQOI2owThgQVkmGsi_Qfymki5USL-a0EGTaKaC6pxiV8O-xlPINsN-Xv-3DiqNHnKs8H_Bpg==&amp;price=0&amp;lp=s0Bgih9A2IsIk-pRbTJmSCRQCMEb7cb_qZIVXRbMtO8aVvYzxfDt-zwT1ruw2zVM" target="_blank" style="background: url(&quot;https://edu-ad-test-cdn.cdn.bcebos.com/bec594a22894adf72160369c5195409b/ff8e9b91778929181a5254810988aaf4.png&quot;) right center no-repeat;"></a>
</div>
<div class="nav-wrap mb10">
<div class="ui-nav">
<div class="inner clearfix">
<ul class="clearfix main-nav" alog-group="general.nav">
<li id="nav-index"><a href="/?fr=nav">首页</a></li>
<li id="zone-menu"><a href="javascript:void(0);">分类</a><b class="d-ic"></b></li>
<li id="jingpin-menu">
<a href="javascript:void(0);">精品内容</a>
<b class="verify-d-ic"></b>
<div class="drop-sub-nav" id="drop-sub-nav">
<a target="_blank" href="//wenku.baidu.com/edu" class="log-xsend" data-logxsend="[1, 101246]">教育文库</a>
<a target="_blank" class="log-xsend" data-logxsend="[1, 101214]" href="//wenku.baidu.com/video/browse/category">文库视频</a>
<a target="_blank" href="//tiku.baidu.com/" data-logxsend="[1, 100761]" class="log-xsend">百度题库</a>
<a target="_blank" class="log-xsend" data-logxsend="[1, 100799]" href="/jingpin">精品文库</a>
<a target="_blank" href="/org/zone?zoneid=2" class="log-xsend" data-logxsend="[1, 101247]">学术专区</a>
<a target="_blank" href="//wenku.baidu.com/ndbgc/org/legal?fr=syjp">法律专区</a>
<a target="_blank" href="/org/browse/meeting" class="log-xsend" data-logxsend="[1, 101248]">会议中心</a>
</div>
</li>
<li id="nav-edu">
<a href="//wenku.baidu.com/wenkuverify?from=1" target="_blank" class="log-xsend" data-logxsend="[1, 101253]">申请认证<span class="ui-bz-hot-ic" style="position: absolute; top: 2px;"></span></a>
</li>
<li class="" id="jghz-menu">
<a href="javascript:void(0);" style="cursor:default;">机构合作</a>
<b class="verify-d-ic"></b>
<div class="drop-sub-nav" id="jghz-drop-sub-nav">
<a target="_blank" href="/org/index">机构认证</a>
<a target="_blank" href="https://eduai.baidu.com/intro">教育云平台</a>
<a target="_blank" href="https://jiaoyu.baidu.com/topic/bsplatform/tob_doc?fr=home">品牌推广</a>
<a target="_blank" href="https://jiaoyu.baidu.com/topic/bsplatform/technical_cooperation" data-logxsend="[1, 100841]" class="log-xsend">技术服务</a>
<a target="_blank" href="https://jiaoyu.baidu.com/topic/bsplatform/agentrecruitment" data-logxsend="[1, 100958]" class="log-xsend">代理招募</a>
</div>
</li>
<li class="last" id="channel-menu">
<a href="javascript:void(0);" style="cursor:default;">频道专区</a>
<b class="verify-d-ic"></b>
<div class="drop-sub-nav" id="channel-drop-sub-nav">

<a target="_blank" href="https://wenku.baidu.com/activity/browse/fitmentsubject?ch=yezhifengfitment" data-logxsend="[1, 101542,{page: &quot;yezhifengfitment&quot;}]" class="log-xsend">环保家装</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/ylbuild?ch=youlubuild" data-logxsend="[1, 101542,{page: &quot;youlubuild&quot;}]" class="log-xsend">一级建造师</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/ciscosubject?ch=ciscosubject" data-logxsend="[1, 101542,{page: &quot;ciscosubject&quot;}]" class="log-xsend">企业IT技术</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/xiongdilian?ch=itxiongdiliansubject" data-logxsend="[1, 101542,{page: &quot;itxiongdiliansubject&quot;}]" class="log-xsend">IT培训</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/ylfire?ch=youlufire" data-logxsend="[1, 101542,{page: &quot;youlufire&quot;}]" class="log-xsend">消防工程师</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/channelsubject?ch=1810monalisa" data-logxsend="[1, 101542,{page: &quot;1810monalisa&quot;}]" class="log-xsend">瓷砖选材</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/sapsubject?ch=sapsubject" data-logxsend="[1, 101542,{page: &quot;sapsubject&quot;}]" class="log-xsend">企业应用软件</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/channelsubject?ch=1810meeting" data-logxsend="[1, 101542,{page: &quot;1810meeting&quot;}]" class="log-xsend">会议平台</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/hudun?ch=hudunsubject" data-logxsend="[1, 101542,{page: &quot;hudunsubject&quot;}]" class="log-xsend">PDF转换</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/yunxuepc?ch=yunxuepc" data-logxsend="[1, 101542,{page: &quot;yunxuepc&quot;}]" class="log-xsend">心理咨询师</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/yunxuerd?ch=yunxuerd" data-logxsend="[1, 101542,{page: &quot;yunxuerd&quot;}]" class="log-xsend">营养师</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/ylyaoshi?ch=ylyaoshi" data-logxsend="[1, 101542,{page: &quot;ylyaoshi&quot;}]" class="log-xsend">执业药师</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/schoolsubject?ch=jdxxwschool" data-logxsend="[1, 101542,{page: &quot;jdxxwschool&quot;}]" class="log-xsend">中高考学习</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/yljiankang?ch=yljiankang" data-logxsend="[1, 101542,{page: &quot;yljiankang&quot;}]" class="log-xsend">健康管理师</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/jingjishi?ch=jingjishi" data-logxsend="[1, 101542,{page: &quot;jingjishi&quot;}]" class="log-xsend">经济师</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/bim?ch=bim" data-logxsend="[1, 101542,{page: &quot;bim&quot;}]" class="log-xsend">BIM工程师</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/yasisubject?ch=yasisubject" data-logxsend="[1, 101542,{page: &quot;yasisubject&quot;}]" class="log-xsend">雅思考试</a>
<a target="_blank" href="https://wenku.baidu.com/activity/browse/tuofusubject?ch=tuofusubject" data-logxsend="[1, 101542,{page: &quot;tuofusubject&quot;}]" class="log-xsend">托福考试</a>
<a target="_blank" href="https://wenku.baidu.com/ndbgc/channel/happybox?ch=happybox" data-logxsend="[1, 101542,{page: &quot;happybox&quot;}]" class="log-xsend">数据恢复</a>
</div>
</li>
</ul>
<ul class="main-nav side-nav clearfix">
<li style="width: 122px;">
<a href="/user/browse/vip/" style="width: 120px;" target="_blank" class=" wkmember-li-top">
<b class="n-ic wkmember-ic iconfont"></b>
<b class="havenew-ic" style=""></b>
会员中心</a>
<b class="verify-d-ic" style="left: auto; right: 10px;"></b>
<div class="drop-sub-nav member-sub-nav" id="drop-sub-nav">
<a target="_blank" href="/user/browse/newvipfreedoczone" data-logxsend="[1, 100831]" class="log-xsend">
VIP免费专区</a>
<a target="_blank" href="/user/browse/annualvip" data-logxsend="[1, 100592]" class="log-xsend">
VIP福利专区</a>
<a target="_blank" href="/duihuan">兑换VIP</a>
</div>
</li>
<li class="last">
<a href="/user/mydocs?fr=nav" id="nav-myWenku" class="logSend" data-logsend="{&quot;send&quot;:[&quot;general&quot;,&quot;usercenter&quot;,{&quot;refer&quot;:&quot;navigator&quot;}]}"><b class="n-ic mywk-ic"></b>个人中心</a>
<b class="verify-d-ic" id="mark-arrow"></b>
<div class="drop-sub-nav" id="reward-task">
<a href="/user/browse/knowledgecenter" target="_blank">云知识</a>
<a target="_blank" href="/task/browse/rewardlist">悬赏任务</a>
<a target="_blank" href="/task/browse/daily">每日任务</a>
<a class="" target="_blank" href="/wenkuverify?from=2">专业认证</a>
<a href="//jianli.baidu.com" target="_blank">我的简历</a>
</div>
</li>
</ul>
<div class="cate hide" id="wk-all-cate">
<dl>
<dt><b class="t-tag cg"></b><a href="/portal/browse/zoneedu" target="_blank">教育频道<b class="li-aw n-ic"></b></a></dt>
<dd>
<a href="https://wenku.baidu.com/edu" target="_blank" class="log-xsend" data-logxsend="[1, 100647, {index:1}]">中小学教案</a>
<a href="http://gaokao.baidu.com/?&amp;channel=pc6" target="_blank" class="log-xsend" data-logxsend="[1, 100647, {index:2}]">高考题库</a>
<a href="https://wenku.baidu.com/portal/composition/ks" target="_blank" class="log-xsend" data-logxsend="[1, 100647, {index:3}]">作文库</a>
</dd>
</dl>
<dl>
<dt><b class="t-tag cc"></b><a href="/pro/index" target="_blank">专业资料<b class="li-aw n-ic"></b></a></dt>
<dd>
<a href="//wenku.baidu.com/ndbgc/org/legal?fr=syzy" target="_blank">合同范本</a>
<a href="/list/63" target="_blank">IT/计算机</a>
<a href="/list/230" target="_blank">工程科技</a>
</dd>
</dl>
<dl class="home-left-third">
<dt><b class="t-tag cg"></b><a href="/form/index" target="_blank">实用文档<b class="li-aw n-ic"></b></a></dt>
<dd>
<a href="/list/71" target="_blank">求职/职场</a>
<a href="/list/77" target="_blank">总结/汇报</a>
<a href="/list/73" target="_blank">党团工作</a>
</dd>
</dl><dl class="tob-home-left"><dt><b class="t-tag cg"></b><a href="/pgc/browse/exam" target="_blank">资格考试<b class="li-aw n-ic"></b></a></dt><dd><a href="https://wenku.baidu.com/activity/browse/xiongdilian?ch=itxiongdiliansubject" style="position:relative;" target="_blank">IT培训<span class="ui-bz-0-ic" style="position: absolute;top: -11px;right: -20px;"></span></a><a href="https://wenku.baidu.com/activity/browse/yunxuepc?ch=yunxuepc" style="position:relative;" target="_blank">心理师<span class="ui-bz-0-ic" style="position: absolute;top: -11px;right: -20px;"></span></a><a href="https://wenku.baidu.com/activity/browse/yunxuerd?ch=yunxuerd" style="position:relative;" target="_blank">营养师<span class="ui-bz-0-ic" style="position: absolute;top: -11px;right: -20px;"></span></a><a href="https://wenku.baidu.com/activity/browse/yasisubject?ch=yasisubject" style="position:relative;" target="_blank">雅思<span class="ui-bz-0-ic" style="position: absolute;top: -11px;right: -20px;"></span></a><a href="https://wenku.baidu.com/activity/browse/tuofusubject?ch=tuofusubject" style="position:relative;" target="_blank">托福<span class="ui-bz-0-ic" style="position: absolute;top: -11px;right: -20px;"></span></a></dd></dl><dl class="tob-home-left last"><dt><b class="t-tag cg"></b><a href="/life/index" target="_blank">专业方案<b class="li-aw n-ic"></b></a></dt><dd><a href="https://wenku.baidu.com/activity/browse/fitmentsubject?ch=yezhifengfitment&amp;adredirectfr=https%3A%2F%2Fwenku.baidu.com%2F" style="position:relative;" target="_blank">环保家装<span class="ui-bz-0-ic" style="position: absolute;top: -11px;right: -20px;"></span></a><a href="https://wenku.baidu.com/activity/browse/ciscosubject?ch=ciscosubject" style="position:relative;" target="_blank">企业IT技术<span class="ui-bz-0-ic" style="position: absolute;top: -11px;right: -20px;"></span></a><a href="https://wenku.baidu.com/activity/browse/channelsubject?ch=1810monalisa" style="position:relative;" target="_blank"> 瓷砖选材<span class="ui-bz-0-ic" style="position: absolute;top: -11px;right: -20px;"></span></a><a href="https://wenku.baidu.com/activity/browse/channelsubject?ch=1811magiceras" style="position:relative;" target="_blank">少儿英语<span class="ui-bz-0-ic" style="position: absolute;top: -11px;right: -20px;"></span></a><a href="https://wenku.baidu.com/activity/browse/channelsubject?ch=1810meeting" style="position:relative;" target="_blank">会议平台<span class="ui-bz-0-ic" style="position: absolute;top: -11px;right: -20px;"></span></a><a href="https://wenku.baidu.com/activity/browse/qiaowaisubject?ch=qiaowaisubject" style="position:relative;" target="_blank">出国移民<span class="ui-bz-0-ic" style="position: absolute;top: -11px;right: -20px;"></span></a></dd></dl>
</div>
</div>
</div>
</div>
</div>
</div>
<div id="bd">
<div class="bd-wrap" style="min-width: 1126px;">

<div id="fc-left" class="fc-left ec-result3" style="display: none">
<a id="fc-click" class="log-xsend" data-logxsend="[1, 102036, {index: 2}]" target="_blank" href="" datasign="">
<div class="click-content" style="height: 320px;">
<img src="" alt="测试" width="80" height="80">
<div class="content"></div>
<div class="logo"></div>
</div>
</a>
<div class="remove">
<span class="vip">VIP去广告</span>
<span class="close">X</span>
</div>
</div>
<div class="body body-v3" style="width: 1126px;">

<div class="crubms-wrap">
<div id="page-curmbs" class="crumbs ui-crumbs mb10">
<ul alog-group="general.curmbs">
<li><a target="_blank" href="//wenku.baidu.com?fr=crumbs" class="logSend" data-logsend="{&quot;send&quot;:[&quot;general&quot;,&quot;crumb1&quot;]}">百度文库</a></li>
<li><a href="/pro/index" class="logSend" data-logsend="{&quot;send&quot;:[&quot;general&quot;,&quot;crumb2&quot;]}">专业资料</a></li>
<li><a href="/list/63" class="logSend" data-logsend="{&quot;send&quot;:[&quot;general&quot;,&quot;crumb3&quot;]}">IT/计算机</a></li>
<li class="current logSend"><a href="/list/162" data-logsend="{&quot;send&quot;:[&quot;general&quot;,&quot;crumb4&quot;]}">计算机硬件及网络</a></li>
</ul>
</div>
</div>


<div class="main">


<script>
    if (typeof PDC !== 'undefined') {
        PDC.view_start();
    }
</script>
<div class="mod doc-main " id="doc-main" style="width: 890px;">
<b class="top"><b class="tl"></b><b class="tr"></b></b>
<div class="inner">

 <div id="doc-header-test" class="hd doc-header no-doc-desc">
<div class="top-ads-banner-wrap super-vip">
<a href="javascript:;" class="top-ads-container top-ads-banner-goto-cashier log-xsend" data-logxsend="[1, 100017]" data-href="/cashier/browse/vipcashier?dqStatCode=31_8_9_10&amp;id=">
<p class="left-image svip-icon"></p>
<div class="right-info">
<p class="right-first-para">加入文库VIP &gt;</p>
<p class="right-second-para">获取下载特权</p>
</div>
</a>
</div><h1 class="reader_ab_test with-top-banner">
<b class="ic ic-doc"></b><span id="doc-tittle-0">涉<wbr>密<wbr>计<wbr>算<wbr>机<wbr>管<wbr>理<wbr>制<wbr>度<wbr></span>
</h1>
<div class="doc-value" style="overflow: visible;">
<span class="author">
<span class="ic ic-user"></span>
<a target="_blank" class="user log-xsend " data-logxsend="[1,100593]" href="/u/文库新人?from=wenku">岑影s
</a>
<i>|</i><em class="date">2019-09-02</em>
</span>
<i>|</i>
<span id="doc-info-0"><b class="bannerScore"></b><span class="high-quality">4.0分</span><span>(高于<span class="high-quality">74.24</span>%的文档)</span><i>|</i><span class="ic ic-read-num"></span>46<i>|</i><span class="ic ic-down-num"></span>0</span>
<a id="docReport-0" title="举报违规文档" class="report" href="###" data-has-report="0"><i>|</i>
<b class="ic ic-report mr5"></b>
<span>举报</span>
</a>
<div class="qrHover">&nbsp;&nbsp;&nbsp;<div class="wrap"><div class="qrcode" title="https://wk.baidu.com/topic/nadownload?refer=1020999h&amp;deeplink=1&amp;docid=e167fbacae45b307e87101f69e3143323968f5cc"><canvas width="90" height="90" style="display: none;"></canvas><img alt="Scan me!" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFoAAABaCAYAAAA4qEECAAAGXElEQVR4Xu2d25KjQAxDk///6GxlM5lqGls6bsilpryvC00jZFkySeZ6uVxul8V/t9v21Ov1ulvpeczz/+ZzxhOyY9S58zXV+s9rzetF+34eO+9/EarLHZkGOiDIy4AmTKCMiNZybL2vnVVIZb2IcRnrSaVUKnK+9njdX0Y30FuYMnlZwem+8g7oTK/GCzh2Vo6NGEhupgLEkWOzKv4PXiI5ka430NOTXiHRTJaXAU26OGFppnHEqajmlZ1/VKPfzugGekuRlzFaddsjPnTFp8/MHrW0shfigN7O6AZ6gdEk+TipiFxHxDR3rTNSX5Q8s+al9kOS7Ud99ApYs6WqPCTS4BroxGr9KaBdGatgoaQki7AR81ywGKvjU+uu4LRJhisLuJu9r+mOUSnyGx/gCk7/gb6tJAlztcrY8ay4XtHmF9yyxb+BthCdcwCeRyvLpppVxQpmbqPSH9QaJIRkFi0KOyVZpIP/BvrxfmS5IWdAq/ibRVkVcbOnrwKFOmelUma2VyJ5VLXuhcLm3hrofK6sJGtmd+SwNkA/XYeLmJGTcBo1XpzoL2F9RUNnFq6kVGIxSbv8dR0NdAxXA/2Di9NqVdLET58GtNNox/RRq6KNV2a2rjmRcBPx0kX71YacNddwDw30FhbnJBSZVIUsJUNSrvNTJW9LVPDJPGzWiCK/Sxqy27eqGNV8G2hjGSo6LoF+SseKtSIBoBJu3LFKSxUTsz5TGdUSC6eqNv1cB3mSDfQWfgQ0eWL0GNkUxAcKs9JzbmS0cBUNVfdzRh/aVCAdKlGQqzcdrUsSZ6VpnZ0IMywkwWagj+gkYTIZVpGHumLDiO91TCZePtT+Bjr20YRwpSbbQL8J6PmdoYvMc3CINFkNx4ksZPp71rpkbl7ZJ+kBu8DSQNe/aVIC2unN+ISzhrY6B3BNqhIsVvw/cT6K4dk1xwdg59Fq4O8AGmWGAOAetur4ZMo4g5VV7yiH6pjZ96v1D0kH8bsOYPUgFXikXB2wkVY7t6GGVYp4DbR5s52lVRXMpI+uMI8w2SU3UrYkImdAkGAxMzCSjJXxbgM9fdP3I0CrEpnLZCWmZo2DDOjPivaVxlZprqRf7D4S5ppB5CTUhdwmGuhpnEmsVcTaBvqBSvohx5UpW8Vzk4hLGhGZVTvZqpBIhRvpo91bcNUwnE+NLBDRSQfMeN0/B/R4c65REDCdnRx7gUpgLk0qBrr7iPpRtB5ahzK6gc6HTQjolTFpJhmV8SMZFEWylQUh4nyyoKVIVFl33u9G+xvo7aNbyQhkmrmb3lHGjI2OaHK2LtG8yuCJ7GWF2coUkGs20MFPDKkmGAUsBPT8SaUVy6Y88UopZusRv0tePqjmRUBz1RmtYX9TiYSQBtr/LF0DPbHkY4xWFuvsiFwpSRJ4iD2M0iupUGUGQvlyGt1Ax/avDDT9LjgZZ6q4m5l5UqqqwbkqqCRacqzCQVZCAx3DQ2YoJflynyYl0zESAIhtfB6T3QDxsOrNNtkDSXlknd0xDfQWkq8C2jGOaKpinnsrEyW3yvCnElhIRc+VKAOLS2OkCRy9AfK+kjbVoymSgJc1YpQMiQtQ3ZW6AHWdTPMr55A9qmZGqirTauSjG+gHfA10QtWKljp38xagK+WQ6WWEhZvi3c+pdHxXeZFGZwAr21gZM8x4bAKQi+CqwTXQDwTIw7Bf6IyAdvp1NFhk6xPmOaaPwFRcEmmuyqk00OYNSwVgCTSddagLVsKCkhun40p3SYMjHrwyTnD73Wh0A81+Ym21wf8+XDfrUEwmwcIxhIxfzxoUkYncfL9q/xmjZWA5Q4vI/EJ1aGfvKmOA8X4qD/vlQJdmqz8f6SXnHGFR5ukjUpwVp52j2uiuwWFcy76cJdpEGiXxmq6hkVmH2q9b//7/DbT4Sz5RaIiY91VAZ6xZHTsqOzczyLG+sgcSmpQEkeCjfPP88E/5E05HYjpxHRETXcf/00CT0pwZXmlsEcsqUzvnasYKI42eBKCdj3YbJmXbQO9/Y/ptQFe6uGPICsuIDocBw/wJvcihKKKdqtFKS1fY7oIGsZVfC7Ta/ArjXGCpSBIBTbIKBC1XgZVR7ebe3OBfBQDCuAb6gSD+qxUVNpGqIJFZNejs/Ir/JXKmRqHExeyaIQFnPsY5FbVmA11AvIGOP+kfkegfRMyIH+aYcrMAAAAASUVORK5CYII=" style="display: block;"></div><div class="qr-title">马上扫一扫<div class="qr-text">手机打开<br>随时查看</div></div></div><span class="guide-to-app iconfont"><span style="font-size:12px;color:#666;">手机打开</span></span></div></div>
<div class="doc-desc-wrap" style="width: 890px;">
</div>
<hr>
</div>
<div class="bd doc-reader" style="position: relative" oncopy="return false">
<div class="doc-tag-wrap super-vip fixed" style="visibility: visible;">
<div class="doc-tag doc-tag-professional">
<i class="triangle-left"></i>
<span>VIP专享文档</span>
<div class="triangle-wrap">
<i class="top-triangle"></i>
<i class="bottom-triangle"></i>
</div>
<div class="tag-info">
<i class="triangle-icon"></i>
VIP专享文档是百度文库认证用户/机构上传的专业性文档，文库VIP用户或购买VIP专享文档下载特权礼包的其他会员用户可用VIP专享文档下载特权免费下载VIP专享文档。只要带有以下“VIP专享文档”标识的文档便是该类文档。<a href="/portal/browse/help#help/29">了解文档类型</a>
</div>
</div>
<div class="doc-tag doc-tag-vip-free">
<i class="triangle-left"></i>
<span>VIP免费文档</span>
<div class="triangle-wrap">
<i class="top-triangle"></i>
<i class="bottom-triangle"></i>
</div>
<div class="tag-info">
<i class="triangle-icon"></i>
VIP免费文档是特定的一类共享文档，会员用户可以免费随意获取，非会员用户需要消耗下载券/积分获取。只要带有以下“VIP免费文档”标识的文档便是该类文档。<a href="/portal/browse/help#help/29">了解文档类型</a>
</div>
</div>
<div class="doc-tag doc-tag-pay-discount">
<i class="triangle-left"></i>
<span>VIP尊享8折文档</span>
<div class="triangle-wrap">
<i class="top-triangle"></i>
<i class="bottom-triangle"></i>
</div>
<div class="tag-info">
<i class="triangle-icon"></i>
VIP专享8折文档是特定的一类付费文档，会员用户可以通过设定价的8折获取，非会员用户需要原价获取。只要带有以下“VIP专享8折优惠”标识的文档便是该类文档。<a href="/portal/browse/help#help/29">了解文档类型</a>
</div>
</div>
<div class="doc-tag doc-tag-pay-normal">
<i class="triangle-left"></i>
<span>付费文档</span>
<div class="triangle-wrap">
<i class="top-triangle"></i>
<i class="bottom-triangle"></i>
</div>
<div class="tag-info">
<i class="triangle-icon"></i>
付费文档是百度文库认证用户/机构上传的专业性文档，需要文库用户支付人民币获取，具体价格由上传人自由设定。只要带有以下“付费文档”标识的文档便是该类文档。<a href="/portal/browse/help#help/29">了解文档类型</a>
</div>
</div>
<div class="doc-tag doc-tag-ticket" style="display: block;">
<i class="triangle-left"></i>
<span>共享文档</span>
<div class="triangle-wrap">
<i class="top-triangle"></i>
<i class="bottom-triangle"></i>
</div>
<div class="tag-info">
<i class="triangle-icon"></i>
共享文档是百度文库用户免费上传的可与其他用户免费共享的文档，具体共享方式由上传人自由设定。只要带有以下“共享文档”标识的文档便是该类文档。<a href="/portal/browse/help#help/29">了解文档类型</a>
</div>
</div>
</div>
<div class="reader-container xreader" id="reader-container-1" style="width: 890px;">
<div class="reader-container-inner" id="reader-container-inner-1">
<div class="mod reader-page complex reader-page-1">
<b class="top"><b class="tl"></b><b class="tr"></b></b>
<div class="inner">

<div class="bd" id="pageNo-1" data-page-no="1" data-mate-width="892.979" data-mate-height="1262.879" style="height: 1244.52px;" data-scale="0.70709782964164" data-render=""></div>
</div>
<b class="bottom"><b class="bl"></b><b class="br"></b></b>
</div><div id="html-reader-banner-2" class="banner-ad banner-wrap">
<div id="wkad21"><script type="text/javascript">    (function() {        var impMonitorUrls = [];        var clickMonitorUrls = [];        function visitUrl(url) {            var img = new Image();            img.src = url;            return img;        }        function visitAllUrls(urls) {            for (var i = 0; i < urls.length; i++) {                visitUrl(urls[i]);            }        }        function addEventListener(node, event, func, useCapture) {            node = node || document;            useCapture = useCapture || false;            if (node.addEventListener) {                node.addEventListener(event, func, useCapture);            } else {                node.attachEvent('on' + event, func);            }        }        function init() {            var imgLink = document.getElementById('img_link');            if (imgLink) {                addEventListener(imgLink, 'click', function() {                            visitAllUrls(clickMonitorUrls);                        }, false);            }        }        function req_imp12() {            visitUrl("https://eduad.baidu.com/impression/wenku_post_json?p=9TourizqioHgE8KYEzbuEjr1yN1C_HKI0AJj3SXrm5xDId_OsUv0RXg9uWlibakHBXX7d8bWBkcLDSVehADD7KBLn4k8KeLmtR-t6zT8plF7a0LiCfM3Gl2HPdG3oX_aWyEtbP0n4ec5Y_cf6FSartW7IwtzZEVZ07WIuLOIEfuSFQRgUEnVMeHptxCeWDzRWd1xCVHooAux5Wk2_DtBllGCE-B2LKwS5tPq3T5x_6r2Q_MtjC1B4JUkJ5cIKHPCzxomqc23Pa84OKhrWqcdqsqLeg3gG1BtEu045B8Y_EGzKxWqNtzLmmH6ZRIt8vxjafd2xceP2jPLskJTT8y3O9_P4LcUGtpEB_p71yPlQCXX0F2Gs42BaH5j8skwjKqI4Q46E9ro-HokU9f5g95cqC4DggDvE6RlEL_C5EOhD_KbtniU0S04TjMbzMcI7ifUpggI0taLaEk4J1L3ExB2MgMTzsB-2ecsPQCUDOzmUhcviQI5qvjj0k3SgTRH6mE8StAq4G4ccMte57mxVK_wGQAAJxL4ShmhhFG-nSZQ2UpRzpqgsb1Dp3xtPPN9UdFyjB-mLwdSekMYYoY-UE7Pk3easRgpdDU2VHdQDhxru4eKSnBNjlYQIJlLY4kDou1ycWAage4Ff3_1Mwy6vw-nc8Idz5HQ9OM5WuQERqEUT8u7iaK6XMLT6uJi-d2eyPbhdUx_oOL7GSejJ_dQgw_QquUawqzVUC00-ostsywmmYUs8DPjSxNKgOczklIsHeIA&price=0");            visitAllUrls(impMonitorUrls);            init();        }        if (window.attachEvent) {            window.attachEvent('onload', req_imp12);        }        else if (window.addEventListener) {           window.addEventListener('load', req_imp12, false);        }    }) ();</script><style>    .product {        position: relative;    }    .adv-logo {        position: absolute;        bottom: 1px;        z-index: 100;    }    .ad-label {        left: 1px;    }    .dsp-logo {        right: 1px;    }</style><div class="product">    <a class="img_area" id="img_link" href="https://eduad.baidu.com/click/wenku_post_json?p=9TourizqioHgE8KYEzbuEjr1yN1C_HKI0AJj3SXrm5xDId_OsUv0RXg9uWlibakHBXX7d8bWBkcLDSVehADD7KBLn4k8KeLmtR-t6zT8plF7a0LiCfM3Gl2HPdG3oX_aWyEtbP0n4ec5Y_cf6FSartW7IwtzZEVZ07WIuLOIEfuSFQRgUEnVMeHptxCeWDzRWd1xCVHooAux5Wk2_DtBllGCE-B2LKwS5tPq3T5x_6r2Q_MtjC1B4JUkJ5cIKHPCzxomqc23Pa84OKhrWqcdqsqLeg3gG1BtEu045B8Y_EGzKxWqNtzLmmH6ZRIt8vxjafd2xceP2jPLskJTT8y3O9_P4LcUGtpEB_p71yPlQCXX0F2Gs42BaH5j8skwjKqI4Q46E9ro-HokU9f5g95cqC4DggDvE6RlEL_C5EOhD_KbtniU0S04TjMbzMcI7ifUpggI0taLaEk4J1L3ExB2MgMTzsB-2ecsPQCUDOzmUhcviQI5qvjj0k3SgTRH6mE8StAq4G4ccMte57mxVK_wGQAAJxL4ShmhhFG-nSZQ2UpRzpqgsb1Dp3xtPPN9UdFyjB-mLwdSekMYYoY-UE7Pk3easRgpdDU2VHdQDhxru4eKSnBNjlYQIJlLY4kDou1ycWAage4Ff3_1Mwy6vw-nc8Idz5HQ9OM5WuQERqEUT8u7iaK6XMLT6uJi-d2eyPbhdUx_oOL7GSejJ_dQgw_QquUawqzVUC00-ostsywmmYUs8DPjSxNKgOczklIsHeIA&amp;price=0&amp;lp=VDU-_bE4y9O75Fqy-TOY0Tfe6T4HMZwrPcei_VIih-puXAJB8x-2xDKPrE8QG_Tux6ic6GuRkKXlfqqo2UHwYg==" target="_blank">        <img src="https://edu-ad-test-cdn.cdn.bcebos.com/81812fa1911a9ae023ab97576179a236/882a5f45da664bafbd82b4ff41b6c345.jpg">    </a></div><a class="ad-logo"></a></div>
<a class="ad-logo"></a>
<div id="html-reader-our-ad-1" class="event-banner banner-block ad-hidden" style="width: 890px;"></div>
</div>

<div class="mod reader-page complex reader-page-2">
<b class="top"><b class="tl"></b><b class="tr"></b></b>
<div class="inner">

<div class="bd" id="pageNo-2" data-page-no="2" data-mate-width="892.979" data-mate-height="1262.879" style="height: 1244.52px;" data-scale="0.70709782964164" data-render=""></div>
</div>
<b class="bottom"><b class="bl"></b><b class="br"></b></b>
</div><div id="html-reader-AD-5" class="banner-ad banner-wrap test">
<div id="wkad21-2"><div class="fc-parallax-scrolling">              <div class="fc-parallax-scrolling-wrapper" style="top: 0px;">                              <a class="fc-parallax-scrolling-run fc-parallax-scrolling-with-image fc-parallax-scrolling-d9b779 fc-link" href="http://www.baidu.com/baidu.php?url=af0000aF4eAvq9HI8dOG7A_oNWrgDWUOoCKJoAGZF7M7TQvEGVkU6cUOgyKKdd88jwl_8jMQUK0Qm7qnGj46n37RfeCYWOEqYrrKEfoVFwJh7IjmdAyBXcKSD3K3obJeZngAoKaTYVpswEEQOlscn0_zsTCh8DeoJ0UNA5p-T4kq9ZRMKpssQTFxY_VUth6xJ1ywmjBYfTzbILXLX0.Db_ifSyJU7Z6YL5WWHjfInBapjEJknphU8gWE3t_dZl2n5fSQJlPW-4xl53tEQdxom4XgeOQlSL-4Xo_HZQzOYx1Xx4xqM4xx4TEQduknTEQexzOQOgOwSOzSOz4XgJOikztELOBXxL4XgoGm4XgSFex94XgJOAkztELOPztEy9AkztElZ3tEQd8knTEQtEqMeOQ-4XoQrFW-4xUexEt8g-l3nHZQzOe5zSOz4XgJl4tHZQzOYx-qOztEQdsn_TEQO_SL-4XVASPW-4xdSE3tEQddFTkztElMMOw4Xgo6mbWCnYcO2eHWtVNHn5FKjweXlyrW9SW-SEwOcuYtZmOCz4O9zslxUblr1SFqqSEdLOYXvOIqqIOetPaZqX5OuOBTxdtZ3Sy1OgvXQ5ZJlPW-4xl53tEQdxGiqW-4xEODtOEztEgi1akztEtHvOjztEgi1jykztEtHvOjgztEg7oum4XgeOQlSL-4XoQrFW-4xUexEt8g-l8kGBsgmhrg-OCOhtOzOe5zSOz4XgJ17Ine7Bm4XgvO-SgSESWqO-qO-ztEyeKBm4Xg4xe5LSgQzqg3vrg-SO48g-l3Ayrg-OvxUztEy9AkztElZ3tEQSZt5XJ9fkkOS_DZKsTZ-JJu94c2V7tv2jZLu89IT-9MW8tXMuT1vg4r1_8vUQSM_8LgtxZkzFHjg8_RojPak8LvIhwf0.U1YY0ZDq_eg7k_gDsEitvsKspynqnfKY5UrdkTUiCUo70A-V5HDsP1T0u1dLTv410ZNG5fKspyfqP0KWpyfqrHn0UgfqnWfsr0KopHYs0ZFY5HTkPsK-pyfqrH0znjc0mhbqnW0Y0AdW5H00TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0AdGujYs0A-kIjYs0A7B5HKxn0K-ThTqn0KsTjYs0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0AuY5H00TA6qn0KET1Ys0AFL5H00UMfqn0K1XWY0mgPxpywW5y41QyPV0A-bm1Y0IZN15HT1nj6znHb1nHT4njm3PW6kP1c0ThNkIjYkPHTknW61PWR3rH6L0ZPGujYsnj0drHRknhuWPhDYPW9b0AP1UHdjrjNAnRckwDwawHf4wWfz0A7W5HD0TA3qn0KkUgfqrHb40Z7VT1Ys0ZGY5H00UyPxuMFEUHYs0Aw9UMNBuNqsUA78pyw15H00TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KGTvP_5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KEIjYs0AqzTZfqnanscznsc10WnansQW0snj0snansczns0APzm1YkrjDLnf&amp;word=%E8%BD%A6%E7%89%8C%E6%8B%8D%E5%8D%96%E4%BB%B7">                     <div class="fc-parallax-scrolling-text">                         <div class="fc-parallax-scrolling-text-inner">                             <div class="fc-parallax-scrolling-title fc-parallax-scrolling-text-line">                                 广汽本田 锐·混动家族,无需插电,强劲如一                             </div>                             <div class="fc-parallax-scrolling-content">                                 <div class="fc-parallax-scrolling-content-left">                                     <p class="fc-parallax-scrolling-content-inner">                                         <span class="fc-parallax-scrolling-tag">广告</span>                                         <span class="fc-parallax-scrolling-sub fc-parallax-scrolling-text-line">"奥德赛锐·混动,搭载第三代i-MMD混动技术,尽显混动MPV运动个性"!</span>                                         <span class="fc-parallax-scrolling-bogus">查看详情 &gt;</span>                                     </p>                                 </div>                             </div>                         </div>                     </div>                     <div class="fc-parallax-scrolling-image">                         <ul>                             <li>                                 <div style="background-image: url(http://ns-strategy.cdn.bcebos.com/ns-strategy/upload/applvyou/part-004688-76.jpg)"></div>                             </li>                             <li class="fc-parallax-scrolling-second-image">                                 <div style="background-image: url(http://ns-strategy.cdn.bcebos.com/ns-strategy/upload/applvyou/part-004167-1204.jpg)"></div>                             </li>                             <li>                                 <div style="background-image: url(http://ns-strategy.cdn.bcebos.com/ns-strategy/upload/applvyou/part-000584-899.jpg)"></div>                             </li>                         </ul>                     </div>                 </a>                                           <a class="fc-parallax-scrolling-run fc-parallax-scrolling-with-image fc-parallax-scrolling-25ae84 fc-link" href="http://www.baidu.com/baidu.php?url=af0000aF4eAvq9HI84k89Vgmdrep5WF0opPWMJ9cI5uivak06QthAHL-wlnBJIpY0diXxMDCdUSATLYA8AhvwgesGpcaYuGRVisoU39VNSYDONE6XNl-3hVGbEwRZpbQE81_SrH6a0bS_HFN7AnYYaF-5MWi1Wcp0dqDrg7a61JPuGT_rW4B1hds-uaRBZ1HWnpI_iezjNVSBWbxS6.7Y_NR2Ar5Od66sw5I7M9CE9exQQTBaPrMLek8sHfGmEukmntpyuCp88aFeCEETkblTMWYS5ZIblkECFSq17erQKA-hpAo-oozuPv1W_LIPMWdCrmJCRnTXZWeTrHl3TMdusfYZ8Bt_VznrHl3vglygtV7tIjM93OgA1nh29tQPK5L8stx-gblxZTGyAp7BEFkvNJ.U1Y10ZDq_eg7k_gDsEitvsKspynqnfKY5UrdkTU7knQY1x60pyYqnH0LPsKM5gI1UMn0Iybq0ZKGujYY0APGujY4nsKVIjYzPj030AVG5H00TMfqP1DL0ANGujY4njcsn6KBpHYznjf0Uynqn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00Uy-b5H00pg7Y5H00mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uMfqn0KspjYs0Aq15H00mMTqn0K8IjYs0ZPl5fK9TdqGuAnqUMnVmvY0pywW5fKYIgnqnHn1n1RzPHDdn1R1PWf1rHczPW00ThNkIjYkPHTknW61PWR3rH6L0ZPGujYsnj0drHRknhuWPhDYPW9b0AP1UHdjrjNAnRckwDwawHf4wWfz0A7W5HD0TA3qn0KkUgfqrHb40Z7VT1Ys0ZGY5H00UyPxuMFEUHYs0Aw9UMNBuNqsUA78pyw15H00TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KGTvP_5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KEIjYs0AqzTZfqnanscznsc10WnansQW0snj0snansczns0APzm1Y1n1czPs&amp;word=%E8%BD%A6%E7%89%8C%E6%8B%8D%E5%8D%96%E4%BB%B7">                     <div class="fc-parallax-scrolling-text">                         <div class="fc-parallax-scrolling-text-inner">                             <div class="fc-parallax-scrolling-title fc-parallax-scrolling-text-line">                                 车牌拍卖网-正规网上拍卖平台                             </div>                             <div class="fc-parallax-scrolling-content">                                 <div class="fc-parallax-scrolling-content-left">                                     <p class="fc-parallax-scrolling-content-inner">                                         <span class="fc-parallax-scrolling-tag">广告</span>                                         <span class="fc-parallax-scrolling-sub fc-parallax-scrolling-text-line">车牌拍卖网-拍卖上京东,网罗全球好物,低价狂欢拍,福利享不停,捡漏捡到手软,速抢.</span>                                         <span class="fc-parallax-scrolling-bogus">查看详情 &gt;</span>                                     </p>                                 </div>                             </div>                         </div>                     </div>                     <div class="fc-parallax-scrolling-image">                         <ul>                             <li>                                 <div style="background-image: url(http://ns-strategy.cdn.bcebos.com/ns-strategy/upload/applvyou/part-004336-409.jpg)"></div>                             </li>                             <li class="fc-parallax-scrolling-second-image">                                 <div style="background-image: url(http://ns-strategy.cdn.bcebos.com/ns-strategy/upload/applvyou/part-004167-1204.jpg)"></div>                             </li>                             <li>                                 <div style="background-image: url(http://ns-strategy.cdn.bcebos.com/ns-strategy/upload/applvyou/part-002953-1515.jpg)"></div>                             </li>                         </ul>                     </div>                 </a>                      </div>      </div> </div>
<a class="ad-logo"></a>
<div id="html-reader-our-ad-1" class="event-banner banner-block ad-hidden"></div>
</div>

<div class="mod reader-page complex reader-page-3">
<b class="top"><b class="tl"></b><b class="tr"></b></b>
<div class="inner">

<div class="bd" id="pageNo-3" data-page-no="3" data-mate-width="892.979" data-mate-height="1262.879" style="height: 1244.52px;" data-scale="0.70709782964164" data-render=""></div>
</div>
<b class="bottom"><b class="bl"></b><b class="br"></b></b>
</div><div id="html-reader-go-more" class="banner-wrap more-btn-banner" style="height: auto; display: none;">
<div class="banner-core-wrap super-vip"><div class="doc-banner-text">下载文档到电脑，使用更方便</div>            <div class="doc-banner-value"><div><span class="icon-ticket"></span>2下载券</div><div class="doc-banner-ticket-rights">（您持有<span>0</span>下载券，积分不足无法兑换）</div></div>    <div class="doc-banner-btns super-vip">                                <div class="btn-pay-vip"><i></i>VIP免券下载                <div class="new-user-discount-tip">VIP新客立减2元</div></div>    </div><div class="doc-banner-tip super-vip"><div class="doc-banner-rights-wrap"><span class="icon-triangle" style="left: 221.734px;"></span><div class="download-pro-doc"><i></i>享VIP专享文档下载特权</div><div class="download-share-doc"><i></i>赠共享文档下载特权</div><div class="yuedu-vip"><i></i>赠百度阅读VIP精品版</div></div></div></div>
<div class="continue-to-read">
<div class="banner-more-btn">
<span class="moreBtn goBtn">
<span>还剩3页未读，</span>
<span class="fc2e">继续阅读</span>
</span>
<p class="down-arrow goBtn"></p>
</div>
<div class="hengxian"></div>
</div>
<div class="wubai-wrap">
<div class="wubai-title">
<span class="wubai-icon"></span>
<p>定制HR最喜欢的简历</p>
</div>
<a href="/org/browse/jianlidingzhi" target="_blank" class="wubai-rukou log-xsend" data-logxsend="[1, 100844]">
我要定制简历</a>
</div>
<div class="fc-container" style="display: block;"><div class="fc-wrap fc-wrap-real-container"><div class="relate-title"><p class="content" style="display: none;"></p></div><div class="fc-inner"><style type="text/css">.zIZnAL {margin: 20px auto 30px;text-align: center;}.zIZnAL .jvunAH {margin-bottom: 20px;}.zIZnAL .sOWSwe {margin-right: 10px;font-size: 14px;color: #333;display: inline-block;overflow: hidden;white-space: nowrap;text-overflow: ellipsis;vertical-align: bottom;max-width: 320px;}.zIZnAL .sOWSwe font {color: #333!important;}.zIZnAL .WB_gPy {font-size: 13px;color: #666;}.zIZnAL .CvykjT {display: inline-block;border: 1px solid #2fad85;border-radius: 2px;}.zIZnAL .CvykjT a {display: block;padding: 12px 24px;font-size: 18px;color: #2fad86;background-color: #fff;}.zIZnAL .CvykjT a:hover {color: #fff;background-color: #2fad85;text-decoration: none;}</style><div class="zIZnAL"><div class="jvunAH JHErtw"><a class="sOWSwe" href="http://www.baidu.com/baidu.php?url=af0000aF4eAvq9HI8zrvvd48ROBgsV-jATZmlT5prEzVkdGUbHCYi8dzRS9tujaQlVLZ_IjOakhdq252k1XO1ueZsTAKSmtuPUuFZxZG819UHZEULwBZOfZO0yr5e-QM08ercYjEWUyQ3C1eBbP7wTmZDPBgHxUrRdF-8TS4AtPtqT1l7zx7tYtJbYDAyQ-vBMVxSTJo8Q3-B2qSV0.DR_NR2Ar5Od66uxGiOVH4R5C6HqamJDZ0hl4Sumh5ktSNnQV5KugztU5A1KYGWyAp7WFYq5ZcC0.U1Yk0ZDqzoQjVnWVE5lOzIQRd_URenO6_8D0TA-W5HD0IjvelTjkVXxgYtO6_8ZykVxL0A-V5HRLnsKM5gK1UMn0Iybq0ZKGujYY0APGujY4nsKVIjYs0AVG5H00TMfqP1DL0ANGujY0mhbqnW0Yg1nsn-t1njn0Uynqn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00Uy-b5H00pg7Y5H00mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uMfqn0KspjYs0Aq15H00mMTqn0K8IjYs0ZPl5fK9TdqGuAnqUMnVmLf0pywW5fKYIgnqnHDLnjn4PWf1rHDsnHRkP1b4njR0ThNkIjYkPHTknW61PWR4njRz0ZPGujYsnj0drHRknhuWPvP-uhfk0AP1UHdjrjNAnRckwDwawHf4wWfz0A7W5HD0TA3qn0KkUgfqrHb40Z7VT1Ys0ZGY5H00UyPxuMFEUHYs0Aw9UMNBuNqsUA78pyw15fKsmgwxuhk9u1Ys0AwWpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5H00uhPdIjYs0A-1mvsqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0AqY5H00ULFsIjYsc10Wc10Wnansc108nj0snj0sc10Wc100mLFW5HRLnHDL&amp;word=%E4%BB%80%E4%B9%88%E8%BD%AF%E4%BB%B6%E5%8F%AF%E4%BB%A5%E5%88%B6%E9%80%A0%E7%9B%B8%E5%86%8C&amp;shh=wenku.baidu.com" target="_blank">婚礼电子相册制作 - 免费预览,N多模版,一键生成大片</a><span class="WB_gPy">广告</span></div></div></div></div><script>(function(win){win.ecom = win.ecom || {};win.ecom.pl2 = win.ecom.pl2 || {};win.ecom.pl2.imTimesign = parseInt("87" || 0, 10);win.ecom.pl2.searchId = "00059512fc7cefd1";})(window);(function(a){function b(d){var c=location.href.match("debug=1");var g=window.jQuery||{};if(!c){try{d(a.pl2,g)}catch(f){}}else{d(a.pl2,g)}}a.pl2.run=function(d,c){if(c||arguments.length==1){bds.ready(function(){b(d)})}else{b(d)}};a.pl2.q=function(f,g){g=g||document;if(g.getElementsByClassName){return g.getElementsByClassName(f)}else{var d=[];var c=g.all||g.getElementsByTagName("*");var e=c.length;f=f.replace(/\-/g,"\\-");var h=new RegExp("(^|\\s)"+f+"(\\s|$)");while(--e>=0){if(h.test(c[e].className)){d.push(c[e])}}return d}}})(window.ecom);(function(v){var h=undefined,g=undefined;var l=0,k=0;var e=0;var o=0;var i=0;var d=0;var m=0;var b=0;var t=0;var r=/link\?url\=([^\&]+)/;var n=/\?url\=([^\.]+)\./;function s(){var y=t.href;var x=r.exec(y)||n.exec(y);return x?x[1]:false}function u(z){var x=s();if(x!==false){var y=q(x,z);p(y)}}function p(z){var x="&ck="+[z,e,b,l,k,h,g,m].join(".");if(t.href){var y=t.href;if(y.indexOf("&ck=")==-1){t.href+=x}else{t.href=y.replace(/&ck=[\d.]*/,x)}}}function q(A,C){var B=0;for(var z=0;z<(((e*C)%99)+9);z++){var y=A.length<20?A.length:20;B+=A.charCodeAt((b*z)%A.length)}return B}function w(x){x=x||window.event;e++;if(h===undefined){h=x.clientX}if(g===undefined){g=x.clientY}o=new Date().getTime()}function f(y,x){y=y||window.event;t=y.target||y.srcElement;while(t&&t.tagName!="A"){t=t.parentNode}i=new Date().getTime();b=9999;l=y.clientX;k=y.clientY;if(o===0){m=0}else{m=i-o}u(x)}function j(y,x){d=new Date().getTime();b=d-i;u(x)}function c(C,z,B){var A,x,y;for(y in z){A=z[y];x=B[y];if(window.attachEvent){C.attachEvent("on"+A,x)}else{C.addEventListener(A,x,false)}}}function a(x){return[function(y){w(y)},function(y){f(y,x)},function(y){j(y,x)}]}v.ck=function(B,A){if(B.length===undefined){B=[B]}var x=B.length;var y=0;var z=a(A);for(;y<x;y++){c(B[y],["mouseover","mousedown","mouseup"],z)}}})(window.ecom.pl2);window.ecom.pl2.run(function(c){var e=c.q("JHErtw");for(var b=0;b<e.length;b++){var a=e[b];var d=a.getElementsByTagName("A");c.ck(d,window.ecom.pl2.imTimesign)}},false);</script></div>
<div class="reader-fc-owner"></div>
</div><div id="html-reader-AD-3t4" class="banner-ad banner-wrap hidden-doc-banner" style="display: block;">
</div>

<div class="mod reader-page complex hidden-doc-banner reader-page-4" style="display: block;">
<b class="top"><b class="tl"></b><b class="tr"></b></b>
<div class="inner">

<div class="bd" id="pageNo-4" data-page-no="4" data-mate-width="892.979" data-mate-height="1262.879" style="height: 1244.52px;" data-scale="0.70709782964164" data-render="1"><div class="reader-parent-383e8336c281e53a5802ff9e reader-parent " style="position: relative; top: 0px; left: 0px; transform: scale(0.92); transform-origin: 0px 0px;"><div class="reader-wrap383e8336c281e53a5802ff9e" style="position:absolute;top:0;left:0;width:100%;height:100%;"><div class="reader-main-383e8336c281e53a5802ff9e" style="position:relative;top:0;left:0;width:100%;height:100%;"><div class="reader-txt-layer" style="z-index:1"><div class="ie-fix"><p class="reader-word-layer reader-word-s4-0" style="width:3367px;height:224px;line-height:224px;top:714px;left:4583px;z-index:0;font-family:'宋体','383e8336c281e53a5802ff9e0010004','宋体';letter-spacing:-0.49px;false">如果对您有帮助！感谢评论与分享</p><p class="reader-word-layer reader-word-s4-0" style="width:50px;height:224px;line-height:224px;top:714px;left:7949px;z-index:1;font-family:'Calibri Light','383e8336c281e53a5802ff9e0020004','Calibri Light';font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s4-2" style="width:3141px;height:294px;line-height:294px;top:1252px;left:1442px;z-index:2;false">批准，未经审批不得投入运行。</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:1252px;left:4583px;z-index:3;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:1752px;left:1442px;z-index:4;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:1752px;left:1667px;z-index:5;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:131px;height:294px;line-height:294px;top:1752px;left:1892px;z-index:6;">2</p><p class="reader-word-layer reader-word-s4-1" style="width:6074px;height:294px;line-height:294px;top:1752px;left:2025px;z-index:7;false">、进入涉密计算机系统应进行身份鉴别，要按要求设置并定期</p><p class="reader-word-layer reader-word-s4-4" style="width:2018px;height:294px;line-height:294px;top:2252px;left:1442px;z-index:8;false">更新涉密系统口令。</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:2252px;left:3462px;z-index:9;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:2752px;left:1442px;z-index:10;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:2752px;left:1667px;z-index:11;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:131px;height:294px;line-height:294px;top:2752px;left:1892px;z-index:12;">3</p><p class="reader-word-layer reader-word-s4-1" style="width:6074px;height:294px;line-height:294px;top:2752px;left:2025px;z-index:13;false">、涉密计算机系统应当与国际互联网物理隔离。严禁以任何方</p><p class="reader-word-layer reader-word-s4-5" style="width:5831px;height:294px;line-height:294px;top:3252px;left:1442px;z-index:14;false">式将涉密计算机联入国际互联网或其他非涉密计算机系统。</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:3252px;left:7274px;z-index:15;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:3752px;left:1442px;z-index:16;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:3752px;left:1667px;z-index:17;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:131px;height:294px;line-height:294px;top:3752px;left:1892px;z-index:18;">4</p><p class="reader-word-layer reader-word-s4-1" style="width:5833px;height:294px;line-height:294px;top:3752px;left:2023px;z-index:19;letter-spacing:-0.6px;false">、涉密计算机系统工作场所应作为保密要害部位进行管理。</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:3752px;left:7856px;z-index:20;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:4252px;left:1442px;z-index:21;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:4252px;left:1667px;z-index:22;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:131px;height:294px;line-height:294px;top:4252px;left:1892px;z-index:23;">5</p><p class="reader-word-layer reader-word-s4-1" style="width:4039px;height:294px;line-height:294px;top:4252px;left:2023px;z-index:24;letter-spacing:-0.55px;false">、机关工作人员不得越权访问涉密信息。</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:4252px;left:6062px;z-index:25;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:4752px;left:1442px;z-index:26;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:4752px;left:1667px;z-index:27;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:131px;height:294px;line-height:294px;top:4752px;left:1892px;z-index:28;">6</p><p class="reader-word-layer reader-word-s4-1" style="width:6074px;height:294px;line-height:294px;top:4752px;left:2025px;z-index:29;false">、涉密计算机系统安全保密管理员、密钥管理员和系统管理员</p><p class="reader-word-layer reader-word-s4-6" style="width:3589px;height:294px;line-height:294px;top:5252px;left:1442px;z-index:30;false">应由不同人员担任，并且职责明确。</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:5252px;left:5031px;z-index:31;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:5752px;left:1442px;z-index:32;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:5752px;left:1667px;z-index:33;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-7" style="width:2466px;height:294px;line-height:294px;top:5752px;left:1892px;z-index:34;false">二、涉密计算机使有管理</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:5752px;left:4358px;z-index:35;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:6252px;left:1442px;z-index:36;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:6252px;left:1667px;z-index:37;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:131px;height:294px;line-height:294px;top:6252px;left:1892px;z-index:38;">1</p><p class="reader-word-layer reader-word-s4-1" style="width:6074px;height:294px;line-height:294px;top:6252px;left:2025px;z-index:39;false">、承担涉密事项处理的计算机应专机专用，专人管理，严格控</p><p class="reader-word-layer reader-word-s4-4" style="width:2018px;height:294px;line-height:294px;top:6752px;left:1442px;z-index:40;false">制，不得他人使用。</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:6752px;left:3462px;z-index:41;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:7252px;left:1442px;z-index:42;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:7252px;left:1667px;z-index:43;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:131px;height:294px;line-height:294px;top:7252px;left:1892px;z-index:44;">2</p><p class="reader-word-layer reader-word-s4-1" style="width:6056px;height:294px;line-height:294px;top:7252px;left:2023px;z-index:45;letter-spacing:-0.65px;false">、禁止使用涉密计算机上国际互联网或其它非涉密信息系统。</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:7252px;left:8079px;z-index:46;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:7752px;left:1442px;z-index:47;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:7752px;left:1667px;z-index:48;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:131px;height:294px;line-height:294px;top:7752px;left:1892px;z-index:49;">3</p><p class="reader-word-layer reader-word-s4-1" style="width:6074px;height:294px;line-height:294px;top:7752px;left:2025px;z-index:50;false">、严格一机两用操作程序，未安装物理隔离卡的涉密计算机严</p><p class="reader-word-layer reader-word-s4-6" style="width:4262px;height:294px;line-height:294px;top:8252px;left:1442px;z-index:51;false">禁连接国际互联网或其它非涉密信息系统。</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:8252px;left:5704px;z-index:52;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:8752px;left:1442px;z-index:53;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:8752px;left:1667px;z-index:54;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:131px;height:294px;line-height:294px;top:8752px;left:1892px;z-index:55;">4</p><p class="reader-word-layer reader-word-s4-1" style="width:6075px;height:294px;line-height:294px;top:8752px;left:2025px;z-index:56;false">、涉密计算机系统的软件配置情况及本身有涉密内容的各种应</p><p class="reader-word-layer reader-word-s4-2" style="width:3141px;height:294px;line-height:294px;top:9252px;left:1442px;z-index:57;false">用软件，不得进行外借和拷贝。</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:9252px;left:4583px;z-index:58;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:9752px;left:1442px;z-index:59;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:9752px;left:1667px;z-index:60;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:131px;height:294px;line-height:294px;top:9752px;left:1892px;z-index:61;">5</p><p class="reader-word-layer reader-word-s4-1" style="width:3814px;height:294px;line-height:294px;top:9752px;left:2023px;z-index:62;letter-spacing:-0.59px;false">、未经许可，任何私人的光盘、软盘、</p><p class="reader-word-layer reader-word-s4-3" style="width:138px;height:294px;line-height:294px;top:9752px;left:5839px;z-index:63;">u</p><p class="reader-word-layer reader-word-s4-4" style="width:2018px;height:294px;line-height:294px;top:9752px;left:6079px;z-index:64;false">盘不得在涉密计算机</p><p class="reader-word-layer reader-word-s4-5" style="width:5831px;height:294px;line-height:294px;top:10253px;left:1442px;z-index:65;false">机设备上使用；涉密计算机必需安装防毒软件并定期升级。</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:10253px;left:7274px;z-index:66;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:10753px;left:1442px;z-index:67;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:10753px;left:1667px;z-index:68;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-7" style="width:2466px;height:294px;line-height:294px;top:10753px;left:1892px;z-index:69;false">三、笔记本电脑使用管理</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:10753px;left:4358px;z-index:70;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:11253px;left:1442px;z-index:71;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:11253px;left:1667px;z-index:72;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s4-3" style="width:131px;height:294px;line-height:294px;top:11253px;left:1892px;z-index:73;">1</p><p class="reader-word-layer reader-word-s4-1" style="width:6074px;height:294px;line-height:294px;top:11253px;left:2025px;z-index:74;false">、涉密笔记本电脑由办公室统一管理，使用时必须履行登记手</p><p class="reader-word-layer reader-word-s4-1" style="width:449px;height:294px;line-height:294px;top:11753px;left:1442px;z-index:75;false">续。</p><p class="reader-word-layer reader-word-s4-3" style="width:66px;height:294px;line-height:294px;top:11753px;left:1890px;z-index:76;font-family:simsun;">&ensp;
</p></div></div></div></div></div></div>
</div>
<b class="bottom"><b class="bl"></b><b class="br"></b></b>
</div><div id="html-reader-AD-4t5" class="banner-ad banner-wrap hidden-doc-banner" style="display: block;"><div class="fc-parallax-scrolling">              <div class="fc-parallax-scrolling-wrapper" style="top: 0px;">                              <a class="fc-parallax-scrolling-run fc-parallax-scrolling-with-image fc-parallax-scrolling-d9b779 fc-link" href="http://www.baidu.com/baidu.php?url=af0000aF4eAvq9HI8d1GiShROSBnIo2UE8GVN8i2JTucwdSEIobEWrmiFoceYOTbaq2MNmfFqRhk6mdpcAt1Sxg7QvtZwU28p3LC6ERgvU2m2W1UbwRrJ5uUiYNGVGJ8Wa1pg_EN2zqYBoK3doSEPQ78Ct-fC7IwJLPLkleRDNVRv1cvIQrcrMEhmJHCkE4mveNWeWF_oUYg6r7BNf.DD_ifYgsq_5b1IGuWCFhG696uo34QQr51E3qre__lX519zUqO1xutqPI-x1vndO5uxkSxUbtxZ_SIg1sNR2Ar5Od663rj6tCpbL_L_C69uh6LUCnMW_L4QrxX5i1Pf9IT-WNb_oL4S5H3vur1k1eenqxZIYq-XHFdRojPakgkLXrwf.U1YL0ZDq_eg7k_gDsEitvsKspynqnfKY5UrdkTUiCUo70A-V5HDsP1T0u1dLTv410ZNG5fKspyfqP0KWpyfqrHn0UgfqnWfsr0KopHYs0ZFY5HTkPsK-pyfqrH0znjc0mhbqnW0Y0AdW5H00TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0AdGujYs0A-kIjYs0A7B5HKxn0K-ThTqn0KsTjYs0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0AuY5H00TA6qn0KET1Ys0AFL5H00UMfqn0K1XWY0mgPxpywW5y41QyPV0A-bm1Y0IZN15HDdnjmYrjT4njb1rHmsnHTkPHR10ZF-TgfqnHRLnHc3n1mdrjb3PsK1pyfqnj0sPHbdnHFhm1u9Pjm3u0KWTvYqf16dwW7anRwDfbRYrRmYn6K9m1Yk0ZK85H00TydY5Hb4rfKkUgnqn0KlIjYs0AdWgvuzUvYqn0Kbmy4dmhNxTAk9Uh-bT1Ys0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00pgPWUjYs0ZGsUZN15H00mywhUA7M5HD0UAuW5H00ULfqn0KETMKY5H0WnanWnansc10Wna3snj0snj0WnanWn0KWThnqPjTLnjb&amp;word=%E8%BD%A6%E7%89%8C%E6%8B%8D%E5%8D%96%E4%BB%B7">                     <div class="fc-parallax-scrolling-text">                         <div class="fc-parallax-scrolling-text-inner">                             <div class="fc-parallax-scrolling-title fc-parallax-scrolling-text-line">                                 东风启辰D60EV智趣上市,官方指导价13.78万元起车牌摇号                             </div>                             <div class="fc-parallax-scrolling-content">                                 <div class="fc-parallax-scrolling-content-left">                                     <p class="fc-parallax-scrolling-content-inner">                                         <span class="fc-parallax-scrolling-tag">广告</span>                                         <span class="fc-parallax-scrolling-sub fc-parallax-scrolling-text-line">不限行不限购,置换立享至高5000元补贴;赠送1000元充电积分和高品质智联充电桩;</span>                                         <span class="fc-parallax-scrolling-bogus">查看详情 &gt;</span>                                     </p>                                 </div>                             </div>                         </div>                     </div>                     <div class="fc-parallax-scrolling-image">                         <ul>                             <li>                                 <div style="background-image: url(http://ns-strategy.cdn.bcebos.com/ns-strategy/upload/applvyou/part-004688-76.jpg)"></div>                             </li>                             <li class="fc-parallax-scrolling-second-image">                                 <div style="background-image: url(http://ns-strategy.cdn.bcebos.com/ns-strategy/upload/applvyou/part-004167-1204.jpg)"></div>                             </li>                             <li>                                 <div style="background-image: url(http://ns-strategy.cdn.bcebos.com/ns-strategy/upload/applvyou/part-000584-899.jpg)"></div>                             </li>                         </ul>                     </div>                 </a>                                           <a class="fc-parallax-scrolling-run fc-parallax-scrolling-with-image fc-parallax-scrolling-25ae84 fc-link" href="http://www.baidu.com/baidu.php?url=af0000aF4eAvq9HI8d1GiShROSBnIo2UE8GVN8i2JTucwdSEIobEWrmiFoceYOTbaq2MNmfFqRhk6mdpcAt1Sxg7QvtZwU28p3LC6ERgvU2m2W1UbwRrJ5uUiYNGVGJ8Wa1pg_EN2zqYBoK3doSEPQ78Ct-fC7IwJLPLkleRDNVRv1cvIQrcrMEhmJHCkE4mveNWeWF_oUYg6r7BNf.DD_ifYgsq_5b1IGuWCFhG696uo34QQr51E3qre__lX519zUqO1xutqPI-x1vndO5uxkSxUbtxZ_SIg1sNR2Ar5Od663rj6tCpbL_L_C69uh6LUCnMW_L4QrxX5i1Pf9IT-WNb_oL4S5H3vur1k1eenqxZIYq-XHFdRojPakgkLXrwf.U1YL0ZDq_eg7k_gDsEitvsKspynqnfKY5UrdkTUiCUo70A-V5HDsP1T0u1dLTv410ZNG5fKspyfqP0KWpyfqrHn0UgfqnWfsr0KopHYs0ZFY5HTkPsK-pyfqrH0znjc0mhbqnW0Y0AdW5H00TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0AdGujYs0A-kIjYs0A7B5HKxn0K-ThTqn0KsTjYs0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0AuY5H00TA6qn0KET1Ys0AFL5H00UMfqn0K1XWY0mgPxpywW5y41QyPV0A-bm1Y0IZN15HDdnjmYrjT4njb1rHmsnHTkPHR10ZF-TgfqnHRLnHc3n1mdrjb3PsK1pyfqnj0sPHbdnHFhm1u9Pjm3u0KWTvYqf16dwW7anRwDfbRYrRmYn6K9m1Yk0ZK85H00TydY5Hb4rfKkUgnqn0KlIjYs0AdWgvuzUvYqn0Kbmy4dmhNxTAk9Uh-bT1Ys0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00pgPWUjYs0ZGsUZN15H00mywhUA7M5HD0UAuW5H00ULfqn0KETMKY5H0WnanWnansc10Wna3snj0snj0WnanWn0KWThnqPjTLnjb&amp;word=%E8%BD%A6%E7%89%8C%E6%8B%8D%E5%8D%96%E4%BB%B7">                     <div class="fc-parallax-scrolling-text">                         <div class="fc-parallax-scrolling-text-inner">                             <div class="fc-parallax-scrolling-title fc-parallax-scrolling-text-line">                                 东风启辰D60EV智趣上市,官方指导价13.78万元起车牌摇号                             </div>                             <div class="fc-parallax-scrolling-content">                                 <div class="fc-parallax-scrolling-content-left">                                     <p class="fc-parallax-scrolling-content-inner">                                         <span class="fc-parallax-scrolling-tag">广告</span>                                         <span class="fc-parallax-scrolling-sub fc-parallax-scrolling-text-line">不限行不限购,置换立享至高5000元补贴;赠送1000元充电积分和高品质智联充电桩;</span>                                         <span class="fc-parallax-scrolling-bogus">查看详情 &gt;</span>                                     </p>                                 </div>                             </div>                         </div>                     </div>                     <div class="fc-parallax-scrolling-image">                         <ul>                             <li>                                 <div style="background-image: url(http://ns-strategy.cdn.bcebos.com/ns-strategy/upload/applvyou/part-004688-76.jpg)"></div>                             </li>                             <li class="fc-parallax-scrolling-second-image">                                 <div style="background-image: url(http://ns-strategy.cdn.bcebos.com/ns-strategy/upload/applvyou/part-004167-1204.jpg)"></div>                             </li>                             <li>                                 <div style="background-image: url(http://ns-strategy.cdn.bcebos.com/ns-strategy/upload/applvyou/part-000584-899.jpg)"></div>                             </li>                         </ul>                     </div>                 </a>                      </div>      </div> <a class="ad-logo"></a></div>

<div class="mod reader-page complex hidden-doc-banner reader-page-5" style="display: block;">
<b class="top"><b class="tl"></b><b class="tr"></b></b>
<div class="inner">

<div class="bd" id="pageNo-5" data-page-no="5" data-mate-width="892.979" data-mate-height="1262.879" style="height: 1244.52px;" data-scale="0.70709782964164" data-render="1"><div class="reader-parent-383e8336c281e53a5802ff9e reader-parent " style="position:relative;top:0;left:0;-webkit-transform:scale(0.92);-webkit-transform-origin:left top;"><div class="reader-wrap383e8336c281e53a5802ff9e" style="position:absolute;top:0;left:0;width:100%;height:100%;"><div class="reader-main-383e8336c281e53a5802ff9e" style="position:relative;top:0;left:0;width:100%;height:100%;"><div class="reader-txt-layer" style="z-index:1"><div class="ie-fix"><p class="reader-word-layer reader-word-s5-0" style="width:3367px;height:224px;line-height:224px;top:714px;left:4583px;z-index:0;font-family:'宋体','383e8336c281e53a5802ff9e0010005','宋体';letter-spacing:-0.49px;false">如果对您有帮助！感谢评论与分享</p><p class="reader-word-layer reader-word-s5-0" style="width:50px;height:224px;line-height:224px;top:714px;left:7949px;z-index:1;font-family:'Calibri Light','383e8336c281e53a5802ff9e0020005','Calibri Light';font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:1252px;left:1442px;z-index:2;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:1252px;left:1667px;z-index:3;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:131px;height:294px;line-height:294px;top:1252px;left:1892px;z-index:4;">2</p><p class="reader-word-layer reader-word-s5-2" style="width:6074px;height:294px;line-height:294px;top:1252px;left:2025px;z-index:5;false">、涉密笔记本电脑严禁安装无线网卡等无线设备，严禁联接国</p><p class="reader-word-layer reader-word-s5-3" style="width:1122px;height:294px;line-height:294px;top:1752px;left:1442px;z-index:6;false">际互联网。</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:1752px;left:2563px;z-index:7;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:2252px;left:1442px;z-index:8;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:2252px;left:1667px;z-index:9;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:131px;height:294px;line-height:294px;top:2252px;left:1892px;z-index:10;">3</p><p class="reader-word-layer reader-word-s5-2" style="width:6074px;height:294px;line-height:294px;top:2252px;left:2025px;z-index:11;false">、涉密笔记本电脑限委机关工作人员使用，禁止将涉密笔记本</p><p class="reader-word-layer reader-word-s5-2" style="width:1572px;height:294px;line-height:294px;top:2752px;left:1442px;z-index:12;letter-spacing:-0.31px;false">电脑借与他人。</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:2752px;left:3013px;z-index:13;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:3252px;left:1442px;z-index:14;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:3252px;left:1667px;z-index:15;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:131px;height:294px;line-height:294px;top:3252px;left:1892px;z-index:16;">4</p><p class="reader-word-layer reader-word-s5-2" style="width:6074px;height:294px;line-height:294px;top:3252px;left:2025px;z-index:17;false">、涉密笔记本电脑中的涉密信息不得存入硬盘，要存入软盘、</p><p class="reader-word-layer reader-word-s5-2" style="width:1124px;height:294px;line-height:294px;top:3752px;left:1442px;z-index:18;false">移动硬盘、</p><p class="reader-word-layer reader-word-s5-1" style="width:138px;height:294px;line-height:294px;top:3752px;left:2552px;z-index:19;">u</p><p class="reader-word-layer reader-word-s5-2" style="width:5358px;height:294px;line-height:294px;top:3752px;left:2744px;z-index:20;letter-spacing:-1.6900000000000002px;false">盘等移动存储介质，必须定期清理，与涉密笔记本电脑</p><p class="reader-word-layer reader-word-s5-3" style="width:1122px;height:294px;line-height:294px;top:4252px;left:1442px;z-index:21;false">分离保管。</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:4252px;left:2563px;z-index:22;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:4752px;left:1442px;z-index:23;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:4752px;left:1667px;z-index:24;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:131px;height:294px;line-height:294px;top:4752px;left:1892px;z-index:25;">5</p><p class="reader-word-layer reader-word-s5-2" style="width:6074px;height:294px;line-height:294px;top:4752px;left:2025px;z-index:26;false">、不准携带储涉密信息的笔记本电脑出国或去公共场所，确因</p><p class="reader-word-layer reader-word-s5-4" style="width:4262px;height:294px;line-height:294px;top:5252px;left:1442px;z-index:27;false">工作需要携带的，必须办理相关审批手续。</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:5252px;left:5704px;z-index:28;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:5752px;left:1442px;z-index:29;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:5752px;left:1667px;z-index:30;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-5" style="width:2691px;height:294px;line-height:294px;top:5752px;left:1892px;z-index:31;false">四、移动存储介质使用管理</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:5752px;left:4583px;z-index:32;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:6252px;left:1442px;z-index:33;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:6252px;left:1667px;z-index:34;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:131px;height:294px;line-height:294px;top:6252px;left:1892px;z-index:35;">1</p><p class="reader-word-layer reader-word-s5-2" style="width:224px;height:294px;line-height:294px;top:6252px;left:2025px;z-index:36;">、</p><p class="reader-word-layer reader-word-s5-2" style="width:3364px;height:294px;line-height:294px;top:6252px;left:2144px;z-index:37;letter-spacing:-0.67px;false">涉密存储介质由办公室统一管理，</p><p class="reader-word-layer reader-word-s5-5" style="width:2691px;height:294px;line-height:294px;top:6252px;left:5405px;z-index:38;false">使用时必须履行登记手续。</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:6252px;left:8099px;z-index:39;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:6752px;left:1442px;z-index:40;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:6752px;left:1667px;z-index:41;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:131px;height:294px;line-height:294px;top:6752px;left:1892px;z-index:42;">2</p><p class="reader-word-layer reader-word-s5-2" style="width:6074px;height:294px;line-height:294px;top:6752px;left:2025px;z-index:43;false">、涉密存储介质应按存储信息的最高密级标注密级，并按相同</p><p class="reader-word-layer reader-word-s5-4" style="width:2243px;height:294px;line-height:294px;top:7252px;left:1442px;z-index:44;false">密级的秘密载体管理。</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:7252px;left:3685px;z-index:45;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:7752px;left:1442px;z-index:46;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:7752px;left:1667px;z-index:47;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:131px;height:294px;line-height:294px;top:7752px;left:1892px;z-index:48;">3</p><p class="reader-word-layer reader-word-s5-2" style="width:4712px;height:294px;line-height:294px;top:7752px;left:2023px;z-index:49;letter-spacing:-0.56px;false">、禁止将涉密存储介质接入非涉密计算机使用。</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:7752px;left:6735px;z-index:50;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:8252px;left:1442px;z-index:51;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:8252px;left:1667px;z-index:52;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:131px;height:294px;line-height:294px;top:8252px;left:1892px;z-index:53;">4</p><p class="reader-word-layer reader-word-s5-2" style="width:6074px;height:294px;line-height:294px;top:8252px;left:2025px;z-index:54;false">、不得将涉密存储价质带出办公场所，如因工作需要必须带出</p><p class="reader-word-layer reader-word-s5-4" style="width:3589px;height:294px;line-height:294px;top:8752px;left:1442px;z-index:55;false">的，需履行相应的审批和登记手续。</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:8752px;left:5031px;z-index:56;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:9252px;left:1442px;z-index:57;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:9252px;left:1667px;z-index:58;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:131px;height:294px;line-height:294px;top:9252px;left:1892px;z-index:59;">5</p><p class="reader-word-layer reader-word-s5-2" style="width:1343px;height:294px;line-height:294px;top:9252px;left:2023px;z-index:60;letter-spacing:-1.1300000000000001px;false">、个人使用的</p><p class="reader-word-layer reader-word-s5-1" style="width:138px;height:294px;line-height:294px;top:9252px;left:3423px;z-index:61;">u</p><p class="reader-word-layer reader-word-s5-2" style="width:4483px;height:294px;line-height:294px;top:9252px;left:3617px;z-index:62;letter-spacing:-0.78px;false">盘等移动存储介质，不得存储涉密信息，因工</p><p class="reader-word-layer reader-word-s5-6" style="width:4710px;height:294px;line-height:294px;top:9752px;left:1442px;z-index:63;false">作需要必须使用的，使用后要及时消除密信息。</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:9752px;left:6152px;z-index:64;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:10253px;left:1442px;z-index:65;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:10253px;left:1667px;z-index:66;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-6" style="width:4037px;height:294px;line-height:294px;top:10253px;left:1892px;z-index:67;false">五、数码复钱机、多功能一体机使用管理</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:10253px;left:5929px;z-index:68;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:10753px;left:1442px;z-index:69;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:10753px;left:1667px;z-index:70;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:131px;height:294px;line-height:294px;top:10753px;left:1892px;z-index:71;">1</p><p class="reader-word-layer reader-word-s5-2" style="width:6074px;height:294px;line-height:294px;top:10753px;left:2025px;z-index:72;false">、数码复印机、多功能一体机必须指定专人使用，其他任何人</p><p class="reader-word-layer reader-word-s5-4" style="width:2243px;height:294px;line-height:294px;top:11253px;left:1442px;z-index:73;false">未经许可，不得使用。</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:11253px;left:3685px;z-index:74;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:11753px;left:1442px;z-index:75;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:66px;height:294px;line-height:294px;top:11753px;left:1667px;z-index:76;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s5-1" style="width:131px;height:294px;line-height:294px;top:11753px;left:1892px;z-index:77;">2</p><p class="reader-word-layer reader-word-s5-2" style="width:6074px;height:294px;line-height:294px;top:11753px;left:2025px;z-index:78;false">、处理涉密信息的数码复印机、多功能一体机不得连接普通电
</p></div></div></div></div></div></div>
</div>
<b class="bottom"><b class="bl"></b><b class="br"></b></b>
</div><div id="html-reader-AD-5t6" class="banner-ad banner-wrap hidden-doc-banner" style="display: block;">
</div>

<div class="mod reader-page complex hidden-doc-banner reader-page-6" style="display: block;">
<b class="top"><b class="tl"></b><b class="tr"></b></b>
<div class="inner">

<div class="bd" id="pageNo-6" data-page-no="6" data-mate-width="892.979" data-mate-height="1262.879" style="height: 1244.52px;" data-scale="0.70709782964164" data-render="1"><div class="reader-parent-383e8336c281e53a5802ff9e reader-parent " style="position:relative;top:0;left:0;-webkit-transform:scale(0.92);-webkit-transform-origin:left top;"><div class="reader-wrap383e8336c281e53a5802ff9e" style="position:absolute;top:0;left:0;width:100%;height:100%;"><div class="reader-main-383e8336c281e53a5802ff9e" style="position:relative;top:0;left:0;width:100%;height:100%;"><div class="reader-txt-layer" style="z-index:1"><div class="ie-fix"><p class="reader-word-layer reader-word-s6-0" style="width:3367px;height:224px;line-height:224px;top:714px;left:4583px;z-index:0;font-family:'宋体','383e8336c281e53a5802ff9e0010006','宋体';letter-spacing:-0.49px;false">如果对您有帮助！感谢评论与分享</p><p class="reader-word-layer reader-word-s6-0" style="width:50px;height:224px;line-height:224px;top:714px;left:7949px;z-index:1;font-family:'Calibri Light','383e8336c281e53a5802ff9e0020006','Calibri Light';font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s6-2" style="width:2916px;height:294px;line-height:294px;top:1252px;left:1442px;z-index:2;false">话线，不得与委局域网连接。</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:1252px;left:4358px;z-index:3;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:1752px;left:1442px;z-index:4;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:1752px;left:1667px;z-index:5;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:131px;height:294px;line-height:294px;top:1752px;left:1892px;z-index:6;">3</p><p class="reader-word-layer reader-word-s6-1" style="width:2197px;height:294px;line-height:294px;top:1752px;left:2023px;z-index:7;letter-spacing:-5.45px;false">、复制涉密文件、资料</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:1752px;left:4221px;z-index:8;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-1" style="width:3766px;height:294px;line-height:294px;top:1752px;left:4333px;z-index:9;letter-spacing:-3.4000000000000004px;false">、图纸等必须严格履行审批手续，复制</p><p class="reader-word-layer reader-word-s6-1" style="width:4037px;height:294px;line-height:294px;top:2252px;left:1442px;z-index:10;letter-spacing:-0.66px;false">件必须按密件处理，不得降低密级使用。</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:2252px;left:5479px;z-index:11;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:2752px;left:1442px;z-index:12;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:2752px;left:1667px;z-index:13;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:131px;height:294px;line-height:294px;top:2752px;left:1892px;z-index:14;">4</p><p class="reader-word-layer reader-word-s6-2" style="width:5608px;height:294px;line-height:294px;top:2752px;left:2023px;z-index:15;false">、处理涉密信息完毕后，必须立即销毁存储的涉密信息。</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:2752px;left:7631px;z-index:16;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:3252px;left:1442px;z-index:17;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:3252px;left:1667px;z-index:18;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-1" style="width:3587px;height:294px;line-height:294px;top:3252px;left:1892px;z-index:19;letter-spacing:-0.75px;false">六、国际互联网上发布信息保密制度</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:3252px;left:5479px;z-index:20;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:3752px;left:1442px;z-index:21;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:3752px;left:1667px;z-index:22;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:131px;height:294px;line-height:294px;top:3752px;left:1892px;z-index:23;">1</p><p class="reader-word-layer reader-word-s6-1" style="width:6074px;height:294px;line-height:294px;top:3752px;left:2025px;z-index:24;false">、在国际互联网上发布信息必须由办公室统一管理，指定专人</p><p class="reader-word-layer reader-word-s6-4" style="width:1122px;height:294px;line-height:294px;top:4252px;left:1442px;z-index:25;false">负责操作，</p><p class="reader-word-layer reader-word-s6-1" style="width:5606px;height:294px;line-height:294px;top:4252px;left:2490px;z-index:26;letter-spacing:-0.71px;false">其它科室和个人不得擅自在互联网上发布涉及工作内容的</p><p class="reader-word-layer reader-word-s6-4" style="width:1122px;height:294px;line-height:294px;top:4752px;left:1442px;z-index:27;false">任何信息。</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:4752px;left:2563px;z-index:28;font-family:simsun;">&ensp;
</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:5252px;left:1442px;z-index:29;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:5252px;left:1667px;z-index:30;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:131px;height:294px;line-height:294px;top:5252px;left:1892px;z-index:31;">2</p><p class="reader-word-layer reader-word-s6-1" style="width:224px;height:294px;line-height:294px;top:5252px;left:2023px;z-index:32;">、</p><p class="reader-word-layer reader-word-s6-5" style="width:6056px;height:294px;line-height:294px;top:5252px;left:2153px;z-index:33;false">在国际互联网上发布涉及工作内容的信息必须履行审批手续，</p><p class="reader-word-layer reader-word-s6-1" style="width:3814px;height:294px;line-height:294px;top:5752px;left:1442px;z-index:34;letter-spacing:-0.59px;false">必须由市建设口保密领导小组审查后，</p><p class="reader-word-layer reader-word-s6-1" style="width:3141px;height:294px;line-height:294px;top:5752px;left:5180px;z-index:35;letter-spacing:-0.5800000000000001px;false">交一把手书记签批手方可发布。</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:5752px;left:8210px;z-index:36;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:6252px;left:1442px;z-index:37;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:6252px;left:1667px;z-index:38;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:131px;height:294px;line-height:294px;top:6252px;left:1892px;z-index:39;">3</p><p class="reader-word-layer reader-word-s6-5" style="width:5383px;height:294px;line-height:294px;top:6252px;left:2023px;z-index:40;false">、严禁将任何涉密文件、信息等发布到国际互联网上。</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:6252px;left:7406px;z-index:41;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:6752px;left:1442px;z-index:42;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:6752px;left:1667px;z-index:43;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:131px;height:294px;line-height:294px;top:6752px;left:1892px;z-index:44;">4</p><p class="reader-word-layer reader-word-s6-1" style="width:4712px;height:294px;line-height:294px;top:6752px;left:2023px;z-index:45;letter-spacing:-0.56px;false">、严禁将案件、信访信息发布到国际互联网上。</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:6752px;left:6735px;z-index:46;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-1" style="width:2693px;height:294px;line-height:294px;top:7252px;left:1442px;z-index:47;letter-spacing:-0.51px;false">感谢阅读，希望能帮助您！</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:7252px;left:4135px;z-index:48;font-family:simsun;">&ensp;</p><p class="reader-word-layer reader-word-s6-3" style="width:66px;height:294px;line-height:294px;top:7752px;left:1442px;z-index:49;font-family:simsun;">&ensp;
</p></div></div></div></div></div></div>
</div>
<b class="bottom"><b class="bl"></b><b class="br"></b></b>
</div>

</div>



<div class="new-fc-container"></div>



<div id="sampling-area" style="display: block; position: absolute; top: -9999px; left: -9999px;">1234567890ABCDEFGHIJKLMNabcdefghijklmn!@#$%^&amp;&amp;*()_+.一三五七九贰肆陆扒拾，。青玉案元夕东风夜放花千树更吹落星如雨宝马雕车香满路凤箫声动玉壶光转一夜鱼龙舞蛾儿雪柳黄金缕笑语盈盈暗香去众里寻他千百度暮然回首那人却在灯火阑珊处 </div>
<span id="edit-docPrice" style="display:none;"></span>
<div class="6 doc-bottom-wrap complex  hidden-doc-banner" id="doc_bottom_wrap" style="display: block;">
<div class="bd" id="bottom-download" data-scale="0.70709782964164" data-render="1">
<div class="pay-page-inner reader-end-download bottom-core-wrap super-vip"><div class="doc-bottom-text">阅读已结束，下载本文需要</div>            <div class="doc-bottom-value"><div><span class="icon-ticket"></span>2下载券</div><div class="doc-bottom-ticket-rights">（您持有<span>0</span>下载券，积分不足无法兑换）</div></div>    <div class="doc-bottom-btns super-vip">                                <div class="btn-pay-vip"><i></i>VIP免券下载                <div class="new-user-discount-tip">VIP新客立减2元</div></div>    </div><div class="doc-bottom-tip super-vip"><div class="doc-bottom-rights-wrap"><span class="icon-triangle" style="left: 221.734px;"></span><div class="download-pro-doc"><i></i>享VIP专享文档下载特权</div><div class="download-share-doc"><i></i>赠共享文档下载特权</div><div class="yuedu-vip"><i></i>赠百度阅读VIP精品版</div></div></div></div>
<div class="wubai-wrap">
<div class="hengxian"></div>
<div class="wubai-title">
<span class="wubai-icon"></span>
<p>定制HR最喜欢的简历</p>
</div>
<a href="/org/browse/jianlidingzhi" target="_blank" title="" class="wubai-rukou log-xsend" data-logxsend="[1, 100844]">我要定制简历</a>
</div></div>
<div class="wkfc-wrap" style="display: block;"><div class="hengxian"></div><div class="fc-wrap fc-wrap-real-container"><div class="relate-title"><p class="content" style="display: none;"></p></div><div class="fc-inner"><style type="text/css">.zIZnAL {margin: 20px auto 30px;text-align: center;}.zIZnAL .jvunAH {margin-bottom: 20px;}.zIZnAL .sOWSwe {margin-right: 10px;font-size: 14px;color: #333;display: inline-block;overflow: hidden;white-space: nowrap;text-overflow: ellipsis;vertical-align: bottom;max-width: 320px;}.zIZnAL .sOWSwe font {color: #333!important;}.zIZnAL .WB_gPy {font-size: 13px;color: #666;}.zIZnAL .CvykjT {display: inline-block;border: 1px solid #2fad85;border-radius: 2px;}.zIZnAL .CvykjT a {display: block;padding: 12px 24px;font-size: 18px;color: #2fad86;background-color: #fff;}.zIZnAL .CvykjT a:hover {color: #fff;background-color: #2fad85;text-decoration: none;}</style><div class="zIZnAL"><div class="jvunAH JHErtw"><a class="sOWSwe" href="http://www.baidu.com/baidu.php?url=af0000aF4eAvq9HI8zrvvd48ROBgsV-jATZmlT5prEzVkdGUbHCYi8dzRS9tujaQlVLZ_IjOakhdq252k1XO1ueZsTAKSmtuPUuFZxZG819UHZEULwBZOfZO0yr5e-QM08ercYjEWUyQ3C1eBbP7wTmZDPBgHxUrRdF-8TS4AtPtqT1l7zx7tYtJbYDAyQ-vBMVxSTJo8Q3-B2qSV0.DR_NR2Ar5Od66uxGiOVH4R5C6HqamJDZ0hl4Sumh5ktSNnQV5KugztU5A1KYGWyAp7WFYq5ZcC0.U1Yk0ZDqzoQjVnWVE5lOzIQRd_URenO6_8D0TA-W5HD0IjvelTjkVXxgYtO6_8ZykVxL0A-V5HRLnsKM5gK1UMn0Iybq0ZKGujYY0APGujY4nsKVIjYs0AVG5H00TMfqP1DL0ANGujY0mhbqnW0Yg1nsn-t1njn0Uynqn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00Uy-b5H00pg7Y5H00mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uMfqn0KspjYs0Aq15H00mMTqn0K8IjYs0ZPl5fK9TdqGuAnqUMnVmLf0pywW5fKYIgnqnHDLnjn4PWf1rHDsnHRkP1b4njR0ThNkIjYkPHTknW61PWR4njRz0ZPGujYsnj0drHRknhuWPvP-uhfk0AP1UHdjrjNAnRckwDwawHf4wWfz0A7W5HD0TA3qn0KkUgfqrHb40Z7VT1Ys0ZGY5H00UyPxuMFEUHYs0Aw9UMNBuNqsUA78pyw15fKsmgwxuhk9u1Ys0AwWpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5H00uhPdIjYs0A-1mvsqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0AqY5H00ULFsIjYsc10Wc10Wnansc108nj0snj0sc10Wc100mLFW5HRLnHDL&amp;word=%E4%BB%80%E4%B9%88%E8%BD%AF%E4%BB%B6%E5%8F%AF%E4%BB%A5%E5%88%B6%E9%80%A0%E7%9B%B8%E5%86%8C" target="_blank">婚礼电子相册制作 - 免费预览,N多模版,一键生成大片</a><span class="WB_gPy">广告</span></div></div></div></div></div><script>(function(win){win.ecom = win.ecom || {};win.ecom.pl2 = win.ecom.pl2 || {};win.ecom.pl2.imTimesign = parseInt("87" || 0, 10);win.ecom.pl2.searchId = "00059512fc7cefd1";})(window);(function(a){function b(d){var c=location.href.match("debug=1");var g=window.jQuery||{};if(!c){try{d(a.pl2,g)}catch(f){}}else{d(a.pl2,g)}}a.pl2.run=function(d,c){if(c||arguments.length==1){bds.ready(function(){b(d)})}else{b(d)}};a.pl2.q=function(f,g){g=g||document;if(g.getElementsByClassName){return g.getElementsByClassName(f)}else{var d=[];var c=g.all||g.getElementsByTagName("*");var e=c.length;f=f.replace(/\-/g,"\\-");var h=new RegExp("(^|\\s)"+f+"(\\s|$)");while(--e>=0){if(h.test(c[e].className)){d.push(c[e])}}return d}}})(window.ecom);(function(v){var h=undefined,g=undefined;var l=0,k=0;var e=0;var o=0;var i=0;var d=0;var m=0;var b=0;var t=0;var r=/link\?url\=([^\&]+)/;var n=/\?url\=([^\.]+)\./;function s(){var y=t.href;var x=r.exec(y)||n.exec(y);return x?x[1]:false}function u(z){var x=s();if(x!==false){var y=q(x,z);p(y)}}function p(z){var x="&ck="+[z,e,b,l,k,h,g,m].join(".");if(t.href){var y=t.href;if(y.indexOf("&ck=")==-1){t.href+=x}else{t.href=y.replace(/&ck=[\d.]*/,x)}}}function q(A,C){var B=0;for(var z=0;z<(((e*C)%99)+9);z++){var y=A.length<20?A.length:20;B+=A.charCodeAt((b*z)%A.length)}return B}function w(x){x=x||window.event;e++;if(h===undefined){h=x.clientX}if(g===undefined){g=x.clientY}o=new Date().getTime()}function f(y,x){y=y||window.event;t=y.target||y.srcElement;while(t&&t.tagName!="A"){t=t.parentNode}i=new Date().getTime();b=9999;l=y.clientX;k=y.clientY;if(o===0){m=0}else{m=i-o}u(x)}function j(y,x){d=new Date().getTime();b=d-i;u(x)}function c(C,z,B){var A,x,y;for(y in z){A=z[y];x=B[y];if(window.attachEvent){C.attachEvent("on"+A,x)}else{C.addEventListener(A,x,false)}}}function a(x){return[function(y){w(y)},function(y){f(y,x)},function(y){j(y,x)}]}v.ck=function(B,A){if(B.length===undefined){B=[B]}var x=B.length;var y=0;var z=a(A);for(;y<x;y++){c(B[y],["mouseover","mousedown","mouseup"],z)}}})(window.ecom.pl2);window.ecom.pl2.run(function(c){var e=c.q("JHErtw");for(var b=0;b<e.length;b++){var a=e[b];var d=a.getElementsByTagName("A");c.ck(d,window.ecom.pl2.imTimesign)}},false);</script></div>
<div id="next_doc_box" class="hiddenForDownload" style="display: block;">
<a href="/view/ffba7dc2842458fb770bf78a6529647d272834aa.html?rec_flag=default" class="log-xsend" data-logxsend="[1, 100574, {index:2}]">
<span class="next_text">下一篇</span>
<i class="iconfont"></i>
</a>
</div>
<a class="ic reader-fullScreen xllDownloadLayerHit_left top-right-fullScreen" href="javascript:;" title="全屏显示" data-toolsbar-log="fullscreen" alog-action="htmltoolbar.fullscreen"></a></div>
<div id="shareWrap-1" style="display:none;">
<div id="shareMore-1" class="reader-share reader-tools-share" style="display: block;">
<dl>
<dt>把文档贴到Blog、BBS或个人站等：</dt>
<dd class="reder-code-box">
<input id="readerCode-1" onclick="this.select()" class="reader-code">
<a id="copyCode-1" href="javascript:void(0);" class="cp_btn logSend" data-logsend="{&quot;send&quot;:[&quot;view&quot;,&quot;share&quot;,{&quot;sns&quot;:&quot;web_player&quot;}]}">复制</a>
<span id="copyResult-1"></span>
<a id="viewReader-1" class="pre" href="javascript:void(0);">预览</a>
</dd>
<dd>
<input id="normalSize-1" name="reader-share" type="radio" checked="true">
<label for="normalSize-1">普通尺寸(450*500pix)</label>
<input id="bigSize-1" class="big" name="reader-share" type="radio" value="">
<label for="bigSize-1">较大尺寸(630*500pix)</label>
</dd>
</dl>
</div>
</div>
<form name="downloadForm" action="/user/submit/download" method="post" target="runDown">
<input name="ct" value="20008" type="hidden">
<input name="doc_id" value="e167fbacae45b307e87101f69e3143323968f5cc" type="hidden">
<input name="retType" value="newResponse" type="hidden">
<input name="sns_type" type="hidden">
<input type="hidden" name="storage" value="1">
<input type="hidden" name="useTicket" value="0">
<input type="hidden" name="target_uticket_num" value="0">
<input type="hidden" name="downloadToken" value="991b72f69eb82c25f453f3d643cf2e8d">
<input type="hidden" name="sz" value="19851">
<input type="hidden" name="v_code" value="0">
<input type="hidden" name="v_input" value="0">
<input type="hidden" name="req_vip_free_doc" value="0">
</form>
</div>
<div class="ft" style="width: 890px;">
<div style="position: relative;">
<div class="union-ad-bottom" id="wkgg" style="display: block; border: 0px;"><div class="bottom-plat-wrap"> <div class="bottom-plat-title">搜索推荐</div>  <a class="bottom-plat-ad" href="https://eduad.baidu.com/click/wenku_post_json?p=0l-37DNTj1fKt3qAe8n3o5v7PLN_7EPKok2lTFukec6ek_TEu-hW97VfkmqShf6X8mvr-a-GqlPx9kYxYcabv4LqD_Smip2vdyQiuxZ1_KVcVqKXfJaMWNaDlgBA3fgb7eOQyoDwv50zHhNXxHTBfGickD09EasgNuaeiyXBgI-CBgLlTR7Irh5vQ1E2LTkH2CpC_U55YWqNSCC8wsqs-3bRknr7pxrZn4Uxf-_vRXU5XIpXnM27TPow4OpYUn3y-dOqXCtY2tKvIhgM0R6l9LN0CO_KCKras85-ntE1fhjVXTWw7vQvJ-mspGGloILCCtqpGcwkWR7J12r1ZCmUfvQqwtct5z2_sW7V_La7asP3octAU-H169Qj1R_pDmpKbhriasHkddqfQMq_ELLL504Qw0gmThh2RqttaNyxXWywIBz17BoFgATTzkb5XxNgFJw_UwIFL4bM9TGkEt6SbQ==&amp;price=0&amp;lp=VDU-_bE4y9O75Fqy-TOY0Tfe6T4HMZwrPcei_VIih-puXAJB8x-2xDKPrE8QG_TuSua4Ynre4zjI09rSV0afvQ=="> <div class="bottom-plat-item"> <div class="bottom-plat-item-img"> <img src="https://edu-ad-test-cdn.cdn.bcebos.com/78baf201c5887ce857028f0819f611ff/e7709a2813ab33e7549e5c32837018a9.jpg"> </div> <div class="bottom-plat-item-content"> <p>2019年教师资格证《报考条件》公布——3类非师范生恐不能报名</p> <p>12118224人感兴趣</p> </div> </div> <div class="bottom-plat-item"> <div class="bottom-plat-item-img"> <img src="https://edu-ad-test-cdn.cdn.bcebos.com/a334c3217128fcd5bcdb1b1e0e617a48/abd6d80bf5a067e18e7a4b580291fcff.jpg"> </div> <div class="bottom-plat-item-content"> <p>2019年教师资格证报名时间即将截止——非师范生最后的机会</p> <p>12118224人感兴趣</p> </div> </div> <div class="bottom-plat-item"> <div class="bottom-plat-item-img"> <img src="https://edu-ad-test-cdn.cdn.bcebos.com/84e0e5e31feae5d5713316d9f2a8d2ed/c4978fc7ea27ffd76ff13c6eb91177ea.jpg"> </div> <div class="bottom-plat-item-content"> <p>2019年教师资格证考试科目增加3科——立即查看新增科目</p> <p>12118224人感兴趣</p> </div> </div> </a> </div></div><a class="ad-vip-close-bottom" data-unionad="" style="top: 19px;"></a>
</div>
<div class="kgrecommend-wrap"></div>
<div class="mod bottom-doc-list pt20 " id="bottom-doc-list-3">

<div class="hd">
<h4>你可能喜欢</h4>
</div>
<div class="bd stru-recom-new">
<div class="tagList-wrap">
<div class="tagList tabControl" alog-group="view.strurecom.tag.total">
<textarea id="tagList-template-3" style="display:none">                &lt;%for (var i = 0, len = data.length; i &lt; len; i++) {%&gt;
                    &lt;%var className = '';%&gt;
                    &lt;%if (i === 0) {%&gt;
                        &lt;%className = 'current';%&gt;
                    &lt;%}%&gt;
                    &lt;a href="javascript:;" class="&lt;%=className%&gt; logSend log-xsend"
                        title="&lt;%=util.encodeHTML((data[i]['tag_name']))%&gt;"
                        data-logsend="{'send':['view','tag_link',{'from':'srs','tag_no':'&lt;%=(i+1)%&gt;','ply':'xreader','doc_srs_strategy':'&lt;%=doc_srs_strategy%&gt;','doc_srs_tag':'&lt;%=doc_srs_tag%&gt;'}]}"
                        alog-action="view.strurecom.tag.&lt;%=i%&gt;"
                        data-logxsend="[1, 101465, {'index': '&lt;%=i + 1%&gt;', 'tagName': '&lt;%=encodeURIComponent(data[i].tag_name)%&gt;'}]"&gt;
                        &lt;%=util.cutString(data[i]['tag_name'],10,'...')%&gt;
                    &lt;/a&gt;
                &lt;%}%&gt;
                </textarea>
</div>
</div>
<div class="tabContent tableList data c-gray9">
<textarea id="tableList-template-3" style="display:none">
                &lt;% for (var i = 0, len = data.length; i &lt; len; i++) { %&gt;
                    &lt;%var status = 'disabled';%&gt;
                    &lt;% if (i == 0) {%&gt;
                        &lt;%status = 'current';%&gt;
                    &lt;%}%&gt;
                    &lt;%var docList = data[i]['related_doc_infos'];%&gt;
                    &lt;div class="&lt;%=status%&gt;"&gt;
                        &lt;div alog-group="view.strurecom.doc"&gt;
                            &lt;div class="guess-u-like"&gt;
                            &lt;%for (var j = 0, n = docList.length; j &lt; n; j++) {%&gt;
                                &lt;%// mark_pay_doc： 1：付费文档； 2：积分文档； 0：免费文档 %&gt;
                            
                                &lt;%var markPayDoc = 0;%&gt;
                                &lt;% if (+docList[j].pay_price) {%&gt;
                                    &lt;%var markPayDoc = 1;%&gt;
                                &lt;%} else if (+docList[j].docTicket) {%&gt;
                                    &lt;%var markPayDoc = 2;%&gt;
                                &lt;%}%&gt;
                                &lt;div class="txtL one-info-block"&gt;
                                    &lt;div class="image-wrap"&gt;
                                        &lt;a href="/view/&lt;%=docList[j]['doc_id']%&gt;.html"
                                            data-mark-pay-doc="&lt;%=markPayDoc%&gt;"
                                            target="_blank" class="logSend log-xsend fcClick"
                                            data-logsend="{'send':['view','doc_link',{'from':'srs','tag_no':'&lt;%=(i+1)%&gt;','ply':'xreader','doc_srs_strategy':'&lt;%=doc_srs_strategy%&gt;','doc_srs_tag':'&lt;%=doc_srs_tag%&gt;'}]}"
                                            data-logxsend="[1,100029,{'index':'&lt;%=j + 1%&gt;','click_doc_id':'&lt;%=docList[j]['doc_id']%&gt;', 'tagName':'&lt;%=encodeURIComponent(docList[j].title)%&gt;'}]"
                                            title="&lt;%=util.encodeHTML(docList[j].title)%&gt;"&gt;
                                            &lt;%if (docList[j]['cover_url']) {%&gt;
                                                &lt;img src="&lt;%=docList[j]['cover_url']%&gt;"&gt;
                                            &lt;%} else if (docType[docList[j]['doc_type']].toString() === 'ppt') {%&gt;
                                                &lt;img src="//wkstatic.bdimg.com/static/wkview/widget/stru_recom/image/default-image-ppt_f21179f.jpg"&gt;
                                            &lt;%} else {%&gt;
                                                &lt;img src="//wkstatic.bdimg.com/static/wkview/widget/stru_recom/image/default-image_f16d940.jpg"&gt;
                                            &lt;%}%&gt;
                                        &lt;/a&gt;
                                        &lt;b class="ic ic-type-icon ic-&lt;%=docType[docList[j]['doc_type']].toString()%&gt;"&gt;&lt;/b&gt;
                                    &lt;/div&gt;
                                    &lt;div class="doc-info-box"&gt;
                                        &lt;div class="doc-title"&gt;
                                            &lt;a href="/view/&lt;%=docList[j]['doc_id']%&gt;.html" target="_blank" class="logSend log-xsend fcClick"
                                                data-logsend="{'send':['view','doc_link',{'from':'srs','tag_no':'&lt;%=(i+1)%&gt;','ply':'xreader','doc_srs_strategy':'&lt;%=doc_srs_strategy%&gt;','doc_srs_tag':'&lt;%=doc_srs_tag%&gt;'}]}"
                                                data-logxsend="[1,100029,{'index':'&lt;%=j + 1%&gt;','click_doc_id':'&lt;%=docList[j]['doc_id']%&gt;', 'tagName':'&lt;%=encodeURIComponent(docList[j].title)%&gt;'}]"
                                                title="&lt;%=util.encodeHTML(docList[j].title)%&gt;"&gt;
                                                &lt;%=util.cutString(docList[j].title,25,'...')%&gt;
                                            &lt;/a&gt;
                                        &lt;/div&gt;
                                        &lt;div class="doc-other-info"&gt;
                                            &lt;%if (docList[j] &amp;&amp; docList[j]['qualityScore']) {%&gt;
                                                &lt;span class="doc-score"&gt;&lt;%=docList[j]['qualityScore']%&gt;&lt;/span&gt; 分
                                            &lt;%} else {%&gt;
                                                &lt;span class="doc-score"&gt;0.0&lt;/span&gt; 分
                                            &lt;%}%&gt;

                                            &lt;%if (docList[j] &amp;&amp; docList[j]['view_count']) {%&gt;
                                                &lt;span class="doc-view-count"&gt;&lt;%=docList[j]['view_count']%&gt;人阅读&lt;/span&gt;
                                            &lt;%} else {%&gt;
                                                &lt;span class="doc-view-count"&gt;0人阅读&lt;/span&gt;
                                            &lt;%}%&gt;
                                        &lt;/div&gt;
                                    &lt;/div&gt;
                                &lt;/div&gt;
                            &lt;%}%&gt;
                            &lt;/div&gt;
                        &lt;/div&gt;
                        &lt;div&gt;
                            &lt;p class="list-more" colspan="4"&gt;
                                &lt;a href="//wenku.baidu.com/search?word=&lt;%=data[i]['tag_name']%&gt;&amp;tn=SE_huins0007_nhui0007"
                                    title="&lt;%=data[i]['tag_name']%&gt;"
                                    target="_blank" class="logSend log-xsend"
                                    data-logxsend="[1, 100180, {'tagName': '&lt;%=encodeURIComponent(data[i].tag_name)%&gt;'}]"
                                    data-logsend="{'send':['view','more_link',{'from':'srs','tag_no':'&lt;%=(i+1)%&gt;','ply':'xreader','doc_srs_strategy':'&lt;%=doc_srs_strategy%&gt;','doc_srs_tag':'&lt;%=doc_srs_tag%&gt;'}]}"&gt;
                                    更多与“&lt;span&gt;&lt;%=data[i]['tag_name']%&gt;&lt;/span&gt;”相关的内容&gt;&gt;
                                &lt;/a&gt;
                            &lt;/p&gt;
                        &lt;/div&gt;
                    &lt;/div&gt;
                &lt;%}%&gt;
            </textarea>
</div>
</div>
</div>
<div id="doc-comment" class="doc-comment">
<h4>
您的评论<span class="star-act">
<b class="ct-star value-star ic-star-off"></b>
<b class="ct-star value-star ic-star-off"></b>
<b class="ct-star value-star ic-star-off"></b>
<b class="ct-star value-star ic-star-off"></b>
<b class="ct-star value-star ic-star-off"></b>
</span>
<span class="f-star"></span>
<span class="tip">*感谢支持，给文档评个星吧！</span>
</h4>
<div class="post-comment-wrap clearfix">
<div class="add-ct-tip">
<div class="add-ct-wrap">
<p style="padding:10px;">
<textarea class="post-comment-ipt" placeholder="写点评论支持下文档贡献者~"></textarea>
</p>
<p class="length-tip">240</p>
</div>
<a class="add-new-btn post-comment-btn" href="javascript:void(0);">发布评论</a>
<div id="captcha-wrap" style="display:none;">
<input id="v_input" placeholder="输入验证码" name="v_input">
<img id="captcha">
<a class="change-captcha" href="javascript:void(0);">换一换</a>
<input type="hidden" id="v_code" name="v_code">
</div>
<p class="tip"></p>
</div>
</div>
<div class="comment-wrap">
<h4>
用户评价<span class="ct-num"></span>
</h4>
<p class="loading" style="display: none;">评论加载中...</p>
<ul class="comment-list hide" id="comment-list" style="display: block; margin-top: -10px;">
    
        <li class="no-comment">暂无评论</li>
    
</ul>
</div>
</div>
<div id="pager"><div class="ui-pager pager-center"><div class="pager"><div class="pager-inner"></div></div></div></div>
<script type="text/template" id="comment-item-tpl">
    <div class="ct-item-wrap">
        <div class="clearfix ct-con-wrap">
            <div class="ct-extra-into">
                <p><%= create_time %></p>
                <p>
                    <% if ( "小虫很酷" == uname ) { %>
                        <a href="javascript:void(0);" class="delete-btn">删除</a>
                    <% } %>
                    <a href="javascript:void(0);" class="reply-btn">回复 (<span class="ry-num">0</span>)</a>
                </p>
            </div>

            <div class="ct-con">
                <div class="avatar-wrap">
                    <div>
                        <a href="<%= url %>" target="_blank"><img class="avatar" src="<%= avatar %>" /></a>
                    </div>
                </div>
                <div class="main-con">
                    <p>
                        <span class="ct-star" >
                            <% var onNum = Math.ceil( star ); %>
                            <% var offNum = 5 - onNum; %>
                            <% for ( var i = 0; i < onNum; i++ ) { %>
                                <b class="ic-star-score star-score-on"></b>
                            <% } %>
                            <% for ( var i = 0; i < offNum; i++ ) { %>
                                <b class="ic-star-score star-score-off"></b>
                            <% } %>
                        </span>
                        <a class="uname" href="<%= url %>" target="_blank"><%= tname %></a>

                        <% if ( oInfo.org_name ) { %>
                            <span class="bg-comment ic-over"></span>
                        <% } else if ( title ) { %>
                            <span class="bg-comment ic-ver"></span>
                            <span class="title"><%= title %></span>
                        <% } %>
                    </p>
                    <div class="ct-atc">
                        <p><%- content %></p>
                    </div>
                </div>
            </div>
        </div>

        <div class="reply-wrap">
            <div class="bg-comment ic-arrow"></div>
            <div class="post-reply clearfix">
                <a class="add-new-btn post-reply-btn" href="javascript:void(0);">回复</a>
                <input type="text" class="post-reply-ipt" />
            </div>

            <div class="info-tip clearfix">
                <p class="error-tip"></p>
                <p class="reply-num">共<%= reply_count %>条回复</p>
            </div>

            <ul class="reply-list">

            </ul>
        </div>
    </div>
</script>
<script type="text/template" id="comment-list-tpl">
    <% if ( commentList.length > 0 ) { %>
        <% _.each( commentList, function( item ) { %>
            <li class="ct-item" data-reply-id="<%= item.reply_id %>" id="item-<%= item.reply_id %>">
                <div class="ct-item-wrap">
                    <div class="clearfix ct-con-wrap">
                        <div class="ct-extra-into">
                            <p><%= item.create_time %></p>
                            <p>
                                <% if ( "小虫很酷" == item.uname || item.is_uid_admin ) { %>
                                    <a href="javascript:void(0);" class="delete-btn">删除</a>
                                <% } %>
                                <a href="javascript:void(0);" class="reply-btn">
                                    回复 (<span class="ry-num"><%= item.reply_count %></span>)
                                </a>
                            </p>
                        </div>

                        <div class="ct-con">
                            <div class="avatar-wrap">
                                <div>
                                    <a href="<%= item.url %>" target="_blank">
                                        <img class="avatar" src="<%= item.avatar %>" />
                                    </a>
                                </div>
                            </div>
                            <div class="main-con">
                                <p>
                                    <span class="ct-star" >
                                        <% var onNum = Math.ceil( item.star ); %>
                                        <% var offNum = 5 - onNum; %>
                                        <% for ( var i = 0; i < onNum; i++ ) { %>
                                            <b class="ic-star-score star-score-on"></b>
                                        <% } %>
                                        <% for ( var i = 0; i < offNum; i++ ) { %>
                                            <b class="ic-star-score star-score-off"></b>
                                        <% } %>
                                    </span>
                                    <a class="uname" href="<%= item.url %>" target="_blank"><%= item.tname %></a>

                                    <% if ( item.oInfo.org_name ) { %>
                                        <span class="bg-comment ic-over"></span>
                                    <% } else if ( item.title ) { %>
                                        <span class="bg-comment ic-ver"></span>
                                        <span class="title"><%= item.title %></span>
                                    <% } %>
                                </p>
                                <div class="ct-atc">
                                    <p><%- item.content %></p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="reply-wrap">
                        <div class="bg-comment ic-arrow"></div>
                        <div class="post-reply clearfix">
                            <a class="add-new-btn post-reply-btn" href="javascript:void(0);">回复</a>
                            <input type="text" class="post-reply-ipt" />
                        </div>

                        <div class="info-tip clearfix">
                            <p class="error-tip"></p>
                            <p class="reply-num">共<%= item.reply_count %>条回复</p>
                        </div>

                        <ul class="reply-list">

                        </ul>
                    </div>
                </div>
            </li>
        <% } ); %>
    <% } else { %>
        <li class="no-comment">暂无评论</li>
    <% } %>
</script>
<script type="text/template" id="reply-item-tpl">
    <div class="ry-item-wrap">
        <p class="date">
            <%= create_time %><br/>
            <% if ( "小虫很酷" == uname ) { %>
                <a href="javascript:void(0);" class="delete-btn delete-reply-btn">删除</a>
            <% } %>
        </p>

        <div class="reply-info">
            <p>
                <a class="uname" href="<%= url %>" target="_blank"><%= tname %></a>

                <% if ( oInfo.org_name ) { %>
                    <span class="bg-comment ic-over"></span>
                <% } else if ( title ) { %>
                    <span class="bg-comment ic-ver"></span>
                    <span class="title"><%= title %></span>
                <% } %>
            </p>
            <div class="ct-atc">
                <p><%- content %></p>
            </div>
        </div>
    </div>
</script>
<script type="text/template" id="reply-list-tpl">
    <% _.each( replyList, function( item, key ) { %>
        <li class="ry-item clearfix <% if ( key == replyList.length - 1 ) { %> last <%}%>"
            data-reply-id="<%= item.reply_id %>" id="item-<%= item.reply_id %>"
        >
            <div class="ry-item-wrap">
                <p class="date">
                    <%= item.create_time %><br/>
                    <% if ( "小虫很酷" == item.uname ) { %>
                        <a href="javascript:void(0);" class="delete-btn delete-reply-btn">删除</a>
                    <% } %>
                </p>

                <div class="reply-info">
                    <p>
                        <a class="uname" href="<%= item.url %>" target="_blank"><%= item.tname %></a>
                        <% if ( item.oInfo.org_name ) { %>
                            <span class="bg-comment ic-over"></span>
                        <% } else if ( item.title ) { %>
                            <span class="bg-comment ic-ver"></span>
                            <span class="title"><%= item.title %></span>
                        <% } %>
                    </p>
                    <div class="ct-atc">
                        <p><%- item.content %></p>
                    </div>
                </div>
            </div>
        </li>
    <% } ); %>
</script>
<div style="position: relative; display: inline-block;">
<div id="ggbtm" style="padding-top: 0px; overflow: hidden; width: 890px;"><div class="fc-parallax-scrolling">              <div class="fc-parallax-scrolling-wrapper" style="top: -88px;">                              <a class="fc-parallax-scrolling-run fc-parallax-scrolling-without-image fc-parallax-scrolling-d9b779 fc-link" href="http://www.baidu.com/baidu.php?url=af0000aF4eAvq9HI8keXk3neeXgsqDctk5DLaEZGmieE3zvjaY7PMGx6pAFVqPPH13O7Fnb-2qLkKDy60drQxzj4Sg8JTLoryR9snYklEwHyYROo7nw7t3NOnmStIDUd3BRraXNXZXNjVdR0SRcjIy2vjFWkZGqUe11tEXgNkcqoCS4Iqk2dn2cmplImA_xEO1xNx-kzTs-1_VVeh6.DD_NR2Ar5Od663rj6tGbkHFB9JiBa596WuCGWel4hQe8yPrMofdTEUBmo3e8h1IELe81GolYPgQjPfm3dqMuk345ZIgblYPgQGCRAnMy9J4TTH7p-muCyr5uu_tN.U1Yz0ZDq_eg7k_gDsEitvsKspynqnfKY5TM8vqJ1VTASkTHaq0KGUHYknjTL0ATqILP8TsKdpHY0TA-b5Hf0mv-b5Hb10AdY5H00pvbqn0KzIjYLnHT0uy-b5HbsnW0z0AFG5HcsP0KVm1Ys0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0KVpyfqn0KGTgfqn0K9mWYsg100ugFM5H00TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KhIjYs0ZKC5H00ULnqn0KBI1Ys0A4Y5H00TLCq0A71gv-bm1d8TzdWUfKGuAnq0ZwdT1YknH6YnHRYP164nWm4PHcvnWD4PfKzug7Y5HDdP1DzrjnvPH64rjT0Tv-b5H0snjR4PHDzuhnvmHfvrAf0mLPV5Rn3PRmkfW7DwDF7Pj-APjc0mynqnfKsUWYs0Z7VIjY4rHb0Tyd15H00XMfqn0KVmdqhThqV5H00uA78IyF-gLK_my4GuZnq0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00pgPWUjYs0ZGsUZN15H00mywhUA7M5HD0UAuW5H00UvnqnfKEIjYk0AqzTZfqnBnsc1nWnin4P1R3P1T4c1DYn1Rkc108nj0snj0sc1DWnans0APzm1YkP1cvn6&amp;word=%E8%BD%A6%E7%89%8C%E6%8B%8D%E5%8D%96%E4%BB%B7">                     <div class="fc-parallax-scrolling-text">                         <div class="fc-parallax-scrolling-title fc-parallax-scrolling-text-line">深圳车辆拍卖 人人车-靠谱                         </div>                         <div class="fc-parallax-scrolling-content">                             <span class="fc-parallax-scrolling-tag">广告</span>                             <span class="fc-parallax-scrolling-sub fc-parallax-scrolling-text-line">深圳车辆拍卖人人车一键购车"零"首付,可分期,门槛低,买车上「人人车」</span>                             <span class="fc-parallax-scrolling-bogus">查看详情 &gt;</span></div>                     </div>                 </a>                                           <a class="fc-parallax-scrolling-run fc-parallax-scrolling-without-image fc-parallax-scrolling-25ae84 fc-link" href="http://www.baidu.com/baidu.php?url=af0000aF4eAvq9HI8s8K6lcY9u_K9H2atfpoKniz6_yBqD977c9DbV9efoKJRTIxGbSA5Eh4KhsS6QsLC_OzatOeY4GHeYRN39kyGIRnOC4BSEh8AO3YGV3crR-Owspx39RNVwmk1PxEc0JC5IVNTe2e6XkEF4PTp3vJk0XpwuCx_ZI--aL8XZn6pi2BIU-6t2d2jTJuTmLy7bHf36.DR_iwGY3vIixQN6u3gC6Y_1IJpDDzUM1F9CI3yXyPBPrM-Eukmc3S_Q5QDksYTTQCTT5QGuxjRMfMoWC_YPUGVQ7xy7M-eRlrKYdvFWub_tIS1uE_lTMy7M-CFhY_x3EegqUOzO3xYOkxeJ-muCy2e5ZIv20.U1Yk0ZDq_eg7k_gDsEitvsKspynqnfKY5TgDsEi1VTAS0A-V5HDsP1T0u1dLTv410ZNG5fKspyfqP0KWpyfqrHn0Ugfqn0KopHYs0ZFY5HTkPsK-pyfqrH0znjc0mhbqnW0Y0AdW5H00TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0AdGujYs0A-kIjYs0A7B5HKxn0K-ThTqn0KsTjYs0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0AuY5H00TA6qn0KET1Ys0AFL5H00UMfqn0K1XWY0mgPxpywW5y41QyPV0A-bm1Y0IZN15HD3nHbzP1DsrHcvPjm4n1TLrHc40ZF-TgfqnHRLnHc3n1mdrjb3PsK1pyfqnj0sPHbdnHFhm1u9Pjm3u0KWTvYqf16dwW7anRwDfbRYrRmYn6K9m1Yk0ZK85H00TydY5Hb4rfKkUgnqn0KlIjYs0AdWgvuzUvYqn0Kbmy4dmhNxTAk9Uh-bT1Y0TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KGTvP_5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KEm1Yk0AqY5HD0ULFsIjYkc1DWnznzc1nsrjTdnWTWPH0snanknH0sna3snj0snj0Wninsc100mLFW5HnkrHnY&amp;word=%E8%BD%A6%E7%89%8C%E6%8B%8D%E5%8D%96%E4%BB%B7">                     <div class="fc-parallax-scrolling-text">                         <div class="fc-parallax-scrolling-title fc-parallax-scrolling-text-line">拍卖车辆-瓜子二手车官网!                         </div>                         <div class="fc-parallax-scrolling-content">                             <span class="fc-parallax-scrolling-tag">广告</span>                             <span class="fc-parallax-scrolling-sub fc-parallax-scrolling-text-line">免费卖二手车,平均7天售出;100%个人车源,259项检测,30天可退,每分钟成交一辆!</span>                             <span class="fc-parallax-scrolling-bogus">查看详情 &gt;</span></div>                     </div>                 </a>                      </div>      </div> </div>
<a class="ggbtm-vip-close" style="top: 0;"></a>
</div>
</div>
</div>
<b class="bottom"><b class="bl"></b><b class="br"></b></b>
</div>

<div class="ys-ads-mask">
</div>

</div>


<div class="aside aside-v3">

<div class="aside-wrap ">
<div class="doc-upload  no-doc-desc" id="doc-upload" data-login="1">
<a id="uploadDoc-2" href="/new?fr=view" class="ic view-sps btn-upload btn-upload-new log-xsend" data-logxsend="[1,100602]" alog-action="view.uploadbtn" target="_blank"><span class="opennew">上传文档</span></a>
<div class="new-upload-btns">
<a class="log-xsend" data-logxsend="[1, 101746,{index: 5}]" href="/new?fr=view" target="_blank">本地上传</a>
<a class="create-doc log-xsend" data-logxsend="[1, 101746,{index: 6}]" href="/user/browse/editordoc?fr=view" target="_blank">创建文档<span class="ui-bz-new-ic"></span></a>
</div>
</div>
<div class="doc-aside-border" id="doc-aside-border">
<a id="wkad18" class="mt10 ad-area log-xsend" data-logxsend="[1,100619]" style="text-align:center;display:block">   </a>
<div class="goldclue-wrap"></div>
<div id="tm-placeholder-TANGRAM$5" style="display: block; width: 200px; height: 0px;"></div><div id="fixed-box" class="fixing-box" style="position: fixed; top: 35px; width: 200px; z-index: 999; left: 992.5px;">
<div class="service-entry"></div>
<div id="view-like-recom"><div id="__elm_view-like-recom__qk_1"><div class="mod page-doc-list relate-doc ">
<b class="top"><b class="tl"></b><b class="tr"></b></b>
<div class="inner">

<div class="hd clearfix">
<div class="act page-control">
<span class="page-info">
<span id="pageNum-4-relate" class="current-page">1</span>
<span class="tail-info">/3</span>
</span>
<span class="tabControl" alog-group="view.relatedoc.page">
<a id="pagePre-4-relate" class="view-sps pre-null" href="javascript:void(0);"></a>
<a id="pageNext-4-relate" class="view-sps next" href="javascript:void(0);"></a>
</span>
</div>
<h4>
<a href="//wenku.baidu.com/search?word=%C9%E6%C3%DC%BC%C6%CB%E3%BB%FA%B9%DC%C0%ED%D6%C6%B6%C8&amp;lm=0&amp;od=0" class="title-update" target="_blank">
相关文档推荐</a>
</h4>
</div>
<div class="bd">
<ul id="pageList-4-relate" class="tabContent relate_doc_list" alog-group="view.relatedoc.doc">
<li class="current" id="add-new">
<div class="item frist-item view-like-recom-fc"><style type="text/css">.InzQEF {padding: 0;}.JzOTib {display: block;position: relative; text-decoration: none;}.JzOTib:hover .DOtAyS{text-decoration: underline;}.xO_AFl {display: flex;flex-wrap: wrap;color: #333;}.gl-display {display: flex;}.ercEQI {width: 15px;height: 15px; vertical-align: middle;align-items: center; display: inline-block;background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QAAAAAAAD5Q7t/AAAACXBIWXMAAAsSAAALEgHS3X78AAABoUlEQVQ4y5XUv0sXQBjH8dd9MyFBKkgShwoiAmkIbnMoCIoim0PCqaCt1ptqCm4N+hciiFIILFqidk+npsAMQiMoCBL5pnENnfIl8is+291z934+z4+7EHMtGMKmvdsA1gYwgil86XO4W1L4vLWIuY7hAEbxeAArmC8pdPuFjLlexgQWSwqzbW8VKx10cHgXwEu8wg3MxFxfN9d+dDq7JR1zXcQVnCgpnMRRXIq53i4p/NBU9AO8w3hJIZQUPkFJ4SveNFX6QmKu93AOF2Oux/9xX8Dz3hbtZPdxC9+wHHM9g+XWiKWSwsOY63Cvkn09Ct7GXK+2SNMlhfeYwSOM4yNOt+MHe5WsN8ALnMc07mA15jqBByhYKCmc7VG7uQ0pKXyPuU7iGsZKCqsNGlFbe5+WFH7/L+/ewk7hwxagwRfwBIMlhes7Fa8XMotTMdfRpmKwTeRImw19ITHXQyWFZ5hrdZhHFxs4UlLY2A1SEZr8SdzEAu6WFI6VFGqf+2uoIea65O9Yr2C9pLD9JcRcA4Z3AFSMYS60t/ETv+zdBjH0B+CnmSRP5TRwAAAAAElFTkSuQmCC') center no-repeat;background-size:cover;filter: progid:DXImageTransform.Microsoft.AlphaImageLoader(src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QAAAAAAAD5Q7t/AAAACXBIWXMAAAsSAAALEgHS3X78AAABoUlEQVQ4y5XUv0sXQBjH8dd9MyFBKkgShwoiAmkIbnMoCIoim0PCqaCt1ptqCm4N+hciiFIILFqidk+npsAMQiMoCBL5pnENnfIl8is+291z934+z4+7EHMtGMKmvdsA1gYwgil86XO4W1L4vLWIuY7hAEbxeAArmC8pdPuFjLlexgQWSwqzbW8VKx10cHgXwEu8wg3MxFxfN9d+dDq7JR1zXcQVnCgpnMRRXIq53i4p/NBU9AO8w3hJIZQUPkFJ4SveNFX6QmKu93AOF2Oux/9xX8Dz3hbtZPdxC9+wHHM9g+XWiKWSwsOY63Cvkn09Ct7GXK+2SNMlhfeYwSOM4yNOt+MHe5WsN8ALnMc07mA15jqBByhYKCmc7VG7uQ0pKXyPuU7iGsZKCqsNGlFbe5+WFH7/L+/ewk7hwxagwRfwBIMlhes7Fa8XMotTMdfRpmKwTeRImw19ITHXQyWFZ5hrdZhHFxs4UlLY2A1SEZr8SdzEAu6WFI6VFGqf+2uoIea65O9Yr2C9pLD9JcRcA4Z3AFSMYS60t/ETv+zdBjH0B+CnmSRP5TRwAAAAAElFTkSuQmCC',sizingMethod='scale');/*兼容ie8以下*/-ms-filter: "progid:DXImageTransform.Microsoft.AlphaImageLoader(src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAARCAYAAAA7bUf6AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QAAAAAAAD5Q7t/AAAACXBIWXMAAAsSAAALEgHS3X78AAABoUlEQVQ4y5XUv0sXQBjH8dd9MyFBKkgShwoiAmkIbnMoCIoim0PCqaCt1ptqCm4N+hciiFIILFqidk+npsAMQiMoCBL5pnENnfIl8is+291z934+z4+7EHMtGMKmvdsA1gYwgil86XO4W1L4vLWIuY7hAEbxeAArmC8pdPuFjLlexgQWSwqzbW8VKx10cHgXwEu8wg3MxFxfN9d+dDq7JR1zXcQVnCgpnMRRXIq53i4p/NBU9AO8w3hJIZQUPkFJ4SveNFX6QmKu93AOF2Oux/9xX8Dz3hbtZPdxC9+wHHM9g+XWiKWSwsOY63Cvkn09Ct7GXK+2SNMlhfeYwSOM4yNOt+MHe5WsN8ALnMc07mA15jqBByhYKCmc7VG7uQ0pKXyPuU7iGsZKCqsNGlFbe5+WFH7/L+/ewk7hwxagwRfwBIMlhes7Fa8XMotTMdfRpmKwTeRImw19ITHXQyWFZ5hrdZhHFxs4UlLY2A1SEZr8SdzEAu6WFI6VFGqf+2uoIea65O9Yr2C9pLD9JcRcA4Z3AFSMYS60t/ETv+zdBjH0B+CnmSRP5TRwAAAAAElFTkSuQmCC',sizingMethod='scale')";}.DOtAyS {margin-left: 8px; display: inline-block;}.oUtzge {flex: 1;flex-direction: column;overflow: hidden;word-break: break-word;justify-content: space-around;}.oUtzge h1 {margin: 0;font-size: 14px; color: #333;}.oUtzge h1 em {color: #ff9c00;}.oUtzge p { margin-left:23px;font-size: 12px; height:22px; line-height:18px; vertical-align:top;color: #999;}.oUtzge .eRbypq{overflow: hidden;text-overflow:ellipsis;-o-text-overflow:ellipsis;-webkit-text-overflow:ellipsis;-moz-text-overflow:ellipsis;word-wrap: break-word;white-space: nowrap;display: inline-block;max-width: 130px;vertical-align: middle;}.AkMoXe {margin-left:15px;color: #666;display: inline-block;vertical-align: middle;}</style><div class="InzQEF nOSvkR KNkTOH"><a class="JzOTib" href="http://www.baidu.com/baidu.php?url=af0000aF4eAvq9HI8YAHm9TU3XwEkrX83dGsGHKXCAF4knLx8o1GL6HDiLiyW-oDCE6n2MUtOXpNGgWMRdL6ejFN0B3QR-MuaA1TD47015fIsPWat2Iz2gzKfx_vVCrvAP9hS43Gzk3BjEuuEv3jBTITMc9-Bba4Rky9beM8PKhCowq4l58_9H7IIx2zTpMi7qWJpAANpJ6lBl34f0.DR_NR2Ar5Od66uxGiOVH4R5C6HqamJDZ0hl4Sumh5ktSNnQV5KugztU5A1KYGWyAp7WFYq5ZcC0.U1Yk0ZDqzoQjVnWVE5lOzIQRd_URenO6_8D0TA-W5HD0IjvelTjkVXxgYtO6_8ZykVxL0A-V5HR1rfKM5gK1UMn0Iybq0ZKGujYY0APGujY4nsKVIjYs0AVG5H00TMfqP1DL0ANGujY0mhbqnW0Yg1nsn-t1njn0Uynqn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00Uy-b5H00pg7Y5H00mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uMfqn0KspjYs0Aq15H00mMTqn0K8IjYs0ZPl5fK9TdqGuAnqUMnVmLf0pywW5fKYIgnqnHDLnjn4PWf1rHDsnHRkP1b4njR0ThNkIjYkPHTknW61PWR4njRz0ZPGujYsnj0drHRknhuWPvP-uhfk0AP1UHdjrjNAnRckwDwawHf4wWfz0A7W5HD0TA3qn0KkUgfqrHb40Z7VT1Ys0ZGY5H00UyPxuMFEUHYs0Aw9UMNBuNqsUA78pyw15fKsmgwxuhk9u1Ys0AwWpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5H00uhPdIjYs0A-1mvsqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0AqY5H00ULFsIjYsc10Wc10Wnansc108nj0snj0sc10Wc100mLFW5HmzPWT4&amp;word=%E4%BB%80%E4%B9%88%E8%BD%AF%E4%BB%B6%E5%8F%AF%E4%BB%A5%E5%88%B6%E9%80%A0%E7%9B%B8%E5%86%8C&amp;shh=wenku.baidu.com" target="_blank"><div class="xO_AFl"><div class="oUtzge gl-display"><h1 class="j-contain-h1"><span class="ercEQI"></span><span class="DOtAyS">婚礼电子相册制作 - 免..</span></h1><p class="j-contain-desc"><span class="eRbypq" style="*cursor: pointer">www.aimeike.tv</span><span class="AkMoXe">广告</span></p></div></div></a></div></div>
<div class="item">
<div id="wk_sid" style="display:block;">
<p class="doc-title">
<b class="ic ic-doc"></b>
<a href="/view/8a9141ad4a35eefdc8d376eeaeaad1f346931198.html?rec_flag=default" class="rec-items A-relate-doc logSend log-xsend " data-logsend="{&quot;send&quot;:[&quot;view&quot;,&quot;relateDoc&quot;,{&quot;from&quot;:&quot;related&quot;,&quot;right&quot;:&quot;docClick&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;listNo&quot;:&quot;1&quot;,&quot;ply&quot;:&quot;html&quot;,&quot;price&quot;:&quot;0&quot;}]}" price="0" data-index="3" data-source-id="8a9141ad4a35eefdc8d376eeaeaad1f346931198" data-click-docid="8a9141ad4a35eefdc8d376eeaeaad1f346931198" data-list-docids="8a9141ad4a35eefdc8d376eeaeaad1f346931198,961fdda786c24028915f804d2b160b4e777f8169,5a6f0accbf1e650e52ea551810a6f524ccbfcba8,ffba7dc2842458fb770bf78a6529647d272834aa,3c4bb9c5b207e87101f69e3143323968011cf4bb,ae723ba42bf90242a8956bec0975f46526d3a757,f56e535c82d049649b6648d7c1c708a1294a0a09,a71d3856a0c7aa00b52acfc789eb172ded6399ad,f75d48ba11661ed9ad51f01dc281e53a580251ae,77e372bb91c69ec3d5bbfd0a79563c1ec4dad74c" data-price-type="2" data-relate-doccomposition="0,10,0" data-mark-pay-doc="2" target="_blank" title="涉密计算机管理制度精品资料" data-score-mode="">
涉密计算机管理制度精品...
</a>
</p>
<div class="gd-g tail-info">
<div class="gd-g-u gd-u-3-8 0">
<span title="3分，1人评">
<b class="ic ic-star-s-on"></b><b class="ic ic-star-s-on"></b><b class="ic ic-star-s-on"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b>
</span>
</div>
<div class="gd-g-u gd-u-1-4 pd-l-6">
27页</div>
<div class="gd-g-u pd-l-12 gd-u-7-24"></div>
</div>
</div>
<div id="wkad4" style="text-align:center;"></div>
</div>
<div class="item">
<div id="wk_sid" style="display:block;">
<p class="doc-title">
<b class="ic ic-doc"></b>
<a href="/view/961fdda786c24028915f804d2b160b4e777f8169.html?rec_flag=default" class="rec-items A-relate-doc logSend log-xsend " data-logsend="{&quot;send&quot;:[&quot;view&quot;,&quot;relateDoc&quot;,{&quot;from&quot;:&quot;related&quot;,&quot;right&quot;:&quot;docClick&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;listNo&quot;:&quot;2&quot;,&quot;ply&quot;:&quot;html&quot;,&quot;price&quot;:&quot;0&quot;}]}" price="0" data-index="4" data-source-id="961fdda786c24028915f804d2b160b4e777f8169" data-click-docid="961fdda786c24028915f804d2b160b4e777f8169" data-list-docids="8a9141ad4a35eefdc8d376eeaeaad1f346931198,961fdda786c24028915f804d2b160b4e777f8169,5a6f0accbf1e650e52ea551810a6f524ccbfcba8,ffba7dc2842458fb770bf78a6529647d272834aa,3c4bb9c5b207e87101f69e3143323968011cf4bb,ae723ba42bf90242a8956bec0975f46526d3a757,f56e535c82d049649b6648d7c1c708a1294a0a09,a71d3856a0c7aa00b52acfc789eb172ded6399ad,f75d48ba11661ed9ad51f01dc281e53a580251ae,77e372bb91c69ec3d5bbfd0a79563c1ec4dad74c" data-price-type="2" data-relate-doccomposition="0,10,0" data-mark-pay-doc="2" target="_blank" title="涉密计算机管理检查记录表" data-score-mode="">
涉密计算机管理检查记录...
</a>
</p>
<div class="gd-g tail-info">
<div class="gd-g-u gd-u-3-8 0">
<span title="2分，1人评">
<b class="ic ic-star-s-on"></b><b class="ic ic-star-s-on"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b>
</span>
</div>
<div class="gd-g-u gd-u-1-4 pd-l-6">
2页</div>
<div class="gd-g-u pd-l-12 gd-u-7-24"></div>
</div>
</div>
<div id="wkad4" style="text-align:center;"></div>
</div>
<div class="item">
<div id="wk_sid" style="display:block;">
<p class="doc-title">
<b class="ic ic-doc"></b>
<a href="/view/5a6f0accbf1e650e52ea551810a6f524ccbfcba8.html?rec_flag=default" class="rec-items A-relate-doc logSend log-xsend " data-logsend="{&quot;send&quot;:[&quot;view&quot;,&quot;relateDoc&quot;,{&quot;from&quot;:&quot;related&quot;,&quot;right&quot;:&quot;docClick&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;listNo&quot;:&quot;3&quot;,&quot;ply&quot;:&quot;html&quot;,&quot;price&quot;:&quot;0&quot;}]}" price="0" data-index="5" data-source-id="5a6f0accbf1e650e52ea551810a6f524ccbfcba8" data-click-docid="5a6f0accbf1e650e52ea551810a6f524ccbfcba8" data-list-docids="8a9141ad4a35eefdc8d376eeaeaad1f346931198,961fdda786c24028915f804d2b160b4e777f8169,5a6f0accbf1e650e52ea551810a6f524ccbfcba8,ffba7dc2842458fb770bf78a6529647d272834aa,3c4bb9c5b207e87101f69e3143323968011cf4bb,ae723ba42bf90242a8956bec0975f46526d3a757,f56e535c82d049649b6648d7c1c708a1294a0a09,a71d3856a0c7aa00b52acfc789eb172ded6399ad,f75d48ba11661ed9ad51f01dc281e53a580251ae,77e372bb91c69ec3d5bbfd0a79563c1ec4dad74c" data-price-type="2" data-relate-doccomposition="0,10,0" data-mark-pay-doc="2" target="_blank" title="涉密计算机保密管理制度" data-score-mode="">
涉密计算机保密管理制度
</a>
</p>
<div class="gd-g tail-info">
<div class="gd-g-u gd-u-3-8 0">
<span title="1分，1人评">
<b class="ic ic-star-s-on"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b>
</span>
</div>
<div class="gd-g-u gd-u-1-4 pd-l-6">
2页</div>
<div class="gd-g-u pd-l-12 gd-u-7-24"></div>
</div>
</div>
<div id="wkad4" style="text-align:center;"></div>
</div>
<div class="item">
<div id="wk_sid" style="display:block;">
<p class="doc-title">
<b class="ic ic-doc"></b>
<a href="/view/ffba7dc2842458fb770bf78a6529647d272834aa.html?rec_flag=default" class="rec-items A-relate-doc logSend log-xsend " data-logsend="{&quot;send&quot;:[&quot;view&quot;,&quot;relateDoc&quot;,{&quot;from&quot;:&quot;related&quot;,&quot;right&quot;:&quot;docClick&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;listNo&quot;:&quot;4&quot;,&quot;ply&quot;:&quot;html&quot;,&quot;price&quot;:&quot;0&quot;}]}" price="0" data-index="6" data-source-id="ffba7dc2842458fb770bf78a6529647d272834aa" data-click-docid="ffba7dc2842458fb770bf78a6529647d272834aa" data-list-docids="8a9141ad4a35eefdc8d376eeaeaad1f346931198,961fdda786c24028915f804d2b160b4e777f8169,5a6f0accbf1e650e52ea551810a6f524ccbfcba8,ffba7dc2842458fb770bf78a6529647d272834aa,3c4bb9c5b207e87101f69e3143323968011cf4bb,ae723ba42bf90242a8956bec0975f46526d3a757,f56e535c82d049649b6648d7c1c708a1294a0a09,a71d3856a0c7aa00b52acfc789eb172ded6399ad,f75d48ba11661ed9ad51f01dc281e53a580251ae,77e372bb91c69ec3d5bbfd0a79563c1ec4dad74c" data-price-type="2" data-relate-doccomposition="0,10,0" data-mark-pay-doc="2" target="_blank" title="涉密和非涉密计算机保密管理制度" data-score-mode="">
涉密和非涉密计算机保密...
</a>
</p>
<div class="gd-g tail-info">
<div class="gd-g-u gd-u-3-8 0">
<span title="0.5分，1人评">
<b class="ic ic-star-s-half"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b>
</span>
</div>
<div class="gd-g-u gd-u-1-4 pd-l-6">
7页</div>
<div class="gd-g-u pd-l-12 gd-u-7-24"></div>
</div>
</div>
<div id="wkad4" style="text-align:center;"></div>
</div>
</li><li>
<div class="item">
<div id="wk_sid" style="display:block;">
<p class="doc-title">
<b class="ic ic-doc"></b>
<a href="/view/3c4bb9c5b207e87101f69e3143323968011cf4bb.html?rec_flag=default" class="rec-items A-relate-doc logSend log-xsend " data-logsend="{&quot;send&quot;:[&quot;view&quot;,&quot;relateDoc&quot;,{&quot;from&quot;:&quot;related&quot;,&quot;right&quot;:&quot;docClick&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;listNo&quot;:&quot;5&quot;,&quot;ply&quot;:&quot;html&quot;,&quot;price&quot;:&quot;0&quot;}]}" price="0" data-index="7" data-source-id="3c4bb9c5b207e87101f69e3143323968011cf4bb" data-click-docid="3c4bb9c5b207e87101f69e3143323968011cf4bb" data-list-docids="8a9141ad4a35eefdc8d376eeaeaad1f346931198,961fdda786c24028915f804d2b160b4e777f8169,5a6f0accbf1e650e52ea551810a6f524ccbfcba8,ffba7dc2842458fb770bf78a6529647d272834aa,3c4bb9c5b207e87101f69e3143323968011cf4bb,ae723ba42bf90242a8956bec0975f46526d3a757,f56e535c82d049649b6648d7c1c708a1294a0a09,a71d3856a0c7aa00b52acfc789eb172ded6399ad,f75d48ba11661ed9ad51f01dc281e53a580251ae,77e372bb91c69ec3d5bbfd0a79563c1ec4dad74c" data-price-type="2" data-relate-doccomposition="0,10,0" data-mark-pay-doc="2" target="_blank" title="涉密计算机制度" data-score-mode="">
涉密计算机制度
</a>
</p>
<div class="gd-g tail-info">
<div class="gd-g-u gd-u-3-8 0">
<span title="1分，1人评">
<b class="ic ic-star-s-on"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b>
</span>
</div>
<div class="gd-g-u gd-u-1-4 pd-l-6">
14页</div>
<div class="gd-g-u pd-l-12 gd-u-7-24"></div>
</div>
</div>
<div id="wkad4" style="text-align:center;"></div>
</div>
<div class="item">
<div id="wk_sid" style="display:block;">
<p class="doc-title">
<b class="ic ic-doc"></b>
<a href="/view/ae723ba42bf90242a8956bec0975f46526d3a757.html?rec_flag=default" class="rec-items A-relate-doc logSend log-xsend " data-logsend="{&quot;send&quot;:[&quot;view&quot;,&quot;relateDoc&quot;,{&quot;from&quot;:&quot;related&quot;,&quot;right&quot;:&quot;docClick&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;listNo&quot;:&quot;6&quot;,&quot;ply&quot;:&quot;html&quot;,&quot;price&quot;:&quot;0&quot;}]}" price="0" data-index="8" data-source-id="ae723ba42bf90242a8956bec0975f46526d3a757" data-click-docid="ae723ba42bf90242a8956bec0975f46526d3a757" data-list-docids="8a9141ad4a35eefdc8d376eeaeaad1f346931198,961fdda786c24028915f804d2b160b4e777f8169,5a6f0accbf1e650e52ea551810a6f524ccbfcba8,ffba7dc2842458fb770bf78a6529647d272834aa,3c4bb9c5b207e87101f69e3143323968011cf4bb,ae723ba42bf90242a8956bec0975f46526d3a757,f56e535c82d049649b6648d7c1c708a1294a0a09,a71d3856a0c7aa00b52acfc789eb172ded6399ad,f75d48ba11661ed9ad51f01dc281e53a580251ae,77e372bb91c69ec3d5bbfd0a79563c1ec4dad74c" data-price-type="2" data-relate-doccomposition="0,10,0" data-mark-pay-doc="2" target="_blank" title="涉密和非涉密计算机保密管理制度流程" data-score-mode="">
涉密和非涉密计算机保密...
</a>
</p>
<div class="gd-g tail-info">
<div class="gd-g-u gd-u-3-8 0">
<span title="1分，1人评">
<b class="ic ic-star-s-on"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b>
</span>
</div>
<div class="gd-g-u gd-u-1-4 pd-l-6">
2页</div>
<div class="gd-g-u pd-l-12 gd-u-7-24"></div>
</div>
</div>
<div id="wkad4" style="text-align:center;"></div>
</div>
<div class="item">
<div id="wk_sid" style="display:block;">
<p class="doc-title">
<b class="ic ic-doc"></b>
<a href="/view/f56e535c82d049649b6648d7c1c708a1294a0a09.html?rec_flag=default" class="rec-items A-relate-doc logSend log-xsend " data-logsend="{&quot;send&quot;:[&quot;view&quot;,&quot;relateDoc&quot;,{&quot;from&quot;:&quot;related&quot;,&quot;right&quot;:&quot;docClick&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;listNo&quot;:&quot;7&quot;,&quot;ply&quot;:&quot;html&quot;,&quot;price&quot;:&quot;0&quot;}]}" price="0" data-index="9" data-source-id="f56e535c82d049649b6648d7c1c708a1294a0a09" data-click-docid="f56e535c82d049649b6648d7c1c708a1294a0a09" data-list-docids="8a9141ad4a35eefdc8d376eeaeaad1f346931198,961fdda786c24028915f804d2b160b4e777f8169,5a6f0accbf1e650e52ea551810a6f524ccbfcba8,ffba7dc2842458fb770bf78a6529647d272834aa,3c4bb9c5b207e87101f69e3143323968011cf4bb,ae723ba42bf90242a8956bec0975f46526d3a757,f56e535c82d049649b6648d7c1c708a1294a0a09,a71d3856a0c7aa00b52acfc789eb172ded6399ad,f75d48ba11661ed9ad51f01dc281e53a580251ae,77e372bb91c69ec3d5bbfd0a79563c1ec4dad74c" data-price-type="2" data-relate-doccomposition="0,10,0" data-mark-pay-doc="2" target="_blank" title="涉密计算机管理整套表格" data-score-mode="">
涉密计算机管理整套表格
</a>
</p>
<div class="gd-g tail-info">
<div class="gd-g-u gd-u-3-8 0">
<span title="1分，1人评">
<b class="ic ic-star-s-on"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b>
</span>
</div>
<div class="gd-g-u gd-u-1-4 pd-l-6">
42页</div>
<div class="gd-g-u pd-l-12 gd-u-7-24"></div>
</div>
</div>
<div id="wkad4" style="text-align:center;"></div>
</div>
<div class="item">
<div id="wk_sid" style="display:block;">
<p class="doc-title">
<b class="ic ic-pdf"></b>
<a href="/view/a71d3856a0c7aa00b52acfc789eb172ded6399ad.html?rec_flag=default" class="rec-items A-relate-doc logSend log-xsend " data-logsend="{&quot;send&quot;:[&quot;view&quot;,&quot;relateDoc&quot;,{&quot;from&quot;:&quot;related&quot;,&quot;right&quot;:&quot;docClick&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;listNo&quot;:&quot;8&quot;,&quot;ply&quot;:&quot;html&quot;,&quot;price&quot;:&quot;0&quot;}]}" price="0" data-index="10" data-source-id="a71d3856a0c7aa00b52acfc789eb172ded6399ad" data-click-docid="a71d3856a0c7aa00b52acfc789eb172ded6399ad" data-list-docids="8a9141ad4a35eefdc8d376eeaeaad1f346931198,961fdda786c24028915f804d2b160b4e777f8169,5a6f0accbf1e650e52ea551810a6f524ccbfcba8,ffba7dc2842458fb770bf78a6529647d272834aa,3c4bb9c5b207e87101f69e3143323968011cf4bb,ae723ba42bf90242a8956bec0975f46526d3a757,f56e535c82d049649b6648d7c1c708a1294a0a09,a71d3856a0c7aa00b52acfc789eb172ded6399ad,f75d48ba11661ed9ad51f01dc281e53a580251ae,77e372bb91c69ec3d5bbfd0a79563c1ec4dad74c" data-price-type="2" data-relate-doccomposition="0,10,0" data-mark-pay-doc="2" target="_blank" title="涉密计算机信息系统管理制度" data-score-mode="">
涉密计算机信息系统管理...
</a>
</p>
<div class="gd-g tail-info">
<div class="gd-g-u gd-u-3-8 0">
<span title="1分，1人评">
<b class="ic ic-star-s-on"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b>
</span>
</div>
<div class="gd-g-u gd-u-1-4 pd-l-6">
2页</div>
<div class="gd-g-u pd-l-12 gd-u-7-24"></div>
</div>
</div>
<div id="wkad4" style="text-align:center;"></div>
</div>
<div class="item">
<div id="wk_sid" style="display:block;">
<p class="doc-title">
<b class="ic ic-doc"></b>
<a href="/view/f75d48ba11661ed9ad51f01dc281e53a580251ae.html?rec_flag=default" class="rec-items A-relate-doc logSend log-xsend " data-logsend="{&quot;send&quot;:[&quot;view&quot;,&quot;relateDoc&quot;,{&quot;from&quot;:&quot;related&quot;,&quot;right&quot;:&quot;docClick&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;listNo&quot;:&quot;9&quot;,&quot;ply&quot;:&quot;html&quot;,&quot;price&quot;:&quot;0&quot;}]}" price="0" data-index="11" data-source-id="f75d48ba11661ed9ad51f01dc281e53a580251ae" data-click-docid="f75d48ba11661ed9ad51f01dc281e53a580251ae" data-list-docids="8a9141ad4a35eefdc8d376eeaeaad1f346931198,961fdda786c24028915f804d2b160b4e777f8169,5a6f0accbf1e650e52ea551810a6f524ccbfcba8,ffba7dc2842458fb770bf78a6529647d272834aa,3c4bb9c5b207e87101f69e3143323968011cf4bb,ae723ba42bf90242a8956bec0975f46526d3a757,f56e535c82d049649b6648d7c1c708a1294a0a09,a71d3856a0c7aa00b52acfc789eb172ded6399ad,f75d48ba11661ed9ad51f01dc281e53a580251ae,77e372bb91c69ec3d5bbfd0a79563c1ec4dad74c" data-price-type="2" data-relate-doccomposition="0,10,0" data-mark-pay-doc="2" target="_blank" title="涉密计算机管理规定" data-score-mode="">
涉密计算机管理规定
</a>
</p>
<div class="gd-g tail-info">
<div class="gd-g-u gd-u-3-8 0">
<span title="0.5分，1人评">
<b class="ic ic-star-s-half"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b><b class="ic ic-star-s-off"></b>
</span>
</div>
<div class="gd-g-u gd-u-1-4 pd-l-6">
2页</div>
<div class="gd-g-u pd-l-12 gd-u-7-24"></div>
</div>
</div>
<div id="wkad4" style="text-align:center;"></div>
</div>
</li><li>
<div class="item">
<div id="wk_sid" style="display:block;">
<p class="doc-title">
<b class="ic ic-pdf"></b>
<a href="/view/77e372bb91c69ec3d5bbfd0a79563c1ec4dad74c.html?rec_flag=default" class="rec-items A-relate-doc logSend log-xsend " data-logsend="{&quot;send&quot;:[&quot;view&quot;,&quot;relateDoc&quot;,{&quot;from&quot;:&quot;related&quot;,&quot;right&quot;:&quot;docClick&quot;,&quot;copyright&quot;:&quot;&quot;,&quot;listNo&quot;:&quot;10&quot;,&quot;ply&quot;:&quot;html&quot;,&quot;price&quot;:&quot;0&quot;}]}" price="0" data-index="12" data-source-id="77e372bb91c69ec3d5bbfd0a79563c1ec4dad74c" data-click-docid="77e372bb91c69ec3d5bbfd0a79563c1ec4dad74c" data-list-docids="8a9141ad4a35eefdc8d376eeaeaad1f346931198,961fdda786c24028915f804d2b160b4e777f8169,5a6f0accbf1e650e52ea551810a6f524ccbfcba8,ffba7dc2842458fb770bf78a6529647d272834aa,3c4bb9c5b207e87101f69e3143323968011cf4bb,ae723ba42bf90242a8956bec0975f46526d3a757,f56e535c82d049649b6648d7c1c708a1294a0a09,a71d3856a0c7aa00b52acfc789eb172ded6399ad,f75d48ba11661ed9ad51f01dc281e53a580251ae,77e372bb91c69ec3d5bbfd0a79563c1ec4dad74c" data-price-type="2" data-relate-doccomposition="0,10,0" data-mark-pay-doc="2" target="_blank" title="涉密电脑管理制度涉密和非涉密计算机保密管理制度" data-score-mode="">
涉密电脑管理制度涉密和...
</a>
</p>
<div class="gd-g tail-info">
<div class="gd-g-u gd-u-3-8 0">
<span title="4分，1人评">
<b class="ic ic-star-s-on"></b><b class="ic ic-star-s-on"></b><b class="ic ic-star-s-on"></b><b class="ic ic-star-s-on"></b><b class="ic ic-star-s-off"></b>
</span>
</div>
<div class="gd-g-u gd-u-1-4 pd-l-6">
4页</div>
<div class="gd-g-u pd-l-12 gd-u-7-24"></div>
</div>
</div>
<div id="wkad4" style="text-align:center;"></div>
</div>
</li>
</ul>
</div>
</div>
<b class="bottom"><b class="bl"></b><b class="br"></b></b>
</div>

</div><div id="__elm_view-like-recom__qk_2"></div></div>
<div id="guess-like-doc"></div>
<div class="zhixin-right"></div>
<div class="fengchao-right" style="display: block;"><iframe src="https://entry.baidu.com/rp/home?psid=u2744350&amp;pswidth=200&amp;psheight=166&amp;ifr=infr%3A1_cross%3A0_drs%3A4_pcs%3A1278x969_pss%3A1268x5335_cfv%3A0_cpl%3A3_chi%3A1_cce%3A1_cec%3AGBK_tlm%3A1571283661_ecd%3A1_adw%3Aundefinedxundefined&amp;di=u2744350&amp;rsi0=200&amp;rsi1=166&amp;title=%E6%B6%89%E5%AF%86%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%AE%A1%E7%90%86%E5%88%B6%E5%BA%A6%C2%A0-%20%E7%99%BE%E5%BA%A6%E6%96%87%E5%BA%93&amp;ref=&amp;ltu=https%3A%2F%2Fwenku.baidu.com%2Fview%2Fe167fbacae45b307e87101f69e3143323968f5cc.html%3Frec_flag%3Ddefault%26sxts%3D1571282613997&amp;t=1571283661990" width="200" height="166" scrolling="no" frameborder="0" style="width: 200px; height: 166px; background-color: transparent;"></iframe><script type="text/javascript" id="BDEMBED_PSIDu2744350">var cpro_psid = "u2744350";var cpro_pswidth = "200";var cpro_psheight = "166";</script></div>
</div>
<div id="viewSideDown" class="viewSideDown" style="display: none">
<div class="viewSideDown-layout">
<a class="btn-viewSideDown-close" href="javascript:;"></a>
<a href="http://wenku.baidu.com/miti" class="log-xsend" data-logxsend="[1, 100447]" target="_blank">
<img src="">
</a>
</div>
</div>
</div>
</div>
</div>


</div>
</div>
</div>
<div id="ft">

<div class="footer">
<p>
<span class="cr">©2019&nbsp;Baidu</span>&nbsp;<span>|&nbsp;由&nbsp;百度云&nbsp;提供计算服务</span>&nbsp;|&nbsp;<a href="http://www.baidu.com/duty/" class="Bidu" target="_blank">使用百度前必读</a>&nbsp;|&nbsp;<a href="https://wenku.baidu.com/portal/browse/help#help/24" class="Xieyi" target="_blank">文库协议</a>&nbsp;|&nbsp;<a href="https://jiaoyu.baidu.com/topic/bsplatform/brand_promotion" class="Xieyi" target="_blank">广告服务</a>&nbsp;|&nbsp;<a href="https://jiaoyu.baidu.com/topic/bsplatform/institutional_database" class="Xieyi" target="_blank">企业文库</a>&nbsp;|&nbsp;<a href="/portal/browse/websitemap" class="Xieyi" target="_blank">网站地图</a>
</p>
</div>

</div>
</div>

<script type="text/javascript">
		var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
		document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3Fd8bfb560f8d03bbefc9bdecafc4a4bf6' type='text/javascript'%3E%3C/script%3E"));
	</script><script src=" https://hm.baidu.com/h.js?d8bfb560f8d03bbefc9bdecafc4a4bf6" type="text/javascript"></script>
<script type="text/javascript" id="bdshare_js" data="type=tools&amp;uid=39124"></script>
<script type="text/javascript" id="bdshell_js" src="//edu-wenku.bdimg.com/v1/pc/bdshare/static/api/js/share.js?cdnversion=11"></script>
<div class="ad-taishan-bar">
<a href="###" target="_blank" class="log-xsend" data-logxsend="[1, 100968, {index: 1}]"></a>
<div class="ad-bar-close"></div>
</div>
<div class="ad-taishan">
<a href="###" target="_blank" class="log-xsend" data-logxsend="[1, 100968, {index: 2}]"></a>
</div>


<script type="text/javascript" src="//passport.baidu.com/passApi/js/uni_armorwidget_wrapper.js"></script>
<script type="text/javascript" src="//passport.baidu.com/passApi/js/uni_login_wrapper.js"></script>
<script type="text/javascript">var pageId='wenku-view';</script>






<script>alog && alog('speed.set', 'drt', +new Date);</script>

<script>
    if (window.viewTime && window.viewTime.t) {
        // body 渲染完成时间
        window.viewTime.bt = new Date().getTime();
    }
    void function(a,b,c,d,e,f){function g(b){a.attachEvent?a.attachEvent("onload",b,!1):a.addEventListener&&a.addEventListener("load",b)}function h(a,c,d){d=d||15;var e=new Date;e.setTime((new Date).getTime()+1e3*d),b.cookie=a+"="+escape(c)+";path=/;expires="+e.toGMTString()}function i(a){var c=b.cookie.match(new RegExp("(^| )"+a+"=([^;]*)(;|$)"));return null!=c?unescape(c[2]):null}function j(){var a=i("PMS_JT");if(a){h("PMS_JT","",-1);try{a=a.match(/{["']s["']:(\d+),["']r["']:["']([\s\S]+)["']}/),a=a&&a[1]&&a[2]?{s:parseInt(a[1]),r:a[2]}:{}}catch(c){a={}}a.r&&b.referrer.replace(/#.*/,"")!=a.r||alog("speed.set","wt",a.s)}}if(a.alogObjectConfig){var k=a.alogObjectConfig.sample,l=a.alogObjectConfig.rand;d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d,k&&l&&l>k||(g(function(){alog("speed.set","lt",+new Date),e=b.createElement(c),e.async=!0,e.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),f=b.getElementsByTagName(c)[0],f.parentNode.insertBefore(e,f)}),j())}}(window,document,"script","/hunter/alog/dp.min.js");
</script>
<script type="text/javascript" src="//wkstatic.bdimg.com/static/wkcommon/modjs/mod_2cc47b9.js"></script><script type="text/javascript">require.resourceMap({"res":{"wkcommon:widget\/dp_performance\/dp_First\/dp_First.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/ui\/js_core\/log\/log.js"]},"wkcommon:widget\/ui\/reader\/config\/config.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/lib\/fis\/data\/data.js","wkcommon:widget\/ui\/js_core\/mvp\/template\/template.js"]},"wkcommon:widget\/ui\/reader\/model\/doc\/model.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/util\/util.js","wkcommon:widget\/ui\/js_core\/mvp\/model\/model.js","wkcommon:widget\/ui\/js_core\/mvp\/template\/template.js","wkcommon:widget\/ui\/js_core\/log\/log.js","wkcommon:widget\/lib\/fis\/data\/data.js","wkcommon:widget\/ui\/lib\/jquery\/jquery.js"]},"wkcommon:widget\/ui\/reader\/model\/model.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/ui\/reader\/model\/doc\/model.js"]},"wkcommon:widget\/ui\/reader\/view\/doc\/util.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/lib\/fis\/data\/data.js"]},"wkcommon:widget\/ui\/reader\/view\/doc\/render.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/util\/util.js","wkcommon:widget\/ui\/reader\/view\/doc\/util.js"]},"wkcommon:widget\/ui\/reader\/view\/doc\/view.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/util\/util.js","wkcommon:widget\/ui\/js_core\/mvp\/view\/view.js","wkcommon:widget\/ui\/reader\/view\/doc\/render.js"]},"wkcommon:widget\/ui\/reader\/view\/view.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/ui\/reader\/view\/doc\/view.js","wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/util\/util.js"]},"wkcommon:widget\/ui\/reader\/strategy\/doc\/util.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js"]},"wkcommon:widget\/ui\/reader\/strategy\/doc\/strategy.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/util\/util.js","wkcommon:widget\/ui\/js_core\/preload\/preload.js","wkcommon:widget\/ui\/reader\/strategy\/doc\/util.js","wkcommon:widget\/ui\/js_core\/log\/log.js","wkcommon:widget\/lib\/fis\/data\/data.js","wkcommon:widget\/dp_performance\/dp_First\/dp_First.js"]},"wkcommon:widget\/ui\/reader\/strategy\/strategy.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/ui\/reader\/strategy\/doc\/strategy.js","wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/util\/util.js"]},"wkcommon:widget\/ui\/reader\/presenter\/presenter.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/mvp\/presenter\/presenter.js","wkcommon:widget\/ui\/js_core\/mvp\/event\/event.js","wkcommon:widget\/ui\/reader\/config\/config.js","wkcommon:widget\/ui\/reader\/model\/model.js","wkcommon:widget\/ui\/reader\/view\/view.js","wkcommon:widget\/ui\/reader\/strategy\/strategy.js","wkcommon:widget\/ui\/reader_plugin\/reader_plugin.js"]},"wkcommon:widget\/ui\/reader\/reader.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/ui\/reader\/presenter\/presenter.js"]},"wkcommon:widget\/ui\/reader_plugin\/ZeroClipboard\/ZeroClipboard.js":{"pkg":"wkcommon:p12"},"wkcommon:widget\/ui\/reader_plugin\/qrcode\/qrcode.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/ui\/js_core\/qrcode\/qrcode.js","wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/util\/util.js","wkcommon:widget\/lib\/fis\/data\/data.js","wkcommon:widget\/ui\/js_core\/log\/log.js"]},"wkcommon:widget\/ui\/reader_plugin\/translate.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/util\/util.js"]},"wkcommon:widget\/ui\/reader_plugin\/baike.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/mvp\/template\/template.js","wkcommon:widget\/ui\/js_core\/util\/util.js"]},"wkcommon:widget\/ui\/reader_plugin\/copylimit\/copylimit.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/_dialog\/_dialog.js","wkcommon:widget\/lib\/fis\/data\/data.js","wkcommon:widget\/ui\/js_core\/log\/log.js","wkcommon:widget\/lib\/doT\/doT.min.js"]},"wkcommon:widget\/ui\/reader_plugin\/copy.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/util\/util.js","wkcommon:widget\/ui\/reader_plugin\/ZeroClipboard\/ZeroClipboard.js","wkcommon:widget\/lib\/fis\/data\/data.js","wkcommon:widget\/ui\/reader_plugin\/qrcode\/qrcode.js","wkcommon:widget\/ui\/reader_plugin\/translate.js","wkcommon:widget\/ui\/reader_plugin\/baike.js","wkcommon:widget\/sendToPhoneDialog\/sendToPhoneDialog.js","wkcommon:widget\/ui\/reader_plugin\/copylimit\/copylimit.js","wkcommon:widget\/ui\/js_core\/log\/log.js"]},"wkcommon:widget\/ui\/reader_plugin\/log.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/lib\/fis\/data\/data.js"]},"wkcommon:widget\/ui\/reader_plugin\/keyword\/match_card\/match_card.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/ui\/lib\/browser\/browser.js"]},"wkcommon:widget\/ui\/reader_plugin\/keyword\/search.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/ui\/lib\/jquery\/jquery.js","wkcommon:widget\/ui\/lib\/array\/array.js","wkcommon:widget\/ui\/js_core\/util\/util.js","wkcommon:widget\/ui\/lib\/browser\/browser.js","wkcommon:widget\/ui\/reader_plugin\/keyword\/match_card\/match_card.js"]},"wkcommon:widget\/ui\/reader_plugin\/keyword\/match_card\/getKeycard.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/ui\/reader_plugin\/keyword\/search.js","wkcommon:widget\/ui\/js_core\/util\/util.js","wkcommon:widget\/ui\/lib\/sio\/sio.js","wkcommon:widget\/ui\/lib\/object\/object.js","wkcommon:widget\/ui\/js_core\/log\/log.js","wkcommon:widget\/ui\/lib\/jquery\/jquery.js","wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/lib\/fis\/data\/data.js","wkcommon:widget\/ui\/lib\/inCharset\/inCharset.js","wkcommon:widget\/ui\/lib\/browser\/browser.js","wkcommon:widget\/ui\/js_core\/toolkit\/toolkit.js","wkcommon:widget\/lib\/doT\/doT.min.js"]},"wkcommon:widget\/ui\/reader_plugin\/keyword\/main.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/ui\/reader_plugin\/keyword\/search.js","wkcommon:widget\/ui\/js_core\/util\/util.js","wkcommon:widget\/ui\/lib\/sio\/sio.js","wkcommon:widget\/ui\/lib\/object\/object.js","wkcommon:widget\/ui\/js_core\/log\/log.js","wkcommon:widget\/ui\/lib\/jquery\/jquery.js","wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/lib\/fis\/data\/data.js","wkcommon:widget\/ui\/lib\/inCharset\/inCharset.js","wkcommon:widget\/ui\/lib\/browser\/browser.js","wkcommon:widget\/ui\/reader_plugin\/keyword\/match_card\/getKeycard.js"]},"wkcommon:widget\/ui\/reader_plugin\/videokeyword\/search.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/ui\/lib\/jquery\/jquery.js","wkcommon:widget\/ui\/lib\/array\/array.js","wkcommon:widget\/ui\/js_core\/util\/util.js","wkcommon:widget\/ui\/lib\/browser\/browser.js"]},"wkcommon:widget\/ui\/reader_plugin\/videokeyword\/video_card\/videocard.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/ui\/js_core\/util\/util.js","wkcommon:widget\/ui\/js_core\/log\/log.js","wkcommon:widget\/ui\/lib\/jquery\/jquery.js","wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/lib\/fis\/data\/data.js","wkcommon:widget\/ui\/lib\/inCharset\/inCharset.js","wkcommon:widget\/ui\/lib\/browser\/browser.js","wkcommon:widget\/ui\/js_core\/toolkit\/toolkit.js","wkcommon:widget\/lib\/doT\/doT.min.js"]},"wkcommon:widget\/ui\/reader_plugin\/videokeyword\/main.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/ui\/reader_plugin\/videokeyword\/search.js","wkcommon:widget\/ui\/js_core\/util\/util.js","wkcommon:widget\/ui\/lib\/sio\/sio.js","wkcommon:widget\/ui\/lib\/object\/object.js","wkcommon:widget\/ui\/js_core\/log\/log.js","wkcommon:widget\/ui\/lib\/jquery\/jquery.js","wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/lib\/fis\/data\/data.js","wkcommon:widget\/ui\/lib\/inCharset\/inCharset.js","wkcommon:widget\/ui\/lib\/browser\/browser.js","wkcommon:widget\/ui\/reader_plugin\/videokeyword\/video_card\/videocard.js"]},"wkcommon:widget\/ui\/reader_plugin\/reader_plugin.js":{"pkg":"wkcommon:p12","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/reader_plugin\/copy.js","wkcommon:widget\/ui\/reader_plugin\/log.js","wkcommon:widget\/ui\/reader_plugin\/keyword\/main.js","wkcommon:widget\/ui\/reader_plugin\/videokeyword\/main.js"]},"wkcommon:widget\/ui\/reader_plugin\/keyword\/idList.js":{"pkg":"wkcommon:p12"},"wkcommon:widget\/ui\/reader_plugin\/keyword\/wordList.js":{"pkg":"wkcommon:p12"},"wkcommon:widget\/ui\/reader_plugin\/search.js":{"pkg":"wkcommon:p12"},"wkcommon:widget\/ui\/pay\/cart\/cart.js":{"pkg":"wkcommon:p14","deps":["wkcommon:widget\/ui\/lib\/jquery\/jquery.js","wkcommon:widget\/ui\/js_core\/mvp\/event\/event.js","wkcommon:widget\/lib\/fis\/data\/data.js"]},"wkcommon:widget\/ui\/pay\/flow.js":{"pkg":"wkcommon:p14","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js"]},"wkcommon:widget\/ui\/pay\/mediator.js":{"pkg":"wkcommon:p14","deps":["wkcommon:widget\/ui\/js_core\/mvp\/event\/event.js"]},"wkcommon:widget\/ui\/pay\/util.js":{"pkg":"wkcommon:p14","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/_dialog\/_dialog.js"]},"wkcommon:widget\/ui\/pay\/presenter.js":{"pkg":"wkcommon:p14","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/pay\/flow.js","wkcommon:widget\/ui\/js_core\/mvp\/presenter\/presenter.js","wkcommon:widget\/ui\/pay\/util.js"]},"wkcommon:widget\/ui\/pay\/view\/setting.js":{"pkg":"wkcommon:p14"},"wkcommon:widget\/ui\/pay\/view\/confirmBuy.js":{"pkg":"wkcommon:p14","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/mvp\/view\/view.js","wkcommon:widget\/ui\/js_core\/mvp\/template\/template.js","wkcommon:widget\/ui\/js_core\/_dialog\/_dialog.js","wkcommon:widget\/ui\/js_core\/util\/util.js","wkcommon:widget\/ui\/pay\/view\/setting.js","wkcommon:widget\/ui\/pay\/util.js"]},"wkcommon:widget\/ui\/pay\/view\/payDialog.js":{"pkg":"wkcommon:p14","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/util\/util.js","wkcommon:widget\/ui\/js_core\/_dialog\/_dialog.js","wkcommon:widget\/ui\/pay\/mediator.js"]},"wkcommon:widget\/ui\/pay\/view\/waitBuy.js":{"pkg":"wkcommon:p14","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/mvp\/view\/view.js","wkcommon:widget\/ui\/js_core\/mvp\/template\/template.js","wkcommon:widget\/ui\/pay\/view\/payDialog.js","wkcommon:widget\/ui\/js_core\/util\/util.js","wkcommon:widget\/ui\/pay\/util.js"]},"wkcommon:widget\/ui\/pay\/view\/buySuccess.js":{"pkg":"wkcommon:p14","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/mvp\/view\/view.js","wkcommon:widget\/ui\/js_core\/mvp\/template\/template.js","wkcommon:widget\/ui\/pay\/view\/payDialog.js","wkcommon:widget\/ui\/js_core\/util\/util.js"]},"wkcommon:widget\/ui\/pay\/view\/buyFail.js":{"pkg":"wkcommon:p14","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/js_core\/mvp\/view\/view.js","wkcommon:widget\/ui\/js_core\/mvp\/template\/template.js","wkcommon:widget\/ui\/pay\/view\/payDialog.js","wkcommon:widget\/ui\/pay\/view\/setting.js","wkcommon:widget\/ui\/js_core\/util\/util.js"]},"wkcommon:widget\/ui\/pay\/viewList.js":{"pkg":"wkcommon:p14","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/pay\/view\/confirmBuy.js","wkcommon:widget\/ui\/pay\/view\/waitBuy.js","wkcommon:widget\/ui\/pay\/view\/buySuccess.js","wkcommon:widget\/ui\/pay\/view\/buyFail.js","wkcommon:widget\/ui\/js_core\/util\/util.js","wkcommon:widget\/ui\/lib\/jquery\/jquery.js"]},"wkcommon:widget\/ui\/pay\/pay.js":{"pkg":"wkcommon:p14","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/pay\/presenter.js","wkcommon:widget\/ui\/js_core\/mvp\/event\/event.js","wkcommon:widget\/ui\/pay\/viewList.js"]},"wkcommon:widget\/ui\/payCheck\/payCheck.js":{"pkg":"wkcommon:p14","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/lib\/jquery\/jquery.js","wkcommon:widget\/ui\/js_core\/_dialog\/_dialog.js","wkcommon:widget\/ui\/js_core\/login\/login.js"]},"wkcommon:widget\/ui\/lib\/async_widget\/async_widget.js":{"url":"\/\/wkstatic.bdimg.com\/static\/wkcommon\/widget\/ui\/lib\/async_widget\/async_widget_e8d6637.js","deps":["wkcommon:widget\/ui\/lib\/jquery\/jquery.js"]},"wkview:widget\/common_toc\/reader_html\/page_body\/main.js":{"url":"\/\/wkstatic.bdimg.com\/static\/wkview\/widget\/common_toc\/reader_html\/page_body\/main_ca25087.js","deps":["wkcommon:widget\/ui\/lib\/async_widget\/async_widget.js","wkcommon:widget\/ui\/lib\/browser\/browser.js","wkview:widget\/crmAd\/crmAd2.js","wkview:widget\/crm_multi\/crm_multi.js","wkview:widget\/crmAd\/zyAd.js","wkview:widget\/commerce\/fengchao\/modelAnimation.js","wkview:widget\/ui\/detectImgBlock\/detectImgBlock.js","wkview:widget\/ui\/detectImgBlock\/hijack.js","wkcommon:widget\/ui\/lib\/BigPipe\/BigPipe.js","wkview:widget\/crmAd\/crmAd3.js","wkview:widget\/fengchao_right\/fengchao_right.js","wkcommon:widget\/vipNoAdDialog\/vipNoAdDialog.js","wkview:widget\/commerce\/fengchao\/left.js","wkcommon:widget\/lib\/tangram\/base\/base.js","wkcommon:widget\/ui\/lib\/jquery\/jquery.js","wkview:widget\/ad_xpageForm\/xpageForm.js","wkview:widget\/node_modules\/@baidu\/wenku-model-user\/index.js","wkcommon:widget\/ui\/js_core\/log\/log.js","wkcommon:widget\/lib\/fis\/data\/data.js"]},"wkview:widget\/common_toc\/common\/main.js":{"url":"\/\/wkstatic.bdimg.com\/static\/wkview\/widget\/common_toc\/common\/main_3e09e8a.js","deps":["wkcommon:widget\/lib\/tangram\/base\/base.js","wkview:widget\/common_item\/cloudSync\/cloudSync.js","wkview:widget\/common_item\/todoAction\/todoAction.js","wkview:widget\/common_item\/someLog\/someLog.js"]}},"pkg":{"wkcommon:p12":{"url":"\/\/wkstatic.bdimg.com\/static\/wkcommon\/pkg\/pkg_wkcommon_htmlReader_5998cf0.js","has":["wkcommon:widget\/dp_performance\/dp_First\/dp_First.js","wkcommon:widget\/ui\/reader\/config\/config.js","wkcommon:widget\/ui\/reader\/model\/doc\/model.js","wkcommon:widget\/ui\/reader\/model\/model.js","wkcommon:widget\/ui\/reader\/view\/doc\/util.js","wkcommon:widget\/ui\/reader\/view\/doc\/render.js","wkcommon:widget\/ui\/reader\/view\/doc\/view.js","wkcommon:widget\/ui\/reader\/view\/view.js","wkcommon:widget\/ui\/reader\/strategy\/doc\/util.js","wkcommon:widget\/ui\/reader\/strategy\/doc\/strategy.js","wkcommon:widget\/ui\/reader\/strategy\/strategy.js","wkcommon:widget\/ui\/reader\/presenter\/presenter.js","wkcommon:widget\/ui\/reader\/reader.js","wkcommon:widget\/ui\/reader_plugin\/ZeroClipboard\/ZeroClipboard.js","wkcommon:widget\/ui\/reader_plugin\/qrcode\/qrcode.js","wkcommon:widget\/ui\/reader_plugin\/translate.js","wkcommon:widget\/ui\/reader_plugin\/baike.js","wkcommon:widget\/ui\/reader_plugin\/copylimit\/copylimit.js","wkcommon:widget\/ui\/reader_plugin\/copy.js","wkcommon:widget\/ui\/reader_plugin\/log.js","wkcommon:widget\/ui\/reader_plugin\/keyword\/match_card\/match_card.js","wkcommon:widget\/ui\/reader_plugin\/keyword\/search.js","wkcommon:widget\/ui\/reader_plugin\/keyword\/match_card\/getKeycard.js","wkcommon:widget\/ui\/reader_plugin\/keyword\/main.js","wkcommon:widget\/ui\/reader_plugin\/videokeyword\/search.js","wkcommon:widget\/ui\/reader_plugin\/videokeyword\/video_card\/videocard.js","wkcommon:widget\/ui\/reader_plugin\/videokeyword\/main.js","wkcommon:widget\/ui\/reader_plugin\/reader_plugin.js","wkcommon:widget\/ui\/reader_plugin\/keyword\/idList.js","wkcommon:widget\/ui\/reader_plugin\/keyword\/wordList.js","wkcommon:widget\/ui\/reader_plugin\/search.js"]},"wkcommon:p14":{"url":"\/\/wkstatic.bdimg.com\/static\/wkcommon\/pkg\/pkg_wkcommon_pay_90be412.js","has":["wkcommon:widget\/ui\/pay\/cart\/cart.js","wkcommon:widget\/ui\/pay\/flow.js","wkcommon:widget\/ui\/pay\/mediator.js","wkcommon:widget\/ui\/pay\/util.js","wkcommon:widget\/ui\/pay\/presenter.js","wkcommon:widget\/ui\/pay\/view\/setting.js","wkcommon:widget\/ui\/pay\/view\/confirmBuy.js","wkcommon:widget\/ui\/pay\/view\/payDialog.js","wkcommon:widget\/ui\/pay\/view\/waitBuy.js","wkcommon:widget\/ui\/pay\/view\/buySuccess.js","wkcommon:widget\/ui\/pay\/view\/buyFail.js","wkcommon:widget\/ui\/pay\/viewList.js","wkcommon:widget\/ui\/pay\/pay.js","wkcommon:widget\/ui\/payCheck\/payCheck.js"]}}});</script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkcommon/pkg/pkg_wkcommon_npm_9cc6154.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkcommon/pkg/pkg_first_paint_1938465.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkcommon/pkg/pkg_wkcommon_index_03eee7c.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkcommon/pkg/pkg_wkcommon_base_15e4ca2.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkcommon/pkg/pkg_wkcommon_lib_24de2d8.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkview/widget/node_modules/davidshimjs-qrcodejs/qrcode_6606823.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkview/widget/node_modules/dot/examples/express/lib/app_1c701f8.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkview/widget/node_modules/dot/doT_46d84c3.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkview/pkg/pkg_wkview_npm_6e2a6f9.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkcommon/widget/node_modules/vue/dist/vue_9f2cc6e.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkview/pkg/toctoolbar_fb86dc5.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkview/pkg/viewcommon_0633496.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkview/widget/ui/html_view/widget_d6e8ec2.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkview/widget/ad_smallflow/ad_smallflow_5fa29c1.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkcommon/widget/ess/getEssQuery_23822b2.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkview/pkg/viewcommon2_37cc9fc.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkview/pkg/xreaderview_a6c1cfc.js"></script><script type="text/javascript" src="//wkstatic.bdimg.com/static/wkview/third_party/fengchao_plugin/parallax-scrolling-webku.min-0_0754c4e.js"></script><script type="text/javascript">
!function(){            //service worker相关统计
            require.async(['wkcommon:widget/ui/js_core/log/log.js'],function(Log){
                try {
                    function testMime (key, value) {
                        var mimeTypes = navigator.mimeTypes;
                        for (var i in mimeTypes) {
                        if (mimeTypes[i][key] === value) {
                            return true;
                        }
                        }
                        return false;
                    }
                    if (navigator.userAgent.indexOf('Chrome') !== -1) {
                        Log.xsend(1, 101033);
                        if (navigator.mimeTypes) {
                            if (testMime('type', 'application/vnd.chromium.remoting-viewer')) {
                                Log.xsend(1, 101032);
                            }
                        }
                    }
                    if ('serviceWorker' in navigator && 'PushManager' in window) {
                        Log.xsend(1, 101034);
                    }
                } catch (e) {

                }
            });
        }();
!function(){        require.async('wkview:widget/ui/nsTypeMap/nsTypeMap.js');
    }();
!function(){    var $ = require('wkcommon:widget/ui/lib/jquery/jquery.js');
    var sessionX = require('wkcommon:widget/sessionX/sessionX.js');
    var sessionXMgr = sessionX.sessionXMgr;
    var urlParam = sessionXMgr.getUrlParam();
    window.wkCommonLogParam = typeof window.wkCommonLogParam === 'object'
        ? window.wkCommonLogParam : {};
    $.extend(true, window.wkCommonLogParam, {
        '_sessionx_url_param': JSON.stringify(urlParam)
    });
}();
!function(){    require.async(['wkcommon:widget/lib/fis/data/data.js', 'wkcommon:widget/ui/lib/jquery/jquery.js', 'wkcommon:widget/user_bar/user_bar.js'], function (Data, $) {
        Data.set('isPgcPop', '0');
        Data.set('smallFlow',true);
        $( '#reg' ).attr( 'href', 'https://passport.baidu.com/v2/?reg&tpl=do&u=' + encodeURIComponent( location.href ) );
    });
}();
!function(){    window.escapeSymbol=function(e){return String(e).replace(/[#%&+=\/\\\ \u3000\f\r\n\t]/g,function(e){return"%"+(256+e.charCodeAt()).toString(16).substring(1).toUpperCase()})},window.setHeadUrl=function(e){if(document.getElementById("kw").value){var t=new RegExp("[?]");if(!t.test(e.href)){var r=e.href;e.href=e.getAttribute("data-href"),e.setAttribute("data-href",r)}e.href=e.href.replace("?newmap=1&ie=utf-8&s=s%26wd%3D","?newmap=1&ie=utf-8&s=s&wd="),e.href=e.href.replace(new RegExp("("+e.getAttribute("wdfield")+"=)[^&]*"),"$1"+encodeURIComponent(document.getElementById("kw").value)).replace("?newmap=1&ie=utf-8&s=s&wd=","?newmap=1&ie=utf-8&s=s%26wd%3D"),e.href=e.href.replace(new RegExp("("+e.getAttribute("wdfield")+"=)[^&]*"),"$1"+window.escapeSymbol(document.getElementById("kw").value))
}else{var t=new RegExp("[?]");if(t.test(e.href)){var r=e.href;e.href=e.getAttribute("data-href"),e.setAttribute("data-href",r)}}};;
    }();
!function(){    require.async(['wkcommon:widget/lib/tangram/base/base.js', 'wkcommon:widget/lib/fis/data/data.js', 'wkcommon:widget/header/search_box/search_box.js'], function(T, Data){

    var hotword = T.json.parse('[{\x22content\x22:\x22ppt\\u6a21\\u7248\x22,\x22isnew\x22:\x221\x22},{\x22content\x22:\x22\\u5c0f\\u5b66\\u4f5c\\u6587\x22,\x22isnew\x22:\x221\x22},{\x22content\x22:\x22\\u5c0f\\u5b66\\u6570\\u5b66\\u516c\\u5f0f\x22,\x22isnew\x22:\x220\x22}]');

    Data.set('hotword', hotword);
    });
}();
!function(){    require.async(['wkcommon:widget/header/category/category.js'], function (Category) {
        new Category();
    });
}();
!function(){    require.async(["wkcommon:widget/lib/tangram/base/base.js", "wkcommon:widget/ui/js_core/login/login.js", "wkcommon:widget/ui/lib/jquery/jquery.js", "wkcommon:widget/ui/js_core/log/log.js"],function(e,n,i,o){e.dom.ready(function(){var t=(e.event,e.g);o.xsend(1,100753);var a=document.location.pathname,r={"nav-index":/^\/$/i,"nav-edu":/^\/edu/i,"nav-org":/^\/org\/index/i},u=(n.login,100);for(var c in r)if(r.hasOwnProperty(c)){var s=r[c];if(s.test&&s.test(a)){var d=t(c);d&&e.addClass(d,"current")}}!function(){var n=document.location.pathname,i=(e.dom.g("zone-menu"),e.dom.q("ui-sub-nav","hd","div")[0]),o=[/^\/edu\/index$/i,/^\/ppt\/index$/i,/^\/life\/index$/i,/^\/pro\/index$/i,/^\/form\/index$/i,/^\/topic$/i],t=function(){for(var e={isZonePage:!1,zoneType:""},i=0,t=o.length;t>i;i++){var a=o[i];
a.test(n)&&(e.isZonePage=!0,e.zoneType=n)}return e}();if(t.isZonePage&&i)for(var a=i.getElementsByTagName("a"),r=0,u=a.length;u>r;r++){var c=a[r],s=c.getAttribute("href");(t.zoneType===s||document.location.href===s)&&e.dom.addClass(c.parentNode,"current")}}(),function(){function e(){a.hide(),t.removeClass("current")}function n(){a.show(),t.addClass("current")}var o="";if(!o){var t=i("#zone-menu"),a=i("#wk-all-cate"),r=null;t.mouseenter(function(){r&&clearTimeout(r),r=setTimeout(function(){n()
},u)}).mouseleave(function(n){r&&clearTimeout(r),n.relatedTarget!=a[0]&&e()}),a.mouseenter(function(){n()}).mouseleave(function(){e()})}}(),function(n){var i=null;n("ul.main-nav li").on("mouseenter",function(){var e=n(this),o=e.find(".drop-sub-nav");o.length&&o.find(">a").length&&(i=setTimeout(function(){o.show(),e.addClass("current")},u))}),e.cookie.get("__join_jiaoyu_vip")?n(".havenew-ic").hide():(n(".havenew-ic").show(),n(".jiaoyu-vip").on("click",function(){n(".havenew-ic").hide(),e.cookie.set("__join_jiaoyu_vip",1,{path:"/"})
})),n("ul.main-nav li").on("mouseleave",function(){i&&clearTimeout(i),n(this).find(".drop-sub-nav").hide(),n(this).removeClass("current")})}(i)})});;
}();
!function(){    require.async('wkview:widget/ui/nsTypeMap/nsTypeMap.js');
}();
!function(){    require.async(['wkview:widget/top_ads_banner/top_ads_banner.js', 'wkcommon:widget/ui/js_core/log/log.js'], function (topAdsBanner, Log) {
        new topAdsBanner({
            crumbs: '专业资料,IT\/计算机,计算机硬件及网络'
        });
         Log.xsend(1, 102184, {
            index: 'show',
            item: +'1',
            hasAnyTagShowedInView: +'0'
        });
    });
}();
!function(){			var tagArr = [];
		require.async(['wkview:widget/doc_header_new/index.js'], function (Index) {
		this.index = new Index({
			id: '0',
			veritype: '',
			oid: '',
			hasTag: !!'',
			tagArr: tagArr
		});
	});
}();
!function(){    require.async(['wkview:widget/common_toc/common/doc_tag/index.js'], function (DocTag) {
        this.docTag = new DocTag();
    });
}();
!function(){    require.async(['wkcommon:widget/ui/lib/jquery/jquery.js', 'wkcommon:widget/vipNoAdDialog/vipNoAdDialog.js'], function($, NoAdDialog) {
        if ($('.ad-logo').length > 0) {
            $('.ad-logo').each(function () {
                $(this).click(function () {
                    new NoAdDialog();
                });
            });
        }
    })
}();
!function(){        require.async(['wkview:widget/common_toc_reader/common/doc_banner/compAsync/index.js'], function (CompAsync) {
            new CompAsync();
        });

    }();
!function(){    require.async(['wkcommon:widget/ui/lib/jquery/jquery.js', 'wkcommon:widget/vipNoAdDialog/vipNoAdDialog.js'], function($, NoAdDialog) {
        if ($('#html-reader-AD-3t4').length > 0) {
            $('#html-reader-AD-3t4').on('click', '.ad-logo', function () {
                new NoAdDialog();
            });
        }
    })
}();
!function(){    require.async(['wkview:widget/common_toc_reader/common/doc_banner/index.js', 'wkview:widget/common_toc_reader/common/ad/ad.js'], function (DB, ad) {
        this.db = new DB({
            id: '2'
        });

        var isJiaoyuVip = parseInt('0', 10);
        var jobHunt = {
            isJobHunt: parseInt('', 10),
            buttonTips: '',
            url: '',
            statisticsClickId: '',
            pageTips: '',
            statisticsDisplayId: '',
            keyword: ''
        };
        if ('xreader' === 'ppt') {
            jobHunt = false;
        }
        var docInfo = {
            docId: 'e167fbacae45b307e87101f69e3143323968f5cc',
            title: '涉密计算机管理制度'
        };
        var adBlockStatus = +'';
        ad.init(isJiaoyuVip, jobHunt, docInfo, adBlockStatus);
    })
}();
!function(){        require.async(["wkcommon:widget/lib/tangram/base/base.js", "wkcommon:widget/lib/fis/data/data.js", "wkcommon:widget/ui/reader/reader.js", "wkcommon:widget/ui/js_core/log/log.js", "wkview:widget/ui/view/reader_pace/reader_pace.js", "wkview:widget/common_toc_reader/reader_xreader/index.js", "wkview:widget/common_item/endPageFcShow/endPageFcShow.js", "wkview:widget/view_recom_thirdad/endPageGoldClueAd/endPageGoldClueAd.js"],function(){{var e=arguments,o=0,d=e[o++],n=e[o++],a=e[o++],r=e[o++],t=e[o++],i=e[o++];e[o++],e[o++]}d.dom.ready(function(){r.xsend(1,101170),window.viewTime.s=(new Date).getTime();var e=d.dom.g("reader-container-1"),o=parseInt("1",10),c=parseInt("6",10),s=[o,Math.min(o+49,c)],f=!0,g=n.get("WkInfo");g.DocInfo.isApi&&(f=!1),window.player=a.reader({type:"doc",els:d.dom.query(".bd",e),doc_id:"e167fbacae45b307e87101f69e3143323968f5cc",doc_id_update:"383e8336c281e53a5802ff9e",pageCount:s[1]-s[0]+1,startPage:o,isLogin:parseInt("1",10),zoomLevel:1,copyable:!parseInt("0",10),pw:e.offsetWidth-4,ph:e.offsetHeight,container:e,readerVersion:"6",loadingHTML:'<div class="xreader-loading-layer"></div>',errorHTML:'<div class="xreader-error-layer"></div>',needPlugins:f}),r.send("view","load",{docId:"e167fbacae45b307e87101f69e3143323968f5cc",success:1,docType:"doc",ext:"doc",fr:"in",version:"6",cid1:"3",cid2:"63",cid3:"162",cid4:"0",ply:"html"});var l=n.get("WkInfo").readerFromSetting;l&&(document.body.style.visibility=""),window.player&&window.player.create();var I=!1,p=d.lang.eventCenter;I&&p.addEventListener("ReaderCreate.after",function(e,o){var d=o.reader;d.NS_IK_getPagethOnClose=function(){return d.getPage()},d.NS_IK_getPageOffset=function(){return 0};var n={getReader:function(){return d}},a=t.readerPace,r=new a(n);r.sendPaceInRate(),p.removeEventListener("ReaderCreate.after","RP")},"RP");var w=function(){var e=1,o=i.htmlReader;window.reader=new o({el:"reader-container-1",doc_id:"e167fbacae45b307e87101f69e3143323968f5cc",doc_id_update:"383e8336c281e53a5802ff9e",htmlUrls:'{\x22ttf\x22:[{\x22pageIndex\x22:1,\x22param\x22:\x22&md5sum=eca395b49edb00ad238df924ac49504b&range=0-100457&sign=190fc0dc96\x22},{\x22pageIndex\x22:2,\x22param\x22:\x22&md5sum=eca395b49edb00ad238df924ac49504b&range=100458-204795&sign=190fc0dc96\x22},{\x22pageIndex\x22:3,\x22param\x22:\x22&md5sum=eca395b49edb00ad238df924ac49504b&range=204796-282690&sign=190fc0dc96\x22},{\x22pageIndex\x22:4,\x22param\x22:\x22&md5sum=eca395b49edb00ad238df924ac49504b&range=282691-356753&sign=190fc0dc96\x22},{\x22pageIndex\x22:5,\x22param\x22:\x22&md5sum=eca395b49edb00ad238df924ac49504b&range=356754-425667&sign=190fc0dc96\x22},{\x22pageIndex\x22:6,\x22param\x22:\x22&md5sum=eca395b49edb00ad238df924ac49504b&range=425668-&sign=190fc0dc96\x22}],\x22json\x22:[{\x22pageIndex\x22:1,\x22pageLoadUrl\x22:\x22https:\\\/\\\/wkbjcloudbos.bdimg.com\\\/v1\\\/docconvert9104\\\/wk\\\/eca395b49edb00ad238df924ac49504b\\\/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sun%2C%2001%20Dec%202019%2011%3A40%3A57%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2019-10-17T03%3A40%3A57Z%2F3600%2Fhost%2Fbbb7a797ea9bd57341c0bfb9f5bda00bccccf02884007c3017b7f78c09b823ae&x-bce-range=0-11751&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3MTI4NzI1NywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.CHWLp%2ByjGlvs%2B%2BplswsZsr96EwzBAqOwKSXtR%2Bi9O0o%3D.1571287257\x22},{\x22pageIndex\x22:2,\x22pageLoadUrl\x22:\x22https:\\\/\\\/wkbjcloudbos.bdimg.com\\\/v1\\\/docconvert9104\\\/wk\\\/eca395b49edb00ad238df924ac49504b\\\/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sun%2C%2001%20Dec%202019%2011%3A40%3A57%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2019-10-17T03%3A40%3A57Z%2F3600%2Fhost%2Fbbb7a797ea9bd57341c0bfb9f5bda00bccccf02884007c3017b7f78c09b823ae&x-bce-range=11752-24038&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3MTI4NzI1NywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.dGde%2FJCzJmFsQ%2BCqoqmkPgTs3UffdV3AKJHjsnXLfxc%3D.1571287257\x22},{\x22pageIndex\x22:3,\x22pageLoadUrl\x22:\x22https:\\\/\\\/wkbjcloudbos.bdimg.com\\\/v1\\\/docconvert9104\\\/wk\\\/eca395b49edb00ad238df924ac49504b\\\/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sun%2C%2001%20Dec%202019%2011%3A40%3A57%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2019-10-17T03%3A40%3A57Z%2F3600%2Fhost%2Fbbb7a797ea9bd57341c0bfb9f5bda00bccccf02884007c3017b7f78c09b823ae&x-bce-range=24039-35817&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3MTI4NzI1NywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.Y15n1bl94dzoN4io3%2BmF3LAuBfBBRUTIbyUxYYe3MeE%3D.1571287257\x22},{\x22pageIndex\x22:4,\x22pageLoadUrl\x22:\x22https:\\\/\\\/wkbjcloudbos.bdimg.com\\\/v1\\\/docconvert9104\\\/wk\\\/eca395b49edb00ad238df924ac49504b\\\/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sun%2C%2001%20Dec%202019%2011%3A40%3A57%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2019-10-17T03%3A40%3A57Z%2F3600%2Fhost%2Fbbb7a797ea9bd57341c0bfb9f5bda00bccccf02884007c3017b7f78c09b823ae&x-bce-range=35818-47363&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3MTI4NzI1NywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.l9kcUkNhUbpAeuFLp7lquY%2Fogs0fQ5Hr0FkMO2ew0is%3D.1571287257\x22},{\x22pageIndex\x22:5,\x22pageLoadUrl\x22:\x22https:\\\/\\\/wkbjcloudbos.bdimg.com\\\/v1\\\/docconvert9104\\\/wk\\\/eca395b49edb00ad238df924ac49504b\\\/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sun%2C%2001%20Dec%202019%2011%3A40%3A57%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2019-10-17T03%3A40%3A57Z%2F3600%2Fhost%2Fbbb7a797ea9bd57341c0bfb9f5bda00bccccf02884007c3017b7f78c09b823ae&x-bce-range=47364-59116&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3MTI4NzI1NywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.4lFOwf84AdKqXUtgaL%2BRjNPMt1YZdSD4fLH226W%2BQtg%3D.1571287257\x22},{\x22pageIndex\x22:6,\x22pageLoadUrl\x22:\x22https:\\\/\\\/wkbjcloudbos.bdimg.com\\\/v1\\\/docconvert9104\\\/wk\\\/eca395b49edb00ad238df924ac49504b\\\/0.json?responseContentType=application%2Fjavascript&responseCacheControl=max-age%3D3888000&responseExpires=Sun%2C%2001%20Dec%202019%2011%3A40%3A57%20%2B0800&authorization=bce-auth-v1%2Ffa1126e91489401fa7cc85045ce7179e%2F2019-10-17T03%3A40%3A57Z%2F3600%2Fhost%2Fbbb7a797ea9bd57341c0bfb9f5bda00bccccf02884007c3017b7f78c09b823ae&x-bce-range=59117-&token=eyJ0eXAiOiJKSVQiLCJ2ZXIiOiIxLjAiLCJhbGciOiJIUzI1NiIsImV4cCI6MTU3MTI4NzI1NywidXJpIjp0cnVlLCJwYXJhbXMiOlsicmVzcG9uc2VDb250ZW50VHlwZSIsInJlc3BvbnNlQ2FjaGVDb250cm9sIiwicmVzcG9uc2VFeHBpcmVzIiwieC1iY2UtcmFuZ2UiXX0%3D.P3D3EdyH9n0FVmcRsGS3r7%2F%2BojkcmM%2FvopEiKIbz6g8%3D.1571287257\x22}],\x22png\x22:[]}',type:n.get("WkInfo").docType["4"],startPage:parseInt("1",10),pageCount:parseInt("6",10),totalPageNum:parseInt("6",10),isPayMent:parseInt("0",10),ispaided:parseInt("",10),shareElId:"shareMore-1",zoomLevel:e,reader:window.player,version:"6",bookmark:[parseInt("0",10),parseInt("0",10)],isPrivate:Boolean(""),isLogin:parseInt("1",10),uid:"1",toPage:parseInt("1",10),payment:parseInt("0",10),needPlugins:f})};w(),d.lang.eventCenter.addEventListener("smallFlowDownBtn",function(){r.xsend(1,101167)})})});;
    }();
!function(){    require.async(['wkview:widget/common_toc_reader/common/doc_bottom/compAsync/index.js'], function (CompAsync) {
        new CompAsync();
    });
    require.async(['wkview:widget/common_toc_reader/common/doc_bottom/doc_bottom.js'], function (DB) {
        this.db = new DB();
    })
}();
!function(){    require.async(['wkview:widget/next_doc/next_doc.js'], function (ND) {
        ND();
    });
}();
!function(){    require.async(["wkcommon:widget/lib/tangram/base/base.js", "wkview:widget/ui/view/doc_share/doc_share.js", "wkview:widget/ui/view/pay_org_vip/pay_org_vip.js", "wkcommon:widget/ui/payCheck/payCheck.js", "wkcommon:widget/lib/fis/data/data.js", "wkcommon:widget/ui/js_core/log/log.js", "wkcommon:widget/ui/js_core/util/util.js", "wkview:widget/ui/util/util.js", "wkview:widget/common_toc_reader/reader_xreader/index.js", "wkcommon:widget/ui/js_core/login/login.js", "wkcommon:widget/ui/js_core/dialogCashier/dialogCashier.js", "wkview:widget/ui/view/down_doc/down_doc.js", "wkview:widget/ui/view/down_wangpan/down_doc.js"],function(){{var e=arguments,o=0,d=e[o++],n=e[o++],i=(e[o++],e[o++],e[o++]),c=e[o++],t=e[o++],r=e[o++],a=(e[o++],e[o++]),s=(e[o++],e[o++]),l=e[o++],f=s.downDocCreate();l.downDocCreate()}d.lang.eventCenter.addEventListener("download.doc",function(e,o){o=o||{};var d=o.from||!1;"payDialog"===d?f.getFile():f.start()}),i.set("readerStartPage",parseInt("1",10)),d.lang.eventCenter.addEventListener("pack.button.hide",function(){$(".pack-pay").css("display","inline-block")});var w=3;d.dom.ready(function(){function e(){var e=d.page.getViewWidth(),o=d.dom.query("#bd .body")[0].offsetWidth,n=d.dom.g("doc");n.style.width=o>e?o+"px":"auto",n=null}$("body").addClass("newTools"),$(".btn-login-joinvip-rightnow").on("click",function(){d.lang.eventCenter.addEventListener("Login.Success",function(e){d.event.stop(e),c.xsend(1,101911),window.location.href="/cashier/browse/dispatch?dqStatCode=31_8_9_97&from_doc=e167fbacae45b307e87101f69e3143323968f5cc"});var e=i.get("WkInfo").PageInfo.isLogin;e||c.xsend(1,100349),c.xsend(1,100349),c.xsend(1,101911),window.location.href="/cashier/browse/dispatch?dqStatCode=31_8_9_97&from_doc=e167fbacae45b307e87101f69e3143323968f5cc"});var o=n.shareToCreate({el:d.dom.q("reader-tools-share")[0],view:"viewReader-1",copy:"copyCode-1",panel:"panel-1",closePanel:"closePanel-1",toggleSize:["normalSize-1","bigSize-1"],codeText:"readerCode-1",copyResult:"copyResult-1"});o.show();var s=function(){var e=d.dom.g("normalSize-1").checked;return e?"small":"big"};d.event.on("viewReader-1","click",function(){c.send("view","share",{subtype:"sharepreview",size:s(),pos:"top",copyright:3,readerVersion:w})}),d.event.on("copyCode-1","click",function(){c.send("view","share",{subtype:"sharecopy",size:s(),pos:"top",copyright:3,readerVersion:w})}),d.lang.eventCenter.addEventListener("Reader.zoomChange",function(){var o=d.dom.query("#bd .body")[0],n=d.dom.query("#bd .bd-wrap")[0],i=d.dom.query("#bd .crubms-wrap");i.length>1&&(i=i[0],i.style.width=o.offsetWidth+"px"),n.style.minWidth=o.offsetWidth+"px",e()}),d.lang.eventCenter.addEventListener("Reader.WindowResize",e),d.lang.eventCenter.addEventListener("Reader.fullScreenResize",e),parseInt("0",10)&&c.send("view","payview",{docId:"e167fbacae45b307e87101f69e3143323968f5cc",docType:"doc",ext:"doc",fr:"in",version:"6",cid1:"3",cid2:"63",cid3:"162",cid4:"0",ply:"html",pn:"6"});var l="",f="",g=t.debounce(function(){c.send("view","toolbarClick",{area:"toolbar",mode:f,item:l,docType:"doc",ext:"doc",fr:"in",version:"6",cid1:"3",cid2:"63",cid3:"162",cid4:"0",ply:"html"})},1e3);d.lang.eventCenter.addEventListener("ReaderToolsBar.itemClick",function(e,o){var d=o.setting.isFullScreen;l=o.name,f=d?"fullscreen":"normalscreen","fullscreen"===l&&(f=d?"normalscreen":"fullscreen",l=d?"fullscreen":"normalscreen"),g()});var p=parseInt("1",10),v=(new Date).getTime(),u=function(e){c.send("view","browse",{docId:"e167fbacae45b307e87101f69e3143323968f5cc",docType:"doc",ext:"doc",page:e,fr:"in",version:"6",cid1:"3",cid2:"63",cid3:"162",cid4:"0",ply:"html"})};d.lang.eventCenter.addEventListener("Reader.scroll",function(e,o){var d=o.currentPage;if(d!==p){var n=(new Date).getTime();n-v>500&&u(p),p=d,v=n}}),function(){d.lang.eventCenter.addEventListener("view-log",function(e,o){var d=o.method||"send",n=o.args||[],r=i.get("WkInfo").DocInfo;("send"===d||"nslog"===d)&&n.length>2&&t.mix(n[2]||{},{cid1:r.cid1,cid2:r.cid2,cid3:r.cid3,cid4:r.cid4,docId:r.docId,doctype:r.docType},!0),c[d]&&c[d].apply(this,n)})}();window.name="",document.body.focus(),d.event.on(window,"onbeforeunload",function(){var e=window.reader.getPage(),o=0;r.saveViewedPage("e167fbacae45b307e87101f69e3143323968f5cc",e,o)}),d.cookie.remove("newMark",{path:"/view/"}),d.lang.eventCenter.addEventListener("do-login",function(){a.login.verlogin(function(){location.reload()})})})});;
}();
!function(){	require.async(['wkcommon:widget/ui/lib/jquery/jquery.js', 'wkcommon:widget/lib/tangram/base/base.js', 'wkcommon:widget/lib/fis/data/data.js', 'wkview:widget/kg_recommend/util/config.js'], function ($, T, Data, config) {

        // 在原来的view页面底部——你可能喜欢（stru_recom.tpl）模块没有数据就派发kgRecommendview
        T.lang.eventCenter.addEventListener('kgRecommendview', kgRecommendviewRender);

        function kgRecommendviewRender () {
            // 全局变量
            Data.set('docId', 'e167fbacae45b307e87101f69e3143323968f5cc');

            // 请求总接口，判断是否有知识图谱相关推荐模块
            var url = config.url[config.type['getrelinfo']];
            var options = {
                doc_id: 'e167fbacae45b307e87101f69e3143323968f5cc'
            };
            $.getJSON(url + '?callback=?', options).then(function (data) {
                if (data.code === 0) {
                    require.async(['wkview:widget/kg_recommend/kg_recommend.js'], function (kgRecommend) {
                        // 入口文件
                        new kgRecommend.main({
                            'el': '.kgrecommend-wrap',
                            'docId': 'e167fbacae45b307e87101f69e3143323968f5cc',
                            'data': data
                        });
                    });
                }
            });
        }
	});
}();
!function(){    require.async(['wkview:widget/stru_recom/index.js'], function (Recom) {
        this.recom = new Recom({
			readerType: 'xreader',
            recommendType: '',
            uid: '3',
            docId: 'e167fbacae45b307e87101f69e3143323968f5cc',
            refer_query: ''
        });
    });
}();
!function(){    require.async('wkview:widget/comment/comment_default/comment_default.js');
}();
!function(){    require.async(['wkview:widget/ad/commonAd/commonAd.js'], function (page) {
        page.init();
    });
}();
!function(){    require.async(['wkcommon:widget/ui/lib/jquery/jquery.js', 'wkcommon:widget/vipNoAdDialog/vipNoAdDialog.js'], function($, NoAdDialog) {
        $('.ft .ad-vip-close-bottom, .ggbtm-vip-close').on('click', function() {
            new NoAdDialog();
        });
    });
}();
!function(){    require.async(['wkcommon:widget/lib/tangram/base/base.js', 'wkcommon:widget/ui/js_core/login/login.js', 'wkcommon:widget/ui/js_core/log/log.js', 'wkcommon:widget/ui/lib/store/store.js', 'wkcommon:widget/lib/fis/data/data.js', 'wkcommon:widget/ui/lib/jquery/jquery.js'], function (T, Login, log, Store, Data, $) {
        log.xsend(1,100601);
        var login = Login.login;
        var islogin = $('.doc-upload').data('login');
        var $uploadWrap = $('.doc-upload').find('.new-upload-btns');

        if (islogin == true) {
            $('.btn-upload').attr('href', '/new?fr=view');
            $('.btn-upload').attr('target', '_blank');
        }
        T.event.on('uploadDoc-2', 'click', function (e) {
            login.verlogin(function () {}, null, null, {
                actionName: 'upload',
                fromMod: 'upload'
            });
        });

        //上传按钮
        $('.btn-upload-new').hover(function () {
            $uploadWrap.show();
        }, function () {
            $uploadWrap.hide();
        });
        $uploadWrap.hover(function () {
            $uploadWrap.show();
        }, function () {
            $uploadWrap.hide();
        });

        $uploadWrap.on('click', 'a', function (event) {
            login.verlogin(function () {}, null, null, {
                actionName: 'upload',
                fromMod: 'upload'
            });
        });

        $('.btn-upload-new').on('click', function () {
            var WkInfo = Data.get('WkInfo') || {};
            if (~~WkInfo.DocInfo.is_exam_link) {
                log.xsend(1, 100718);
            }
        });
    });
}();
!function(){    require.async(['wkcommon:widget/ui/js_core/log/log.js'], function (log) {
        log.xsend(1, 100621);
    });
}();
!function(){    require.async(['wkview:widget/common_item/serviceEntry/index.js'], function(Index) {
        this.index = new Index({
            docTitle: '涉密计算机管理制度',
            cid1: '3',
            cid2: '63',
            cid3: '162'
        });
    });
}();
!function(){    require.async(['wkview:widget/ad/viewSideDownAd/viewSideDown.js'], function (viewSideDown) {});
}();
!function(){    require.async(["wkcommon:widget/360tip/360tip.js"],function(e){var r=e.showTopTip,t={referer:""};new r(t).create()});;
}();
!function(){    var bds_config = {
        bdPic: '//gss0.baidu.com/70cFsjip0QIZ8tyhnq/img/iknow/wenku/erweima2001.jpg',
        snsKey: {
            tsina: 2273341579,
            tqq: 801199444
        },
        bdText: '我正在@百度文库 阅读【涉密计算机管理制度】这篇文章，推荐给大家！用文库客户端可以免积分下载该文档，客户端下载地址：http://'
            + location.host
            + '/apps?fr=2001 想立即阅读该文档点这里：'
    };
    document.getElementById('bdshell_js').src = '//edu-wenku.bdimg.com/v1/pc/bdshare/static/api/js/share.js?cdnversion=' + new Date().getHours();
    // 重写qzone分享事件
    require.async(['wkcommon:widget/lib/tangram/base/base.js'], function (T) {
        // 重写qzone分享事件
        var qzones = T.q('sns_qzone');
        if (qzones) {
            T.array.each(qzones, function (item, i) {
                T.event.on(item, 'mouseover', function () {
                    T.ajax.post(
                        '/user/interface/qqShareOption',
                        'app=bind_status',
                        function (xhr, responseText) {
                            try {
                                var errno = eval('(' + responseText + ')');
                                // 如果已绑定
                                if (errno.list.join(',').indexOf('qq') > -1) {
                                    if (item.innerHTML.indexOf('分享到QQ空间') < 0) {
                                        item.innerHTML = '';
                                    }
                                    qzones[i].onclick = function () {
                                        window.open(
                                            'http://'
                                                + location.host
                                                + '/user/browse/qqShare?url=' + T.string.encodeHTML(location.href),
                                            'blank'
                                        );
                                    }
                                }
                            }
                            catch (ex) {}
                        }
                    );
                });
            });
        }
    });
}();
!function(){    require.async(['wkcommon:widget/ui/lib/jquery/jquery.js', 'wkview:widget/fix_searchbar/fix_searchbar.js', 'wkcommon:widget/lib/fis/data/data.js'], function ($, FSB, Data) {
        var WkInfo = Data.get("WkInfo") || {};
        WkInfo.UserInfo = WkInfo.UserInfo || {};
        WkInfo.UserInfo = $.extend(true, {}, {"status":0,"need_set_cookie":0,"uid":1724948680,"uname":null,"displayname":null,"ltime":1571110234,"utime":1571110234,"atime":1571110234,"acount":0,"gdata":null,"pdata":"1\u0000\u0000100\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000\u0000","encoding":"gbk","isIncomplete":0,"isLogin":true,"uip":"119.136.91.187","uipNum":"3143338103","tableId":35,"registerType":0,"verifiedEmail":true,"snsBinded":0,"isHalfUname":0,"isFrom":0,"isNoUname":false,"utype":0,"wenkuLogin":1,"wenkuReg":0,"power":1,"isAdmin":false,"exp":"20","wealth":"0","gradeTitle":null,"gradeLevel":"\u04bb","gradeNum":1,"isPayUpload":0,"isProfessionalUpload":0,"isPGCPopup":0,"isPGC":0,"isBGC":0,"isBusinessUser":0,"headicon":"https:\/\/gss0.bdstatic.com\/7Ls0a8Sm1A5BphGlnYG\/sys\/portraitn\/item\/wenku.1.77c38886.XftyCgxYBqZM-LwMActxfQ.jpg","isRealName":1,"userGradeName":"\u04bb","userGradeNum":1,"userGradeTitle":null,"userName":null,"userScore":"20","smallFlowProfessionalDoc":1,"sf_svip":2111}, WkInfo.UserInfo);
        $(function () {
            new FSB.fixSearchBar({
                evaluateBoxId: '#doc-evaluate-mod',
                evaluateTagId: '#doc-main',
                evaluatePreCl: '.reder-share-model'
            });
            $('.top-down-load-container').addClass('view_change_test');
        });
    } );
}();
!function(){    require.async(['wkview:widget/ad_taishan/ad_taishan.js'], function (adTaishan) {
        T.lang.eventCenter.addEventListener('ReaderCreate.after', function () {
            adTaishan.init();
        });
    });
}();
!function(){	require.async(['wkcommon:widget/lib/tangram/base/base.js', 'wkcommon:widget/ui/js_core/log/log.js', 'wkcommon:widget/ui/lib/jquery/jquery.js', 'wkcommon:widget/ui/js_core/util/util.js', 'wkcommon:widget/ui/js_core/eventCenter/eventCenter.js'], function (T, log, $, util, E) {
		$.ajax({
			url: '/doc/interface/gaokaozhenti?docid=e167fbacae45b307e87101f69e3143323968f5cc',
			success: function (json) {
				if (json.data.flag) {
					log.xsend(1, json.data.act_id);
				}
			}
		});
		// 阅读器统计
		log.send('view', 'htmlview', {
			docId: 'e167fbacae45b307e87101f69e3143323968f5cc',
			docType: 'doc',
			cid1: '3',
			cid2: '63',
			cid3: '162',
			cid4: '0',
			totalPageNum: '6',
			pn: '1'
		});

		// 浏览历史记录请求
					T.dom.ready(function () {
				var url = '/browse/vw?doc_id=e167fbacae45b307e87101f69e3143323968f5cc';
				T.ajax.get(url);
			});
		
		util.windowResize(function () {
			resize();
		});

		setTimeout(function () {
			resize();
		}, 1000);
		function resize() {
			$('#html-reader-our-ad-1').css( 'width', $('.reader-container').css('width') );
			$('#ggbtm').css('width', $('.reader-container').css('width') );
		}

	});
}();
!function(){    require.async(['wkview:widget/common_toc/reader_html/page_body/main.js'], function (PageBody) {
        this.pageBody = new PageBody({
            docId: 'e167fbacae45b307e87101f69e3143323968f5cc',
            docTitle: '涉密计算机管理制度',
            flag: +'1',
            needShowAd: +'1',
            needShowAd2: +'1',
            orgName: '',
            is_tianyancha_doc: ''
        });
    });
}();
!function(){    require.async(['wkcommon:widget/ui/js_core/log/log.js', 'wkcommon:widget/lib/fis/data/data.js'], function (log, Data) {
    var WkInfo = Data.get('WkInfo') || {};
    var WkAdInfo = WkInfo.WkAdInfo || {};
    var offAdSmallFlow = WkAdInfo.offAdSmallFlow || 1;
        log.xsend(1, 100737, {
            sf_svip: '2111' || 0,
            reader_type: 'reader_html',
            offAdSmallFlow: offAdSmallFlow
        });
        var professionalDoc = '' || 0;
        if (professionalDoc) {
            log.xsend(1, 101653);
        }
        var $isPartnerDoc = '' || 0;
        var $isPaied = '' || 0;
        var $isPickDoc = '0' || 0;
        if (+$isPartnerDoc) {
            log.xsend(1, 101792, {
                index: 10
            });
            if (+$isPaied) {
                log.xsend(1, 101792, {
                    index: 11
                });
            }
        }
        if (+$isPickDoc) {
            log.xsend(1, 101835, {
                index: 1
            });
        }
    });
}();
!function(){        require.async(['wkview:widget/common_toc/common/main.js'], function () {})
    }();
</script>
<div id="docBubble" class="docBubble"><i class="triangle-t"></i><i title="关闭" class="close markSend">关闭</i><div class="tl"><div class="inner log-xsend" data-logxsend="[1,100002]"></div></div><div class="tr"></div><div class="bl"></div></div><div class="tangram-suggestion-main fsb-suggestion-main" id="tangram-suggestion--TANGRAM$3-main" data-guid="TANGRAM$3" style="position: absolute; display: none; left: 335.5px; top: 109px; width: 534px;"><div id="tangram-suggestion--TANGRAM$3" class="tangram-suggestion" style="position:relative; top:0px; left:0px"></div></div><div class="tangram-suggestion-main fsb-suggestion-main" id="tangram-suggestion--TANGRAM$4-main" data-guid="TANGRAM$4" style="position: absolute; display: none; left: 335.5px; top: 109px; width: 534px;"><div id="tangram-suggestion--TANGRAM$4" class="tangram-suggestion" style="position:relative; top:0px; left:0px"></div></div><div class="fix-searchbar-wrap" style=""> <div class="bg-opacity"></div> <div class="sb-con clearfix" style="width: 1118px;"> <div class="evaluate-wrap"> <div class="evaluate"></div> </div> <a href="/" class="wk-logo bg-fsb"></a> <div class="search-form-wrap"> <form action="/search" name="ftop" id="topSearchBox" method="get" class="fsb-search-form">
<span class="s_ipt_wr s_ipt_wr-with535">
<input id="kw" name="word" class="s_ipt" maxlength="256" tabindex="1" value="" data-default="" autocomplete="off" style="margin-left: 6px;">
<span class="s_ipt_plhd" id="kw-plhd">搜试试</span>
<span class="hot-box">2</span>
<span class="arrow-box"></span>
</span><span class="s_btn_wr">
<input type="submit" id="sb" value="搜索文档" class="s_btn s_btn_wr_click">
</span><span class="s_tools"><a class="sp-xs-tips log-xsend" data-logxsend="[1, 100955, {&quot;index&quot;:1}]" href="/task/browse/rewardbegin?fr=home" target="_blank">悬赏文档</a></span>
<div class="g-sl" alog-group="switch.doctype">
<label for="t_all"><input type="radio" name="lm" value="0" class="type-check" id="t_all" checked="">全部</label>
<label for="t_doc"><input type="radio" name="lm" value="1" class="type-check" id="t_doc">DOC</label>
<label for="t_ppt"><input type="radio" name="lm" value="3" class="type-check" id="t_ppt">PPT</label>
<label for="t_txt"><input type="radio" name="lm" value="5" class="type-check" id="t_txt">TXT</label>
<label for="t_pdf"><input type="radio" name="lm" value="2" class="type-check" id="t_pdf">PDF</label>
<label for="t_xls"><input type="radio" name="lm" value="4" class="type-check" id="t_xls">XLS</label>
<div style="clear:both"></div>
</div>
<input type="hidden" name="od" value="0">
<input type="hidden" name="fr" value="top_home">
<input type="hidden" name="ie" value="gbk">
<input type="hidden" id="ext-spara" name="fr_ext" value="ceiling"></form> <div class="search-form-holder"></div></div> <a class="gk-2016-flow log-xsend" target="_blank" data-logxsend="[1, 100781, {‘index’: 1}]"></a> <div class="qrHover">&nbsp;&nbsp;&nbsp; <div class="wrap-big"> <div class="qrcode"></div> <div class="qr-title">马上扫一扫</div> <div class="qr-text"> 手机打开<br> 随时查看 </div> </div> <span class="open-in-phone"> <span style="font-size:14px;color:#5DC1A2;" class="iconfont"></span> 在手机打开 </span> <div class="add-has-money-pay" style="line-height: 20px;"> <div class="add-money-icon"><div class="add-img"></div></div> <div class="add-has-money-text"><span class="banner-text log-xsend addUnderLine" data-href="https://wenku.baidu.com/ndgoods/browse/customizedppt" style="white-space: normal; width: 83px;">专业PPT定制！</span></div> </div> </div> <div class="top-down-load-container view_change_test"> <a id="top-download-btn" class="top-download-btn ui-bz-btn-senior " href="javascript:void(0);"> <b class="ui-btn-p-16 ui-btn-btc"> <i class="iconfont"></i>下载</b> </a>             <span class="top-download-price">                 <span class="top-download-text">2&nbsp;下载券</span> </span>             <span class="top-download-tip" style="display:none;">                 <span class="text">做任务领下载券</span>                 <a href="//wenku.baidu.com/task/browse/daily" target="_blank" class="btn">立即前往</a>                 <span class="adorn"></span>             </span>         </div> <div class="user-bar-new user-bar-login" style="left: 914px;">  <ul class="inner"> <!--未登录-->  <li class="mn-lk-w member-icon" id="user-bar-uname">  <a id="userNameCon" href="/user/mydocs" target="_blank" class="uname-search-bar mn-lk user-my-name log-xsend user-bar-home-link" data-logxsend="[1, 100795, {'index': 'fis-search-bar' }]"> <span class="text-dec-under">  小虫很酷  </span> <span id="wk-user-icon-home-search-bar"><span class="iconfont ic-not-vip"></span></span> </a> <div class="user-my-name-tip-search-bar user-mn-tip"> <ul class="user-mn-tip-inner"> <li class="user-info-wrap"> <div class="user-image" style="background-image:url(https://gss0.bdstatic.com/7Ls0a8Sm1A5BphGlnYG/sys/portraitn/item/wenku.1.77c38886.XftyCgxYBqZM-LwMActxfQ.jpg)"></div> <div class="user-tip-info"> <a class="user-name log-xsend" href="/user/mydocs" target="_blank" data-logxsend="[1, 101969, {'index':'name-search-bar'}]">  小虫很酷  <div class="tip-vip-ico"><span class="iconfont ic-not-vip"></span></div> </a> <div class="vip-info"> <span class="tip-vip-status">您还未开通VIP</span> <a class="tip-vip-btn-search-bar" href="/ndcashier/browse/jiaoyuvipcashier?cashier_code=ViewXdIdcardKt" target="_blank">立即开通</a> </div> </div> <a href="https://passport.baidu.com/?logout&amp;aid=7&amp;u=https%3A//wenku.baidu.com/view/e167fbacae45b307e87101f69e3143323968f5cc.html%3Frec_flag%3Ddefault%26sxts%3D1571282613997" id="logout-btn" class="log-xsend tip-logout" data-logxsend="[1, 102114, {'index': 'logout'}]">退出</a> </li> <li class="card-info"> <a class="card-item log-xsend" href="/user/mydocs" target="_blank" data-logxsend="[1, 101969, {'index':'user-search-bar'}]"> <span class="card-ico"><i class="user-card"></i></span> 个人中心 </a> <a class="card-item log-xsend" href="/ndvipmember/browse/index" target="_blank" data-logxsend="[1, 101969, {'index':'vip-search-bar'}]"> <span class="card-ico"><i class="vipmember-card"></i></span> 会员中心 </a> <a class="card-item log-xsend" href="/user/task?fr=status" target="_blank" alog-action="fisSearchBar.mytask" data-logxsend="[1, 101969, {'index':'task-search-bar'}]"> <span class="card-ico"><i class="task-card"></i></span> 我的任务 </a>  <a class="card-item log-xsend" href="/wenkuverify?from=3" target="_blank" data-logxsend="[1, 100135, {'index':'auth-search-bar'}]"> <span class="card-ico"><i class="auth-card"></i></span> 申请认证 </a>  </li> </ul> </div> </li> <li style="position: relative;"><a href="/cashier/browse/dispatch?dqStatCode=ViewXdVipWordKt" target="_blank" title="" style="height: auto;" id="my-wkHome-vip-tips-search-bar" class="log-xsend"><span class="s-vip-text">加入VIP</span></a><div class="vip-tips-hover-div clearfix" style="width: 180px;"><div class="vip-tips-hover-div-content"><ul><li class="icon-pro-doc">享VIP专享文档下载特权</li><li class="icon-share-doc">赠共享文档下载特权</li><li class="icon-free-doc">100w优质文档免费下载</li><li class="icon-yuedu-vip">赠百度阅读VIP精品版</li></ul><a target="_blank" class="log-xsend vip-tips-hover-gotocashier ljkt-btn-gold vip-tips-hover-to-cashier" data-logxsend="[1, 101547, {'index': 0,'pptChuileiView': undefined}]" href="/cashier/browse/dispatch?dqStatCode=ViewXdVipBtmKt">立即开通</a></div></div></li>  <!--登录--> </ul> </div> <div class="fix-searchbar-gaokao"></div> <div class="tob-fc-bar"> </div> </div>     <div class="fix-searchbar-ad"> <a href="javascript:;" class="btn-fix-searchbar-close"></a>         <a href="//wenku.baidu.com/miti" class="fix-searchbar-img log-xsend" data-logxsend="[1, 100452]" target="_blank">             <img src="https://edu-wenku.bdimg.com/icms_transform/img/iknow/wenku/img_miti_topbar_400x50.png"> </a>     </div></div><div id="reader-qrcode-tip" class="ui-panel trg-tl" tabindex="-1" style="left: -9000px; top: -9000px;"><div class="tips-wrap"><span class="trangle"></span><div class="inner"><div class="hd"><span class="title">选择内容扫一扫<br>立即发送到手机</span><span class="act"><a href="###" class="ir close">×</a></span></div><div class="bd"><div id="reader-qrcode-marker"></div><div class="vip-text super-vip"><a target="_blank" href="/cashier/browse/vipcashier?cashier_code=send_joinvip">VIP享无限制发送特权</a></div><div id="reader-qrcode-msg" style="display:none">*已选择了<span id="reader-qrcode-wordnum"></span>字，最多支持100字</div></div></div></div></div><div id="reader-translate-tip" class="ui-panel trg-tl" tabindex="-1" style="left: -9000px; top: -9000px;"><div class="tips-wrap"><span class="trangle"></span><div class="inner"><div class="hd"><span class="title">以下结果由<img src="https://edu-wenku.bdimg.com/icms_transform/img/iknow/wenku/fanyi/fanyi.png">提供：<span id="reader-translate-title"></span></span><span class="act"><a href="###" class="ir close">×</a></span></div><div class="bd"><div id="reader-translate-marker"></div></div><div class="ft"><a href="http://fanyi.baidu.com/" id="reader-fanyi-link" target="_blank">百度翻译</a></div></div></div></div><div id="reader-baike-tip" class="ui-panel trg-tl" tabindex="-1" style="left: -9000px; top: -9000px;"><div class="tips-wrap"><span class="trangle"></span><div class="inner"><div class="hd"><span class="title">百科词条：<span id="reader-baike-title"></span></span><span class="act"><a href="###" class="ir close">×</a></span></div><div class="bd"><div id="reader-baike-marker"></div></div><div class="ft"><a href="http://baike.baidu.com/" target="_blank">百度百科</a></div></div></div></div><div id="tip-gc" style="display:none;"></div><div class="reader-back2top-wrap" id="activity-tg" style="display: none;"><a href="javascript:;" class="reader-convert"><span class="convert-bg"></span>格式转换</a><a href="javascript:;" class="reader-download-app" style="right: -1px;"><span class="app-bg"></span>客户端</a><a href="javascript:;" class="go-crawer log-xsend" data-logxsend="[1, 101889,{}]" style="right: -1px;"><span class="crawer-bg"></span>极速收纳</a><a class="reader-feedback log-xsend help-feedback" title="反馈" tabindex="-1" hidefocus="true" data-toolsbar-log="feedback" alog-action="htmltoolbar.feedback" data-logxsend="[1, 101890]" style="cursor: pointer; right: -1px;"><span class="feedback-icon"></span>反馈</a><a class="reader-backToTop" href="###" title="回到顶部" tabindex="-1" hidefocus="true" data-toolsbar-log="gotop" alog-action="htmltoolbar.back2top" style="right: -1px;"><span class="bg-index s-ic top"></span></a><div class="reader-convert-wrap"><i></i><p>VIP专享文档格式转换特权，PDF、Word、Excel、JPG、HTML等多种格式便捷转换</p></div><div class="reader-app-qrcode-wrap"><img src="https://edu-wenku.bdimg.com/v1/pc/app-qrcode_20170308.png" width="130" height="130"><p>扫码下载文库APP</p><p>随时随地浏览文档</p></div><div class="vip-container-wrap" style="display: none;"><div class="wrap-body"><div class="title"><span class="text">百度教育VIP专属资源,免费任性!</span><a class="more log-xsend" href="/user/browse/jiaoyuvipzone#recommend" target="_blank" data-logxsend="[1, 101182]">更多</a><span class="close"></span></div><div class="left-wrap"><div class="image-book"></div></div><div class="right-wrap"><div class="big">中国历史风云录</div><div class="small">和教科书迥然不同的中国历史挽救你被洗脑的智商</div><div class="btn"><a class="read log-xsend" target="_blank" data-logxsend="[1, 101183]" style="width: 160px;">加入VIP免费读全本</a><div class="collect" style="display: none;"><i class="icon"></i><span class="shoucang">收藏</span><div class="collect-wrap"><span class="first">已收藏至百度阅读<a href="/customer/mybook?item=collected" target="_blank" class="closet">我的书架</a></span></div></div></div></div></div></div><div class="video-container-wrap" style="display: none;"></div><div class="crawer-guide-wrap">全网好内容不错过<br>试试极速收纳吧!</div></div><div class="reader-tools-bar-wrap tools-bar-small tools-bar-smaller"><div class="reader-tools-bar" style="margin: auto; width: 1124px;"><div class="reader-tools-bar-center clearfix"><div class="left"><a class="ic reader-fullScreen xllDownloadLayerHit_left" href="javascript:;" title="全屏显示" data-toolsbar-log="fullscreen" alog-action="htmltoolbar.fullscreen"></a><div class="reader-tools-zoom xllDownloadLayerHit_left"><a href="###" class="ic zoom-decrease" title="缩小" data-toolsbar-log="zoomout" alog-action="htmltoolbar.zoomout"></a><a href="###" class="ic zoom-add" title="放大" data-toolsbar-log="zoomin" alog-action="htmltoolbar.zoomin"></a></div><div class="reader-tools-praise xllDownloadLayerHit_left"><i class="praise-add-num"></i><i class="praise-decrease-num"></i><a href="javascript:;" class="praise-add" title="点赞" data-toolsbar-log="zoomout" alog-action="htmltoolbar.zoomout"></a><a href="javascript:;" class="praise-decrease" title="点踩" data-toolsbar-log="zoomin" alog-action="htmltoolbar.zoomin"></a></div><div class="reader-tools-btn-wrap favo-wrap" tabindex="-1" hidefocus="true"><a class="reader-favo reader-favo-new" href="###" data-toolsbar-log="collect" alog-action="htmltoolbar.favo"></a></div><div class="mod doc-evaluate" id="doc-evaluate-mod" style="display: block;"><div class="content" id="reader-evaluate-content-wrap" data-id="e167fbacae45b307e87101f69e3143323968f5cc" data-value="-1" data-doc-value="0"><span class="evaluate-title">评价文档：</span><span id="total-star" class="star" alog-group="view.evaltotal"><b class="value-star total ic-star-t-off"></b><b class="value-star total ic-star-t-off"></b><b class="value-star total ic-star-t-off"></b><b class="value-star total ic-star-t-off"></b><b class="value-star total ic-star-t-off"></b></span><span class="value-tip" id="doc-evaluate-tips"></span></div><div class="value-pop"><span class="bot"></span><span class="top"></span><p></p></div></div><div class="reder-share-model bdshare_t bds_tools_32 get-codes-bdshare"><a href="javascript:;" class="ico-share"></a><div class="shareContent share-toggle"><div class="shareTitle ">分享到：</div><a href="#" title="分享到QQ空间" class="share_lv1_btn qqzone logSend share-toggle" data-logsend="{&quot;send&quot;:[&quot;view&quot;,&quot;share&quot;,{&quot;sns&quot;:&quot;mqqzone&quot;,&quot;from&quot;:&quot;html_view_toolbar&quot;}]}">QQ空间</a><a href="#" title="分享到新浪微博" class="share_lv1_btn sinaweibo bds_tsina logSend share-toggle" data-logsend="{&quot;send&quot;:[&quot;view&quot;,&quot;share&quot;,{&quot;sns&quot;:&quot;msina&quot;,&quot;from&quot;:&quot;html_view_toolbar&quot;}]}">新浪微博</a><a href="#" title="分享到微信" class="share_lv1_btn share_lv1_btn_weixin weixin logSend share-toggle" id="share_lv1_btn_weixin" data-logsend="{&quot;send&quot;:[&quot;view&quot;,&quot;share&quot;,{&quot;sns&quot;:&quot;mweixin&quot;,&quot;from&quot;:&quot;html_view_toolbar&quot;}]}">微信</a><span class="btn-close"></span><div class="weixinTips" id="weixinTips"><div class="qrcode reader-weixin-share-qrcode" id="weixinQrcode"></div><p>扫二维码，快速分享到微信朋友圈</p></div></div></div><div class="reader-tools-btn-wrap favo-wrap"><div class="reader-download reader-wangpan-box" data-toolsbar-log="download"><a title="转存到百度网盘" href="javascript:void(0);" class="reader-wangpan btn-download" alog-action="htmltoolbar.download"></a><div class="wangpan-tip" style="display: block;"><span class="icon-triangle"></span><span class="icon-wangpan"></span><span class="tip-text">文档可以转存到百度网盘啦！</span><span class="btn-close"></span></div></div></div></div><div class="center" style="width: 890px;"><div class="centerLeft"><div class="reader-tools-page xllDownloadLayerHit_left"><input type="text" class="page-input" data-toolsbar-log="jumppage"><span class="page-count">/6</span></div></div><div class="centerRight" style="right: -50px;"><div class="toolbar-core-btns-wrap super-vip"><div class="toolbar-core-btns-value-text"><div>2下载券</div></div><div class="reader-download btn-download" data-toolsbar-log="download" alog-action="htmltoolbar.download">立即下载</div>        <div class="btn-pay-vip"><div class="text-secondary">加入VIP</div><div class="text-primary">免券下载</div><div class="new-user-discount-tip"><span class="icon-triangle"></span><span class="icon-new-user"></span><span class="tip-text">VIP新客<span class="red-text">立减2元</span></span><span class="btn-close"></span></div></div></div></div></div><div class="right" style="display: none;"></div></div></div></div><div id="reader-helper-el" class="ui-panel trg-tl" style="left: -9000px; top: -9000px; z-index: 9002;"><div class="tips-wrap"><span class="trangle"></span><div class="inner"><span id="reader-link-wrap" style="display:none;"><a href="###" target="_blank" id="reader-link-button" alog-action="htmlplugin.openlink">打开链接</a><span> | </span></span><a href="###" id="reader-copy-button" alog-action="htmlplugin.copy" style="z-index: 9001;">复制</a><span> | </span><a href="###" id="reader-qrcode-button" class="log-xsend" data-logxsend="[1, 100786]">发送到手机</a><span> | </span><a href="###" id="reader-search-button" target="_blank" alog-action="htmlplugin.search" class="log-xsend" data-logxsend="[1,100161]">搜索</a><span> | </span><a href="###" id="reader-translate-button" class="log-xsend" data-logxsend="[1, 100787]" alog-action="htmlplugin.translate">翻译</a></div></div></div><div style="position: absolute; left: -8994px; top: -8989px; width: 48px; height: 32px; z-index: 9002;"><embed id="ZeroClipboardMovie_1" src="/static/wkcommon/widget/ui/reader_plugin/ZeroClipboard/ZeroClipboard.swf" loop="false" menu="false" quality="best" bgcolor="#ffffff" width="48" height="32" name="ZeroClipboardMovie_1" align="middle" allowscriptaccess="always" allowfullscreen="false" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" flashvars="id=1&amp;width=48&amp;height=32" wmode="transparent"></div><div id="reader-copy-success-tip" class="ui-panel trg-tl" tabindex="-1" style="left: -9000px; top: -9000px; z-index: 9003;"><div class="tips-wrap"><span class="trangle"></span><div class="inner"><div class="bd"><span class="tip-text"><b class="ic ic-radic"></b>文字已复制</span></div></div></div></div><div id="reader-wkvideo-card" style="display: none;"></div><script src="https://su.bdimg.com/static/dspui/js/ue.js"></script><script src="https://cpro.baidustatic.com/cpro/ui/c.js"></script></body></html>
'''

import re

pattern = ">(.+?)</p>"

all_list = re.findall(pattern=pattern, string=div)

all_list = list(map(lambda item: item.split(">")[-1], all_list))

data = ""
for i in range(len(all_list)):
    if all_list[i] == "&ensp;":
        data += "\n"
    elif all_list[i] == "&ensp;" and all_list[i + 1] == "&ensp;" and all_list[i + 2] == "&ensp;":
        data += "\n"
        i += 3
    elif all_list[i] == "如果对您有帮助！感谢评论与分享":
        data += ""
    else:
        data += all_list[i]
with open("txt.txt", "w") as file:
    file.write(data)
