## 1 概述

NGINX Ingress Controller 是使用 Kubernetes Ingress 资源对象构建的，用 ConfigMap 来存储 Nginx 配置的一种 Ingress Controller 实现。

安装 ingress-nginx 有多种方式，本文使用 helm3.6 方式进行安装。

其他安装方式可以参考文档：[https://kubernetes.github.io/ingress-nginx/deploy/](https://kubernetes.github.io/ingress-nginx/deploy/)

本文 k8s 集群环境是在 centos7 系统上由 kubeadm 搭建的单 master 集群：

```bash
[root@k8s-master ~]# kubectl get nodes -o wide
NAME      STATUS   ROLES    AGE   VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE                KERNEL-VERSION           CONTAINER-RUNTIME
master1   Ready    master   36d   v1.19.3   192.168.5.60   <none>        CentOS Linux 7 (Core)   3.10.0-1160.el7.x86_64   docker://19.3.11
node1     Ready    <none>   36d   v1.19.3   192.168.5.61   <none>        CentOS Linux 7 (Core)   3.10.0-1160.el7.x86_64   docker://19.3.11
node2     Ready    <none>   36d   v1.19.3   192.168.5.62   <none>        CentOS Linux 7 (Core)   3.10.0-1160.el7.x86_64   docker://19.3.11

```

## 2 helm介绍

Helm 是一个用于对需要在 k8s 上部署的复杂应用进行定义、安装和更新。Helm 以 Char 的方式对应用软件进行描述，可以方便地创建、版本化、共享和发布复杂的应用软件。

* 官方英文文档：[https://helm.sh/docs/](https://helm.sh/docs/)
* 官方中文文档：[https://helm.sh/zh/docs/](https://helm.sh/zh/docs/)

### 2.1 helm的主要概念

* **Chart**

Helm的应用包，采用tgz格式。类似于 Yum 的 RPM 包，其包含了一组定义 Kubernetes 资源相关的 YAML 文件，也称为应用 Chart。

* **Repoistory**

Helm 的应用仓库，Repository 本质上是一个 Web 服务器，该服务器保存了一系列的 Chart 应用包以供用户下载，并且提供了一个该 Repository 的 Chart 包的清单文件以供查询，Helm可以同时管理多个不同的Repository。

Helm社区官方提供了stable和incubator仓库，但Helm社区没有打算独占仓库，而是允许其他人和组织也可以搭建仓库。仓库可以是公共仓库，也可以是私有仓库。

* **Release**

在 Kubernetes 集群上运行的 Chart 的一个实例。在同一个集群上，一个 Chart 可以安装很多次。每次安装都会创建一个新的 Release。例如一个 MySQL Chart，如果想在服务器上运行两个 MySQL 数据库，就可以把这个 Chart 安装两次。每次安装都会生成一个新的Release。

### 2.2 helm安装

Helm安装官方文档：[https://helm.sh/docs/intro/install/](https://helm.sh/docs/intro/install/)

这里安装 helm v3 版本，直接从 github 下载源码包：

```bash

# 下载
[root@k8s-master ~]# wget https://get.helm.sh/helm-v3.6.0-linux-amd64.tar.gz

# 解压
[root@k8s-master ~]# tar -zxvf helm-v3.6.0-linux-amd64.tar.gz

# 移动到环境变量目录里面即可
[root@k8s-master ~]# mv linux-amd64/helm /usr/local/bin/helm

# 输出版本
[root@k8s-master ~]# helm version
version.BuildInfo{Version:"v3.6.3", GitCommit:"d506314abfb5d21419df8c7e7e68012379db2354", GitTreeState:"clean", GoVersion:"go1.16.5"}


```

### 2.3 chart包的目录结构

```bash

# 创建一个chart，chart的名称叫 helm-test
[root@k8s-master ~]# helm create helm-test
Creating helm-test
[root@k8s-master ~]# cd helm-test/

# 查看 chart 的目录结构
[root@k8s-master helm-test]# tree .
.
├── charts      
├── Chart.yaml   
├── templates
│   ├── deployment.yaml
│   ├── _helpers.tpl
│   ├── hpa.yaml
│   ├── ingress.yaml
│   ├── NOTES.txt
│   ├── serviceaccount.yaml
│   ├── service.yaml
│   └── tests
│       └── test-connection.yaml
└── values.yaml     

3 directories, 10 files
[root@k8s-master helm-test]# 


```

chart 是 Helm 的应用打包格式。chart 由一系列文件组成，这些文件描述了 Kubernetes 部署应用时所需要的资源。上面通过 helm 命令创建了一个 chart 包，目录结构说明如下：

* `helm-test`：是 chart 包的名称
* `charts` 目录： 保存依赖文件的目录，如果依赖其他的 chart，则会保存在这里
* `Chart.yaml` 文件：用于描述 chart 信息的 yaml 文件，如版本信息等
* `values.yaml` 文件：chart 支持在安装的时根据参数进行定制化配置，而 values.yaml 则提供了这些配置参数的默认值，可以在安装前根据需要修改 values.yaml 的参数
* `templates` 目录：各类 Kubernetes 资源的配置模板都放置在这里。Helm 会将 values.yaml 中的参数值注入到模板中生成标准的 YAML 配置文件

## 3 helm 安装 ingress-nginx

### 3.1 添加 ingress-nginx 官方helm仓库

```bash

[root@k8s-master ~]# helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
[root@k8s-master ~]# helm repo update


```

执行这一步的时候，我报错了：

```bash

[root@k8s-master ~]# helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
Error: looks like "https://kubernetes.github.io/ingress-nginx" is not a valid chart repository or cannot be reached: Get "https://kubernetes.github.io/ingress-nginx/index.yaml": dial tcp [::1]:443: connect: connection refused

```

可以看到是无法访问到 `https://kubernetes.github.io` ，估计是被墙了。ping 一下域名发现解析到了 127.0.0.1：

```bash

[root@k8s-master ~]# ping kubernetes.github.io
PING kubernetes.github.io (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.084 ms
64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.055 ms
64 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.068 ms
^C
--- kubernetes.github.io ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2000ms
rtt min/avg/max/mdev = 0.055/0.069/0.084/0.011 ms


```

本地检查没有配置 hosts 信息，所以这应该是 DNS 解析的问题，尝试更换 DNS 服务器，`114.114.144.144` 或者 `8.8.8.8` 都是一样不能访问。于是找到站长之家，获取一下 kubernetes.github.io 域名的 IP 地址：

[![](https://img2020.cnblogs.com/blog/1686603/202109/1686603-20210915105349430-1018597888.png)](https://img2020.cnblogs.com/blog/1686603/202109/1686603-20210915105349430-1018597888.png)

获取到 IP 地址后，选择一个IP地址，配置本地hosts解析：

```bash
[root@k8s-master ~]# echo "185.199.108.153 kubernetes.github.io" >> /etc/hosts

```

然后重新添加仓库，可以看到已添加成功。

```bash
# 添加仓库
[root@k8s-master ~]# helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
"ingress-nginx" has been added to your repositories

# 更新
[root@k8s-master ~]# helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "ingress-nginx" chart repository
Update Complete. ⎈Happy Helming!⎈

```

### 3.2 下载ingress-nginx的chart包

```bash

[root@k8s-master ~]# cd /usr/local/src/

# 查找ingress-nginx的chart包
[root@k8s-master src]# helm search repo ingress-nginx
NAME                            CHART VERSION   APP VERSION     DESCRIPTION                                       
ingress-nginx/ingress-nginx     4.0.1           1.0.0           Ingress controller for Kubernetes using NGINX a...

# 下载下来
[root@k8s-master src]# helm pull ingress-nginx/ingress-nginx

# 以tgz为后缀的包就是我们下载的chart包
[root@k8s-master src]# ls
helm-v3.6.3-linux-amd64.tar.gz  ingress-nginx-4.0.1.tgz  linux-amd64

# 解压
[root@k8s-master src]# tar -zxvf ingress-nginx-4.0.1.tgz 

# 目录结构如下
[root@k8s-master src]# cd ingress-nginx
[root@k8s-master ingress-nginx]# ls
CHANGELOG.md  Chart.yaml  ci  OWNERS  README.md  templates  values.yaml


```


### 3.3 修改 values.yaml 文件

下载下来的 chart 包，需要修改一下资源清单配置文件，修改 values.yaml 文件如下：

修改 ingress-nginx-contorller 的镜像仓库地址，默认是 k8s.gcr.io 国内无法访问，这里用到github上一个同步 ingress-nginx-contorller 的仓库 `docker.io/willdockerhub/ingress-nginx-controller`

[![](https://img2020.cnblogs.com/blog/1686603/202109/1686603-20210915105408981-283529024.png)](https://img2020.cnblogs.com/blog/1686603/202109/1686603-20210915105408981-283529024.png)

修改 hostNetwork 的值为 `true`：

[![](https://img2020.cnblogs.com/blog/1686603/202109/1686603-20210915105422987-1841567589.png)](https://img2020.cnblogs.com/blog/1686603/202109/1686603-20210915105422987-1841567589.png)

dnsPolicy的值改为: `ClusterFirstWithHostNet`

[![](https://img2020.cnblogs.com/blog/1686603/202109/1686603-20210915105432192-1794375509.png)](https://img2020.cnblogs.com/blog/1686603/202109/1686603-20210915105432192-1794375509.png)

nodeSelector 添加标签: `ingress: "true"`，用于部署 ingress-controller 到指定节点

[![](https://img2020.cnblogs.com/blog/1686603/202109/1686603-20210915105441457-530052337.png)](https://img2020.cnblogs.com/blog/1686603/202109/1686603-20210915105441457-530052337.png)

kind类型更改为：`DaemonSet`

[![](https://img2020.cnblogs.com/blog/1686603/202109/1686603-20210915105450288-959835711.png)](https://img2020.cnblogs.com/blog/1686603/202109/1686603-20210915105450288-959835711.png)

kube-webhook-certgen的镜像地址改为国内仓库地址 `registry.aliyuncs.com/google_containers/kube-webhook-certgen`

[![](https://img2020.cnblogs.com/blog/1686603/202109/1686603-20210915105458108-2086546893.png)](https://img2020.cnblogs.com/blog/1686603/202109/1686603-20210915105458108-2086546893.png)

### 3.4 执行安装

资源清单文件修改完成后，执行helm安装：

```bash

# 先创建一个名称空间
[root@k8s-master ~]# kubectl create ns ingress-nginx
namespace/ingress-nginx created

# 进入chart目录
[root@k8s-master ~]# cd /usr/local/src/ingress-nginx

# helm安装
[root@k8s-master ingress-nginx]# helm install ingress-nginx -n ingress-nginx .
NAME: ingress-nginx
LAST DEPLOYED: Wed Sep 15 10:17:09 2021
NAMESPACE: ingress-nginx
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
The ingress-nginx controller has been installed.
It may take a few minutes for the LoadBalancer IP to be available.
You can watch the status by running 'kubectl --namespace ingress-nginx get services -o wide -w ingress-nginx-controller'

An example Ingress that makes use of the controller:

  apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    annotations:
      kubernetes.io/ingress.class: 
    name: example
    namespace: foo
  spec:
    rules:
      - host: www.example.com
        http:
          paths:
            - backend:
                serviceName: exampleService
                servicePort: 80
              path: /
    # This section is only required if TLS is to be enabled for the Ingress
    tls:
        - hosts:
            - www.example.com
          secretName: example-tls

If TLS is enabled for the Ingress, a Secret containing the certificate and key must also be provided:

  apiVersion: v1
  kind: Secret
  metadata:
    name: example-tls
    namespace: foo
  data:
    tls.crt: <base64 encoded cert>
    tls.key: <base64 encoded key>
  type: kubernetes.io/tls
[root@k8s-master ingress-nginx]# 


```

出现上面的命令输出表示安装完成了，安装完成后，需要给节点打上刚刚设置的标签 `ingress=true`，让 Pod 调度到指定的节点，比如调度到 master 节点：

```bash

# 给master节点打上标签 ingress=ture
[root@k8s-master ingress-nginx]# kubectl label node master1 ingress=true
node/master1 labeled

# k8s默认集群中，出于安全考虑，默认配置下Kubernetes不会将Pod调度到Master节点。测试环境无所谓，所以执行下面命令去除master的污点：
[root@k8s-master ingress-nginx]# kubectl taint node master1 node-role.kubernetes.io/master-


```
执行完成之后，就可以看到 ingress-nginx 部署到了master节点了：

```bash

[root@k8s-master ~]# kubectl get all -n ingress-nginx
NAME                                 READY   STATUS    RESTARTS   AGE
pod/ingress-nginx-controller-nldt4   1/1     Running   0          3m45s

NAME                                         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
service/ingress-nginx-controller             LoadBalancer   10.103.248.36   <pending>     80:30318/TCP,443:30865/TCP   3m45s
service/ingress-nginx-controller-admission   ClusterIP      10.104.51.205   <none>        443/TCP                      3m46s

NAME                                      DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR                         AGE
daemonset.apps/ingress-nginx-controller   1         1         1       1            1           ingress=true,kubernetes.io/os=linux   3m45s


```

Pod也是部署在了master节点：

```bash

[root@k8s-master ~]# kubectl get pods -n ingress-nginx -o wide
NAME                             READY   STATUS    RESTARTS   AGE     IP             NODE      NOMINATED NODE   READINESS GATES
ingress-nginx-controller-nldt4   1/1     Running   0          4m12s   192.168.5.60   master1   <none>           <none>



```
### 3.5 测试 ingress-nginx

创建后端的 nginx 的 Pod 和 Service:

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: svc-demo
spec:
  replicas: 2
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - image: nginx:1.18.0
        name: svc-demo
        ports:
        - containerPort: 80

---

apiVersion: v1
kind: Service
metadata:
  name: svc-demo
spec:
  selector:  
    app: myapp
  ports:
  - targetPort: 80  # 后端Pod的端口
    port: 8080 # 服务要暴露的端口

```

查看 Pod 和 Service：

```bash

[root@k8s-master service]# kubectl get pods,svc 
NAME                           READY   STATUS    RESTARTS   AGE
pod/svc-demo-f9785fc46-hz6db   1/1     Running   1          7d22h
pod/svc-demo-f9785fc46-m99mj   1/1     Running   1          7d22h

NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          36d
service/svc-demo     NodePort    10.106.152.13   <none>        8080:31195/TCP   29d


```

创建 ingress 规则，`ingress-nginx.yaml`：

```bash

apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: "nginx"
  name: example
spec:
  rules: # 一个ingress可以配置多个rules
  - host: foo.bar.com # 域名配置，可以不写，匹配*，或者写 *.bar.com
    http:
      paths: # 相当于nginx的location，同一个host可以配置多个path
      - backend:
          serviceName: svc-demo  # 代理到哪个svc
          servicePort: 8080 # svc的端口
        path: /

```

创建ingress：

```bash
[root@k8s-master service]#  kubectl apply -f ingress-nginx.yaml

[root@k8s-master service]# kubectl get ingress
Warning: extensions/v1beta1 Ingress is deprecated in v1.14+, unavailable in v1.22+; use networking.k8s.io/v1 Ingress
NAME      CLASS    HOSTS         ADDRESS   PORTS   AGE
example   <none>   foo.bar.com             80      21m


```

window的 hosts 配置解析：

```bash

192.168.5.60 foo.bar.com


```
浏览器访问，可以看到已经成功通过ingress将请求转发到后端Pod上了。

[![](https://img2020.cnblogs.com/blog/1686603/202109/1686603-20210915105520693-237645752.png)](https://img2020.cnblogs.com/blog/1686603/202109/1686603-20210915105520693-237645752.png)

至此，一个简单的ingress示例就完成了，本文over。
