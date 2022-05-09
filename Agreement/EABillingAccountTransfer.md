# 转让 Microsoft 客户协议的 Azure 订阅计费所有权


在以下情况下，转移 Azure 订阅的计费所有权：

* 要将订阅的计费责任转移到其他计费所有者。
* 要将 Azure 订阅从一个许可协议转移到另一个许可协议。 例如，从企业协议或 Microsoft 在线订阅协议 (MOSA) 转移到 Microsoft 客户协议。

[检查你是否有权访问 Microsoft 客户协议](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/mca-request-billing-ownership?toc=/azure/cost-management-billing/microsoft-customer-agreement/toc.json#check-for-access)。

转移只会移动 Azure 订阅的计费责任 - 不会移动绑定到订阅的 Azure 资源，因此不会中断 Azure 服务。

此过程包含以下任务，我们将逐步引导你完成这些任务：

1. 请求计费所有权
2. 审阅/批准转移请求
3. 检查转移请求状态

发送或接受转移请求时，即表示你同意条款和条件。 有关详细信息，请参阅[转移条款和条件](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/subscription-transfer#transfer-terms-and-conditions)。

在开始之前，请确保请求计费所有权的对象具有以下角色之一：

* 对于 Microsoft 客户协议，此人必须具有计费帐户或者相关计费配置文件或发票科目的所有者或参与者角色。 有关详细信息，请参阅[计费角色和任务](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/understand-mca-roles#invoice-section-roles-and-tasks)。
* 对于企业协议，此人必须是帐户所有者。
* 对于 Microsoft 在线订阅协议，此人必须是帐户管理员。

 备注

若要进行转移，目标帐户必须是具有有效支付形式的付费帐户。 例如，如果目标是 Azure 免费帐户，则可以将其升级为 Microsoft 客户协议中的即用即付 Azure 计划。 然后就可以进行转移。

准备就绪后，请使用以下说明。 也可以继续观看以下视频，其中概述了该过程的每个步骤。

<iframe src="https://www.youtube-nocookie.com/embed/gfiUI2YLsgc" frameborder="0" allowfullscreen="true" data-linktype="external" title="视频: gfiUI2YLsgc"></iframe>

## 创建转移请求

以下过程演示如何通过选择“计费范围”>“计费帐户”>“计费对象信息”>“发票科目”导航到“转移请求”，然后单击“添加新请求”。 如果通过选择计费对象信息导航到“添加新请求”，则必须先选择计费对象信息，然后选择发票科目。

1. 以 Microsoft 客户协议计费帐户的发票科目所有者或参与者身份登录到 [Azure 门户](https://portal.azure.com/)。 使用接受 Microsoft 客户协议时使用的凭据。
2. 搜索“成本管理 + 计费”。
   [![Screenshot that shows Azure portal search for Cost Management + Billing.](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/billing-search-cost-management-billing.png)](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/billing-search-cost-management-billing.png#lightbox)
3. 在计费范围页中，选择“计费范围”，然后选择用于支付订阅中的 Azure 使用费用的计费帐户。 选择标记了“Microsoft 客户协议”的计费帐户。
   [![Screenshot that shows search in portal for Cost Management + Billing.](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/billing-scopes.png)](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/billing-scopes.png#lightbox)
   Azure 门户会记住你访问的最后一个计费范围，并在你下一次转到“成本管理 + 计费”页时显示该范围。 如果你早前访问过“成本管理 + 计费”，则看不到计费范围页。 如果是这样，请检查你是否处于[正确的范围](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/mca-request-billing-ownership?toc=/azure/cost-management-billing/microsoft-customer-agreement/toc.json#check-for-access)。 否则，请[切换范围](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/view-all-accounts#switch-billing-scope-in-the-azure-portal)，选择 Microsoft 客户协议的计费帐户。
4. 选择左侧的“计费对象信息”，然后从列表中选择“计费对象信息”。 在你接管订阅所有权后，系统会根据此计费对象信息计收订阅使用费用。
   [![Screenshot that shows selecting billing profiles.](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/billing-profile.png)](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/billing-profile.png#lightbox)
   备注

   如果看不到“计费对象信息”，则表明你未处于正确的计费范围。 需要为 Microsoft 客户协议选择计费帐户，然后选择“计费对象信息”。 若要了解如何更改范围，请参阅[在 Azure 门户中切换计费范围](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/view-all-accounts#switch-billing-scope-in-the-azure-portal)。
5. 选择左侧的“发票科目”，然后从列表中选择发票科目。 各计费对象信息都默认包含发票科目。 选择要将 Azure 订阅计费转移到的发票 - 这是 Azure 订阅使用转移到的发票。
   [![Screenshot that shows selecting invoice sections.](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/invoice-section.png)](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/invoice-section.png#lightbox)
6. 选择左下角的“转移请求”，然后选择“添加新请求”。 输入要从其请求计费所有权的用户的电子邮件地址。 用户必须具有旧订阅的帐户管理员角色。
   [![Screenshot that shows selecting transfer requests.](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/transfer-request-add-email.png)](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/transfer-request-add-email.png#lightbox)
7. 选择“发送转移请求”。

## 审阅并批准转移请求

1. 用户将收到一封电子邮件，其中包含查看转让请求的说明。 选择“查看请求”，在 Azure 门户中打开它。
   [![Screenshot that shows review transfer request email.](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/mca-review-transfer-request-email.png)](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/mca-review-transfer-request-email.png#lightbox)
2. 在 Azure 门户中，用户选择要从中转移 Azure 产品的计费帐户。 然后，在“订阅”选项卡上选择符合条件的订阅。
   [![Screenshot showing the Subscriptions tab.](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/review-transfer-request-subscriptions-select.png)](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/review-transfer-request-subscriptions-select.png#lightbox)
   备注

   无法转移已禁用的订阅。
3. 如果有可供转移的预留项，请选择“预留”选项卡，然后选择它们。 [![Screenshot showing the Reservations tab.](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/review-transfer-request-reservations-select.png)](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/review-transfer-request-reservations-select.png#lightbox)
4. 选择“查看请求”选项卡，验证有关要转移的订阅和预留项的信息。 如果出现“警告”或“失败”状态消息，请查看以下信息。 做好继续操作的准备后，请选择“转移”。
   [![Screenshot showing the Review request tab where you review your transfer selections.](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/review-transfer-request-complete.png)](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/review-transfer-request-complete.png#lightbox)
5. 此时会短暂出现一条“`Transfer is in progress`”消息。 转移成功完成后，会出现“转移详细信息”页，其中包含“`Transfer completed successfully`”消息。
   [![Screenshot showing the Transfer completed successfully page.](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/transfer-completed-successfully.png)](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/transfer-completed-successfully.png#lightbox)

在“查看请求”选项卡上，可能会显示以下状态消息。

* 准备转移 - 此 Azure 产品已通过验证，可以进行转移。
* 警告 - 所选 Azure 产品出现警告。 虽然仍可转移该产品，但这样做会产生一些后果，如果用户希望采取缓解措施，则他们应该了解这些后果。 例如，要转移的 Azure 订阅从 RI 中获益。 转移后，订阅将不再获得该权益。 若要最大程度地节省成本，请确保 RI 关联到可使用其权益的另一订阅。 此外，用户还可以选择返回到“选择”页并取消选择此 Azure 订阅。 有关详细信息，请选择“查看详细信息”。
* “失败”- 由于出现错误，无法转移所选的 Azure 产品。 用户需要返回“选择”页并取消选择此产品以转移其他选定的 Azure 产品。

## 检查转移请求状态

作为已请求转移的用户，请执行以下操作：

1. 登录 [Azure 门户](https://portal.azure.com/)。
2. 搜索“成本管理 + 计费”。
3. 在计费范围页中，选择已在其中启动转移请求的计费帐户，然后在左侧菜单中选择“转移请求”。
4. 选择已在其中启动转移请求的计费对象信息和发票科目，查看状态。
   [![Screenshot that shows the list of transfers with their status. ](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/transfer-requests-status-completed.png)](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/transfer-requests-status-completed.png#lightbox)

“转移请求”页将显示以下信息：

| 列        | 定义                                             |
| --------- | ------------------------------------------------ |
| 请求日期  | 发送转移请求的日期                               |
| Recipient | 已向其发送转移计费所有权请求的用户的电子邮件地址 |
| 到期日期  | 请求过期的日期                                   |
| 状态      | 转移请求的状态                                   |

转移请求可能处于以下状态之一：

| 状态         | 定义                                                              |
| ------------ | ----------------------------------------------------------------- |
| 正在进行     | 用户未接受转移请求。                                              |
| Processing   | 用户已批准转移请求。 用户选择的订阅的计费正在转移到你的发票科目。 |
| 已完成       | 用户选择的订阅的计费已转移到你的发票科目。                        |
| 已完成但出错 | 请求已完成，但用户选择的某些订阅的计费无法转移。                  |
| 已过期       | 用户未及时接受请求，请求现已过期。                                |
| 已取消       | 有权访问转移请求的某人取消了该请求。                              |
| 已拒绝       | 用户拒绝了转移请求。                                              |

作为已批准转移的用户，请执行以下操作：

1. 选择一个转移请求以查看详细信息。 转移详细信息页将显示以下信息：
   ![Screenshot that shows the Transfer status page with example status.](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/transfer-status-success-approver-view.png)[](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/media/mca-request-billing-ownership/transfer-status-success-approver-view.png#lightbox)

| 列                     | 定义                                                                                         |
| ---------------------- | -------------------------------------------------------------------------------------------- |
| 转移 ID                | 转移请求的唯一 ID。 提交支持请求时，请与 Azure 支持人员共享该 ID，以加速你的支持请求的处理。 |
| 请求转移的日期         | 发送转移请求的日期。                                                                         |
| 转移请求者             | 发送转移请求的用户的电子邮件地址。                                                           |
| 转移请求到期日期       | 仅当转移状态为“`Pending`”时才显示。 转移请求的过期日期。                                 |
| 发送给收件人的转移链接 | 仅当转移状态为“`Pending`”时才显示。 发送给用户的 URL，用于查看转移请求。                 |
| 转移完成日期           | 仅当转移状态为“`Completed`”时才显示。 完成转移的日期和时间。                             |

## 支持的订阅类型

可以请求下面列出的订阅类型的计费所有权。

* [操作包](https://azure.microsoft.com/offers/ms-azr-0025p/)^1^
* [Azure 开放式许可](https://azure.microsoft.com/offers/ms-azr-0111p/)^1^
* [Azure Pass 赞助](https://azure.microsoft.com/offers/azure-pass/)^1^
* [Enterprise 开发/测试](https://azure.microsoft.com/offers/ms-azr-0148p/)
* [免费试用版](https://azure.microsoft.com/offers/ms-azr-0044p/)^1^
* [即用即付](https://azure.microsoft.com/offers/ms-azr-0003p/)
* [即用即付开发/测试](https://azure.microsoft.com/offers/ms-azr-0023p/)
* [Microsoft Azure 计划](https://azure.microsoft.com/offers/ms-azr-0017g/)^2^
* [Microsoft Azure 赞助套餐](https://azure.microsoft.com/offers/ms-azr-0036p/)^1^
* [Microsoft 企业协议](https://azure.microsoft.com/pricing/enterprise-agreement/)
* [Microsoft 客户协议](https://azure.microsoft.com/pricing/purchase-options/microsoft-customer-agreement/)
* [Microsoft 合作伙伴网络](https://azure.microsoft.com/offers/ms-azr-0025p/)^1^
* [MSDN 平台](https://azure.microsoft.com/offers/ms-azr-0062p/)^1^
* [Visual Studio Enterprise (BizSpark) 订户](https://azure.microsoft.com/offers/ms-azr-0064p/)^1^
* [Visual Studio Enterprise (MPN) 订户](https://azure.microsoft.com/offers/ms-azr-0029p/)^1^
* [Visual Studio Enterprise 订户](https://azure.microsoft.com/offers/ms-azr-0063p/)^1^
* [Visual Studio Professional](https://azure.microsoft.com/offers/ms-azr-0059p/)^1^
* [Visual Studio Test Professional 订户](https://azure.microsoft.com/offers/ms-azr-0060p/)^1^

^1^ 转移后，订阅中可用的任何额度在新帐户中都将不可用。

^2^ 仅支持在 Azure 网站上注册期间创建的帐户中的订阅。

## 其他信息

以下部分提供有关转移订阅的附加信息。

### 取消以前的支持计划

如果你有一个 Azure 支持计划并想要将所有 Azure 订阅转移到新协议，则必须取消该支持计划，因为它不会随订阅一起转移。 例如，在将 Microsoft 在线订阅协议（在 Web 上购买的 Azure 订阅）转移到 Microsoft 客户协议时，就需要这样做。 若要取消支持计划，请执行以下操作：

如果旧帐户的帐户管理员凭据不同于用于访问新 Microsoft 客户协议帐户的凭据，请使用旧帐户的凭据。

1. 通过 [https://portal.azure.com](https://portal.azure.com/) 登录到 Azure 门户。
2. 导航到“成本管理 + 计费”。
3. 在左侧窗格中选择“计费范围”。
4. 选择与你的 Microsoft 支持计划关联的计费帐户。
   * 对于 Microsoft 客户协议：
     * 在左侧窗格中选择“周期性费用”。
     * 在支持计划行项右侧的右侧窗格中，选择省略号图标 (...)，然后选择“关闭自动续订” 。
   * 对于 Microsoft 在线订阅协议 (MOSA)：
     * 在左侧窗格中选择“订阅”。
     * 在右侧窗格中选择支持计划订阅，然后选择“取消”。

### 访问历史发票

在将计费所有权转移到新的 Microsoft 客户协议帐户后，你可能想要访问旧 Microsoft 在线订阅协议帐户（在 Web 上购买的 Azure 订阅）的发票。 为此，请按照以下步骤操作：

如果旧帐户的帐户管理员凭据不同于用于访问新 Microsoft 客户协议帐户的凭据，请使用旧帐户的凭据。

1. 通过 [https://portal.azure.com/](https://portal.azure.com/) 登录到 Azure 门户。
2. 导航到“成本管理 + 计费”。
3. 在左侧窗格中选择“计费范围”。
4. 选择与你的 Microsoft 在线订阅协议帐户关联的计费帐户。
5. 在左侧窗格中选择“发票”以访问历史发票。

### 服务不会中断

订阅中的 Azure 服务将保持正常运行，而不会出现任何中断。 我们只会转换用户选择转移的 Azure 订阅的计费关系。

### 已禁用的订阅

无法转移已禁用的订阅。 订阅必须处于活动状态才能转移其计费所有权。

### Azure 资源转移

订阅中的所有资源（例如 VM、磁盘和网站）都会转移。

### Azure 市场产品转移

Azure 市场产品将连同各自的订阅一起转移。

### Azure 预留项转移

如果正在转移企业协议 (EA) 订阅或 Microsoft 客户协议，则 Azure 预留会自动与订阅一起移动。

### 对 Azure 服务的访问权限

在转换期间，使用 [Azure 基于角色的访问控制 (Azure RBAC)](https://docs.microsoft.com/zh-cn/azure/role-based-access-control/overview) 为现有用户、组或服务主体分配的访问权限不受影响。

### 转移的订阅费用

订阅的原始计费所有者负责支付转移完成之前所报告的所有费用。 你的发票科目负责支付从转移开始时报告的费用。 可能有些费用是在转移之前发生的，但在转移之后才报告。 这些费用将显示在你的发票科目中。

### 取消转移请求

在批准或拒绝转移请求之前，你可以取消该请求。 若要取消转移请求，请转到[转移详细信息页](https://docs.microsoft.com/zh-cn/azure/cost-management-billing/manage/mca-request-billing-ownership?toc=/azure/cost-management-billing/microsoft-customer-agreement/toc.json#check-the-transfer-request-status)，并在页面底部选择“取消”。

### 软件即服务 (SaaS) 转移

SaaS 产品不会随订阅一起转移。 请让用户[联系 Azure 支持人员](https://portal.azure.com/?#blade/Microsoft_Azure_Support/HelpAndSupportBlade)转移 SaaS 产品的计费所有权。 除了计费所有权以外，用户还可以转移资源所有权。 使用资源所有权可以执行管理操作，例如删除产品，以及查看产品详细信息。 用户必须是 SaaS 产品的资源所有者才能转移资源所有权。

## 检查访问权限

检查协议类型以确定你是否有权访问 Microsoft 客户协议的计费帐户。

1. 请访问 Azure 门户以检查是否有计费帐户访问权限。 搜索并选择“成本管理 + 计费”。
   ![Screenshot that shows an Azure portal search for Cost Management + Billing.](https://docs.microsoft.com/zh-cn/azure/includes/media/billing-check-mca/billing-search-cost-management-billing.png)
2. 如果仅有权访问一个计费范围，请从菜单选择“属性” 。 如果计费帐户类型为“Microsoft 客户协议” ，则有权访问 Microsoft 客户协议的计费帐户。
   ![Microsoft Customer Agreement, Billing Account Type, Properties, Microsoft Azure portal](https://docs.microsoft.com/zh-cn/azure/includes/media/billing-check-mca/billing-mca-property.png)
3. 如果有权访问多个计费范围，请检查“计费帐户”列中的类型。 如果任何范围的计费帐户类型为“Microsoft 客户协议” ，则有权访问 Microsoft 客户协议的计费帐户。
   [![Microsoft Customer Agreement, Billing Account Type, Billing account list, Microsoft Azure portal](https://docs.microsoft.com/zh-cn/azure/includes/media/billing-check-mca/billing-mca-in-the-list.png)](https://docs.microsoft.com/zh-cn/azure/includes/media/billing-check-mca/billing-mca-in-the-list-zoomed-in.png#lightbox)
