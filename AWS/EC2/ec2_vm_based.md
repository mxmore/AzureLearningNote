# Amazon EC2 虚拟化技术演进：从 Xen 到 Nitro


今年2月，由光环新网运营的AWS 中国（北京）区域和由西云数据运营的 AWS 中国（宁夏）区域发布新的实例类型，新的实例类型包括 **C5、C5d、R5、R5d** 。除了这四种之外，在AWS国外部分区域还上线了最新的C5n。

![](https://ask.qcloudimg.com/http-save/yehe-4895051/9jw6p8h4de.jpeg?imageView2/2/w/1620)

这些新实例类型个个都具有鲜明的特征，我简单整理归纳如下：

* **C5实例** ：性价比显著提升（与 C4 实例相比，C5 实例提供了更高的内存与 vCPU 比率，并且性价比提高了 25%，某些应用程序提高了 50% 以上），更大的实例大小（C5 实例新的更大的实例 c5.18xlarge提供了 72 个 vCPU 和 144 GiB 内存并提供了 25 Gbps 的网络带宽）。
* **C5d实例** ：基于本地 NVMe 的 SSD 磁盘将被物理连接到主机服务器，提供与C5实例的生命周期相耦合的块级存储。c5d.18xlarge 规格的实例支持2块900GB的NVMe SSD作为本地存储。
* **C5n实例** ：这是C5 系列的最新成员，其c5n.18xlarge规格可提供高达 100Gbps 的网络吞吐量。
* **R5实例** ：其最大实例规格支持96 vCPU、768 GiB内存和25 Gbps 网络带宽。
* **R5d实例** ：R5d 实例与 R5 实例规格相同，它还包括高达 3.6 TB 的本地 NVMe 存储。

这些实例类型之所以如此实力超群，我认为主要归功于两点：

* 处理器升级

C5 实例配备  **Intel Xeon Platinum 8000 系列 (Skylake-SP) 处理器** ，它发布于2017/Q3，具有高达 3.4GHz 的稳定全核 Turbo CPU 时钟速度，并使用 Intel Turbo Boost Technology 来允许单个核心睿频高达3.5GHz。C5 实例为新的 Intel 高级矢量扩展 512 (AVX-512) 指令集提供了支持，与上一代 C4 实例相比，矢量和浮点计算性能提高最高可达2倍。
而发布于2015年的C4 实例类型，配备Intel Xeon E5-2666 v3 (Haswell) 处理器。其时钟频率为2.9 GHz，配合Intel® Turbo Boost后最高可达3.5 GHz。

* 采用了AWS Nitro 虚拟化平台

**AWS Nitro** 将是这篇文章的主角。本文会从它的发展历程、架构、所创造的价值等方面进行分析和介绍，试图总结出AWS上虚拟化基础平台发展的脉络。

# **AWS EC2虚拟化发展历程**

下表总结了AWS曾经采用的虚拟化技术，以及这些技术之间的性能对比：

![](https://ask.qcloudimg.com/http-save/yehe-4895051/x9am8w8o7k.jpeg?imageView2/2/w/1620)

* **#1是全模拟技术** 。这种虚拟化方式能支持未修改的客户机操作系统，但速度会严重下降。典型产品是VMware 在1986年发布的虚拟化产品。AWS 并没有采用这种虚拟化技术，放在表格中只是为了做对比用。
* #2 是 **基于Xen的半虚拟化技术** （Paravirtualization，PV）。PV 要求修改客户机内核和驱动。EC2第一个采用半虚拟化的实例类型是 m1.small。
* #3 到 #6 是 **基于Xen和CPU硬件的全虚拟化技术** （Hardware-assisted virtualization，HVM）。采用Xen HVM 技术的虚拟机运行在具有CPU和内存（VT-x）硬件虚拟化能力的处理器上，并使用半虚拟化驱动程序用于网络和存储设备。HVM 3.0 中尚未实现中断和定时器半虚拟化，但在4.0中已有改善。
* #7 和 #8 则是 **AWS Nitro技术** ，这是AWS 研发的一种新虚拟化平台。后面会有详细介绍。

过去几年中，Xen是AWS上虚拟化技术的主体，业已成为业界标准之一，已经非常成熟。那么，为什么AWS要从Xen 向 Nitro 发展呢？这得从Xen 的架构说起。

![](https://ask.qcloudimg.com/http-save/yehe-4895051/jgaetruxnq.jpeg?imageView2/2/w/1620)

从上图可以看出，Xen 实现了虚拟机的CPU 和内存虚拟化，但是虚拟机的I/O 访问，包括网络和存储等，都是通过虚拟机中的前端模块和 dom0 中的后端模块通信，然后由dom0 中的后端模块通过设备驱动实现的。 **这I/O路径太长，这降低了I/O性能，而且dom0还会和业务虚拟机抢占宿主机资源，很难实现管理虚机和业务虚机之间的平衡，以及避免抖动** 。

2013年，AWS 采用 Xen PV虚拟化技术的 **cr1.8xlarge 实例**的架构如下图所示：

![](https://ask.qcloudimg.com/http-save/yehe-4895051/8zbcp6ym9o.jpeg?imageView2/2/w/1620)

这是严格意义上 **未采用Nitro技术的最后一个EC2型号** 。简要说明：

* 图中的硬件（Hardware），是运行虚拟机的[物理服务器](https://cloud.tencent.com/product/cpm?from=10680)，采用了当时很强大的标准10Gbps网卡，以及管理一些本地磁盘的存储HBA卡。Hardware上既运行用户的业务虚拟机，还运行Xen的dom0虚拟机。
* VMM采用Xen项目的PV模式。
* 图中 Amzon Linux 代表Xen dom0，它负责访问硬件，向虚拟机提供I/O 能力。

图中 cr1.8xlarge 代表一个这种规格的虚拟机，它的本地存储、EBS卷和VPC网络访问都是通过Xen管理的dom0 虚拟机实现的。

# **Nitro起源和发展**

针对传统虚拟化架构存在的问题， **从2012年开始** ，AWS EC2虚拟化团队就开始思考以下问题：

1. 能做出比纯软件架构更好的hypervisor吗？
2. 设备模型本身很复杂，而且它会和业务虚拟机竞争CPU和系统资源，同时技术上它很难避免抖动发生
3. hypervisor太重了，能将hypervisor 和它周边的组件解耦吗？

从成立之日起，AWS就善于听取客户的呼声和建议，并不断进行迭代式改进，而不是大刀阔斧地从头设计一个新架构。根据该原则，AWS团队首先从最难的网络部分着手，其位置就是上图中的金黄色虚线框所示位置。从2013年开始，一些EC2实例类型开始支持网络接口的硬件虚拟化：单根I/O虚拟化（ **SR-IOV** ），而第一个是2013年1月发布的C3，它首次采用了AWS **增强型网络** （enhanced networking）。这最初是通过ixgbe驱动程序实现的，速度高达10 Gbps。

c3.8xlarge的架构如下图所示：

![](https://ask.qcloudimg.com/http-save/yehe-4895051/q7z6qo8upd.jpeg?imageView2/2/w/1620)

c3.8xlarge的架构与cr1.8xlarge相比，在宿主机上增加了一块新网卡，这块网卡和原有的标准网络通过一个回环线（loopback cable）连接起来。虚机VPC网络功能不再通过Xen 的dom0 实现，而是直接访问宿主机上的这块硬件网卡。 **C3 是AWS EC2 历史上增长最快的几个实例类型之一** ，它尤其以控制性能抖动和持续的网络性能著称。这可以看做Nitro思想的发源，那就是将软件功能卸载到专有硬件上。

下一个改进方向是 **EBS存储访问性能提升** 。

2015年，AWS推出了C4实例类型， **它针对EBS卷使用了硬件虚拟化技术** 。c4.8xlarge的架构如下图所示。仔细对比能发现，这个新架构与C3中的网络架构改进有些不同。在虚拟机中，还保留了“前端-后端”这种Xen传统架构，这是当时为了兼容性和稳妥新考虑，因为NVMe在当时来说还是一种非常新的技术。在宿主机上，采用了新收购的Annapurna Labs公司开发一种卡(下图中黄色虚线框内)，它能将远端存储以NMVe形式呈现给虚拟机。

![](https://ask.qcloudimg.com/http-save/yehe-4895051/s3d335frox.jpeg?imageView2/2/w/1620)

这个改进的结果是，宿主机上的CPU被Xen占用得少了，能更多地被虚机使用了。

2016年5月发布的 **X1 是第一个支持ENA的实例类型** 。ENA是增强型网络的最新实现，速度高达25 Gbps。ENA，全称是Elastic Network Adapter，它正是Nitro项目的一部分，它是由Annapurna Labs公司开发的。

![](https://ask.qcloudimg.com/http-save/yehe-4895051/5rgu9kgv0p.jpeg?imageView2/2/w/1620)

现在的ENA，能用于虚拟机和物理机，它以开源项目形式发布在github上。ENA 是AWS网络虚拟化一关键技术，它使得虚拟机能够绕过内核和用户空间网络处理程序，直接操作网卡硬件，这显著提升了网络效率。

从用户使用角度，也许只是用了一个新网卡驱动。但是其底层采用了Annapurna Labs公司开发的定制网络ASIC硬件卡。这是Nitro第一款真正的专用硬件卡。它不仅卸载了VPC网络功能，还卸载了EBS 存储网络功能。因此这是一种完全的网络负载卸载硬件。

![](https://ask.qcloudimg.com/http-save/yehe-4895051/8w0zxkzydx.jpeg?imageView2/2/w/1620)

下一步的优化方向在**实例存储**上。2017年，AWS发布了存储优化实例类型i3，它使用了SR-IOV和NVMe存储驱动。这是 **AWS首次采用Annapurna Labs研发的Nitro存储卡所管理的SSD磁盘** ，这些磁盘被直接映射给虚拟机，虚拟机通过NVME驱动来使用宿主机上的SSD磁盘。这能实现磁盘300万以上的IOPS性能。Nitro 芯片负责包括磁盘监控、加密、QoS等职责。

![](https://ask.qcloudimg.com/http-save/yehe-4895051/ciex593vhd.jpeg?imageView2/2/w/1620)

显然，到这时候为止，仍然剩下的问题只能是Xen 自身，以及它的管理功能部分了。Xen过于笨重，因为作为传统 Hypervisor，它必须做很多事情 - 它必须保护物理硬件和 BIOS，它必须虚拟化 CPU，虚拟化存储，虚拟化网络，并提供丰富的管理功能。其管理性dom0虚拟机会抢占业务虚机的系统资源。那到底能不能把Xen彻底替换掉呢？答案是肯定的，因为AWS在技术上从来没让人失望过。

2017年11月，AWS发布了C5 实例类型，它**首次使用基于KVM的Nitro hypervisor** 替换了Xen，hypervisor 软件大大被简化，Xen 所用的 dom0 也不需要了。其架构示意图如下：

![](https://ask.qcloudimg.com/http-save/yehe-4895051/9iiaddeqpo.jpeg?imageView2/2/w/1620)

AWS Nitro 重新构建了EC2虚拟化基础架构。Nitro 系统将存储、网络和安全功能卸载（offload）到专用的硬件（Nitro卡）上，带来的好处是虚拟化实例几乎可以为客户机操作系统提供主机的所有 CPU 和内存，同时Hypervisor 的功能也因此大大减弱。

Nitro 还被用到2017年发布的**AWS 首个物理机实例类型 i3.metal**中。下图是i3.metal架构示意图：

![](https://ask.qcloudimg.com/http-save/yehe-4895051/b7lxaq44yh.jpeg?imageView2/2/w/1620)

在i3.metal 中，Nitro 发挥了基础性作用。它的安全芯片通过提供硬件保护和固件验证功能为I3实例提供安全保障；它的各种卡，使得I3实例具备基于非易失性存储器标准 (NVMe) SSD 的实例存储，通过ENA支持高达 25Gbps 的聚合网络带宽。

# **Nitro 架构**

AWS Nitro 系统是模块化组件的集合，可以使用广泛的计算、存储、内存和网络选项来设计 EC2 实例，为新一代EC2实例提供动力。它包括三大部分：

![](https://ask.qcloudimg.com/http-save/yehe-4895051/457e9n5eum.jpeg?imageView2/2/w/1620)

## **Nitro 卡**

![](https://ask.qcloudimg.com/http-save/yehe-4895051/r2adtf7qqb.jpeg?imageView2/2/w/1620)

这些Nitro 卡是硬件，插入到宿主机的PCIe卡槽中，采用SR-IOV 直通（passthrough）技术将这些卡呈现给实例。包括：

* **VPC Data Plane（用于VPC访问的Nitro卡）** ：本质上是一块通过PCIe附加到宿主机上的一块定制网卡，支持网络封包和解包、安全组、限速器和路由等功能。实例通过ENA驱动和它通信。同时，该卡还带有一些网络加速功能。以限速器为例，每个Nitro支持的实例，不管它在哪个区域哪个数据中心哪个宿主机上，都会有一致的性能，这对分布式应用非常重要。
* **EBS Data Plane（用于EBS卷访问的Nitro卡）** ：本质上是一块通过PCIe附加到宿主机上的一块定制卡。通过该卡，远端存储被以NVMe设备形式展现给实例，实例通过标准NVMe驱动程序访问该卡。它首次被用在C4中。支持卷加密、存储加速；支持I3裸机实例。
* **Instance Storage Data Plane（用于实例存储访问的Nitro卡）** ：通过该卡，本地磁盘被以NVMe设备形式展现给实例，实例通过标准NVMe驱动程序访问这些磁盘。支持加密、限速器和本地磁盘监控。

除了卡之外，Nitro 还提供 **卡控制器（Card Controller）** 。它提供API端点，负责协调所有Nitro卡、Nitro Hypervisor和Nitro安全芯片。它还利用Nitro安全芯片实现了Hardware Root Of Trust（硬件信任根），支持实例监控、计量和认证。它还为Nitro EBS卡实现了NVMe控制器。

## **Nitro 安全芯片**

Nitro安全芯片整合到宿主机主板中，控制对所有非易失性存储的访问，持续监控和保护硬件资源，并在每次系统启动时独立验证固件。

## **Nitro hypervisor**

Nitro hypervisor位于 **极简化的定制的Linux 内核中，基于KVM** ，带有定制的VMM和小用户空间应用。它只负责管理内存和CPU分配，将Nitro卡虚拟功能分配给实例，监控和计量硬件等，不再需要提供任何网络功能。因此它只需执行虚拟机所需指令，快速而且简单，在大多数工作负载中能提供接近裸机的性能。

Nitro 各组件之间的关系如下图所示:

![](https://ask.qcloudimg.com/http-save/yehe-4895051/d39l9hq2vr.jpeg?imageView2/2/w/1620)

# **Nitro 带来的丰富价值**

## **更高网络访问性能**

利用Nitro提供的新一代 Elastic Network Adapter (ENA) 和 NVM Express (NVMe) 技术，C5 实例提供了高达 25 Gbps 的网络带宽和更低延迟及抖动。 **2018年发布的更强大变体 C5n 实例，支持网络带宽高达 100 Gbps** ，用户的仿真、内存缓存、[数据湖](https://cloud.tencent.com/solution/datalake_storage?from=10680)以及其他通讯密集型应用运行得将比以往更好。

采用Nitro增强网络功能后的网络延迟对比：

![](https://ask.qcloudimg.com/http-save/yehe-4895051/xjhvgg5551.jpeg?imageView2/2/w/1620)

（Series 1：cc2.8xlarge，2：c3.8xlarge，3：c4.8xlarge，4：c5.18xlarge，5：c5.18xlarge（采用ENAv2））

网络和存储带宽对比:

![](https://ask.qcloudimg.com/http-save/yehe-4895051/i1y8x81nt7.jpeg?imageView2/2/w/1620)

(1:c3.8xlarge,2:c4.8xlarge,3:c5.18xlarge,4:c5n.18xlarge. Series1:网络，Series2：存储)

## **更高EBS和本地存储访问性能**

Nitro 使得实例可通过物理方式连接到主机服务器的基于 NVMe 的本地 SSD 块级存储，以及将远端存储以NVMe设备的形式呈现给实例。

2019年3月，由Nitro支撑的新计算密集型 C5 和 C5d 实例已经在AWS 北京和宁夏区域推出。 **C5实例支持高达9Gbps 的专用 Amazon EBS 带宽** 。而  **C5d 最大实例规格则可使用两块900G的NVMe SSD** 。这些实例非常适合需要访问高速、低延迟的本地存储的应用程序。

## **更大实例大小和CPU内存比率**

由Nitro支撑的C5实例，其实例的CPU和内存比率，由C4的1：1.875上升到1：2；实例的最大规格，从C4的36vCPU/60Gib内存，上升到 **72vCPU/144Gib内存** 。

## **更低虚拟化花销**

Nitro Hypervisor 是一款 **轻薄的静态的虚拟机管理程序** ，可管理虚拟机的内存和CPU分配，并提供与大多数工作负载无法区分的性能。据Netflix公司Brendan Gregg 观察，Nitro Hypervisor的性能损耗非常小，通常不到1％，他的结论是  **Nitro提供的虚拟化性能接近裸设备** 。

## **更低Hypervisor抖动**

有了Nitro后，就不再需要为存储和网络I/O再预留CPU和内存资源了。这不仅使得可以向EC2实例分配更多资源，为更大的实例规格提供了可能，还为实现一个简单的轻量的hypervisor提供了可能，而这就为实现更低hypervisor抖动创造了条件。

下图是一AWS 客户在三种EC2实例上采用对延迟要求极低的一实时应用做的对比测试。蓝色是C5，红色是i3.metal，黄色是C4。SLA 是用于测试的实时应用所能忍受的最高延迟。

![](https://ask.qcloudimg.com/http-save/yehe-4895051/9oubsanvtd.jpeg?imageView2/2/w/1620)

从上图中的测试结果看， **C5 相对裸机只有一点极小的附加开销，而且性能非常平稳，几乎没有波动** ，能完全满足应用的SLA需求。而C4则有相对较大的波动，只能大概满足70的SLA。

## **更多实例类型**

AWS发布了基于Nitro的实例存储实例类型  **C5d，M5d 和 R5d** ，提供低延迟高吞吐的基于NVMe的实例存储。

AWS在2017 re：Invent上宣布了基于Nitro的**AWS EC2 Bare Metal实例** I3.metal。它没有性能开销，能够运行你喜欢的任何东西，比如Xen，KVM，容器，ESXi，FireCracker微虚机等；支持非虚拟化环境，支持容器环境，同时还能继续使用比如EBS、ELB和VPC等基础服务；支持比如SAP HANA和其它内存型应用。

AWS还基于Nitro发布了采用AMD EPYC处理器的系列实例 **R5，M5和T3** ，最高可降低10%成本。

AWS发布了基于Nitro的具有100Gbps网络带宽的实例类型 **C5n** ，这是运行HPC和分布式机器学习负载的理想类型。

AWS发布了基于Nitro的采用AWS Graviton（基于ARM）处理器的实例类型 **A1** ，最高可降低45%成本。

## **更低价格、更高性价比**

下表显示了AWS 北京（BJS）和中卫（ZHY）区域的4代和5代EC2实例的价格比较，你可以看到实实在在的价格下降：

![](https://ask.qcloudimg.com/http-save/yehe-4895051/qp4799otqu.jpeg?imageView2/2/w/1620)

目前，Nitro支撑的C5 实例提供了 EC2 产品系列中最佳的价格/计算性能比。与C4实例相比，其性价比提高了49% 。

与R4实例相比，由Nitro支撑的R5实例为每个vCPU提供额外5%的内存，且每 GiB 价格低50%。R5实例非常适用于高性能数据库、分布式内存缓存、内存数据库和大数据分析等应用程序。

## **为更多性能优化提供了可能**

对于需要深度定制化EC2 的用户而言，Nitro 还带了了另外的好处：对于EC2 更深入的监控和优化。在由Nitro支撑的C5实例中，你可以得到 **数百个PMC 计数器** （Performance Monitoring Counters ，[性能监控](https://cloud.tencent.com/product/apm?from=10680)计数器）。作为对比，以前的实例类型中，你只能看到区区7个PMCs。更多的PMC计数器，为性能优化提供了更多可能。

# **小结**

亚马逊 AWS CTO 沃纳·威格尔（Werner Vogels）曾经说过，“在亚马逊 AWS，我们90%到95%的新项目都是基于客户给我们的反馈，剩下5%也是从客户角度出发所做得创新尝试。”

而Nitro 正是这种项目之一，它诞生于2013年，成年于2017年，现在还在不断成长中。Nitro 正在作为AWS核心虚拟化架构平台，推动着AWS最核心的EC2产品家族不断往 **更大** （单实例的vCPU和内存更大）、 **更快** （I/O速度更快）、 **更安全** （采用Nitro安全芯片）、 **更稳定** （Hypervisor抖动更低）、 **更多类型** 、**更高性价**比方向演进，支撑越来越多用户越来越多的业务场景，创造着越来越大的业务价值。

主要参考文档：

1. AWS re:Invent 2018: Powering Next-Gen EC2 Instances: Deep Dive into the Nitro System (CMP303-R1)
2. AWS re:Invent 2017: C5 Instances and the Evolution of Amazon EC2 Virtualization (CMP332)
3. AWS re:Invent 2018: Deep Dive on Amazon EC2 Instances & Performance Optimization Best Practices （CMP307）
4. AWS re:Invent 2018:Optimizing Network Performance for Amazon EC2 Instances (CMP308-R1)
