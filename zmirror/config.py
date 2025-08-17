# coding=utf-8
# 这是为Google和中文维基(无缝整合)镜像配置的示例配置文件
#
# 使用方法:
#   1. 复制本文件到 zmirror 根目录(wsgi.py所在目录), 并重命名为 config.py
#   2. 修改 my_host_name 为你自己的域名
#
# 各项设置选项的详细介绍请看 config_default.py 中对应的部分
# 本配置文件假定你的服务器本身在墙外
# 如果服务器本身在墙内(或者在本地环境下测试, 请修改`Proxy Settings`中的设置
#
# 由于google搜索结果经常会出现中文维基, 所以顺便把它也加入了.
# google跟中文维基之间使用了本程序的镜像隔离功能, 可以保证中文维基站的正常使用
#
# 本配置文件试图还原出一个功能完整的google.
#   但是由于程序本身所限, 还是不能[完整]镜像过来整个[google站群]
#   在后续版本会不断增加可用的网站
#
# 以下google服务完全可用:
#   google网页搜索/学术/图片/新闻/图书/视频(搜索)/财经/APP搜索/翻译/网页快照/...
#   google搜索与中文维基百科无缝结合
# 以下服务部分可用:
#     gg地图(地图可看, 左边栏显示不正常)/G+(不能登录)
# 以下服务暂不可用(因为目前无法解决登录的问题):
#     所有需要登录的东西, docs之类的
#

# Github: https://github.com/aploium/zmirror

# ############## Local Domain Settings ##############
my_host_name = 'my.ynsc.com'
my_host_scheme = 'https://'
my_host_port = None  # None表示使用默认端口, 可以设置成非标准端口, 比如 81

# ############## Target Domain Settings ##############
target_domain = 'www.google.com.hk'
target_scheme = 'https://'
verbose_level = 2
# 这里面大部分域名都是通过 `enable_automatic_domains_whitelist` 自动采集的, 我只是把它们复制黏贴到了这里
# 实际镜像一个新的站时, 手动只需要添加很少的几个域名就可以了.
# 自动采集(如果开启的话)会不断告诉你新域名
external_domains = (
    'www.google.com',
    'webcache.googleusercontent.com',  # Google网页快照
    'images.google.com.hk',
    'images.google.com',
    'apis.google.com',

    # Google学术
    'scholar.google.com.hk',
    'scholar.google.com',

    # 中文维基百科
    'zh.wikipedia.org',
    'zh.m.wikipedia.org',
    'upload.wikipedia.org',
    'meta.wikimedia.org',
    'login.wikimedia.org',
   'en.wikipedia.org',
   'upload.wikimedia.org',
  
    # Google静态资源域名
    'ssl.gstatic.com',
    'www.gstatic.com',
    'encrypted-tbn0.gstatic.com',
    'encrypted-tbn1.gstatic.com',
    'encrypted-tbn2.gstatic.com',
    'encrypted-tbn3.gstatic.com',
    'csi.gstatic.com',
    'fonts.googleapis.com',

    # Google登陆支持
    'accounts.google.com',
    'accounts.youtube.com',
    'accounts.google.com.hk',
    'myaccount.google.com',
    'myaccount.google.com.hk',

    'ajax.googleapis.com',
    'translate.google.com',
    'translate.google.com.hk',
    'video.google.com.hk',
    'books.google.com',
    'cloud.google.com',
    'analytics.google.com',
    'security.google.com',
    'investor.google.com',
    'families.google.com',
    'clients1.google.com',
    'clients2.google.com',
    'clients3.google.com',
    'clients4.google.com',
    'clients5.google.com',
    'talkgadget.google.com',
    'news.google.com.hk',
    'news.google.com',
    'support.google.com',
    'docs.google.com',
    'books.google.com.hk',
    'chrome.google.com',
    'profiles.google.com',
    'feedburner.google.com',
    'cse.google.com',
    'sites.google.com',
    'productforums.google.com',
    'encrypted.google.com',
    'm.google.com',
    'research.google.com',
    'maps.google.com.hk',
    'hangouts.google.com',
    'developers.google.com',
    'get.google.com',
    'afp.google.com',
    'groups.google.com',
    'payments.google.com',
    'photos.google.com',
    'play.google.com',
    'mail.google.com',
    'code.google.com',
    'tools.google.com',
    'drive.google.com',
    'script.google.com',
    'goto.google.com',
    'calendar.google.com',
    'wallet.google.com',
    'privacy.google.com',
    'ipv4.google.com',
    'video.google.com',
    'store.google.com',
    'fi.google.com',
    'apps.google.com',
    'events.google.com',
    'notifications.google.com',
    'plus.google.com',
    'dl.google.com',
    'manifest.googlevideo.com',
    'storage.googleapis.com',

    'gg.google.com',

    'scholar.googleusercontent.com',
    'translate.googleusercontent.com',
    't0.gstatic.com',
    't1.gstatic.com',
    't2.gstatic.com',
    't3.gstatic.com',
    's-v6exp1-ds.metric.gstatic.com',
    'ci4.googleusercontent.com',
    'gp3.googleusercontent.com',
    'accounts.gstatic.com',

    # For Google Map (optional)
    'maps-api-ssl.google.com',
    'maps.gstatic.com',
    'maps.google.com',
    'fonts.gstatic.com',
    'lh1.googleusercontent.com',
    'lh2.googleusercontent.com',
    'lh3.googleusercontent.com',
    'lh4.googleusercontent.com',
    'lh5.googleusercontent.com',
    'lh6.googleusercontent.com',

    # 'upload.wikimedia.org',
    'id.google.com.hk',
    'id.google.com',

    # misc
    'inputtools.google.com',
    'inbox.google.com',
    '-v6exp3-v4.metric.gstatic.com',
    '-v6exp3-ds.metric.gstatic.com',
    'if-v6exp3-v4.metric.gstatic.com',
    'public.talk.google.com',
    'ie.talkgadget.google.com',
    'client-channel.google.com',
    'maps.googleapis.com',
    'people-pa.clients6.google.com',
    'myphonenumbers-pa.googleapis.com',
    'clients6.google.com',
    'staging.talkgadget.google.com',
    'preprod.hangouts.sandbox.google.com',
    'dev-hangoutssearch-pa-googleapis.sandbox.google.com',
    'picasaweb.google.com',
    'schemas.google.com',
    'contact.talk.google.com',
    'groupchat.google.com',
    'friendconnectchat.google.com',
    'muvc.google.com',
    'bot.talk.google.com',
    'prom.corp.google.com',
    'stun.l.google.com',
    'stun1.l.google.com',
    'stun2.l.google.com',
    'stun3.l.google.com',
    'stun4.l.google.com',
    'onetoday.google.com',
    'plus.googleapis.com',
    'youtube.googleapis.com',
    'picasa.google.com',
    "www-onepick-opensocial.googleusercontent.com",

    'plus.sandbox.google.com',

    # gmail misc
    'gmail.com',
    'www.gmail.com',
    'chatenabled.mail.google.com',
    'filetransferenabled.mail.google.com',
    'gmail.google.com',
    'googlemail.l.google.com',
    'isolated.mail.google.com',
    'm.gmail.com',
    'm.googlemail.com',
    'mail-settings.google.com',
    'm.android.com',
  # youtube
    'm.youtube.com',

    's.youtube.com',
    'accounts.youtube.com',

    'apis.google.com',
    'plus.google.com',
    'accounts.google.com',
    'content.google.com',
    'apis.google.com',
    'ajax.googleapis.com',
    'www.googletagservices.com',
    'partner.googleadservices.com',
    'tpc.googlesyndication.com',
    'pagead2.googlesyndication.com',
    'video.google.com',
    'fonts.googleapis.com',
    'maps.googleapis.com',
    'maps.google.com',
    'maps-api-ssl.google.com',
    'support.google.com',
    'csi.gstatic.com',

    'redirector.googlevideo.com',
    'gg.google.com',

    'clients1.google.com',
    'clients6.google.com',
    'www.googleapis.com',
    'www.google.com',
    'www.gstatic.com',
    'www.youtube-nocookie.com',
    's.ytimg.com',
    'i.ytimg.com',
    'i1.ytimg.com',
    'encrypted.google.com',
    'fonts.gstatic.com',
    'ssl.gstatic.com',
    'yt3.ggpht.com',
    'fonts.googleapis.com',

    'youtu.be',

    'daily-0.consent.corp.youtube.com',
    'daily-1.consent.corp.youtube.com',
    'daily-2.consent.corp.youtube.com',
    'daily-3.consent.corp.youtube.com',
    'daily-4.consent.corp.youtube.com',
    'daily-5.consent.corp.youtube.com',
    'daily-6.consent.corp.youtube.com',

    'consent-daily-0.sandbox.youtube.com',
    'consent-daily-1.sandbox.youtube.com',
    'consent-daily-2.sandbox.youtube.com',
    'consent-daily-3.sandbox.youtube.com',
    'consent-daily-4.sandbox.youtube.com',
    'consent-daily-5.sandbox.youtube.com',
    'consent-daily-6.sandbox.youtube.com',
    'consent-autopush.sandbox.youtube.com',
    'www.corp.google.com',
    'spreadsheets.google.com',
    'ytlegos-dashboard.corp.google.com',

    #facebook
    "facebook.com",
    "m.facebook.com",
    "mqtt.facebook.com",
    "s-static.ak.facebook.com",
    "profile.ak.facebook.com",
    "static.ak.facebook.com",
    "b.static.ak.facebook.com",
    "graph.facebook.com",
    "ssl.facebook.com",
    "staticxx.facebook.com",
    "api.facebook.com",
    "secure-profile.facebook.com",
    "secure.facebook.com",
    "zh-cn.facebook.com",
    "login.facebook.com",
    "message-facebook.com",
    "attachments.facebook.com",
    "touch.facebook.com",
    "apps.facebook.com",
    "upload.facebook.com",
    "developers.facebook.com",
    "act.channel.facebook.com",
    "0-act.channel.facebook.com",
    "1-act.channel.facebook.com",
    "2-act.channel.facebook.com",
    "3-act.channel.facebook.com",
    "4-act.channel.facebook.com",
    "5-act.channel.facebook.com",
    "6-act.channel.facebook.com",
    "inyour-slb-01-05-ash3.facebook.com",
    "origincache-starfacebook-ai-01-05-ash3.facebook.com",
    "beta-chat-01-05-ash3.facebook.com",
    "channel-ecmp-05-ash3.facebook.com",
    "channel-staging-ecmp-05-ash3.facebook.com",
    "channel-testing-ecmp-05-ash3.facebook.com",
    "0-edge-chat.facebook.com",
    "1-edge-chat.facebook.com",
    "2-edge-chat.facebook.com",
    "3-edge-chat.facebook.com",
    "4-edge-chat.facebook.com",
    "5-edge-chat.facebook.com",
    "6-edge-chat.facebook.com",
    "api-read.facebook.com",
    "bigzipfiles.facebook.com",
    "check4.facebook.com",
    "check6.facebook.com",
    "code.facebook.com",
    "connect.facebook.com",
    "edge-chat.facebook.com",
    "pixel.facebook.com",
    "star.c10r.facebook.com",
    "star.facebook.com",
    "zh-tw.facebook.com",
    "b-api.facebook.com",
    "b-graph.facebook.com",
    "orcart.facebook.com",
    "s-static.facebook.com",
    "vupload.facebook.com",
    "vupload2.vvv.facebook.com",
    "d.facebook.com",
    "fbexternal-a.akamaihd.net",
    "fbcdn-creative-a.akamaihd.net",
    "fbcdn-video-a-a.akamaihd.net",
    "fbcdn-video-b-a.akamaihd.net",
    "fbcdn-video-c-a.akamaihd.net",
    "fbcdn-video-d-a.akamaihd.net",
    "fbcdn-video-e-a.akamaihd.net",
    "fbcdn-video-f-a.akamaihd.net",
    "fbcdn-video-g-a.akamaihd.net",
    "fbcdn-video-h-a.akamaihd.net",
    "fbcdn-video-i-a.akamaihd.net",
    "fbcdn-video-j-a.akamaihd.net",
    "fbcdn-video-k-a.akamaihd.net",
    "fbcdn-video-l-a.akamaihd.net",
    "fbcdn-video-m-a.akamaihd.net",
    "fbcdn-video-n-a.akamaihd.net",
    "fbcdn-video-o-a.akamaihd.net",
    "fbcdn-video-p-a.akamaihd.net",
    "fbcdn-vthumb-a.akamaihd.net",
    "fbcdn-sphotos-a-a.akamaihd.net",
    "fbcdn-sphotos-b-a.akamaihd.net",
    "fbcdn-sphotos-c-a.akamaihd.net",
    "fbcdn-sphotos-d-a.akamaihd.net",
    "fbcdn-sphotos-e-a.akamaihd.net",
    "fbcdn-sphotos-f-a.akamaihd.net",
    "fbcdn-sphotos-g-a.akamaihd.net",
    "fbcdn-sphotos-h-a.akamaihd.net",
    "fbcdn-profile-a.akamaihd.net",
    "fbcdn-photos-a.akamaihd.net",
    "fbcdn-photos-e-a.akamaihd.net",
    "fbcdn-sphotos-a.akamaihd.net",
    "fbstatic-a.akamaihd.net",
    "fbcdn.net",

    "video.xx.fbcdn.net",
    "video.xx.fbcdn.net",
    "scontent.xx.fbcdn.net",
    "external.xx.fbcdn.net",

    "scontent-a.xx.fbcdn.net",
    "scontent-b.xx.fbcdn.net",
    "scontent-c.xx.fbcdn.net",
    "scontent-d.xx.fbcdn.net",
    "scontent-e.xx.fbcdn.net",
    "scontent-mxp.xx.fbcdn.net",
    "scontent-a-lax.xx.fbcdn.net",
    "scontent-a-sin.xx.fbcdn.net",
    "scontent-b-lax.xx.fbcdn.net",
    "scontent-b-sin.xx.fbcdn.net",
    "vthumb.ak.fbcdn.net",
    "photos-a.ak.fbcdn.net",
    "photos-b.ak.fbcdn.net",
    "photos-c.ak.fbcdn.net",
    "photos-d.ak.fbcdn.net",
    "photos-e.ak.fbcdn.net",
    "photos-f.ak.fbcdn.net",
    "photos-g.ak.fbcdn.net",
    "photos-h.ak.fbcdn.net",
    "creative.ak.fbcdn.net",
    "external.ak.fbcdn.net",
    "b.static.ak.fbcdn.net",
    "static.ak.fbcdn.net",
    "origincache-ai-01-05-ash3.fbcdn.net",
    "profile.ak.fbcdn.net",
    "vpn.tfbnw.net",
    "ent-a.xx.fbcdn.net",
    "ent-b.xx.fbcdn.net",
    "ent-c.xx.fbcdn.net",
    "ent-d.xx.fbcdn.net",
    "ent-e.xx.fbcdn.net",
    "s-external.ak.fbcdn.net",
    "s-static.ak.fbcdn.net",
    "static.thefacebook.com",
    "ldap.thefacebook.com",
    "attachment.fbsbx.com",
    "connect.facebook.net",
    "live.fb.com",
    "work.fb.com",
    "techprep.fb.com",
    "nonprofits.fb.com",
    "managingbias.fb.com",
    "rightsmanager.fb.com",
    "instantarticles.fb.com",
    "messengerplatform.fb.com",
    "threatexchange.fb.com",

    "cx.atdmt.com",

    "fb-s-d-a.akamaihd.net",
    "fbcdn-photos-a-a.akamaihd.net",
    "fbcdn-photos-c-a.akamaihd.net",
    "fbcdn-photos-d-a.akamaihd.net",
    "fbcdn-photos-b-a.akamaihd.net",
    "fb-s-c-a.akamaihd.net",

    "ar-ar.facebook.com",
    "bg-bg.facebook.com",
    "bs-ba.facebook.com",
    "ca-es.facebook.com",
    "da-dk.facebook.com",
    "el-gr.facebook.com",
    "es-la.facebook.com",
    "es-es.facebook.com",
    "fa-ir.facebook.com",
    "fi-fi.facebook.com",
    "fr-fr.facebook.com",
    "fr-ca.facebook.com",
    "hi-in.facebook.com",
    "hr-hr.facebook.com",
    "id-id.facebook.com",
    "it-it.facebook.com",
    "ko-kr.facebook.com",
    "mk-mk.facebook.com",
    "ms-my.facebook.com",
    "pl-pl.facebook.com",
    "pt-br.facebook.com",
    "pt-pt.facebook.com",
    "ro-ro.facebook.com",
    "sl-si.facebook.com",
    "sr-rs.facebook.com",
    "th-th.facebook.com",
    "vi-vn.facebook.com",
    "error.facebook.com",
    "ja-jp.facebook.com",
    "de-de.facebook.com",
    "l.facebook.com",
    "static.xx.fbcdn.net",
    "scontent-lax3-1.xx.fbcdn.net",
    "external-lax3-1.xx.fbcdn.net",
    "video-lax3-1.xx.fbcdn.net",

    #insagram
    'instagramstatic-a.akamaihd.net',
    'scontent.cdninstagram.com',
    'help.instagram.com',
    'blog.instagram.com',
    'api.instagram.com',

    'www.facebook.com',
    'connect.facebook.net',
    'static.xx.fbcdn.net',
    'pixel.facebook.com',
    'facebook.com',
    'scontent.xx.fbcdn.net',
    '3-edge-chat.facebook.com',
    'm.facebook.com',
    'fbcdn-photos-a-a.akamaihd.net',
    'api.facebook.com',
    'api-read.facebook.com',
    'l.facebook.com',
    'zh-cn.facebook.com',
    'upload.facebook.com',
    'vupload2.facebook.com',
    'vupload-edge.facebook.com',
    'staticxx.facebook.com',
    'external.xx.fbcdn.net',

    'fonts.googleapis.com',

    'scontent-lax3-1.cdninstagram.com',
    'l.instagram.com',
    'scontent-sjc2-1.cdninstagram.com',

    #twitter pc
   'mobile.twitter.com',

    't.co',
    'dev.twitter.com',
    'ads.twitter.com',
    'analytics.twitter.com',
    'pic.twitter.com',
    'api.twitter.com',
    'platform.twitter.com',
    'upload.twitter.com',
    'ton.twitter.com',
    'support.twitter.com',
    'about.twitter.com',
    'tweetdeck-devel.atla.twitter.com',
    'tweetdeck-devel.smf1.twitter.com',
    'tdapi-staging.smf1.twitter.com',
    'tweetdeck.localhost.twitter.com',
    'tweetdeck.twitter.com',
    'tdapi-staging.atla.twitter.com',
    'localhost.twitter.com',
    'donate.twitter.com',
    'syndication.twitter.com',
    'status.twitter.com',
    'engineering.twitter.com',
    'help.twitter.com',
    'blog.twitter.com',
    'business.twitter.com',
    'cards-dev.twitter.com',

    'caps.twitter.com',
    'quickread.twitter.com',
    'tailfeather.twimg.com',
    'publish.twitter.com',
    'brand.twitter.com',
    't.lv.twimg.com',
    'media.twitter.com',

    'g2.twimg.com',
    'hca.twimg.com',
    'g.twimg.com',
    'video.twimg.com',
    'ma.twimg.com',
    'abs.twimg.com',
    'pbs.twimg.com',
    'ton.twimg.com',
    'ma-0.twimg.com',
    'ma-1.twimg.com',
    'ma-2.twimg.com',
    'o.twimg.com',
    'abs-0.twimg.com',
    'abs-1.twimg.com',
    'abs-2.twimg.com',
    'amp.twimg.com',

    'www.google.com',
    'ssl.gstatic.com',
    'www.gstatic.com',
    'apis.google.com',
    'encrypted-tbn0.gstatic.com',
    'encrypted-tbn1.gstatic.com',
    'encrypted-tbn2.gstatic.com',
    'encrypted-tbn3.gstatic.com',
    'accounts.google.com',
    'accounts.youtube.com',
    'fonts.googleapis.com',

    #twitter m
    'twitter.com',

    't.co',
    'dev.twitter.com',
    'ads.twitter.com',
    'analytics.twitter.com',
    'pic.twitter.com',
    'api.twitter.com',
    'platform.twitter.com',
    'upload.twitter.com',
    'ton.twitter.com',
    'support.twitter.com',
    'about.twitter.com',
    'tweetdeck-devel.atla.twitter.com',
    'tweetdeck-devel.smf1.twitter.com',
    'tdapi-staging.smf1.twitter.com',
    'tweetdeck.localhost.twitter.com',
    'tweetdeck.twitter.com',
    'tdapi-staging.atla.twitter.com',
    'localhost.twitter.com',
    'donate.twitter.com',
    'syndication.twitter.com',
    'status.twitter.com',
    'engineering.twitter.com',
    'help.twitter.com',
    'blog.twitter.com',
    'business.twitter.com',
    'cards-dev.twitter.com',

    'caps.twitter.com',
    'quickread.twitter.com',
    'tailfeather.twimg.com',
    'publish.twitter.com',
    'brand.twitter.com',
    't.lv.twimg.com',
    'media.twitter.com',

    'g2.twimg.com',
    'hca.twimg.com',
    'g.twimg.com',
    'video.twimg.com',
    'ma.twimg.com',
    'abs.twimg.com',
    'pbs.twimg.com',
    'ton.twimg.com',
    'ma-0.twimg.com',
    'ma-1.twimg.com',
    'ma-2.twimg.com',
    'o.twimg.com',
    'abs-0.twimg.com',
    'abs-1.twimg.com',
    'abs-2.twimg.com',
    'amp.twimg.com',

    'www.google.com',
    'apis.google.com',
    'accounts.google.com',
    'accounts.youtube.com',
    'fonts.googleapis.com',
    'ssl.gstatic.com',
    'www.gstatic.com',
    'encrypted-tbn0.gstatic.com',
    'encrypted-tbn1.gstatic.com',
    'encrypted-tbn2.gstatic.com',
    'encrypted-tbn3.gstatic.com',
    'x.com',
)

# 强制所有Google站点使用HTTPS
force_https_domains = 'ALL'

# 自动动态添加域名
enable_automatic_domains_whitelist = True
domains_whitelist_auto_add_glob_list = (
    '*.google.com', '*.gstatic.com', '*.google.com.hk', '*.googleapis.com', "*.googleusercontent.com",)

# ############## Proxy Settings ##############
# 如果你在墙内使用本配置文件, 请指定一个墙外的http代理
is_use_proxy = False
# 代理的格式及SOCKS代理, 请看 http://docs.python-requests.org/en/latest/user/advanced/#proxies
requests_proxies = dict(
    http='http://127.0.0.1:8123',
    https='https://127.0.0.1:8123',
)

# ############## Sites Isolation ##############
enable_individual_sites_isolation = True

# 镜像隔离, 用于支持Google和维基共存
isolated_domains = {'zh.wikipedia.org', 'zh.m.wikipedia.org'}

# ############## URL Custom Redirect ##############
url_custom_redirect_enable = True
url_custom_redirect_list = {
    # 这是一个方便的设置, 如果你访问 /wiki ,程序会自动重定向到后面这个长长的wiki首页
    '/wiki': '/extdomains/https-zh.wikipedia.org/',
    # 这是gmail
    '/gmail': '/extdomains/mail.google.com/mail/u/0/h/girbaeneuj90/',
}

# ############# Additional Functions #############
# 移除google搜索结果页面的url跳转
#   原理是往页面中插入一下面这段js
# js来自: http://userscripts-mirror.org/scripts/review/117942
custom_inject_content = {
    "head_first": [
        {
            "content": r"""<script>
function checksearch(){
   var list = document.getElementById('ires');
   if(list){
       document.removeEventListener('DOMNodeInserted',checksearch,false);
       document.addEventListener('DOMNodeInserted',clear,false)
   }
};

function clear(){
   var i; var items = document.querySelectorAll('a[onmousedown]');
   for(i =0;i<items.length;i++){
       items[i].removeAttribute('onmousedown');
   }
};
document.addEventListener('DOMNodeInserted',checksearch,false)
</script>""",
            "url_regex": r"^www\.google(?:\.[a-z]{2,3}){1,2}",
        },
    ]
}
