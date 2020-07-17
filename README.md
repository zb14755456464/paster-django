# 通过 gunicorn django-paster-settings 部署django
# 项目打包安装
cd paster-django
python3 setup.py install
# 校验启动命令是否正确
deploy -h 
# 启动项目
gunicorn --paster etc/config.ini

# 测试访问
curl localhost:8000/index/
