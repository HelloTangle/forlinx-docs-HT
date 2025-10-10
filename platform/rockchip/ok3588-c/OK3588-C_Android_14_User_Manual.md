# Android14.0\_User's Manual\_V1.0

Document classification: □ Top secret □ Secret □ Internal information ■ Open

## Copyright Notice

The copyright of this manual belongs to Baoding Folinx Embedded Technology Co., Ltd. Without the written permission of our company, no organizations or individuals have the right to copy, distribute, or reproduce any part of this manual in any form, and violators will be held legally responsible.

Forlinx adheres to copyrights of all graphics and texts used in all publications in original or license-free forms.

The drivers and utilities used for the components are subject to the copyrights of the respective manufacturers. The license conditions of the respective manufacturer are to be adhered to. Related license expenses for the operating system and applications should be calculated/declared separately by the related party or its representatives.

## Overview

This manual is designed to help you quickly familiarize yourselves with the product, and understand the interface functions and testing methods. It primarily covers the testing of interface functions on the development board, the methods for flashing images, and troubleshooting procedures for common issues encountered in use. In the process of testing, some commands are annotated to facilitate the user's understanding, mainly for practical use. Please refer to “OK3588--C\_Android14.0_User’s Compilation Manual” provided by Forlinx for kernel compilation, related application compilation methods, development environment construction, etc. 

The manual is primarily divided into seven chapters:

+ Chapter 1. focuses on the overall overview of the product, and briefly introduces the development board in the interface resources, the relevant driver path in the kernel source code, and the description of the key parts of the information;
+ Chapter 2. mainly focuses on the fast booting of the product, which can be achieved through two methods: serial port login and network login, as well as the relevant introduction of the U-Boot menu;
+ Chapter 3. Android Function Test;
+ Chapter 4. focuses on the product's image update, mainly describing the method of updating the image to the storage device, and users can choose the corresponding flashing method according to the actual situation;
+ Chapter 5. is mainly about the OTA upgrade test of the product system;
+ Chapter 6. is mainly about the different display and different touch function of the product system;
+ Chapter 7. is mainly about the root authority management of the product system.

A description of some of the symbols and formats associated with this manual:

| **Format**| **Meaning**|
|:----------:|----------|
| **Note** | Note or information that requires special attention, be sure to read carefully|
| 📚 | Relevant notes on the test chapters|
| ️️🛤️ ️ | Indicates the related path.|
| <font style="color:blue;">Blue font on gray background</font>| Refers to commands entered at the command line(Manual input required).|
| <font style="color:black;">Black font</font>| Serial port output message after entering a command|
| **<font style="color:black;">Bold black</font>**| Key information in the serial port output message|
| //| Interpretation of input instructions or output information|
| Username@Hostname| console: development board serial port login account information, through which the user can determine the environment for function operation.|

After packaging the file system, you can use the “ls” command to view the generated files.

```plain
forlinx@ubuntu:~/3588$ ls                                  //List the files in this directory
OK3588-android-source  OK3588-android-source.tar.bz2
```

+ forlinx@ubuntu: the username is forlinx and the hostname is ubuntu, indicating that the operation is performed in the development environment ubuntu;
+ //: Explanation of the instruction, no input required;
+ <font style="color:blue;">Ls: </font>Blue font on a gray background, indicating relevant commands that need to be entered manually;
+ **OK3588-android-source**: The bottom black font is the output information after the input command, and the bold font is the key information. Here is the packed file system.

---


## Application Scope

This manual is mainly applicable to the Android14.0 operating system on the Forlinx OK3588-C platform. Other platforms can also refer to it, but there will be differences between different platforms. Please make modifications according to the actual conditions.

## Revision History

| **Date**| **Manual Version**| **SoM Version**| **Carrier Board Version**| **Revision History**|
|:----------:|:----------:|:----------:|----------|----------|
| 01/09/2025 | V1.0| V1.1| V1.1 and Above| OK3588-C_Android14.0_User's Manual Initial Version |

## 1\. OK3588 Development Board Description

RK3588 is a low-power, high-performance processor based on ARM64 architecture, which includes 4-core Cortex-A55 and 4-core Conrtex-A76 as well as independent NEON processor and neural network processor NPU, and it can be applied to computers, cell phones, personal mobile Internet, and digital multimedia devices.

Connection method is board-to-board, and main interfaces are shown in the figure below:

![Image](./images/OK3588-C_Android_14_User_Manual/1756801257271_d0a8d4dc_f09c_4bd3_bfe4_aff97930d9ea.jpeg)

**Front**

![Image](./images/OK3588-C_Android_14_User_Manual/1718940821408_beea409e_33fa_496f_a72c_967e8b8a77bd.png)

**Back**

**Note: Hardware parameters are no longer described in this software manual. Before referring to this manual for software development, please read the "OK3588-C\_User’s Hardware Manual” to understand the product naming rules and the hardware configuration information of the product you are using, which will help you to use this product.**

### 1.1 CPU/GPU/NPU Frequency Description

**RK3588J industrial grade SoM frequencies are described below:**

**Note: For the industrial-grade RK3588J SoM, to better test the maximum performance of this SOC, starting from version R4 and subsequent versions, the SoM in the user materials will default to operate in overclocking mode (Without performance requirements, it is recommended to modify it to the normal mode).**

Refer to “Rockchip RK3588J Datasheet V1.1-03/08/2023.pdf ”

Table 3-2 Recommended operating conditions

| Maximum CPU A76 frequency, normal mode ①| 1.6GHz
|----------|----------
| Maximum CPU A76 frequency, overclocking mode ②| 2.0GHz
| Maximum CPU A55 frequency, normal mode ①| 1.3GHz
| Maximum CPU A55 frequency, overclocking mode ②| 1.7GHz
| Maximum GPU frequency, normal mode ①| 700MHz
| Maximum GPU frequency, overclocking mode ②| 850MHz
| Maximum NPU frequency, normal mode ①| 800MHz
| Maximum NPU frequency, overclocking mode ②| 950MHz

① Normal mode indicates that the chip is operating at a safe voltage and frequency; For industrial environments, it is highly recommended to keep it in normal mode to reasonably ensure longevity.

②Overclocking mode will bring higher frequency, and the corresponding voltage will also increase. When running in overclocking mode for a long time, the life of the chip may be shortened, especially in high temperature conditions.

To switch to "normal mode", you need to add # include "rk3588j.dtsi" to the reference in the kernel device tree. The path is:

OK3588-android14-source/kernel-5.10/arch/arm64/boot/dts/rockchip/OK3588-C-Common.dtsi

![Image](./images/OK3588-C_Android_14_User_Manual/1718940821698_9b5343e2_7076_4e7c_a7f7_2c8aab90f447.png)

**RK3588 commercial grade SoM frequencies are described below:**

Refer to “Rockchip RK3588 Datasheet V1.7-17/11/2023.pdf ”

Table 3-2 Recommended operating conditions

| Maximum CPU A76 frequency| 2.2-2.4 GHz
|----------|----------
| Maximum CPU A55 frequency| 1.8GHz
| Maximum GPU frequency| 1GHz
| Maximum NPU frequency| 1GHz

### **1.2 Android14.0 System Software Resources Features**

| **Device**| **Location of driver source code in the kernel**| **Device Name**|
|----------|----------|----------|
| **LCD Backlight Driver**| **drivers/video/backlight/pwm\_bl.c**| **/sys/class/backlight**|
| **USB Port**| **drivers/usb/storage/**||
| **USB Mouse**| **drivers/hid/usbhid/**| **/dev/input/mice**|
| **Ethernet**| **drivers/net/ethernet/stmicro/stmmac**||
| **SD/micro TF card driver**| **drivers/mmc/host/dw\_mmc-rockchip.c**| **/dev/block/mmcblk1pX**|
| **EMMC Driver**| **drivers/mmc/host/dw\_mmc-rockchip.c**| **/dev/block/mmcblk2pX**|
| **OV13850**| **drivers/media/i2c/ov13850.c**| **/dev/videoX**|
| **LCD Controller**| **drivers/gpu/drm/rockchip/rockchip\_drm\_vop.c**||
| **MIPI CSI**| **drivers/media/platform/rockchip/cif/mipi-csi2.c**||
| **MIPI DSI**| **drivers/gpu/drm/rockchip/dw-mipi-dsi2-rockchip.c**||
| **LCD Touch Driver**| **drivers/input/touchscreen/edt-ft5x06.c**| **/dev/input/eventX**|
| **RTC Real Time Clock Driver**| **drivers/rtc/rtc-rx8010.c**   **drivers/rtc/rtc-pcf8563.c**| **/dev/rtc0**|
| **serial port**| **drivers/tty/serial/8250/8250\_dw.c**| **/dev/ttySX**|
| **Key Driver**| **drivers/input/keyboard/adc-keys.c**| **/dev/input/eventX**|
| **LED**| **drivers/leds/leds-gpio.c**||
| **I2S**| **sound/soc/rockchip/rockchip\_i2s\_tdm.c**||
| **Audio Driver**| **sound/soc/codecs/nau8822.c**| **/dev/snd/**|
| **PMIC**| **ddrivers/mfd/rk806-core.c**||
| **PCIE**| **drivers/pci/controller/dwc/pcie-dw-rockchip.c**||
| **Watchdog**| **drivers/watchdog/dw\_wdt.c**||
| **SPI**| **drivers/spi/spi-rockchip.c**||
| **PWM**| **drivers/video/backlight/pwm\_bl.c**||

### **1.3 EMMC Memory Partition Table**

The following table is the eMMC memory partition information of Android operating system (the size of a block is 512bit when calculating):

| **Partition Index**| **Name**| **Offset / block**| **Size/block**
|----------|----------|----------|----------
| N/A| security| 0x00002000| 0x00002000
| 1| uboot| 0x00004000| 0x00004000
| 2| trust| 0x00006000| 0x00002000
| 3| misc| 0x00008000| 0x00002000
| 4| dtbo| 0x0000a000| 0x00002000
| 5| vbmeta| 0x0000c000| 0x00000800
| 6| boot| 0x0000c800| 0x00020000
| 7| recovery| 0x0002c800| 0x00030000
| 8| backup| 0x0005c800| 0x000c0000
| 9| cache| 0x0011c800| 0x000c0000
| 10| metadata| 0x001dc800| 0x00020000
| 11| frp| 0x001fc800| 0x00000400
| 12| baseparameter| 0x001fcc00| 0x00000800
| 13| super| 0x001fd400| 0x00614000
| 14| userdata| 0x00811400| 

## 2\. Fast Startup

### **2.1 Preparation Before Startup**

+ 12V2A or 12V3A DC Power Cable
+ Debugging serial cable                                                                                         

The debug serial port on the development board is a Type-C socket, allowing connecting the development board to a PC using a USB to Type-C cable to monitor the status of the development board.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940829853_11e7dc47_93fa_44b4_84f9_15099a646a85.png)

### **2.2 Debugging Serial Driver Installation**

The debugging serial port of the OK3588 - C platform uses a Type - C interface. There is an on - board USB to UART chip, so there's no need to purchase a USB to serial port debugging tool. It is extremely simple and convenient to use.

To install the driver, please use the driver package DriverAssitant \_ v5.13.zip provided in the 3-tool directory.

Run DriverInstall.exe directly after the unzipping is completed; in order to ensure the driver is the latest version, please unstall the driver first, then install again.

### **2.3 Serial Port Login**

#### 2.3.1 Serial Port Connection Settings

 **Description:**

+ **Serial port terminal login user: serial port terminal automatically logs in root user without password;**
+ **Serial port settings: baud rate 115200, data bit 8, stop bit 1, no parity bit, no flow control;**
+ **Hardware Requirements: Type-C cable required to connect PC and development boards;**
+ **Software requirements: PC Windows system needs to install the super terminal software. Because the terminal software has many types, users can choose their familiar one.**

In the following, we take the putty terminal software as an example to introduce the serial port login method:

Step 1: Connect the serial port number of the computer---check the serial port number from the device manager (Based on the port actually recognized by the computer );

![Image](./images/OK3588-C_Android_14_User_Manual/1718940830154_f1183938_03bf_4ed0_b9c1_61c3cb36999d.png)

Step 2: Open and set up putty, then set the“ line according to the COM port of the computer used, baud rate 115200;

![Image](./images/OK3588-C_Android_14_User_Manual/1718940830351_944c8fb8_def2_4746_9449_2cd8763908a1.png)

Step 3: After the setting, input the COM port used by the computer in Saved Sessions. The following figure takes COM3 as an example, save the settings, open the serial port again later, and click on the saved port number;

![Image](./images/OK3588-C_Android_14_User_Manual/1718940830538_2553e7fc_b6d5_434b_ace7_7864de173fe8.png)

#### 2.3.2 Serial Login

After the terminal software on the PC side is set, connect the PC and the development board through the serial port cable, and power on after connecting the power supply. The startup information can be seen through the terminal software.

The following startup message indicates a successful start, allowing a new command line to be entered by pressing Enter:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940830731_94ee0055_dc57_46dc_a75b_940b5d86a20a.png)

### **2.4 Screen Switching**

OK3588 supports various screen interfaces such as MIPI DSI, HDMI, eDP, DP, RGB, etc., and can simultaneously perform mirroring and independent display for up to four screens. Currently there are three screen switching methods: uboot menu dynamic control; kernel device tree designation; DisplayHwConfig application control.

OK3588 contains 4 display controllers, i.e. 4 VP. It supports up to 4 screens simultaneously. The maximum resolution of VP0 is 7680x4320; the maximum resolution of VP1 is 4096x4320; the maximum resolution of VP2 is 4096x4320; the maximum resolution of VP3 is 2048x1080.

#### 2.4.1 Dynamic Control of Uboot Menu

##### 2.4.1.1 Display Type Settings

This method allows switching without recompiling and burn-in of existing supported screens.

During the uboot self-boot process, press the space bar at the serial terminal to bring up the control options:

```bash
Hit key to stop autoboot('Spacebar'):  0
---------------------------------------------
0:Exit to console
1:Reboot
2:Display type
---------------------------------------------
```

Enter 2 at the terminal to access the Screen Control sub-menu:

```bash
---------------------------------------------
hdmi0 and edp0 share same port, only one can be used.
hdmi1 and edp1 share same port, only one can be used.
only four VPs internally, so up to four interfaces can be activated
hdmi edp dp can only be displayed on VP0 or VP1 or VP2.
dsi0 dsi1 can only be displayed on VP2 or  VP3.
rgb can only be displayed on VP3.

Select  display
  0:Exit
  1: hdmi0 => VP0
  2: hdmi1 =>
  3: edp0  =>
  4: edp1  =>
  5: dp0   =>
  6: dp1   =>
  7: mipi0 =>
  8: mipi1 =>
  9: rgb   =>
  a: primary display  => HDMI0
b: primary display resolution => 1920x1080p50
---------------------------------------------
```

According to the content of the comments in the uboot menu, you can get the uboot display menu setting rules:

1\. Both hdmi0 and edp0 use the same port, and only one of them can be used at the same time;

2\. HDMI1 and EDP1 share the same port, and only one of them can be used at a time;

3\. There are only four VP internally, so a maximum of four interfaces can be activated;

4\. HDMI, EDP, and DP can only be displayed on VP0, VP1, or VP2;

5\. DSI0 and DSI1 can only be displayed on VP2 or VP3;

6\. RGB can only be displayed on VP3.

When setting up the display, enter the serial number corresponding to the display interface and VP will be assigned to the corresponding interface. If you input again, the system will switch the available VP (Virtual Ports) for this port one by one, or close the VP assigned to this port.

Enter a to switch the main screen display. Only the interface assigned with VP can be set as the main screen display.

**Setup Examples**:

As shown in the figure below, VP is assigned to hdmi0, hdmi1, dp0 and mipi0, so the main screen display can be selected from one of the above four interfaces. Because the HDMI interface is used, the EDP interface cannot be used. The primary display also selects HDMI0 with VP0 assigned and sets the resolution to 1920x1080.

**Note: When the primary screen is HDMI or DP, you need to set the "primary display resolution" to 3840x2160 and connect the primary screen before the device is powered on. Otherwise, connecting the main screen after startup will result in resolution switching on the secondary screen. When the main screen is EDP or MIPI, the primary display resolution option will not take effect.**

```bash
---------------------------------------------
Select  display
  0:Exit
  1: hdmi0 => VP0
  2: hdmi1 => VP1
  3: edp0  =>
  4: edp1  =>
  5: dp0   => VP2
  6: dp1   =>
  7: mipi0 => VP3
  8: mipi1 =>
  9: rgb   =>
  a: primary display  => HDMI0
b: primary display resolution => 1920x1080p50
---------------------------------------------
```

#### 2.4.2 Kernel Device Tree Specification

This method does not require the connection of a serial terminal, and the system image defaults to the desired configuration selection, which is suitable for mass production. However, we need to manually modify the device tree and regenerate the system image once again

Note: This method has a higher priority than the screen selection in U-Boot and the DisplayHwConfig application. After modifying the device tree, the selection in U-Boot will not take effect.

Device tree path: kernel-6.1/arch/arm64/boot/dts/rockchip/OK3588-C-Common.dtsi

In the kernel source code, open the device dtsi file and find the following node:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940830946_1935c571_9a4a_436b_abc6_ddbe18e07737.png)

The node has a default disabled state and needs to be changed to an okay enabled node. Change according to screen requirements.

**Parameter Description:**

| | **Meaning**
|----------|----------
| status| Describe the node state: disabled is for off, okay is for on
| HDMI0| Specify the VP assigned to HDMI0
| HDMI1| Specify the VP assigned to HDMI1
| EDP0| Specify the VP assigned to EDP0
| EDP1| Specify the VP assigned to EDP1
| DP0| Specify the VP assigned to DP0
| DP1| Specify the VP assigned to DP1
| MIPI0| Specify the VP assigned to MIPI0
| MIPI1| Specify the VP assigned to MIPI1
| RGB| Specify the VP assigned to RGB
| primary\_display| Specify the main screen display

Users need to change the setting parameters as required. After saving, it is necessary to recompile and generate an image.

An annotated description of the node:

1\. Both hdmi0 and edp0 use the same port, and only one of them can be used at the same time;

2\. HDMI1 and EDP1 share the same port, and only one of them can be used at a time;

3\. There are only four VP internally, so a maximum of four interfaces can be activated;

4\. HDMI, EDP, and DP can only be displayed on VP0, VP1, or VP2;

5\. DSI0 and DSI1 can only be displayed on VP2 or VP3;

6\. RGB can only be displayed on VP3.

So the optional parameters for HDMI0/1, EDP0/1, DP0/1 are "VP0", "VP1", "VP2", and "OFF";

MIPI0/1 optional parameters are: "VP2", "VP3";

The RGB optional parameter is: "VP3";

The primary\_display parameter depends on the actual display interface assigned to get the VP.

**Note: When modifying the device tree, you need to follow the annotation rules to avoid using conflicts. The driver does not detect whether the forlinx-control configuration conforms to the rules. An error in the setting will cause abnormal display. For the display interface set to "OFF", blocking, deleting, or retaining is possible. It’s not necessary to set all four VP.**

**Examples**:

Assign VP0 to HDMI0, VP1 to HDMI1, VP2 unused, and VP3 for RGB use. Set the main screen to HDMI0.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940831160_05a365a0_cb31_4721_8ec5_c7e9cdb3d04a.png)

After saving, recompile to generate the image.

### **2.5 System Shutdown**

In general, the power can be turned off directly. If there is data storage, function use, or other operations, avoid turning off the power arbitrarily during operation to prevent irreversible damage to the file. In such cases, only re-flashing the firmware can resolve the issue. To ensure that data is not completely written, enter the sync command to complete data synchronization before turning off the power.

Note: For products designed based on the SoM, if there are scenarios where accidental power loss causes the system to shut down unexpectedly, measures such as adding power-loss protection can be incorporated into the design.

## 3\. Android Function Use and Test

### **3.1 Main Interface Display**

![Image](./images/OK3588-C_Android_14_User_Manual/1718940851764_add4982c_67b8_43fa_b30f_26a38599a66c.png)

### **3.2 Application**

Swipe up on the main screen to bring up the following screen.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940852125_3ab8d177_fbc4_4891_bce5_c6ccc6f6fb9c.png)

Note: After software version updates, there may be minor differences, which do not represent the actual images for each subsequent version update and are provided for reference only.

### **3.3 Language Settings**

Click “![Image](./images/OK3588-C_Android_14_User_Manual/1718940852445_596f8ecb_5e13_45b8_a0a9_eb9b20e905cd.png)”, on the application interface to enter the setting interface:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940852654_09f5669c_469c_465c_844f_fab9ae36d499.png)

Click "" on the application interface to enter the system interface.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940852893_546e7eaa_dbca_4884_ac82_a1f93c40afe1.png)

Click "Language and input method" to enter the language setting interface:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940853119_274361bf_2ee9_45c0_b72d_11c98c363c8e.png)

Click "Language" to enter the language selection interface:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940853315_fb907dfb_2994_43ea_87ef_ba5f7ad629c3.png)

Click "Add Language" to add a new language.

If you want to remove an installed language, you can click the icon with three dots in the upper right corner, select Remove, check the language you want to delete, click the trash can icon in the upper right corner, and a dialog box pops up, "Do you want to remove the selected language?" Click “Confirm” to deleted the language.

### **3.4 Picture and Audio View**

Store the picture and video files to be viewed into the TF card, and insert the TF card into the development board.

Click "![Image](./images/OK3588-C_Android_14_User_Manual/1718940853535_9a11c3e1_7395_4a08_a80a_dd8083272ee2.png)" on the application interface to enter the TF card picture browsing interface.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940854054_ba732e9c_d6e6_465a_8f04_b738a3ebaabc.png)

Configure permissions:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940854376_8eba1510_4871_4e3d_a0a8_fb4004a6f23b.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940854625_6a81c631_e807_402f_bb0d_7528b156f634.png)

After configuration, enter the picture and video view:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940854943_e622b66d_329b_4f9d_9aa4_94abe8bc4a95.png)

Click on the pictures and videos to view:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940855260_bea26119_a890_40eb_8af5_750ecb31ef31.jpeg)

### **3.5 Multimedia Test**

Store the audio file to be played into the TF card, and insert the TF card into the development board.

Click "![Image](./images/OK3588-C_Android_14_User_Manual/1718940855553_619a0b2a_7e14_4f3f_ae84_01e76703daf9.png)" in the application interface to enter the music player interface.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940855774_7d1a04aa_1f20_486c_a85f_98aa5549281f.png)

Click "![Image](./images/OK3588-C_Android_14_User_Manual/1718940855977_8cea84b4_558d_4351_9370_08b40b4a8bd3.png)" in the interface to enter the song list interface.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940856205_c29fe46e_81c8_46be_8c31_1972f7711a0f.png)

Click Play Music to enter the play interface.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940856428_a7b5c971_70f8_4d65_90a7_3105ce27773f.png)

The priority of sound playback is headphone > HDMI audio > carrier board speaker, and the volume can be adjusted by pressing the physical keys VOL + and VOL- on the carrier board of the development board.

### **3.6 Recording (Supports Mic input)**

Click the video "![Image](./images/OK3588-C_Android_14_User_Manual/1718940856611_8bb56dd9_9cfa_4a14_9df7_12b8308fa6a2.png)" in the application interface to enter the recorder interface:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940856871_ecb37d19_17a6_46e4_a021_d235c0ef8a8f.png)

Configure permissions:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940857142_166b57e9_3fa7_4df7_9f68_e3a817d4199e.png)

Click the round button to start recording: (Note: the pointer will swing according to the sound level during normal recording).

![Image](./images/OK3588-C_Android_14_User_Manual/1718940857349_6b63fbbf_4aa2_44b4_9e10_533820356262.png)

Click the square button to stop recording, and finally click the done button to save.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940857576_820871e7_6a67_4e3e_ac35_7ea3ad6458a8.png)

Click the "![Image](./images/OK3588-C_Android_14_User_Manual/1718940857811_48b7d1f3_2894_43fc_aae3_3424122ac6a7.png)" button below to display the previously recorded audio file.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940858035_c470d6cd_25ef_4c0d_9580_f061bd7429a7.png)

Click on the audio file you want to play, and the recording will start playing.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940858271_fe6b026b_7cd6_4e58_aced_7f7a6f58d64b.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940858462_ea22b036_fde4_4cb6_ac42_2073c334aa29.png)

### **3.7 Adjusting the Volume**

Click “![Image](./images/OK3588-C_Android_14_User_Manual/1718940858645_25cf73f5_ebd1_4f1e_a54b_407d27052933.png)”, on the application interface to enter the setting interface:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940858846_79ef215e_2a9e_4dca_b81b_9a6f1e6254f9.png)

Click "Sound" in the settings interface to enter the volume settings interface.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940859071_b8833ee0_1f08_423e_806e_b02e0d1b6855.png)

This interface allows you to adjust each section's volume and supports media volume adjustment using the physical buttons VOL- and VOL+ on the base plate. The default alarm tone is Cesium. Click "Default Alarm Tone" to modify it.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940859260_125990ed_f017_4008_8835_b419b8d7c849.png)

### **3.8 Display Settings**

Click “![Image](./images/OK3588-C_Android_14_User_Manual/1718940859453_95a99126_d6b7_4096_a0d7_5dcfba9d61c0.png)”, on the application interface to enter the setting interface:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940859635_fce240fb_d343_4516_899e_d45212ab572f.png)

Click "Display" in the setting interface, enter the display setting interface, and select "Brightness" for the backlight setting, then the brightness adjustment slider will appear, adjust the brightness. Because the development board provided by Forlinx does not have a power sensing chip, the automatic screen rotation function in the advanced options does not work.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940859840_ac3b357a_3e8e_4abe_92c8_e0156a76fe66.png)

The default setting of OK3588 is to never turn off the screen. If you need to sleep and wake up, please click the "Screen timeout" option to select the sleep time.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940860050_12e278bb_3a09_4935_8fa6_ef1308a96cda.png)

Select screen sleep time.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940860236_8502bc78_9334_446f_ac2e_94608da6f5bd.png)

If there is no operation on the interface within the set sleep time, the screen will enter the sleep mode, and pressing the PWRON physical button on the carrier board will wake up the screen.

### **3.9 Time Setting（RTC）**

Click “![Image](./images/OK3588-C_Android_14_User_Manual/1718940860464_22ea1d4e_1a24_405a_b710_bd64a3294b1f.png)”, on the application interface to enter the setting interface:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940860644_66edba9b_f6b7_4647_963f_60ba6abd8897.png)

Select "System," where you can change the date and time, and even after power failure, the time can still be synchronized (ensure that the button battery is installed on the board).

![Image](./images/OK3588-C_Android_14_User_Manual/1718940860838_a5d8aa72_ddb7_436e_bb51_6ac1e166680a.png)

The default is "Turn off network-provided time" and the time format is 24 hours.

Set the date and time separately：

![Image](./images/OK3588-C_Android_14_User_Manual/1718940861066_a578d44d_ce13_4880_b9ca_2008ca511c89.png)

Click on “Set Date.”

![Image](./images/OK3588-C_Android_14_User_Manual/1718940861309_2775c797_aaa9_43c8_b2a7_c3a587818325.png)

Click on “Set Time.”

![Image](./images/OK3588-C_Android_14_User_Manual/1718940861719_e3b8b1ae_b6a5_465f_80d5_381190e603f7.png)

### **3.10 Ethernet Test**

OK3588 has two Gigabit NICs on board (Ethernet ETH0 and Ethernet ETH1).

**Description:**

+ **When 4G and Ethernet exist at the same time, Ethernet is preferred by default; When 4G WIFI exists at the same time, WIFI is preferred by default. When both WiFi and Ethernet are present, Ethernet is prioritized by default.**

1\. Gigabit network port test:

Prepare a router and a network cable that can be connected to the external network port.

After inserting the network cable, click "![Image](./images/OK3588-C_Android_14_User_Manual/1718940861904_5044199e_b450_41db_a258_99db21943c31.png)" on the application interface:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940862085_cd2c7080_8c28_4e19_b48d_663ab9302441.png)

Click Network and Internet:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940862284_57f61d68_7ed2_412f_90d0_bac1eea2b042.png)

Click "Ethernet ETH0" to choose to automatically obtain IP DHCP or static IP. DHCP is recommended. If you set a static IP, make sure your network parameters are available.

Click "Ethernet":

![Image](./images/OK3588-C_Android_14_User_Manual/1718940862478_90cd6a73_53e3_46e9_b16a_ea7d555ad59a.png)

The default IP acquisition method is "dhcp". If you want to set a static IP, click Ethernet Ip mode:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940862718_98873593_5e2a_47fa_9154_424dec1473ff.png)

Select Static for static IP configuration:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940862943_569943d1_5051_4c94_8ee9_4e45c51321a7.png)

Click CONNECT to complete the configuration:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940863139_66193319_b0ed_4499_a745_ea2cc8514f34.png)

Click Lightning on the application interface for network test:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940863365_645a2c4f_1364_450d_831b_45bdbfc367b8.png)

Enter "[http://www.forlinx. net](http://www.forlinx.com)” in the domain name column and click "Start" to enter the official website of Forlinx.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940863696_36419b8d_9fc5_4e6d_b89d_09b12b60da3e.png)

### **3.11 WiFi Internet**

**Description:**

+ **When 4G and Ethernet exist at the same time, Ethernet is preferred by default; When 4G WIFI exists at the same time, WIFI is preferred by default. When both WiFi and Ethernet are present, Ethernet is prioritized by default;**
+ **When testing WiFi, unplug the wired network.**

The OK3588 supports two modules onboard, the AW-CM276MA and the AW-XM458. Open Settings, select "Network \& Internet", and click "WLAN":

![Image](./images/OK3588-C_Android_14_User_Manual/1718940864025_06484d1e_2829_47f5_a6b2_0f4fad4621f4.png)

Click "Use WLAN":

![Image](./images/OK3588-C_Android_14_User_Manual/1718940864282_5bdbecbd_046b_46de_858f_b19ec4f40b3c.png)

Click on the WIFI to be connected and enter the password:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940864520_ff2629f1_22dd_4887_ad10_5b547b168612.png)

After successful connection, you can open the browser and enter the URL for network test:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940864780_72de18f2_99fb_4339_8cf1_d75297209c7d.png)

### **3.12 WiFi Hotspot Test**

OK3588 supports the sharing of Ethernet or mobile networks through WIFI for WIFI hotspot testing. First, plug the network cable into the OK3588 ETH0 connector. Open Settings and click Network and Internet.

Click "Hotspot \&tethering":

![Image](./images/OK3588-C_Android_14_User_Manual/1718940865108_c253897a_6790_46e4_b0d7_09e68fe95049.png)

Click WLAN Hotspot:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940865329_e2fd5f8c_d315_4ca7_abcf_a5fc556a4f5e.png)

Enable the WLAN hotspot and set the hot spot name and password:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940865552_3edf1119_4227_4773_b99d_f1b423821f31.png)

First set the hotspot name:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940865940_f3c112e2_fb81_4de8_8c7f_76816fcc9c45.png)

Click “Confirm”.

Set hotspot password:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940866189_030fd1ac_c057_455a_b4c1_618509781ef6.png)

Click “Confirm”.

After connecting to the hotspot through the mobile phone, you can surf the Internet normally.

### **3.13 4G/5G Module Test**

**Description:**

+ **When 4G and Ethernet exist at the same time, Ethernet is preferred by default; When 4G WIFI exists at the same time, WIFI is preferred by default. When both WiFi and Ethernet are present, Ethernet is prioritized by default;**
+ **When testing 4G, unplug the wired network and turn off WiFi;**
+ **When using the 4G module, dial the S2 to ON, and when using the 5G module, dial to the other end.**

The OK3588 carrier board supports 4G modules (EM05) and 5G modules (RM500U, RM500Q). Before the test, please power off the development board, connect the 4G/5G module and insert the SIM card (pay attention to the direction of the SIM card), and start the development board.

Open Settings, select "Network and Internet", and click "SIM card":

![Image](./images/OK3588-C_Android_14_User_Manual/1718940866450_18bc9f19_c68d_45e0_9350_1b5bd119ff56.png)

The default mobile network is on:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940866665_05981542_30f0_4e0c_b6a8_6724a66c585f.png)

Link 4G appears in the drop-down menu when the connection is successful.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940866896_840506dc_be19_4a0b_ac71_c89e4aff104a.png)

After successful connection, you can open the browser for network test:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940867189_00f3370c_f7b1_4e5e_b9a8_7acfdf757b64.png)

The test method of 5G is the same as that of 4G, and the difference is that the icon display is different:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940867478_8cc23a57_16c4_4dbd_af6f_8763ad9ef07b.png)

### **3.14 Bluetooth Test**

**Description: The current system does not support iPhone Bluetooth connection.**

The Bluetooth function test of OK3588 platform uses the WiFi \& Bluetooth integrated module, which supports the connection of Bluetooth devices as the main device to transmit/receive files.

The testing method is as follows:

Click “![Image](./images/OK3588-C_Android_14_User_Manual/1718940867672_c4726e29_409b_4b9c_9c13_fbf2c62f6f27.png)”, on the application interface to enter the setting interface:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940867865_a14ba787_7eaf_49ff_8ec2_c092c74faf64.png)

Click "Connected device" to enter the Bluetooth setting interface.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940868057_21ec4604_9e63_4cfa_bfd1_b7555c0e5657.png)

Click "+ pair with new device", open PC Bluetooth to scan at the same time, and click the Bluetooth device to be connected.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940868310_e1c66ce5_b32a_4655_9ad8_b769b283b6ec.png)

Click "Pairing", the mobile phone performs the corresponding pairing operation, and the interface of successful Bluetooth connection displays:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940868641_a1213099_e8ee_4e15_8940_6791fe52d668.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940868881_b1d78566_f2d0_437b_8fa1_4dd88a8ff31b.png)

1\. File transfer file test:

Accept the file:

The mobile phone shares photos to the OK3588 using Bluetooth; click "Accept" will start the outgoing.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940869108_d6c3b872_2d68_4f4f_8da0_84c9fdb26b1a.png)

The transfer progress will be displayed in the prompt bar, and you can view the picture after the transfer is completed.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940869328_256493ee_2994_4a8a_8eb6_e560fbe9f951.png)

2\. File transfer test:

Click “![Image](./images/OK3588-C_Android_14_User_Manual/1718940869617_06edf6aa_22e3_4f59_af5d_270bc2e68288.png)” File Application to enter the file system interface.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940869802_9027bf3a_218a_4186_a326_74f12e37499e.png)

Select an image and click the share button in the top right corner "![Image](./images/OK3588-C_Android_14_User_Manual/1718940870088_cacd908e_01fa_4c16_ac60_1f739f41acb3.png)".

![Image](./images/OK3588-C_Android_14_User_Manual/1718940870286_9a525cbb_633f_49ed_81ab_6d59a7f07288.png)

Send via Bluetooth.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940870491_f0618d34_edfb_41af_9ff7_9f094d7bcce9.png)

Select the previously paired device, select the phone to receive the file, and the Bluetooth transfer will start.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940870715_9c646170_ba1b_474c_ab48_b1d278bf4197.png)

You can view the transfer progress in the notification bar, and after the transfer is complete, you can view the received images on your phone.

### **3.15 Key Test (Sleep Wake-up)**

There are 8 keys on the development board, including VOL +, VOL-, MENU, ESC, HOME, PWRON, RESET and Maskroom.

| **Key**| **Function**
|----------|----------
| Recovery/VOL+| VOL+
| VOL-| VOL-
| PWRON| Wake up from sleep and power on/off
| Maskroom| Work with RESET to enter maskrom mode.
| RESET| RESET
| MENU| Pop-up menu Home screen settings, Widget, Wallpaper
| ESC| Return

The default factory setting is the non-hibernation state. At this time, press the PWRON key lightly to turn off the screen and enter the hibernation state (note that the carrier board cannot be inserted into the wake-up source such as USBOTG). The hibernation print information is as follows:

```bash
de345678INFO:    PMU1_PWR_CON(0x1) PMU1_CRU_PWR_CON(0x2f) PMU1_WAKEUP_INT_CON(0x100)
PMU2_BUS_IDLE_ST(0x27fffff 0x0) PMU2_BUS_IDLE_ACK(0x27fffff 0x0) PMU2_PWR_GATE_ST(0x6fffffff 0x0)
PMU2_BUS_IDLE_CON(0x0 0xfd80 0xf007) PMU2_BIU_AUTO_CON(0xffff 0xffff 0x7)
PMU2_PWR_GATE_CON(0x0 0x9000 0x3)
PMU2_VOL_GATE_CON(0x7 0x0 0x3)
PMU2_QCHANNEL_PWR_CON(0x0) PMU2_QCHANNEL_STATUS(0xfe0007f)
PMU1_DDR_PWR_CON(0x747 0x747 0x747 0x747)
PMU1_DDR_PWR_SFTCON(0x900 0x900 0x900 0x900)
PMU1_PLLPD_CON(0xffff 0x3)
PMU2_DSU_PWR_CON(0x3)
PMU2_CORE_PWR_CON0(0x1 0x1)
PMU2_CORE_AUTO_PWR_CON0(0x0 0x0)
PMU2_CLUSTER_IDLE_CON(0x75)
INFO:    PMU0_PWR_CON(0x0) PMU0_WAKEUP_INT_CON(0x0)
PMU0_DDR_RET_CON(0x0 0x0)
PMU1_GRF_SOC_CON2(0x7777) PMU0_GRF_OS_REGS9(0xf2acf6f4)
S
```

In the sleep state, press the PWRON key again to wake up the CPU. Press and hold PWRON to shut down the device

The other buttons have simpler functions, so please test them yourself.

### **3.16 TF Card and USB Storage Test**

It is a test of TF card and USB storage device. Insert the USB device into the OK3588 USB Host port. The system will automatically detect the insertion of the USB flash drive.

Click “![Image](./images/OK3588-C_Android_14_User_Manual/1718940870904_e0b170d3_9008_46d8_94b6_6d9a01ebbc64.png)”, on the application interface to enter the setting interface:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940871077_e97e2689_db4a_41df_87f9_affafbb167c2.png)

Click "Storage" to view the internal storage device and the inserted U disk device:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940871279_a555155e_52a4_4185_8863_ebc78eb1dc95.png)

Click "MASS U disk" to view the contents of the U disk for reading and writing:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940871673_d7d698ea_f8c2_42f7_8b23_ed63fab415d6.png)

Click the file.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940871919_a7875cf3_ea72_4b52_bab8_bc372182a31e.png)

The TF card reading and writing method is the same as the U disk reading and writing test method. Insert the TF card into the TF card slot, and the system will automatically detect the insertion of the TF card. You can also view the contents of the TF card in the storage interface:![Image](./images/OK3588-C_Android_14_User_Manual/1718940872209_07167ff9_a243_4534_929c_96eeb8386d2c.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940872470_d924ecf0_9552_4998_a5fb_298266d70949.png)

### **3.17 USB Mouse Test**

Once the system is running, you can plug in a USB mouse into the USB host. You will then see the mouse cursor “</font>![Image](./images/OK3588-C_Android_14_User_Manual/1718940872695_b43cb3fd_d14a_4a2c_9f96_40e210aa3683.png)<font style="color:#000000;">”, within the interface, and you can navigate and operate the Android system using the mouse.

### **3.18 USB OTG Interface Test**

The OK3588 development board supports USB OTG functionality.

Typec0 of the development board is connected to the computer through the otg cable, and the computer will recognize the board as follows:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940872870_c63a428a_532c_47f4_878a_630f552f06dc.png)

### **3.19 Serial Port Test**

UART2, UART4, UART6, UART9, a total of four serial ports led out from the OK3588 carrier board; UART2 for debugging serial port, UART6 for Bluetooth serial port, and UART9 for 485 serial port. The default device names of UART4 and UART9 in the development board are ttyS4 and ttyS9 respectively. Take the test of UART4 serial port as an example, short-circuit the receiving and transmitting pins of UART4 according to the schematic diagram of the development board, corresponding to PIN7 and PIN10 respectively.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940873077_66f4f3db_35bf_4357_a8cf_a42bb896366a.png)

Open the serial port test program on the desktop![Image](./images/OK3588-C_Android_14_User_Manual/1718940873299_589c4ea1_dcc9_470f_b35c_9b3a0e3126cc.png).

![Image](./images/OK3588-C_Android_14_User_Manual/1718940873538_0b1dfb17_04a8_4b48_a9fe_5e9e6bb072af.png)

Click the "SETUP" button:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940873796_dd45eb36_7cf3_4cd4_b5c8_944920886b8c.png)

Set serial port device, baud rate and display format:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940874004_57297b44_a639_4f3c_8085_b55823a4aaf3.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940874230_15709e28_b324_4fec_8ac8_c4d39c97d49e.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940874414_b8f2501b_6f8a_47b6_add9_3053bc10fc40.png)

Then click the "Loopback" option in the previous menu to perform the loopback test.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940874700_75833af7_0fad_41b4_90a7_c5313d1cd3af.png)

Click the "CONSOLE" option in the previous menu to perform the send-receive test:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940874915_81194e6a_dd6d_4bbf_9e71_ed10ea89b3c6.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940875423_e1abe183_ad29_4cd1_add9_c67466f758e5.png)

### **3.20 Watchdog Test**

Click![Image](./images/OK3588-C_Android_14_User_Manual/1718940877395_f50e79a6_5822_45bb_ab34_43f1f2dd0f9a.png) "forlinux \_ watchdog \_ test" "on the application interface to enter the watchdog test:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940877667_6533bb77_d1dd_4491_a1d2_3be6787df24c.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940877945_df761718_b899_45c8_9b4c_82f4f8c301b8.png)

There are three buttons on the interface: "start", "feed" and "stop". Click "start" to see the dog and "feed" to feed the dog:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940878167_889ba672_3654_4a6b_859e_3304d79e9710.png)

If a timeout (timeout of 10S) is not performed to feed the dog, the system reboots. Click "stop" to stop the watchdog test, and the system will not start:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940878366_cf33c763_78c0_4f07_8d01_031e915426b6.png)

### **3.21 Camera Test**

#### 3.21.1 UVC Camera Test

Click on the camera in the application interface:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940878650_f124d2eb_0b66_4c82_9043_360114c3cc72.png)

Configure permissions:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940878930_a2a62514_7da5_475c_ab45_b021f234801d.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940879132_52ab1ecb_cf03_45d9_915b_e1c2c6a45f40.png)

Enter the preview interface and click the photo button on the right to take a photo:

Swipe the screen to the right to open the options for switching between photo and video mode, as well as accessing settings.

![Image](./images/OK3588-C_Android_14_User_Manual/1721890643832_71418849_2fe4_4623_b6b2_400612db339c.png)

Tap on the settings button in the top right corner to adjust settings such as resolution and image quality.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940880055_4ec30317_f3cd_43e1_b53e_ccd7d1323346.png)

Click the video button to enter the video preview interface:

Click the video button to record the video:

![Image](./images/OK3588-C_Android_14_User_Manual/1721890763616_707f7024_6605_4543_99a2_a05574d832af.png)

#### **3.21.2 OV13855 Camera Test**

OK3588 supports 5 x mipi Camera, in which CAM1 and CAM2 are used for OV13855 and CAM3, CAM4 and CAM5 are used for MIPI OV5645.

Please power off first, plug in two OV13855 Cameras, and power on to start.

Click on the camera in the application interface:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940881009_15efed50_7203_4942_bc2d_e5db52c13dcc.png)

Configure permissions:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940881274_72834fe4_425c_4777_961f_21511c11f406.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940881439_1b6e5474_4658_4189_8a22_c6d241ef60d3.png)

Enter the preview interface and click the photo button on the right to take a photo:<u><font style="color:#000000;"> </font></u>![Image](./images/OK3588-C_Android_14_User_Manual/1721891522720_eb5d5aeb_42f4_4d65_922b_c9d18c969360.png)![Image](./images/OK3588-C_Android_14_User_Manual/1721891610968_dc014b4a_f46b_49bc_adea_a9d9fd012028.png)

Swipe the screen to the right to open the options for switching between photo and video mode, as well as accessing settings.

Tap on the settings button in the top right corner to adjust settings such as resolution and image quality.

Click the video button to enter the video preview interface:

![Image](./images/OK3588-C_Android_14_User_Manual/1721891447795_3b70ab31_8401_4a6c_8f12_aa6a6fc3468b.png)

Click the video button to record the video:

![Image](./images/OK3588-C_Android_14_User_Manual/1721893524238_9db0bd0a_734c_4aa2_93b4_27d6733ef48a.png)

### **3.22 HDMI Resolution Setting Test**

OK3588 platform supports dynamic setting of HDMI resolution.

Click “![Image](./images/OK3588-C_Android_14_User_Manual/1718940883852_a3c1f1bf_e337_4385_a7a7_d93b311dd079.png)”, on the application interface to enter the setting interface:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940884012_037d02cd_7df3_4e2d_aa1a_05b8e2c82de7.png)

Click "Display", select "Advanced", and click "HDMI" to configure HDMI:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940884210_adcfee37_9e77_4a7f_96f1_7e12c99a03bc.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940884451_ff05dd28_66bd_457a_9fac_4f281b26e6af.png)

You can dynamically select the desired resolution based on the resolution supported by the current HDMI screen:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940884642_e81b06db_1e8b_430c_ac9e_f2e5cd918910.png)

After restarting, the device will take effect.

### **3.23 Factory Reset**

The OK3588 platform supports restoring factory settings.

Click “![Image](./images/OK3588-C_Android_14_User_Manual/1718940884897_dfc7fe83_d595_4703_89e0_38963a2b0609.png)”, on the application interface to enter the setting interface:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940885116_c14afa8b_db64_46b9_80bb_70d5d59da08b.png)

Click "System":

![Image](./images/OK3588-C_Android_14_User_Manual/1718940885312_b4c4e1f3_bd9d_4513_a35a_772b9e423afa.png)

Click "Reset option" and select "Clear all data (restore factory settings)":

![Image](./images/OK3588-C_Android_14_User_Manual/1718940885569_bae964bd_d2ec_45b0_b29d_9d072d583a81.png)

Then click "Clear All Data".

![Image](./images/OK3588-C_Android_14_User_Manual/1718940885786_e1977ee2_cb28_4f47_98f8_7b8811bbca38.png)

Wait for OK3588 to restore the default factory settings. Please do not power off during the process of restoring the factory settings.

### **3.24 APK Installation with TF Card**

After loading the TF card according to the previous steps, you can see an APK file after entering the TF card directory.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940885984_1018124e_d1da_4141_abdc_0394482e38e8.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940886206_1b506013_3e51_4065_a8c6_3256076b7930.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940886616_03276922_faf0_46eb_a2a1_fecdbedaad86.png)

Double-click the APK file to install and configure permissions:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940886878_40fadb02_05f3_4902_97be_fa61bc342b55.png)

Click "Install" to complete the installation:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940887176_6bc257d6_021c_4888_843a_4f95fac44c5b.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940887446_8bf8c21b_0047_4dba_a4db_53295ad4ccea.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940887661_5faa9ef2_523a_4628_a212_033543dab0d1.png)

### **3.25 WiFi ADB Test**

**Note: Only one of USB ADB and WIFI ADB can be used at the same time.**

Follow the previous section to connect to WIFI, click "![Image](./images/OK3588-C_Android_14_User_Manual/1718940888104_c9c97cbc_3d2b_4115_979a_dcdce047e2d1.png)" after successfully connecting to WIFI:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940888308_56ddf819_5705_4ee7_9a34_4fd826d223c0.png)

Click “About Tablet PC”:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940888516_28f85cb4_7461_41b3_963a_e398f682d896.png)

Continuously click the "Version number" prompt to enter the development mode:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940888787_3fa900c8_0877_4c0a_94e9_1485af1bce2f.png)

Return to the previous layer and select "System" in the setting interface:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940889002_3f0220c2_99d3_40ca_8b32_f3380b997137.png)

Select Developer Options, you need to turn off "USB Debugging" and turn on "Wireless Debugging":

![Image](./images/OK3588-C_Android_14_User_Manual/1718940889225_5764655f_4d43_43b8_a41d_f1dafc6243d8.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940889471_0e5e95a0_8aa4_4f2c_af95_ad215feccaad.png)

Record the "IP address and port" of the current WIFI.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940889678_6e117ba5_1314_4137_a3ad_93512f79c8ae.png)

Open the window command and control window, type "adb connect 192.168.1.61:43985" to connect to wifi:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940889861_17a6067b_558b_4862_9348_81ceaca8446f.png)

Type "adb devices" to see the connected devices. Enter "adb shell" to access the device terminal.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940890105_8a11e591_37cf_438b_8f31_172782b5bc1f.png)

Type "adb disconnect" to disconnect, and then type "adb devices" to see the devices.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940890299_f6ab1a28_ae41_45c5_8c73_b3d7f50308b8.png)

### **3.26 Navigation and Status Bar Settings**

The current release supports showing/hiding the navigation and status bars.

Select Show Navigation Bar and Show Status Bar to control whether they are hidden.

Restart OK3588.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940892015_6867ac9f_a1d8_491d_8910_98572d2654a2.png)

Block the navigation bar, top slide bar, and right mouse button for the return function.

### **3.27 Artificial Intelligence Test**

OK3588 android platform supports tensorflow lite and other mainstream AI frameworks. TFL Detect is used here to test target detection routines for customer reference. Routines such as accessories need to be installed by yourself.

The TFL Detect test routine![Image](./images/OK3588-C_Android_14_User_Manual/1718940893133_81954254_4686_40cf_8701_1bbd45d3b882.png)is the official routine of tensorflow lite, which can run directly on the OK3588 platform without modification. It mainly uses the computing performance of the A-core, which occupies relatively high CPU, but it can often achieve higher detection frame rate by using multi-wire.

Test by placing the item in front of the camera will automatically recognize the item.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940893435_f6d2a8bb_0ca3_4084_b356_01894a9b7d7d.png)

### **3.28 Screen Lock Test**

**Note**: **By default, Android will not lock the screen when it is started for the first time. If it is not modified, it will be opened in the lock screen state after restarting.**

OK3588 does not lock the screen by default. If you need to lock the screen, you can set the screen lock through Settings-> Security and Privacy->, as follows:

![Image](./images/OK3588-C_Android_14_User_Manual/1756801260353_a9446aaa_658f_4096_a471_ecf25114d0de.png)

Select a screen lock method.

### **3.29 NPU Test**

OK3588 The current test NPU examples are: rknn\_mobilenet\_demo\_Android, rknn\_ssd\_demo\_Android, and rknn\_multiple\_input\_demo\_Android, respectively, and the test routines are located at:

️ <font style="color:#000000;">Path: OK3588-C（Android）User Profile\\Android\\Program\\rknpu.tar.bz2</font>

Here is an example of rknn\_ssd\_demo\_Android to test the NPU:

Open the window comman

![Image](./images/OK3588-C_Android_14_User_Manual/1718940893935_f7351fdd_0e82_442f_ab6d_84dc62db9359.png)

Enter the following command to upload the test routine to the development board file system.

```bash
adb root
adb push rknpu.tar.bz2 /data/
adb shell
cd /data
tar xvf rknpu.tar.bz2
```

Then enter the following command to test

```bash
cd /data/rknpu/rknn_ssd_demo_Android/
```

![Image](./images/OK3588-C_Android_14_User_Manual/1718940894132_c7ac7a67_6640_4ce2_9eec_dd85b4e6c555.png)

Run the rknn\_ssd\_demo as follows:

```bash
chmod +x rknn_ssd_demo
export LD_LIBRARY_PATH=./lib
./rknn_ssd_demo model/RK3588/ssd_inception_v2.rknn  model/bus.jpg
```

![Image](./images/OK3588-C_Android_14_User_Manual/1718940894371_6077686f_ea34_4567_90f0_259e45da8491.png)

Pull the out.jpg file from the current directory to any directory in the window via adb.

```bash
adb pull /data/rknpu/rknn_ssd_demo_Android/out.jpg .
```

![Image](./images/OK3588-C_Android_14_User_Manual/1718940894640_443f6f8b_5734_4446_a35c_bf069deb0270.png)

Open the out. jpg file by using the diagram viewing software

![Image](./images/OK3588-C_Android_14_User_Manual/1718940894882_665bd85f_1852_4f73_bdbb_dd869f4fc2c4.jpeg)

### **3.30 Hdmi In Test**

OK3588 Hdmi rx supports resolutions up to 3840x2160 @ P60 and 4096x2160p @ P24.

After inserting the HDMI cable, open ![Image](./images/OK3588-C_Android_14_User_Manual/1756801260554_57607286_b35d_4148_b7b4_83b9783dd6b2.png)in the application interface.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940898672_b2e998b1_b399_4957_a994_8c2f4c697959.png)

#### **3.30.1 SERIAL PORT DEMO**

Click "SERIAL PORT DEMO" "to enter the serial port test interface.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940899411_9a683cb7_f4e0_45c1_9e1d_46a9c85b20c0.png)

Device: Select the serial port to be tested.

Baud Rate: Select the baud rate of the serial port.

Data Bits: Specify serial port data bits.

Data Bits: Specify serial port stop bits.

Connect TX, RX of the corresponding uart4 serial port on the OK3588 development board (pin positions as shown in Figure 1 3.19 Section).

![Image](./images/OK3588-C_Android_14_User_Manual/1718940899631_743e93ef_0fe2_4036_af35_1713befebc7c.png)

After setting the above contents, click the OPEN button to start the test

Display the set serial port information in the Status column.

Add the content to be sent in the Received Data column, and click SEND to send data.

Send data will be received in the Send Data column. Click CLEAR to clear the received data in the Send Data column.

#### **3.30.2 SPI DEMO**

Click "SPI DEMO" "to enter the SPI test interface (no SPI test interface is reserved on the 3588 board).

![Image](./images/OK3588-C_Android_14_User_Manual/1718940899840_5a011ab3_8b1c_4372_a51a_03836183df80.png)

Device: Specifiy the SPI to use.

SPI Mode: Specify one of the four modes.

Bit order: Specify one of 1 (LSB), 0 (MSB).

Bits: Specifiy the number of bits in the data.

Speed: Specify the transmission rate in the range of 10-1000000.

After the above is set, click OPEN to start the test. Connect the miso and mosi pins of the selected spi on the OK3588.

Enter the data to be sent in the Sent Data field and receive the sent data in the Received Data field.

#### **3.30.3 I2C DEMO**

Click "I2C DEMO" to enter the i2c test interface.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940900082_d90ab4f2_7b36_4b97_a517_a59eb1608827.png)

The RTC chip is connected to the I2C, and clicking the READ button will read the time in the RTC register.

Fill in the time in the columns of Year, Hour, Minute, and Second, and click the WRITE button to write the data into the corresponding registers of the RTC.

#### **3.30.4 GPIO DEMO**

Click GPIO DEMO “ to enter the gpio test interface.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940900309_52fcb0e8_fb8a_48ed_80e4_1594fefe072b.png)

The formula in the upper right corner of the above figure, is the method of calculating the gpio serial number.

Select GPIO in the drop-down bar, click the GET button, and get the high level 1 or low level 0 in the GPIO Value bar.

Enter a 1 or 0 in the GPIO Value field and click the SET button to set the GPIO output high or low specified in the drop-down field.

#### **3.30.5 WATCHDOG DEMO**

Click "WATCHDOG DEMO" to enter the Watchdog test interface.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940900617_3aa59fb4_4ec0_4ee4_a6d1_bfc8ebe91eb7.png)

Clicking the START button will start the watchdog and start a 15-second countdown, when the countdown reaches 0, the device will reboot.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940900835_c3a0c1bb_f7b4_4bb7_93bf_83d63ab4e1e4.png)

Turning on Auto Feed will enable automatic dog feeding; clicking on MANUAL FEED "will manually feed the watchdog once. Clicking the STOP button will stop the watchdog.

#### **3.30.6 ADC DEMO**

Click "ADC DEMO" to enter the adc test interface.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940901069_79a3afeb_c798_41df_8c30_e0218a599118.png)

Click IN\_VOLTAGE0\_RAW to select the ADC channel, click the START button to start the test, the ADC value will be displayed in the "ADCValue" column.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940901258_7cb44e9d_5cde_4cd6_b315_a414471d640e.png)

Click "STOP" to stop the test:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940901484_88732f5f_4d80_458e_b1f9_9d871702a54b.png)

## 4\. System Flashing

### **4.1 OTG System Flashing**

#### **4.1.1 OTG Driver Installation**

️Path: Software Data \\ 3-Tools\\DriverAssitant\_v5.13.zip

Extract the above path file to any directory and run it with administrator privileges

Open DriverInstall.exe.

![Image](./images/OK3588-C_Android_14_User_Manual/1756801262304_8cca6218_f872_448e_b0b0_a811a681522c.png)

Click "Driver Installation”.

![Image](./images/OK3588-C_Android_14_User_Manual/1756801262382_6b678a97_02ac_4d71_b355_d7fac17cd6db.png)

#### **4.1.2 OTG Flashing Test**

**4.1.2.1 RKDevTool Flashing Test**

Path: 3-Tools \\ RKDevTool\_v3.30\_for\_window.zip

It is a development tool provided by Rockchip Micro. Unzip it to a full English path before use, connect the Typc0 port of the development board and the host computer with a Type-C cable, press and hold the recovery key of the development board and don't release it, then press the reset key to reset the system, and release the recovery key after about two seconds. There will be prompts on the Rockchip development tool : loader device found

**Note: The operation to recognize the device is that the recovery button should be in the pressed state when the development board is powered on.**

**Theoretically, Rockchip development tools have no requirements for the unzip directory. However, some users have feedback that the unzip directory should be in full English. If the tool doesn't match the following figure, please consider unzipping it in an English directory.**

Open the Rockchip development tool:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940926455_346fca05_9187_4e68_b8be_e67d9a7aeb31.png)

Click the "Upgrade Firmware" tab, click the "Firmware" button to select the full upgrade image update.img. The program will be parsing the firmware, so wait a while.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940926673_2fa1ff40_e5be_48cc_b1ef_ca3d9a0f1d8d.png)

Click the "Upgrade" button to upgrade.

**Introduction to MASKROM mode**

If the loader is damaged and cannot enter the Loader mode, press and hold the red Maskrom key and then press the reset key to enter the maskrom mode for flashing.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940926916_f54eb5f4_ae39_4746_9bae_43ddac2c3111.png)

At this time, the system will prompt the discovery of a maskrom device. The flashing process is consistent with the loader mode, so it is best to use an update.img burning.

**Note: Don't click "Device Partition Table" in maskrom mode, it is invalid. A separate burn in maskrom mode will not clear the UBOOT environment variables.**

**Introduction to Downloading the Individual Image Function**

This feature is useful when you need to download a separate image. This function is only applicable in loader flashing mode.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940927185_50def76d_2f52_47e6_981b_3c8db6a66864.png)

1. Click ① Download image tab;
2. Click ② Device partition table to read the mirror partition location;
3. Click the ③ check box to select the image to be flashed separately;
4. Click ④Here to select a image;
5. Click ⑤ to execute for flashing;
6. Restart after flashing.

**4.1.2.2 Factory Tool Flashing Test**

Factory Tool is a factory batch OTG flashing tool, which does not need to read the image and supports large file flashing. Use this tool if RKDevTool is not compatible. Before use, you need to decompress to the full English path, connect the development board to the host, press the recovery key, press the reset key to reset, and release the recovery key after two seconds. There will be prompts on the Rockchip development tool : loader device found

**Note: The operation to recognize the device is that the recovery button should be in the pressed state when the development board is powered on.**

**Theoretically, Rockchip development tools have no requirements for the unzip directory. However, some users have feedback that the unzip directory should be in full English. If the tool doesn't match the following figure, please consider unzipping it in an English directory.**

Open the Rockchip development tool:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940927449_52d6de41_ce5e_43a6_9007_76cd8dd857af.png)

Click to select the firmware, and click to start. At this time to recognize the loader device will automatically start burning.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940927753_f00a4e70_f91f_4895_9c83_67d6b22e3ac3.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940928070_85202ada_f163_448f_b3dc_e85253b5ee1d.png)

### **4.2 TF Card Flashing**

TF card production, flashing and testing

**Note: The tested TF card capacity is up to 16G, using 32G and above TF card may fail to flash.**

Copy the SDDisk Tool \_ v1.78.zip from the 3-tools directory to any windows directory. Run SD\_Firmware\_Tool.exe with administrator privileges.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940928423_15e9601c_a5af_4cce_b4a3_ee97d01478cf.png)

Select the disk device, check "Firmware Upgrade" and select update.img. Click Start Creating.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940928624_eafd6d6b_d06b_40d3_ab18_5893b25153ff.png)

![Image](./images/OK3588-C_Android_14_User_Manual/1718940928812_649ac8d5_5fe7_4939_9c18_f23d48098a4d.png)

Insert the TF card into the development board and start, the system will automatically enter the flashing process. When the flashing is complete, both the screen and the serial port will prompt:

Please remove SD CARD!!!, wait for reboot.

At this time, pull out the TF card, the system automatically restarts (please do not power down directly).

During mass production, check the flashing status by SoM heartbeat light.  Heartbeat light modes are as follows:

1. Kernel startup phase: Heartbeat light mode, regular intermittent flashes;
2. Flashing preparation phase: EMMC indicator light, off;
3. Flashing in progress phase: EMMC indicator light, on;
4. Flashing completion phase: Heartbeat light mode, regular intermittent flashes.

Serial port information during the burning process:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940929006_7048b010_3721_4a3c_894e_04e2bd2ae674.png)

If the automatic restart does not occur after removing the TF card, a manual restart can also complete the burning. Please be patient during the burning process.

## 5\. System OTA upgrade Test

OTA (over the air) upgrade is a standard software upgrade method provided by Android system. It has powerful functions, and the current version of system OTA upgrade provides two methods of local complete package upgrade and network upgrade.

### **5.1 OTA Upgrade Package Compilation**

You can use the build.sh in the OK3588 - android14 - source directory to compile the full OTA upgrade package. Please modify the Android code first, and then compile the OK3588 system upgrade package:

```bash
forlinx@ubuntu20:~/OK3588-android14-source$ ./build.sh -KAuop
```

The directories of the generated files are rockdev/Image - ok3588\_c/ and IMAGE/OK3588\_C\_USERDEBUG\_OK3588 - C - ANDROID\_\_xxxxxxxxxx/IMAGES/.

Among them, ok3588\_c - ota - eng.root.zip is the full upgrade package, and ok3588\_c - target\_files - eng.root.zip is the incremental upgrade package.   
Rename either ok3588\_c - ota - eng.root.zip or ok3588\_c - target\_files - eng.root.zip to update.zip, and it can be used for a full OTA upgrade.

**Note: The full upgrade package contains the complete system, while the incremental upgrade package contains the differences between two versions. Therefore, you need to ensure that the development board has been flashed with the lower - version system before using the incremental upgrade to ensure a correct upgrade.**

### **5.2 OTA Local Upgrade**

Copy the update.zip generated in the previous section to the root directory of the USB or TF card, or the /data/media/0/ directory, the system will automatically detect the upgrade package and pop up the upgrade dialogue box.

The following is done in adb mode:

```bash
adb root
adb remount
adb push updata.zip /data/media/0/
```

After waiting for a while, the interface prompts whether to install the upgrade package window.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940987481_f2223664_f0ed_475e_998d_f428c7e2b1db.png)

Click "Installation”.

The debugging window prints the following information:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940988058_b6600e05_17e9_432f_a9da_6a20ad4dd171.png)

After that, it will automatically restart and enter the Recovery system to automatically complete the OTA package upgrade. At this time, it cannot be powered off and wait for the upgrade.

When completed, it will automatically restart to the main Android interface.

After the system restarts, a dialog box pops up on the interface to prompt congratulations on the success of the upgrade.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940988320_ee782346_fe3b_46ca_a2be_d170ee657211.png)

Click "Yes".

Finally, you can verify that the android system has been modified.

**Note: The prompt for firmware upgrade operation after the system reboot is the correct prompt because the file /data/media/0/update.zip exists, so it will wait for a few minutes to pop up the prompt. The Firmware Prompt dialog will not pop up after deleting the/data/media/0/update.zip.**

### **5.3 OTA Network Upgrade**

1\. Environment Setup

Edit the device/rockchip/rk3588/ok3588\_c/ok3588\_c.mk file and modify the server IP address through ro.vendor.ota.host.

![Image](./images/OK3588-C_Android_14_User_Manual/1756801263848_4a4f3b10_d5cc_4646_acfa_fb6172c9c5f3.png)

Execute ./build.sh -KAuop to compile the upgrade firmware.

The directories of the generated files are rockdev/Image-ok3588\_c/ and IMAGE/OK3588\_C\_USERDEBUG\_OK3588-C-ANDROID\_\_xxxxxxxxxx/IMAGES/.

Among them, ok3588\_c-ota-eng.root.zip is the full upgrade package, and ok3588\_c-target\_files-eng.root.zip is the incremental upgrade package.   
Rename either ok3588\_c - ota - eng.root.zip or ok3588\_c - target\_files - eng.root.zip to update.zip, and it can be used for a full OTA upgrade.

Extract apache-tomcat-7.0.29.tar.gz to PC Ubuntu home directory, copy update.zip to /home/forlinx/apache-tomcat-7.0.29/webapps/OtaUpdater/WEB-INF/packages/ ok3588\_c/1.0.0/1.0.1.zip.

Enable apache-tomcat.

```bash
cd /home/forlinx/apache-tomcat-7.0.29
./bin/startup.sh
```

Disable apache-tomcat.

```bash
./bin/shutdown.sh
```

2\. Network Upgrade Test

Connect network and power up OK3588 board, and the prompt dialog box will pop up to prompt system upgrading.

![Image](./images/OK3588-C_Android_14_User_Manual/152.png)

Click "Yes", the upgrade 1.0.1.zip file will be downloaded via http protocol.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940989332_9bba55e7_29ef_495d_a30c_0954b33d3f70.png)

![Image](./1718940987829_ba310991_112d_4158_8002_70e8b2f2f8d1-1758268600056-7.png)

The system will restart automatically, and the serial port terminal will print as follows:

![Image](./images/OK3588-C_Android_14_User_Manual/1718940989800_a5e943d3_bfd7_486e_b27d_d35c0637c225.png)

After this reboot, the android interface prompts that the upgrade is complete.

![Image](./images/OK3588-C_Android_14_User_Manual/1718940988320_ee782346_fe3b_46ca_a2be_d170ee657211.png)

Click “Yes”.

**Note: If prompted to upgrade again, click "No", because OK3588 can get the remote 1.0.1.zip upgrade package through the network, so it will remind you whether you need to upgrade or not.**

## 6\. Multi-display with Independent Touch Control

The multi-display with independent touch control function enables you to use the DisplayHwConfig app to set the main and secondary screens, the binding relationship between the display and VOP, the binding relationship between the display and touch (input) devices, customize the DPI settings, and display the app itself on different screens.

After the parameter settings are completed, restart the device for the settings to take effect.

The source code of the app is located in vendor/forlinx/DisplayHwConfig.

### **6.1 Primary and Secondary Screens Settings**

Click the “PRIMARY DISPLAY” button to specify the primary screen.

![Image](./images/OK3588-C_Android_14_User_Manual/1.png)

Select the display you want to set as the primary screen from the menu and click “OK”.

![Image](./images/OK3588-C_Android_14_User_Manual/2.png)

**Note: When setting the primary screen, make sure the selected display is bound to a VOP (Video Output Processor) and the relevant DTS (Device Tree Source) nodes are enabled. Otherwise, the Android system will indicate that the primary screen does not exist.**

The currently opened display device, excluding the primary screen, is the secondary screen. The configuration of secondary screens is adaptive and does not require manual settings.

### **6.2 Binding between Display and VOP Settings**

Click the non - “PRIMARY DISPLAY” button to set the binding relationship between supported displays and VOP.

![Image](./images/OK3588-C_Android_14_User_Manual/3.png)

Click the button to enter the VOP selection page, and click “OK” to save the changes.

![Image](./images/OK3588-C_Android_14_User_Manual/4.png)

**Note: The red text below shows the rules for binding VOP. Also, ensure that the same VOP is not bound to multiple devices.** 

### **6.3 Binding between Display and Touch (Input) Devices**

This function can dynamically bind the display and touch devices together to achieve the asynchronous touch function. 

![Image](./images/OK3588-C_Android_14_User_Manual/5.png)

The display information will be presented according to the binding relationship between the display and VOP. The drop - down menu shows the information of the current touch (input) devices. Select one and click “Save” to establish the binding relationship.

![Image](./images/OK3588-C_Android_14_User_Manual/6.png)

The displayed information will be presented according to the binding relationship between the display and VOP. The drop - down menu shows the information of the current touch (input) devices. Select one of them and click “Save” to establish the binding relationship.

The driver of the touch (input) device needs to support the phys parameter so that the app can obtain the information of the touch device.   
In the driver, the content of the phys parameter of the struct input\_dev structure needs to be added.   
You can refer to the following methods:

Add the input - phy attribute to the touch device node in the device tree and specify the content of phys.

```bash
ft5x06_dsi0: ft5x06@38 {
    compatible = "edt,edt-ft5406", "edt,edt-ft5x06";
    reg = <0x38>;
    pinctrl-names = "ft5x06_default";
    pinctrl-0 = <&ft5x06_dsi0_gpio>;
    interrupt-parent = <&gpio3>;
    interrupts = <RK_PC0 IRQ_TYPE_EDGE_FALLING>;
    // irq-gpio = <&gpio3 RK_PC0 GPIO_ACTIVE_HIGH>;
    // reset-gpio = <&gpio3 RK_PB7 GPIO_ACTIVE_HIGH>;
    touchscreen-size-x = <1024>;
    touchscreen-size-y = <600>;
    input-phy = "ft5x06_2_38/input0";
    status = "okay";
    };
```

Add the content to obtain input - phy and configure phys in the touch device driver.

```bash
    const char *location;
    // 'input-phy(location)' is a crucial parameter for binding touch and display in the Android layer and must exist.
    // It is essential to ensure that the 'input-phy(location)' is unique for each device.
    of_property_read_string(client->dev.of_node, "input-phy", &location);
    if (location) {
        input->phys = location;
    }
```

**Note: If you want to verify whether the multi - touch function is set correctly, each display device should display a different app, and then click on them respectively. You can also click the “Display on this screen” button to display the app on the specified screen and perform touch operations.**

### 6.4 DPI Custom Settings 

For the main displays with different resolutions and sizes, the display effects are different even with the same DPI. Therefore, a function to customize the system DPI is provided.

![Image](./images/OK3588-C_Android_14_User_Manual/7.png)

Enter the specified DPI value in the “Display DPI” input box, then click “Save”. The settings will take effect after restarting.

### **6.5 APP Display on Different Screens**

By clicking the “Display on this screen” button, the app can be displayed on different displays.

![Image](./images/OK3588-C_Android_14_User_Manual/8.png)

## 7\. Root Permission Management

Root permission management is located in the “ANDROID System Configuration” of the App DisplayHwConfig.

The source code of the app is located in vendor/forlinx/DisplayHwConfig.

Root permission management can control the shell, ADB, and apps separately or uniformly.

### **7.1 Shell Permission Control**

Select “Enable shell” to grant root permission to the shell.

![Image](./images/OK3588-C_Android_14_User_Manual/9.png)

When the root permission of the shell is enabled, executing su in the serial terminal can successfully obtain root permission.

When the root permission of the shell is disabled, executing su in the serial terminal will have the following behavior:

```bash
console:/ $ su
su: not allowed
```

### **7.2 ADB Permission Control**

Select “Enable ADB” to grant root permission to ADB.

![Image](./images/OK3588-C_Android_14_User_Manual/10.png)

When the root permission of ADB is enabled, executing adb root in the PC terminal can successfully obtain root permission.

When the root permission of ADB is disabled, executing adb root in the PC terminal will have the following behavior:

```bash
C:\Users\forlinx>adb root
adbd cannot run as root
```

### **7.3 APP Permission Control**

Select “Enable APP” to grant root permission to the app.

![Image](./images/OK3588-C_Android_14_User_Manual/11.png)

When the root permission of the app is enabled, opening RootCheck will show that the app root permission is enabled.

![Image](./images/OK3588-C_Android_14_User_Manual/12.png)

When the root permission of the app is disabled, opening RootCheck will show that the app root permission is disabled.

![Image](./images/OK3588-C_Android_14_User_Manual/13.png)

RootCheck is not pre - installed in the system and needs to be installed manually. The source code is in “Software materials\\2 - Images and source code\\2 - Test programs”.