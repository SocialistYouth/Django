# 云端部署WebRTC
1. 创建django项目 -> django-admin startproject WebRTC
2. 修改allowed Host(在/WebRTC/WebRTC/settings.py文件下)
3. 添加app --> python3 manage.py startapp instantVideo
4. 进入admin页面前，更新数据库 --> python3 manage.py migrate
5. 创建管理员账号 --> python3 manage.py createsuperuser
6. 修改时区 --> settings.py文件下TIME_ZONE = 'Asia/Shanghai'
7. 手动将创建的app加入到settings.py配置文件中
> - 在INSTALLED_APPS中添加'instantVideo.apps.InstantvideoConfig',
8. 设置整个项目的静态文件的地址
> - import os
> - STATIC_ROOT = os.path.join(BASE_DIR, 'static')

