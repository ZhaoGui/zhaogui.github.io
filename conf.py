# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "zhaogui/zhaogui.github.io@master"
}

# 站点设置
site_name = "北林有涧"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020-01-20T16:51+08:00"
author = "猎暄"
email = "alan.gui@foxmail.com"
author_homepage = "http://zhaogui.applinzi.com/resume"
description = "北林有涧，独寐寤歌。"
key_words = ['北林', '猎暄', '北林有涧', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "产品锦鲤",
        "url": "http://zhaogui.applinzi.com/resume",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "北林有涧",
        "url": "https://zhuanlan.zhihu.com/beilin",
        "brief": "知乎专栏"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
