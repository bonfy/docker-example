# Docker Examples

## 大纲

### Docker 是什么

* Git
    * Version
    * Layer
    * Docker Hub
* Ansible
    * Dockerfile
* 环境隔离
    * Namespace
    * cgroup


### Docker 解决了什么问题

* 经典问题： 自己电脑上能跑为什么到了服务器上就出错了？
    * 当然以前也能解决这个问题 比如用 VM 是可以解决的
    * Docker 能解决，而且用的资源更少

### Docker 如何使用

* Docker images 是 缓存 在你的Cache里的


### Docker 命令

```cmd
$ docker --help
$ docker info

# Image related
$ docker build
$ docker pull
$ docker images ls
$ docker rmi

# Container related
$ docker run 
$ docker ps
$ docker rm
$ docker exec 
$ docker stop
$ docker start
```


### 开发人员可以用它来干嘛

* Windows 开发Linux程序
* 方便安装 删除一些依赖的程序 - 如 Mysql 或者 Redis 之类的
* 方便做多版本测试 - 如 Python 2 与 Python 3 测试
* 是 k8s 等的基础
