# 使用 Azure 超级磁盘


本文介绍如何部署和使用超级磁盘，有关超级磁盘的概念性信息，请参阅 [Azure 中有哪些可用的磁盘类型？](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-types#ultra-disks)。

Azure 超级磁盘为 Azure IaaS 虚拟机 (VM) 提供高吞吐量、高 IOPS 和一致且低延迟的磁盘存储。 此新产品提供出类拔萃的性能，其可用性级别与我们的现有磁盘产品相同。 超级磁盘的一个主要优点是能够动态更改 SSD 的性能和工作负载，而无需重启 VM。 超级磁盘适用于 SAP HANA、顶层数据库等数据密集型工作负荷，以及事务密集型工作负荷。

## 正式发布版的范围和限制

超级磁盘不能用作 OS 磁盘，并且只能创建为空数据磁盘。 超级磁盘也不能与某些特性和功能一起使用，包括磁盘快照、磁盘导出、更改磁盘类型、VM 映像、可用性集、Azure 专用主机或 Azure 磁盘加密。 Azure 备份和 Azure Site Recovery 不支持超级磁盘。 此外，仅支持未缓存的读取和未缓存的写入。

超级磁盘默认支持 4k 物理扇区大小。 512E 扇区大小作为一种正式发布的产品/服务提供，无需注册。 大多数应用程序都与 4k 扇区大小兼容，但某些应用程序需要 512 字节扇区大小。 例如，Oracle Database 需要 12.2 版或更高版本才能支持 4k 本机磁盘。 对于较旧版本的 Oracle DB，需要 512 字节扇区大小。

对于超级磁盘，目前唯一可用的基础结构冗余选项是可用性区域。 使用任何其他冗余选项的 VM 无法附加超级磁盘。

下表概述了可使用超级磁盘的区域以及相应的可用性选项。

 备注

如果以下列表中的某个区域没有支持超级磁盘的可用性区域，则该区域中的 VM 必须在没有基础结构冗余的情况下部署，才能附加超级磁盘。

| 冗余选项                 | 区域                                                                                                                                                                                                     |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **单个 VM**        | 澳大利亚中部``巴西南部``印度中部``东亚``德国中西部``韩国中部``美国中北部、美国中南部、美国西部``US Gov 亚利桑那州、US Gov 德克萨斯州、US Gov 弗吉尼亚州 |
| **两个可用性区域** | 法国中部                                                                                                                                                                                                 |
| **三个可用性区域** | 澳大利亚东部``加拿大中部``欧洲北部、欧洲西部``Japan East``东南亚``瑞典中部``英国南部``美国中部、美国东部、美国东部 2、美国西部 2、美国西部 3            |

在每个具有超级磁盘的受支持区域中，并非每个 VM 大小都可用。 下表列出了与超级磁盘兼容的 VM 系列。

| VM 类型  | 大小                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 说明                                                                                                       |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 常规用途 | [DSv3 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/dv3-dsv3-series#dsv3-series)、[Ddsv4 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/ddv4-ddsv4-series#ddsv4-series)、[Dsv4 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/dv4-dsv4-series#dsv4-series)、[Dasv4 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/dav4-dasv4-series#dasv4-series)                                                                                                                                                                                                                                                  | CPU 与内存之比平衡。 适用于测试和开发、小到中型数据库和低到中等流量 Web 服务器。                           |
| 计算优化 | [FSv2 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/fsv2-series)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 高 CPU 与内存之比。 适用于中等流量的 Web 服务器、网络设备、批处理和应用程序服务器。                        |
| 内存优化 | [ESv3 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/ev3-esv3-series#esv3-series)、[Easv4 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/eav4-easv4-series#easv4-series)、[Edsv4 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/edv4-edsv4-series#edsv4-series)、[Esv4 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/ev4-esv4-series#esv4-series)、[M 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/m-series)、[Mv2 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/mv2-series)、[Msv2/Mdsv2 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/msv2-mdsv2-series) | 高内存与 CPU 之比。 适用于关系数据库服务器、中到大型规模的缓存和内存中分析。                               |
| 存储优化 | [LSv2 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/lsv2-series)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 较高的磁盘吞吐量和 IO，是大数据、SQL、NoSQL 数据库、数据仓库和大型事务数据库的理想之选。                   |
| GPU 优化 | [NCv2 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/ncv2-series)、[NCv3 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/ncv3-series)、[NCasT4_v3 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/nct4-v3-series)、[ND 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/nd-series)、[NDv2 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/ndv2-series)、[NVv3 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/nvv3-series)、[NVv4 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/nvv4-series)                                                                         | 针对大量图形绘制和视频编辑的专用虚拟机，以及带有深度学习功能的模型定型和推断 (ND)。 可选择单个或多个 GPU。 |
| 性能优化 | [HB 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/hb-series)、[HC 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/hc-series)、[HBv2 系列](https://docs.microsoft.com/zh-cn/azure/virtual-machines/hbv2-series)                                                                                                                                                                                                                                                                                                                                                                                                                 | 速度最快、功能最强大的 CPU 虚拟机具有可选的高吞吐量网络接口 (RDMA)。                                       |

## 确定 VM 大小和区域可用性

### 使用可用性区域的 VM

若要利用超级磁盘，需要确定你位于哪个可用性区域中。 并非每个区域都支持每一种使用超级磁盘的 VM 大小。 若要确定地区、区域和 VM 大小是否支持超级磁盘，请运行以下任一命令，确保首先替换“region”、“vmSize”和“subscription”值 ：

#### CLI

**Azure CLI**复制

```
subscription="<yourSubID>"
# example value is southeastasia
region="<yourLocation>"
# example value is Standard_E64s_v3
vmSize="<yourVMSize>"

az vm list-skus --resource-type virtualMachines  --location $region --query "[?name=='$vmSize'].locationInfo[0].zoneDetails[0].Name" --subscription $subscription
```

#### PowerShell

**PowerShell**复制

```
$region = "southeastasia"
$vmSize = "Standard_E64s_v3"
$sku = (Get-AzComputeResourceSku | where {$_.Locations.Contains($region) -and ($_.Name -eq $vmSize) -and $_.LocationInfo[0].ZoneDetails.Count -gt 0})
if($sku){$sku[0].LocationInfo[0].ZoneDetails} Else {Write-host "$vmSize is not supported with Ultra Disk in $region region"}
```

响应将会类似于以下形式，其中 X 为用于在所选地区进行部署的区域。 X 可能是1、2 或 3。

预留“区域”值，它表示可用性区域，部署超级磁盘时将会需要该值。

| ResourceType | 名称         | 位置    | 区域 | 限制 | 功能 | 值 |
| ------------ | ------------ | ------- | ---- | ---- | ---- | -- |
| disks        | UltraSSD_LRS | eastus2 | X    |      |      |    |

 备注

如果命令没有响应，则说明所选区域中的超级磁盘不支持所选 VM 大小。

现在，你已了解要部署到哪个区域，请按照本文中的部署步骤，部署附加超级磁盘的 VM，或将超级磁盘附加到某个现有的 VM。

### 没有冗余选项的 VM

目前，在所选区域中部署的超级磁盘在部署时不可使用任何冗余选项。 但是，并不是每一种支持超级磁盘的磁盘大小都可以在这些区域中。 若要确定哪些磁盘大小支持超级磁盘，可以使用以下任一代码片段。 请确保先替换 `vmSize` 和 `subscription` 值：

**Azure CLI**复制

```
subscription="<yourSubID>"
region="westus"
# example value is Standard_E64s_v3
vmSize="<yourVMSize>"

az vm list-skus --resource-type virtualMachines  --location $region --query "[?name=='$vmSize'].capabilities" --subscription $subscription
```

**Azure PowerShell**复制

```
$region = "westus"
$vmSize = "Standard_E64s_v3"
(Get-AzComputeResourceSku | where {$_.Locations.Contains($region) -and ($_.Name -eq $vmSize) })[0].Capabilities
```

响应将会类似于以下形式，`UltraSSDAvailable True` 指示 VM 大小是否支持此区域中的超级磁盘。

复制

```
Name                                         Value
----                                         -----
MaxResourceVolumeMB                          884736
OSVhdSizeMB                                  1047552
vCPUs                                        64
HyperVGenerations                            V1,V2
MemoryGB                                     432
MaxDataDiskCount                             32
LowPriorityCapable                           True
PremiumIO                                    True
VMDeploymentTypes                            IaaS
vCPUsAvailable                               64
ACUs                                         160
vCPUsPerCore                                 2
CombinedTempDiskAndCachedIOPS                128000
CombinedTempDiskAndCachedReadBytesPerSecond  1073741824
CombinedTempDiskAndCachedWriteBytesPerSecond 1073741824
CachedDiskBytes                              1717986918400
UncachedDiskIOPS                             80000
UncachedDiskBytesPerSecond                   1258291200
EphemeralOSDiskSupported                     True
AcceleratedNetworkingEnabled                 True
RdmaEnabled                                  False
MaxNetworkInterfaces                         8
UltraSSDAvailable                            True
```

## 使用 Azure 资源管理器部署超级磁盘

首先，确定要部署的 VM 大小。 有关受支持的 VM 大小的列表，请参阅[正式发布版的范围和限制](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-enable-ultra-ssd?tabs=azure-portal#ga-scope-and-limitations)部分。

如果需要创建具有多个超级磁盘的 VM，请参考示例[创建具有多个超级磁盘的 VM](https://aka.ms/ultradiskArmTemplate)。

如果要使用自己的模板，请确保将 `Microsoft.Compute/virtualMachines` 和 `Microsoft.Compute/Disks` 的“apiVersion”设置为“`2018-06-01`”（或更高版本）。

将磁盘 sku 设置为“UltraSSD_LRS”，然后设置磁盘容量、IOPS、可用性区域和吞吐量（以 MBps 为单位），以创建超级磁盘。

在预配 VM 后，可以对数据磁盘进行分区和格式设置并为工作负荷配置这些磁盘。

## 部署超级磁盘

* [Portal](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-enable-ultra-ssd?tabs=azure-portal#tabpanel_1_azure-portal)
* [Azure CLI](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-enable-ultra-ssd?tabs=azure-portal#tabpanel_1_azure-cli)
* [PowerShell](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-enable-ultra-ssd?tabs=azure-portal#tabpanel_1_azure-powershell)

本部分介绍如何部署配备超级磁盘作为数据磁盘的虚拟机。 假定你已熟悉如何部署虚拟机，如果你尚不熟悉，请参阅我们的[快速入门：在 Azure 门户中创建 Windows 虚拟机](https://docs.microsoft.com/zh-cn/azure/virtual-machines/windows/quick-create-portal)。

1. 登录到 [Azure 门户](https://portal.azure.com/)并导航到部署虚拟机 (VM)。
2. 确保选择[受支持的 VM 大小和区域](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-enable-ultra-ssd?tabs=azure-portal#ga-scope-and-limitations)。
3. 选择“可用性选项”中的“可用性区域” 。
4. 按你的选择填写其余条目。
5. 选择“磁盘”。
   [![Screenshot of vm creation flow, Basics blade.](https://docs.microsoft.com/zh-cn/azure/virtual-machines/media/virtual-machines-disks-getting-started-ultra-ssd/new-ultra-vm-create.png)](https://docs.microsoft.com/zh-cn/azure/virtual-machines/media/virtual-machines-disks-getting-started-ultra-ssd/new-ultra-vm-create.png#lightbox)
6. 在“磁盘”边栏选项卡上，为“启用超级磁盘兼容性”选择“是” 。
7. 选择“创建并附加新磁盘”，以立即附加超级磁盘。
   ![Screenshot of vm creation flow, disk blade, ultra is enabled and create and attach a new disk is highlighted.](https://docs.microsoft.com/zh-cn/azure/virtual-machines/media/virtual-machines-disks-getting-started-ultra-ssd/new-ultra-vm-disk-enable.png)
8. 在“创建新磁盘”边栏选项卡上，输入名称，然后选择“更改大小” 。
   ![Screenshot of create a new disk blade, change size highlighted.](https://docs.microsoft.com/zh-cn/azure/virtual-machines/media/virtual-machines-disks-getting-started-ultra-ssd/new-ultra-create-disk.png)
9. 将“磁盘 SKU”更改为“超级磁盘” 。
10. 将“自定义磁盘大小 (GiB)”、“磁盘 IOPS”和“磁盘吞吐量”的值更改为所选值 。
11. 在两个边栏选项卡中都选择“确定”。
    ![Screenshot of the select a disk size blade, ultra disk selected for storage type, other values highlighted.](https://docs.microsoft.com/zh-cn/azure/virtual-machines/media/virtual-machines-disks-getting-started-ultra-ssd/new-select-ultra-disk-size.png)
12. 继续执行 VM 部署，该过程与部署任何其他 VM 相同。

## 部署超级磁盘 - 512 字节扇区大小

* [Portal](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-enable-ultra-ssd?tabs=azure-portal#tabpanel_2_azure-portal)
* [Azure CLI](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-enable-ultra-ssd?tabs=azure-portal#tabpanel_2_azure-cli)
* [PowerShell](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-enable-ultra-ssd?tabs=azure-portal#tabpanel_2_azure-powershell)

1. 登录到 [Azure 门户](https://portal.azure.com/)，然后搜索并选择“磁盘”。
2. 选择“+新建”以创建新磁盘。
3. 选择支持超级磁盘的地区并选择可用性区域，根据需要填写其余值。
4. 选择“更改大小”。
   ![Screenshot of create disk blade, region, availability zone, and change size highlighted.](https://docs.microsoft.com/zh-cn/azure/virtual-machines/media/virtual-machines-disks-getting-started-ultra-ssd/create-managed-disk-basics-workflow.png)
5. 对于“磁盘 SKU”，请选择“超级磁盘”，然后根据所需性能填写值并选择“确定” 。
   ![Screenshot of creating ultra disk.](https://docs.microsoft.com/zh-cn/azure/virtual-machines/media/virtual-machines-disks-getting-started-ultra-ssd/select-disk-size-ultra.png)
6. 在“基本信息”边栏选项卡中，选择“高级”选项卡 。
7. 为“逻辑扇区大小”选择“512”，然后选择“查看 + 创建” 。
   ![Screenshot of selector for changing the ultra disk logical sector size to 512.](https://docs.microsoft.com/zh-cn/azure/virtual-machines/media/virtual-machines-disks-getting-started-ultra-ssd/select-different-sector-size-ultra.png)

## 附加超级磁盘

* [Portal](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-enable-ultra-ssd?tabs=azure-portal#tabpanel_3_azure-portal)
* [Azure CLI](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-enable-ultra-ssd?tabs=azure-portal#tabpanel_3_azure-cli)
* [PowerShell](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-enable-ultra-ssd?tabs=azure-portal#tabpanel_3_azure-powershell)

或者，如果现有 VM 位于能够使用超级磁盘的地区/可用性区域中，则可以使用超级磁盘，而不必创建新 VM。 方法是：在现有 VM 上启用超级磁盘，然后将其附加为数据磁盘。 若要启用超级磁盘兼容性，则必须停止该 VM。 在停止该 VM 后，可以启用兼容性，然后重启该 VM。 在启用了兼容性后，即可附加超级磁盘：

1. 导航到 VM 并将其停止，等待它解除分配。
2. 在解除分配 VM 后，请选择“磁盘”。
3. 选择“其他设置”。
   ![Screenshot of the disk blade, additional settings highlighted.](https://docs.microsoft.com/zh-cn/azure/virtual-machines/media/virtual-machines-disks-getting-started-ultra-ssd/new-ultra-disk-additional-settings.png)
4. 为“启用超级磁盘兼容性”选择“是” 。
   ![Screenshot of enable ultra disk compatibility.](https://docs.microsoft.com/zh-cn/azure/virtual-machines/media/virtual-machines-disks-getting-started-ultra-ssd/enable-ultra-disks-existing-vm.png)
5. 选择“保存”。
6. 选择“创建并附加新磁盘”，并填写新磁盘的名称。
7. 对于“存储类型”，请选择“超级磁盘” 。
8. 将“大小 (GiB)”、“最大 IOPS”和“最大吞吐量”的值更改为所选值 。
9. 在返回到磁盘的边栏选项卡后，选择“保存”。
   ![Screenshot of disk blade, adding a new ultra disk.](https://docs.microsoft.com/zh-cn/azure/virtual-machines/media/virtual-machines-disks-getting-started-ultra-ssd/new-create-ultra-disk-existing-vm.png)
10. 再次启动 VM。

## 调整超级磁盘的性能

* [Portal](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-enable-ultra-ssd?tabs=azure-portal#tabpanel_4_azure-portal)
* [Azure CLI](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-enable-ultra-ssd?tabs=azure-portal#tabpanel_4_azure-cli)
* [PowerShell](https://docs.microsoft.com/zh-cn/azure/virtual-machines/disks-enable-ultra-ssd?tabs=azure-portal#tabpanel_4_azure-powershell)

超级磁盘具有一项可用于调整其性能的独特功能。 可以在磁盘本身上从 Azure 门户完成这些调整。

1. 导航到 VM 并选择“磁盘”。
2. 选择要修改其性能的超级磁盘。
   ![Screenshot of disks blade on your vm, ultra disk is highlighted.](https://docs.microsoft.com/zh-cn/azure/virtual-machines/media/virtual-machines-disks-getting-started-ultra-ssd/select-ultra-disk-to-modify.png)
3. 选择“大小 + 性能”，然后完成修改。
4. 选择“保存”。
   ![Screenshot of configuration blade on your ultra disk, disk size, iops, and throughput are highlighted, save is highlighted.](https://docs.microsoft.com/zh-cn/azure/virtual-machines/media/virtual-machines-disks-getting-started-ultra-ssd/modify-ultra-disk-performance.png)

## 后续步骤
