# Ddv5 和 Ddsv5 系列


适用于：✔️ Linux VM ✔️ Windows VM ✔️ 灵活规模集 ✔️ 统一规模集

Ddv5 和 Ddsv5 系列虚拟机采用第三代 Intel® Xeon® Platinum 8370C (Ice Lake) 处理器，具有[超线程配置](https://www.intel.com/content/www/us/en/architecture-and-technology/hyper-threading/hyper-threading-technology.html)，为大多数通用工作负载提供了更好的价值主张。 这一新款处理器全核睿频时钟速度为 3.5 GHz，具备 [Intel® 睿频加速技术](https://www.intel.com/content/www/us/en/architecture-and-technology/turbo-boost/turbo-boost-technology.html)、[Intel® 高级矢量扩展 512 (Intel® AVX-512)](https://www.intel.com/content/www/us/en/architecture-and-technology/avx-512-overview.html) 和 [Intel® 深度学习加速](https://software.intel.com/content/www/us/en/develop/topics/ai/deep-learning-boost.html)。 这些虚拟机提供 vCPU 与内存和临时存储的组合，以满足与大多数企业工作负载相关的要求，例如中小型数据库、中低流量 Web 服务器、应用程序服务器等。

## Ddv5 系列

Ddv5 系列虚拟机采用第三代 Intel® Xeon® Platinum 8370C (Ice Lake) 处理器，这款处理器全核睿频时钟速度可达 3.5 GHz。 这些虚拟机提供多达 96 个 vCPU 和 384 GiB 的 RAM，以及快速的本地 SSD 存储（容量多达 3,600 GiB）。 与上一代相比，Ddv5 系列虚拟机为大多数通用工作负载提供了更好的价值主张（例如，提高了可伸缩性并升级了 CPU）。 这些虚拟机还具有快速的大容量本地 SSD 存储（容量多达 3,600 GiB）。

Ddv5 系列虚拟机支持标准 SSD 和标准 HDD 磁盘类型。 要使用高级 SSD 或超级磁盘存储，请选择 Ddsv5 系列虚拟机。 磁盘存储与虚拟机分开计费。 [查看磁盘定价](https://azure.microsoft.com/pricing/details/managed-disks/)。

[高级存储](https://docs.microsoft.com/zh-cn/azure/virtual-machines/premium-storage-performance)：不支持
[高级存储缓存](https://docs.microsoft.com/zh-cn/azure/virtual-machines/premium-storage-performance)：不支持
[实时迁移](https://docs.microsoft.com/zh-cn/azure/virtual-machines/maintenance-and-updates)：支持
[内存保留更新](https://docs.microsoft.com/zh-cn/azure/virtual-machines/maintenance-and-updates)：支持
[VM 代系支持](https://docs.microsoft.com/zh-cn/azure/virtual-machines/generation-2)：第 1 代和第 2 代
[加速网络](https://docs.microsoft.com/zh-cn/azure/virtual-network/create-vm-accelerated-networking-cli)：必需
[临时 OS 磁盘](https://docs.microsoft.com/zh-cn/azure/virtual-machines/ephemeral-os-disks)：支持
[嵌套虚拟化](https://docs.microsoft.com/zh-CN/virtualization/hyper-v-on-windows/user-guide/nested-virtualization)：支持

| 大小                 | vCPU | 内存:GiB | 临时存储 (SSD) GiB | 最大数据磁盘数 | 临时存储的最大吞吐量：IOPS/MBps^*^ | 最大 NIC 数 | 最大网络带宽 (Mbps) |
| -------------------- | ---- | -------- | ------------------ | -------------- | ---------------------------------- | ----------- | ------------------- |
| Standard_D2d_v5^1,2^ | 2    | 8        | 75                 | 4              | 9000/125                           | 2           | 12500               |
| Standard_D4d_v5      | 4    | 16       | 150                | 8              | 19000/250                          | 2           | 12500               |
| Standard_D8d_v5      | 8    | 32       | 300                | 16             | 38000/500                          | 4           | 12500               |
| Standard_D16d_v5     | 16   | 64       | 600                | 32             | 75000/1000                         | 8           | 12500               |
| Standard_D32d_v5     | 32   | 128      | 1200               | 32             | 150000/2000                        | 8           | 16000               |
| Standard_D48d_v5     | 48   | 192      | 1800               | 32             | 225000/3000                        | 8           | 24000               |
| Standard_D64d_v5     | 64   | 256      | 2400               | 32             | 300000/4000                        | 8           | 30000               |
| Standard_D96d_v5     | 96   | 384      | 3600               | 32             | 450000/4000                        | 8           | 35000               |

^*^ 这些 IOP 值可以通过使用 [Gen2 VM](https://docs.microsoft.com/zh-cn/azure/virtual-machines/generation-2) 来保证
^1^ 默认情况下，必须在所有 Ddv5 虚拟机上启用加速网络。
^2^ 加速网络可应用于两个 NIC。

## Ddsv5 系列

Ddsv5 系列虚拟机采用第三代 Intel® Xeon® Platinum 8370C (Ice Lake) 处理器，这款处理器全核睿频时钟速度可达 3.5 GHz。 这些虚拟机提供多达 96 个 vCPU 和 384 GiB 的 RAM，以及快速的本地 SSD 存储（容量多达 3,600 GiB）。 与上一代相比，Ddsv5 系列虚拟机为大多数通用工作负载提供了更好的价值主张（例如，提高了可伸缩性并升级了 CPU）。

Ddsv5 系列虚拟机支持标准 SSD、标准 HDD 和高级 HDD 磁盘类型。 还可根据超级磁盘存储的区域可用性附加该存储。 磁盘存储与虚拟机分开计费。 [查看磁盘定价](https://azure.microsoft.com/pricing/details/managed-disks/)。

[高级存储](https://docs.microsoft.com/zh-cn/azure/virtual-machines/premium-storage-performance)：支持
[高级存储缓存](https://docs.microsoft.com/zh-cn/azure/virtual-machines/premium-storage-performance)：支持
[实时迁移](https://docs.microsoft.com/zh-cn/azure/virtual-machines/maintenance-and-updates)：支持
[内存保留更新](https://docs.microsoft.com/zh-cn/azure/virtual-machines/maintenance-and-updates)：支持
[VM 代系支持](https://docs.microsoft.com/zh-cn/azure/virtual-machines/generation-2)：第 1 代和第 2 代
[加速网络](https://docs.microsoft.com/zh-cn/azure/virtual-network/create-vm-accelerated-networking-cli)：必需
[临时 OS 磁盘](https://docs.microsoft.com/zh-cn/azure/virtual-machines/ephemeral-os-disks)：支持
[嵌套虚拟化](https://docs.microsoft.com/zh-CN/virtualization/hyper-v-on-windows/user-guide/nested-virtualization)：支持

| 大小                  | vCPU | 内存:GiB | 临时存储 (SSD) GiB | 最大数据磁盘数 | 临时存储的最大吞吐量：IOPS/MBps^*^ | 最大非缓存磁盘吞吐量：IOPS/MBps | 突发非缓存磁盘的最大吞吐量：IOPS/MBps^3^ | 最大 NIC 数 | 最大网络带宽 (Mbps) |
| --------------------- | ---- | -------- | ------------------ | -------------- | ---------------------------------- | ------------------------------- | ---------------------------------------- | ----------- | ------------------- |
| Standard_D2ds_v5^1,2^ | 2    | 8        | 75                 | 4              | 9000/125                           | 3750/85                         | 10000/1200                               | 2           | 12500               |
| Standard_D4ds_v5      | 4    | 16       | 150                | 8              | 19000/250                          | 6400/145                        | 20000/1200                               | 2           | 12500               |
| Standard_D8ds_v5      | 8    | 32       | 300                | 16             | 38000/500                          | 12800/290                       | 20000/1200                               | 4           | 12500               |
| Standard_D16ds_v5     | 16   | 64       | 600                | 32             | 75000/1000                         | 25600/600                       | 40000/1200                               | 8           | 12500               |
| Standard_D32ds_v5     | 32   | 128      | 1200               | 32             | 150000/2000                        | 51200/865                       | 80000/2000                               | 8           | 16000               |
| Standard_D48ds_v5     | 48   | 192      | 1800               | 32             | 225000/3000                        | 76800/1315                      | 80000/3000                               | 8           | 24000               |
| Standard_D64ds_v5     | 64   | 256      | 2400               | 32             | 375000/4000                        | 80000/1735                      | 80000/3000                               | 8           | 30000               |
| Standard_D96ds_v5     | 96   | 384      | 3600               | 32             | 450000/4000                        | 80000/2600                      | 80000/4000                               | 8           | 35000               |

^*^ 这些 IOP 值可以通过使用 [Gen2 VM](https://docs.microsoft.com/zh-cn/azure/virtual-machines/generation-2) 来保证
^1^ 默认情况下，必须在所有 Ddsv5 虚拟机上启用加速网络。
^2^ 加速网络可应用于两个 NIC。
^3^ Ddsv5 系列虚拟机可通过[突发方式](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disk-bursting)提高其磁盘性能，最大突发的持续时间一次长达 30 分钟。

## 大小表定义

* 存储容量的单位为 GiB 或 1024^3 字节。 比较以 GB（1000^3 字节）为单位的磁盘和以 GiB（1024^3 字节）为单位的磁盘时，请记住以 GiB 为单位的容量数显得更小。 例如，1023 GiB = 1098.4 GB。
* 磁盘吞吐量的单位为每秒输入/输出操作数 (IOPS) 和 Mbps，其中 Mbps = 10^6 字节/秒。
* 数据磁盘可以在缓存或非缓存模式下运行。 对于缓存数据磁盘操作，主机缓存模式设置为 **ReadOnly** 或  **ReadWrite** 。 对于非缓存数据磁盘操作，主机缓存模式设置为  **None** 。
* 如要了解如何为虚拟机获得最佳存储性能，请参阅[虚拟机和磁盘性能](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-performance)。
* **预期的网络带宽**是指跨所有 NIC 为每个 VM 类型分配的最大聚合带宽，适用于所有目标。 有关详细信息，请参阅[虚拟机网络带宽](https://docs.microsoft.com/zh-cn/azure/virtual-network/virtual-machine-network-throughput)。
  上限不能保证。 这些限制能够为目标应用程序选择适当的虚拟机类型提供指导。 实际的网络性能取决于多种因素，比如网络拥塞、应用程序负载和网络设置。 有关如何优化网络吞吐量的信息，请参阅[为 Azure 虚拟机优化网络吞吐量](https://docs.microsoft.com/zh-cn/azure/virtual-network/virtual-network-optimize-network-bandwidth)。 如要在 Linux 或 Windows 中达到预期的网络性能，可能需要选择特定的版本或优化虚拟机。 有关详细信息，请参阅[带宽/吞吐量测试 (NTTTCP)](https://docs.microsoft.com/zh-cn/azure/virtual-network/virtual-network-bandwidth-testing)。

## 其他大小和信息

* [常规用途](https://docs.microsoft.com/zh-cn/azure/virtual-machines/sizes-general)
* [内存优化](https://docs.microsoft.com/zh-cn/azure/virtual-machines/sizes-memory)
* [存储优化](https://docs.microsoft.com/zh-cn/azure/virtual-machines/sizes-storage)
* [GPU 优化](https://docs.microsoft.com/zh-cn/azure/virtual-machines/sizes-gpu)
* [高性能计算](https://docs.microsoft.com/zh-cn/azure/virtual-machines/sizes-hpc)
* [前几代](https://docs.microsoft.com/zh-cn/azure/virtual-machines/sizes-previous-gen)

定价计算器：[定价计算器](https://azure.microsoft.com/pricing/calculator/)

有关磁盘类型的详细信息，请参阅[磁盘类型](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-types#ultra-disks)
