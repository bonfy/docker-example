# Beta

## Intro

```cmd
$ docker version
Client: Docker Engine - Community
 Version:           19.03.12
 API version:       1.40
 Go version:        go1.13.10
 Git commit:        48a66213fe
 Built:             Mon Jun 22 15:45:50 2020    
 OS/Arch:           linux/amd64
 Experimental:      false
 ....

$ docker info
Client:
 Debug Mode: false

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 0
 Server Version: 19.03.12
 ...


# Run Docker
$ docker run -it ubuntu bash
                                                                                                        
Unable to find image 'ubuntu:latest' locally 
latest: Pulling from library/ubuntu 
a4a2a29f9ba4: Pull complete
127c9761dcba: Pull complete
d13bf203e905: Pull complete
4039240d2e0b: Pull complete
Digest: sha256:35c4a2c15539c6c1e4e5fa4e554dac323ad0107d8eb5c582d6ff386b383b7dce 
Status: Downloaded newer image for ubuntu:latest
root@f509774ab9c5:/#

# Docker container
$ docker ps 
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES 
f509774ab9c5        ubuntu              "bash"              3 minutes ago       Up 3 minutes                            quizzical_jepsen

$ docker top f509774ab9c5
docker top f509774ab9c5 
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD  
root                23375               23357               0                   05:22               pts/0               00:00:00            bash 

# PPID 是 宿主机 父进程 pid

$ ps -ef | grep 23375
root     23375 23357  0 05:22 pts/0    00:00:00 bash 
root     23464 23419  0 05:30 pts/2    00:00:00 grep 23375

# 可以在 宿主机上 运行 kill -9 pid 删除docker container
# 当然 我们有更好的方式

$ docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE 
ubuntu              latest              74435f89ab78        2 weeks ago         73.9MB


$ docker run 
# docker stop/start/restart container_id
```