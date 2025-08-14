# <font style="color:rgb(38, 38, 38);">免责声明</font>
<font style="color:rgb(38, 38, 38);">本手册版权归保定飞凌嵌入式技术有限公司所有。未经本公司的书面许可，任何单位和个人无权以任何形式复制、传播、转载本手册的任何部分，违者将被追究法律责任。 </font>

<font style="color:rgb(38, 38, 38);">保定飞凌嵌入式有限公司所提供的所有服务内容旨在协助用户加速产品的研发进度，在服务过程中所提供的任何程序、文档、测试结果、方案、支持等资料和信息，都仅供参考，用户有权不使用或自行参考修改，本公司不提供任何的完整性、可靠性等保证，若在用户使用过程中因任何原因造成的特别的、偶然的或间接的损失，本公司不承担任何责任。</font>

# **适用范围**
本文主要适用于飞凌LS1046平台Ubuntu18.04系统，其他平台也可以参考，但是不同平台之间会存在差异，需要客户自行修改以适应自己的使用。

# **<font style="color:rgb(0,0,0);">更新记录</font>**
| **日期** | **手册版本** | **更新内容** |
| --- | --- | --- |
| 20220511 | V1.0 | 初版 |


# 1.修改Serdes配置方案
客户在使用LS1046实际开发过程中需要用到不同的SerDes配置方案，本文主要讲述软件上的修改。

由于LS104x系列开发板引入了【复位控制字】Reset configuration word (RCW)的配置方法，通过这种配置方法客户可以方便的进行引脚的功能定义，也就是实现引脚的PinMUX功能。

LS104x平台所特有的SerDes Module也是要通过RCW来进行配置，从而将不同的SerDes通道选择为不同的功能。以LS1046A为例，可配置的两路SerDes有：

![](https://cdn.nlark.com/yuque/0/2024/png/43856062/1721975449529-ed2ec306-a89e-414f-885b-54f6e3cb0f00.png)

![](https://cdn.nlark.com/yuque/0/2024/png/43856062/1721975410147-9f322c8f-c0b7-4e01-91e5-933c00d44fbd.png)

但是这个被称为RCW的配置方法还有很多客户还不是很了解，所以本文以一个LS1046A的实际需求为例，来详细说明一下修改的过程以供客户后续定制参考。

飞凌的OK1046A-C开发板提供了两种SerDes配置方案，分别为：1040_5559和1133_5559，与上表功能对应可以看到这两种SerDes的功能分别为：

1040_5559：

![](https://cdn.nlark.com/yuque/0/2024/png/43856062/1721975533908-74841a28-9af7-46cd-b37b-dccc04a84f5d.png)

<font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">可以看到，有一个</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">XFI for MAC 9</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">，一个</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">QSGMII for MAC6</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">，</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">MAC5</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">，</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">MAC10</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">，</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">MAC1</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">，另外有三个</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">PCIe x1</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">接口。</font>

1133_5559：

![](https://cdn.nlark.com/yuque/0/2024/png/43856062/1721975596632-96a31e09-0af0-44d5-9f17-314d686f4c7c.png)

可以看到，有一个XFI for MAC 9，一个XFI for MAC10，一个SGMII for MAC5，一个SGMII for MAC6，另外有三个PCIe x1接口。

这时，如果我们有一个项目需求，需要5个网口：其中一个是核心板自带的RGMII网口，另外要SerDes引出的四个SGMII网口，这时我们发现上面飞凌提供的两种SerDes配置都不满足我们的要求，然后经过查阅SerDes配置表，发现1333_5a59可以满足我们的要求：

![](https://cdn.nlark.com/yuque/0/2024/png/43856062/1721975646431-b9af15a9-e581-4ab5-972f-92414ae3c442.png)

<font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">那么接下来我们就以此为例进行配置的修改</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">。</font>

<font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">我们先整理一下我们的项目中</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">PHY</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">与</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">MAC</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">的对应关系：</font>

![](https://cdn.nlark.com/yuque/0/2024/png/43856062/1721975678982-0734fd2f-9f91-420a-b1b1-29faa41b2a61.png)

首先我们需要知道，飞凌的OK1046A-C的两种RCW的文件在源码中的位置为：

flexbuild/packages/firmware/rcw/ls1046ardb/FORLINX/rcw_1800_qspiboot_1040_5559.rcw

flexbuild/packages/firmware/rcw/ls1046ardb/FORLINX/rcw_1800_qspiboot_1133_5559.rcw

我们为了开发便利，在rcw_1800_qspiboot_1133_5559.rcw的基础上进行修改。

## **<font style="color:rgb(0,0,0);">1.</font>****<font style="color:rgb(0,0,0);">1 </font>****<font style="color:rgb(0,0,0);">修改</font>****<font style="color:rgb(0,0,0);">RCW</font>****<font style="color:rgb(0,0,0);">配置</font>**
首先修改RCW配置为1333_5a59，分别修改SRDS_PRTCL_S1和SRDS_PRTCL_S2的值，此处要将16进制转化为10进制换算，如0x1333的十进制为4915，0x5a59的十进制为23129。

```plain
---a/flexbuild/packages/firmware/rcw/ls1046ardb/FORLINX/rcw_1800_qspiboot_1133_5559.rcw
+++b/flexbuild/packages/firmware/rcw/ls1046ardb/FORLINX/rcw_1800_qspiboot_1133_5559.rcw
@@ -69,8 +69,8 @@ SYS_PLL_RAT=7
MEM_PLL_RAT=21
CGA_PLL1_RAT=18
CGA_PLL2_RAT=16
-SRDS_PRTCL_S1=4403
-SRDS_PRTCL_S2=21849
+SRDS_PRTCL_S1=4915
+SRDS_PRTCL_S2=23129
SRDS_PLL_REF_CLK_SEL_S1=1
SRDS_PLL_REF_CLK_SEL_S2=0
SRDS_DIV_PEX_S1=1
@@ -88,7 +88,7 @@ SPI_EXT=1
SPI_BASE=2
```

## **<font style="color:rgb(0,0,0);">1.2</font>****<font style="color:rgb(0,0,0);"> </font>****<font style="color:rgb(0,0,0);">修改</font>****<font style="color:rgb(0,0,0);">uboot</font>****<font style="color:rgb(0,0,0);">配置</font>**
先在头文件中添加我们所需的PHY地址的定义，该文件在源码中的位置为：

flexbuild/packages/firmware/u-boot/include/configs/ls1046ardb.h

```plain
--- a/include/configs/ls1046ardb.h
+++ b/include/configs/ls1046ardb.h
@@ -179,7 +179,10 @@
#define RGMII_PHY1_ADDR                        0x1
#define RGMII_PHY2_ADDR                        0x2

-#define SGMII_PHY2_ADDR                        0x3
+#define SGMII_PHY1_ADDR                        0x2
+#define SGMII_PHY2_ADDR                        0x5
+#define SGMII_PHY3_ADDR                        0x3
+#define SGMII_PHY4_ADDR                        0x4

#define QSGMII_PORT1_PHY_ADDR          8
#define QSGMII_PORT2_PHY_ADDR          9
```

Uboot的网络初始化代码在源码中的位置为：

flexbuild/packages/firmware/u-boot/board/freescale/ls1046ardb/eth.c

此时我们要修改网络部分的配置

```plain
--- a/board/freescale/ls1046ardb/eth.c
+++ b/board/freescale/ls1046ardb/eth.c
@@ -35,28 +35,33 @@ int board_eth_init(bd_t *bis)
/* Register the 1G MDIO bus */
fm_memac_mdio_init(bis, &dtsec_mdio_info);


+       /*
+       //注释掉对原底板上万兆网的MDIO总线的定义
        tgec_mdio_info.regs =
                (struct memac_mdio_controller *)CONFIG_SYS_FM1_TGEC_MDIO_ADDR;
        tgec_mdio_info.name = DEFAULT_FM_TGEC_MDIO_NAME;
+       */


/* Register the 10G MDIO bus */
-       fm_memac_mdio_init(bis, &tgec_mdio_info);
+       //注释掉对原底板上万兆网的MDIO总线的初始化
+       /*fm_memac_mdio_init(bis, &tgec_mdio_info);*/


/* Set the two on-board RGMII PHY address */
        fm_info_set_phy_address(FM1_DTSEC3, RGMII_PHY1_ADDR);
-       fm_info_set_phy_address(FM1_DTSEC4, RGMII_PHY2_ADDR);
+       //注释掉对原底板上MAC4的RGMII网口的MAC与PHY的绑定
+       //fm_info_set_phy_address(FM1_DTSEC4, RGMII_PHY2_ADDR);


/* Set the on-board AQ PHY address */
-       fm_info_set_phy_address(FM1_10GEC1, FM1_10GEC1_PHY_ADDR);
+       //注释掉对原底板上万兆网口的MAC与PHY的绑定
+       //fm_info_set_phy_address(FM1_10GEC1, FM1_10GEC1_PHY_ADDR);


        switch (srds_s1) {
+       //修改SerDes的SGMII网络相关配置
-       case 0x1133:
+       case 0x1333:
        /* Set the two on-board SGMII PHY address */
        //fm_info_set_phy_address(FM1_DTSEC5, SGMII_PHY1_ADDR);
        //关闭MAC5的使能，绑定MAC6与其关联的PHY地址
-               fm_disable_port(FM1_DTSEC5);
-               fm_info_set_phy_address(FM1_DTSEC6, SGMII_PHY2_ADDR);
-               run_command("setenv serdes1 1133", 0);
+               fm_disable_port(FM1_DTSEC4);
+               //绑定MAC10，MAC5，MAC6，MAC2与其关联的PHY地址
+               fm_info_set_phy_address(FM1_DTSEC10, SGMII_PHY1_ADDR);
+               fm_info_set_phy_address(FM1_DTSEC5, SGMII_PHY2_ADDR);
+               fm_info_set_phy_address(FM1_DTSEC6, SGMII_PHY3_ADDR);
+               fm_info_set_phy_address(FM1_DTSEC2, SGMII_PHY4_ADDR);
+               //设置环境变量serdes1为1333
+               run_command("setenv serdes1 1333", 0);
                break;
        case 0x1040:
                /* QSGMII on lane B, MAC 6/5/10/1 */
@@ -81,9 +86,11 @@ int board_eth_init(bd_t *bis)
                fm_info_set_mdio(i, dev);
        /* XFI on lane A, MAC 9 */
+       /*
+       //注释掉对原底板上万兆网的MDIO总线上对挂载的MAC的注册
        dev = miiphy_get_dev_by_name(DEFAULT_FM_TGEC_MDIO_NAME);
        fm_info_set_mdio(FM1_10GEC1, dev);
-
+       */
        cpu_eth_init(bis);
#endif
```

修改完此部分后则Uboot部分对网络配置的代码修改完成。

## **<font style="color:rgb(0,0,0);">1.3</font>****<font style="color:rgb(0,0,0);"> </font>****<font style="color:rgb(0,0,0);">修改设备树</font>**
**注意：客户在参照修改时应以实际的设备树路径为准。**

首先我们需要知道，飞凌的OK1046A-C的两种RCW配置所对应的设备树文件在源码中的位置为：

flexbuild/packages/linux/linux/arch/arm64/boot/dts/freescale/fsl-ls1046a-rdb-sdk-1040-5559.dts

flexbuild/packages/linux/linux/arch/arm64/boot/dts/freescale/fsl-ls1046a-rdb-sdk-1133-5559.dts

设备树部分我们也可以基于fsl-ls1046a-rdb-sdk-1133-5559.dts进行修改，首先需要修改设备树的Makefile，增加对我们需要的DTS文件的编译。

```plain
--- a/arch/arm64/boot/dts/freescale/Makefile
+++ b/arch/arm64/boot/dts/freescale/Makefile
@@ -14,6 +14,7 @@ dtb-$(CONFIG_ARCH_LAYERSCAPE) += fsl-ls1046a-qds-sdk.dtb
dtb-$(CONFIG_ARCH_LAYERSCAPE) += fsl-ls1046a-rdb.dtb
dtb-$(CONFIG_ARCH_LAYERSCAPE) += fsl-ls1046a-rdb-sdk.dtb
dtb-$(CONFIG_ARCH_LAYERSCAPE) += fsl-ls1046a-rdb-sdk-1133-5559.dtb
+dtb-$(CONFIG_ARCH_LAYERSCAPE) += fsl-ls1046a-rdb-sdk-1333-5a59.dtb
dtb-$(CONFIG_ARCH_LAYERSCAPE) += fsl-ls1046a-rdb-sdk-1040-5559.dtb
dtb-$(CONFIG_ARCH_LAYERSCAPE) += fsl-ls1046a-rdb-usdpaa-1133-5559.dtb
dtb-$(CONFIG_ARCH_LAYERSCAPE) += fsl-ls1046a-rdb-usdpaa-1040-5559.dtb
```

其次我们将dts文件进行复制和重命名，执行命令

```plain
cp flexbuild/packages/linux/linux/arch/arm64/boot/dts/freescale/fsl-ls1046a-rdb-sdk-1133-5559.dts 
   flexbuild/packages/linux/linux/arch/arm64/boot/dts/freescale/fsl-ls1046a-rdb-sdk-1333-5a59.dts
```

接下来我们修改fsl-ls1046a-rdb-sdk-1333-5a59.dts文件

```plain
--- arch/arm64/boot/dts/freescale/fsl-ls1046a-rdb-sdk-1333-5a59.dts
+++ arch/arm64/boot/dts/freescale/fsl-ls1046a-rdb-sdk-1333-5a59.dts
@@ -54,8 +54,9 @@
        };
        
+       /* 启用MAC2，并将其注册为接口是sgmii，同时PHY地址为sgmii_phy4，即4 */
        ethernet@e2000 {
-               status = "disabled";
-       };
+               phy-handle = <&sgmii_phy4>;
+               phy-connection-type = "sgmii";
+       };


        ethernet@e4000 {
                phy-handle = <&rgmii_phy1>;
@@ -63,27 +64,26 @@
        };

        
+       /* 禁用MAC4 */
        ethernet@e6000 {
-               phy-handle = <&rgmii_phy2>;
-               phy-connection-type = "rgmii-txid";
+               status = "disabled";
        };

        
+       /* 启用MAC5，并将其注册为接口是sgmii，同时PHY地址为sgmii_phy2，即5 */
         ethernet@e8000 {
-               status = "disabled";
-       };
+               phy-handle = <&sgmii_phy2>;
+               phy-connection-type = "sgmii";
+        };


+       /* 启用MAC6，并将其注册为接口是sgmii，同时PHY地址为sgmii_phy3，即3 */
        ethernet@ea000 {
-               phy-handle = <&sgmii_phy2>;
+               phy-handle = <&sgmii_phy3>;
                phy-connection-type = "sgmii";
        };

        
+       /* 禁用MAC9，即禁用底板万兆网接口 */
-       ethernet@f0000 { /* 10GEC1 */
-               phy-handle = <&aqr105_phy>;
-               phy-connection-type = "xgmii";
+       ethernet@f0000 {
+               status = "disabled";
        };

        
+       /* 启用MAC10，并将其注册为接口是sgmii，同时PHY地址为sgmii_phy1，即2 */
-       ethernet@f2000 { /* 10GEC2 */
-               fixed-link = <0 1 1000 0 0>;
-               phy-connection-type = "xgmii";
+       ethernet@f2000 {
+               phy-handle = <&sgmii_phy1>;
+               phy-connection-type = "sgmii";
        };

        
        mdio@fc000 {
@@ -91,20 +91,21 @@
                     reg = <0x1>;
        };

        
+               /* 修改PHY地址 */
-               rgmii_phy2: ethernet-phy@2 {
-                       reg = <0x2>;
-               };
+               sgmii_phy1: ethernet-phy@2 {
+                        reg = <0x2>;
+               };

-               sgmii_phy2: ethernet-phy@3 {
-                       reg = <0x3>;
+               sgmii_phy2: ethernet-phy@5 {
+                       reg = <0x5>;
+
+               sgmii_phy3: ethernet-phy@3 {
+                        reg = <0x3>;
+                };
+
+               sgmii_phy4: ethernet-phy@4 {
+                        reg = <0x4>;
+                };
         };

         
+       /* 禁用万兆网的MDIO */
-       mdio@fd000 {
-               aqr105_phy: ethernet-phy@0 {
-                       compatible = "ethernet-phy-ieee802.3-c45";
-                       reg = <0x0>;
-               };
         };
};


@@ -130,13 +131,15 @@
        ethernet@0 {
                status = "disabled";
        };
+       /*修改dpaa的配置，禁用掉MAC1，MAC4，MAC9，启用MAC2，MAC3，MAC5，MAC6，MAC10*/
-       ethernet@1 {
+       ethernet@3 {
                status = "disabled";
        };
-       ethernet@4 {
-               status = "disabled";
-       };
-
+       ethernet@8 {
+               status = "disabled";
+        };
        ethernet@9 {
                compatible = "fsl,dpa-ethernet";
                fsl,fman-mac = <&enet7>;
```

至此，设备树部分代码修改完成。

修改完成的设备树完整源码如下：

```plain
#include "fsl-ls1046a-rdb.dts"
#include "qoriq-qman-portals-sdk.dtsi"
#include "qoriq-bman-portals-sdk.dtsi"

&fman0 {
       ethernet@e0000 {
               status = "disabled";
       };
       
       ethernet@e2000 {
               phy-handle = <&sgmii_phy4>;
               phy-connection-type = "sgmii";
       };
       
       ethernet@e4000 {
               phy-handle = <&rgmii_phy1>;
               phy-connection-type = "rgmii-txid";
       };
       
      ethernet@e6000 {
               status = "disabled";
       };
       
      ethernet@e8000 {
               phy-handle = <&sgmii_phy2>;
               phy-connection-type = "sgmii";
       };
       
      ethernet@ea000 {
               phy-handle = <&sgmii_phy3>;
               phy-connection-type = "sgmii";
       };
       
      ethernet@f0000 {
               status = "disabled";
       };
       
      ethernet@f2000 {
               phy-handle = <&sgmii_phy1>;
               phy-connection-type = "sgmii";
       };
       
      mdio@fc000 {
               rgmii_phy1: ethernet-phy@1 {
                        reg = <0x1>;
               };
       
               sgmii_phy1: ethernet-phy@2 {
                        reg = <0x2>;
               };
       
               sgmii_phy2: ethernet-phy@5 {
                        reg = <0x5>;
               };
       
               sgmii_phy3: ethernet-phy@3 {
                        reg = <0x3>;
               };
       
                sgmii_phy4: ethernet-phy@4 {
                        reg = <0x4>;
               };
      };
};

&bman_fbpr {
       compatible = "fsl,bman-fbpr";
       alloc-ranges = <0 0 0x10000 0>;
};

&qman_fqd {
       compatible = "fsl,qman-fqd";
       alloc-ranges = <0 0 0x10000 0>;
};

&qman_pfdr {
       compatible = "fsl,qman-pfdr";
       alloc-ranges = <0 0 0x10000 0>;
};

&soc {
       #include "qoriq-dpaa-eth.dtsi"
       #include "qoriq-fman3-0-6oh.dtsi"
};

&fsldpaa {
         ethernet@0 {
                 status = "disabled";
         };
        ethernet@3 {
                 status = "disabled";
         };
        ethernet@8 {
                status = "disabled";
         };
         ethernet@9 {
                 compatible = "fsl,dpa-ethernet";
                 fsl,fman-mac = <&enet7>;
                 dma-coherent;
         };
};

&fman0 {
       compatible = "fsl,fman", "simple-bus";
};
```

## **<font style="color:rgb(0,0,0);">1.4</font>****<font style="color:rgb(0,0,0);"> </font>****<font style="color:rgb(0,0,0);">修改</font>****<font style="color:rgb(0,0,0);">flex-build</font>****<font style="color:rgb(0,0,0);">编译工具</font>**
由于我们增加了设备树文件并且修改了RCW部分关于SerDes的配置，所以flex-build编译工具在制作烧写镜像的时候会有一些问题，我们需要进行相应的修改。

这一部分主要是uboot会通过读环境变量中的serdes1参数来选择加载对应的dts设备树文件

涉及到的文件在源码中的位置为：

flexbuild/configs/board/ls1046ardb/manifest

修改内容为：

```plain
--- a/flexbuild/configs/board/ls1046ardb/manifest
+++ b/flexbuild/configs/board/ls1046ardb/manifest
@@ -39,7 +39,7 @@ securevalidate_enc="setenv secureboot_validate 'load \$devtype \$devnum:2 \$kern
securevalidate_dec="setenv secureboot_validate 'size \$devtype \$devnum:2 /Image;setexpr imgsize \$filesize - 0x30 ;echo Decapsulating linux image; setenv key_addr 0x87000000; mw \$key_addr $key_id_1;setexpr \$key_addr \$key_addr + 0x4; mw \$key_addr $key_id_2;setexpr \$key_addr \$key_addr + 0x4; mw \$key_addr key_id_3;setexpr \$key_addr \$key_addr + 0x4; mw \$key_addr $key_id_4; blob dec \$kernel_addr_r \$load_addr \$imgsize \$key_addr; cp.b \$load_addr \$kernel_addr_r \$filesize ;size \$devtype \$devnum:2 /fsl-ls1046a-rdb-sdk.dtb;setexpr imgsize \$filesize - 0x30 ;echo Decapsulating dtb image; blob dec \$fdt_addr_r \$load_addr \$imgsize \$key_addr; cp.b \$load_addr \$fdt_addr_r \$filesize ; '"
-distroboot='part uuid $devtype $devnum:3 partuuid3; setenv bootargs console=ttyS0,115200 earlycon=uart8250,mmio,0x21c0500 root=PARTUUID=$partuuid3 rw rootwait $othbootargs; if load $devtype $devnum:2 $load_addr /boot/uEnv.txt; then echo Importing environment from uEnv.txt ...; env import -t $load_addr $filesize; fi; load $devtype $devnum:2 $kernel_addr_r /boot/Image;load $devtype $devnum:2 $fdt_addr_r /boot/fsl-ls1046a-rdb-sdk-$serdes1-5559.dtb; env exists secureboot && echo validating secureboot && run secureboot_validate;booti $kernel_addr_r - $fdt_addr_r'
+distroboot='part uuid $devtype $devnum:3 partuuid3; setenv bootargs console=ttyS0,115200 earlycon=uart8250,mmio,0x21c0500 root=PARTUUID=$partuuid3 rw rootwait $othbootargs; if load $devtype $devnum:2 $load_addr /boot/uEnv.txt; then echo Importing environment from uEnv.txt ...; env import -t $load_addr $filesize; fi; load $devtype $devnum:2 $kernel_addr_r /boot/Image;load $devtype $devnum:2 $fdt_addr_r /boot/fsl-ls1046a-rdb-sdk-$serdes1-5a59.dtb; env exists secureboot && echo validating secureboot && run secureboot_validate;booti $kernel_addr_r - $fdt_addr_r'
```

上面的代码修改的内容就在于fsl-ls1046a-rdb-sdk-$serdes1-5559.dtb变为了fsl-ls1046a-rdb-sdk-$serdes1-5a59.dtb，客户可以仔细观察。

其次是修改flex-builder源码，将新增加的dtb文件拷贝到生成的镜像路径中

涉及到的文件在源码中的位置为：flexbuild/tools/flex-builder

修改内容为：

```plain
--- a/flexbuild/tools/flex-builder
+++ b/flexbuild/tools/flex-builder
@@ -459,7 +459,7 @@ gen_bootpart() {
if [ "$MACHINE" = "ls1046ardb" ]; then
cp $FBDIR/build/linux/linux/arm64/Image $FBDIR/build/images/boot
-       cp $FBDIR/build/linux/linux/arm64/fsl-ls1046a-rdb-sdk-1133-5559.dtb $FBDIR/build/images/boot
+       cp $FBDIR/build/linux/linux/arm64/fsl-ls1046a-rdb-sdk-1333-5a59.dtb $FBDIR/build/images/boot
cp $FBDIR/build/linux/linux/arm64/fsl-ls1046a-rdb-sdk-1040-5559.dtb $FBDIR/build/images/boot
cp $FBDIR/build/firmware/u-boot/ls1046ardb/ls1046ardb_boot.scr $FBDIR/build/images/boot
cp $FBDIR/build/firmware/u-boot/ls1046ardb/ls1046ardb_update.scr $FBDIR/build/images
```

至此，网络部分所有的代码修改完成

然后就可以参照软件手册编译章节编译系统，然后使用U盘更新系统即可使用

