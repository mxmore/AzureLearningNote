# 无本地临时磁盘的 Azure VM 规格

```txt
提示

请尝试使用[虚拟机选择器工具](https://aka.ms/vm-selector)查找最适合你工作负载的其他尺寸。

本文提供有关没有本地临时磁盘（即无本地临时磁盘）的 Azure VM 大小的常见问题解答 (FAQ)。

```

## 无本地临时磁盘是什么意思？

通常，我们的 VM 规格（例如 Standard_D2s_v3、Standard_E48_v3）包含一个小型本地磁盘（例如 D:驱动器）。 对于 [Dasv5](https://docs.microsoft.com/zh-cn/azure/virtual-machines/dasv5-dadsv5-series) 和 [Easv5](https://docs.microsoft.com/zh-cn/azure/virtual-machines/easv5-eadsv5-series) 等 VM 系列，小型本地磁盘已不再存在。 不过，你仍然可以附加标准 HDD、高级 SSD 或超级 SSD 以将其用作远程存储。

## 如果仍需本地临时磁盘，该怎么办？

如果你的工作负载需要本地临时磁盘，我们仍将提供 [Dadsv5](https://docs.microsoft.com/zh-cn/azure/virtual-machines/dasv5-dadsv5-series) 等大小。

```txt
 备注

本地临时磁盘不是持久性的；若要确保数据是持久性数据，请使用标准 HDD、高级 SSD 或超级 SSD 选项。
```

## 是否可将具有本地临时磁盘的 VM 规格调整为无本地临时磁盘的 VM 规格？

否。 只允许下方的组合调整规格：

1. VM（具有本地临时磁盘）-> VM（具有本地临时磁盘）；以及
2. VM（无本地临时磁盘）-> VM（无本地临时磁盘）。

如果你想知道解决方法，请查看下一个问题。

```txt
 备注

如果映像依赖于资源磁盘，或者本地临时磁盘上存在页面文件或交换文件，则无磁盘映像将不起作用，而需改用“具有磁盘”替代项。
```

## 如何从具有本地临时磁盘的 VM 规格迁移到无本地临时磁盘的 VM 规格？

可按以下步骤迁移：

1. 以本地管理员身份连接到具有本地临时磁盘（例如 D: 驱动器）的虚拟机。
2. 按照[使用 D: 驱动器作为 Windows VM 上的数据驱动器](https://docs.microsoft.com/zh-cn/azure/virtual-machines/windows/change-drive-letter)的“将 pagefile.sys 临时移到 C 驱动器”部分中所述的指导原则，将本地临时磁盘（D: 驱动器）中的页面文件移到 C: 驱动器。

```txt
 备注

   按照“使用 D: 驱动器作为 Windows VM 上的数据驱动器”的“将 pagefile.sys 临时移到 C 驱动器”部分中所述的指导原则，将本地临时磁盘（D: 驱动器）中的页面文件移到 C: 驱动器。 **不严格按照所述步骤操作可能导致出现错误消息 -“无法调整 VM 大小，因为不允许将资源磁盘 VM 规格更改为非资源磁盘 VM 规格，反之亦然。”**
```

3. 按照[使用门户或 Azure CLI 创建快照](https://docs.microsoft.com/zh-cn/azure/virtual-machines/linux/snapshot-copy-managed-disk)中所述的步骤创建 VM 的快照。
4. 按照[使用 CLI 从快照创建虚拟机](https://docs.microsoft.com/zh-cn/previous-versions/azure/virtual-machines/scripts/virtual-machines-linux-cli-sample-create-vm-from-snapshot)中所述的步骤，使用快照创建新的无磁盘 VM（例如 Dv5、Dsv5、Dasv5、Ev5、Esv5、Easv5 系列）。

## 这些 VM 规格是否支持 Linux 和 Windows 操作系统 (OS)？

是的。

## 这是否会中断自定义脚本、自定义映像或在本地临时磁盘上具有暂存文件或页面文件的 OS 映像？

如果自定义 OS 映像指向本地临时磁盘，则该映像可能无法通过此无磁盘规格正常工作。
