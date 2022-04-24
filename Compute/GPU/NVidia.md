# NVidia GPU学习笔记


## NVidia RTX

主要用于实现实时光影追踪， 基于RTX平台构建的应用程序具有实时照片级渲染和AI增强图形， 视频和图片的处理能力强大功能


## NVidia Tesla



## Tensor Core VS CUDA Core

链接：https://www.zhihu.com/question/451127498/answer/1855483569

虽然都是核心，但是并不是说一个负责训练一个负责推理。CUDA是NVIDIA推出的统一计算架构，NVIDIA过去的几乎每款GPU都有CUDA Core，而Tensor Core是最近几年才有的，Tensor Core是专为执行[张量](https://www.zhihu.com/search?q=%E5%BC%A0%E9%87%8F&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A1855483569%7D)或矩阵运算而设计的专用执行单元，而这些运算正是深度学习所采用的核心计算函数。Tensor核心在训练方面能够提供高达**12倍**的teraflops (TFLOPS) 峰值，而在推理方面则可提供**6倍**的TFLOPS峰值。每个Tensor核心每个时钟周期可执行64次浮点混合乘加 (FMA) 运算。

CUDA内核：每一个GPU时钟执行一次值乘法

```text
1 x 1 per GPU clock
```

TENSOR核心：每个GPU时钟执行一次矩阵乘法

```text
[1 1 1       [1 1 1
 1 1 1   x    1 1 1    per GPU clock
 1 1 1]       1 1 1]
```

Tensor Core使用的计算能力要比Cuda Core高得多，这就是为什么Tensor Core能加速处于深度学习神经网络训练和推理运算核心的矩阵计算，能够在维持超低精度损失的同时大幅加速推理吞吐效率。

矩阵-矩阵乘法（GEMM）运算是神经网络训练和推理的核心，本质是在网络互联层中将大矩阵输入数据和权重相乘。每个Tensor核心都在矩阵中运行，并执行以下运算：

D=A*B+C

![](https://pic1.zhimg.com/80/v2-f600b65980d4694633fdae2611cf3bb3_720w.jpg?source=1940ef5c)

Turing架构Tensor核心中设计添加了INT8和INT4精度模式，以推断可以容忍量化的工作负载。而Ampere架构GA10x GPU中的新第三代Tensor Core架构可加速更多数据类型，并包括新的稀疏性功能，与Turing架构中的Tensor Core相比，矩阵乘法的速度提高了2倍。

![](https://pica.zhimg.com/80/v2-87e0dce4b64084f6673033a156014bda_720w.jpg?source=1940ef5c)
Turing vs Ampere Tensor Core
