## 参考：
https://www.youtube.com/watch?v=0rRwwwB-qFo

https://caq98i.top/article/?page=106

## 部署:
mkdir /www

docker run -it --net host -v /www:/home/www --name caq98i anqiqii/flask39 bash

pip install cchardet fastcache

## 修改config.py配置文件中的example.com为自己的域名：
my_host_name = 'example.com'
## 建议fork仓库，修改后再拉取。容器里面没有vi、vim、nano命令。无法编辑。

cd /home/www &&
git clone https://github.com/你的GitHub用户名/zmirror &&
cd zmirror &&
chown -R www-data . && 
chgrp -R www-data . &&



## 启动zmirror服务：
uwsgi --ini uwsgi.ini

## 如果报错：realpath() of uwsgi.ini failed: No such file or directory [core/utils.c line 3662]
## 执行：
mv uwsig.ini uwsgi.ini

## 停止或重启：
uwsgi --stop uwsgi_pid

uwsgi --reload uwsgi_pid

## caddy反向代理配置文件示例：


example.com {

    encode gzip zstd
    
    tls you@example.com   # 证书由 Caddy 自动签发/续期

    @static {
        path /static/* /media/*
    }
    handle @static {
        root * /srv/app
        file_server
    }

    handle {
        reverse_proxy 127.0.0.1:3031 {
            header_up X-Real-IP {remote_host}
            header_up X-Forwarded-For {remote_host}
            header_up X-Forwarded-Proto {scheme}
            header_up Host {host}
        }
    }

    log {
        output file /var/log/caddy/app_access.log {
            roll_size 10mb
            roll_keep 10
            roll_keep_for 720h
        }
    }
 }   




