# 0 OK3576-C_硬件手册

RK3576是一颗高性能、低功耗的应用处理器芯片，集成了4个Cortex-A72和4个Cortex-A53及独立的NEON协处理器；适用于ARM PC、边缘计算、个人移动互联网设备及其它多媒体产品。

RK3576内置了多种功能强大的嵌入式硬件引擎，为高端应用提供了优异的性能，支持4K@120fps 的H.265、VP9、AVS2和AV1解码器，支持4k@60fps的H.264解码器；还支持4K@60fps的H.264 和H.265编码器，高质量的JPEG编码器/解码器，专门的图像预处理器和后处理器。

内置3D GPU，能够完全兼容OpenGL ES1.1/2.0/3.2、OpenCL 2.0和Vulkan1.1。带有MMU的特殊2D硬件引擎将最大限度地提高显示性能，并提供流畅的操作体验。

引入了新一代完全基于硬件的最大16M像素ISP（图像信号处理器），实现了多种算法加速器，如HDR、3A、CAC、3DNR、2DNR、锐化、去雾、增强、鱼眼校正、伽马校正等。

内嵌的NPU支持INT4/INT8/INT16/FP16/BF16/TF32混合运算。此外，凭借其强大的兼容性，可以轻松转换基于TensorFlow/MXNet/PyTorch/Caffe等一系列框架的网络模型。

RK3576具有高性能的外部存储器接口（LPDDR4/LPDDR4X/LPDDR5），能够支持苛刻的存储器带宽（能够支持存储器高带宽要求的系统），还提供了一套完整的外设接口，以灵活支持各类应用。

目标应用有:

+ 信息发布终端
+ 智能座舱
+ 智慧大屏
+ AR/VR
+ 边缘计算
+ 高端IPC
+ 智能NVR、
+ 高端平板
+ ARM PC

……

**RK3576处理器框图**

![Image](./images/OK3576C_hardware/0670391ab6534230aede3ea9e26b9868.png)

# 第二章  FET3576-C核心板介绍
## 2.1  FET3576-C核心板外观图


![Image](./images/OK3576C_hardware/4f8192591c6345b28917a806d32b2885.png)

**核心板正面视图**



![Image](./images/OK3576C_hardware/361c5272c28d45c58b73ad736e028066.png)

**核心板反面视图**

## 
## 2.2  FET3576-C 核心板框图
![Image](./images/OK3576C_hardware/67bbd894eb35475086ac27181de438c4.png)

**核心板框图**



## 2.3  FET3576-C核心板尺寸图
FET3576-C核心板尺寸图如下： 

![Image](./images/OK3576C_hardware/1b8554b0e9fd4294a0ba44d3349e636f.png)

**顶层尺寸图**

![Image](./images/OK3576C_hardware/c9d3447b465546be9ad438beb6c92363.png)

**底层尺寸图**

单位：mm![Image](./images/OK3576C_hardware/679223260c33478eaf0b7de83224e418.png)

结构尺寸：68mm×50mm，尺寸公差±0.15mm；更多详细尺寸请见用户资料dxf结构文件。

制版工艺：厚度1.6mm，10层沉金 PCB。

连接器：四个0.4mm间距，100pin 板对板连接器。连接器尺寸图见附录。

核心板的四角预留了四个直径2.2mm的安装孔，产品使用在震动环境的客户可以安装固定螺丝，提高产品连接的可靠性。

用户可以参考开发板设计，在底板使用M2，L=1.5mm的贴片螺母，贴片螺母的规格参见下图

![Image](./images/OK3576C_hardware/e1bbcd19a64f483a8ca0679afb0b8a85.png)

![Image](./images/OK3576C_hardware/9e128ca24ffc4042bff00c58c7aff308.png)



## 2.4 性能参数
### 2.4.1  系统主频
| **名称** | **规格** |  |  |  | **说明** |
| :---: | :---: | --- | --- | --- | :---: |
|  | **最小** | **典型** | **最大** | **单位** |  |
| 系统主频Arm® Cortex®-A72 | - | - | 2300 | MHz | - |
| 系统主频Arm® Cortex®-A53 | - | - | 2200 | MHz |  |
| 系统主频Arm® Cortex®-M0 | - | - | - | - | - |


### 2.4.2  供电参数
| **参数** | **引脚标号** | **规格** |  |  |  | **说明** |
| :---: | :---: | :---: | --- | --- | --- | :---: |
|  |  | **最小** | **典型** | **最大** | **单位** |  |
| 主电源电压 | 12V | 11.5 | 12 | 12.4 | V | - |


### 2.4.3  工作环境
| **参数描述** |  | **规格** |  |  |  | **说明** |
| :---: | --- | :---: | --- | --- | --- | :---: |
|  |  | **最小** | **典型** | **最大** | **单位** |  |
| 工作温度 | 工作环境 | 0 | 25 | 80 | ℃ | 商业级 |
|  | 存储环境 | -40 | 25 | +125 | ℃ |  |
| 湿度 | 工作环境 | 10 | - | 90 | ％RH | 无凝露 |
|  | 存储环境 | 5 | - | 95 | ％RH |  |


### 2.4.4  核心板接口速度
| **参数** | **规格** |  |  |  | **说明** |
| :---: | :---: | --- | --- | --- | :---: |
|  | **最小** | **典型** | **最大** | **单位** |  |
| 串口通讯速度 | - | 115200 | 4M | bps | - |
| SPI时钟频率 | - | - | 50 | MHz | - |
| I2C通讯速度 | - | 100 | 400 | Kbps | - |
| USB3.0接口速度 | - | - | 5 | Gbps | - |
| USB2.0接口速度 | - | - | 480 | Mbps | - |
| CAN通讯速度 | - | - | 1 | Mbps | - |
| PCIe2.1 | - | - | 5 | Gbps | - |


### 2.4.5  ESD特性
| 参数 | 规格 |  | 单位 | 适用范围 |
| :---: | :---: | --- | :---: | :---: |
|  | 最小 | 最大 |  |  |
| ESD HBM(ESDA/JEDEC JS-001-2017) | -2000 | 2000 | V | 核心板所有引出信号 |
| ESD CDM(ESDA/JEDEC JS-002-2018) | -250 | 250 | V | 核心板所有引出信号 |


注：

1、以上数据由瑞芯微官方提供

2、核心板所有引出信号均为静电敏感信号，在底板设计时应对接口做好静电防护，并在核心板运输、组装、使用过程中注意做好静电防护

## 2.5  核心板接口资源
FET3576-C核心板接口资源支持如下表：

| **功能** | **数量** | **参数** |
| :---: | :---: | --- |
| MIPI CSI | 5 | ·支持 5 个 CSI-2 接口   ·其中 4 个接口为 2 个 D-PHY v1.2 data-lane，2.4Gbps/lane   ·这 4 个接口可以组合成 2 个拥有 4 data-lane 接口   ·另外 1 个接口支持 4 D-PHY data-lane 或者 3 C-PHY trios   ·D-PHY v2.0，lane speed is 4.5Gbps   ·C-PHY v1.1，trio speed is 2.4Gsps |
| DVP | 1 | ·8/10/12/16-bit 标准DVP接口，最高150MHz数据输入；   ·支持 BT.601/BT.656 和 BT.1120 VI 接口； |
| HDMI/eDP TX | 1 **<font style="color:#ff0000;">*</font>**<sup>**<font style="color:#ff0000;">1</font>**</sup> | ·支持1 个 HDMI / eDP TX 组合接口   ·HDMI 接口   ·HDMI v2.1   ·最高支持 4K@120Hz   ·支持数据格式：RGB/YUV444/YUV422/YUV420 8/10-bit   ·支持 CEC和ARC   ·HDCP v2.3 和 HDCP v1.4   ·eDP接口   ·eDP v1.3   ·Main link containing 4 physical lanes   ·最高支持 4K@60Hz   ·HDCP v1.3 |
| DP TX | 1 **<font style="color:#ff0000;">*</font>**<sup>**<font style="color:#ff0000;">1</font>**</sup> | ·支持1 路 USB / DP 组合接口   ·USB 接口   ·USB 3.2 Gen1x1   ·Dual-Role Device(DRD)   ·DisplayPort TX 接口   ·DisplayPort v1.4   · Supports 1/2/4 lanes with lane speed including 1.62、2.7、5.4 and 8.1Gbps   ·支持最高 4K@120Hz   ·支持数据格式：RGB/YUV444/YUV422/YUV420 8/10-bit   ·支持 Multi-Stream Transport (MST) with 3 displays   ·支持 DP Altmode on USB Type-C   ·支持 HDCP v2.3 and HDCP v1.3 |
| MIPI DSI | 1 **<font style="color:#ff0000;">*</font>**<sup>**<font style="color:#ff0000;">1</font>**</sup> | ·支持 1 个MIPI DSI-2 TX 接口   ·D-PHY v2.0 or C-PHY v1.1   ·4 data lanes on D-PHY   ·3 data trios on C-PHY   ·支持最高 2560 x 1600@60Hz   ·支持数据格式：RGB (up to 10bit) |
| Parallel | 1 **<font style="color:#ff0000;">*</font>**<sup>**<font style="color:#ff0000;">1</font>**</sup> | ·支持 1 个并行输出接口   ·支持 RGB/BT.656/BT1120   ·最高支持 1920 x 1080@60Hz   ·支持数据格式：RGB (up to 10bit) |
| EBC | 1 **<font style="color:#ff0000;">*</font>**<sup>**<font style="color:#ff0000;">1</font>**</sup> | ·支持 1 个 EBC 输出接口   ·支持 E-ink EPD (Electronic paper Display)   ·支持 2560 x 1920 硬解码   ·支持数据总线宽度：16-bit   ·支持高达 32 level gray scale   ·支持 Direct mode、LUT mode、3-window mode   ·支持 window display mode |
| SAI | ≤5 | ·支持 5 个 SAI 接口   ·SAI 0/1 支持 4 TX lanes 和 4 RX lanes   ·SAI 2/3/4 支持 1TX lane 和 1 RX lane   ·支持 I2S/TDM/PCM 模式 **<font style="color:#ff0000;">*</font>**<sup>**<font style="color:#ff0000;">2</font>**</sup>   ·支持最高采样率：192KHz   ·支持音频分辨率：16bits 到 32bits |
| SPDIF TX | ≤2 | ·支持 2 路 SPDIF TX 端口 |
| SPDIF RX | ≤2 | ·支持 2 路 SPDIF RX 端口 |
| PDM | ≤2 | ·最高 8 channels，音频分辨率从16 ~24 位，采样率达192KHz   ·支持PDM主接收模式 |
| Ethernet | ≤2 | ·2路GMAC，提供RGMII / RMII接口引出   ·支持10/100/1000Mbps数据传输速率 |
| Combo high speed interface | 2 | ·支持 1 个 PCIe2.1/SATA3.1 interface with one data lane   ·支持 1 个 PCIe2.1/SATA3.1/USB3.2 Gen1x1 interface with one data lane |
| USB 2.0 OTG | 2 | ·支持两路USB2.0 OTG |
| SDIO | ≤2 | ·SDIO v3.0，4-bit data bus widths |
| SPI | ≤5 | ·支持 two chip-select in each interface   ·支持 serial-master 和 serial-slave mode |
| I2C | ≤9 | ·支持7位和10位地址模式   ·标准模式数据传输速率100k bits/s，在快速模式下400k bits/s |
| I3C | ≤2 | ·支持 2 个 I3C master ports |
| UART | ≤12 | ·内置2路64 bit FIFO，可分别用于TX和RX   ·支持5位、6位、7位、8位串行数据收发，波特率高达4Mbps   ·12路UART均支持自动流控模式   ·12路UART均支持RS485模式 |
| CAN | ≤2 | ·遵循 CAN 和 CAN FD 规范   ·支持CAN标准帧和扩展帧收发   ·支持8192-bit receive FIFO |
| DSMC | ≤1 | ·Supports up to select 4 chips   ·Supports 8-wire and 16-wire serial transfer mode   ·Supports configurable serial address width:16 bits or 32 bits |
| FlexBus | ≤1 | ·Supports built-in DMA and ping-pong operation for allocating two address   ·Supports transmission and receiving mode   ·Supports single mode and continuous mode |
| PWM | ≤16 | ·最高支持16个片上PWM，具有基于中断的操作，支持捕获模式 |
| ADC | ≤8 | ·支持8路12bit单端输入SAR-ADC，采样率高达1MS/s |
| GPIO | n | ·所有的 GPIO 可以被用于生成中断   ·支持电平触发和边沿触发中断   ·支持配置电平触发极性   ·支持上升沿触发、下降沿触发和双沿触发中断   ·支持配置上下拉（弱上拉和弱下拉）   ·支持配置驱动能力 |


注：表中参数为硬件设计或CPU理论值。

接口存在GPIO复用，为理论最大数量。

*1 Video Port

·Video Port0 supports up to 4K@120Hz with 10 bit data

  ·Video Port1 supports up to 2560x1600@60Hz with 10-bit data

  ·Video Port2 supports up to 1920x1080@60Hz with 8-bit data

  ·Each Video Port may connect to any of HDMI/eDP/DP/DSI-2

  ·Port1 and Port2 may connect to parallel output interface

*2 单根 TDM 设计时钟最高 50MHz，使用 TDM 模式时，可以结合音频采样频率、分辨率来计算理论可支持的音频通道数，看是否满足项目需求。

## 2.6  FET3576-C核心板引脚定义
### 2.6.1  FET3576-C核心板引脚原理图
![Image](./images/OK3576C_hardware/e97fda686e244204ae690ad984b42cad.png)

![Image](./images/OK3576C_hardware/07499dd7d9234ece9bec4c925c40b2d6.png)

![Image](./images/OK3576C_hardware/7ffe2b4bfcd0456593533b1efb04dd28.png)

![Image](./images/OK3576C_hardware/23bd375a3ddb4c279b4f25c420797a6a.png)



### 2.6.2  FET3576-C核心板引脚功能说明
**注1：**

**    Num —— **核心板连接器引脚序号；

**    Ball —— **CPU引脚球号

**    GPIO —— **CPU引脚通用I/O口序号

**    Vol  ——** 引脚信号电平

**注2：**

**信号名称 ——**核心板连接器网络名称，信号右上角角标含义如下图：

| **角标序号** | **角标含义** |
| :---: | --- |
| [1] | 引脚可配置为中断使用 |
| [2] | 引脚默认电平为1.8V |
| [3] | 引脚为CPU启动相关引脚，不推荐作为IO使用 |
| [4] | 专用引脚，不能作为IO使用 |


**    引脚描述 ——**核心板引脚信号名称描述  

**    默认功能 ——**核心板所有引脚功能均按下表的“默认功能”作了规定，请勿修改，否则可能和出厂 驱动冲突。如有疑问，请及时联系我们的销售或技术支持。

**注3: “默认功能”一栏中标明“底板勿用”的引脚是核心板使用的引脚，底板设计时不可使用**

**表1 P1连接器接口（奇）引脚定义**

| **NUM** | **BALL** | **信号名称** | **GPIO** | **VOL** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| 1 | —— | GND | —— | —— | 地 | GND |
| 3 | B25 | SDMMC_D1 |  | 1.8V/3.3V | SD/MMC接口数据信号1 | SDMMC_D1 |
| 5 | B24 | SDMMC_D0 |  | 1.8V/3.3V | SD/MMC接口数据信号0 | SDMMC_D0 |
| 7 | 1B21 | SDMMC_CLK |  | 1.8V/3.3V | SD/MMC接口时钟信号 | SDMMC_CLK |
| 9 | 1A21 | SDMMC_CMD |  | 1.8V/3.3V | SD/MMC接口命令信号 | SDMMC_CMD |
| 11 | B23 | SDMMC_D3 |  | 1.8V/3.3V | SD/MMC接口数据信号3 | SDMMC_D3 |
| 13 | A23 | SDMMC_D2 |  | 1.8V/3.3V | SD/MMC接口数据信号2 | SDMMC_D2 |
| 15 | —— | GND | —— | —— | 地 | GND |
| 17 | 2U12 | HDMI_TX_SBDN | —— | —— | HDMISBD信号- | HDM0_TX_SBD_N |
| 19 | 2T12 | HDMI_TX_SBDP | —— | —— | HDMISBD信号+ | HDM0_TX_SBD_P |
| 21 | —— | GND | —— | —— | 地 | GND |
| 23 | AK26 | HDMI_TX_D3N | —— | —— | HDMI差分信号3- | HDMI_TX_D3_N |
| 25 | AL26 | HDMI_TX_D3P | —— | —— | HDMI差分信号3+ | HDMI_TX_D3_P |
| 27 | —— | GND | —— | —— | 地 | GND |
| 29 | AK27 | HDMI_TX_D0N | —— | —— | HDMI差分信号0- | HDMI_TX_D0_N |
| 31 | 1AE24 | HDMI_TX_D0P | —— | —— | HDMI差分信号0+ | HDMI_TX_D0_P |
| 33 | —— | GND | —— | —— | 地 | GND |
| 35 | AL28 | HDMI_TX_D1N | —— | —— | HDMI差分信号1- | HDMI_TX_D1_N |
| 37 | AK28 | HDMI_TX_D1P | —— | —— | HDMI差分信号1+ | HDMI_TX_D1_P |
| 39 | —— | GND | —— | —— | 地 | GND |
| 41 | AK29 | HDMI_TX_D2N | —— | —— | HDMI差分信号2- | HDMI_TX_D2_N |
| 43 | AJ28 | HDMI_TX_D2P | —— | —— | HDMI差分信号2+ | HDMI_TX_D2_P |
| 45 | —— | GND | —— | —— | 地 | GND |
| 47 | —— | —— | —— | —— |  |  |
| 49 | —— | —— | —— | —— |  |  |
| 51 | —— | GND | —— | —— | 地 | GND |
| 53 | —— | —— | —— | —— |  |  |
| 55 | —— | —— | —— | —— |  |  |
| 57 | —— | GND | —— | —— | 地 | GND |
| 59 | —— | —— | —— | —— |  |  |
| 61 | —— | —— | —— | —— |  |  |
| 63 | —— | GND | —— | —— | 地 | GND |
| 65 | —— | —— | —— | —— |  |  |
| 67 | —— | —— | —— | —— |  |  |
| 69 | —— | GND | —— | —— | 地 | GND |
| 71 | —— | —— | —— | —— |  |  |
| 73 | —— | —— | —— | —— |  |  |
| 75 | —— | GND | —— | —— | 地 | GND |
| 77 | —— | —— | —— | —— |  |  |
| 79 | —— | —— | —— | —— |  |  |
| 81 | —— | GND | —— | —— | 地 | GND |
| 83 | —— | —— | —— | —— |  |  |
| 85 | —— | —— | —— | —— |  |  |
| 87 | —— | GND | —— | —— | 地 | GND |
| 89 | —— | —— | —— | —— |  |  |
| 91 | —— | —— | —— | —— |  |  |
| 93 | —— | GND | —— | —— | 地 | GND |
| 95 | —— | —— | —— | —— |  |  |
| 97 | —— | —— | —— | —— |  |  |
| 99 | —— | GND | —— | —— | 地 | GND |


**表2 P1连接器接口（偶）引脚定义**

| **NUM** | **BALL** | **信号名称** | **GPIO** | **VOL** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| 2 | —— | GND | —— | —— | 地 | GND |
| 4 | —— | —— | —— | —— | —— | —— |
| 6 | —— | —— | —— | —— | —— | —— |
| 8 | —— | GND | —— | —— | 地 | GND |
| 10 | —— | —— | —— | —— | —— | —— |
| 12 | —— | —— | —— | —— | —— | —— |
| 14 | —— | GND | —— | —— | 地 | GND |
| 16 | —— | —— | —— | —— | —— | —— |
| 18 | —— | —— | —— | —— | —— | —— |
| 20 | —— | GND | —— | —— | 地 | GND |
| 22 | —— | —— | —— | —— | —— | —— |
| 24 | —— | —— | —— | —— | —— | —— |
| 26 | —— | GND | —— | —— | 地 | GND |
| 28 | A25 | SARADC_VIN0_BOOT | —— | 1.8V | BOOT启动配置输入 | SARADC_VIN0_BOOT |
| 30 | 1A22 | SARADC_VIN1_KEY/RECOVERY | —— | 1.8V | <font style="color:rgb(255, 0, 0);">通用ADC1</font> | SARADC_VIN1_KEY/RECOVERY |
| 32 | 1B19 | SARADC_VIN2_HW_ID | —— | 1.8V | 通用ADC2 | SARADC_VIN2_HW_ID |
| 34 | 1C19 | SARADC_VIN3_HP_HOOK | —— | 1.8V | <font style="color:rgb(255, 0, 0);">通用ADC3</font> | SARADC_VIN3_HP_HOOK |
| 36 | 1E18 | SARADC_VIN4 | —— | 1.8V | 通用ADC4 | SARADC_VIN4 |
| 38 | 1D19 | SARADC_VIN5 | —— | 1.8V | 通用ADC5 | SARADC_VIN5 |
| 40 | 1D21 | SARADC_VIN6 | —— | 1.8V | 通用ADC6 | SARADC_VIN6 |
| 42 | 1E19 | SARADC_VIN7_LCD_ID | —— | 1.8V | 通用ADC7 | SARADC_VIN7_LCD_ID |
| 44 | —— | GND | —— | —— | 地 | GND |
| 46 | B19 | HDMI_TX_ON_H |  | 3.3V | HDMI_TX开启信号 | HDMI_TX_ON_H |
| 48 | B20 | TYPEC_DPTX_AUX_PUPDCTL2 |  | 3.3V | TYPEC_DPTX_AUX_PUPDCTL22信号 | TYPEC_DPTX_AUX_PUPDCTL2 |
| 50 | 1C18 | GPIO2_B5_d |  | 3.3V | USB_HUB_RST_3V3复位信号 | USB_HUB_RST_3V3 |
| 52 | AK3 | HDMI_TX_CEC_M0 |  | 3.3V | HDMICEC信号 | HDMI_TX_CEC_M0 |
| 54 | 1A19 | CAN1_RX_M3 |  | 3.3V | CAN1数据接收 | CAN1_RX_M3_3V3 |
| 56 | A21 | I2C8_SCL_M2 |  | 3.3V | I2C8时钟 | I2C8_SCL_M2 |
| 58 | 1AE2 | HDMI_TX_SDA |  | 3.3V | HDMI串行数据 | HDMI_TX_SDA |
| 60 | B21 | I2C8_SDA_M2 |  | 3.3V | I2C8数据 | I2C8_SDA_M2 |
| 62 | —— | GND | —— | —— | 地 | GND |
| 64 | A19 | PCIE0_PERSTn |  | 3.3V | PCIE复位信号 | PCIE0_PERSTn |
| 66 | 1A20 | CAN1_TX_M3 |  | 3.3V | CAN1数据发送 | CAN1_TX_M3_3V3 |
| 68 | AL2 | HDMI_TX_SCL |  | 3.3V | HDMI串行时钟 | HDMI_TX_SCL |
| 70 | 1D16 | I2C7_SCL_M1 |  | 3.3V | I2C7时钟 | I2C7_SCL_M1 |
| 72 | 1B18 | I2C7_SDA_M1 |  | 3.3V | I2C7数据 | I2C7_SDA_M1 |
| 74 | 1Y22 | PCIE0_WAKEn_M0 |  | 3.3V | PCIE唤醒激活信号 | PCIE0_WAKEn_M0 |
| 76 | 1B16 | GPIO2_B3_d |  | 3.3V | 4G/5G模组复位信号 | 4G/5G_PWREN |
| 78 | 1A17 | PCIE0_CLKREQn_M0 |  | 3.3V | PCIE时钟请求信号 | PCIE0_CLKREQn_M0 |
| 80 | 1A18 | GPIO2_B1_d |  | 3.3V | 4G/5G模组电源控制信号 | 4G/5G_MOD_PWREN |
| 82 | B22 | TYPEC_DPTX_AUX_PUPDCTL1 |  | 3.3V | TYPEC_DPTX_AUX_PUPDCTL1信号 | TYPEC_DPTX_AUX_PUPDCTL1 |
| 84 | —— | GND | —— | —— | 地 | GND |
| 86 | —— | —— | —— | —— | —— | —— |
| 88 | —— | —— | —— | —— | —— | —— |
| 90 | —— | GND | —— | —— | 地 | GND |
| 92 | 2T4 | USB2_HOST1_DP | —— | —— | USB20_HOST1数据+ | USB20_HOST1_D_P |
| 94 | 2T5 | USB2_HOST1_DM | —— | —— | USB20_HOST1数据- | USB20_HOST1_D_N |
| 96 | —— | GND | —— | —— | 地 | GND |
| 98 | 2T9 | USB2_OTG1_ID | —— | —— | USB2_OTG1_ID信号 | x |
| 100 | 2T10 | USB2_OTG1_VBUSDET | —— | —— | USB2_OTG1_VBUSDET插入检测 | USB2_OTG1_VBUSDET |


**表3 P2连接器接口（奇）引脚定义**

| **NUM** | **BALL** | **信号名称** | **GPIO** | **VOL** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| 1 | AB29 | I2C2_SDA_M0 |  | 3.3V | I2C2数据 | I2C2_SDA_M0 |
| 3 | 1W21 | PWM0_CH1_M0 |  | 3.3V | PWM0_CH1_M0 | x |
| 5 | AD28 | PWM1_CH0_M0 |  | 3.3V | PWM1_CH0_M0 | x |
| 7 | 1U24 | UART0_TX_M0_DEBUG |  | 3.3V | UART0发送 | UART0_TX_M0_DEBUG |
| 9 | AA28 | UART0_RX_M0_DEBUG |  | 3.3V | UART0接收 | UART0_RX_M0_DEBUG |
| 11 | 1W24 | I2C2_SCL_M0 |  | 3.3V | I2C2时钟 | I2C2_SCL_M0 |
| 13 | 1W22 | PWM0_CH0_M0 |  | 3.3V | PWM0_CH0_M0 | PWM0_CH0_M0(MIPI屏幕背光PWM) |
| 15 | —— | GND | —— | —— | 地 | GND |
| 17 | —— | —— | —— | —— | —— | —— |
| 19 | 1E21 | GPIO3_D4_d | GPIO3_D4_d | 1.8V | GMAC1_INT中断 | GMAC1_INT |
| 21 | 1D10 | GPIO3_D5_d | GPIO3_D5_d | 1.8V | GMAC1_RESET复位 | GMAC1_RESET |
| 23 | —— | —— | —— | —— | —— | —— |
| 25 | —— | —— | —— | —— | —— | —— |
| 27 | —— | —— | —— | —— | —— | —— |
| 29 | 1AA23 | GPIO0_D3_d_1V8 |  | 1.8V | HP_DET_L耳机插入检测 | HP_DET_L(headphone) |
| 31 | 1D9 | I2C5_SCL_M3 |  | 1.8V | I2C5时钟 | I2C5_SCL_M3 |
| 33 | 1B10 | I2C5_SDA_M3 |  | 1.8V | I2C5数据 | I2C5_SDA_M3 |
| 35 | 1A4 | I2C3_SCL_M0 |  | 1.8V | I2C3时钟 | I2C3_SCL_M0 |
| 37 | 1B7 | CAM_CLK2_OUT_M0 |  | 1.8V | CAM_CLK2_OUT_M0 | x |
| 39 | 1A5 | UART5_TX_M1 |  | 1.8V | UART5发送数据 | UART5_TX_M1_1V8 |
| 41 | 1B12 | CAM_CLK1_OUT_M0 |  | 1.8V | CAM_CLK1_OUT_M0 | x |
| 43 | B8 | I2C3_SDA_M0 |  | 1.8V | I2C3数据 | I2C3_SDA_M0 |
| 45 | 1E7 | CAM_CLK0_OUT_M0 |  | 1.8V | CAM_CLK0_OUT_M0 | x |
| 47 | —— | —— | —— | —— | —— | —— |
| 49 | A7 | SAI1_SDO0_M0 |  | 1.8V | I2S 数据输出数据 | SAI1_SDO0_M0 |
| 51 | 1C10 | GPIO3_D6_d |  | 1.8V | 4G/5G 复位 | 4G/5G_RESET |
| 53 | 1B6 | SAI1_LRCK_M0 |  | 1.8V | I2S 发送帧时钟 | SAI1_LRCK_M0 |
| 55 | 1C6 | SAI1_SCLK_M0 |  | 1.8V | I2S 位时钟 | SAI1_SCLK_M0 |
| 57 | —— | —— | —— | —— | —— | —— |
| 59 | 1A6 | SAI1_SDI0_M0 |  | 1.8V | I2S 数据输入数据 | SAI1_SDI0_M0 |
| 61 | B7 | UART5_RX_M1 |  | 1.8V | UART5接收数据 | UART5_RX_M1_1V8 |
| 63 | —— | GND | —— | —— | 地 | GND |
| 65 | 1D6 | SAI1_MCLK_M0 |  | 1.8V | I2S 主时钟 | SAI1_MCLK_M0 |
| 67 | V29 | GPIO0_A0_d |  | 1.8V | IIC中断 | IIC_GPIO_INT |
| 69 | 1B9 | UART8_RX_M0 |  | 1.8V | UART8接收数据 | UART8_RX_M0_1V8 |
| 71 | AK2 | HDMI_TX_HPDIN_M0_1V8 |  | 1.8V | HDMI发送链接检测 | HDMI_TX_HPDIN_M0_1V8 |
| 73 | 1D7 | UART8_TX_M0 |  | 1.8V | UART8发送数据 | UART8_TX_M0_1V8 |
| 75 | Y29 | GPIO0_A5_d |  | 1.8V | TYPEC0中断 | TYPEC0_INT |
| 77 | 1C7 | UART8_RTSN_M0 |  | 1.8V | UART8请求发送 | UART8_RTSN_M0_1V8 |
| 79 | 1C12 | UART8_CTSN_M0 |  | 1.8V | UART8清除发送 | UART8_CTSN_M0_1V8 |
| 81 | —— | GND | —— | —— | 地 | GND |
| 83 | 1L23 | PCIE1_REFCLKP | —— | —— | PCIE1时钟输出/输入+ | x |
| 85 | 1M23 | PCIE1_REFCLKN | —— | —— | PCIE1时钟输出/输入- | x |
| 87 | —— | GND | —— | —— | 地 | GND |
| 89 | N28 | PCIE1_TXP/USB3_HOST1_SSTXP | —— | —— | USB3_HOST1发送差分+ | USB3_HOST1_SSTXP |
| 91 | N29 | PCIE1_TXN/USB3_HOST1_SSTXN | —— | —— | USB3_HOST1发送差分- | USB3_HOST1_SSTXN |
| 93 | —— | GND | —— | —— | 地 | GND |
| 95 | M28 | PCIE1_RXP/USB3_HOST1_SSRXP | —— | —— | USB3_HOST1接收差分+ | USB3_HOST1_SSRXP |
| 97 | M29 | PCIE1_RXN/USB3_HOST1_SSRXN | —— | —— | USB3_HOST1接收差分- | USB3_HOST1_SSRXN |
| 99 | —— | GND | —— | —— | 地 | GND |


**表4 P2连接器接口（偶）引脚定义**

| **NUM** | **BALL** | **信号名称** | **GPIO** | **VOL** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| 2 | —— | GND | —— | —— | 地 | GND |
| 4 | —— | —— | —— | —— | —— | —— |
| 6 | —— | —— | —— | —— | —— | —— |
| 8 | —— | GND | —— | —— | 地 | GND |
| 10 | —— | —— | —— | —— | —— | —— |
| 12 | —— | —— | —— | —— | —— | —— |
| 14 | —— | GND | —— | —— | 地 | GND |
| 16 | —— | —— | —— | —— | —— | —— |
| 18 | —— | —— | —— | —— | —— | —— |
| 20 | —— | GND | —— | —— | 地 | GND |
| 22 | —— | —— | —— | —— | —— | —— |
| 24 | —— | —— | —— | —— | —— | —— |
| 26 | —— | GND | —— | —— | 地 | GND |
| 28 | —— | —— | —— | —— | —— | —— |
| 30 | —— | —— | —— | —— | —— | —— |
| 32 | —— | GND | —— | —— | 地 | GND |
| 34 | —— | —— | —— | —— | —— | —— |
| 36 | —— | —— | —— | —— | —— | —— |
| 38 | —— | GND | —— | —— | 地 | GND |
| 40 | —— | —— | —— | —— | —— | —— |
| 42 | —— | —— | —— | —— | —— | —— |
| 44 | —— | GND | —— | —— | 地 | GND |
| 46 | —— | —— | —— | —— | —— | —— |
| 48 | —— | —— | —— | —— | —— | —— |
| 50 | —— | GND | —— | —— | 地 | GND |
| 52 | —— | —— | —— | —— | —— | —— |
| 54 | —— | —— | —— | —— | —— | —— |
| 56 | —— | GND | —— | —— | 地 | GND |
| 58 | —— | —— | —— | —— | —— | —— |
| 60 | —— | —— | —— | —— | —— | —— |
| 62 | —— | GND | —— | —— | 地 | GND |
| 64 | 1N23 | PCIE0_REFCLKN | —— | —— | PCIE0时钟输出/输入- | PCIE0_REFCLKN |
| 66 | 1N22 | PCIE0_REFCLKP | —— | —— | PCIE0时钟输出/输入+ | PCIE0_REFCLKP |
| 68 | —— | GND | —— | —— | 地 | GND |
| 70 | R29 | PCIE0_RXN/SATA0_RXN | —— | —— | PCIE0数据接收- | PCIE0_RXN |
| 72 | R28 | PCIE0_RXP/SATA0_RXP | —— | —— | PCIE0数据接收+ | PCIE0_RXP |
| 74 | —— | GND | —— | —— | 地 | GND |
| 76 | P28 | PCIE0_TXN/SATA0_TXN | —— | —— | PCIE0数据发送- | PCIE0_TXN |
| 78 | P29 | PCIE0_TXP/SATA0_TXP | —— | —— | PCIE0数据发送+ | PCIE0_TXP |
| 80 | —— | GND | —— | —— | 地 | GND |
| 82 | —— | —— | —— | —— | —— | —— |
| 84 | —— | —— | —— | —— | —— | —— |
| 86 | —— | GND | —— | —— | 地 | GND |
| 88 | —— | —— | —— | —— | —— | —— |
| 90 | —— | —— | —— | —— | —— | —— |
| 92 | —— | GND | —— | —— | 地 | GND |
| 94 | —— | —— | —— | —— | —— | —— |
| 96 | —— | —— | —— | —— | —— | —— |
| 98 | —— | GND | —— | —— | 地 | GND |
| 100 | —— | RESET_L | —— | —— | 复位 | RESET_L |


**表5 P3连接器接口（奇）引脚定义**

| **NUM** | **BALL** | **信号名称** | **GPIO** | **VOL** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| 1 | —— | GND | —— | —— | 地 | GND |
| 3 | AL10 | USB3_OTG0_SSRX1N/DP_TX_D0N | —— | —— | USB3_OTG0_SSRX1N接收差分信号1- | USB3_OTG0_SSRX1N |
| 5 | AK10 | USB3_OTG0_SSRX1P/DP_TX_D0P | —— | —— | USB3_OTG0_SSRX1P接收差分信号1+ | USB3_OTG0_SSRX1P |
| 7 | —— | GND | —— | —— | 地 | GND |
| 9 | AL11 | USB3_OTG0_SSTX1P/DP_TX_D1P | —— | —— | USB3_OTG0_SSTX1P发送差分信号1+ | USB3_OTG0_SSTX1P |
| 11 | AK11 | USB3_OTG0_SSTX1N/DP_TX_D1N | —— | —— | USB3_OTG0_SSTX1N发送差分信号1- | USB3_OTG0_SSTX1N |
| 13 | —— | GND | —— | —— | 地 | GND |
| 15 | AL12 | USB3_OTG0_SSRX2N/DP_TX_D2N | —— | —— | USB3_OTG0_SSRX2N接收差分信号2- | USB3_OTG0_SSRX2N |
| 17 | AK12 | USB3_OTG0_SSRX2P/DP_TX_D2P | —— | —— | USB3_OTG0_SSRX2P接收差分信号2+ | USB3_OTG0_SSRX2P |
| 19 | —— | GND | —— | —— | 地 | GND |
| 21 | AL13 | USB3_OTG0_SSTX2P/DP_TX_D3P | —— | —— | USB3_OTG0_SSTX2P发送差分信号2+ | USB3_OTG0_SSTX2P |
| 23 | AK13 | USB3_OTG0_SSTX2N/DP_TX_D3N | —— | —— | USB3_OTG0_SSTX2N发送差分信号2- | USB3_OTG0_SSTX2N |
| 25 | —— | GND | —— | —— | 地 | GND |
| 27 | B27 | SDMMC1_D1_M0 |  | 1.8V | SD/MMC接口数据信号1 | SDMMC1_D1_M0 |
| 29 | A28 | SDMMC1_D0_M0 |  | 1.8V | SD/MMC接口数据信号0 | SDMMC1_D0_M0 |
| 31 | —— | GND | —— | —— | 地 | GND |
| 33 | 1B22 | SDMMC1_CLK_M0 |  | 1.8V | SD/MMC接口时钟信号 | SDMMC1_CLK_M0 |
| 35 | B26 | SDMMC1_CMD_M0 |  | 1.8V | SD/MMC接口命令信号 | SDMMC1_CMD_M0 |
| 37 | —— | GND | —— | —— | 地 | GND |
| 39 | A27 | SDMMC1_D3_M0 |  | 1.8V | SD/MMC接口数据信号3 | SDMMC1_D3_M0 |
| 41 | 1A23 | SDMMC1_D2_M0 |  | 1.8V | SD/MMC接口数据信号2 | SDMMC1_D2_M0 |
| 43 | —— | GND | —— | —— | 地 | GND |
| 45 | C29 | SAI2_SDO_M0 |  | 1.8V | I2S数据输出数据 | SAI2_SDO_M0 |
| 47 | 1D22 | SAI2_SCLK_M0 |  | 1.8V | I2S位时钟 | SAI2_SCLK_M0 |
| 49 | —— | GND | —— | —— | 地 | GND |
| 51 | 1A24 | SAI2_LRCK_M0 |  | 1.8V | I2S发送帧时钟 | SAI2_LRCK_M0 |
| 53 | C28 | SAI2_SDI_M0 |  | 1.8V | I2S数据输入数据 | SAI2_SDI_M0 |
| 55 | —— | GND | —— | —— | 地 | GND |
| 57 | AK15 | MIPI_DPHY_DSI_TX_D0N | —— | —— | MIPI_DPHY_DSI发送数据0- | MIPI_DPHY_DSI_TX_D0N |
| 59 | AL15 | MIPI_DPHY_DSI_TX_D0P | —— | —— | MIPI_DPHY_DSI发送数据0+ | MIPI_DPHY_DSI_TX_D0P |
| 61 | —— | GND | —— | —— | 地 | GND |
| 63 | AK16 | MIPI_DPHY_DSI_TX_D1N | —— | —— | MIPI_DPHY_DSI发送数据1- | MIPI_DPHY_DSI_TX_D1N |
| 65 | AL16 | MIPI_DPHY_DSI_TX_D1P | —— | —— | MIPI_DPHY_DSI发送数据1+ | MIPI_DPHY_DSI_TX_D1P |
| 67 | —— | GND | —— | —— | 地 | GND |
| 69 | AL17 | MIPI_DPHY_DSI_TX_CLKN | —— | —— | MIPI_DPHY_DSI发送时钟- | MIPI_DPHY_DSI_TX_CLKN |
| 71 | AL17 | MIPI_DPHY_DSI_TX_CLKP | —— | —— | MIPI_DPHY_DSI发送时钟+ | MIPI_DPHY_DSI_TX_CLKP |
| 73 | —— | GND | —— | —— | 地 | GND |
| 75 | AK18 | MIPI_DPHY_DSI_TX_D2N | —— | —— | MIPI_DPHY_DSI发送数据2- | MIPI_DPHY_DSI_TX_D2N |
| 77 | AL18 | MIPI_DPHY_DSI_TX_D2P | —— | —— | MIPI_DPHY_DSI发送数据2+ | MIPI_DPHY_DSI_TX_D2P |
| 79 | —— | GND | —— | —— | 地 | GND |
| 81 | AK19 | MIPI_DPHY_DSI_TX_D3N | —— | —— | MIPI_DPHY_DSI发送数据3- | MIPI_DPHY_DSI_TX_D3N |
| 83 | AL19 | MIPI_DPHY_DSI_TX_D3P | —— | —— | MIPI_DPHY_DSI发送数据3+ | MIPI_DPHY_DSI_TX_D3P |
| 85 | —— | GND | —— | —— | 地 | GND |
| 87 |  | CARRIER_BOARD_EN | —— | —— | CARRIER使能 | CARRIER_BOARD_EN |
| 89 | —— | GND | —— | —— | 地 | GND |
| 91 |  | VCC12V_DCIN | —— | —— | 12V电源输入 | VCC12V_DCIN |
| 93 |  | VCC12V_DCIN | —— | —— | 12V电源输入 | VCC12V_DCIN |
| 95 |  | VCC12V_DCIN | —— | —— | 12V电源输入 | VCC12V_DCIN |
| 97 |  | VCC12V_DCIN | —— | —— | 12V电源输入 | VCC12V_DCIN |
| 99 |  | VCC12V_DCIN | —— | —— | 12V电源输入 | VCC12V_DCIN |


**表6 P3连接器接口（偶）引脚定义**

| **NUM** | **BALL** | **信号名称** | **GPIO** | **VOL** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| 2 | —— | GND | —— | —— | 地 | GND |
| 4 | —— | —— | —— | —— | —— | —— |
| 6 | —— | —— | —— | —— | —— | —— |
| 8 | —— | —— | —— | —— | —— | —— |
| 10 | —— | —— | —— | —— | —— | —— |
| 12 | —— | GND | —— | —— | 地 | GND |
| 14 | 2R6 | USB2_OTG0_ID | —— | —— | USB2_OTG0_ID信号 | X |
| 16 | 2P3 | USB2_OTG0_VBUSDET | —— | —— | USB2_OTG0_VBUSDET插入检测 | USB2_OTG0_VBUSDET |
| 18 | AL9 | USB2_OTG0_DM | —— | —— | USB2_OTG0_DM数据- | USB2_OTG0_DM |
| 20 | AK9 | USB2_OTG0_DP | —— | —— | USB2_OTG0_DP数据+ | USB2_OTG0_DP |
| 22 | 2T2 | DP_TX_AUXP | —— | —— | DP_TX_AUXP信号 | DP_TX_AUXP |
| 24 | 2T3 | DP_TX_AUXN | —— | —— | DP_TX_AUXN信号 | DP_TX_AUXN |
| 26 | —— | GND | —— | —— | 地 | GND |
| 28 | 1B23 | UART4_TX_M1 | —— | 1.8V | UART4发送数据 | UART4_TX_M1 |
| 30 | B28 | UART4_RX_M1 | —— | 1.8V | UART4接收数据 | UART4_RX_M1 |
| 32 | —— | GND | —— | —— | 地 | GND |
| 34 | B29 | UART4_RTSN_M1 | —— | 1.8V | UART4请求发送 | UART4_RTSN_M1 |
| 36 | 1C23 | UART4_CTSN_M1 | —— | 1.8V | UART4清除发送 | UART4_CTSN_M1 |
| 38 | —— | GND | —— | —— | 地 | GND |
| 40 | A26 | WIFI_REG_ON_H | —— | 1.8V | WIFI_REG_ON_H信号 | WIFI_REG_ON_H |
| 42 | 1C22 | BT_REG_ON_H | —— | 1.8V | BT_REG_ON_H信号 | BT_REG_ON_H |
| 44 | —— | GND | —— | —— | 地 | GND |
| 46 | 1E21 | HOST_WAKE_BT_H | —— | 1.8V | HOST_WAKE_BT_H信号 | HOST_WAKE_BT_H |
| 48 | 1E22 | GPIO1_D5_d | —— | 1.8V | GPIO_D5_d_1V8信号 | GPIO_D5_d_1V8 |
| 50 | —— | GND | —— | —— | 地 | GND |
| 52 | 1U22 | WIFI_WAKE_HOST_H | —— | 1.8V | WIFI_WAKE_HOST_H信号 | WIFI_WAKE_HOST_H |
| 54 | 1P23 | BT_WAKE_HOST_H | —— | 1.8V | BT_WAKE_HOST_H信号 | BT_WAKE_HOST_H |
| 56 | —— | GND | —— | —— | 地 | GND |
| 58 | AK20 | MIPI_DPHY_CSI0_RX_D0P/MIPI_CPHY_CSI_RX_TRIO0_B | —— | —— | MIPI_DPHY_CSI0_RX_D0P接收数据0+ | MIPI_DPHY_CSI0_RX_D0P |
| 60 | AL20 | MIPI_DPHY_CSI0_RX_D0N/MIPI_CPHY_CSI_RX_TRIO0_A | —— | —— | MIPI_DPHY_CSI0_RX_D0N接收数据0- | MIPI_DPHY_CSI0_RX_D0N |
| 62 | —— | GND | —— | —— | 地 | GND |
| 64 | AK21 | MIPI_DPHY_CSI0_RX_D1P/MIPI_CPHY_CSI_RX_TRIO1_A | —— | —— | MIPI_DPHY_CSI0_RX_D1P接收数据1+ | MIPI_DPHY_CSI0_RX_D1P |
| 66 | AL21 | MIPI_DPHY_CSI0_RX_D1N/MIPI_CPHY_CSI_RX_TRIO0_C | —— | —— | MIPI_DPHY_CSI0_RX_D1N接收数据1- | MIPI_DPHY_CSI0_RX_D1N |
| 68 | —— | GND | —— | —— | 地 | GND |
| 70 | AK22 | MIPI_DPHY_CSI0_RX_CLKP/MIPI_CPHY_CSI_RX_TRIO1_C | —— | —— | MIPI_DPHY_CSI0_RX_CLKP接收时钟+ | MIPI_DPHY_CSI0_RX_CLKP |
| 72 | AL22 | MIPI_DPHY_CSI0_RX_CLKN/MIPI_CPHY_CSI_RX_TRIO1_B | —— | —— | MIPI_DPHY_CSI0_RX_CLKN接收时钟- | MIPI_DPHY_CSI0_RX_CLKN |
| 74 | —— | GND | —— | —— | 地 | GND |
| 76 | AK23 | MIPI_DPHY_CSI0_RX_D2P/MIPI_CPHY_CSI_RX_TRIO2_B | —— | —— | MIPI_DPHY_CSI0_RX_D2P接收数据2+ | MIPI_DPHY_CSI0_RX_D2P |
| 78 | AL23 | MIPI_DPHY_CSI0_RX_D2N/MIPI_CPHY_CSI_RX_TRIO2_A | —— | —— | MIPI_DPHY_CSI0_RX_D2N接收数据2- | MIPI_DPHY_CSI0_RX_D2N |
| 80 | —— | GND | —— | —— | 地 | GND |
| 82 | AK24 | MIPI_DPHY_CSI0_RX_D3P/NO_USE | —— | —— | MIPI_DPHY_CSI0_RX_D3P接收数据3+ | MIPI_DPHY_CSI0_RX_D3P |
| 84 | AL24 | MIPI_DPHY_CSI0_RX_D3N/MIPI_CPHY_CSI_RX_TRIO2_C | —— | —— | MIPI_DPHY_CSI0_RX_D3N接收数据3- | MIPI_DPHY_CSI0_RX_D3N |
| 86 | —— | GND | —— | —— | 地 | GND |
| 88 | —— | PWRON_L | —— | —— | 上电控制 | PWRON_L |
| 90 | 1U21 | SDMMC0_DET_L |  | 1.8V | SDMMC卡检测信号 | SDMMC_DET_L |
| 92 | B6 | GPIO4_B2_d | GPIO4_B2_d | 1.8V | GMAC0复位 | GMAC0_RESET |
| 94 | 1U23 | GPIO0_A2_d | GPIO0_A2_d | 1.8V | GMAC0中断 | GMAC0_INT |
| 96 | —— | GND | —— | —— | 地 | GND |
| 98 | —— | VCC12V_DCIN | —— | —— | 12V电源输入 | VCC12V_DCIN |
| 100 | —— | VCC12V_DCIN | —— | —— | 12V电源输入 | VCC12V_DCIN |


**表7 P4连接器接口（奇）引脚定义**

| **NUM** | **BALL** | **信号名称** | **GPIO** | **VOL** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | --- | :---: | --- | :---: |
| 1 | 1AA22 | GPIO0_C5_d | GPIO0_C5_d | 3.3V | MIPI_DSI1中断 | MIPI_DSI1_INT |
| 3 | 1Y23 | GPIO0_C7_d | GPIO0_C7_d | 3.3V | PCIE0_PRSN2_3V3热插拔检测 | PCIE0_PRSN2_3V3 |
| 5 | 1B15 | GMAC1_MDIO_M0 |  | 3.3V | GMAC1串行管理数据 | GMAC1_MDIO_M0 |
| 7 | 1B13 | GMAC1_MDC_M0 |  | 3.3V | GMAC1串行管理时钟 | GMAC1_MDC_M0 |
| 9 | 1W23 | GPIO0_D0_d | GPIO0_D0_d | 3.3V | MIPI_DSI1复位 | MIPI_DSI1_RESET |
| 11 | AB28 | I2C0_SCL_M1 |  | 3.3V | I2C0时钟 | I2C0_SCL_M1 |
| 13 | —— | GND | —— | —— | 地 | GND |
| 15 | 1V24 | I2C0_SDA_M1 |  | 3.3V | I2C0数据 | I2C0_SDA_M1 |
| 17 | 1AE1 | GPIO4_C6_d | GPIO4_C6_d | 3.3V | GPIO4_C6_d | GPIO4_C6_d |
| 19 | AJ1 | GPIO4_C7_d | GPIO4_C7_d | 3.3V | MIPI_DSI2复位信号 | PCIE_PWR_EN_3V3 |
| 21 | AL3 | UART6_TX_M3 |  | 3.3V | UART6发送数据 | UART6_TX_M3_3V3 |
| 23 | ALK1 | UART6_RX_M3 |  | 3.3V | UART6接收数据 | UART6_RX_M3_3V3 |
| 25 |  | WIFI_PEN_3V3 |  | 3.3V | WIFI_PEN_3V3使能信号   <font style="background-color:#FFFF00;">(3.3V上拉，未连接GPIO)</font> | WIFI_PEN_3V3 |
| 27 | —— | GND | —— | —— | 地 | GND |
| 29 | 1C5 | CAN0_TX_M2_3V3 |  | 3.3V | CAN0数据发送 | CAN0_TX_M2_3V3 |
| 31 | 1B5 | CAN0_RX_M2_3V3 |  | 3.3V | CAN0数据接收 | CAN0_RX_M2_3V3 |
| 33 | 1Y24 | GPIO0_B6_d | GPIO0_B6_d | 3.3V | TF_PWR_EN_3V3使能信号 | TF_PWR_EN_3V3 |
| 35 | 1D18 | ETH_CLK1_25M_OUT_M0 |  | 3.3V | PHY 25MHz 参考时钟输出 | ETH_CLK1_25M_OUT_M0 |
| 37 | 1E15 | ETH1_MCLK_M0 |  | 3.3V | PHY 125MHz 同步时钟输入 | ETH1_MCLK_M0 |
| 39 | 1Y21 | GPIO0_C6_d | GPIO0_C6_d | 3.3V | MIPI_DSI1使能信号 | MIPI_DSI1_EN |
| 41 | —— | GND | —— | —— | 地 | GND |
| 43 | 1D12 | I2C4_SDA_M3 |  | 1.8V | I2C4数据 | I2C4_SDA_M3 |
| 45 | 1E9 | I2C4_SCL_M3 |  | 1.8V | I2C4时钟 | I2C4_SCL_M3 |
| 47 | A9 | GMAC0_MDIO_M0 |  | 1.8V | GMAC0串行管理数据 | GMAC0_MDIO_M0 |
| 49 | 1A7 | GMAC0_MDC_M0 |  | 1.8V | GMAC0 串行管理时钟 | GMAC0_MDC_M0 |
| 51 | —— | GND | —— | —— | 地 | GND |
| 53 | —— | —— | —— | —— | —— | —— |
| 55 | —— | —— | —— | —— | <font style="color:rgb(255, 0, 0);">——</font> | —— |
| 57 | 1D13 | ETH_CLK0_25M_OUT_M0 |  | 1.8V | PHY 25MHz 参考时钟输出 | ETH_CLK0_25M_OUT_M0 |
| 59 | —— | —— | —— | —— | <font style="color:rgb(255, 0, 0);">——</font> | —— |
| 61 | B14 | ETH0_MCLK_M0 |  | 1.8V | PHY 125MHz 同步时钟输入 | ETH0_MCLK_M0 |
| 63 | —— | GND | —— | —— | 地 | GND |
| 65 | AE28 | MIPI_DPHY_CSI1_RX_D0N | —— | —— | MIPI_DPHY_CSI1_RX_D0N数据接收0- | MIPI_DPHY_CSI1_RX_D0N |
| 67 | AE29 | MIPI_DPHY_CSI1_RX_D0P | —— | —— | MIPI_DPHY_CSI1_RX_D0P数据接收0+ | MIPI_DPHY_CSI1_RX_D0P |
| 69 | —— | GND | —— | —— | 地 | GND |
| 71 | AF28 | MIPI_DPHY_CSI1_RX_D1N | —— | —— | MIPI_DPHY_CSI1_RX_D1N数据接收1- | MIPI_DPHY_CSI1_RX_D1N |
| 73 | AF29 | MIPI_DPHY_CSI1_RX_D1P | —— | —— | MIPI_DPHY_CSI1_RX_D1P数据接收1+ | MIPI_DPHY_CSI1_RX_D1P |
| 75 | —— | GND | —— | —— | 地 | GND |
| 77 | 1AC23 | MIPI_DPHY_CSI1_RX_CLKN | —— | —— | MIPI_DPHY_CSI1_RX_CLKN时钟- | MIPI_DPHY_CSI1_RX_CLKN |
| 79 | 1AC22 | MIPI_DPHY_CSI1_RX_CLKP | —— | —— | MIPI_DPHY_CSI1_RX_CLKP时钟+ | MIPI_DPHY_CSI1_RX_CLKP |
| 81 | —— | GND | —— | —— | 地 | GND |
| 83 | AG28 | MIPI_DPHY_CSI1_RX_D2N/   MIPI_DPHY_CSI2_RX_D0N | —— | —— | MIPI_DPHY_CSI2_RX_D0N数据接收0- | MIPI_DPHY_CSI2_RX_D0N |
| 85 | AG29 | MIPI_DPHY_CSI1_RX_D2P/   MIPI_DPHY_CSI2_RX_D0P | —— | —— | MIPI_DPHY_CSI2_RX_D0P数据接收0+ | MIPI_DPHY_CSI2_RX_D0P |
| 87 | —— | GND | —— | —— | 地 | GND |
| 89 | AH28 | MIPI_DPHY_CSI1_RX_D3N/   MIPI_DPHY_CSI2_RX_D1N | —— | —— | MIPI_DPHY_CSI2_RX_D1N数据接收1- | MIPI_DPHY_CSI2_RX_D1N |
| 91 | AH29 | MIPI_DPHY_CSI1_RX_D3P/   MIPI_DPHY_CSI2_RX_D1P | —— | —— | MIPI_DPHY_CSI2_RX_D1P数据接收1+ | MIPI_DPHY_CSI2_RX_D1P |
| 93 | —— | GND | —— | —— | 地 | GND |
| 95 | 1AD22 | MIPI_DPHY_CSI2_RX_CLKN | —— | —— | MIPI_DPHY_CSI2_RX_CLKN时钟- | MIPI_DPHY_CSI2_RX_CLKN |
| 97 | 1AD21 | MIPI_DPHY_CSI2_RX_CLKN | —— | —— | MIPI_DPHY_CSI2_RX_CLKN时钟+ | MIPI_DPHY_CSI2_RX_CLKN |
| 99 | —— | GND | —— | —— | 地 | GND |


**表8 P4连接器接口（偶）引脚定义**

| **NUM** | **BALL** | **信号名称** | **GPIO** | **VOL** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| 2 | AD29 | PWM1_CH1_M0 |  | 3.3V | PWM1 | x |
| 4 | AC28 | GPIO0_D1_d |  | 3.3V | TYPEC使能 | TYPEC0_PWREN |
| 6 | —— | —— | —— | —— | —— | —— |
| 8 | —— | GND | —— | —— | 地 | GND |
| 10 | B9 | GMAC0_TXD3_M0 |  | 1.8V | GMAC0 数据发送 3 | GMAC0_TXD3_M0 |
| 12 | 1A8 | GMAC0_TXD2_M0 |  | 1.8V | GMAC0 数据发送 2 | GMAC0_TXD2_M0 |
| 14 | B10 | GMAC0_TXD1_M0 |  | 1.8V | GMAC0 数据发送 1 | GMAC0_TXD1_M0 |
| 16 | 1A9 | GMAC0_TXD0_M0 |  | 1.8V | GMAC0 数据发送 0 | GMAC0_TXD0_M0 |
| 18 | A11 | GMAC0_TXCTL_M0 |  | 1.8V | GMAC0 发送控制 | GMAC0_TXCTL_M0 |
| 20 | B11 | GMAC0_TXCLK_M0 |  | 1.8V | GMAC0 发送时钟 | GMAC0_TXCLK_M0 |
| 22 | —— | GND | —— | —— | 地 | GND |
| 24 | 1A10 | GMAC0_RXD3_M0 |  | 1.8V | GMAC0接收数据 3 | GMAC0_RXD3_M0 |
| 26 | B12 | GMAC0_RXD2_M0 |  | 1.8V | GMAC0 接收数据 2 | GMAC0_RXD2_M0 |
| 28 | 1A11 | GMAC0_RXD1_M0 |  | 1.8V | GMAC0接收数据 1 | GMAC0_RXD1_M0 |
| 30 | A13 | GMAC0_RXD0_M0 |  | 1.8V | GMAC0 接收数据 0 | GMAC0_RXD0_M0 |
| 32 | B13 | GMAC0_RXCTL_M0 |  | 1.8V | GMAC0 接收控制 | GMAC0_RXCTL_M0 |
| 34 | 1A12 | GMAC0_RXCLK_M0 |  | 1.8V | GMAC0 接收时钟 | GMAC0_RXCLK_M0 |
| 36 | —— | GND | —— | —— | 地 | GND |
| 38 | 1A13 | GMAC1_TXD3_M0 |  | 3.3V | GMAC1数据发送 3 | GMAC1_TXD3_M0 |
| 40 | A15 | GMAC1_TXD2_M0 |  | 3.3V | GMAC1 数据发送 2 | GMAC1_TXD2_M0 |
| 42 | B15 | GMAC1_TXD1_M0 |  | 3.3V | GMAC1 数据发送 1 | GMAC1_TXD1_M0 |
| 44 | 1A14 | GMAC1_TXD0_M0 |  | 3.3V | GMAC1 数据发送 0 | GMAC1_TXD0_M0 |
| 46 | B16 | GMAC1_TXCTL_M0 |  | 3.3V | GMAC1 发送控制 | GMAC1_TXCTL_M0 |
| 48 | 1C15 | GMAC1_TXCLK_M0 |  | 3.3V | GMAC1 发送时钟 | GMAC1_TXCLK_M0 |
| 50 | —— | GND | —— | —— | 地 | GND |
| 52 | 1A15 | GMAC1_RXD3_M0 |  | 3.3V | GMAC1接收数据 3 | GMAC1_RXD3_M0 |
| 54 | A17 | GMAC1_RXD2_M0 |  | 3.3V | GMAC1 接收数据 2 | GMAC1_RXD2_M0 |
| 56 | B17 | GMAC1_RXD1_M0 |  | 3.3V | GMAC1接收数据 1 | GMAC1_RXD1_M0 |
| 58 | 1A16 | GMAC1_RXD0_M0 |  | 3.3V | GMAC1接收数据 0 | GMAC1_RXD0_M0 |
| 60 | B18 | GMAC1_RXCTL_M0 |  | 3.3V | GMAC1接收控制 | GMAC1_RXCTL_M0 |
| 62 | 1D15 | GMAC1_RXCLK_M0 |  | 3.3V | GMAC1 接收时钟 | GMAC1_RXCLK_M0 |
| 64 | —— | GND | —— | —— | 地 | GND |
| 66 | H28 | MIPI_DPHY_CSI3_RX_D0P | —— | —— | MIPI_DPHY_CSI3_RX_D0P数据接收0+ | MIPI_DPHY_CSI3_RX_D0P |
| 68 | H29 | MIPI_DPHY_CSI3_RX_D0N | —— | —— | MIPI_DPHY_CSI3_RX_D0N数据接收0- | MIPI_DPHY_CSI3_RX_D0N |
| 70 | —— | GND | —— | —— | 地 | GND |
| 72 | J28 | MIPI_DPHY_CSI3_RX_D1P | —— | —— | MIPI_DPHY_CSI3_RX_D1P数据接收1+ | MIPI_DPHY_CSI3_RX_D1P |
| 74 | J29 | MIPI_DPHY_CSI3_RX_D1N | —— | —— | MIPI_DPHY_CSI3_RX_D1N数据接收1- | MIPI_DPHY_CSI3_RX_D1N |
| 76 | —— | GND | —— | —— | 地 | GND |
| 78 | 1H22 | MIPI_DPHY_CSI3_RX_CLKP | —— | —— | MIPI_DPHY_CSI3_RX_CLKP时钟+ | MIPI_DPHY_CSI3_RX_CLKP |
| 80 | 1H23 | MIPI_DPHY_CSI3_RX_CLKN | —— | —— | MIPI_DPHY_CSI3_RX_CLKN时钟- | MIPI_DPHY_CSI3_RX_CLKN |
| 82 | —— | GND | —— | —— | 地 | GND |
| 84 | K28 | MIPI_DPHY_CSI3_RX_D2P/   MIPI_DPHY_CSI4_RX_D0P | —— | —— | MIPI_DPHY_CSI4_RX_D0P数据接收0+ | MIPI_DPHY_CSI4_RX_D0P |
| 86 | K29 | MIPI_DPHY_CSI3_RX_D2N/   MIPI_DPHY_CSI4_RX_D0N | —— | —— | MIPI_DPHY_CSI4_RX_D0N数据接收0- | MIPI_DPHY_CSI4_RX_D0N |
| 88 | —— | GND | —— | —— | 地 | GND |
| 90 | L28 | MIPI_DPHY_CSI3_RX_D3P/   MIPI_DPHY_CSI4_RX_D1P | —— | —— | MIPI_DPHY_CSI4_RX_D1P数据接收1+ | MIPI_DPHY_CSI4_RX_D1P |
| 92 | L29 | MIPI_DPHY_CSI3_RX_D3N/   MIPI_DPHY_CSI4_RX_D1N | —— | —— | MIPI_DPHY_CSI4_RX_D1N数据接收1- | MIPI_DPHY_CSI4_RX_D1N |
| 94 | —— | GND | —— | —— | 地 | GND |
| 96 | 1K22 | MIPI_DPHY_CSI4_RX_CLKP | —— | —— | MIPI_DPHY_CSI4_RX_CLKP时钟+ | MIPI_DPHY_CSI4_RX_CLKP |
| 98 | 1K23 | MIPI_DPHY_CSI4_RX_CLKN | —— | —— | MIPI_DPHY_CSI4_RX_CLKN时钟- | MIPI_DPHY_CSI4_RX_CLKN |
| 100 | —— | GND | —— | —— | 地 | GND |


## 2.7  FET3576-C核心板引脚说明（按功能划分）
**注1： 核心板所有引脚功能均按下表的“默认功能”作了规定，请勿修改，否则可能和出厂驱动冲突。如有疑问，请及时联系我们的销售或技术支持。**

**注2：用户在有多种功能扩展需求时可参阅参考中《FET3576-C核心板管脚复用对照表》,但若需了解更详细的信息，建议用户查阅相关资料文档及芯片数据手册及参考手册。**

**注3：“信号名称”一栏默认为核心板对应到底板上的引脚名称。**



### 2.7.1  电源引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| 电源 | VCC12V_DCIN | 电源输入 | 核心板电源供电引脚，12V | P3_91 |
|  |  |  |  | P3_93 |
|  |  |  |  | P3_95 |
|  |  |  |  | P3_97 |
|  |  |  |  | P3_99 |
|  |  |  |  | P3_98 |
|  |  |  |  | P3_100 |
|  | Carry_Board_PEN | 电源使能 | 用于底板外设供电使能 | P3_87 |
|  | GND | 地 | 核心板电源地，所有GND引脚都需要连接 | —— |


### 2.7.2  复位控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| 核心板复位 | RESET_L | I | 核心板断电复位，低电平有效 | P2_100 |


### 2.7.3  烧录控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | --- | :---: |
| Maskrom模式 | SARADC_VIN0_BOOT | I | 开机前拉低，进入Maskrom模式 | P1_28 |
| Recovery模式 | SARADC_VIN1_KEY/RECOVERY | I | 开机前拉低，进入Recovery模式 | P1_30 |


### 2.7.4  功能按键引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| --- | :---: | :---: | :---: | :---: |
| Maskrom按键 | SARADC_VIN0_BOOT | I | 开机前拉低，进入Maskrom模式 | P1_28 |
| 开关机 | PWRON_L | I | 核心板供电开关，低电平关机 | P3_88 |
| V+/RECOVERY按键 | SARADC_VIN1_KEY/RECOVERY | I | 音量加/Recovery按键 | P1_30 |
| V-按键 |  | I | 音量减按键 | P1_30 |
| MENU按键 |  | I | 菜单按键 | P1_30 |
| ESC按键 |  | I | 退出按键 | P1_30 |


### 2.7.5  USB数据/控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| USB | TYPEC_DPTX_AUX_PUPDCTL2 | O | DP_AUX上下拉 | P1_48 |
|  | USB_HUB_RST_3V3 | O | USB_HUB复位 | P1_50 |
|  | TYPEC_DPTX_AUX_PUPDCTL1 | O | DP_AUX上下拉 | P1_82 |
|  | USB2_HOST1_D_P | I/O | USB2.0_HOST数据+ | P1_92 |
|  | USB2_HOST1_D_N | I/O | USB2.0_HOST数据- | P1_94 |
|  | USB2_OTG1_ID | I | USB2_OTG1_ID脚 | P1_98 |
|  | USB2_OTG1_VBUSDET | I | USB2_OTG1_VBUSDET脚 | P1_100 |
|  | TYPEC0_INT | I | Type-C接口CC芯片中断 | P2_75 |
|  | USB3_HOST1_SSTX_P | O | USB3.0_HOST1发送+ | P2_89 |
|  | USB3_HOST1_SSTX_N | O | USB3.0_HOST1发送- | P2_91 |
|  | USB3_HOST1_SSRX_P | I | USB3.0_HOST1接受+ | P2_95 |
|  | USB3_HOST1_SSRX_N | I | USB3.0_HOST1接受- | P2_97 |
|  | USB3_OTG0_SSRX1_N | I | USB3.0_OTG0接受1- | P3_3 |
|  | USB3_OTG0_SSRX1_P | I | USB3.0_OTG0接受1+ | P3_5 |
|  | USB3_OTG0_SSTX1_P | O | USB3.0_OTG0发送1+ | P3_9 |
|  | USB3_OTG0_SSTX1_N | O | USB3.0_OTG0发送1- | P3_11 |
|  | USB3_OTG0_SSRX2_N | I | USB3.0_OTG接收2- | P3_15 |
|  | USB3_OTG0_SSRX2_P | I | USB3.0_OTG接收2+ | P3_17 |
|  | USB3_OTG0_SSTX2_P | O | USB3.0_OTG0发送2+ | P3_21 |
|  | USB3_OTG0_SSTX2_N | O | USB3.0_OTG0发送2- | P3_23 |
|  | USB2_OTG0_ID | I | USB2_OTG0_ID脚 | P3_14 |
|  | USB2_OTG0_VBUSDET | I | USB2_OTG0_VBUSDET脚 | P3_16 |
|  | USB2_OTG0_D_N | I/O | USB2.0_OTG数据- | P3_18 |
|  | USB2_OTG0_D_P | I/O | USB2.0_OTG数据+ | P3_20 |
|  | DP_TX_AUX_P | I/O | DP_TX_AUX数据+ | P3_22 |
|  | DP_TX_AUX_N | I/O | DP_TX_AUX数据- | P3_24 |
|  | TYPEC0_PWREN | O | Type-C接口电源使能 | P4_4 |


### 2.7.6  SD接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| SDIO | SDMMC0_D0 | I/O | SDIO数据位0 | P1_5 |
|  | SDMMC0_D1 | I/O | SDIO数据位1 | P1_3 |
|  | SDMMC0_D2 | I/O | SDIO数据位2 | P1_13 |
|  | SDMMC0_D3 | I/O | SDIO数据位3 | P1_11 |
|  | SDMMC0_CLK | O | SDIO时钟 | P1_7 |
|  | SDMMC0_CMD | I/O | SDIO命令信号 | P1_9 |
|  | SDMMC0_DET_L | I | SD卡插拔检测 | P3_90 |
|  | TF_PWR_EN_3V3 | O | SD卡供电使能 | P4_33 |


### 2.7.7  WIFI接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| 控制脚 | WIFI_REG_ON_H | O | WIFI电源使能 | P3_40 |
|  | WIFI_WAKE_HOST_H | I/O | 无线网唤醒主机 | P3_52 |
|  | BT_WAKE_HOST_H | I/O | 蓝牙唤醒主机 | P3_54 |
|  | HOST_WAKE_BT_H | I/O | 主机唤醒蓝牙 | P3_46 |
|  | BT_REG_ON_H | O | 蓝牙电源使能 | P3_42 |
|  | WIFI_PEN_3V3 | O | WIFI模块电源使能 | P4_25 |
| SDIO | SDMMC1_D0_M0 | I/O | SDIO数据位0 | P3_29 |
|  | SDMMC1_D1_M0 | I/O | SDIO数据位1 | P3_27 |
|  | SDMMC1_D2_M0 | I/O | SDIO数据位2 | P3_41 |
|  | SDMMC1_D3_M0 | I/O | SDIO数据位3 | P3_39 |
|  | SDMMC1_CLK_M0 | O | SDIO时钟 | P3_33 |
|  | SDMMC1_CMD_M0 | I/O | SDIO命令信号 | P3_35 |
| PCM | SAI2_SDI_M0 | I | PCM数据输入 | P3_53 |
|  | SAI2_SDO_M0 | O | PCM数据输出 | P3_45 |
|  | SAI2_LRCK_M0 | O | PCM同步控制信号 | P3_51 |
|  | SAI2_SCLK_M0 | O | PCM时钟信号 | P3_47 |
| UART | UART4_TX_M1 | O | UART4数据发送 | P3_28 |
|  | UART4_RX_M1 | I | UART4数据接收 | P3_30 |
|  | UART4_RTSN_M1 | O | UART4发送请求 | P3_34 |
|  | UART4_CTSN_M1 | I | UART4发送允许 | P3_36 |


### 2.7.8  UART接口控制引脚
| **默认功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| UART0 | UART0_TX_M0_DEBUG | O | UART0数据发送 | P2_7 |
|  | UART0_RX_M0_DEBUG | I | UART0数据接收 | P2_9 |
| UART5 | UART5_TX_M1 | O | UART5数据发送 | P2_39 |
|  | UART5_RX_M1 | I | UART5数据接收 | P2_61 |
| UART6 | UART6_TX_M3 | O | UART6数据发送 | P4_21 |
|  | UART6_RX_M3 | I | UART6数据接收 | P4_23 |
| UART8 | UART8_TX_M0 | O | UART8数据发送 | P2_73 |
|  | UART8_RX_M0 | I | UART8数据接收 | P2_69 |
|  | UART8_RTSN_M0 | O | UART8发送请求 | P2_77 |
|  | UART8_CTSN_M0 | I | UART8发送允许 | P2_79 |


### 2.7.9  IIC接口控制引脚
| **默认功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| I2C0 | I2C0_SCL_M1 | O | I2C时钟 | P4_11 |
|  | I2C0_SDA_M1 | I/O | I2C数据 | P4_15 |
| I2C2 | I2C2_SCL_M0 | O | I2C时钟 | P2_11 |
|  | I2C2_SDA_M0 | I/O | I2C数据 | P2_1 |
| I2C3 | I2C3_SCL_M0 | O | I2C时钟 | P2_35 |
|  | I2C3_SDA_M0 | I/O | I2C数据 | P2_43 |
| I2C4 | I2C4_SCL_M3 | O | I2C时钟 | P4_45 |
|  | I2C4_SDA_M3 | I/O | I2C数据 | P4_43 |
| I2C5 | I2C5_SCL_M3 | O | I2C时钟 | P5_31 |
|  | I2C5_SDA_M3 | I/O | I2C数据 | P5_33 |
| I2C7 | I2C7_SCL_M1 | O | I2C时钟 | P1_70 |
|  | I2C7_SDA_M1 | I/O | I2C数据 | P1_72 |
| I2C8 | I2C8_SCL_M2 | O | I2C时钟 | P1_56 |
|  | I2C8_SDA_M2 | I/O | I2C数据 | P1_60 |
| HDMI_I2C | HDMI_TX_SCL | O | I2C时钟 | P1_68 |
|  | HDMI_TX_SDA | I/O | I2C数据 | P1_58 |


### 2.7.10  以太网接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| GMAC0 | ETH_CLK0_25M_OUT_M0 | O | PHY 25MHz 参考时钟输出 | P4_57 |
|  | ETH0_MCLK_M0 | I | PHY 125MHz 同步时钟输入 | P4_61 |
|  | GMAC0_INT | I | RGMII中断 | P3_94 |
|  | GMAC0_RESET | O | RGMII复位 | P3_92 |
|  | GMAC0_MDC_M0 | O | 串行管理时钟 | P4_49 |
|  | GMAC0_MDIO_M0 | I/O | 串行管理数据 | P4_47 |
|  | GMAC0_TXD3_M0 | O | RGMII数据发送3 | P4_10 |
|  | GMAC0_TXD2_M0 | O | RGMII数据发送2 | P4_12 |
|  | GMAC0_TXD1_M0 | O | RGMII数据发送1 | P4_14 |
|  | GMAC0_TXD0_M0 | O | RGMII数据发送0 | P4_16 |
|  | GMAC0_TXCTL_M0 | O | RGMII发送控制 | P4_18 |
|  | GMAC0_TXCLK_M0 | O | RGMII发送时钟 | P4_20 |
|  | GMAC0_RXD3_M0 | I | RGMII接收数据3 | P4_24 |
|  | GMAC0_RXD2_M0 | I | RGMII接收数据2 | P4_26 |
|  | GMAC0_RXD1_M0 | I | RGMII接收数据1 | P4_28 |
|  | GMAC0_RXD0_M0 | I | RGMII接收数据0 | P4_30 |
|  | GMAC0_RXCTL_M0 | I | RGMII接收控制 | P4_32 |
|  | GMAC0_RXCLK_M0 | I | RGMII接收时钟 | P4_34 |
| GMAC1 | ETH_CLK1_25M_OUT_M0 | O | PHY 25MHz 参考时钟输出 | P4_35 |
|  | ETH1_MCLK_M0 | I | PHY 125MHz 同步时钟输入 | P4_37 |
|  | GMAC1_INT | I | RGMII中断 | P2_19 |
|  | GMAC1_RESET | O | RGMII复位 | P2_21 |
|  | GMAC1_MDC_M0 | O | 串行管理时钟 | P4_7 |
|  | GMAC1_MDIO_M0 | I/O | 串行管理数据 | P4_5 |
|  | GMAC1_TXD3_M0 | O | RGMII数据发送3 | P4_38 |
|  | GMAC1_TXD2_M0 | O | RGMII数据发送2 | P4_40 |
|  | GMAC1_TXD1_M0 | O | RGMII数据发送1 | P4_42 |
|  | GMAC1_TXD0_M0 | O | RGMII数据发送0 | P4_44 |
|  | GMAC1_TXCTL_M0 | O | RGMII发送控制 | P4_46 |
|  | GMAC1_TXCLK_M0 | O | RGMII发送时钟 | P4_48 |
|  | GMAC1_RXD3_M0 | I | RGMII接收数据3 | P4_52 |
|  | GMAC1_RXD2_M0 | I | RGMII接收数据2 | P4_54 |
|  | GMAC1_RXD1_M0 | I | RGMII接收数据1 | P4_56 |
|  | GMAC1_RXD0_M0 | I | RGMII接收数据0 | P4_58 |
|  | GMAC1_RXCTL_M0 | I | RGMII接收控制 | P4_60 |
|  | GMAC1_RXCLK_M0 | I | RGMII接收时钟 | P4_62 |


### 2.7.11  MIPI_CSI接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| MIPI_CSI0 | MIPI_DPHY_CSI0_RX_D0_P | I | CSI数据0+ | P3_58 |
|  | MIPI_DPHY_CSI0_RX_D0_N | I | CSI数据0- | P3_60 |
|  | MIPI_DPHY_CSI0_RX_D1_P | I | CSI数据1+ | P3_64 |
|  | MIPI_DPHY_CSI0_RX_D1_N | I | CSI数据1- | P3_66 |
|  | MIPI_DPHY_CSI0_RX_CLK_P | I | CSI时钟+ | P3_70 |
|  | MIPI_DPHY_CSI0_RX_CLK_N | I | CSI时钟- | P3_72 |
|  | MIPI_DPHY_CSI0_RX_D2_P | I | CSI数据2+ | P3_76 |
|  | MIPI_DPHY_CSI0_RX_D2_N | I | CSI数据2- | P3_78 |
|  | MIPI_DPHY_CSI0_RX_D3_P | I | CSI数据3+ | P3_82 |
|  | MIPI_DPHY_CSI0_RX_D3_N | I | CSI数据3- | P3_84 |
| MIPI_CSI1 | MIPI_DPHY_CSI1_RX_D0_P | I | CSI数据0+ | P4_67 |
|  | MIPI_DPHY_CSI1_RX_D0_N | I | CSI数据0- | P4_65 |
|  | MIPI_DPHY_CSI1_RX_D1_P | I | CSI数据1+ | P4_73 |
|  | MIPI_DPHY_CSI1_RX_D1_N | I | CSI数据1- | P4_71 |
|  | MIPI_DPHY_CSI1_RX_CLK_P | I | CSI时钟+ | P4_79 |
|  | MIPI_DPHY_CSI1_RX_CLK_N | I | CSI时钟- | P4_77 |
| MIPI_CSI2 | MIPI_DPHY_CSI2_RX_D0_P | I | CSI数据0+ | P4_85 |
|  | MIPI_DPHY_CSI2_RX_D0_N | I | CSI数据0- | P4_83 |
|  | MIPI_DPHY_CSI2_RX_D1_P | I | CSI数据1+ | P4_91 |
|  | MIPI_DPHY_CSI2_RX_D1_N | I | CSI数据1- | P4_89 |
|  | MIPI_DPHY_CSI2_RX_CLK_P | I | CSI时钟+ | P4_97 |
|  | MIPI_DPHY_CSI2_RX_CLK_N | I | CSI时钟- | P4_95 |
| MIPI_CSI3 | MIPI_DPHY_CSI3_RX_D0_P | I | CSI数据0+ | P4_66 |
|  | MIPI_DPHY_CSI3_RX_D0_N | I | CSI数据0- | P4_68 |
|  | MIPI_DPHY_CSI3_RX_D1_P | I | CSI数据1+ | P4_72 |
|  | MIPI_DPHY_CSI3_RX_D1_N | I | CSI数据1- | P4_74 |
|  | MIPI_DPHY_CSI3_RX_CLK_P | I | CSI时钟+ | P4_78 |
|  | MIPI_DPHY_CSI3_RX_CLK_N | I | CSI时钟- | P4_80 |
| MIPI_CSI4 | MIPI_DPHY_CSI4_RX_D0_P | I | CSI数据0+ | P4_84 |
|  | MIPI_DPHY_CSI4_RX_D0_N | I | CSI数据0- | P4_86 |
|  | MIPI_DPHY_CSI4_RX_D1_P | I | CSI数据1+ | P4_90 |
|  | MIPI_DPHY_CSI4_RX_D1_N | I | CSI数据1- | P4_92 |
|  | MIPI_DPHY_CSI4_RX_CLK_P | I | CSI时钟+ | P4_96 |
|  | MIPI_DPHY_CSI4_RX_CLK_N | I | CSI时钟- | P4_98 |


### 2.7.12  MIPI_DSI接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | --- | :---: |
| MIPI_DSI | MIPI_DPHY_DSI_TX_D0_P | O | DSI数据0+ | P3_59 |
|  | MIPI_DPHY_DSI_TX_D0_N | O | DSI数据0- | P3_57 |
|  | MIPI_DPHY_DSI_TX_D1_P | O | DSI数据1+ | P3_65 |
|  | MIPI_DPHY_DSI_TX_D1_N | O | DSI数据1- | P3_63 |
|  | MIPI_DPHY_DSI_TX_CLK_P | O | DSI时钟+ | P3_71 |
|  | MIPI_DPHY_DSI_TX_CLK_N | O | DSI时钟- | P3_69 |
|  | MIPI_DPHY_DSI_TX_D2_P | O | DSI数据2+ | P3_77 |
|  | MIPI_DPHY_DSI_TX_D2_N | O | DSI数据2- | P3_75 |
|  | MIPI_DPHY_DSI_TX_D3_P | O | DSI数据3+ | P3_83 |
|  | MIPI_DPHY_DSI_TX_D3_N | O | DSI数据3- | P3_81 |
|  | PWM0_CH0_M0 | O | 屏幕PWM调光 | P2_13 |
|  | MIPI_DSI1_EN | O | 屏幕电源使能 | P4_39 |
|  | MIPI_DSI1_RESET | O | 屏幕触摸复位 | P4_9 |
|  | MIPI_DSI1_INT | I | 屏幕触摸中断 | P4_1 |


### 2.7.13  PCIE接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| PCIE | PCIE0_TX_P | O | PCIE数据发送+ | P2_78 |
|  | PCIE0_TX_N | O | PCIE数据发送- | P2_76 |
|  | PCIE0_RX_P | I | PCIE数据接收+ | P2_72 |
|  | PCIE0_RX_N | I | PCIE数据接收- | P2_70 |
|  | PCIE0_REFCLK_P | O | PCIE时钟输出+ | P2_66 |
|  | PCIE0_REFCLK_N | O | PCIE时钟输出- | P2_64 |
|  | PCIE0_WAKEn_M0 | I | PCIE唤醒激活信号 | P1_74 |
|  | PCIE0_CLKREQn_M0 | O | PCIE时钟请求信号 | P1_78 |
|  | PCIE0_PERSTn | I | PCIE复位信号 | P1_64 |
|  | PCIE0_PRSN2_3V3 | O | PCIE插入检测信号 | P4_3 |
|  | PCIE_PWR_EN_3V3 | O | PCIE 3.3V电源使能 | P4_19 |


### 2.7.14  HDMI接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| HDMI | HDMI_TX_HPDIN_M0_1V8 | I | HDMI热插拔检测 | P2_71 |
|  | HDMI_TX_CEC_M0 | I/O | HDMI_CEC识别 | P1_52 |
|  | HDMI_TX_SBD_N | O | HDMI_SBD(ARC)- | P1_17 |
|  | HDMI_TX_SBD_P | O | HDMI_SBD(ARC)+ | P1_19 |
|  | HDMI_TX_D3_N | O | HDMI差分数据3- | P1_23 |
|  | HDMI_TX_D3_P | O | HDMI差分数据3+ | P1_25 |
|  | HDMI_TX_D0_N | O | HDMI差分数据0- | P1_29 |
|  | HDMI_TX_D0_P | O | HDMI差分数据0+ | P1_31 |
|  | HDMI_TX_D1_N | O | HDMI差分数据1- | P1_35 |
|  | HDMI_TX_D1_P | O | HDMI差分数据1+ | P1_37 |
|  | HDMI_TX_D2_N | O | HDMI差分数据2- | P1_41 |
|  | HDMI_TX_D2_P | O | HDMI差分数据2+ | P1_43 |
|  | HDMI_TX_SCL | O | I2C时钟 | P1_68 |
|  | HDMI_TX_SDA | I/O | I2C数据 | P1_58 |


### 2.7.15  I2S音频接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| I2S | SAI1_MCLK_M0 | O | I2S主时钟 | P2_65 |
|  | SAI1_SCLK_M0 | I/O | I2S串行时钟 | P2_55 |
|  | SAI1_LRCK_M0 | I/O | I2S左右声道切换 | P2_53 |
|  | SAI1_SDO0_M0 | O | I2S串行数据输出 | P2_49 |
|  | SAI1_SDI0_M0 | I | I2S串行数据输入 | P2_59 |
|  | HP_DET_L | I | 耳机插入检测 | P2_29 |
|  | SARADC_VIN3_HP_HOOK | I | 耳机线控按键 | P1_34 |


### 2.7.16  CAN接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| CAN0 | CAN0_TX_M2_3V3 | O | CAN0数据发送 | P4_29 |
|  | CAN0_RX_M2_3V3 | I | CAN0数据接受 | P4_31 |
| CAN1 | CAN1_TX_M3_3V3 | O | CAN1数据发送 | P1_66 |
|  | CAN1_RX_M3_3V3 | I | CAN1数据接受 | P1_54 |


### 2.7.17  4G/5G模组控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| 4G/5G模组控制 | 4G/5G_PWREN | O | 供电使能 | P1_76 |
|  | 4G/5G_RESET | O | 4G/5G模组复位 | P2_51 |
|  | 4G/5G_MOD_PWREN | O | 4G/5G模组电源使能 | P1_80 |


### 2.7.18  ADC接口控制接口
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| ADC | SARADC_VIN2_HW_ID | I | ADC输入 | P1_32 |
|  | SARADC_VIN4 | I | ADC输入 | P1_36 |
|  | SARADC_VIN5 | I | ADC输入 | P1_38 |
|  | SARADC_VIN6 | I | ADC输入 | P1_40 |
|  | SARADC_VIN7 | I | ADC输入 | P1_42 |


### 2.7.19  其他控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| IO扩展 | IIC_GPIO_INT | I | IO扩展芯片中断 | P2_67 |


## 2.8  核心板硬件设计说明
   FET3576-C核心板已经将电源、存储电路集成于一个小巧的模块上，所需的外部电路非常简洁，构成一个最小系统只需要 12V 电源、复位按键、烧录SD卡、启动配置即可运行，如下图所示：

最小系统原理图可以参见附录四。不过一般情况下，除最小系统外建议连接上一些外部设备，例如调试串口，用来查看打印信息；预留OTG接口，用来输出调试信息。做好这些后，再在此基础上根据飞凌提供的核心板默认接口定义来添加用户需要的功能。

核心板外围电路的设计可参见第三章的3.5节“OK3576-C底板说明”。

# 第三章 OK3576-C嵌入式开发平台介绍
## 3.1  OK3576-C开发板接口图
飞凌OK3576-C开发平台核心板和底板采用接插件的连接方式，主要接口如下图所示：





![Image](./images/OK3576C_hardware/de566621a7ee4eddb1b0898d80a41e62.jpeg)





![Image](./images/OK3576C_hardware/ec45bef41f294fe39e46c17f3993659b.jpeg)

## 3.2  OK3576-C开发板尺寸图
OK3576-C开发板和天线板尺寸图如下：

![Image](./images/OK3576C_hardware/ff2e07381b08482c89e1044c92dccefa.png)

底板PCB尺寸：130mm×190mm，更多详细尺寸请见用户资料dxf文件；

固定孔尺寸：间距：120mm×180mm，孔径：3.2mm；

制版工艺：厚度1.6mm，4层PCB；

电源电压：直流12V； 

天线板用于4G，5G天线的安装固定，外形尺寸：20mm×140mm，更多详细尺寸参见下图：

OK3576-C底板预留了2个直径3.2mm散热片的安装孔，用户可以根据现场环境选配安装散热片，散热片和核心板接触面请加一层绝缘的导热硅胶垫。飞凌自选的核心板散热片尺寸为：38mm×38mm×23mm，更多详细尺寸参见下图： 

![Image](./images/OK3576C_hardware/a366a4ed569a4bf98fd4d4273309eb8f.jpeg)![Image](./images/OK3576C_hardware/60073a4142074c70913a41aee8bdcb6d.jpeg)

## 3.3  底板命名规范
ABC-D+IK:M

| **字段** | **字段描述** | **值** | **说明** |
| :---: | --- | --- | --- |
| A | 合格等级 | PC | 原型样品 |
|  |  | 空白 | 大规模生产 |
| B | 产品线标识 | OK | 飞凌嵌入式开发板 |
| C | CPU名称 | RK3576 | RK3576 |
| - | 分段标识 | - |  |
| D | 连接方式 | Cx | 板对板连接器 |
| + | 分段标识 | + | 此标识之后为配置参数部分 |
| I | 运行温度 | I | -40 to 85℃ |
| K | PCB版本号 | 10 | V1.0 |
|  |  | xx | Vx.x |
| :M | 厂家内部标识 | :X | 此内容为厂家内部标识，对客户使用无影响 |


## 3.4  底板资源
| **功能** | **数量** | **参数** |
| :---: | :---: | --- |
| MIPI CSI | 5 | 1 x MIPI DPHY V2.0 4lanes接口，每lane最高支持4.5Gbps；通过1个26pins FPC座引出，默认挂载OV13855摄像头； |
|  |  | 4 xMIPI DPHY V1.2 2lanes接口，每lane最高支持2.4Gbps；通过4个26pins FPC座引出，默认挂载OV5645摄像头； |
| MIPI DSI | 1 | MIPI接口支持4 lanes输出，最高分辨率为2560 x 1600@60Hz； |
|  |  | 适配飞凌7吋MIPI屏，分辨率为1024x 600@30fps； |
| HDMI TX | 1 | 通过标准HDMI插座引出； |
|  |  | HDMI v2.1 最高支持 4K@120Hz； |
| DP TX | 1 | 1个DP接口与USB3.1 Gen1结合使用，通过Type-C接口引出； |
|  |  | DisplayPort v1.4 最高支持4K@120Hz； |
| USB3.1 Gen1 | 1 | 通过Type-C接口引出； |
|  |  | 与DP TX结合使用； |
| USB3.0 HOST | 3 | 通过3个Type-A USB接口引出； |
| PCIe2.0 | 1 | 通过PCIe x 1插槽引出； |
|  |  | 支持5Gbps速率； |
| Ethernet | 2 | 通过2个RJ45接口引出； |
|  |  | 支持10/100/1000 Mbps数据传输速率； |
| TF卡 | 1 | 可插入TF卡，速率达150MHz，支持SDR104 模式； |
| Audio | 1 | 板载Codec芯片，支持耳机输出、MIC输入级Speaker输出等功能； |
| CAN | 2 | 通过CAN收发器引出两路CAN总线； |
|  |  | 遵循 CAN 和 CAN FD 规范； |
| RS485 | 2 | 通过RS485收发器引出2路RS485总线； |
| UART | 1 | 通过2.44mm间距引出； |
|  |  | 波特率高达4Mbps； |
| 4G/5G | 1 | 支持M.2封装的4G/5G模块； |
| WIFI&BT | 1 | 板载海华AW-CM358SM-WIFI&BT模块； |
|  |  | 支持WIFI 2.4G/5G ,蓝牙5.0； |
| ADC | 5 | 通过2.44mm间距排针引出； |
|  |  | 12bit单端输入SAR-ADC，采样率高达1MS/s； |
| RTC | 1 | 板载RTC芯片及电池插座； |
| GPIO | 8 | 通过2.44mm间距排针引出8路GPIO、同时引出3.3V和1.8V电源； |


**注：**

1. **表中参数为硬件设计或CPU理论值；**
2. **“TBD”表示现阶段暂未开发功能；**



## 3.5  OK3576-C底板说明
**注：下图中元件位号有“_DNP”标识的，代表此元器件默认不焊接。**

**    本章节的原理图仅是为了方便阅读，可能会有更改，请用户设计一定要按照源文件原理图为准。**

### 3.5.1  底板电源
开发板使用12V电源适配器供电，电源接口为DC005规格的插座。拨动开关S1为开发板的电源开关，按照底板丝印指示方向拨动开关控制上下电。S1后级并联TVS管进行静电防护，F1保险丝进行过流保护，D1与F1配合进行防反接保护。VCC12V_DCIN同时给FET3576核心板和底板其他外设进行供电。

![Image](./images/OK3576C_hardware/8f0d16a14b7c4f4c83fabcd2938e9030.png)

VCC12V_DCIN通过U3（DC-DC）降压至VCC_5V，VCC_5V给底板其他外设供电。（这里需要注意12V降5V DC-DC芯片选型时，芯片的输出功率要足够大，建议输出电流6A以上，保证为后级提供足够电流）

核心板通过12V供电正常启动后，通过CARRIER_BOARD_EN引脚输出高电平，来控制U3使能输出VCC_5V电源为开发板的部分外设供电。（该信号电平为3.3V，驱动能力为10K上拉，如果被使能设备使能引脚所需驱动能力超出该范围，则需要添加缓冲器或者门电路用来增加驱动能力，确保核心板和底板上电正常）。

![Image](./images/OK3576C_hardware/128471a6a74f4f279a2e2e18a6d1f500.png)

VCC_5V通过U4（DC-DC）降压至VCC_3V3。VCC_3V3电源为开发板的部分设备供电。

![Image](./images/OK3576C_hardware/7630fdfda1b84ce6adff7ee928028331.png)

VCC_3V3通过U2（LDO）降压至VCC_1V8。VCC_1V8电源为开发板的部分设备供电。

![Image](./images/OK3576C_hardware/4b99d7b608354ef19a887be439626779.png)

**注意：**

**1、客户自行设计时，务必保证电源的上电时序；**

**2、升降压芯片的器件选型及外部布局需要参考对应的芯片手册，确保良好的电源回路。**

### 3.5.2  复位及开关机信号
RESET_L为核心板复位信号输入，为方便调试，连接到按键上。

![Image](./images/OK3576C_hardware/11b99632bfc042ed97ef04c08ac8aaaf.png)

PWRON_L为核心板开关机信号输入，为方便调试，连接到按键上。

![Image](./images/OK3576C_hardware/4d5fa53c86e54842b22f061c06ef68bc.png)

### 3.5.3  Boot配置
RK3576支持多种启动引导方式，在芯片复位结束后，芯片内部集成的引导代码可以在如下接口设备进行引导，具体引导顺序可根据实际应用需求进行选择：

·Serial Flash(FSPI0、FSPI1_M0、FSPI1_M1)

·eMMC

·UFS

·SDMMC0 Card

如果在上述设备中没有引导代码，可以通过USB2.0 OTG0接口USB2_OTG0_DP/DM信号将系统代码下载到这些设备中，同时也支持从USB 3.2 Gen1x1 OTG0接口的USB3_OTG0_SSRX1P/N与USB3_OTG0_SSTX1P/N信号烧录固件。请注意，如果需要支持USB3.0升级固件且需要支持2Lane DP 时，必须采用USB3.2 Gen1x1 OTG0+DP 2Lane(Swap ON)的方案。

**引导顺序选择**：

RK3576的Boot启动顺序可以通过SARADC_VIN0_BOOT Pin（PIN：P1_28）进行设置，从不同接口对应的外设启动，如下表所示硬件通过配置不同的上下拉电阻值，设计 Config1-Config11 共 11 种模式的外设引导顺序，可根据实际应用需求进行对应配置。

表3.5.3.1 Boot启动顺序配置表

| Item | Rup | Rdown | ADC | BOOT MODE |
| :---: | :---: | :---: | :---: | --- |
| Config1 | DNP | 10K | 0 | USB (Maskrom mode) |
| Config2 | 10K | 1.13K | 416 | FSPI0→USB |
| Confi 3 | 10K | 2.49K | 816 | FSPI1_M0→EMMC→USB |
| Config4 | 10K | 4.3K | 1231 | FSPI1_M1→EMMC→USB |
| Config5 | 10K | 6.8K | 1658 | FSPI0→UFS→USB |
| Config6 | 10K | 10K | 2048 | FSPI1_M0→UFS→USB |
| Config7 | 10K | 14.7K | 2437 | UFS→USB |
| Config8 | 10K | 23.2K | 2862 | UFS→SDMMC0→USB |
| Config9 | 10K | 40.2K | 3279 | RFU |
| Config10 | 10K | 88.7K | 3680 | EMMC→SDMMC0→USB |
| Config11 | 10K | DNP | 4095 | EMMC→USB |


核心板上SARADC_VIN0_BOOT配置为10K上拉，因此核心板默认从eMMC启动。底板可以增加下拉电阻，以实现其他的引导顺序。按照以上Config1设置，OK3576-C将SARADC_VIN0_BOOT通过轻触按键连接至GND，以实现Maskrom mode。

![Image](./images/OK3576C_hardware/75639444b4a14617b9233b34d6378034.png)

SARADC_VIN1用于对地短路进入Recovery状态，核心板将其用10K电阻上拉至1.8V电源。OK3576-C上，按键阵列采用并联型，可以通过增减按键并调整分压电阻比例来调整输入键值，实现多键输入以满足客户产品需求；设计中建议任意两个按键键值必须大于±35，即中心电压差必须大于123mV。如下图：

![Image](./images/OK3576C_hardware/84e45d7883984284bc6a116e2ea78d6d.png)

**注意:**

**1、用于按键采集时，靠近按键需做ESD防护，而且0键值的必须串接100ohm电阻加强抗静电浪涌能力（如果只有一个按键时，ESD必须靠近按键，先经过ESD→100ohm电阻→1nF→芯片管脚）；**

### 3.5.4  系统初始化配置信号
FET3576中有一个重要信号会影响系统的启动配置，需要在上电前配置完毕并保持状态稳定：

SDMMC0_DET_L（PIN：P3_90）（默认功能为SDMMC_DET）：决定 VCCIO1 电源域 IO 是 SDMMC0 还是 JTAG 功能。

FET3576的JTAG功能与SDMMC功能复用在一起，通过SDMMC0_DET_L管脚来切换IOMUX的功能，故该管脚也需要在上电前完成配置，否则JTAG功能无输出会影响到引导阶段的调试，而SDMMC0无输出会影响到SDMMC0 boot功能。

![Image](./images/OK3576C_hardware/31a0ba653cf8430b98028456f1540d06.png)

1. 该管脚检测为高电平，则对应IO切换到JTAG功能；
2. 当检测到为低电平（大部分SD卡插入会拉低该管脚，如果不是需要特殊处理），对应IO切换为SDMMC0 功能；
3. 系统起来后，可切换成由寄存器来控制IOMUX，那么该管脚可以释放出来；
4. 为方便查询，这个管脚的配置状态与功能对应如下表所示：

表3.5.4.1 FET3576系统初始化配置信号描述 

| 信号名 | 内部上下拉 | 描述 |
| :---: | :---: | --- |
| SDMMC0_DET_L | 上拉 | SDMMC/ARM JTAG管脚复用选择控制信号：   0：识别为SD卡插入，SDMMC/ JTAG管脚复用为SDMMC0功能；   1：未识别为SD卡插入，SDMMC/ JTAG管脚复用为 JTAG功能（Default） |


### 3.5.5  JTAG与 UART Debug电路
RK3576 芯片的 JTAG 接口符合 IEEE1149.1 标准，PC 可通过 SWD 模式（两线模式）连接 DSTREAM

仿真器，调试芯片内部的 ARM Core。

JTAG 接口说明如下表所示：

表3.5.5.1 FET3576 JTAG Debug接口信号

| 信号名 | 描述 |
| --- | --- |
| JTAG_TCK_M0/M1 | SWD模式时钟输入 |
| JTAG_TMS_M0/M1 | SWD模式数据输入输出 |


RK3576的JTAG有2个复用，其中JTAG_TCK_M0/JTAG_TMS_M0位于VCCIO1域，和SDMMC0复用IOMUX；JTAG_TCK_M1/JTAG_TMS_M1位于PMUIO1域，和UART_Debug——UART0_M0复用，IOMUX复用情况如下图所示。

![Image](./images/OK3576C_hardware/cfe2f8173baa4f5aa336290e0a729450.png)



FET3576的UART Debug默认选择UART0_TX_M0_DEBUG（P2_7）/UART0_RX_M0_DEBUG（P2_9）。UART Debug信号如果使用插件引出，则需要串接100ohm电阻，靠近插件位置需增加TVS管。

OK3576-C开发板为方便用户调试，使用USB转UART芯片将UART Debug信号转成USB信号，通过Type-C插座引出，用户用USB Type-A转UAB Type-C的线将OK3576-C的P16与PC机连接，安装CP2102驱动即可。原理图如下：

![Image](./images/OK3576C_hardware/68baad275cec4f00baa797b0c39bb54c.png)![Image](./images/OK3576C_hardware/85940f31576a4273adae6f580311ea22.png)![Image](./images/OK3576C_hardware/c136cb7b66f9493faacc165c9fc08c00.png)

**注意:**

**1、为方便后期调试，请用户在自行设计底板时将此调试串口引出；**

**2、建议保留Q1、Q2，这样能有效防止核心板未上电时，U6电流通过UART0_TX/RX回流到CPU中，影响启动，甚至造成损坏。**

### 3.5.6  IIC扩展IO
为了引出更为丰富的接口，底板部分使能和复位信号由IIC转IO芯片U5完成。同时U5空余的部分IO通过P17引出，方便用户扩展，原理如下图：

![Image](./images/OK3576C_hardware/4662d734d2fd451d80ccbcc0f1fec066.png)![Image](./images/OK3576C_hardware/bd9362fafb61419e992a895d40989028.png)

### 3.5.7  SARADC接口
OK3576-C通过P18将SARADC_VIN2/VIN4/VIN5/VIN6/VIN7引出，R371为可变电阻，通过将SARADC_VIN2/VIN4/VIN5/VIN6/VIN7与P18的4、6、8、10排针短接，在调整R371可变电阻阻值时，通过ADC可以读取到电压变化。如下图所示：

![Image](./images/OK3576C_hardware/ac8103e9d74e4116ab0b662e85c48db9.png)

**注意:**

**1.SARADC_VINx在使用时，靠近管脚必须增加1nF电容消抖；**

### 3.5.8  TF Card
底板P20为TF Card接口，可以支持系统启动与烧写。

![Image](./images/OK3576C_hardware/352d8ac8e5094294ab9dfb75c37235d9.png)![Image](./images/OK3576C_hardware/edf162fa27b54aac94b778525498828b.png)

**注意：**

**1、TF卡供电电源需要受控，参考底板电路；**

**2、SDIO阻抗要求： 单端50ohm，信号等长控制50mil;**

### 3.5.9  RTC电路
OK3576-C提供一个板载外置RTC功能，以实现更精准计时和更低功耗，原理图如下：

![Image](./images/OK3576C_hardware/35d8ae772bc0493dbaa606aedee55494.png)

### 3.5.10  Ethernet电路
底板支持双路1000/100/10M以太网接口，通过RJ45引出。

![Image](./images/OK3576C_hardware/8980d1a7e5dd4ae8a5219f0b5d81a322.png)![Image](./images/OK3576C_hardware/8a00c3e7214e44768e8b3dc95daaf12d.png)

**<font style="color:#ff0000;">注：</font>**

**<font style="color:#ff0000;">1.下表为RK3576 RGMII/RMII接口设计：</font>**

**<font style="color:#ff0000;">表3.5.10.1 RK3576 RGMII/RMII接口设计</font>**

| **信号** | **IO类型**   **（芯片端）** | **RGMII接口** | **信号描述** | **RMII接口** | **信号描述** |
| :---: | :---: | :---: | :---: | :---: | :---: |
| <font style="color:rgb(255, 0, 0);">GMACx_TXD[3:0]</font> | <font style="color:rgb(255, 0, 0);">输出</font> | <font style="color:rgb(255, 0, 0);">RGMIIxTXD[3:0]</font> | <font style="color:rgb(255, 0, 0);">数据发送</font> | <font style="color:rgb(255, 0, 0);">RMIIx_TXD[1:0]</font> | <font style="color:rgb(255, 0, 0);">数据发送</font> |
| <font style="color:rgb(255, 0, 0);">GMACx_TXCLK</font> | <font style="color:rgb(255, 0, 0);">输出</font> | <font style="color:rgb(255, 0, 0);">RGMIIx_TXCLK</font> | <font style="color:rgb(255, 0, 0);">数据发送参考时钟</font> | <font style="color:rgb(255, 0, 0);">--</font> | <font style="color:rgb(255, 0, 0);">--</font> |
| <font style="color:rgb(255, 0, 0);">GMACx_TXCTL</font> | <font style="color:rgb(255, 0, 0);">输出</font> | <font style="color:rgb(255, 0, 0);">RGMIIx_TXCTL</font> | <font style="color:rgb(255, 0, 0);">数据发送使能（上升沿）和数据发送错误（下降沿）</font> | <font style="color:rgb(255, 0, 0);">RMIIx_TXEN</font> | <font style="color:rgb(255, 0, 0);">数据发送使能信号</font> |
| <font style="color:rgb(255, 0, 0);">GMACx_RXD[3:0]</font> | <font style="color:rgb(255, 0, 0);">输入</font> | <font style="color:rgb(255, 0, 0);">RGMIIx_RXD[3:0]</font> | <font style="color:rgb(255, 0, 0);">数据接收</font> | <font style="color:rgb(255, 0, 0);">RMIIx_RXD[1:0]</font> | <font style="color:rgb(255, 0, 0);">数据接收</font> |
| <font style="color:rgb(255, 0, 0);">GMACx_RXCLK</font> | <font style="color:rgb(255, 0, 0);">输入</font> | <font style="color:rgb(255, 0, 0);">RGMIIx_RXCLK</font> | <font style="color:rgb(255, 0, 0);">数据接收参考时钟</font> | <font style="color:rgb(255, 0, 0);">--</font> | <font style="color:rgb(255, 0, 0);">--</font> |
| <font style="color:rgb(255, 0, 0);">GMACx_RXCTL</font> | <font style="color:rgb(255, 0, 0);">输入</font> | <font style="color:rgb(255, 0, 0);">RGMIIx_RXCTL</font> | <font style="color:rgb(255, 0, 0);">数据接收有效（上升沿）和接收错误（下降沿）</font> | <font style="color:rgb(255, 0, 0);">RMIIx_RXCTL</font> | <font style="color:rgb(255, 0, 0);">数据接收有效和载波侦听</font> |
| <font style="color:rgb(255, 0, 0);">GMACx_MCLKINOUT</font> | <font style="color:rgb(255, 0, 0);">输入/输出</font> | <font style="color:rgb(255, 0, 0);">RGMIIx_MCLKI_</font>   <font style="color:rgb(255, 0, 0);">125M</font> | <font style="color:rgb(255, 0, 0);">PHY发送125MHz给MAC，可选</font> | <font style="color:rgb(255, 0, 0);">RMII_MCLKIN_50M or RMII_MCLKOUT_50M</font> | <font style="color:rgb(255, 0, 0);">RMII数据发送和数据接收参考时钟</font> |
| <font style="color:rgb(255, 0, 0);">ETHx_REFCLKO_</font>   <font style="color:rgb(255, 0, 0);">25M</font> | <font style="color:rgb(255, 0, 0);">输出</font> | <font style="color:rgb(255, 0, 0);">ETHx_REFCLK_</font>   <font style="color:rgb(255, 0, 0);">25M</font> | <font style="color:rgb(255, 0, 0);">RK3576提供25MHz时钟替代PHY晶体</font> | <font style="color:rgb(255, 0, 0);">ETHx_REFCLKO_</font>   <font style="color:rgb(255, 0, 0);">25M</font> | <font style="color:rgb(255, 0, 0);">RK3576提供25MHz时钟替代PHY晶体</font> |
| <font style="color:rgb(255, 0, 0);">GMACx_MDC</font> | <font style="color:rgb(255, 0, 0);">输出</font> | <font style="color:rgb(255, 0, 0);">RGMIIx_MDC</font> | <font style="color:rgb(255, 0, 0);">管理数据时钟</font> | <font style="color:rgb(255, 0, 0);">RMIIx_MDC</font> | <font style="color:rgb(255, 0, 0);">管理数据时钟</font> |
| <font style="color:rgb(255, 0, 0);">GMACx_MDIO</font> | <font style="color:rgb(255, 0, 0);">输入/输出</font> | <font style="color:rgb(255, 0, 0);">RGMIIx_MDIO</font> | <font style="color:rgb(255, 0, 0);">管理数据输出/输入</font> | <font style="color:rgb(255, 0, 0);">RMIIx_MDIO</font> | <font style="color:rgb(255, 0, 0);">管理数据输出/输入</font> |


**<font style="color:#ff0000;">2.在RGMII模式下，RK3576芯片内部TX/RX时钟路径集成了delayline，支持调整；参考图默认配置是：TXCLK与data之间时序由MAC来控制，RXCLK与data之间时序由PHY来控制（如使用RTL8211F/FI即RXCLK默认开启2nS delay，其它PHY要注意这个配置）；</font>**

**<font style="color:#ff0000;">3.GMAC0接口电平仅支持1.8V，GMAC1接口电平默认为3.3V（如必须要改成1.8V，请联系飞凌），需要注意PHY芯片RGMII信号电源域供电电压是否和GMACx接口电平匹配；</font>**

**<font style="color:#ff0000;">4.Ethernet PHY的Reset信号需要用GPIO来控制，GPIO的电平必须和PHY IO电平匹配，靠近PHY管脚必须增加100nF电容，加强抗静电能力，注意：RTL8211F/FI的复位管脚只支持3.3V电平；</font>**

**<font style="color:#ff0000;">5.TXD0-TXD3，TXCLK，TXEN需在FET3576端预留串接0ohm电阻，根据实际情况有条件提高信号质量；</font>**

**<font style="color:#ff0000;">6.RXD0-RXD3，RXCLK，RXDV需在PHY端串接22ohm电阻，以提高信号质量；</font>**

**<font style="color:#ff0000;">7.PHY使用外置晶体时，晶体电容请根据实际使用的晶体的负载电容值选择，控制频偏在±20ppm以内；</font>**

**<font style="color:#ff0000;">8.</font>** **<font style="color:#ff0000;">RTL8211F/FI的RSET管脚外接电阻为2.49K ohm精度为1%，不得随意修改；</font>**

**<font style="color:#ff0000;">9.</font>** **<font style="color:#ff0000;">MDIO必须外部加上拉电阻，推荐1.5-1.8Kohm，上拉电源必须和IO电源保持一致；</font>**

**<font style="color:#ff0000;">10.PCB Layout需要保证RGMII信号参考平面完整，需要保证PHY芯片外围电源参考平面完整；</font>**

**<font style="color:#ff0000;">11.等长要求：RGMII的接收和发送可分组等长，等长要求≤12.4mil；</font>**

**<font style="color:#ff0000;">12.阻抗要求：单端50ohm；</font>**

### 3.5.11  RS485接口
OK3576-C支持两路RS485接口

RS485收发器芯片U8/U9，收发器芯片信号为TDH341S485S，隔离耐压高达5000VDC，总线静电防护能力高达15kV（HBM），＞25Kv/us瞬态抗扰度。同时OK3576-C底板兼容了更高级别的浪涌脉冲群多级防护电路，如下图所示：

![Image](./images/OK3576C_hardware/0400e8b56e6f40ef859c3edb71a3575c.png)

### 3.5.12  CAN接口
OK3576-C板载两个CAN收发器芯片U10、U11，收发器芯片信号为TDH541SCANFD，隔离耐压高达5000VDC，总线静电防护能力高达15kV（HBM），＞25Kv/us瞬态抗扰度。同时OK357-C底板兼容了更高级别的浪涌脉冲群多级防护电路，如下图所示：

![Image](./images/OK3576C_hardware/d2fbac0305374352a5a8d71e04c06471.png)

### 3.5.13  Audio
OK3576-C板载一个I2S接口的Codec芯片U31，支持MIC输入、耳机输出以及1W 8Ω喇叭输出。原理如下图所示：

![Image](./images/OK3576C_hardware/8143d666b6b14f10b434b85c234ec6b9.png)

### 3.5.14  4G&5G接口
OK3576-C集成一个M.2 Key-B接口，兼容4G和5G模块，由于4G和5G模块供电电压不同，因此需要拨动S2，选择相应的供电电压。

![Image](./images/OK3576C_hardware/1cd3de7564904bbdaf19e4439150b9df.png)

### 3.5.15  USB2.0/USB3.0_A/Type-C USB3.0电路
RK3576芯片内置两个USB3 OTG控制器，两个USB3控制器都内嵌了USB2.0 OTG。

**其中USB3 OTG0/DP1.4接口应用如下**

USB3.2 Gen1x1 OTG0/DP1.4组成Combo PHY，USB3 OTG0控制器与PHY的内部复用图如下：

![Image](./images/OK3576C_hardware/c919cbe6c1e140699b1b967b039ca5e8.png)

USB3 OTG0控制器支持SS/HS/FS/LS，内嵌的USB2.0（HS/FS/LS）信号采用USB2.0 OTG PHY，信号名见下图的红色方框内；RK3576默认使用该接口做Fireware的Download，应用中请务必要预留出此接口。

![Image](./images/OK3576C_hardware/2dd1e32feccf41259764dee9d1ec2981.png)

**注意：USB2_OTG0_DP/USB2_OTG0_DM支持Download Firmware，如果产品不用这个接口，在调试与生产过程中必须要预留此接口，注意：USB2_OTG0_VBUSDET也必须连接！**

USB 3.2的SS信号（5Gbps）与DP1.4复用，使用USB/DP的Combo PHY；信号如下图的红色方框内。

![Image](./images/OK3576C_hardware/f8cb831b0c534f8eb8ab698dd73da5b4.png)

由于USB3的OTG和USB2.0的OTG是同一个USB3的控制器，因此USB3和USB2.0的OTG只能同时做Device或者做HOST，不能USB3的OTG做HOST，USB2.0的OTG做Device或者USB3 的OTG做Device而USB2.0的OTG做HOST。

USB3 OTG0 Controller和DP1.4 Controller通过USB3/DP1.4的Combo PHY组合成一个完整的 TYPEC口，此Combo PHY支持Display Alter mode，Lane0和Lane2在DP mode下做TX，在USB mode下做 RX；TX和RX共享Lane0和Lane2。

这个USB3/DP1.4的Combo PHY支持Lane间的交换（SWAP），因此一个TYPEC标准口可以有如下五种的配置：

配置一：Type-C 4Lane(with DP function)

![Image](./images/OK3576C_hardware/784ef4f2cd9248f7a2f76fb9d1ade09a.png)

配置二：USB2.0 OTG+DP1.4 4Lane(Swap OFF)

![Image](./images/OK3576C_hardware/7b815bee410a4b1aa09070399bdf21e3.png)

配置三：USB2.0 OTG+DP1.4 4Lane(Swap ON)

![Image](./images/OK3576C_hardware/b58f70e57c734601aabe543b544778d8.png)

配置四：USB3.2 Gen1x1 OTG0+DP1.4 2Lane(Swap OFF)

![Image](./images/OK3576C_hardware/8ade452fcd524726b81444611043dd94.png)

配置五：USB3.2 Gen1x1 OTG0+DP1.4 2Lane(Swap ON)

![Image](./images/OK3576C_hardware/e286b0e502c14e07adc6c020d9e6df67.png)

**注意：RK3576支持从USB 3.2 Gen1x1 OTG0接口的USB3_OTG0_SSRX1P/N与USB3_OTG0_SSTX1P/N 信号下载固件。需要支持USB3.0升级固件且需要支持2Lane DP时，必须采用USB3.2 Gen1x1 OTG0+DP 2Lane(Swap ON)的方案。**

**其中USB3 OTG1接口应用如下**

PCIE1/SATA1/USB3 OTG1组成Comb PHY1，USB3 OTG1控制器与PHY的内部复用图如下：

![Image](./images/OK3576C_hardware/51d12731e5604d7ba52ac681951a05e9.png)

USB3 OTG1控制器支持SS/HS/FS/LS，内嵌了USB2.0（HS/FS/LS）信号构成PCIE1/SATA1/USB3 OTG1 COMBO PHY1；管脚分布如下：

![Image](./images/OK3576C_hardware/aab6facb553540f1a7f8d5b7b7bc0364.png)

USB20 OTG1 的管脚分配如下图：

![Image](./images/OK3576C_hardware/24df6f6f007d4f4d9c55255988d5d756.png)

由于USB3的OTG1和USB2.0的OTG1是同一个USB3的控制器，因此USB3和USB2.0的OTG1 只能同时做Device或者做HOST，不能USB3的OTG做HOST，USB2.0的OTG做Device或者USB3 的OTG做Device而USB2.0的OTG做HOST。

**注意：PCIE1/SATA1/USB3 OTG1 的 COMBO PHY1 设置成 PCIe 或者 SATA 功能时，USB3 OTG1 功能不能使用，并且 USB2.0 PHY1 也不能使用；因此要使用 USB2.0 OTG1 时，PCIE1/SATA1/USB3 OTG1 的 COMBO PHY1 必须设置成 USB3 功能！！！**



PCIE1/SATA1/USB3 OTG1 的 COMBO PHY1 中 USB3 OTG1 的应用方式有如下几种：

配置一：USB3.2 Gen1x1 OTG1

![Image](./images/OK3576C_hardware/aed730f162db4d128a3852fb8a1cf90c.png)

配置二：USB2 OTG1

![Image](./images/OK3576C_hardware/2d61f0bb3af643af8758b77777ecff50.png)

配置三：USB2/USB3 不用，PCIE 和 SATA 的具体应用方式详见 PCIE 和 SATA 章节

![Image](./images/OK3576C_hardware/efb291338ec0463085815b8ee4c453a6.png)



OK3576-C开发板上使用一颗USB HUB芯片将单路USB2.0/USB3.0_HOST转为4路，其中三路USB3.0分别接到3个Type-A接口供客户使用，每一路可提供最大1A电流输出并具有限流开关保护功能，剩余一路USB3.0提供给4G&5G模块使用。

FET3576支持一路USB/DP组合接口，支持USB 3.2 Gen1x1，DisplayPort v1.4；在OK3576-C底板上设计为一个标准的Type-C USB 3.0全功能接口，支持数据传输与DP显示输出。

下图是USB3.0 HUB部分的电路：

![Image](./images/OK3576C_hardware/a22b9efda78144d38876278dafe21c6b.png)![Image](./images/OK3576C_hardware/3a9fdba28dca45d3a91f3020aa48aa30.png)

额外使用两颗开关电源为USB HUB芯片提供3.3V和1.2V的电源：

![Image](./images/OK3576C_hardware/bb14a6cc1e0f4a5d8f44a7a26f867490.png)

USB HUB芯片转出的三路USB3.0接口都搭配USB供电限流开关芯片，为Type-A接口提供稳定的电源和限流保护功能：

![Image](./images/OK3576C_hardware/ef0e1468e02443638e6dd2c53ba1f647.png)![Image](./images/OK3576C_hardware/6cabe3c4fd7c4d11b012479783d692ae.png)![Image](./images/OK3576C_hardware/ebbdcd11f4a049e7bf6818d041efb909.png)

**注意： **

**1. USB数据线都需要做90Ω差分阻抗；**

**2. 请选择合适的ESD器件；**

下图是Type-C USB 3.0接口部分的电路：

![Image](./images/OK3576C_hardware/edde3b2b1bfe403eaaa2a203ee2285ff.png)

上图是Type-C接口CC协议芯片电路，用来支持Type-C正反插识别等功能；

![Image](./images/OK3576C_hardware/dce80cc4edcf41fabce3fe484ac8b528.png)

上图是Type-C USB3.0接口的差分信号电路与ESD防护器件。

**<font style="color:#ff0000;">注意：</font>**

**<font style="color:#ff0000;">1.</font>** **<font style="color:#ff0000;"> USB2_OTG0_DN/</font>** **<font style="color:#ff0000;">USB2_OTG0_DP是系统固件烧写口，如果产品不用这个接口，在调试与生产过程中必须要预留此接口，不然会无法调试及生产烧写固件；</font>**

**<font style="color:#ff0000;">2.</font>** **<font style="color:#ff0000;">USB2_OTG0_ID内部有大概12Kohm电阻上拉到1.8V；</font>**

**<font style="color:#ff0000;">3.  </font>************<font style="color:#ff0000;">USB2_OTG0_VBUSDET是OTG和Device模式检测脚，芯片内部有一个下拉40Kohm的电阻；高为DEVICE 设备，2.7-3.3V，TYP：3.0V，建议在管脚放置一个100nF电容。</font>**

**<font style="color:#ff0000;">4.  OTG模式可以设置以下三种模式：</font>**

**<font style="color:#ff0000;">·	OTG模式：根据ID脚状态自动切换是device模式或HOST模式，ID高为device，ID拉低为HOST，处在device模式时，还会判断VBUSDET脚是否为高（大于2.3V），如果为高，才会拉高DP，开始枚举；</font>**

**<font style="color:#ff0000;">·Device模式：设置为这个模式时，无需ID脚，只需判断VBUSDET脚是否为高（大于2.3V），如果为高，才会拉高DP，开始枚举；</font>**

**<font style="color:#ff0000;">·HOST模式：设置为这个模式时，ID和VBUSDET状态都无需要关心。（如果产品只需要HOST模式，但是由于仅USB2_OTG0_DN/ USB2_OTG0_DP是系统固件烧写口，在调试与生产过程都需要用这个口，烧写和adb调试时，需要设置成device模式，因此USB2_OTG0_VBUSDET信号也必须接）。</font>**

**<font style="color:#ff0000;">若采用TYPEC接口， USB2_OTG0_VBUSDET信号通过4.7K电阻拉高到3.3V即可。</font>**

**<font style="color:#ff0000;">5.  为加强抗静电和浪涌能力，信号上必须预留ESD器件，USB2.0信号的ESD寄生电容不得超过3pF，另外USB2.0信号的DP/DM串接2.2ohm电阻，加强抗静电浪涌能力；</font>**

**<font style="color:#ff0000;">6.  为抑制电磁辐射，可以考虑在信号线上预留共模电感（Common mode choke），在调试过程中根据实际情况选择使用电阻或者共模电感；</font>**

**<font style="color:#ff0000;">7.</font>** **<font style="color:#ff0000;">如果有用USB2_OTG0_ID信号，为加强抗静电和浪涌能力，信号上必须预留ESD器件，而且串接100ohm电阻，不得删减；</font>**

**<font style="color:#ff0000;">8.</font>** **<font style="color:#ff0000;">当HOST功能时，5V电源建议增加限流开关，限流大小根据应用需要可调整，限流开关使用3.3V的GPIO控制，建议5V电源增加22uF和100nF以上的电容滤波；若USB口可能接移动硬盘，建义滤波增加电容到100uF以上。</font>**

**<font style="color:#ff0000;">9.</font>** **<font style="color:#ff0000;">TYPEC协议要求在SSTXP/N线上增加100nF交流耦合电容，AC耦合电容建议使用0201封装，更低的ESR和ESL，也可减少线路上的阻抗变化。</font>**

**<font style="color:#ff0000;">10. TYPEC座子所有信号都必须增加ESD器件，布局时靠近USB连接器放置。对于SSTXP/N，SSRXP/N信号，ESD寄生电容不得超过0.3pF。</font>**

**<font style="color:#ff0000;">11. USB 2.0控制差分阻抗90ohm±10%，差分对内最大时延＜10mil；</font>**

**<font style="color:#ff0000;">12. USB 3.0控制差分阻抗90ohm±10%，差分对内最大时延＜3mil；</font>**



### 3.5.16  SATA3.1接口
RK3576芯片拥有2个SATA3.1 控制器，和PCIe以及USB3_OTG1控制器复用Comb PHY0/1，具体路径请见下图。

·支持SATA PM功能，每个port可以支持5个设备；

·支持SATA 1.5Gb/s，SATA 3.0Gb/s，SATA 6.0Gb/s speeds ；

·支持eSATA。

![Image](./images/OK3576C_hardware/78d253915ff345faadcd8998e3113de1.png)

SATA0 控制器使用 Comb PHY0（与 PCIe0 Controller 控制器复用）。

![Image](./images/OK3576C_hardware/e663e6eea91844d4b0aac2ca9bb67198.png)

SATA1 控制器使用 Comb PHY1（与 PCIe1 Controller 控制器以及 USB3_OTG1 控制器复用）。

![Image](./images/OK3576C_hardware/bc643117b9814cfba5ec047f5e5d00c4.png)

SATA0/1控制器相关控制IO有： 

·SATA0_ACTLED：SATA0接口有数据传输时LED闪烁控制输出； 

·SATA1_ACTLED：SATA1 接口有数据传输时LED闪烁控制输出； 

·SATA_CPDET：SATA热拔插设备的插拔检测输入； 

·SATA_MPSWIT：SATA热拔插设备的开关检测输入； 

·SATA_CPPOD：SATA 控制热拔插设备电源开关输出； 

·其中SATA_CPDET、SATA_MPSWIT、SATA_CPPOD是SATA0/1共用接口，可通过寄存器配置是SATA0还是SATA1 

·其中SATA0_ACTLED、SATA1_ACTLED复用到两个位置，一个在VCCIO6电源域，一个在VCCIO4电源域。

**<font style="color:#ff0000;">注意：</font>**

1. **<font style="color:#ff0000;">Slot设计时，外围电路及电源需要满足Spec要求；</font>**
2. **<font style="color:#ff0000;">一个SATA接口外接SATA PM时，最多只能支持5个Port，不支持多个SATA PM超过6 个Port以上；</font>**
3. **<font style="color:#ff0000;">SATA接口的TXP/N，RXP/N 差分信号上串接的10nF交流耦合电容，AC耦合电容建议使用0201封装，更低的ESR和ESL，也可减少线路上的阻抗变化；</font>**
4. **<font style="color:#ff0000;">eSATA接口座子所有信号都必须增加ESD器件，布局时靠近座子放置，ESD寄生电容不得超过0.4pF；</font>**



### 3.5.17  PCIE2.1电路
RK3576拥有2个PCIe2.1控制器，两个都只支持RC模式(RC是Root Complex缩写)，不支持EP，如下：

1. Controller 0(1Lane)，PCIe0 Controller x1 Lane(Only RC)
2. Controller 1(1Lane)，PCIe1 Controller x1 Lane(Only RC)

2个PCIe2.1控制器与SATA3.1/USB3.2_Gen1x1组成两个Combo PHY，一个是 PCIe2.1/SATA3.1

Combo PHY0、另一个是 PCIe2.1/SATA3.1/USB3.2_Gen1x1 Combo PHY1。

Controller和PHY之间的映射关系图如下：

![Image](./images/OK3576C_hardware/9a41442f01a04562bff971b57d527988.png)

PCIe0 控制器(RC)与 SATA0 控制器复用 PCIe2.1/SATA3.1 Combo PHY0；封装管脚如下图：

![Image](./images/OK3576C_hardware/911020bcf7d8463c9304cd9fd29d3c50.png)

PCIe1 控制器(RC)、SATA1 控制器、USB3 OTG1 控制器复用 PCIe2.1/SATA3.1/USB3.2_Gen1x1 

Combo PHY1；封装管脚如下图：

![Image](./images/OK3576C_hardware/5d4d4b0f091e488f9928f8bdc1483b8d.png)

PCIE0/1_REFCLKP/N 可支持输出也可支持输入，默认输出提供给 EP 设备，如下示意图：

![Image](./images/OK3576C_hardware/4d3bd48a066446d6980dfa970165b429.png)

PCIE0/1_REFCLKP/N 若做输入时，示意图如下：

![Image](./images/OK3576C_hardware/3cc4b6a541964b1490dc0f8f1acf2ead.png)

OK3576-C开发板中有一个PCIe0通道连接PCIe x1插槽支持PCIe2.0×1Lane模式。

支持PCle Gen1（2.4 GT/s）协议，另一路PCIe1复用为USB3.0功能。

PCIe0 PCIe2.0×1Lane 部分电路如下图所示：

![Image](./images/OK3576C_hardware/e6e4b7374d274b688db775782f9e0379.png)

上图为PCIE接口的12V供电控制电路。

![Image](./images/OK3576C_hardware/df64e8e1d83a4719a46896aefc92538b.png)

上图为PCIE接口3.3V供电与使能控制电路，U42是5V转3.3V降压芯片。

![Image](./images/OK3576C_hardware/9a474f67a8194c7cb32bd96a6dc70390.png)

上图是PCIEX1插槽电路设计。

**<font style="color:#ff0000;">PCIe2.1设计中请注意：</font>**

1. **<font style="color:#ff0000;">Slot设计时，外围电路及电源需要满足Spec要求；</font>**
2. **<font style="color:#ff0000;">PCIe2.1接口的TXP/N差分信号上串接的100nF交流耦合电容，AC耦合电容建议使用0201封装，更低的ESR和ESL，也可减少线路上的阻抗变化；</font>**
3. **<font style="color:#ff0000;">PCIE0/1_CLKREQN必须使用功能脚，不能用GPIO替代；</font>**
4. **<font style="color:#ff0000;">PCIE0/1_PERSTN/WAKEN/PRSNT 在 RK3576 上面不指定特定的 IO，直接使用电平匹配的 GPIO</font>**

**<font style="color:#ff0000;">口来做控制功能脚就可以；</font>**

1. **<font style="color:#ff0000;">标准的PCIe Slot：PCIEx_CLKREQN，PCIEx_WAKEN，PCIEx_PERSTN为3.3V电平；需要注意做好 RK3576 端的电平匹配；</font>**
2. **<font style="color:#ff0000;">使用 PCIe 功能的时候，复用的 SATA/USB 功能无法使用，SATA/USB 对应的功能详见其模块说明；</font>**
3. **<font style="color:#ff0000;">PCIe2.1 功能模块没有使用时，数据线 PCIE0/1_TXP/TXN、PCIE0/1_RXP/RXN 和参考时钟线PCIE0/1_REFCLKP/ REFCLKN 悬空即可；AVDD0V85 和 AVDD1V8 两路电源接地处理，注意软件对应的dts 配置需要 disable；</font>**
4. **<font style="color:#ff0000;">PCIe2.1接口匹配设计推荐如下表所示：</font>**

| **信号** | **连接方式** | **说明** |
| --- | --- | --- |
| **<font style="color:rgb(255, 0, 0);">PCIE0/1_TXP/TXN</font>** | **<font style="color:rgb(255, 0, 0);">串接100nF电容（建议0201封装）</font>** | **<font style="color:rgb(255, 0, 0);">PCIe数据输出</font>** |
| **<font style="color:rgb(255, 0, 0);">PCIE0/1_RXP/RXN</font>** | **<font style="color:rgb(255, 0, 0);">直连</font>** | **<font style="color:rgb(255, 0, 0);">PCIe数据输入</font>** |
| **<font style="color:rgb(255, 0, 0);">PCIE0/1_REFCLKP/CLKN</font>** | **<font style="color:rgb(255, 0, 0);">直连</font>** | **<font style="color:rgb(255, 0, 0);">PCIe参考时钟</font>** |
| **<font style="color:rgb(255, 0, 0);">PCIE0/1_CLKREQN</font>** | **<font style="color:rgb(255, 0, 0);">串接 0ohm 电阻</font>** | **<font style="color:rgb(255, 0, 0);">PCIe 参考时钟请求输入(RC 模式)</font>** |
| **<font style="color:rgb(255, 0, 0);">PCIE0/1_WAKEN(RK3576无该信号，用GPIO代替)</font>** | **<font style="color:rgb(255, 0, 0);">串接0ohm电阻</font>** | **<font style="color:rgb(255, 0, 0);">PCIe 唤醒输入(RC 模式)</font>** |
| **<font style="color:rgb(255, 0, 0);">PCIE0/1_PERSTN(RK3576无该信号，用GPIO代替)</font>** | **<font style="color:rgb(255, 0, 0);">串接0ohm电阻</font>** | **<font style="color:rgb(255, 0, 0);">PCIe 全局复位输出(RC 模式)</font>** |
| **<font style="color:rgb(255, 0, 0);">PCIE0/1_PRSNT(RK3576无该信号，用GPIO代替)</font>** | **<font style="color:rgb(255, 0, 0);">串接0ohm电阻</font>** | **<font style="color:rgb(255, 0, 0);">Add In Card 插入检测输入(RC 模式)</font>** |
| **<font style="color:rgb(255, 0, 0);">PCIE_BUTTONRSTN(暂时没用到)</font>** | **<font style="color:rgb(255, 0, 0);">没用，无需连接</font>** | **<font style="color:rgb(255, 0, 0);">外部物理复位PCIe Controller</font>** |


**<font style="color:#ff0000;">10.  数据走线阻抗控制差分85ohm±10%；</font>**

**<font style="color:#ff0000;">11.  时钟走线阻抗控制差分100ohm±10%</font>**

**<font style="color:#ff0000;">12.  差分对内最大时延差＜3mil；</font>**

**<font style="color:#ff0000;">13.  差分对间间距建议大于等于4倍PCI-E线宽。</font>**



### 3.5.18  视频输入接口
FET3576有两个MIPI DPHY CSI RX接口，都支持MIPI V1.2版本，每个通道最大传输速率为 2.5Gbps。

![Image](./images/OK3576C_hardware/2786718e09bf49709dc87353e8d55952.png)

![Image](./images/OK3576C_hardware/470d2d797334437198dd79b73b3b74d3.png)

**MIPI DPHY CSI1/2 RX 接口模式支持情况**： 

1. 支持 4Lane 模式，MIPI_DPHY_CSI1_RX_D[3:0]数据参考 MIPI_DPHY_CSI1_RX_CLK 
2. 支持 2Lane+2Lane 模式：

·MIPI DPHY CSI1_RX_D[1:0]数据参考 MIPI_DPHY_CSI1_RX_CLK 

·MIPI DPHY CSI2_RX_D[1:0]数据参考 MIPI_DPHY_CSI2_RX_CLK

![Image](./images/OK3576C_hardware/79ab42f0e0894db291fa9003c8de622d.png)



**MIPI DPHY CSI3/4 RX 接口模式支持情况： **

1. 支持 4Lane 模式，MIPI_DPHY_CSI3_RX_D[3:0]数据参考 MIPI_DPHY_CSI3_RX_CLK 
2. 支持 2Lane+2Lane 模式：

·MIPI DPHY CSI3_RX_D[1:0]数据参考 MIPI_DPHY_CSI3_RX_CLK 

·MIPI DPHY CSI4_RX_D[1:0]数据参考 MIPI_DPHY_CSI4_RX_CLK

![Image](./images/OK3576C_hardware/54b658d711424beba9b9c652e4369e07.png)

**MIPI_DCPHY_CSI_RX接口情况**

FET3576有一个MIPI DCPHY CSI RX Combo PHY；DPHY支持V2.0版本，CPHY支持V1.1版本。DPHY模式有4Lane，最高传输速率4.5Gbps/Lane；CPHY模式有3Trios，最高传输速5.7Gbps/Trio。

![Image](./images/OK3576C_hardware/3330712704a843c5b8060522fbdfa347.png)

**DPHY和CPHY 配置支持情况： **

MIPI DCPHY Combo PHY的TX和RX只能支持同时配置成DPHY TX、DPHY RX模式，或同时配置成 CPHY TX、CPHY RX 模式。不支持一个配置成DPHY TX一个配置成CPHY RX，或者一个配置成CPHY TX一个配置成DPHY RX。

**MIPI DCPHY工作在DPHY模式时支持情况**：

1. 支持4Lane/2Lane/1Lane模式，MIPI_DPHY_CSI0_RX[3:0]数据参考MIPI_DPHY_CSI0_RX_CLK
2. 不支持拆分成 2Lane+2Lane

**MIPI DCPHY工作在CPHY模式时支持情况：**

1. 支持0/1/2 Trio，每个Trio有Trio_A/Trio_B/Trio_C 3根线，MIPI_CPHY_CSI_RX_TRIO[2:0]_A，MIPI_CPHY_CSI_RX_TRIO[2:0]_B，MIPI_CPHY_CSI_RX_TRIO[2:0]_C。



OK3576-C默认配置为5个Camera接口，分别是：MIPI_DPHY_CSI0_RX 4Lane、MIPI_DPHY_CSI1_RX 2Lane、MIPI_DPHY_CSI2_RX 2Lane、MIPI_DPHY_CSI3_RX 2Lane、MIPI_DPHY_CSI4_RX 2Lane。原理如下图：![Image](./images/OK3576C_hardware/ec68ff4b9ae44f2da911b7f4b046ca1e.png)



**MIPI RX设计需要注意：**

**1.  走线阻抗要求差分100ohm±10%；**

**2.  走线阻抗要求单端50ohn±10%；**

**3.  差分对内最大时延差＜3mil；**

**4.  时钟与数据之间等长＜6mil；**

**5.  差分对间间距建议＞4倍MIPI线宽，至少要3倍MIPI线宽；**

**6.  MIPI与其他信号间距建议＞4倍MIPI线宽，至少要3倍MIPI线宽；**

**7.  配置为CPHY时，组内（TRIO_A\TRIO_B\TRIO_C）最大时延差＜3mil；**

**8.  组间（TRIO0\TRIO1\TRIO2）等长要求＜50mil；**

### 3.5.19  视频输出接口
RK3576芯片的VOP显示输出处理器，它从系统存储器的帧缓冲器中读取视频数据和UI 数据，执行相应的处理，如裁剪、色域空间转换、缩放和叠加，并输出到每个高速显示接口。 

有三个Port 输出，可以从DP、HDMI/eDP、MIPI DSI、LCDC(Parallel Interface)视频接口输出。

最大的视频输出能力：

1. 三屏异显方案，如4096x2160@60Hz，2560x1600@60Hz，1920x1080@60Hz；
2. 双屏异显方案，如4096x2160@120Hz，2560x1600@60Hz。

VOP 和视频接口输出路径图：

![Image](./images/OK3576C_hardware/45e326a19929466e8faccd5697432fa8.png)

OK3576-C开发板支持DP/MIPI_DSI/HDMI 三种显示输出接口。

**3.5.19.1 MIPI_DSI接口**

FET3576有一个MIPI D-PHY/C-PHY Combo PHY TX：

D-PHY支持V2.0版本，D-PHY模式有0/1/2/3 Lane，每个Lane 2根线；最高传输速率2.5Gbps/Lane。

MIPI_DPHY_TX最大分辨率支持2560x1600@60Hz。

C-PHY支持V1.1 版本，C-PHY模式有0/1/2 Trio，每个Trio A/B/C 3根线；最高传输速率 1.7Gsps/Trio。

MIPI_CPHY_TX最大分辨率支持2560x1600@60Hz。

![Image](./images/OK3576C_hardware/cfa21d5a79d14ac9b84d9fa2af27756f.png)

**DPHY和CPHY配置支持情况**： 

MIPI D-PHY/C-PHY Combo PHY的TX和RX只能支持同时配置成DPHY TX，DPHY RX模式或同时配置成CPHY TX，CPHY RX模式，不支持一个配置成DPHY TX，一个配置成CPHY RX；

**MIPI DCPHY工作在D-PHY时模式支持情况**：

支持4Lane模式，MIPI_DPHY_TX_D[3：0]数据参考MIPI_DPHY_TX_CLK。

**MIPI DCPHY工作在C-PHY时模式支持情况： **

支持0/1/2 Trio，每个Trio A/B/C 3根线，MIPI_CPHY_TX_TRIO[2：0]_A，

MIPI_CPHY_TX_TRIO[2：0]_B， MIPI_CPHY_TX_TRIO[2：0]_C。

OK3576-C开发板的MIPI_DSI接口采用1组时钟通道+ 4组数据通道模式，原理图如下：

![Image](./images/OK3576C_hardware/1e606f22de494dd68338f94b39dd59bd.png)

![Image](./images/OK3576C_hardware/6aa529d3edf14a68a449d58cacdaa72c.png)

**设计时需注意：**

**1.  走线阻抗控制差分100ohm±10%；**

**2.  差分对内最大时延差＜3mil；**

**3.  时钟与数据之间等长＜6mil；**

**4.  差分对间间距建议大于等于4倍MIPI线宽，至少要3倍MIPI线宽；**

**5.  MIPI与其他信号间距建议大于等于4倍MIPI线宽，至少要3倍MIPI线宽；**

**6.  配置为CPHY时，单端走线阻抗控制50ohm±10%；**

**7.  组内(TRIO_A\TRIO_B\TRIO_C)最大时延差＜3mil；**

**8.  组间(TRIO0\TRIO1\TRIO2)等长要求＜50mil；**

**9.  各信号所允许过孔数量建议不超过2个；**

**10.  对间间距建议大于等于4倍MIPI线宽；**

**11.  MIPI与其它信号间距建议大于等于4倍MIPI线宽。**

**3.5.19.2 HDMI_TX接口**

RK3576内置一个HDMI/eDP TX Combo PHY。

HDMI/eDP TX Combo PHY支持以下两个模式：

1. HDMI TX 模式：最高支持HDMI2.1，支持HDMI FRL模式并向下兼容HDMI TMDS模式，支持RGB/YUV444/YUV422/YUV420(Up to 10bit)格式。
2. eDP TX模式：最高支持eDP1.3，最大分辨率支持4K@60Hz，支持RGB/YUV444/YUV422(Up to 10bit)格式。

![Image](./images/OK3576C_hardware/1144a00583e04e238fcc6e9556a05b60.png)

RK3576支持HDMI2.1并向下HDMI2.0，HDMI1.4兼容，由于HDMI2.1工作在FRL模式，切换到HDMI2.0及以下模式时，工作在TMDS模式，因采用AC耦合电压模式驱动器。

如下图所示，AC耦合电容容值采用220nF，不得随意更改，交流耦合电容建议使用0201封装，更低的ESR和ESL，也可减少线路上的阻抗变化。

工作在HDMI2.1模式，HDMI_TX_ON_H配置为低电平， Q15，Q16，Q17，Q18不导通。

工作在HDMI2.0及以下模式时，HDMI_TX_ON_H配置为高电平，Q15，Q16，Q17，Q18导通，对地499ohm电阻与Sink端上拉50ohm电阻形成一个直流偏置，大约3V。

**<font style="color:#ff0000;">设计时需注意：</font>**

**<font style="color:#ff0000;">1.  如果只需要支持HDMI2.0及以下模式时，Q15，Q16，Q17，Q18也不能省掉，需要保证机器在未开机时，管子不能导通，因为HDMI CTS Test ID 7-3 TMDS Voff测试项目要求在DUT未上电，Voff电压必须在AVcc+-10mV以内，否则这个测试项无法通过。</font>**

![Image](./images/OK3576C_hardware/de99283558814d00ab5dfc8bedcac83a.png)

FRL模式：在传统的TMDS 架构下，是利用一个独立的通道来传送Clock，但在FRL的架构中，将Clock嵌入在Data的通道中，在Sink端透过Clock Recovery解析出Clock。

下表为FRL速率与通道关系：

| 通道速率 | 通道数 |
| :---: | :---: |
| 3Gbps | 3 |
| 6Gbps | 3 |
| 6Gbps | 4 |
| 8Gbps | 4 |
| 10Gbps | 4 |
| 12Gbps | 4 |


支持ARC/eARC通过HDMI_TX_SBD_P/ HDMI_TX_SBD_N信号到RK3576内部解析出音频数据。

![Image](./images/OK3576C_hardware/b7f2bdbd166f4798b7849a17203dd130.png)

HDMI_TX_HPD是HDMI TX控制器复用到普通GPIO上，电平随所在电源域电压，电源域供电电压有更改，外围电路的上拉电阻电源也必须同步调整。

HDMI_TX_CEC是HDMI控制器CEC功能复用到普通GPIO上功能，电平随所在电源域电压，电源域供电电压有更改，外围电路的上拉电阻电源也必须同步调整。

CEC协议规定是3.3V电平，但是协议要求，往CEC管脚通过27K电阻加3.3V电压，漏电不允许超过1.8uA。



RK3576 IO Domain在未上电时，如果IO上有电压，IO会存在漏电，比如RK3576已经断电了，然后HDMI线还连接着Sink端（电视或显示器），此时Sink端的CEC有电，会通过HDMI线漏电到RK3576 IO上，会造成CEC漏电超过1.8uA，因此外部需要增加一个隔离电路，R189阻值不得随意修改，需要使用27Kohm，Q19默认选择2SK3018，如果要换其它型号，结电容必须相当，如果用结电容过大，不仅会影响工作，认证也会过不了。

![Image](./images/OK3576C_hardware/38f259c4222040d88a1fee40277c22ba.png)

HDMI_TX _SCL/ HDMI_TX _SDA是HDMI TX控制器的I2C/DDC总线，功能复用到普通GPIO上，电平随所在电源域电压，电源域供电电压有更改，外围电路的上拉电阻电源也必须同步调整。

DDC_SCL/DDC_SDA协议规定是5V电平，RK3576 IO不支持5V电平，必须增加电平转换电路，不得删减，默认使用MOS管电平转换，MOS型号默认选择2SK3018，如果要换其它型号，结电容必须相当，如果用结电容过大，不仅影响工作，认证也会过不了。

上拉电阻建议参考照默认值，不要随意修改。

D6二极管不得删减，用来防止Sink端漏电到VCC_5V0。

SDA信号电平转换的MOS栅极和电源之间串拉1K，MOS栅极和源极之间并一个100pF改善时序，不得删除。

![Image](./images/OK3576C_hardware/d419ab16f2ea4ce5b17d249c05787ea7.png)

HDMI座子的Pin18电压需保证在4.8-5.3V之间，管脚需放置1uF去耦电容，不得删减，布局时，靠近HDMI座子管脚放置。

为加强抗静电能力，信号上必须预留ESD器件，HDMI2.1信号的ESD寄生电容不得超过0.2pF，

其它信号的ESD寄生电容建议使用不超过1pF。

**设计时需注意：**

**1.  控制MOS管Coss不能过大，否则会影响信号质量，建议按参考图型号或相应的Coss值。**

**2.  走线阻抗控制差分100ohm±10%；**

**3.  差分对内最大时延差＜3mil；**

**4.  差分对间等长要求＜200mil；**

**5.  差分对间间距建议大于等于7倍HDMI线宽；**

**6.  HDMI与其他信号间距建议大于等于7倍HDMI线宽；**

**7.  建议不加过孔；**

**8.  I/O对地电容不超过0.2pF。**



**3.5.19.2 DP_TX接口**

RK3576支持一个DP1.4 TX PHY（和USB3 OTG0 Combo），最大输出分辨率可达4K@YUV422-120Hz。

·每个Lane速率可支持1.62/2.7G/5.4/8.1Gbps；

·支持1Lane或2Lane或4Lane模式；

·支持RGB/YUV444/YUV422/YUV420 (up to 10bit)格式；

·支持Multi Stream Transport(MST)。

![Image](./images/OK3576C_hardware/a3bc3a45f2c940249350e0a0e32aaf13.png)

·支持Swap on和Swap off两种模式

![Image](./images/OK3576C_hardware/be61200b5c45485e83fc3c3a92e83cb3.png)

·支持3 Channels的MST(Multi-Stream Transport)显示。MST支持三屏异显最大能力为：4096x2160@60Hz、2560x1600@60Hz、1920x1080@60Hz。

![Image](./images/OK3576C_hardware/9dab7aad23074119827c052673fd9e9b.png)

与USB引脚复用关系请查看3.5.15章节。

**设计DP时需要注意：**

**1.  DP0_TX_D0P/DON、DP0_TX_D1P/D1N、DP0_TX_D2P/D2N、DP0_TX_D3P/D3N、**

**DP1_TX_D0P/DON、DP1_TX_D1P/D1N、DP1_TX_D2P/D2N、DP1_TX_D3P/D3N需要串接的100nF交流耦合电容，交流耦合电容建议使用0201封装，更低的ESR和ESL，也可减少线路上的阻抗变化，布局时，靠近FET3576--C管脚放置；**

**2.  走线阻抗控制差分100ohm±10%（只作为DP接口，无复用），差分95ohm±10%（USB3.0/DP1.4复用）；**

**3.  差分对内时延差＜3mil；**

**4.  差分对间等长要求＜500mil；**

**5.  差分对间间距建议大于等于6倍DP线宽；**

**6.  DP与其它信号间距建议大于等于6倍DP线宽；**

**7.  各信号所允许过孔数量建议不超过2个；**

**8.  I/O对地电容不超过0.2pF**

### 3.5.20  WIFI/BT模块电路
OK3576-C板载一颗海华AW-CM358SM WIFI&BT模块，支持WIFI 2.4G/5G/蓝牙5.0；WIFI/BT天线使用SMA接口引出，SDIO、PDM、UART接口与主控连接。原理图如下：

![Image](./images/OK3576C_hardware/dd0cc4f3fde740cea1d55092fe45265c.png)![Image](./images/OK3576C_hardware/6ce7b2908751409591f964d2c4b65b6d.png)

**注意：**

**1、WIFI模块供电电源需要受控，参考底板电路；**

**2、SDIO阻抗要求： 单端50ohm，信号等长控制50mil；**

1. **I2C要求**

一组I2C总线上可以挂载多个从设备，请保证地址无冲突；

I2C总线上需要加上拉电阻，但不要使用多个电阻上拉；

请注意核心板端的I2C和从设备的I2C做电平匹配。

2. **USB设计**

为满足USB眼图要求，USB3.0 TX/RX的PCB线长不应该超过6 inches。

3. **核心板不使用的信号引脚可以悬空，但请务必将所有的GND连接。**
4. **上电时序**

强烈建议用户设计底板时参考开发板设计，使用核心板输出的CARRIER_BOARD_EN作为底板上电的使能，严格控制上电时序。否则可能会造成以下影响：

·通电阶段电流过大；

·设备无法启动；

·最坏情况，对处理器造成不可逆转的损坏。

**注意：详细硬件设计资料请阅读《FET3576-C_硬件设计指南》文档。**

核心板连接器尺寸规格如下：

A=21.52mm、B=19.6mm、C=3.2mm、Contacts=100

![Image](./images/OK3576C_hardware/2f3a8c1f8bbd47bf94dcb40e4caf90ca.png)





对应底板连接器尺寸规格如下：

A=22.6mm、B=19.6mm、C=3.2mm、D=1.45mm、Contacts=100

![Image](./images/OK3576C_hardware/450a473a6dd040f8b83fba358030292f.png)



表1 Linux系统下整机功耗表

| 编号 | 测试项目 | 核心板功率(W) | 开发板功率(含核心板)(W) |
| --- | --- | --- | --- |
| <font style="color:black;">1</font> | <font style="color:black;">无负载启动峰值功率</font> | <font style="color:black;">3.66</font> | <font style="color:black;">5.88</font> |
| <font style="color:black;">2</font> | <font style="color:black;">无负载待机功率</font> | <font style="color:black;">0.82</font> | <font style="color:black;">2.33</font> |
| <font style="color:black;">3</font> | <font style="color:black;">CPU+GPU+内存+eMMC压力测试</font> | <font style="color:black;">5.87</font> | <font style="color:black;">7.39</font> |
| <font style="color:black;">4</font> | <font style="color:black;">7寸液晶屏+4G+U盘+视频解码</font> | <font style="color:black;">2.02</font> | <font style="color:black;">10.02</font> |
| <font style="color:black;">5</font> | <font style="color:black;">7寸液晶屏+4G+U盘+视频编码</font> | <font style="color:black;">3.06</font> | <font style="color:black;">10.48</font> |
| <font style="color:black;">6</font> | <font style="color:black;">Pwron Key 长按关机</font> | <font style="color:black;">0.28</font> | <font style="color:black;">0.32</font> |
| <font style="color:black;">7</font> | <font style="color:black;">Pwron Key 短按休眠</font> | <font style="color:black;">TBD</font> | <font style="color:black;">TBD</font> |


**注：**

1. <font style="color:black;"测试条件：核心板配置是4GB内存+32GB eMMC，4G模组移远EM05-CE，屏幕是飞凌选配产品。核心板是12V供电，底板是12V供电。   
2. 峰值功率:启动过程中的电流峰值乘以供电电压   
3. 待机功率:启动后停留在开机界面时的电流值乘以供电电压。   
4. 功耗仅供参考

![Image](./images/OK3576C_hardware/6cd409726e144fb787e6c8ce3ea7d662.png)![Image](./images/OK3576C_hardware/87b7a821411b4fa68699c630c51f72ab.png)![Image](./images/OK3576C_hardware/2a09a9be398d4ed4900833577d403111.png)![Image](./images/OK3576C_hardware/74ef1fc3a58b41da9d7b5410cc0ba9eb.png)![Image](./images/OK3576C_hardware/59e667504742475a987c1ecb9645a0fa.png)![Image](./images/OK3576C_hardware/faf4ae7240a443c08ecbbe7972823b48.png)![Image](./images/OK3576C_hardware/a1fb6b325f1144619524611092751a89.png)![Image](./images/OK3576C_hardware/20ba5d44ba4540129c00cc6e288fb336.png)![Image](./images/OK3576C_hardware/98cbfc4135b14bd6b37bb69a9f03be6e.png)![Image](./images/OK3576C_hardware/5474d0bae918457a860347cae5ec8c60.png)![Image](./images/OK3576C_hardware/be59f1df5d2647459ca8d20bd1810bf9.png)![Image](./images/OK3576C_hardware/2a8b6938e6da47078ec83d13fd5550ae.png)![Image](./images/OK3576C_hardware/cc2a8ca796934c5891f6c6ae3ba5b628.png)![Image](./images/OK3576C_hardware/2b791e9781c14564a31ee136a9fa58da.png)![Image](./images/OK3576C_hardware/541ed216c5f54e96b85ddbedc4714863.png)![Image](./images/OK3576C_hardware/49db14b25ace48eda80bfeee12eb666b.png)![Image](./images/OK3576C_hardware/938c01c0b986443198d78efab07cf602.png)![Image](./images/OK3576C_hardware/41cde6252184463fba3d48247cf83ec2.png)![Image](./images/OK3576C_hardware/c5f5374600e54690a88f51fa87e83292.png)![Image](./images/OK3576C_hardware/48011e4355b845f283eec61b54f07f67.png)

上图仅为示意图，具体连接情况请见源文件原理图。为满足核心板的正常工作，最小系统包括核心板供电电源，系统烧写电路，以及调试串口电路。



# 01_RK3576简介

RK3576是一颗高性能、低功耗的应用处理器芯片，集成了4个Cortex-A72和4个Cortex-A53及独立的NEON协处理器；适用于ARM PC、边缘计算、个人移动互联网设备及其它多媒体产品。

RK3576内置了多种功能强大的嵌入式硬件引擎，为高端应用提供了优异的性能，支持4K@120fps 的H.265、VP9、AVS2和AV1解码器，支持4k@60fps的H.264解码器；还支持4K@60fps的H.264 和H.265编码器，高质量的JPEG编码器/解码器，专门的图像预处理器和后处理器。

内置3D GPU，能够完全兼容OpenGL ES1.1/2.0/3.2、OpenCL 2.0和Vulkan1.1。带有MMU的特殊2D硬件引擎将最大限度地提高显示性能，并提供流畅的操作体验。

引入了新一代完全基于硬件的最大16M像素ISP（图像信号处理器），实现了多种算法加速器，如HDR、3A、CAC、3DNR、2DNR、锐化、去雾、增强、鱼眼校正、伽马校正等。

内嵌的NPU支持INT4/INT8/INT16/FP16/BF16/TF32混合运算。此外，凭借其强大的兼容性，可以轻松转换基于TensorFlow/MXNet/PyTorch/Caffe等一系列框架的网络模型。

RK3576具有高性能的外部存储器接口（LPDDR4/LPDDR4X/LPDDR5），能够支持苛刻的存储器带宽（能够支持存储器高带宽要求的系统），还提供了一套完整的外设接口，以灵活支持各类应用。

目标应用有:

+ 信息发布终端
+ 智能座舱
+ 智慧大屏
+ AR/VR
+ 边缘计算
+ 高端IPC
+ 智能NVR、
+ 高端平板
+ ARM PC

……

**RK3576处理器框图**

![Image](./images/OK3576C_hardware/0670391ab6534230aede3ea9e26b9868.png)



# 02_FET3576-C核心板介绍

## 2.1  FET3576-C核心板外观图
![Image](./images/OK3576C_hardware/4f8192591c6345b28917a806d32b2885.png)

**核心板正面视图**

![Image](./images/OK3576C_hardware/361c5272c28d45c58b73ad736e028066.png)

**核心板反面视图**

## 2.2  FET3576-C 核心板框图
![Image](./images/OK3576C_hardware/67bbd894eb35475086ac27181de438c4.png)

**核心板框图**



## 2.3  FET3576-C核心板尺寸图
FET3576-C核心板尺寸图如下： 

![Image](./images/OK3576C_hardware/1b8554b0e9fd4294a0ba44d3349e636f.png)

**顶层尺寸图**

![Image](./images/OK3576C_hardware/c9d3447b465546be9ad438beb6c92363.png)

**底层尺寸图**

单位：mm![Image](./images/OK3576C_hardware/679223260c33478eaf0b7de83224e418.png)

结构尺寸：68mm×50mm，尺寸公差±0.15mm；更多详细尺寸请见用户资料dxf结构文件。

制版工艺：厚度1.6mm，10层沉金 PCB。

连接器：四个0.4mm间距，100pin 板对板连接器。连接器尺寸图见附录。

核心板的四角预留了四个直径2.2mm的安装孔，产品使用在震动环境的客户可以安装固定螺丝，提高产品连接的可靠性。

用户可以参考开发板设计，在底板使用M2，L=1.5mm的贴片螺母，贴片螺母的规格参见下图

![Image](./images/OK3576C_hardware/e1bbcd19a64f483a8ca0679afb0b8a85.png)

![Image](./images/OK3576C_hardware/9e128ca24ffc4042bff00c58c7aff308.png)

## 2.4 性能参数
### 2.4.1  系统主频
| **名称** | **规格** | | | | **说明** |
| :---: | :---: | --- | --- | --- | :---: |
| | **最小** | **典型** | **最大** | **单位** |
| 系统主频Arm® Cortex®-A72 | - | - | 2300 | MHz | - |
| 系统主频Arm® Cortex®-A53 | - | - | 2200 | MHz |  |
| 系统主频Arm® Cortex®-M0 | - | - | - | - | - |


### 2.4.2  供电参数
| **参数** | **引脚标号** | **规格** | | | | **说明** |
| :---: | :---: | :---: | --- | --- | --- | :---: |
| | | **最小** | **典型** | **最大** | **单位** |
| 主电源电压 | 12V | 11.5 | 12 | 12.4 | V | - |


### 2.4.3  工作环境
| **参数描述** | | **规格** | | | | **说明** |
| :---: | --- | :---: | --- | --- | --- | :---: |
| | | **最小** | **典型** | **最大** | **单位** |
| 工作温度 | 工作环境 | 0 | 25 | 80 | ℃ | 商业级 |
|  | 存储环境 | -40 | 25 | +125 | ℃ |  |
| 湿度 | 工作环境 | 10 | - | 90 | ％RH | 无凝露 |
|  | 存储环境 | 5 | - | 95 | ％RH |  |


### 2.4.4  核心板接口速度
| **参数** | **规格** | | | | **说明** |
| :---: | :---: | --- | --- | --- | :---: |
| | **最小** | **典型** | **最大** | **单位** |
| 串口通讯速度 | - | 115200 | 4M | bps | - |
| SPI时钟频率 | - | - | 50 | MHz | - |
| I2C通讯速度 | - | 100 | 400 | Kbps | - |
| USB3.0接口速度 | - | - | 5 | Gbps | - |
| USB2.0接口速度 | - | - | 480 | Mbps | - |
| CAN通讯速度 | - | - | 1 | Mbps | - |
| PCIe2.1 | - | - | 5 | Gbps | - |


### 2.4.5  ESD特性
| 参数 | 规格 | | 单位 | 适用范围 |
| :---: | :---: | --- | :---: | :---: |
| | 最小 | 最大 | |
| ESD HBM(ESDA/JEDEC JS-001-2017) | -2000 | 2000 | V | 核心板所有引出信号 |
| ESD CDM(ESDA/JEDEC JS-002-2018) | -250 | 250 | V | 核心板所有引出信号 |


注：

1、以上数据由瑞芯微官方提供；

2、核心板所有引出信号均为静电敏感信号，在底板设计时应对接口做好静电防护，并在核心板运输、组装、使用过程中注意做好静电防护。

## 2.5  核心板接口资源
FET3576-C核心板接口资源支持如下表：

| **功能** | **数量** | **参数** |
| :---: | :---: | --- |
| MIPI CSI | 5 | ·支持 5 个 CSI-2 接口   ·其中 4 个接口为 2 个 D-PHY v1.2 data-lane，2.4Gbps/lane   ·这 4 个接口可以组合成 2 个拥有 4 data-lane 接口   ·另外 1 个接口支持 4 D-PHY data-lane 或者 3 C-PHY trios   ·D-PHY v2.0，lane speed is 4.5Gbps   ·C-PHY v1.1，trio speed is 2.4Gsps |
| DVP | 1 | ·8/10/12/16-bit 标准DVP接口，最高150MHz数据输入；   ·支持 BT.601/BT.656 和 BT.1120 VI 接口； |
| HDMI/eDP TX | 1 **<font style="color:#ff0000;">*</font>**<sup>**<font style="color:#ff0000;">1</font>**</sup> | ·支持1 个 HDMI / eDP TX 组合接口   ·HDMI 接口   ·HDMI v2.1   ·最高支持 4K@120Hz   ·支持数据格式：RGB/YUV444/YUV422/YUV420 8/10-bit   ·支持 CEC和ARC   ·HDCP v2.3 和 HDCP v1.4   ·eDP接口   ·eDP v1.3   ·Main link containing 4 physical lanes   ·最高支持 4K@60Hz   ·HDCP v1.3 |
| DP TX | 1 **<font style="color:#ff0000;">*</font>**<sup>**<font style="color:#ff0000;">1</font>**</sup> | ·支持1 路 USB / DP 组合接口   ·USB 接口   ·USB 3.2 Gen1x1   ·Dual-Role Device(DRD)   ·DisplayPort TX 接口   ·DisplayPort v1.4   · Supports 1/2/4 lanes with lane speed including 1.62、2.7、5.4 and 8.1Gbps   ·支持最高 4K@120Hz   ·支持数据格式：RGB/YUV444/YUV422/YUV420 8/10-bit   ·支持 Multi-Stream Transport (MST) with 3 displays   ·支持 DP Altmode on USB Type-C   ·支持 HDCP v2.3 and HDCP v1.3 |
| MIPI DSI | 1 **<font style="color:#ff0000;">*</font>**<sup>**<font style="color:#ff0000;">1</font>**</sup> | ·支持 1 个MIPI DSI-2 TX 接口   ·D-PHY v2.0 or C-PHY v1.1   ·4 data lanes on D-PHY   ·3 data trios on C-PHY   ·支持最高 2560 x 1600@60Hz   ·支持数据格式：RGB (up to 10bit) |
| Parallel | 1 **<font style="color:#ff0000;">*</font>**<sup>**<font style="color:#ff0000;">1</font>**</sup> | ·支持 1 个并行输出接口   ·支持 RGB/BT.656/BT1120   ·最高支持 1920 x 1080@60Hz   ·支持数据格式：RGB (up to 10bit) |
| EBC | 1 **<font style="color:#ff0000;">*</font>**<sup>**<font style="color:#ff0000;">1</font>**</sup> | ·支持 1 个 EBC 输出接口   ·支持 E-ink EPD (Electronic paper Display)   ·支持 2560 x 1920 硬解码   ·支持数据总线宽度：16-bit   ·支持高达 32 level gray scale   ·支持 Direct mode、LUT mode、3-window mode   ·支持 window display mode |
| SAI | ≤5 | ·支持 5 个 SAI 接口   ·SAI 0/1 支持 4 TX lanes 和 4 RX lanes   ·SAI 2/3/4 支持 1TX lane 和 1 RX lane   ·支持 I2S/TDM/PCM 模式 **<font style="color:#ff0000;">*</font>**<sup>**<font style="color:#ff0000;">2</font>**</sup>   ·支持最高采样率：192KHz   ·支持音频分辨率：16bits 到 32bits |
| SPDIF TX | ≤2 | ·支持 2 路 SPDIF TX 端口 |
| SPDIF RX | ≤2 | ·支持 2 路 SPDIF RX 端口 |
| PDM | ≤2 | ·最高 8 channels，音频分辨率从16 ~24 位，采样率达192KHz   ·支持PDM主接收模式 |
| Ethernet | ≤2 | ·2路GMAC，提供RGMII / RMII接口引出   ·支持10/100/1000Mbps数据传输速率 |
| Combo high speed interface | 2 | ·支持 1 个 PCIe2.1/SATA3.1 interface with one data lane   ·支持 1 个 PCIe2.1/SATA3.1/USB3.2 Gen1x1 interface with one data lane |
| USB 2.0 OTG | 2 | ·支持两路USB2.0 OTG |
| SDIO | ≤2 | ·SDIO v3.0，4-bit data bus widths |
| SPI | ≤5 | ·支持 two chip-select in each interface   ·支持 serial-master 和 serial-slave mode |
| I2C | ≤9 | ·支持7位和10位地址模式   ·标准模式数据传输速率100k bits/s，在快速模式下400k bits/s |
| I3C | ≤2 | ·支持 2 个 I3C master ports |
| UART | ≤12 | ·内置2路64 bit FIFO，可分别用于TX和RX   ·支持5位、6位、7位、8位串行数据收发，波特率高达4Mbps   ·12路UART均支持自动流控模式   ·12路UART均支持RS485模式 |
| CAN | ≤2 | ·遵循 CAN 和 CAN FD 规范   ·支持CAN标准帧和扩展帧收发   ·支持8192-bit receive FIFO |
| DSMC | ≤1 | ·Supports up to select 4 chips   ·Supports 8-wire and 16-wire serial transfer mode   ·Supports configurable serial address width:16 bits or 32 bits |
| FlexBus | ≤1 | ·Supports built-in DMA and ping-pong operation for allocating two address   ·Supports transmission and receiving mode   ·Supports single mode and continuous mode |
| PWM | ≤16 | ·最高支持16个片上PWM，具有基于中断的操作，支持捕获模式 |
| ADC | ≤8 | ·支持8路12bit单端输入SAR-ADC，采样率高达1MS/s |
| GPIO | n | ·所有的 GPIO 可以被用于生成中断   ·支持电平触发和边沿触发中断   ·支持配置电平触发极性   ·支持上升沿触发、下降沿触发和双沿触发中断   ·支持配置上下拉（弱上拉和弱下拉）   ·支持配置驱动能力 |


注：表中参数为硬件设计或CPU理论值。

接口存在GPIO复用，为理论最大数量。

*1 Video Port

·Video Port0 supports up to 4K@120Hz with 10 bit data

  ·Video Port1 supports up to 2560x1600@60Hz with 10-bit data

  ·Video Port2 supports up to 1920x1080@60Hz with 8-bit data

  ·Each Video Port may connect to any of HDMI/eDP/DP/DSI-2

  ·Port1 and Port2 may connect to parallel output interface

*2 单根 TDM 设计时钟最高 50MHz，使用 TDM 模式时，可以结合音频采样频率、分辨率来计算理论可支持的音频通道数，看是否满足项目需求。

## 2.6  FET3576-C核心板引脚定义
### 2.6.1  FET3576-C核心板引脚原理图
![Image](./images/OK3576C_hardware/e97fda686e244204ae690ad984b42cad.png)

![Image](./images/OK3576C_hardware/5c67fe3cb57d43aa926358904ede537d.png)

![Image](./images/OK3576C_hardware/99350f75161c4efbad3510b5b0b7c03a.png)

![Image](./images/OK3576C_hardware/23bd375a3ddb4c279b4f25c420797a6a.png)



### 2.6.2  FET3576-C核心板引脚功能说明
**注1：**

**Num ——** 核心板连接器引脚序号

**Ball ——**CPU引脚球号

**GPIO ——** CPU引脚通用I/O口序号

**Vol  ——**引脚信号电平

**注2：**

**信号名称 ——**核心板连接器网络名称，信号右上角角标含义如下图：

| **角标序号** | **角标含义** |
| :---: | --- |
| [1] | 引脚可配置为中断使用 |
| [2] | 引脚默认电平为1.8V |
| [3] | 引脚为CPU启动相关引脚，不推荐作为IO使用 |
| [4] | 专用引脚，不能作为IO使用 |


**引脚描述 ——**核心板引脚信号名称描述  

**默认功能 ——**核心板所有引脚功能均按下表的“默认功能”作了规定，请勿修改，否则可能和出厂 驱动冲突。如有疑问，请及时联系我们的销售或技术支持。

**注3: “默认功能”一栏中标明“底板勿用”的引脚是核心板使用的引脚，底板设计时不可使用**

**表1 P1连接器接口（奇）引脚定义**

| **NUM** | **BALL** | **信号名称** | **GPIO** | **VOL** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| 1 | —— | GND | —— | —— | 地 | GND |
| 3 | B25 | SDMMC_D1 |  | 1.8V/3.3V | SD/MMC接口数据信号1 | SDMMC_D1 |
| 5 | B24 | SDMMC_D0 |  | 1.8V/3.3V | SD/MMC接口数据信号0 | SDMMC_D0 |
| 7 | 1B21 | SDMMC_CLK |  | 1.8V/3.3V | SD/MMC接口时钟信号 | SDMMC_CLK |
| 9 | 1A21 | SDMMC_CMD |  | 1.8V/3.3V | SD/MMC接口命令信号 | SDMMC_CMD |
| 11 | B23 | SDMMC_D3 |  | 1.8V/3.3V | SD/MMC接口数据信号3 | SDMMC_D3 |
| 13 | A23 | SDMMC_D2 |  | 1.8V/3.3V | SD/MMC接口数据信号2 | SDMMC_D2 |
| 15 | —— | GND | —— | —— | 地 | GND |
| 17 | 2U12 | HDMI_TX_SBDN | —— | —— | HDMISBD信号- | HDM0_TX_SBD_N |
| 19 | 2T12 | HDMI_TX_SBDP | —— | —— | HDMISBD信号+ | HDM0_TX_SBD_P |
| 21 | —— | GND | —— | —— | 地 | GND |
| 23 | AK26 | HDMI_TX_D3N | —— | —— | HDMI差分信号3- | HDMI_TX_D3_N |
| 25 | AL26 | HDMI_TX_D3P | —— | —— | HDMI差分信号3+ | HDMI_TX_D3_P |
| 27 | —— | GND | —— | —— | 地 | GND |
| 29 | AK27 | HDMI_TX_D0N | —— | —— | HDMI差分信号0- | HDMI_TX_D0_N |
| 31 | 1AE24 | HDMI_TX_D0P | —— | —— | HDMI差分信号0+ | HDMI_TX_D0_P |
| 33 | —— | GND | —— | —— | 地 | GND |
| 35 | AL28 | HDMI_TX_D1N | —— | —— | HDMI差分信号1- | HDMI_TX_D1_N |
| 37 | AK28 | HDMI_TX_D1P | —— | —— | HDMI差分信号1+ | HDMI_TX_D1_P |
| 39 | —— | GND | —— | —— | 地 | GND |
| 41 | AK29 | HDMI_TX_D2N | —— | —— | HDMI差分信号2- | HDMI_TX_D2_N |
| 43 | AJ28 | HDMI_TX_D2P | —— | —— | HDMI差分信号2+ | HDMI_TX_D2_P |
| 45 | —— | GND | —— | —— | 地 | GND |
| 47 | —— | —— | —— | —— |  |  |
| 49 | —— | —— | —— | —— |  |  |
| 51 | —— | GND | —— | —— | 地 | GND |
| 53 | —— | —— | —— | —— |  |  |
| 55 | —— | —— | —— | —— |  |  |
| 57 | —— | GND | —— | —— | 地 | GND |
| 59 | —— | —— | —— | —— |  |  |
| 61 | —— | —— | —— | —— |  |  |
| 63 | —— | GND | —— | —— | 地 | GND |
| 65 | —— | —— | —— | —— |  |  |
| 67 | —— | —— | —— | —— |  |  |
| 69 | —— | GND | —— | —— | 地 | GND |
| 71 | —— | —— | —— | —— |  |  |
| 73 | —— | —— | —— | —— |  |  |
| 75 | —— | GND | —— | —— | 地 | GND |
| 77 | —— | —— | —— | —— |  |  |
| 79 | —— | —— | —— | —— |  |  |
| 81 | —— | GND | —— | —— | 地 | GND |
| 83 | —— | —— | —— | —— |  |  |
| 85 | —— | —— | —— | —— |  |  |
| 87 | —— | GND | —— | —— | 地 | GND |
| 89 | —— | —— | —— | —— |  |  |
| 91 | —— | —— | —— | —— |  |  |
| 93 | —— | GND | —— | —— | 地 | GND |
| 95 | —— | —— | —— | —— |  |  |
| 97 | —— | —— | —— | —— |  |  |
| 99 | —— | GND | —— | —— | 地 | GND |


**表2 P1连接器接口（偶）引脚定义**

| **NUM** | **BALL** | **信号名称** | **GPIO** | **VOL** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| 2 | —— | GND | —— | —— | 地 | GND |
| 4 | —— | —— | —— | —— | —— | —— |
| 6 | —— | —— | —— | —— | —— | —— |
| 8 | —— | GND | —— | —— | 地 | GND |
| 10 | —— | —— | —— | —— | —— | —— |
| 12 | —— | —— | —— | —— | —— | —— |
| 14 | —— | GND | —— | —— | 地 | GND |
| 16 | —— | —— | —— | —— | —— | —— |
| 18 | —— | —— | —— | —— | —— | —— |
| 20 | —— | GND | —— | —— | 地 | GND |
| 22 | —— | —— | —— | —— | —— | —— |
| 24 | —— | —— | —— | —— | —— | —— |
| 26 | —— | GND | —— | —— | 地 | GND |
| 28 | A25 | SARADC_VIN0_BOOT | —— | 1.8V | BOOT启动配置输入 | SARADC_VIN0_BOOT |
| 30 | 1A22 | SARADC_VIN1_KEY/RECOVERY | —— | 1.8V | <font style="color:rgb(255, 0, 0);">通用ADC1</font> | SARADC_VIN1_KEY/RECOVERY |
| 32 | 1B19 | SARADC_VIN2_HW_ID | —— | 1.8V | 通用ADC2 | SARADC_VIN2_HW_ID |
| 34 | 1C19 | SARADC_VIN3_HP_HOOK | —— | 1.8V | <font style="color:rgb(255, 0, 0);">通用ADC3</font> | SARADC_VIN3_HP_HOOK |
| 36 | 1E18 | SARADC_VIN4 | —— | 1.8V | 通用ADC4 | SARADC_VIN4 |
| 38 | 1D19 | SARADC_VIN5 | —— | 1.8V | 通用ADC5 | SARADC_VIN5 |
| 40 | 1D21 | SARADC_VIN6 | —— | 1.8V | 通用ADC6 | SARADC_VIN6 |
| 42 | 1E19 | SARADC_VIN7_LCD_ID | —— | 1.8V | 通用ADC7 | SARADC_VIN7_LCD_ID |
| 44 | —— | GND | —— | —— | 地 | GND |
| 46 | B19 | HDMI_TX_ON_H |  | 3.3V | HDMI_TX开启信号 | HDMI_TX_ON_H |
| 48 | B20 | TYPEC_DPTX_AUX_PUPDCTL2 |  | 3.3V | TYPEC_DPTX_AUX_PUPDCTL22信号 | TYPEC_DPTX_AUX_PUPDCTL2 |
| 50 | 1C18 | GPIO2_B5_d |  | 3.3V | USB_HUB_RST_3V3复位信号 | USB_HUB_RST_3V3 |
| 52 | AK3 | HDMI_TX_CEC_M0 |  | 3.3V | HDMICEC信号 | HDMI_TX_CEC_M0 |
| 54 | 1A19 | CAN1_RX_M3 |  | 3.3V | CAN1数据接收 | CAN1_RX_M3_3V3 |
| 56 | A21 | I2C8_SCL_M2 |  | 3.3V | I2C8时钟 | I2C8_SCL_M2 |
| 58 | 1AE2 | HDMI_TX_SDA |  | 3.3V | HDMI串行数据 | HDMI_TX_SDA |
| 60 | B21 | I2C8_SDA_M2 |  | 3.3V | I2C8数据 | I2C8_SDA_M2 |
| 62 | —— | GND | —— | —— | 地 | GND |
| 64 | A19 | PCIE0_PERSTn |  | 3.3V | PCIE复位信号 | PCIE0_PERSTn |
| 66 | 1A20 | CAN1_TX_M3 |  | 3.3V | CAN1数据发送 | CAN1_TX_M3_3V3 |
| 68 | AL2 | HDMI_TX_SCL |  | 3.3V | HDMI串行时钟 | HDMI_TX_SCL |
| 70 | 1D16 | I2C7_SCL_M1 |  | 3.3V | I2C7时钟 | I2C7_SCL_M1 |
| 72 | 1B18 | I2C7_SDA_M1 |  | 3.3V | I2C7数据 | I2C7_SDA_M1 |
| 74 | 1Y22 | PCIE0_WAKEn_M0 |  | 3.3V | PCIE唤醒激活信号 | PCIE0_WAKEn_M0 |
| 76 | 1B16 | GPIO2_B3_d |  | 3.3V | 4G/5G模组复位信号 | 4G/5G_PWREN |
| 78 | 1A17 | PCIE0_CLKREQn_M0 |  | 3.3V | PCIE时钟请求信号 | PCIE0_CLKREQn_M0 |
| 80 | 1A18 | GPIO2_B1_d |  | 3.3V | 4G/5G模组电源控制信号 | 4G/5G_MOD_PWREN |
| 82 | B22 | TYPEC_DPTX_AUX_PUPDCTL1 |  | 3.3V | TYPEC_DPTX_AUX_PUPDCTL1信号 | TYPEC_DPTX_AUX_PUPDCTL1 |
| 84 | —— | GND | —— | —— | 地 | GND |
| 86 | —— | —— | —— | —— | —— | —— |
| 88 | —— | —— | —— | —— | —— | —— |
| 90 | —— | GND | —— | —— | 地 | GND |
| 92 | 2T4 | USB2_HOST1_DP | —— | —— | USB20_HOST1数据+ | USB20_HOST1_D_P |
| 94 | 2T5 | USB2_HOST1_DM | —— | —— | USB20_HOST1数据- | USB20_HOST1_D_N |
| 96 | —— | GND | —— | —— | 地 | GND |
| 98 | 2T9 | USB2_OTG1_ID | —— | —— | USB2_OTG1_ID信号 | x |
| 100 | 2T10 | USB2_OTG1_VBUSDET | —— | —— | USB2_OTG1_VBUSDET插入检测 | USB2_OTG1_VBUSDET |


**表3 P2连接器接口（奇）引脚定义**

| **NUM** | **BALL** | **信号名称** | **GPIO** | **VOL** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| 1 | AB29 | I2C2_SDA_M0 |  | 3.3V | I2C2数据 | I2C2_SDA_M0 |
| 3 | 1W21 | PWM0_CH1_M0 |  | 3.3V | PWM0_CH1_M0 | x |
| 5 | AD28 | PWM1_CH0_M0 |  | 3.3V | PWM1_CH0_M0 | x |
| 7 | 1U24 | UART0_TX_M0_DEBUG |  | 3.3V | UART0发送 | UART0_TX_M0_DEBUG |
| 9 | AA28 | UART0_RX_M0_DEBUG |  | 3.3V | UART0接收 | UART0_RX_M0_DEBUG |
| 11 | 1W24 | I2C2_SCL_M0 |  | 3.3V | I2C2时钟 | I2C2_SCL_M0 |
| 13 | 1W22 | PWM0_CH0_M0 |  | 3.3V | PWM0_CH0_M0 | PWM0_CH0_M0(MIPI屏幕背光PWM) |
| 15 | —— | GND | —— | —— | 地 | GND |
| 17 | —— | —— | —— | —— | —— | —— |
| 19 | 1E21 | GPIO3_D4_d | GPIO3_D4_d | 1.8V | GMAC1_INT中断 | GMAC1_INT |
| 21 | 1D10 | GPIO3_D5_d | GPIO3_D5_d | 1.8V | GMAC1_RESET复位 | GMAC1_RESET |
| 23 | —— | —— | —— | —— | —— | —— |
| 25 | —— | —— | —— | —— | —— | —— |
| 27 | —— | —— | —— | —— | —— | —— |
| 29 | 1AA23 | GPIO0_D3_d_1V8 |  | 1.8V | HP_DET_L耳机插入检测 | HP_DET_L(headphone) |
| 31 | 1D9 | I2C5_SCL_M3 |  | 1.8V | I2C5时钟 | I2C5_SCL_M3 |
| 33 | 1B10 | I2C5_SDA_M3 |  | 1.8V | I2C5数据 | I2C5_SDA_M3 |
| 35 | 1A4 | I2C3_SCL_M0 |  | 1.8V | I2C3时钟 | I2C3_SCL_M0 |
| 37 | 1B7 | CAM_CLK2_OUT_M0 |  | 1.8V | CAM_CLK2_OUT_M0 | x |
| 39 | 1A5 | UART5_TX_M1 |  | 1.8V | UART5发送数据 | UART5_TX_M1_1V8 |
| 41 | 1B12 | CAM_CLK1_OUT_M0 |  | 1.8V | CAM_CLK1_OUT_M0 | x |
| 43 | B8 | I2C3_SDA_M0 |  | 1.8V | I2C3数据 | I2C3_SDA_M0 |
| 45 | 1E7 | CAM_CLK0_OUT_M0 |  | 1.8V | CAM_CLK0_OUT_M0 | x |
| 47 | —— | —— | —— | —— | —— | —— |
| 49 | A7 | SAI1_SDO0_M0 |  | 1.8V | I2S 数据输出数据 | SAI1_SDO0_M0 |
| 51 | 1C10 | GPIO3_D6_d |  | 1.8V | 4G/5G 复位 | 4G/5G_RESET |
| 53 | 1B6 | SAI1_LRCK_M0 |  | 1.8V | I2S 发送帧时钟 | SAI1_LRCK_M0 |
| 55 | 1C6 | SAI1_SCLK_M0 |  | 1.8V | I2S 位时钟 | SAI1_SCLK_M0 |
| 57 | —— | —— | —— | —— | —— | —— |
| 59 | 1A6 | SAI1_SDI0_M0 |  | 1.8V | I2S 数据输入数据 | SAI1_SDI0_M0 |
| 61 | B7 | UART5_RX_M1 |  | 1.8V | UART5接收数据 | UART5_RX_M1_1V8 |
| 63 | —— | NC | —— | —— | 悬空 | 悬空 |
| 65 | 1D6 | SAI1_MCLK_M0 |  | 1.8V | I2S 主时钟 | SAI1_MCLK_M0 |
| 67 | V29 | GPIO0_A0_d |  | 1.8V | IIC中断 | IIC_GPIO_INT |
| 69 | 1B9 | UART8_RX_M0 |  | 1.8V | UART8接收数据 | UART8_RX_M0_1V8 |
| 71 | AK2 | HDMI_TX_HPDIN_M0_1V8 |  | 1.8V | HDMI发送链接检测 | HDMI_TX_HPDIN_M0_1V8 |
| 73 | 1D7 | UART8_TX_M0 |  | 1.8V | UART8发送数据 | UART8_TX_M0_1V8 |
| 75 | Y29 | GPIO0_A5_d |  | 1.8V | TYPEC0中断 | TYPEC0_INT |
| 77 | 1C7 | UART8_RTSN_M0 |  | 1.8V | UART8请求发送 | UART8_RTSN_M0_1V8 |
| 79 | 1C12 | UART8_CTSN_M0 |  | 1.8V | UART8清除发送 | UART8_CTSN_M0_1V8 |
| 81 | —— | GND | —— | —— | 地 | GND |
| 83 | 1L23 | PCIE1_REFCLKP | —— | —— | PCIE1时钟输出/输入+ | x |
| 85 | 1M23 | PCIE1_REFCLKN | —— | —— | PCIE1时钟输出/输入- | x |
| 87 | —— | GND | —— | —— | 地 | GND |
| 89 | N28 | PCIE1_TXP/USB3_HOST1_SSTXP | —— | —— | USB3_HOST1发送差分+ | USB3_HOST1_SSTXP |
| 91 | N29 | PCIE1_TXN/USB3_HOST1_SSTXN | —— | —— | USB3_HOST1发送差分- | USB3_HOST1_SSTXN |
| 93 | —— | GND | —— | —— | 地 | GND |
| 95 | M28 | PCIE1_RXP/USB3_HOST1_SSRXP | —— | —— | USB3_HOST1接收差分+ | USB3_HOST1_SSRXP |
| 97 | M29 | PCIE1_RXN/USB3_HOST1_SSRXN | —— | —— | USB3_HOST1接收差分- | USB3_HOST1_SSRXN |
| 99 | —— | GND | —— | —— | 地 | GND |


**表4 P2连接器接口（偶）引脚定义**

| **NUM** | **BALL** | **信号名称** | **GPIO** | **VOL** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| 2 | —— | GND | —— | —— | 地 | GND |
| 4 | —— | —— | —— | —— | —— | —— |
| 6 | —— | —— | —— | —— | —— | —— |
| 8 | —— | GND | —— | —— | 地 | GND |
| 10 | —— | —— | —— | —— | —— | —— |
| 12 | —— | —— | —— | —— | —— | —— |
| 14 | —— | GND | —— | —— | 地 | GND |
| 16 | —— | —— | —— | —— | —— | —— |
| 18 | —— | —— | —— | —— | —— | —— |
| 20 | —— | GND | —— | —— | 地 | GND |
| 22 | —— | —— | —— | —— | —— | —— |
| 24 | —— | —— | —— | —— | —— | —— |
| 26 | —— | GND | —— | —— | 地 | GND |
| 28 | —— | —— | —— | —— | —— | —— |
| 30 | —— | —— | —— | —— | —— | —— |
| 32 | —— | GND | —— | —— | 地 | GND |
| 34 | —— | —— | —— | —— | —— | —— |
| 36 | —— | —— | —— | —— | —— | —— |
| 38 | —— | GND | —— | —— | 地 | GND |
| 40 | —— | —— | —— | —— | —— | —— |
| 42 | —— | —— | —— | —— | —— | —— |
| 44 | —— | GND | —— | —— | 地 | GND |
| 46 | —— | —— | —— | —— | —— | —— |
| 48 | —— | —— | —— | —— | —— | —— |
| 50 | —— | GND | —— | —— | 地 | GND |
| 52 | —— | —— | —— | —— | —— | —— |
| 54 | —— | —— | —— | —— | —— | —— |
| 56 | —— | GND | —— | —— | 地 | GND |
| 58 | —— | —— | —— | —— | —— | —— |
| 60 | —— | —— | —— | —— | —— | —— |
| 62 | —— | GND | —— | —— | 地 | GND |
| 64 | 1N23 | PCIE0_REFCLKN | —— | —— | PCIE0时钟输出/输入- | PCIE0_REFCLKN |
| 66 | 1N22 | PCIE0_REFCLKP | —— | —— | PCIE0时钟输出/输入+ | PCIE0_REFCLKP |
| 68 | —— | GND | —— | —— | 地 | GND |
| 70 | R29 | PCIE0_RXN/SATA0_RXN | —— | —— | PCIE0数据接收- | PCIE0_RXN |
| 72 | R28 | PCIE0_RXP/SATA0_RXP | —— | —— | PCIE0数据接收+ | PCIE0_RXP |
| 74 | —— | GND | —— | —— | 地 | GND |
| 76 | P28 | PCIE0_TXN/SATA0_TXN | —— | —— | PCIE0数据发送- | PCIE0_TXN |
| 78 | P29 | PCIE0_TXP/SATA0_TXP | —— | —— | PCIE0数据发送+ | PCIE0_TXP |
| 80 | —— | GND | —— | —— | 地 | GND |
| 82 | —— | —— | —— | —— | —— | —— |
| 84 | —— | —— | —— | —— | —— | —— |
| 86 | —— | GND | —— | —— | 地 | GND |
| 88 | —— | —— | —— | —— | —— | —— |
| 90 | —— | —— | —— | —— | —— | —— |
| 92 | —— | GND | —— | —— | 地 | GND |
| 94 | —— | —— | —— | —— | —— | —— |
| 96 | —— | —— | —— | —— | —— | —— |
| 98 | —— | GND | —— | —— | 地 | GND |
| 100 | —— | RESET_L | —— | —— | 复位 | RESET_L |


**表5 P3连接器接口（奇）引脚定义**

| **NUM** | **BALL** | **信号名称** | **GPIO** | **VOL** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| 1 | —— | GND | —— | —— | 地 | GND |
| 3 | AL10 | USB3_OTG0_SSRX1N/DP_TX_D0N | —— | —— | USB3_OTG0_SSRX1N接收差分信号1- | USB3_OTG0_SSRX1N |
| 5 | AK10 | USB3_OTG0_SSRX1P/DP_TX_D0P | —— | —— | USB3_OTG0_SSRX1P接收差分信号1+ | USB3_OTG0_SSRX1P |
| 7 | —— | GND | —— | —— | 地 | GND |
| 9 | AL11 | USB3_OTG0_SSTX1P/DP_TX_D1P | —— | —— | USB3_OTG0_SSTX1P发送差分信号1+ | USB3_OTG0_SSTX1P |
| 11 | AK11 | USB3_OTG0_SSTX1N/DP_TX_D1N | —— | —— | USB3_OTG0_SSTX1N发送差分信号1- | USB3_OTG0_SSTX1N |
| 13 | —— | GND | —— | —— | 地 | GND |
| 15 | AL12 | USB3_OTG0_SSRX2N/DP_TX_D2N | —— | —— | USB3_OTG0_SSRX2N接收差分信号2- | USB3_OTG0_SSRX2N |
| 17 | AK12 | USB3_OTG0_SSRX2P/DP_TX_D2P | —— | —— | USB3_OTG0_SSRX2P接收差分信号2+ | USB3_OTG0_SSRX2P |
| 19 | —— | GND | —— | —— | 地 | GND |
| 21 | AL13 | USB3_OTG0_SSTX2P/DP_TX_D3P | —— | —— | USB3_OTG0_SSTX2P发送差分信号2+ | USB3_OTG0_SSTX2P |
| 23 | AK13 | USB3_OTG0_SSTX2N/DP_TX_D3N | —— | —— | USB3_OTG0_SSTX2N发送差分信号2- | USB3_OTG0_SSTX2N |
| 25 | —— | GND | —— | —— | 地 | GND |
| 27 | B27 | SDMMC1_D1_M0 |  | 1.8V | SD/MMC接口数据信号1 | SDMMC1_D1_M0 |
| 29 | A28 | SDMMC1_D0_M0 |  | 1.8V | SD/MMC接口数据信号0 | SDMMC1_D0_M0 |
| 31 | —— | GND | —— | —— | 地 | GND |
| 33 | 1B22 | SDMMC1_CLK_M0 |  | 1.8V | SD/MMC接口时钟信号 | SDMMC1_CLK_M0 |
| 35 | B26 | SDMMC1_CMD_M0 |  | 1.8V | SD/MMC接口命令信号 | SDMMC1_CMD_M0 |
| 37 | —— | GND | —— | —— | 地 | GND |
| 39 | A27 | SDMMC1_D3_M0 |  | 1.8V | SD/MMC接口数据信号3 | SDMMC1_D3_M0 |
| 41 | 1A23 | SDMMC1_D2_M0 |  | 1.8V | SD/MMC接口数据信号2 | SDMMC1_D2_M0 |
| 43 | —— | GND | —— | —— | 地 | GND |
| 45 | C29 | SAI2_SDO_M0 |  | 1.8V | I2S数据输出数据 | SAI2_SDO_M0 |
| 47 | 1D22 | SAI2_SCLK_M0 |  | 1.8V | I2S位时钟 | SAI2_SCLK_M0 |
| 49 | —— | GND | —— | —— | 地 | GND |
| 51 | 1A24 | SAI2_LRCK_M0 |  | 1.8V | I2S发送帧时钟 | SAI2_LRCK_M0 |
| 53 | C28 | SAI2_SDI_M0 |  | 1.8V | I2S数据输入数据 | SAI2_SDI_M0 |
| 55 | —— | GND | —— | —— | 地 | GND |
| 57 | AK15 | MIPI_DPHY_DSI_TX_D0N | —— | —— | MIPI_DPHY_DSI发送数据0- | MIPI_DPHY_DSI_TX_D0N |
| 59 | AL15 | MIPI_DPHY_DSI_TX_D0P | —— | —— | MIPI_DPHY_DSI发送数据0+ | MIPI_DPHY_DSI_TX_D0P |
| 61 | —— | GND | —— | —— | 地 | GND |
| 63 | AK16 | MIPI_DPHY_DSI_TX_D1N | —— | —— | MIPI_DPHY_DSI发送数据1- | MIPI_DPHY_DSI_TX_D1N |
| 65 | AL16 | MIPI_DPHY_DSI_TX_D1P | —— | —— | MIPI_DPHY_DSI发送数据1+ | MIPI_DPHY_DSI_TX_D1P |
| 67 | —— | GND | —— | —— | 地 | GND |
| 69 | AL17 | MIPI_DPHY_DSI_TX_CLKN | —— | —— | MIPI_DPHY_DSI发送时钟- | MIPI_DPHY_DSI_TX_CLKN |
| 71 | AL17 | MIPI_DPHY_DSI_TX_CLKP | —— | —— | MIPI_DPHY_DSI发送时钟+ | MIPI_DPHY_DSI_TX_CLKP |
| 73 | —— | GND | —— | —— | 地 | GND |
| 75 | AK18 | MIPI_DPHY_DSI_TX_D2N | —— | —— | MIPI_DPHY_DSI发送数据2- | MIPI_DPHY_DSI_TX_D2N |
| 77 | AL18 | MIPI_DPHY_DSI_TX_D2P | —— | —— | MIPI_DPHY_DSI发送数据2+ | MIPI_DPHY_DSI_TX_D2P |
| 79 | —— | GND | —— | —— | 地 | GND |
| 81 | AK19 | MIPI_DPHY_DSI_TX_D3N | —— | —— | MIPI_DPHY_DSI发送数据3- | MIPI_DPHY_DSI_TX_D3N |
| 83 | AL19 | MIPI_DPHY_DSI_TX_D3P | —— | —— | MIPI_DPHY_DSI发送数据3+ | MIPI_DPHY_DSI_TX_D3P |
| 85 | —— | GND | —— | —— | 地 | GND |
| 87 |  | CARRIER_BOARD_EN | —— | —— | CARRIER使能 | CARRIER_BOARD_EN |
| 89 | —— | GND | —— | —— | 地 | GND |
| 91 |  | VCC12V_DCIN | —— | —— | 12V电源输入 | VCC12V_DCIN |
| 93 |  | VCC12V_DCIN | —— | —— | 12V电源输入 | VCC12V_DCIN |
| 95 |  | VCC12V_DCIN | —— | —— | 12V电源输入 | VCC12V_DCIN |
| 97 |  | VCC12V_DCIN | —— | —— | 12V电源输入 | VCC12V_DCIN |
| 99 |  | VCC12V_DCIN | —— | —— | 12V电源输入 | VCC12V_DCIN |


**表6 P3连接器接口（偶）引脚定义**

| **NUM** | **BALL** | **信号名称** | **GPIO** | **VOL** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| 2 | —— | GND | —— | —— | 地 | GND |
| 4 | —— | —— | —— | —— | —— | —— |
| 6 | —— | —— | —— | —— | —— | —— |
| 8 | —— | —— | —— | —— | —— | —— |
| 10 | —— | PMIC_VDC | —— | —— | PMIC_VDC信号 | 核心板启动模式切换 |
| 12 | —— | GND | —— | —— | 地 | GND |
| 14 | 2R6 | USB2_OTG0_ID | —— | —— | USB2_OTG0_ID信号 | X |
| 16 | 2P3 | USB2_OTG0_VBUSDET | —— | —— | USB2_OTG0_VBUSDET插入检测 | USB2_OTG0_VBUSDET |
| 18 | AL9 | USB2_OTG0_DM | —— | —— | USB2_OTG0_DM数据- | USB2_OTG0_DM |
| 20 | AK9 | USB2_OTG0_DP | —— | —— | USB2_OTG0_DP数据+ | USB2_OTG0_DP |
| 22 | 2T2 | DP_TX_AUXP | —— | —— | DP_TX_AUXP信号 | DP_TX_AUXP |
| 24 | 2T3 | DP_TX_AUXN | —— | —— | DP_TX_AUXN信号 | DP_TX_AUXN |
| 26 | —— | GND | —— | —— | 地 | GND |
| 28 | 1B23 | UART4_TX_M1 | —— | 1.8V | UART4发送数据 | UART4_TX_M1 |
| 30 | B28 | UART4_RX_M1 | —— | 1.8V | UART4接收数据 | UART4_RX_M1 |
| 32 | —— | GND | —— | —— | 地 | GND |
| 34 | B29 | UART4_RTSN_M1 | —— | 1.8V | UART4请求发送 | UART4_RTSN_M1 |
| 36 | 1C23 | UART4_CTSN_M1 | —— | 1.8V | UART4清除发送 | UART4_CTSN_M1 |
| 38 | —— | GND | —— | —— | 地 | GND |
| 40 | A26 | WIFI_REG_ON_H | —— | 1.8V | WIFI_REG_ON_H信号 | WIFI_REG_ON_H |
| 42 | 1C22 | BT_REG_ON_H | —— | 1.8V | BT_REG_ON_H信号 | BT_REG_ON_H |
| 44 | —— | GND | —— | —— | 地 | GND |
| 46 | 1E21 | HOST_WAKE_BT_H | —— | 1.8V | HOST_WAKE_BT_H信号 | HOST_WAKE_BT_H |
| 48 | 1E22 | GPIO1_D5_d | —— | 1.8V | GPIO_D5_d_1V8信号 | GPIO_D5_d_1V8 |
| 50 | —— | GND | —— | —— | 地 | GND |
| 52 | 1U22 | WIFI_WAKE_HOST_H | —— | 1.8V | WIFI_WAKE_HOST_H信号 | WIFI_WAKE_HOST_H |
| 54 | 1P23 | BT_WAKE_HOST_H | —— | 1.8V | BT_WAKE_HOST_H信号 | BT_WAKE_HOST_H |
| 56 | —— | GND | —— | —— | 地 | GND |
| 58 | AK20 | MIPI_DPHY_CSI0_RX_D0P/MIPI_CPHY_CSI_RX_TRIO0_B | —— | —— | MIPI_DPHY_CSI0_RX_D0P接收数据0+ | MIPI_DPHY_CSI0_RX_D0P |
| 60 | AL20 | MIPI_DPHY_CSI0_RX_D0N/MIPI_CPHY_CSI_RX_TRIO0_A | —— | —— | MIPI_DPHY_CSI0_RX_D0N接收数据0- | MIPI_DPHY_CSI0_RX_D0N |
| 62 | —— | GND | —— | —— | 地 | GND |
| 64 | AK21 | MIPI_DPHY_CSI0_RX_D1P/MIPI_CPHY_CSI_RX_TRIO1_A | —— | —— | MIPI_DPHY_CSI0_RX_D1P接收数据1+ | MIPI_DPHY_CSI0_RX_D1P |
| 66 | AL21 | MIPI_DPHY_CSI0_RX_D1N/MIPI_CPHY_CSI_RX_TRIO0_C | —— | —— | MIPI_DPHY_CSI0_RX_D1N接收数据1- | MIPI_DPHY_CSI0_RX_D1N |
| 68 | —— | GND | —— | —— | 地 | GND |
| 70 | AK22 | MIPI_DPHY_CSI0_RX_CLKP/MIPI_CPHY_CSI_RX_TRIO1_C | —— | —— | MIPI_DPHY_CSI0_RX_CLKP接收时钟+ | MIPI_DPHY_CSI0_RX_CLKP |
| 72 | AL22 | MIPI_DPHY_CSI0_RX_CLKN/MIPI_CPHY_CSI_RX_TRIO1_B | —— | —— | MIPI_DPHY_CSI0_RX_CLKN接收时钟- | MIPI_DPHY_CSI0_RX_CLKN |
| 74 | —— | GND | —— | —— | 地 | GND |
| 76 | AK23 | MIPI_DPHY_CSI0_RX_D2P/MIPI_CPHY_CSI_RX_TRIO2_B | —— | —— | MIPI_DPHY_CSI0_RX_D2P接收数据2+ | MIPI_DPHY_CSI0_RX_D2P |
| 78 | AL23 | MIPI_DPHY_CSI0_RX_D2N/MIPI_CPHY_CSI_RX_TRIO2_A | —— | —— | MIPI_DPHY_CSI0_RX_D2N接收数据2- | MIPI_DPHY_CSI0_RX_D2N |
| 80 | —— | GND | —— | —— | 地 | GND |
| 82 | AK24 | MIPI_DPHY_CSI0_RX_D3P/NO_USE | —— | —— | MIPI_DPHY_CSI0_RX_D3P接收数据3+ | MIPI_DPHY_CSI0_RX_D3P |
| 84 | AL24 | MIPI_DPHY_CSI0_RX_D3N/MIPI_CPHY_CSI_RX_TRIO2_C | —— | —— | MIPI_DPHY_CSI0_RX_D3N接收数据3- | MIPI_DPHY_CSI0_RX_D3N |
| 86 | —— | GND | —— | —— | 地 | GND |
| 88 | —— | PWRON_L | —— | —— | 上电控制 | PWRON_L |
| 90 | 1U21 | SDMMC0_DET_L |  | 1.8V | SDMMC卡检测信号 | SDMMC_DET_L |
| 92 | B6 | GPIO4_B2_d | GPIO4_B2_d | 1.8V | GMAC0复位 | GMAC0_RESET |
| 94 | 1U23 | GPIO0_A2_d | GPIO0_A2_d | 1.8V | GMAC0中断 | GMAC0_INT |
| 96 | —— | GND | —— | —— | 地 | GND |
| 98 | —— | VCC12V_DCIN | —— | —— | 12V电源输入 | VCC12V_DCIN |
| 100 | —— | VCC12V_DCIN | —— | —— | 12V电源输入 | VCC12V_DCIN |


**表7 P4连接器接口（奇）引脚定义**

| **NUM** | **BALL** | **信号名称** | **GPIO** | **VOL** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | --- | :---: | --- | :---: |
| 1 | 1AA22 | GPIO0_C5_d | GPIO0_C5_d | 3.3V | MIPI_DSI1中断 | MIPI_DSI1_INT |
| 3 | 1Y23 | GPIO0_C7_d | GPIO0_C7_d | 3.3V | PCIE0_PRSN2_3V3热插拔检测 | PCIE0_PRSN2_3V3 |
| 5 | 1B15 | GMAC1_MDIO_M0 |  | 3.3V | GMAC1串行管理数据 | GMAC1_MDIO_M0 |
| 7 | 1B13 | GMAC1_MDC_M0 |  | 3.3V | GMAC1串行管理时钟 | GMAC1_MDC_M0 |
| 9 | 1W23 | GPIO0_D0_d | GPIO0_D0_d | 3.3V | MIPI_DSI1复位 | MIPI_DSI1_RESET |
| 11 | AB28 | I2C0_SCL_M1 |  | 3.3V | I2C0时钟 | I2C0_SCL_M1 |
| 13 | —— | GND | —— | —— | 地 | GND |
| 15 | 1V24 | I2C0_SDA_M1 |  | 3.3V | I2C0数据 | I2C0_SDA_M1 |
| 17 | 1AE1 | GPIO4_C6_d | GPIO4_C6_d | 3.3V | GPIO4_C6_d | GPIO4_C6_d |
| 19 | AJ1 | GPIO4_C7_d | GPIO4_C7_d | 3.3V | MIPI_DSI2复位信号 | PCIE_PWR_EN_3V3 |
| 21 | AL3 | UART6_TX_M3 |  | 3.3V | UART6发送数据 | UART6_TX_M3_3V3 |
| 23 | ALK1 | UART6_RX_M3 |  | 3.3V | UART6接收数据 | UART6_RX_M3_3V3 |
| 25 |  | WIFI_PEN_3V3 |  | 3.3V | WIFI_PEN_3V3使能信号   <font style="background-color:#ffff00;">(3.3V上拉，未连接GPIO)</font> | WIFI_PEN_3V3 |
| 27 | —— | GND | —— | —— | 地 | GND |
| 29 | 1C5 | CAN0_TX_M2_3V3 |  | 3.3V | CAN0数据发送 | CAN0_TX_M2_3V3 |
| 31 | 1B5 | CAN0_RX_M2_3V3 |  | 3.3V | CAN0数据接收 | CAN0_RX_M2_3V3 |
| 33 | 1Y24 | GPIO0_B6_d | GPIO0_B6_d | 3.3V | TF_PWR_EN_3V3使能信号 | TF_PWR_EN_3V3 |
| 35 | 1D18 | ETH_CLK1_25M_OUT_M0 |  | 3.3V | PHY 25MHz 参考时钟输出 | ETH_CLK1_25M_OUT_M0 |
| 37 | 1E15 | ETH1_MCLK_M0 |  | 3.3V | PHY 125MHz 同步时钟输入 | ETH1_MCLK_M0 |
| 39 | 1Y21 | GPIO0_C6_d | GPIO0_C6_d | 3.3V | MIPI_DSI1使能信号 | MIPI_DSI1_EN |
| 41 | —— | GND | —— | —— | 地 | GND |
| 43 | 1D12 | I2C4_SDA_M3 |  | 1.8V | I2C4数据 | I2C4_SDA_M3 |
| 45 | 1E9 | I2C4_SCL_M3 |  | 1.8V | I2C4时钟 | I2C4_SCL_M3 |
| 47 | A9 | GMAC0_MDIO_M0 |  | 1.8V | GMAC0串行管理数据 | GMAC0_MDIO_M0 |
| 49 | 1A7 | GMAC0_MDC_M0 |  | 1.8V | GMAC0 串行管理时钟 | GMAC0_MDC_M0 |
| 51 | —— | GND | —— | —— | 地 | GND |
| 53 | —— | —— | —— | —— | —— | —— |
| 55 | —— | —— | —— | —— | <font style="color:rgb(255, 0, 0);">——</font> | —— |
| 57 | 1D13 | ETH_CLK0_25M_OUT_M0 |  | 1.8V | PHY 25MHz 参考时钟输出 | ETH_CLK0_25M_OUT_M0 |
| 59 | —— | —— | —— | —— | <font style="color:rgb(255, 0, 0);">——</font> | —— |
| 61 | B14 | ETH0_MCLK_M0 |  | 1.8V | PHY 125MHz 同步时钟输入 | ETH0_MCLK_M0 |
| 63 | —— | GND | —— | —— | 地 | GND |
| 65 | AE28 | MIPI_DPHY_CSI1_RX_D0N | —— | —— | MIPI_DPHY_CSI1_RX_D0N数据接收0- | MIPI_DPHY_CSI1_RX_D0N |
| 67 | AE29 | MIPI_DPHY_CSI1_RX_D0P | —— | —— | MIPI_DPHY_CSI1_RX_D0P数据接收0+ | MIPI_DPHY_CSI1_RX_D0P |
| 69 | —— | GND | —— | —— | 地 | GND |
| 71 | AF28 | MIPI_DPHY_CSI1_RX_D1N | —— | —— | MIPI_DPHY_CSI1_RX_D1N数据接收1- | MIPI_DPHY_CSI1_RX_D1N |
| 73 | AF29 | MIPI_DPHY_CSI1_RX_D1P | —— | —— | MIPI_DPHY_CSI1_RX_D1P数据接收1+ | MIPI_DPHY_CSI1_RX_D1P |
| 75 | —— | GND | —— | —— | 地 | GND |
| 77 | 1AC23 | MIPI_DPHY_CSI1_RX_CLKN | —— | —— | MIPI_DPHY_CSI1_RX_CLKN时钟- | MIPI_DPHY_CSI1_RX_CLKN |
| 79 | 1AC22 | MIPI_DPHY_CSI1_RX_CLKP | —— | —— | MIPI_DPHY_CSI1_RX_CLKP时钟+ | MIPI_DPHY_CSI1_RX_CLKP |
| 81 | —— | GND | —— | —— | 地 | GND |
| 83 | AG28 | MIPI_DPHY_CSI1_RX_D2N/   MIPI_DPHY_CSI2_RX_D0N | —— | —— | MIPI_DPHY_CSI2_RX_D0N数据接收0- | MIPI_DPHY_CSI2_RX_D0N |
| 85 | AG29 | MIPI_DPHY_CSI1_RX_D2P/   MIPI_DPHY_CSI2_RX_D0P | —— | —— | MIPI_DPHY_CSI2_RX_D0P数据接收0+ | MIPI_DPHY_CSI2_RX_D0P |
| 87 | —— | GND | —— | —— | 地 | GND |
| 89 | AH28 | MIPI_DPHY_CSI1_RX_D3N/   MIPI_DPHY_CSI2_RX_D1N | —— | —— | MIPI_DPHY_CSI2_RX_D1N数据接收1- | MIPI_DPHY_CSI2_RX_D1N |
| 91 | AH29 | MIPI_DPHY_CSI1_RX_D3P/   MIPI_DPHY_CSI2_RX_D1P | —— | —— | MIPI_DPHY_CSI2_RX_D1P数据接收1+ | MIPI_DPHY_CSI2_RX_D1P |
| 93 | —— | GND | —— | —— | 地 | GND |
| 95 | 1AD22 | MIPI_DPHY_CSI2_RX_CLKN | —— | —— | MIPI_DPHY_CSI2_RX_CLKN时钟- | MIPI_DPHY_CSI2_RX_CLKN |
| 97 | 1AD21 | MIPI_DPHY_CSI2_RX_CLKN | —— | —— | MIPI_DPHY_CSI2_RX_CLKN时钟+ | MIPI_DPHY_CSI2_RX_CLKN |
| 99 | —— | GND | —— | —— | 地 | GND |


**表8 P4连接器接口（偶）引脚定义**

| **NUM** | **BALL** | **信号名称** | **GPIO** | **VOL** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| 2 | AD29 | PWM1_CH1_M0 |  | 3.3V | PWM1 | x |
| 4 | AC28 | GPIO0_D1_d |  | 3.3V | TYPEC使能 | TYPEC0_PWREN |
| 6 | —— | —— | —— | —— | —— | —— |
| 8 | —— | GND | —— | —— | 地 | GND |
| 10 | B9 | GMAC0_TXD3_M0 |  | 1.8V | GMAC0 数据发送 3 | GMAC0_TXD3_M0 |
| 12 | 1A8 | GMAC0_TXD2_M0 |  | 1.8V | GMAC0 数据发送 2 | GMAC0_TXD2_M0 |
| 14 | B10 | GMAC0_TXD1_M0 |  | 1.8V | GMAC0 数据发送 1 | GMAC0_TXD1_M0 |
| 16 | 1A9 | GMAC0_TXD0_M0 |  | 1.8V | GMAC0 数据发送 0 | GMAC0_TXD0_M0 |
| 18 | A11 | GMAC0_TXCTL_M0 |  | 1.8V | GMAC0 发送控制 | GMAC0_TXCTL_M0 |
| 20 | B11 | GMAC0_TXCLK_M0 |  | 1.8V | GMAC0 发送时钟 | GMAC0_TXCLK_M0 |
| 22 | —— | GND | —— | —— | 地 | GND |
| 24 | 1A10 | GMAC0_RXD3_M0 |  | 1.8V | GMAC0接收数据 3 | GMAC0_RXD3_M0 |
| 26 | B12 | GMAC0_RXD2_M0 |  | 1.8V | GMAC0 接收数据 2 | GMAC0_RXD2_M0 |
| 28 | 1A11 | GMAC0_RXD1_M0 |  | 1.8V | GMAC0接收数据 1 | GMAC0_RXD1_M0 |
| 30 | A13 | GMAC0_RXD0_M0 |  | 1.8V | GMAC0 接收数据 0 | GMAC0_RXD0_M0 |
| 32 | B13 | GMAC0_RXCTL_M0 |  | 1.8V | GMAC0 接收控制 | GMAC0_RXCTL_M0 |
| 34 | 1A12 | GMAC0_RXCLK_M0 |  | 1.8V | GMAC0 接收时钟 | GMAC0_RXCLK_M0 |
| 36 | —— | GND | —— | —— | 地 | GND |
| 38 | 1A13 | GMAC1_TXD3_M0 |  | 3.3V | GMAC1数据发送 3 | GMAC1_TXD3_M0 |
| 40 | A15 | GMAC1_TXD2_M0 |  | 3.3V | GMAC1 数据发送 2 | GMAC1_TXD2_M0 |
| 42 | B15 | GMAC1_TXD1_M0 |  | 3.3V | GMAC1 数据发送 1 | GMAC1_TXD1_M0 |
| 44 | 1A14 | GMAC1_TXD0_M0 |  | 3.3V | GMAC1 数据发送 0 | GMAC1_TXD0_M0 |
| 46 | B16 | GMAC1_TXCTL_M0 |  | 3.3V | GMAC1 发送控制 | GMAC1_TXCTL_M0 |
| 48 | 1C15 | GMAC1_TXCLK_M0 |  | 3.3V | GMAC1 发送时钟 | GMAC1_TXCLK_M0 |
| 50 | —— | GND | —— | —— | 地 | GND |
| 52 | 1A15 | GMAC1_RXD3_M0 |  | 3.3V | GMAC1接收数据 3 | GMAC1_RXD3_M0 |
| 54 | A17 | GMAC1_RXD2_M0 |  | 3.3V | GMAC1 接收数据 2 | GMAC1_RXD2_M0 |
| 56 | B17 | GMAC1_RXD1_M0 |  | 3.3V | GMAC1接收数据 1 | GMAC1_RXD1_M0 |
| 58 | 1A16 | GMAC1_RXD0_M0 |  | 3.3V | GMAC1接收数据 0 | GMAC1_RXD0_M0 |
| 60 | B18 | GMAC1_RXCTL_M0 |  | 3.3V | GMAC1接收控制 | GMAC1_RXCTL_M0 |
| 62 | 1D15 | GMAC1_RXCLK_M0 |  | 3.3V | GMAC1 接收时钟 | GMAC1_RXCLK_M0 |
| 64 | —— | GND | —— | —— | 地 | GND |
| 66 | H28 | MIPI_DPHY_CSI3_RX_D0P | —— | —— | MIPI_DPHY_CSI3_RX_D0P数据接收0+ | MIPI_DPHY_CSI3_RX_D0P |
| 68 | H29 | MIPI_DPHY_CSI3_RX_D0N | —— | —— | MIPI_DPHY_CSI3_RX_D0N数据接收0- | MIPI_DPHY_CSI3_RX_D0N |
| 70 | —— | GND | —— | —— | 地 | GND |
| 72 | J28 | MIPI_DPHY_CSI3_RX_D1P | —— | —— | MIPI_DPHY_CSI3_RX_D1P数据接收1+ | MIPI_DPHY_CSI3_RX_D1P |
| 74 | J29 | MIPI_DPHY_CSI3_RX_D1N | —— | —— | MIPI_DPHY_CSI3_RX_D1N数据接收1- | MIPI_DPHY_CSI3_RX_D1N |
| 76 | —— | GND | —— | —— | 地 | GND |
| 78 | 1H22 | MIPI_DPHY_CSI3_RX_CLKP | —— | —— | MIPI_DPHY_CSI3_RX_CLKP时钟+ | MIPI_DPHY_CSI3_RX_CLKP |
| 80 | 1H23 | MIPI_DPHY_CSI3_RX_CLKN | —— | —— | MIPI_DPHY_CSI3_RX_CLKN时钟- | MIPI_DPHY_CSI3_RX_CLKN |
| 82 | —— | GND | —— | —— | 地 | GND |
| 84 | K28 | MIPI_DPHY_CSI3_RX_D2P/   MIPI_DPHY_CSI4_RX_D0P | —— | —— | MIPI_DPHY_CSI4_RX_D0P数据接收0+ | MIPI_DPHY_CSI4_RX_D0P |
| 86 | K29 | MIPI_DPHY_CSI3_RX_D2N/   MIPI_DPHY_CSI4_RX_D0N | —— | —— | MIPI_DPHY_CSI4_RX_D0N数据接收0- | MIPI_DPHY_CSI4_RX_D0N |
| 88 | —— | GND | —— | —— | 地 | GND |
| 90 | L28 | MIPI_DPHY_CSI3_RX_D3P/   MIPI_DPHY_CSI4_RX_D1P | —— | —— | MIPI_DPHY_CSI4_RX_D1P数据接收1+ | MIPI_DPHY_CSI4_RX_D1P |
| 92 | L29 | MIPI_DPHY_CSI3_RX_D3N/   MIPI_DPHY_CSI4_RX_D1N | —— | —— | MIPI_DPHY_CSI4_RX_D1N数据接收1- | MIPI_DPHY_CSI4_RX_D1N |
| 94 | —— | GND | —— | —— | 地 | GND |
| 96 | 1K22 | MIPI_DPHY_CSI4_RX_CLKP | —— | —— | MIPI_DPHY_CSI4_RX_CLKP时钟+ | MIPI_DPHY_CSI4_RX_CLKP |
| 98 | 1K23 | MIPI_DPHY_CSI4_RX_CLKN | —— | —— | MIPI_DPHY_CSI4_RX_CLKN时钟- | MIPI_DPHY_CSI4_RX_CLKN |
| 100 | —— | GND | —— | —— | 地 | GND |


## 2.7  FET3576-C核心板引脚说明（按功能划分）
**注1： 核心板所有引脚功能均按下表的“默认功能”作了规定，请勿修改，否则可能和出厂驱动冲突。如有疑问，请及时联系我们的销售或技术支持。**

**注2：用户在有多种功能扩展需求时可参阅参考中《FET3576-C核心板管脚复用对照表》,但若需了解更详细的信息，建议用户查阅相关资料文档及芯片数据手册及参考手册。**

**注3：“信号名称”一栏默认为核心板对应到底板上的引脚名称。**

### 2.7.1  电源引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| 电源 | VCC12V_DCIN | 电源输入 | 核心板电源供电引脚，12V | P3_91 |
|  |  |  |  | P3_93 |
|  |  |  |  | P3_95 |
|  |  |  |  | P3_97 |
|  |  |  |  | P3_99 |
|  |  |  |  | P3_98 |
|  |  |  |  | P3_100 |
|  | Carry_Board_PEN | 电源使能 | 用于底板外设供电使能 | P3_87 |
|  | GND | 地 | 核心板电源地，所有GND引脚都需要连接 | —— |


### 2.7.2  复位控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| 核心板复位 | RESET_L | I | 核心板断电复位，低电平有效 | P2_100 |


### 2.7.3  核心板启动控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| 核心板启动模式切换 | PMIC_VDC | I | 引脚悬空时，核心板默认上电启动；引脚拉低时，核心板上电不启动，按下PWRON_L按键后启动 | P3_10 |


### 2.7.4  烧录控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | --- | :---: |
| Maskrom模式 | SARADC_VIN0_BOOT | I | 开机前拉低，进入Maskrom模式 | P1_28 |
| Recovery模式 | SARADC_VIN1_KEY/RECOVERY | I | 开机前拉低，进入Recovery模式 | P1_30 |


### 2.7.5  功能按键引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| --- | :---: | :---: | :---: | :---: |
| Maskrom按键 | SARADC_VIN0_BOOT | I | 开机前拉低，进入Maskrom模式 | P1_28 |
| 开关机 | PWRON_L | I | 核心板供电开关，低电平关机 | P3_88 |
| V+/RECOVERY按键 | SARADC_VIN1_KEY/RECOVERY | I | 音量加/Recovery按键 | P1_30 |
| V-按键 |  | I | 音量减按键 | P1_30 |
| MENU按键 |  | I | 菜单按键 | P1_30 |
| ESC按键 |  | I | 退出按键 | P1_30 |


### 2.7.6  USB数据/控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| USB | TYPEC_DPTX_AUX_PUPDCTL2 | O | DP_AUX上下拉 | P1_48 |
|  | USB_HUB_RST_3V3 | O | USB_HUB复位 | P1_50 |
|  | TYPEC_DPTX_AUX_PUPDCTL1 | O | DP_AUX上下拉 | P1_82 |
|  | USB2_HOST1_D_P | I/O | USB2.0_HOST数据+ | P1_92 |
|  | USB2_HOST1_D_N | I/O | USB2.0_HOST数据- | P1_94 |
|  | USB2_OTG1_ID | I | USB2_OTG1_ID脚 | P1_98 |
|  | USB2_OTG1_VBUSDET | I | USB2_OTG1_VBUSDET脚 | P1_100 |
|  | TYPEC0_INT | I | Type-C接口CC芯片中断 | P2_75 |
|  | USB3_HOST1_SSTX_P | O | USB3.0_HOST1发送+ | P2_89 |
|  | USB3_HOST1_SSTX_N | O | USB3.0_HOST1发送- | P2_91 |
|  | USB3_HOST1_SSRX_P | I | USB3.0_HOST1接受+ | P2_95 |
|  | USB3_HOST1_SSRX_N | I | USB3.0_HOST1接受- | P2_97 |
|  | USB3_OTG0_SSRX1_N | I | USB3.0_OTG0接受1- | P3_3 |
|  | USB3_OTG0_SSRX1_P | I | USB3.0_OTG0接受1+ | P3_5 |
|  | USB3_OTG0_SSTX1_P | O | USB3.0_OTG0发送1+ | P3_9 |
|  | USB3_OTG0_SSTX1_N | O | USB3.0_OTG0发送1- | P3_11 |
|  | USB3_OTG0_SSRX2_N | I | USB3.0_OTG接收2- | P3_15 |
|  | USB3_OTG0_SSRX2_P | I | USB3.0_OTG接收2+ | P3_17 |
|  | USB3_OTG0_SSTX2_P | O | USB3.0_OTG0发送2+ | P3_21 |
|  | USB3_OTG0_SSTX2_N | O | USB3.0_OTG0发送2- | P3_23 |
|  | USB2_OTG0_ID | I | USB2_OTG0_ID脚 | P3_14 |
|  | USB2_OTG0_VBUSDET | I | USB2_OTG0_VBUSDET脚 | P3_16 |
|  | USB2_OTG0_D_N | I/O | USB2.0_OTG数据- | P3_18 |
|  | USB2_OTG0_D_P | I/O | USB2.0_OTG数据+ | P3_20 |
|  | DP_TX_AUX_P | I/O | DP_TX_AUX数据+ | P3_22 |
|  | DP_TX_AUX_N | I/O | DP_TX_AUX数据- | P3_24 |
|  | TYPEC0_PWREN | O | Type-C接口电源使能 | P4_4 |


### 2.7.7  SD接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| SDIO | SDMMC0_D0 | I/O | SDIO数据位0 | P1_5 |
|  | SDMMC0_D1 | I/O | SDIO数据位1 | P1_3 |
|  | SDMMC0_D2 | I/O | SDIO数据位2 | P1_13 |
|  | SDMMC0_D3 | I/O | SDIO数据位3 | P1_11 |
|  | SDMMC0_CLK | O | SDIO时钟 | P1_7 |
|  | SDMMC0_CMD | I/O | SDIO命令信号 | P1_9 |
|  | SDMMC0_DET_L | I | SD卡插拔检测 | P3_90 |
|  | TF_PWR_EN_3V3 | O | SD卡供电使能 | P4_33 |


### 2.7.8  WIFI接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| 控制脚 | WIFI_REG_ON_H | O | WIFI电源使能 | P3_40 |
|  | WIFI_WAKE_HOST_H | I/O | 无线网唤醒主机 | P3_52 |
|  | BT_WAKE_HOST_H | I/O | 蓝牙唤醒主机 | P3_54 |
|  | HOST_WAKE_BT_H | I/O | 主机唤醒蓝牙 | P3_46 |
|  | BT_REG_ON_H | O | 蓝牙电源使能 | P3_42 |
|  | WIFI_PEN_3V3 | O | WIFI模块电源使能 | P4_25 |
| SDIO | SDMMC1_D0_M0 | I/O | SDIO数据位0 | P3_29 |
|  | SDMMC1_D1_M0 | I/O | SDIO数据位1 | P3_27 |
|  | SDMMC1_D2_M0 | I/O | SDIO数据位2 | P3_41 |
|  | SDMMC1_D3_M0 | I/O | SDIO数据位3 | P3_39 |
|  | SDMMC1_CLK_M0 | O | SDIO时钟 | P3_33 |
|  | SDMMC1_CMD_M0 | I/O | SDIO命令信号 | P3_35 |
| PCM | SAI2_SDI_M0 | I | PCM数据输入 | P3_53 |
|  | SAI2_SDO_M0 | O | PCM数据输出 | P3_45 |
|  | SAI2_LRCK_M0 | O | PCM同步控制信号 | P3_51 |
|  | SAI2_SCLK_M0 | O | PCM时钟信号 | P3_47 |
| UART | UART4_TX_M1 | O | UART4数据发送 | P3_28 |
|  | UART4_RX_M1 | I | UART4数据接收 | P3_30 |
|  | UART4_RTSN_M1 | O | UART4发送请求 | P3_34 |
|  | UART4_CTSN_M1 | I | UART4发送允许 | P3_36 |


### 2.7.9  UART接口控制引脚
| **默认功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| UART0 | UART0_TX_M0_DEBUG | O | UART0数据发送 | P2_7 |
|  | UART0_RX_M0_DEBUG | I | UART0数据接收 | P2_9 |
| UART5 | UART5_TX_M1 | O | UART5数据发送 | P2_39 |
|  | UART5_RX_M1 | I | UART5数据接收 | P2_61 |
| UART6 | UART6_TX_M3 | O | UART6数据发送 | P4_21 |
|  | UART6_RX_M3 | I | UART6数据接收 | P4_23 |
| UART8 | UART8_TX_M0 | O | UART8数据发送 | P2_73 |
|  | UART8_RX_M0 | I | UART8数据接收 | P2_69 |
|  | UART8_RTSN_M0 | O | UART8发送请求 | P2_77 |
|  | UART8_CTSN_M0 | I | UART8发送允许 | P2_79 |


### 2.7.10  IIC接口控制引脚
| **默认功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| I2C0 | I2C0_SCL_M1 | O | I2C时钟 | P4_11 |
|  | I2C0_SDA_M1 | I/O | I2C数据 | P4_15 |
| I2C2 | I2C2_SCL_M0 | O | I2C时钟 | P2_11 |
|  | I2C2_SDA_M0 | I/O | I2C数据 | P2_1 |
| I2C3 | I2C3_SCL_M0 | O | I2C时钟 | P2_35 |
|  | I2C3_SDA_M0 | I/O | I2C数据 | P2_43 |
| I2C4 | I2C4_SCL_M3 | O | I2C时钟 | P4_45 |
|  | I2C4_SDA_M3 | I/O | I2C数据 | P4_43 |
| I2C5 | I2C5_SCL_M3 | O | I2C时钟 | P5_31 |
|  | I2C5_SDA_M3 | I/O | I2C数据 | P5_33 |
| I2C7 | I2C7_SCL_M1 | O | I2C时钟 | P1_70 |
|  | I2C7_SDA_M1 | I/O | I2C数据 | P1_72 |
| I2C8 | I2C8_SCL_M2 | O | I2C时钟 | P1_56 |
|  | I2C8_SDA_M2 | I/O | I2C数据 | P1_60 |
| HDMI_I2C | HDMI_TX_SCL | O | I2C时钟 | P1_68 |
|  | HDMI_TX_SDA | I/O | I2C数据 | P1_58 |


### 2.7.11  以太网接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| GMAC0 | ETH_CLK0_25M_OUT_M0 | O | PHY 25MHz 参考时钟输出 | P4_57 |
|  | ETH0_MCLK_M0 | I | PHY 125MHz 同步时钟输入 | P4_61 |
|  | GMAC0_INT | I | RGMII中断 | P3_94 |
|  | GMAC0_RESET | O | RGMII复位 | P3_92 |
|  | GMAC0_MDC_M0 | O | 串行管理时钟 | P4_49 |
|  | GMAC0_MDIO_M0 | I/O | 串行管理数据 | P4_47 |
|  | GMAC0_TXD3_M0 | O | RGMII数据发送3 | P4_10 |
|  | GMAC0_TXD2_M0 | O | RGMII数据发送2 | P4_12 |
|  | GMAC0_TXD1_M0 | O | RGMII数据发送1 | P4_14 |
|  | GMAC0_TXD0_M0 | O | RGMII数据发送0 | P4_16 |
|  | GMAC0_TXCTL_M0 | O | RGMII发送控制 | P4_18 |
|  | GMAC0_TXCLK_M0 | O | RGMII发送时钟 | P4_20 |
|  | GMAC0_RXD3_M0 | I | RGMII接收数据3 | P4_24 |
|  | GMAC0_RXD2_M0 | I | RGMII接收数据2 | P4_26 |
|  | GMAC0_RXD1_M0 | I | RGMII接收数据1 | P4_28 |
|  | GMAC0_RXD0_M0 | I | RGMII接收数据0 | P4_30 |
|  | GMAC0_RXCTL_M0 | I | RGMII接收控制 | P4_32 |
|  | GMAC0_RXCLK_M0 | I | RGMII接收时钟 | P4_34 |
| GMAC1 | ETH_CLK1_25M_OUT_M0 | O | PHY 25MHz 参考时钟输出 | P4_35 |
|  | ETH1_MCLK_M0 | I | PHY 125MHz 同步时钟输入 | P4_37 |
|  | GMAC1_INT | I | RGMII中断 | P2_19 |
|  | GMAC1_RESET | O | RGMII复位 | P2_21 |
|  | GMAC1_MDC_M0 | O | 串行管理时钟 | P4_7 |
|  | GMAC1_MDIO_M0 | I/O | 串行管理数据 | P4_5 |
|  | GMAC1_TXD3_M0 | O | RGMII数据发送3 | P4_38 |
|  | GMAC1_TXD2_M0 | O | RGMII数据发送2 | P4_40 |
|  | GMAC1_TXD1_M0 | O | RGMII数据发送1 | P4_42 |
|  | GMAC1_TXD0_M0 | O | RGMII数据发送0 | P4_44 |
|  | GMAC1_TXCTL_M0 | O | RGMII发送控制 | P4_46 |
|  | GMAC1_TXCLK_M0 | O | RGMII发送时钟 | P4_48 |
|  | GMAC1_RXD3_M0 | I | RGMII接收数据3 | P4_52 |
|  | GMAC1_RXD2_M0 | I | RGMII接收数据2 | P4_54 |
|  | GMAC1_RXD1_M0 | I | RGMII接收数据1 | P4_56 |
|  | GMAC1_RXD0_M0 | I | RGMII接收数据0 | P4_58 |
|  | GMAC1_RXCTL_M0 | I | RGMII接收控制 | P4_60 |
|  | GMAC1_RXCLK_M0 | I | RGMII接收时钟 | P4_62 |


### 2.7.12  MIPI_CSI接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| MIPI_CSI0 | MIPI_DPHY_CSI0_RX_D0_P | I | CSI数据0+ | P3_58 |
|  | MIPI_DPHY_CSI0_RX_D0_N | I | CSI数据0- | P3_60 |
|  | MIPI_DPHY_CSI0_RX_D1_P | I | CSI数据1+ | P3_64 |
|  | MIPI_DPHY_CSI0_RX_D1_N | I | CSI数据1- | P3_66 |
|  | MIPI_DPHY_CSI0_RX_CLK_P | I | CSI时钟+ | P3_70 |
|  | MIPI_DPHY_CSI0_RX_CLK_N | I | CSI时钟- | P3_72 |
|  | MIPI_DPHY_CSI0_RX_D2_P | I | CSI数据2+ | P3_76 |
|  | MIPI_DPHY_CSI0_RX_D2_N | I | CSI数据2- | P3_78 |
|  | MIPI_DPHY_CSI0_RX_D3_P | I | CSI数据3+ | P3_82 |
|  | MIPI_DPHY_CSI0_RX_D3_N | I | CSI数据3- | P3_84 |
| MIPI_CSI1 | MIPI_DPHY_CSI1_RX_D0_P | I | CSI数据0+ | P4_67 |
|  | MIPI_DPHY_CSI1_RX_D0_N | I | CSI数据0- | P4_65 |
|  | MIPI_DPHY_CSI1_RX_D1_P | I | CSI数据1+ | P4_73 |
|  | MIPI_DPHY_CSI1_RX_D1_N | I | CSI数据1- | P4_71 |
|  | MIPI_DPHY_CSI1_RX_CLK_P | I | CSI时钟+ | P4_79 |
|  | MIPI_DPHY_CSI1_RX_CLK_N | I | CSI时钟- | P4_77 |
| MIPI_CSI2 | MIPI_DPHY_CSI2_RX_D0_P | I | CSI数据0+ | P4_85 |
|  | MIPI_DPHY_CSI2_RX_D0_N | I | CSI数据0- | P4_83 |
|  | MIPI_DPHY_CSI2_RX_D1_P | I | CSI数据1+ | P4_91 |
|  | MIPI_DPHY_CSI2_RX_D1_N | I | CSI数据1- | P4_89 |
|  | MIPI_DPHY_CSI2_RX_CLK_P | I | CSI时钟+ | P4_97 |
|  | MIPI_DPHY_CSI2_RX_CLK_N | I | CSI时钟- | P4_95 |
| MIPI_CSI3 | MIPI_DPHY_CSI3_RX_D0_P | I | CSI数据0+ | P4_66 |
|  | MIPI_DPHY_CSI3_RX_D0_N | I | CSI数据0- | P4_68 |
|  | MIPI_DPHY_CSI3_RX_D1_P | I | CSI数据1+ | P4_72 |
|  | MIPI_DPHY_CSI3_RX_D1_N | I | CSI数据1- | P4_74 |
|  | MIPI_DPHY_CSI3_RX_CLK_P | I | CSI时钟+ | P4_78 |
|  | MIPI_DPHY_CSI3_RX_CLK_N | I | CSI时钟- | P4_80 |
| MIPI_CSI4 | MIPI_DPHY_CSI4_RX_D0_P | I | CSI数据0+ | P4_84 |
|  | MIPI_DPHY_CSI4_RX_D0_N | I | CSI数据0- | P4_86 |
|  | MIPI_DPHY_CSI4_RX_D1_P | I | CSI数据1+ | P4_90 |
|  | MIPI_DPHY_CSI4_RX_D1_N | I | CSI数据1- | P4_92 |
|  | MIPI_DPHY_CSI4_RX_CLK_P | I | CSI时钟+ | P4_96 |
|  | MIPI_DPHY_CSI4_RX_CLK_N | I | CSI时钟- | P4_98 |


### 2.7.13  MIPI_DSI接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | --- | :---: |
| MIPI_DSI | MIPI_DPHY_DSI_TX_D0_P | O | DSI数据0+ | P3_59 |
|  | MIPI_DPHY_DSI_TX_D0_N | O | DSI数据0- | P3_57 |
|  | MIPI_DPHY_DSI_TX_D1_P | O | DSI数据1+ | P3_65 |
|  | MIPI_DPHY_DSI_TX_D1_N | O | DSI数据1- | P3_63 |
|  | MIPI_DPHY_DSI_TX_CLK_P | O | DSI时钟+ | P3_71 |
|  | MIPI_DPHY_DSI_TX_CLK_N | O | DSI时钟- | P3_69 |
|  | MIPI_DPHY_DSI_TX_D2_P | O | DSI数据2+ | P3_77 |
|  | MIPI_DPHY_DSI_TX_D2_N | O | DSI数据2- | P3_75 |
|  | MIPI_DPHY_DSI_TX_D3_P | O | DSI数据3+ | P3_83 |
|  | MIPI_DPHY_DSI_TX_D3_N | O | DSI数据3- | P3_81 |
|  | PWM0_CH0_M0 | O | 屏幕PWM调光 | P2_13 |
|  | MIPI_DSI1_EN | O | 屏幕电源使能 | P4_39 |
|  | MIPI_DSI1_RESET | O | 屏幕触摸复位 | P4_9 |
|  | MIPI_DSI1_INT | I | 屏幕触摸中断 | P4_1 |


### 2.7.14  PCIE接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| PCIE | PCIE0_TX_P | O | PCIE数据发送+ | P2_78 |
|  | PCIE0_TX_N | O | PCIE数据发送- | P2_76 |
|  | PCIE0_RX_P | I | PCIE数据接收+ | P2_72 |
|  | PCIE0_RX_N | I | PCIE数据接收- | P2_70 |
|  | PCIE0_REFCLK_P | O | PCIE时钟输出+ | P2_66 |
|  | PCIE0_REFCLK_N | O | PCIE时钟输出- | P2_64 |
|  | PCIE0_WAKEn_M0 | I | PCIE唤醒激活信号 | P1_74 |
|  | PCIE0_CLKREQn_M0 | O | PCIE时钟请求信号 | P1_78 |
|  | PCIE0_PERSTn | I | PCIE复位信号 | P1_64 |
|  | PCIE0_PRSN2_3V3 | O | PCIE插入检测信号 | P4_3 |
|  | PCIE_PWR_EN_3V3 | O | PCIE 3.3V电源使能 | P4_19 |


### 2.7.15  HDMI接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| HDMI | HDMI_TX_HPDIN_M0_1V8 | I | HDMI热插拔检测 | P2_71 |
|  | HDMI_TX_CEC_M0 | I/O | HDMI_CEC识别 | P1_52 |
|  | HDMI_TX_SBD_N | O | HDMI_SBD(ARC)- | P1_17 |
|  | HDMI_TX_SBD_P | O | HDMI_SBD(ARC)+ | P1_19 |
|  | HDMI_TX_D3_N | O | HDMI差分数据3- | P1_23 |
|  | HDMI_TX_D3_P | O | HDMI差分数据3+ | P1_25 |
|  | HDMI_TX_D0_N | O | HDMI差分数据0- | P1_29 |
|  | HDMI_TX_D0_P | O | HDMI差分数据0+ | P1_31 |
|  | HDMI_TX_D1_N | O | HDMI差分数据1- | P1_35 |
|  | HDMI_TX_D1_P | O | HDMI差分数据1+ | P1_37 |
|  | HDMI_TX_D2_N | O | HDMI差分数据2- | P1_41 |
|  | HDMI_TX_D2_P | O | HDMI差分数据2+ | P1_43 |
|  | HDMI_TX_SCL | O | I2C时钟 | P1_68 |
|  | HDMI_TX_SDA | I/O | I2C数据 | P1_58 |


### 2.7.16  I2S音频接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| I2S | SAI1_MCLK_M0 | O | I2S主时钟 | P2_65 |
|  | SAI1_SCLK_M0 | I/O | I2S串行时钟 | P2_55 |
|  | SAI1_LRCK_M0 | I/O | I2S左右声道切换 | P2_53 |
|  | SAI1_SDO0_M0 | O | I2S串行数据输出 | P2_49 |
|  | SAI1_SDI0_M0 | I | I2S串行数据输入 | P2_59 |
|  | HP_DET_L | I | 耳机插入检测 | P2_29 |
|  | SARADC_VIN3_HP_HOOK | I | 耳机线控按键 | P1_34 |


### 2.7.17  CAN接口控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| CAN0 | CAN0_TX_M2_3V3 | O | CAN0数据发送 | P4_29 |
|  | CAN0_RX_M2_3V3 | I | CAN0数据接受 | P4_31 |
| CAN1 | CAN1_TX_M3_3V3 | O | CAN1数据发送 | P1_66 |
|  | CAN1_RX_M3_3V3 | I | CAN1数据接受 | P1_54 |


### 2.7.18  4G/5G模组控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| 4G/5G模组控制 | 4G/5G_PWREN | O | 供电使能 | P1_76 |
|  | 4G/5G_RESET | O | 4G/5G模组复位 | P2_51 |
|  | 4G/5G_MOD_PWREN | O | 4G/5G模组电源使能 | P1_80 |


### 2.7.19  ADC接口控制接口
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| ADC | SARADC_VIN2_HW_ID | I | ADC输入 | P1_32 |
|  | SARADC_VIN4 | I | ADC输入 | P1_36 |
|  | SARADC_VIN5 | I | ADC输入 | P1_38 |
|  | SARADC_VIN6 | I | ADC输入 | P1_40 |
|  | SARADC_VIN7 | I | ADC输入 | P1_42 |


### 2.7.20  其他控制引脚
| **功能** | **信号名称** | **I/O** | **默认功能** | **引脚号** |
| :---: | :---: | :---: | :---: | :---: |
| IO扩展 | IIC_GPIO_INT | I | IO扩展芯片中断 | P2_67 |


## 2.8  核心板硬件设计说明
   FET3576-C核心板已经将电源、存储电路集成于一个小巧的模块上，所需的外部电路非常简洁，构成一个最小系统只需要 12V 电源、复位按键、烧录SD卡、启动配置即可运行，如下图所示：  
![Image](./images/OK3576C_hardware/79133405fc0240818d903c9db15a160c.png)  
最小系统原理图可以参见附录四。不过一般情况下，除最小系统外建议连接上一些外部设备，例如调试串口，用来查看打印信息；预留OTG接口，用来输出调试信息。做好这些后，再在此基础上根据飞凌提供的核心板默认接口定义来添加用户需要的功能。

核心板外围电路的设计可参见第三章的3.5节“OK3576-C底板说明”。



# 03_OK3576-C嵌入式开发平台介绍

## 3.1  OK3576-C开发板接口图
飞凌OK3576-C开发平台核心板和底板采用接插件的连接方式，主要接口如下图所示：

![Image](./images/OK3576C_hardware/de566621a7ee4eddb1b0898d80a41e62.jpeg)

![Image](./images/OK3576C_hardware/ec45bef41f294fe39e46c17f3993659b.jpeg)

## 3.2  OK3576-C开发板尺寸图
OK3576-C开发板和天线板尺寸图如下：

![Image](./images/OK3576C_hardware/ff2e07381b08482c89e1044c92dccefa.png)

底板PCB尺寸：130mm×190mm，更多详细尺寸请见用户资料dxf文件；

固定孔尺寸：间距：120mm×180mm，孔径：3.2mm；

制版工艺：厚度1.6mm，4层PCB；

电源电压：直流12V； 

天线板用于4G，5G天线的安装固定，外形尺寸：20mm×140mm，更多详细尺寸参见下图：

OK3576-C底板预留了2个直径3.2mm散热片的安装孔，用户可以根据现场环境选配安装散热片，散热片和核心板接触面请加一层绝缘的导热硅胶垫。飞凌自选的核心板散热片尺寸为：38mm×38mm×23mm，更多详细尺寸参见下图： 

![Image](./images/OK3576C_hardware/a366a4ed569a4bf98fd4d4273309eb8f.jpeg)![Image](./images/OK3576C_hardware/60073a4142074c70913a41aee8bdcb6d.jpeg)

## 3.3  底板命名规范
ABC-D+IK:M

| **字段** | **字段描述** | **值** | **说明** |
| :---: | --- | --- | --- |
| A | 合格等级 | PC | 原型样品 |
|  |  | 空白 | 大规模生产 |
| B | 产品线标识 | OK | 飞凌嵌入式开发板 |
| C | CPU名称 | RK3576 | RK3576 |
| - | 分段标识 | - |  |
| D | 连接方式 | Cx | 板对板连接器 |
| + | 分段标识 | + | 此标识之后为配置参数部分 |
| I | 运行温度 | I | -40 to 85℃ |
| K | PCB版本号 | 10 | V1.0 |
|  |  | xx | Vx.x |
| :M | 厂家内部标识 | :X | 此内容为厂家内部标识，对客户使用无影响 |


## 3.4  底板资源
| **功能** | **数量** | **参数** |
| :---: | :---: | --- |
| MIPI CSI | 5 | 1 x MIPI DPHY V2.0 4lanes接口，每lane最高支持4.5Gbps；通过1个26pins FPC座引出，默认挂载OV13855摄像头； |
|  |  | 4 xMIPI DPHY V1.2 2lanes接口，每lane最高支持2.4Gbps；通过4个26pins FPC座引出，默认挂载OV5645摄像头； |
| MIPI DSI | 1 | MIPI接口支持4 lanes输出，最高分辨率为2560 x 1600@60Hz； |
|  |  | 适配飞凌7吋MIPI屏，分辨率为1024x 600@30fps； |
| HDMI TX | 1 | 通过标准HDMI插座引出； |
|  |  | HDMI v2.1 最高支持 4K@120Hz； |
| DP TX | 1 | 1个DP接口与USB3.1 Gen1结合使用，通过Type-C接口引出； |
|  |  | DisplayPort v1.4 最高支持4K@120Hz； |
| USB3.1 Gen1 | 1 | 通过Type-C接口引出； |
|  |  | 与DP TX结合使用； |
| USB3.0 HOST | 3 | 通过3个Type-A USB接口引出； |
| PCIe2.0 | 1 | 通过PCIe x 1插槽引出； |
|  |  | 支持5Gbps速率； |
| Ethernet | 2 | 通过2个RJ45接口引出； |
|  |  | 支持10/100/1000 Mbps数据传输速率； |
| TF卡 | 1 | 可插入TF卡，速率达150MHz，支持SDR104 模式； |
| Audio | 1 | 板载Codec芯片，支持耳机输出、MIC输入级Speaker输出等功能； |
| CAN | 2 | 通过CAN收发器引出两路CAN总线； |
|  |  | 遵循 CAN 和 CAN FD 规范； |
| RS485 | 2 | 通过RS485收发器引出2路RS485总线； |
| UART | 1 | 通过2.44mm间距引出； |
|  |  | 波特率高达4Mbps； |
| 4G/5G | 1 | 支持M.2封装的4G/5G模块； |
| WIFI&BT | 1 | 板载海华AW-CM358SM-WIFI&BT模块； |
|  |  | 支持WIFI 2.4G/5G ,蓝牙5.0； |
| ADC | 5 | 通过2.44mm间距排针引出； |
|  |  | 12bit单端输入SAR-ADC，采样率高达1MS/s； |
| RTC | 1 | 板载RTC芯片及电池插座； |
| GPIO | 8 | 通过2.44mm间距排针引出8路GPIO、同时引出3.3V和1.8V电源； |


**注：**

1. **表中参数为硬件设计或CPU理论值；**
2. **“TBD”表示现阶段暂未开发功能；**

## 3.5  OK3576-C底板说明
**注：下图中元件位号有“_DNP”标识的，代表此元器件默认不焊接。**

**本章节的原理图仅是为了方便阅读，可能会有更改，请用户设计一定要按照源文件原理图为准。**

### 3.5.1  底板电源
开发板使用12V电源适配器供电，电源接口为DC005规格的插座。拨动开关S1为开发板的电源开关，按照底板丝印指示方向拨动开关控制上下电。S1后级并联TVS管进行静电防护，F1保险丝进行过流保护，D1与F1配合进行防反接保护。VCC12V_DCIN同时给FET3576核心板和底板其他外设进行供电。

![Image](./images/OK3576C_hardware/8f0d16a14b7c4f4c83fabcd2938e9030.png)

VCC12V_DCIN通过U3（DC-DC）降压至VCC_5V，VCC_5V给底板其他外设供电。（这里需要注意12V降5V DC-DC芯片选型时，芯片的输出功率要足够大，建议输出电流6A以上，保证为后级提供足够电流）

核心板通过12V供电正常启动后，通过CARRIER_BOARD_EN引脚输出高电平，来控制U3使能输出VCC_5V电源为开发板的部分外设供电。（该信号电平为3.3V，驱动能力为10K上拉，如果被使能设备使能引脚所需驱动能力超出该范围，则需要添加缓冲器或者门电路用来增加驱动能力，确保核心板和底板上电正常）。

![Image](./images/OK3576C_hardware/128471a6a74f4f279a2e2e18a6d1f500.png)

VCC_5V通过U4（DC-DC）降压至VCC_3V3。VCC_3V3电源为开发板的部分设备供电。

![Image](./images/OK3576C_hardware/7630fdfda1b84ce6adff7ee928028331.png)

VCC_3V3通过U2（LDO）降压至VCC_1V8。VCC_1V8电源为开发板的部分设备供电。

![Image](./images/OK3576C_hardware/4b99d7b608354ef19a887be439626779.png)

**注意：**

**1、客户自行设计时，务必保证电源的上电时序；**

**2、升降压芯片的器件选型及外部布局需要参考对应的芯片手册，确保良好的电源回路。**

### 3.5.2  复位及开关机信号
RESET_L为核心板复位信号输入，为方便调试，连接到按键上。

![Image](./images/OK3576C_hardware/11b99632bfc042ed97ef04c08ac8aaaf.png)

PWRON_L为核心板开关机信号输入，为方便调试，连接到按键上。 

同时PWRON_L信号预留1个2.54mm间距端子座，默认空焊，便于用户扩展。

![Image](./images/OK3576C_hardware/4d5fa53c86e54842b22f061c06ef68bc.png)  
![Image](./images/OK3576C_hardware/76daf64a1cd74d02b29080fb0cda37d8.png)

需要注意核心板连接器P3_10脚的PMIC_VDC信号，该信号可以切换核心板的两种开机模式，上电开机或按键开机；在OK3576-C上通过选焊R331电阻来实现此功能；R331空焊即引脚悬空时，核心板默认上电启动(默认配置)；R331焊接即引脚拉低时，核心板上电不启动，按下PWRON_L按键后启动。  
![Image](./images/OK3576C_hardware/141723d3172043ad915f957437b23552.png)  
![Image](./images/OK3576C_hardware/06d0eb1f49fc42ad883df1c6455c9c1a.png)

### 3.5.3  Boot配置
RK3576支持多种启动引导方式，在芯片复位结束后，芯片内部集成的引导代码可以在如下接口设备进行引导，具体引导顺序可根据实际应用需求进行选择：

·Serial Flash(FSPI0、FSPI1_M0、FSPI1_M1)

·eMMC

·UFS

·SDMMC0 Card

如果在上述设备中没有引导代码，可以通过USB2.0 OTG0接口USB2_OTG0_DP/DM信号将系统代码下载到这些设备中，同时也支持从USB 3.2 Gen1x1 OTG0接口的USB3_OTG0_SSRX1P/N与USB3_OTG0_SSTX1P/N信号烧录固件。请注意，如果需要支持USB3.0升级固件且需要支持2Lane DP 时，必须采用USB3.2 Gen1x1 OTG0+DP 2Lane(Swap ON)的方案。

**引导顺序选择**：

RK3576的Boot启动顺序可以通过SARADC_VIN0_BOOT Pin（PIN：P1_28）进行设置，从不同接口对应的外设启动，如下表所示硬件通过配置不同的上下拉电阻值，设计 Config1-Config11 共 11 种模式的外设引导顺序，可根据实际应用需求进行对应配置。

表3.5.3.1 Boot启动顺序配置表

| Item | Rup | Rdown | ADC | BOOT MODE |
| :---: | :---: | :---: | :---: | --- |
| Config1 | DNP | 10K | 0 | USB (Maskrom mode) |
| Config2 | 10K | 1.13K | 416 | FSPI0→USB |
| Confi 3 | 10K | 2.49K | 816 | FSPI1_M0→EMMC→USB |
| Config4 | 10K | 4.3K | 1231 | FSPI1_M1→EMMC→USB |
| Config5 | 10K | 6.8K | 1658 | FSPI0→UFS→USB |
| Config6 | 10K | 10K | 2048 | FSPI1_M0→UFS→USB |
| Config7 | 10K | 14.7K | 2437 | UFS→USB |
| Config8 | 10K | 23.2K | 2862 | UFS→SDMMC0→USB |
| Config9 | 10K | 40.2K | 3279 | RFU |
| Config10 | 10K | 88.7K | 3680 | EMMC→SDMMC0→USB |
| Config11 | 10K | DNP | 4095 | EMMC→USB |


核心板上SARADC_VIN0_BOOT配置为10K上拉，因此核心板默认从eMMC启动。底板可以增加下拉电阻，以实现其他的引导顺序。按照以上Config1设置，OK3576-C将SARADC_VIN0_BOOT通过轻触按键连接至GND，以实现Maskrom mode。

![Image](./images/OK3576C_hardware/75639444b4a14617b9233b34d6378034.png)

SARADC_VIN1用于对地短路进入Recovery状态，核心板将其用10K电阻上拉至1.8V电源。OK3576-C上，按键阵列采用并联型，可以通过增减按键并调整分压电阻比例来调整输入键值，实现多键输入以满足客户产品需求；设计中建议任意两个按键键值必须大于±35，即中心电压差必须大于123mV。如下图：

![Image](./images/OK3576C_hardware/c033443731a848318c3abca3ff78bb6c.png)

**注意:**

**1、用于按键采集时，靠近按键需做ESD防护，而且0键值的必须串接100ohm电阻加强抗静电浪涌能力（如果只有一个按键时，ESD必须靠近按键，先经过ESD→100ohm电阻→1nF→芯片管脚）；**  

**2、多个按键时，靠近每个按键放置一个ESD管；**

### 3.5.4  系统初始化配置信号
FET3576中有一个重要信号会影响系统的启动配置，需要在上电前配置完毕并保持状态稳定：

SDMMC0_DET_L（PIN：P3_90）（默认功能为SDMMC_DET）：决定 VCCIO1 电源域 IO 是 SDMMC0 还是 JTAG 功能。

FET3576的JTAG功能与SDMMC功能复用在一起，通过SDMMC0_DET_L管脚来切换IOMUX的功能，故该管脚也需要在上电前完成配置，否则JTAG功能无输出会影响到引导阶段的调试，而SDMMC0无输出会影响到SDMMC0 boot功能。

![Image](./images/OK3576C_hardware/31a0ba653cf8430b98028456f1540d06.png)

1. 该管脚检测为高电平，则对应IO切换到JTAG功能；
2. 当检测到为低电平（大部分SD卡插入会拉低该管脚，如果不是需要特殊处理），对应IO切换为SDMMC0 功能；
3. 系统起来后，可切换成由寄存器来控制IOMUX，那么该管脚可以释放出来；
4. 为方便查询，这个管脚的配置状态与功能对应如下表所示：

表3.5.4.1 FET3576系统初始化配置信号描述 

| 信号名 | 内部上下拉 | 描述 |
| :---: | :---: | --- |
| SDMMC0_DET_L | 上拉 | SDMMC/ARM JTAG管脚复用选择控制信号：   0：识别为SD卡插入，SDMMC/ JTAG管脚复用为SDMMC0功能；   1：未识别为SD卡插入，SDMMC/ JTAG管脚复用为 JTAG功能（Default） |


### 3.5.5  JTAG与 UART Debug电路
RK3576 芯片的 JTAG 接口符合 IEEE1149.1 标准，PC 可通过 SWD 模式（两线模式）连接 DSTREAM

仿真器，调试芯片内部的 ARM Core。

JTAG 接口说明如下表所示：

表3.5.5.1 FET3576 JTAG Debug接口信号

| 信号名 | 描述 |
| --- | --- |
| JTAG_TCK_M0/M1 | SWD模式时钟输入 |
| JTAG_TMS_M0/M1 | SWD模式数据输入输出 |


RK3576的JTAG有2个复用，其中JTAG_TCK_M0/JTAG_TMS_M0位于VCCIO1域，和SDMMC0复用IOMUX；JTAG_TCK_M1/JTAG_TMS_M1位于PMUIO1域，和UART_Debug——UART0_M0复用，IOMUX复用情况如下图所示。

![Image](./images/OK3576C_hardware/cfe2f8173baa4f5aa336290e0a729450.png)



FET3576的UART Debug默认选择UART0_TX_M0_DEBUG（P2_7）/UART0_RX_M0_DEBUG（P2_9）。UART Debug信号如果使用插件引出，则需要串接100ohm电阻，靠近插件位置需增加TVS管。

OK3576-C开发板为方便用户调试，使用USB转UART芯片将UART Debug信号转成USB信号，通过Type-C插座引出，用户用USB Type-A转UAB Type-C的线将OK3576-C的P16与PC机连接，安装CP2102驱动即可。原理图如下：

![Image](./images/OK3576C_hardware/68baad275cec4f00baa797b0c39bb54c.png)![Image](./images/OK3576C_hardware/85940f31576a4273adae6f580311ea22.png)![Image](./images/OK3576C_hardware/c136cb7b66f9493faacc165c9fc08c00.png)

**注意:**

**1、为方便后期调试，请用户在自行设计底板时将此调试串口引出；**

**2、建议保留Q1、Q2，这样能有效防止核心板未上电时，U6电流通过UART0_TX/RX回流到CPU中，影响启动，甚至造成损坏。**

### 3.5.6  IIC扩展IO
为了引出更为丰富的接口，底板部分使能和复位信号由IIC转IO芯片U5完成。同时U5空余的部分IO通过P17引出，方便用户扩展，原理如下图：

![Image](./images/OK3576C_hardware/4662d734d2fd451d80ccbcc0f1fec066.png)![Image](./images/OK3576C_hardware/bd9362fafb61419e992a895d40989028.png)

### 3.5.7  SARADC接口
OK3576-C通过P18将SARADC_VIN2/VIN4/VIN5/VIN6/VIN7引出，R371为可变电阻，通过将SARADC_VIN2/VIN4/VIN5/VIN6/VIN7与P18的4、6、8、10排针短接，在调整R371可变电阻阻值时，通过ADC可以读取到电压变化。如下图所示：

![Image](./images/OK3576C_hardware/ac8103e9d74e4116ab0b662e85c48db9.png)

**注意:**

**1.SARADC_VINx在使用时，靠近管脚必须增加1nF电容消抖；**

### 3.5.8  TF Card
底板P20为TF Card接口，可以支持系统启动与烧写。

![Image](./images/OK3576C_hardware/352d8ac8e5094294ab9dfb75c37235d9.png)![Image](./images/OK3576C_hardware/edf162fa27b54aac94b778525498828b.png)

**注意：**

**1、TF卡供电电源需要受控，参考底板电路；**

**2、SDIO阻抗要求： 单端50ohm，信号等长控制50mil;**

### 3.5.9  RTC电路
OK3576-C提供一个板载外置RTC功能，以实现更精准计时和更低功耗，原理图如下：

![Image](./images/OK3576C_hardware/35d8ae772bc0493dbaa606aedee55494.png)

### 3.5.10  Ethernet电路
底板支持双路1000/100/10M以太网接口，通过RJ45引出。

![Image](./images/OK3576C_hardware/8980d1a7e5dd4ae8a5219f0b5d81a322.png)![Image](./images/OK3576C_hardware/8a00c3e7214e44768e8b3dc95daaf12d.png)

**<font style="color:#ff0000;">注：</font>**

**<font style="color:#ff0000;">1.下表为RK3576 RGMII/RMII接口设计：</font>**

**<font style="color:#ff0000;">表3.5.10.1 RK3576 RGMII/RMII接口设计</font>**

| **信号** | **IO类型**   **（芯片端）** | **RGMII接口** | **信号描述** | **RMII接口** | **信号描述** |
| :---: | :---: | :---: | :---: | :---: | :---: |
| <font style="color:rgb(255, 0, 0);">GMACx_TXD[3:0]</font> | <font style="color:rgb(255, 0, 0);">输出</font> | <font style="color:rgb(255, 0, 0);">RGMIIxTXD[3:0]</font> | <font style="color:rgb(255, 0, 0);">数据发送</font> | <font style="color:rgb(255, 0, 0);">RMIIx_TXD[1:0]</font> | <font style="color:rgb(255, 0, 0);">数据发送</font> |
| <font style="color:rgb(255, 0, 0);">GMACx_TXCLK</font> | <font style="color:rgb(255, 0, 0);">输出</font> | <font style="color:rgb(255, 0, 0);">RGMIIx_TXCLK</font> | <font style="color:rgb(255, 0, 0);">数据发送参考时钟</font> | <font style="color:rgb(255, 0, 0);">--</font> | <font style="color:rgb(255, 0, 0);">--</font> |
| <font style="color:rgb(255, 0, 0);">GMACx_TXCTL</font> | <font style="color:rgb(255, 0, 0);">输出</font> | <font style="color:rgb(255, 0, 0);">RGMIIx_TXCTL</font> | <font style="color:rgb(255, 0, 0);">数据发送使能（上升沿）和数据发送错误（下降沿）</font> | <font style="color:rgb(255, 0, 0);">RMIIx_TXEN</font> | <font style="color:rgb(255, 0, 0);">数据发送使能信号</font> |
| <font style="color:rgb(255, 0, 0);">GMACx_RXD[3:0]</font> | <font style="color:rgb(255, 0, 0);">输入</font> | <font style="color:rgb(255, 0, 0);">RGMIIx_RXD[3:0]</font> | <font style="color:rgb(255, 0, 0);">数据接收</font> | <font style="color:rgb(255, 0, 0);">RMIIx_RXD[1:0]</font> | <font style="color:rgb(255, 0, 0);">数据接收</font> |
| <font style="color:rgb(255, 0, 0);">GMACx_RXCLK</font> | <font style="color:rgb(255, 0, 0);">输入</font> | <font style="color:rgb(255, 0, 0);">RGMIIx_RXCLK</font> | <font style="color:rgb(255, 0, 0);">数据接收参考时钟</font> | <font style="color:rgb(255, 0, 0);">--</font> | <font style="color:rgb(255, 0, 0);">--</font> |
| <font style="color:rgb(255, 0, 0);">GMACx_RXCTL</font> | <font style="color:rgb(255, 0, 0);">输入</font> | <font style="color:rgb(255, 0, 0);">RGMIIx_RXCTL</font> | <font style="color:rgb(255, 0, 0);">数据接收有效（上升沿）和接收错误（下降沿）</font> | <font style="color:rgb(255, 0, 0);">RMIIx_RXCTL</font> | <font style="color:rgb(255, 0, 0);">数据接收有效和载波侦听</font> |
| <font style="color:rgb(255, 0, 0);">GMACx_MCLKINOUT</font> | <font style="color:rgb(255, 0, 0);">输入/输出</font> | <font style="color:rgb(255, 0, 0);">RGMIIx_MCLKI_</font>   <font style="color:rgb(255, 0, 0);">125M</font> | <font style="color:rgb(255, 0, 0);">PHY发送125MHz给MAC，可选</font> | <font style="color:rgb(255, 0, 0);">RMII_MCLKIN_50M or RMII_MCLKOUT_50M</font> | <font style="color:rgb(255, 0, 0);">RMII数据发送和数据接收参考时钟</font> |
| <font style="color:rgb(255, 0, 0);">ETHx_REFCLKO_</font>   <font style="color:rgb(255, 0, 0);">25M</font> | <font style="color:rgb(255, 0, 0);">输出</font> | <font style="color:rgb(255, 0, 0);">ETHx_REFCLK_</font>   <font style="color:rgb(255, 0, 0);">25M</font> | <font style="color:rgb(255, 0, 0);">RK3576提供25MHz时钟替代PHY晶体</font> | <font style="color:rgb(255, 0, 0);">ETHx_REFCLKO_</font>   <font style="color:rgb(255, 0, 0);">25M</font> | <font style="color:rgb(255, 0, 0);">RK3576提供25MHz时钟替代PHY晶体</font> |
| <font style="color:rgb(255, 0, 0);">GMACx_MDC</font> | <font style="color:rgb(255, 0, 0);">输出</font> | <font style="color:rgb(255, 0, 0);">RGMIIx_MDC</font> | <font style="color:rgb(255, 0, 0);">管理数据时钟</font> | <font style="color:rgb(255, 0, 0);">RMIIx_MDC</font> | <font style="color:rgb(255, 0, 0);">管理数据时钟</font> |
| <font style="color:rgb(255, 0, 0);">GMACx_MDIO</font> | <font style="color:rgb(255, 0, 0);">输入/输出</font> | <font style="color:rgb(255, 0, 0);">RGMIIx_MDIO</font> | <font style="color:rgb(255, 0, 0);">管理数据输出/输入</font> | <font style="color:rgb(255, 0, 0);">RMIIx_MDIO</font> | <font style="color:rgb(255, 0, 0);">管理数据输出/输入</font> |


**<font style="color:#ff0000;">2.在RGMII模式下，RK3576芯片内部TX/RX时钟路径集成了delayline，支持调整；参考图默认配置是：TXCLK与data之间时序由MAC来控制，RXCLK与data之间时序由PHY来控制（如使用RTL8211F/FI即RXCLK默认开启2nS delay，其它PHY要注意这个配置）；</font>**

**<font style="color:#ff0000;">3.GMAC0接口电平仅支持1.8V，GMAC1接口电平默认为3.3V（如必须要改成1.8V，请联系飞凌），需要注意PHY芯片RGMII信号电源域供电电压是否和GMACx接口电平匹配；</font>**

**<font style="color:#ff0000;">4.Ethernet PHY的Reset信号需要用GPIO来控制，GPIO的电平必须和PHY IO电平匹配，靠近PHY管脚必须增加100nF电容，加强抗静电能力，注意：RTL8211F/FI的复位管脚只支持3.3V电平；</font>**

**<font style="color:#ff0000;">5.TXD0-TXD3，TXCLK，TXEN需在FET3576端预留串接0ohm电阻，根据实际情况有条件提高信号质量；</font>**

**<font style="color:#ff0000;">6.RXD0-RXD3，RXCLK，RXDV需在PHY端串接22ohm电阻，以提高信号质量；</font>**

**<font style="color:#ff0000;">7.PHY使用外置晶体时，晶体电容请根据实际使用的晶体的负载电容值选择，控制频偏在±20ppm以内；</font>**

**<font style="color:#ff0000;">8.</font>** **<font style="color:#ff0000;">RTL8211F/FI的RSET管脚外接电阻为2.49K ohm精度为1%，不得随意修改；</font>**

**<font style="color:#ff0000;">9.</font>** **<font style="color:#ff0000;">MDIO必须外部加上拉电阻，推荐1.5-1.8Kohm，上拉电源必须和IO电源保持一致；</font>**

**<font style="color:#ff0000;">10.PCB Layout需要保证RGMII信号参考平面完整，需要保证PHY芯片外围电源参考平面完整；</font>**

**<font style="color:#ff0000;">11.等长要求：RGMII的接收和发送可分组等长，等长要求≤12.4mil；</font>**

**<font style="color:#ff0000;">12.阻抗要求：单端50ohm；</font>**

### 3.5.11  RS485接口
OK3576-C支持两路RS485接口

RS485收发器芯片U8/U9，收发器芯片信号为TDH341S485S，隔离耐压高达5000VDC，总线静电防护能力高达15kV（HBM），＞25Kv/us瞬态抗扰度。同时OK3576-C底板兼容了更高级别的浪涌脉冲群多级防护电路，如下图所示：

![Image](./images/OK3576C_hardware/0400e8b56e6f40ef859c3edb71a3575c.png)

### 3.5.12  CAN接口
OK3576-C板载两个CAN收发器芯片U10、U11，收发器芯片信号为TDH541SCANFD，隔离耐压高达5000VDC，总线静电防护能力高达15kV（HBM），＞25Kv/us瞬态抗扰度。同时OK357-C底板兼容了更高级别的浪涌脉冲群多级防护电路，如下图所示：

![Image](./images/OK3576C_hardware/d2fbac0305374352a5a8d71e04c06471.png)

### 3.5.13  Audio
OK3576-C板载一个I2S接口的Codec芯片U31，支持MIC输入、耳机输出以及1W 8Ω喇叭输出。原理如下图所示：

![Image](./images/OK3576C_hardware/8143d666b6b14f10b434b85c234ec6b9.png)

### 3.5.14  4G&5G接口
OK3576-C集成一个M.2 Key-B接口，兼容4G和5G模块，由于4G和5G模块供电电压不同，因此需要拨动S2，选择相应的供电电压。

![Image](./images/OK3576C_hardware/1cd3de7564904bbdaf19e4439150b9df.png)

### 3.5.15  USB2.0/USB3.0_A/Type-C USB3.0电路
RK3576芯片内置两个USB3 OTG控制器，两个USB3控制器都内嵌了USB2.0 OTG。

**其中USB3 OTG0/DP1.4接口应用如下**

USB3.2 Gen1x1 OTG0/DP1.4组成Combo PHY，USB3 OTG0控制器与PHY的内部复用图如下：

![Image](./images/OK3576C_hardware/c919cbe6c1e140699b1b967b039ca5e8.png)

USB3 OTG0控制器支持SS/HS/FS/LS，内嵌的USB2.0（HS/FS/LS）信号采用USB2.0 OTG PHY，信号名见下图的红色方框内；RK3576默认使用该接口做Fireware的Download，应用中请务必要预留出此接口。

![Image](./images/OK3576C_hardware/2dd1e32feccf41259764dee9d1ec2981.png)

**注意：USB2_OTG0_DP/USB2_OTG0_DM支持Download Firmware，如果产品不用这个接口，在调试与生产过程中必须要预留此接口，注意：USB2_OTG0_VBUSDET也必须连接！**

USB 3.2的SS信号（5Gbps）与DP1.4复用，使用USB/DP的Combo PHY；信号如下图的红色方框内。

![Image](./images/OK3576C_hardware/f8cb831b0c534f8eb8ab698dd73da5b4.png)

由于USB3的OTG和USB2.0的OTG是同一个USB3的控制器，因此USB3和USB2.0的OTG只能同时做Device或者做HOST，不能USB3的OTG做HOST，USB2.0的OTG做Device或者USB3 的OTG做Device而USB2.0的OTG做HOST。

USB3 OTG0 Controller和DP1.4 Controller通过USB3/DP1.4的Combo PHY组合成一个完整的 TYPEC口，此Combo PHY支持Display Alter mode，Lane0和Lane2在DP mode下做TX，在USB mode下做 RX；TX和RX共享Lane0和Lane2。

这个USB3/DP1.4的Combo PHY支持Lane间的交换（SWAP），因此一个TYPEC标准口可以有如下五种的配置：

配置一：Type-C 4Lane(with DP function)

![Image](./images/OK3576C_hardware/784ef4f2cd9248f7a2f76fb9d1ade09a.png)

配置二：USB2.0 OTG+DP1.4 4Lane(Swap OFF)

![Image](./images/OK3576C_hardware/7b815bee410a4b1aa09070399bdf21e3.png)

配置三：USB2.0 OTG+DP1.4 4Lane(Swap ON)

![Image](./images/OK3576C_hardware/b58f70e57c734601aabe543b544778d8.png)

配置四：USB3.2 Gen1x1 OTG0+DP1.4 2Lane(Swap OFF)

![Image](./images/OK3576C_hardware/8ade452fcd524726b81444611043dd94.png)

配置五：USB3.2 Gen1x1 OTG0+DP1.4 2Lane(Swap ON)

![Image](./images/OK3576C_hardware/e286b0e502c14e07adc6c020d9e6df67.png)

**注意：RK3576支持从USB 3.2 Gen1x1 OTG0接口的USB3_OTG0_SSRX1P/N与USB3_OTG0_SSTX1P/N 信号下载固件。需要支持USB3.0升级固件且需要支持2Lane DP时，必须采用USB3.2 Gen1x1 OTG0+DP 2Lane(Swap ON)的方案。**

**其中USB3 OTG1接口应用如下**

PCIE1/SATA1/USB3 OTG1组成Comb PHY1，USB3 OTG1控制器与PHY的内部复用图如下：

![Image](./images/OK3576C_hardware/51d12731e5604d7ba52ac681951a05e9.png)

USB3 OTG1控制器支持SS/HS/FS/LS，内嵌了USB2.0（HS/FS/LS）信号构成PCIE1/SATA1/USB3 OTG1 COMBO PHY1；管脚分布如下：

![Image](./images/OK3576C_hardware/aab6facb553540f1a7f8d5b7b7bc0364.png)

USB20 OTG1 的管脚分配如下图：

![Image](./images/OK3576C_hardware/24df6f6f007d4f4d9c55255988d5d756.png)

由于USB3的OTG1和USB2.0的OTG1是同一个USB3的控制器，因此USB3和USB2.0的OTG1 只能同时做Device或者做HOST，不能USB3的OTG做HOST，USB2.0的OTG做Device或者USB3 的OTG做Device而USB2.0的OTG做HOST。

**注意：PCIE1/SATA1/USB3 OTG1 的 COMBO PHY1 设置成 PCIe 或者 SATA 功能时，USB3 OTG1 功能不能使用，并且 USB2.0 PHY1 也不能使用；因此要使用 USB2.0 OTG1 时，PCIE1/SATA1/USB3 OTG1 的 COMBO PHY1 必须设置成 USB3 功能！！！**

PCIE1/SATA1/USB3 OTG1 的 COMBO PHY1 中 USB3 OTG1 的应用方式有如下几种：

配置一：USB3.2 Gen1x1 OTG1

![Image](./images/OK3576C_hardware/aed730f162db4d128a3852fb8a1cf90c.png)

配置二：USB2 OTG1

![Image](./images/OK3576C_hardware/2d61f0bb3af643af8758b77777ecff50.png)

配置三：USB2/USB3 不用，PCIE 和 SATA 的具体应用方式详见 PCIE 和 SATA 章节

![Image](./images/OK3576C_hardware/efb291338ec0463085815b8ee4c453a6.png)



OK3576-C开发板上使用一颗USB HUB芯片将单路USB2.0/USB3.0_HOST转为4路，其中三路USB3.0分别接到3个Type-A接口供客户使用，每一路可提供最大1A电流输出并具有限流开关保护功能，剩余一路USB3.0提供给4G&5G模块使用。

FET3576支持一路USB/DP组合接口，支持USB 3.2 Gen1x1，DisplayPort v1.4；在OK3576-C底板上设计为一个标准的Type-C USB 3.0全功能接口，支持数据传输与DP显示输出。

下图是USB3.0 HUB部分的电路：

![Image](./images/OK3576C_hardware/a22b9efda78144d38876278dafe21c6b.png)![Image](./images/OK3576C_hardware/3a9fdba28dca45d3a91f3020aa48aa30.png)

额外使用两颗开关电源为USB HUB芯片提供3.3V和1.2V的电源：

![Image](./images/OK3576C_hardware/bb14a6cc1e0f4a5d8f44a7a26f867490.png)

USB HUB芯片转出的三路USB3.0接口都搭配USB供电限流开关芯片，为Type-A接口提供稳定的电源和限流保护功能：

![Image](./images/OK3576C_hardware/e19224f0e51848b6bfd0f2e8018654d7.png)  
![Image](./images/OK3576C_hardware/bb124fbb6d57433b952f6a47278b8b9f.png)  
![Image](./images/OK3576C_hardware/ebbdcd11f4a049e7bf6818d041efb909.png)

**注意： **

**1. USB数据线都需要做90Ω差分阻抗；**

**2. 请选择合适的ESD器件；**

下图是Type-C USB 3.0接口部分的电路：

![Image](./images/OK3576C_hardware/edde3b2b1bfe403eaaa2a203ee2285ff.png)

上图是Type-C接口CC协议芯片电路，用来支持Type-C正反插识别等功能；

![Image](./images/OK3576C_hardware/dce80cc4edcf41fabce3fe484ac8b528.png)

上图是Type-C USB3.0接口的差分信号电路与ESD防护器件。

**<font style="color:#ff0000;">注意：</font>**

**<font style="color:#ff0000;">1.</font>** **<font style="color:#ff0000;"> USB2_OTG0_DN/</font>** **<font style="color:#ff0000;">USB2_OTG0_DP是系统固件烧写口，如果产品不用这个接口，在调试与生产过程中必须要预留此接口，不然会无法调试及生产烧写固件；</font>**

**<font style="color:#ff0000;">2.</font>** **<font style="color:#ff0000;">USB2_OTG0_ID内部有大概12Kohm电阻上拉到1.8V；</font>**

**<font style="color:#ff0000;">3.  </font>******<font style="color:#ff0000;">USB2_OTG0_VBUSDET是OTG和Device模式检测脚，芯片内部有一个下拉40Kohm的电阻；高为DEVICE 设备，2.7-3.3V，TYP：3.0V，建议在管脚放置一个100nF电容。</font>**

**<font style="color:#ff0000;">4.  OTG模式可以设置以下三种模式：</font>**

**<font style="color:#ff0000;">·	OTG模式：根据ID脚状态自动切换是device模式或HOST模式，ID高为device，ID拉低为HOST，处在device模式时，还会判断VBUSDET脚是否为高（大于2.3V），如果为高，才会拉高DP，开始枚举；</font>**

**<font style="color:#ff0000;">·Device模式：设置为这个模式时，无需ID脚，只需判断VBUSDET脚是否为高（大于2.3V），如果为高，才会拉高DP，开始枚举；</font>**

**<font style="color:#ff0000;">·HOST模式：设置为这个模式时，ID和VBUSDET状态都无需要关心。（如果产品只需要HOST模式，但是由于仅USB2_OTG0_DN/ USB2_OTG0_DP是系统固件烧写口，在调试与生产过程都需要用这个口，烧写和adb调试时，需要设置成device模式，因此USB2_OTG0_VBUSDET信号也必须接）。</font>**

**<font style="color:#ff0000;">若采用TYPEC接口， USB2_OTG0_VBUSDET信号通过4.7K电阻拉高到3.3V即可。</font>**

**<font style="color:#ff0000;">5.  为加强抗静电和浪涌能力，信号上必须预留ESD器件，USB2.0信号的ESD寄生电容不得超过3pF，另外USB2.0信号的DP/DM串接2.2ohm电阻，加强抗静电浪涌能力；</font>**

**<font style="color:#ff0000;">6.  为抑制电磁辐射，可以考虑在信号线上预留共模电感（Common mode choke），在调试过程中根据实际情况选择使用电阻或者共模电感；</font>**

**<font style="color:#ff0000;">7.</font>** **<font style="color:#ff0000;">如果有用USB2_OTG0_ID信号，为加强抗静电和浪涌能力，信号上必须预留ESD器件，而且串接100ohm电阻，不得删减；</font>**

**<font style="color:#ff0000;">8.</font>** **<font style="color:#ff0000;">当HOST功能时，5V电源建议增加限流开关，限流大小根据应用需要可调整，限流开关使用3.3V的GPIO控制，建议5V电源增加22uF和100nF以上的电容滤波；若USB口可能接移动硬盘，建义滤波增加电容到100uF以上。</font>**

**<font style="color:#ff0000;">9.</font>** **<font style="color:#ff0000;">TYPEC协议要求在SSTXP/N线上增加100nF交流耦合电容，AC耦合电容建议使用0201封装，更低的ESR和ESL，也可减少线路上的阻抗变化。</font>**

**<font style="color:#ff0000;">10. TYPEC座子所有信号都必须增加ESD器件，布局时靠近USB连接器放置。对于SSTXP/N，SSRXP/N信号，ESD寄生电容不得超过0.3pF。</font>**

**<font style="color:#ff0000;">11. USB 2.0控制差分阻抗90ohm±10%，差分对内最大时延＜10mil；</font>**

**<font style="color:#ff0000;">12. USB 3.0控制差分阻抗90ohm±10%，差分对内最大时延＜3mil；</font>**

### 3.5.16  SATA3.1接口
RK3576芯片拥有2个SATA3.1 控制器，和PCIe以及USB3_OTG1控制器复用Comb PHY0/1，具体路径请见下图。

·支持SATA PM功能，每个port可以支持5个设备；

·支持SATA 1.5Gb/s，SATA 3.0Gb/s，SATA 6.0Gb/s speeds ；

·支持eSATA。

![Image](./images/OK3576C_hardware/78d253915ff345faadcd8998e3113de1.png)

SATA0 控制器使用 Comb PHY0（与 PCIe0 Controller 控制器复用）。

![Image](./images/OK3576C_hardware/e663e6eea91844d4b0aac2ca9bb67198.png)

SATA1 控制器使用 Comb PHY1（与 PCIe1 Controller 控制器以及 USB3_OTG1 控制器复用）。

![Image](./images/OK3576C_hardware/bc643117b9814cfba5ec047f5e5d00c4.png)

SATA0/1控制器相关控制IO有： 

·SATA0_ACTLED：SATA0接口有数据传输时LED闪烁控制输出； 

·SATA1_ACTLED：SATA1 接口有数据传输时LED闪烁控制输出； 

·SATA_CPDET：SATA热拔插设备的插拔检测输入； 

·SATA_MPSWIT：SATA热拔插设备的开关检测输入； 

·SATA_CPPOD：SATA 控制热拔插设备电源开关输出； 

·其中SATA_CPDET、SATA_MPSWIT、SATA_CPPOD是SATA0/1共用接口，可通过寄存器配置是SATA0还是SATA1 

·其中SATA0_ACTLED、SATA1_ACTLED复用到两个位置，一个在VCCIO6电源域，一个在VCCIO4电源域。

**<font style="color:#ff0000;">注意：</font>**

1. **<font style="color:#ff0000;">Slot设计时，外围电路及电源需要满足Spec要求；</font>**
2. **<font style="color:#ff0000;">一个SATA接口外接SATA PM时，最多只能支持5个Port，不支持多个SATA PM超过6 个Port以上；</font>**
3. **<font style="color:#ff0000;">SATA接口的TXP/N，RXP/N 差分信号上串接的10nF交流耦合电容，AC耦合电容建议使用0201封装，更低的ESR和ESL，也可减少线路上的阻抗变化；</font>**
4. **<font style="color:#ff0000;">eSATA接口座子所有信号都必须增加ESD器件，布局时靠近座子放置，ESD寄生电容不得超过0.4pF；</font>**

### 3.5.17  PCIE2.1电路
RK3576拥有2个PCIe2.1控制器，两个都只支持RC模式(RC是Root Complex缩写)，不支持EP，如下：

1. Controller 0(1Lane)，PCIe0 Controller x1 Lane(Only RC)
2. Controller 1(1Lane)，PCIe1 Controller x1 Lane(Only RC)

2个PCIe2.1控制器与SATA3.1/USB3.2_Gen1x1组成两个Combo PHY，一个是 PCIe2.1/SATA3.1

Combo PHY0、另一个是 PCIe2.1/SATA3.1/USB3.2_Gen1x1 Combo PHY1。

Controller和PHY之间的映射关系图如下：

![Image](./images/OK3576C_hardware/9a41442f01a04562bff971b57d527988.png)

PCIe0 控制器(RC)与 SATA0 控制器复用 PCIe2.1/SATA3.1 Combo PHY0；封装管脚如下图：

![Image](./images/OK3576C_hardware/911020bcf7d8463c9304cd9fd29d3c50.png)

PCIe1 控制器(RC)、SATA1 控制器、USB3 OTG1 控制器复用 PCIe2.1/SATA3.1/USB3.2_Gen1x1 

Combo PHY1；封装管脚如下图：

![Image](./images/OK3576C_hardware/5d4d4b0f091e488f9928f8bdc1483b8d.png)

PCIE0/1_REFCLKP/N 可支持输出也可支持输入，默认输出提供给 EP 设备，如下示意图：

![Image](./images/OK3576C_hardware/4d3bd48a066446d6980dfa970165b429.png)

PCIE0/1_REFCLKP/N 若做输入时，示意图如下：

![Image](./images/OK3576C_hardware/3cc4b6a541964b1490dc0f8f1acf2ead.png)

OK3576-C开发板中有一个PCIe0通道连接PCIe x1插槽支持PCIe2.0×1Lane模式。

支持PCle Gen1（2.4 GT/s）协议，另一路PCIe1复用为USB3.0功能。

PCIe0 PCIe2.0×1Lane 部分电路如下图所示：

![Image](./images/OK3576C_hardware/e6e4b7374d274b688db775782f9e0379.png)

上图为PCIE接口的12V供电控制电路。

![Image](./images/OK3576C_hardware/df64e8e1d83a4719a46896aefc92538b.png)

上图为PCIE接口3.3V供电与使能控制电路，U42是5V转3.3V降压芯片。

![Image](./images/OK3576C_hardware/9a474f67a8194c7cb32bd96a6dc70390.png)

上图是PCIEX1插槽电路设计。

**<font style="color:#ff0000;">PCIe2.1设计中请注意：</font>**

1. **<font style="color:#ff0000;">Slot设计时，外围电路及电源需要满足Spec要求；</font>**
2. **<font style="color:#ff0000;">PCIe2.1接口的TXP/N差分信号上串接的100nF交流耦合电容，AC耦合电容建议使用0201封装，更低的ESR和ESL，也可减少线路上的阻抗变化；</font>**
3. **<font style="color:#ff0000;">PCIE0/1_CLKREQN必须使用功能脚，不能用GPIO替代；</font>**
4. **<font style="color:#ff0000;">PCIE0/1_PERSTN/WAKEN/PRSNT 在 RK3576 上面不指定特定的 IO，直接使用电平匹配的 GPIO</font>**

**<font style="color:#ff0000;">口来做控制功能脚就可以；</font>**

1. **<font style="color:#ff0000;">标准的PCIe Slot：PCIEx_CLKREQN，PCIEx_WAKEN，PCIEx_PERSTN为3.3V电平；需要注意做好 RK3576 端的电平匹配；</font>**
2. **<font style="color:#ff0000;">使用 PCIe 功能的时候，复用的 SATA/USB 功能无法使用，SATA/USB 对应的功能详见其模块说明；</font>**
3. **<font style="color:#ff0000;">PCIe2.1 功能模块没有使用时，数据线 PCIE0/1_TXP/TXN、PCIE0/1_RXP/RXN 和参考时钟线PCIE0/1_REFCLKP/ REFCLKN 悬空即可；AVDD0V85 和 AVDD1V8 两路电源接地处理，注意软件对应的dts 配置需要 disable；</font>**
4. **<font style="color:#ff0000;">PCIe2.1接口匹配设计推荐如下表所示：</font>**

| **信号** | **连接方式** | **说明** |
| --- | --- | --- |
| **<font style="color:rgb(255, 0, 0);">PCIE0/1_TXP/TXN</font>** | **<font style="color:rgb(255, 0, 0);">串接100nF电容（建议0201封装）</font>** | **<font style="color:rgb(255, 0, 0);">PCIe数据输出</font>** |
| **<font style="color:rgb(255, 0, 0);">PCIE0/1_RXP/RXN</font>** | **<font style="color:rgb(255, 0, 0);">直连</font>** | **<font style="color:rgb(255, 0, 0);">PCIe数据输入</font>** |
| **<font style="color:rgb(255, 0, 0);">PCIE0/1_REFCLKP/CLKN</font>** | **<font style="color:rgb(255, 0, 0);">直连</font>** | **<font style="color:rgb(255, 0, 0);">PCIe参考时钟</font>** |
| **<font style="color:rgb(255, 0, 0);">PCIE0/1_CLKREQN</font>** | **<font style="color:rgb(255, 0, 0);">串接 0ohm 电阻</font>** | **<font style="color:rgb(255, 0, 0);">PCIe 参考时钟请求输入(RC 模式)</font>** |
| **<font style="color:rgb(255, 0, 0);">PCIE0/1_WAKEN(RK3576无该信号，用GPIO代替)</font>** | **<font style="color:rgb(255, 0, 0);">串接0ohm电阻</font>** | **<font style="color:rgb(255, 0, 0);">PCIe 唤醒输入(RC 模式)</font>** |
| **<font style="color:rgb(255, 0, 0);">PCIE0/1_PERSTN(RK3576无该信号，用GPIO代替)</font>** | **<font style="color:rgb(255, 0, 0);">串接0ohm电阻</font>** | **<font style="color:rgb(255, 0, 0);">PCIe 全局复位输出(RC 模式)</font>** |
| **<font style="color:rgb(255, 0, 0);">PCIE0/1_PRSNT(RK3576无该信号，用GPIO代替)</font>** | **<font style="color:rgb(255, 0, 0);">串接0ohm电阻</font>** | **<font style="color:rgb(255, 0, 0);">Add In Card 插入检测输入(RC 模式)</font>** |
| **<font style="color:rgb(255, 0, 0);">PCIE_BUTTONRSTN(暂时没用到)</font>** | **<font style="color:rgb(255, 0, 0);">没用，无需连接</font>** | **<font style="color:rgb(255, 0, 0);">外部物理复位PCIe Controller</font>** |


**<font style="color:#ff0000;">10.  数据走线阻抗控制差分85ohm±10%；</font>**

**<font style="color:#ff0000;">11.  时钟走线阻抗控制差分100ohm±10%</font>**

**<font style="color:#ff0000;">12.  差分对内最大时延差＜3mil；</font>**

**<font style="color:#ff0000;">13.  差分对间间距建议大于等于4倍PCI-E线宽。</font>**

### 3.5.18  视频输入接口
FET3576有两个MIPI DPHY CSI RX接口，都支持MIPI V1.2版本，每个通道最大传输速率为 2.5Gbps。

![Image](./images/OK3576C_hardware/2786718e09bf49709dc87353e8d55952.png)

![Image](./images/OK3576C_hardware/470d2d797334437198dd79b73b3b74d3.png)

**MIPI DPHY CSI1/2 RX 接口模式支持情况**： 

1. 支持 4Lane 模式，MIPI_DPHY_CSI1_RX_D[3:0]数据参考 MIPI_DPHY_CSI1_RX_CLK 
2. 支持 2Lane+2Lane 模式：

·MIPI DPHY CSI1_RX_D[1:0]数据参考 MIPI_DPHY_CSI1_RX_CLK 

·MIPI DPHY CSI2_RX_D[1:0]数据参考 MIPI_DPHY_CSI2_RX_CLK

![Image](./images/OK3576C_hardware/79ab42f0e0894db291fa9003c8de622d.png)



**MIPI DPHY CSI3/4 RX 接口模式支持情况： **

1. 支持 4Lane 模式，MIPI_DPHY_CSI3_RX_D[3:0]数据参考 MIPI_DPHY_CSI3_RX_CLK 
2. 支持 2Lane+2Lane 模式：

·MIPI DPHY CSI3_RX_D[1:0]数据参考 MIPI_DPHY_CSI3_RX_CLK 

·MIPI DPHY CSI4_RX_D[1:0]数据参考 MIPI_DPHY_CSI4_RX_CLK

![Image](./images/OK3576C_hardware/54b658d711424beba9b9c652e4369e07.png)

**MIPI_DCPHY_CSI_RX接口情况**

FET3576有一个MIPI DCPHY CSI RX Combo PHY；DPHY支持V2.0版本，CPHY支持V1.1版本。DPHY模式有4Lane，最高传输速率4.5Gbps/Lane；CPHY模式有3Trios，最高传输速5.7Gbps/Trio。

![Image](./images/OK3576C_hardware/3330712704a843c5b8060522fbdfa347.png)

**DPHY和CPHY 配置支持情况： **

MIPI DCPHY Combo PHY的TX和RX只能支持同时配置成DPHY TX、DPHY RX模式，或同时配置成 CPHY TX、CPHY RX 模式。不支持一个配置成DPHY TX一个配置成CPHY RX，或者一个配置成CPHY TX一个配置成DPHY RX。

**MIPI DCPHY工作在DPHY模式时支持情况**：

1. 支持4Lane/2Lane/1Lane模式，MIPI_DPHY_CSI0_RX[3:0]数据参考MIPI_DPHY_CSI0_RX_CLK
2. 不支持拆分成 2Lane+2Lane

**MIPI DCPHY工作在CPHY模式时支持情况：**

1. 支持0/1/2 Trio，每个Trio有Trio_A/Trio_B/Trio_C 3根线，MIPI_CPHY_CSI_RX_TRIO[2:0]_A，MIPI_CPHY_CSI_RX_TRIO[2:0]_B，MIPI_CPHY_CSI_RX_TRIO[2:0]_C。

OK3576-C默认配置为5个Camera接口，分别是：MIPI_DPHY_CSI0_RX 4Lane、MIPI_DPHY_CSI1_RX 2Lane、MIPI_DPHY_CSI2_RX 2Lane、MIPI_DPHY_CSI3_RX 2Lane、MIPI_DPHY_CSI4_RX 2Lane。原理如下图：  
![Image](./images/OK3576C_hardware/6a92930880af491ea79c2e7e1ed539b8.png)



**MIPI RX设计需要注意：**

**1.  走线阻抗要求差分100ohm±10%；**

**2.  走线阻抗要求单端50ohn±10%；**

**3.  差分对内最大时延差＜3mil；**

**4.  时钟与数据之间等长＜6mil；**

**5.  差分对间间距建议＞4倍MIPI线宽，至少要3倍MIPI线宽；**

**6.  MIPI与其他信号间距建议＞4倍MIPI线宽，至少要3倍MIPI线宽；**

**7.  配置为CPHY时，组内（TRIO_A\TRIO_B\TRIO_C）最大时延差＜3mil；**

**8.  组间（TRIO0\TRIO1\TRIO2）等长要求＜50mil；**

### 3.5.19  视频输出接口
RK3576芯片的VOP显示输出处理器，它从系统存储器的帧缓冲器中读取视频数据和UI 数据，执行相应的处理，如裁剪、色域空间转换、缩放和叠加，并输出到每个高速显示接口。 

有三个Port 输出，可以从DP、HDMI/eDP、MIPI DSI、LCDC(Parallel Interface)视频接口输出。

最大的视频输出能力：

1. 三屏异显方案，如4096x2160@60Hz，2560x1600@60Hz，1920x1080@60Hz；
2. 双屏异显方案，如4096x2160@120Hz，2560x1600@60Hz。

VOP 和视频接口输出路径图：

![Image](./images/OK3576C_hardware/45e326a19929466e8faccd5697432fa8.png)

OK3576-C开发板支持DP/MIPI_DSI/HDMI 三种显示输出接口。

#### **3.5.19.1 MIPI_DSI接口**
FET3576有一个MIPI D-PHY/C-PHY Combo PHY TX：

D-PHY支持V2.0版本，D-PHY模式有0/1/2/3 Lane，每个Lane 2根线；最高传输速率2.5Gbps/Lane。

MIPI_DPHY_TX最大分辨率支持2560x1600@60Hz。

C-PHY支持V1.1 版本，C-PHY模式有0/1/2 Trio，每个Trio A/B/C 3根线；最高传输速率 1.7Gsps/Trio。

MIPI_CPHY_TX最大分辨率支持2560x1600@60Hz。

![Image](./images/OK3576C_hardware/cfa21d5a79d14ac9b84d9fa2af27756f.png)

**DPHY和CPHY配置支持情况**： 

MIPI D-PHY/C-PHY Combo PHY的TX和RX只能支持同时配置成DPHY TX，DPHY RX模式或同时配置成CPHY TX，CPHY RX模式，不支持一个配置成DPHY TX，一个配置成CPHY RX；

**MIPI DCPHY工作在D-PHY时模式支持情况**：

支持4Lane模式，MIPI_DPHY_TX_D[3：0]数据参考MIPI_DPHY_TX_CLK。

**MIPI DCPHY工作在C-PHY时模式支持情况： **

支持0/1/2 Trio，每个Trio A/B/C 3根线，MIPI_CPHY_TX_TRIO[2：0]_A，

MIPI_CPHY_TX_TRIO[2：0]_B， MIPI_CPHY_TX_TRIO[2：0]_C。

OK3576-C开发板的MIPI_DSI接口采用1组时钟通道+ 4组数据通道模式，原理图如下：

![Image](./images/OK3576C_hardware/1e606f22de494dd68338f94b39dd59bd.png)

![Image](./images/OK3576C_hardware/6aa529d3edf14a68a449d58cacdaa72c.png)

**设计时需注意：**

**1.  走线阻抗控制差分100ohm±10%；**

**2.  差分对内最大时延差＜3mil；**

**3.  时钟与数据之间等长＜6mil；**

**4.  差分对间间距建议大于等于4倍MIPI线宽，至少要3倍MIPI线宽；**

**5.  MIPI与其他信号间距建议大于等于4倍MIPI线宽，至少要3倍MIPI线宽；**

**6.  配置为CPHY时，单端走线阻抗控制50ohm±10%；**

**7.  组内(TRIO_A\TRIO_B\TRIO_C)最大时延差＜3mil；**

**8.  组间(TRIO0\TRIO1\TRIO2)等长要求＜50mil；**

**9.  各信号所允许过孔数量建议不超过2个；**

**10.  对间间距建议大于等于4倍MIPI线宽；**

**11.  MIPI与其它信号间距建议大于等于4倍MIPI线宽。**

#### **3.5.19.2 HDMI_TX接口**
RK3576内置一个HDMI/eDP TX Combo PHY。

HDMI/eDP TX Combo PHY支持以下两个模式：

1. HDMI TX 模式：最高支持HDMI2.1，支持HDMI FRL模式并向下兼容HDMI TMDS模式，支持RGB/YUV444/YUV422/YUV420(Up to 10bit)格式。
2. eDP TX模式：最高支持eDP1.3，最大分辨率支持4K@60Hz，支持RGB/YUV444/YUV422(Up to 10bit)格式。

![Image](./images/OK3576C_hardware/1144a00583e04e238fcc6e9556a05b60.png)

RK3576支持HDMI2.1并向下HDMI2.0，HDMI1.4兼容，由于HDMI2.1工作在FRL模式，切换到HDMI2.0及以下模式时，工作在TMDS模式，因采用AC耦合电压模式驱动器。

如下图所示，AC耦合电容容值采用220nF，不得随意更改，交流耦合电容建议使用0201封装，更低的ESR和ESL，也可减少线路上的阻抗变化。

工作在HDMI2.1模式，HDMI_TX_ON_H配置为低电平， Q15，Q16，Q17，Q18不导通。

工作在HDMI2.0及以下模式时，HDMI_TX_ON_H配置为高电平，Q15，Q16，Q17，Q18导通，对地499ohm电阻与Sink端上拉50ohm电阻形成一个直流偏置，大约3V。

**<font style="color:#ff0000;">设计时需注意：</font>**

**<font style="color:#ff0000;">1.  如果只需要支持HDMI2.0及以下模式时，Q15，Q16，Q17，Q18也不能省掉，需要保证机器在未开机时，管子不能导通，因为HDMI CTS Test ID 7-3 TMDS Voff测试项目要求在DUT未上电，Voff电压必须在AVcc+-10mV以内，否则这个测试项无法通过。</font>**

![Image](./images/OK3576C_hardware/de99283558814d00ab5dfc8bedcac83a.png)

FRL模式：在传统的TMDS 架构下，是利用一个独立的通道来传送Clock，但在FRL的架构中，将Clock嵌入在Data的通道中，在Sink端透过Clock Recovery解析出Clock。

下表为FRL速率与通道关系：

| 通道速率 | 通道数 |
| :---: | :---: |
| 3Gbps | 3 |
| 6Gbps | 3 |
| 6Gbps | 4 |
| 8Gbps | 4 |
| 10Gbps | 4 |
| 12Gbps | 4 |


支持ARC/eARC通过HDMI_TX_SBD_P/ HDMI_TX_SBD_N信号到RK3576内部解析出音频数据。

![Image](./images/OK3576C_hardware/b7f2bdbd166f4798b7849a17203dd130.png)

HDMI_TX_HPD是HDMI TX控制器复用到普通GPIO上，电平随所在电源域电压，电源域供电电压有更改，外围电路的上拉电阻电源也必须同步调整。

HDMI_TX_CEC是HDMI控制器CEC功能复用到普通GPIO上功能，电平随所在电源域电压，电源域供电电压有更改，外围电路的上拉电阻电源也必须同步调整。

CEC协议规定是3.3V电平，但是协议要求，往CEC管脚通过27K电阻加3.3V电压，漏电不允许超过1.8uA。

![Image](./images/OK3576C_hardware/370ec6fa918a47e78d07ce829b7d9407.png)

RK3576 IO Domain在未上电时，如果IO上有电压，IO会存在漏电，比如RK3576已经断电了，然后HDMI线还连接着Sink端（电视或显示器），此时Sink端的CEC有电，会通过HDMI线漏电到RK3576 IO上，会造成CEC漏电超过1.8uA，因此外部需要增加一个隔离电路，R189阻值不得随意修改，需要使用27Kohm，Q19默认选择2SK3018，如果要换其它型号，结电容必须相当，如果用结电容过大，不仅会影响工作，认证也会过不了。

![Image](./images/OK3576C_hardware/38f259c4222040d88a1fee40277c22ba.png)

HDMI_TX _SCL/ HDMI_TX _SDA是HDMI TX控制器的I2C/DDC总线，功能复用到普通GPIO上，电平随所在电源域电压，电源域供电电压有更改，外围电路的上拉电阻电源也必须同步调整。

DDC_SCL/DDC_SDA协议规定是5V电平，RK3576 IO不支持5V电平，必须增加电平转换电路，不得删减，默认使用MOS管电平转换，MOS型号默认选择2SK3018，如果要换其它型号，结电容必须相当，如果用结电容过大，不仅影响工作，认证也会过不了。

上拉电阻建议参考照默认值，不要随意修改。

D6二极管不得删减，用来防止Sink端漏电到VCC_5V0。

SDA信号电平转换的MOS栅极和电源之间串拉1K，MOS栅极和源极之间并一个100pF改善时序，不得删除。

![Image](./images/OK3576C_hardware/d419ab16f2ea4ce5b17d249c05787ea7.png)

HDMI座子的Pin18电压需保证在4.8-5.3V之间，管脚需放置1uF去耦电容，不得删减，布局时，靠近HDMI座子管脚放置。

为加强抗静电能力，信号上必须预留ESD器件，HDMI2.1信号的ESD寄生电容不得超过0.2pF，

其它信号的ESD寄生电容建议使用不超过1pF。

**设计时需注意：**

**1.  控制MOS管Coss不能过大，否则会影响信号质量，建议按参考图型号或相应的Coss值。**

**2.  走线阻抗控制差分100ohm±10%；**

**3.  差分对内最大时延差＜3mil；**

**4.  差分对间等长要求＜200mil；**

**5.  差分对间间距建议大于等于7倍HDMI线宽；**

**6.  HDMI与其他信号间距建议大于等于7倍HDMI线宽；**

**7.  建议不加过孔；**

**8.  I/O对地电容不超过0.2pF。**

#### **3.5.19.3 DP_TX接口**
RK3576支持一个DP1.4 TX PHY（和USB3 OTG0 Combo），最大输出分辨率可达4K@YUV422-120Hz。

·每个Lane速率可支持1.62/2.7G/5.4/8.1Gbps；

·支持1Lane或2Lane或4Lane模式；

·支持RGB/YUV444/YUV422/YUV420 (up to 10bit)格式；

·支持Multi Stream Transport(MST)。

![Image](./images/OK3576C_hardware/a3bc3a45f2c940249350e0a0e32aaf13.png)

·支持Swap on和Swap off两种模式

![Image](./images/OK3576C_hardware/be61200b5c45485e83fc3c3a92e83cb3.png)

·支持3 Channels的MST(Multi-Stream Transport)显示。MST支持三屏异显最大能力为：4096x2160@60Hz、2560x1600@60Hz、1920x1080@60Hz。

![Image](./images/OK3576C_hardware/9dab7aad23074119827c052673fd9e9b.png)

与USB引脚复用关系请查看3.5.15章节。

**设计DP时需要注意：**

**1.  DP0_TX_D0P/DON、DP0_TX_D1P/D1N、DP0_TX_D2P/D2N、DP0_TX_D3P/D3N、**

**DP1_TX_D0P/DON、DP1_TX_D1P/D1N、DP1_TX_D2P/D2N、DP1_TX_D3P/D3N需要串接的100nF交流耦合电容，交流耦合电容建议使用0201封装，更低的ESR和ESL，也可减少线路上的阻抗变化，布局时，靠近FET3576--C管脚放置；**

**2.  走线阻抗控制差分100ohm±10%（只作为DP接口，无复用），差分95ohm±10%（USB3.0/DP1.4复用）；**

**3.  差分对内时延差＜3mil；**

**4.  差分对间等长要求＜500mil；**

**5.  差分对间间距建议大于等于6倍DP线宽；**

**6.  DP与其它信号间距建议大于等于6倍DP线宽；**

**7.  各信号所允许过孔数量建议不超过2个；**

**8.  I/O对地电容不超过0.2pF**

### 3.5.20  WIFI/BT模块电路
OK3576-C板载一颗海华AW-CM358SM WIFI&BT模块，支持WIFI 2.4G/5G/蓝牙5.0；WIFI/BT天线使用SMA接口引出，SDIO、PDM、UART接口与主控连接。  

注意 ，在低功耗应用场景下，若要实现RK3576休眠再唤醒这个过程中，WIFI模块不重新连接网络，则需要WIFI模块的3.3V与1.8V电源使用输入的12V电源单独供电；可参考OK3576-C这部分设计。  

原理图如下：  
![Image](./images/OK3576C_hardware/3f3a60dbfcf34af8a131e21d92debcda.png)  
![Image](./images/OK3576C_hardware/2e9eb95f3cb041e5b25ff9bfeafadf8e.png)

**注意：**

**1、WIFI模块供电电源需要受控，参考底板电路；**

**2、SDIO阻抗要求： 单端50ohm，信号等长控制50mil；**



# 04_硬件设计指南

1. **I2C要求**

一组I2C总线上可以挂载多个从设备，请保证地址无冲突；

I2C总线上需要加上拉电阻，但不要使用多个电阻上拉；

请注意核心板端的I2C和从设备的I2C做电平匹配。

2. **USB设计**

为满足USB眼图要求，USB3.0 TX/RX的PCB线长不应该超过6 inches。

3. **核心板不使用的信号引脚可以悬空，但请务必将所有的GND连接。**
4. **上电时序**

强烈建议用户设计底板时参考开发板设计，使用核心板输出的CARRIER_BOARD_EN作为底板上电的使能，严格控制上电时序。否则可能会造成以下影响：

·通电阶段电流过大；

·设备无法启动；

·最坏情况，对处理器造成不可逆转的损坏。

**注意：详细硬件设计资料请阅读《FET3576-C_硬件设计指南》文档。**



# 05_连接器尺寸图

核心板连接器尺寸规格如下：

A=21.52mm、B=19.6mm、C=3.2mm、Contacts=100

![Image](./images/OK3576C_hardware/2f3a8c1f8bbd47bf94dcb40e4caf90ca.png)



对应底板连接器尺寸规格如下：

A=22.6mm、B=19.6mm、C=3.2mm、D=1.45mm、Contacts=100

![Image](./images/OK3576C_hardware/450a473a6dd040f8b83fba358030292f.png)



# 06_OK3576-C开发板整机功耗表

表1 Linux系统下整机功耗表

| 编号 | 测试项目 | 核心板功率(W) | 开发板功率(含核心板)(W) |
| --- | --- | --- | --- |
| <font style="color:black;">1</font> | <font style="color:black;">无负载启动峰值功率</font> | <font style="color:black;">3.66</font> | <font style="color:black;">5.88</font> |
| <font style="color:black;">2</font> | <font style="color:black;">无负载待机功率</font> | <font style="color:black;">0.82</font> | <font style="color:black;">2.33</font> |
| <font style="color:black;">3</font> | <font style="color:black;">CPU+GPU+内存+eMMC压力测试</font> | <font style="color:black;">5.87</font> | <font style="color:black;">7.39</font> |
| <font style="color:black;">4</font> | <font style="color:black;">7寸液晶屏+4G+U盘+视频解码</font> | <font style="color:black;">2.02</font> | <font style="color:black;">10.02</font> |
| <font style="color:black;">5</font> | <font style="color:black;">7寸液晶屏+4G+U盘+视频编码</font> | <font style="color:black;">3.06</font> | <font style="color:black;">10.48</font> |
| <font style="color:black;">6</font> | <font style="color:black;">Pwron Key 长按关机</font> | <font style="color:black;">0.28</font> | <font style="color:black;">0.32</font> |
| <font style="color:black;">7</font> | <font style="color:black;">Pwron Key 短按休眠</font> | <font style="color:black;">TBD</font> | <font style="color:black;">TBD</font> |


**注：**

1. <font style="color:black;"测试条件：核心板配置是4GB内存+32GB eMMC，4G模组移远EM05-CE，屏幕是飞凌选配产品。核心板是12V供电，底板是12V供电。   
2. 峰值功率:启动过程中的电流峰值乘以供电电压   
3. 待机功率:启动后停留在开机界面时的电流值乘以供电电压。   
4. 功耗仅供参考



# 07_最小系统原理图

![Image](./images/OK3576C_hardware/6cd409726e144fb787e6c8ce3ea7d662.png)![Image](./images/OK3576C_hardware/87b7a821411b4fa68699c630c51f72ab.png)![Image](./images/OK3576C_hardware/2a09a9be398d4ed4900833577d403111.png)![Image](./images/OK3576C_hardware/74ef1fc3a58b41da9d7b5410cc0ba9eb.png)![Image](./images/OK3576C_hardware/59e667504742475a987c1ecb9645a0fa.png)![Image](./images/OK3576C_hardware/faf4ae7240a443c08ecbbe7972823b48.png)![Image](./images/OK3576C_hardware/a1fb6b325f1144619524611092751a89.png)![Image](./images/OK3576C_hardware/20ba5d44ba4540129c00cc6e288fb336.png)![Image](./images/OK3576C_hardware/98cbfc4135b14bd6b37bb69a9f03be6e.png)![Image](./images/OK3576C_hardware/5474d0bae918457a860347cae5ec8c60.png)![Image](./images/OK3576C_hardware/be59f1df5d2647459ca8d20bd1810bf9.png)![Image](./images/OK3576C_hardware/2a8b6938e6da47078ec83d13fd5550ae.png)![Image](./images/OK3576C_hardware/cc2a8ca796934c5891f6c6ae3ba5b628.png)![Image](./images/OK3576C_hardware/2b791e9781c14564a31ee136a9fa58da.png)![Image](./images/OK3576C_hardware/541ed216c5f54e96b85ddbedc4714863.png)![Image](./images/OK3576C_hardware/49db14b25ace48eda80bfeee12eb666b.png)![Image](./images/OK3576C_hardware/938c01c0b986443198d78efab07cf602.png)![Image](./images/OK3576C_hardware/41cde6252184463fba3d48247cf83ec2.png)![Image](./images/OK3576C_hardware/c5f5374600e54690a88f51fa87e83292.png)![Image](./images/OK3576C_hardware/48011e4355b845f283eec61b54f07f67.png)

上图仅为示意图，具体连接情况请见源文件原理图。为满足核心板的正常工作，最小系统包括核心板供电电源，系统烧写电路，以及调试串口电路。



