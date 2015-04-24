#!/usr/bin/env python
# coding:utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_web.settings")
import django
if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()

def main():
	from blog.models import Article
	f= open('')