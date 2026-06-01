# OK3576-C\_Android14.0\_User’s Manual_V1.0

Document classification: □ Top secret □ Secret □ Internal information ■ Open

## Copyright

The copyright of this manual belongs to Baoding Folinx Embedded Technology Co., Ltd. Without the written permission of our company, no organizations or individuals have the right to copy, distribute, or reproduce any part of this manual in any form, and violators will be held legally responsible.

Forlinx adheres to copyrights of all graphics and texts used in all publications in original or license-free forms.

The drivers and utilities used for the components are subject to the copyrights of the respective manufacturers. The license conditions of the respective manufacturer are to be adhered to. Related license expenses for the operating system and applications should be calculated/declared separately by the related party or its representatives.

## Overview

This manual is designed to help you quickly familiarize yourself with the product, and understand the interface functions and testing methods. It primarily covers the testing of interface functions on the development board, the methods for flashing images, and troubleshooting procedures for common issues encountered in use. During the testing process, some commands are annotated for easy understanding, focusing on practicality and sufficiency. Please refer to OK3576-C\_Android14 User’s Compilation Manual provided by Forlinx for kernel compilation, related application compilation methods, development environment construction, etc.

There are total five chapters:

+ Chapter 1. focuses on the overall overview of the product, and briefly introduces the development board in the interface resources, the relevant driver path in the kernel source code, and the description of the key parts;
+ Chapter 2. mainly focuses on the fast startup of the product, which can be achieved through two methods: serial port login and, as well as the relevant introduction of the U-Boot menu;
+ Chapter 3. Android function test；
+ Chapter 4. focuses on the product's image update, mainly describing the method of updating the image to the storage device, and users can choose the corresponding flashing method according to the actual situation.
+ Chapter 5. is mainly about the OTA upgrade test of the product system.

A description of some of the symbols and formats associated with this manual:

| **Format**| **Meaning**|
|:----------:|----------|
| **Note** | Note or information that requires special attention, be sure to read carefully|
| 📚 | Relevant notes on the test chapters|
| ️🛤️️️️ | Indicates the related path.|
| <font style="color:blue;background-color:#d7d7d7;">Blue on gray</font>| Refers to commands entered at the command line(Manual input required).|
| <font style="color:black;background-color:#d7d7d7;">Black font on gray background</font>| Serial port output message after entering a command|
| **<font style="color:black;background-color:#d7d7d7;">Bold black on gray background</font>**| Key information in the serial port output message|
| //| Interpretation of input instructions or output information|
| Username@Hostname| console: development board serial port login account information, through which the user can determine the environment for function operation.|

Example: Check the loading status of the NXP AW9098 module driver:

```plain
forlinx@ubuntu:~/3576$ ls                                  //List the files in this directory
OK3576-android-source  OK3576-android-source.tar.bz2
```

+ forlinx@ubuntu: the username is forlinx and the hostname is ubuntu, indicating that the operation is performed in the development environment ubuntu.
+ // : Interpretation of command operations or printed information without input.
+ <font style="color:blue;background-color:#e5e5e5;">ls</font>：Blue font on a gray background, indicating the relevant commands that need to be manually entered.
+ **<font style="background-color:#e5e5e5;">OK3576-android-source</font>**：The black font with gray background is the output information after the input command, and the bold font is the key information, which indicates that the NXP AW9098 module driver has been loaded.

## Application Scope

This manual is mainly applicable to the Android14 operating system on the Forlinx OK3576-C platform. Other platforms can also refer to it, but there will be differences between different platforms. Please make modifications according to the actual conditions.

## Materials Description

OK3576-C development board currently provides software documentation for the Android operating system. This document serves as a user manual for Android users and includes relevant functionality testing and explanations for the Android 11 kernel. Users should select the corresponding documentation that matches the image on the development board for their operations. Users can access the documentation and source code of the software and hardware through the web link provided by our company.

Please ask your sales representative for the download link.

**Note: OK3576-C development board is initially flashed with a Linux system at the factory. You need to re-flash the board with an Android image before performing operations.**

**Instructions for flashing the Android system can be found in the “System Flashing” Chapter. After flashing, you can view kernel version information using the steps outlined in the “Serial Port Login” section.**

**For detailed information, refer to the OK3576-C user manual. In this document, the directory where the user manual is located is taken as the root directory of the OK3576-C user manual.**

## Revision History

| **Date**| **Manual Version**| **SoM Version**| **Carrier Board Version**| **Revision History**|
|:----------:|:----------:|:----------:|:----------:|----------|
| 08/11/2024 | V1.0| V1.0| V1.0 and Above| OK3576-C_Android14_User's Manual Initial Version |

## 1\. OK3576 Development Board Description

### 1.1 OK3576 Development Board Description

RK3576 processor, based on ARM64 architecture, is known for its low power consumption and high performance. It integrates 4 Cortex-A53 and 4 Cortex-A72 cores, along with dedicated NEON co-processor and NPU for neural network processing. It's widely used in various fields such as computers, smartphones, and digital multimedia devices.

The connection between SoM and the carrier board is board-to-board.

**<font style="color:#DF2A3F;">When the 2GB OK3576-C runs the full Android 14 system, the remaining memory is less than 100MB. It is recommended that users tailor the system services according to the application scenarios, otherwise the memory may be insufficient.</font>**

**Note: Hardware parameters are no longer described in this software manual. Before referring to this manual for software development, please read the "OK3576-C Hardware Manual" (download in the same way as the software information) to understand the product naming rules and the hardware configuration information of the product you are using, which will help you to use this product.**

### 1.2 **Android14** System Software Resources Features

| **Device**| **Location of driver source code in the kernel**| **Device Name**
|----------|----------|----------
| LCD Backlight Driver| drivers/video/backlight/pwm\_bl.c| /sys/class/backlight
| USB Port| drivers/usb/storage/| 
| USB Mouse| drivers/hid/usbhid/| /dev/input/mice
| Ethernet| drivers/net/ethernet/stmicro/stmmac| 
| SD/micro TF card driver| drivers/mmc/host/dw\_mmc-rockchip.c| /dev/block/mmcblk1pX
| EMMC Driver| drivers/mmc/host/dw\_mmc-rockchip.c| /dev/block/mmcblk2pX
| OV13850| drivers/media/i2c/ov13850.c| /dev/videoX
| LCD Controller| drivers/gpu/drm/rockchip/rockchip\_drm\_vop.c| 
| MIPI CSI| drivers/phy/rockchip/phy-rockchip-mipi-rx.c| 
| MIPI DSI| drivers/phy/rockchip/phy-rockchip-inno-mipi-dphy.c| 
| LCD Touch Driver| drivers/input/touchscreen/gt9xx/\*drivers/input/touchscreen/edt-ft5x06.c| /dev/input/eventX
| RTC Real Time Clock Driver| drivers/rtc/rtc-rx8010.cdrivers/rtc/rtc-pcf8563.c| /dev/rtc0
| serial port| drivers/tty/serial/8250/8250\_dw.c| /dev/ttySX
| Key Driver| drivers/input/keyboard/adc-keys.c| /dev/input/eventX
| LED| drivers/leds/leds-gpio.c| 
| I2S| sound/soc/rockchip/rockchip\_i2s.c| 
| Audio Driver| sound/soc/codecs/rk817\_codec.c| /dev/snd/
| PMIC| drivers/mfd/rk808.c| 
| PCIE| drivers/pci/controller/pcie-rockchip.c| 
| Watchdog| drivers/watchdog/dw\_wdt.c| 
| SPI| drivers/spi/spi-rockchip.c| 
| PWM| drivers/video/backlight/pwm\_bl.c| 

### 1.3 EMMC Memory Partition Table

The following table is the eMMC memory partition information of Android operating system (the size of a block is 512bit when calculating):

| **Partition Index**| **Name**| **Offset / block**| **Size/block**| **Content**|
|----------|----------|----------|----------|----------|
| N/A| security| 0x00000000| 0x00004000| MiniLoaderAll.bin|
| 1| uboot| 0x00004000| 0x00002000| uboot.img|
| 2| misc| 0x00008000| 0x00002000| misc.img|
| 3| dtbo| 0x0000a000| 0x00002000| dtbo.img|
| 4| vbmeta| 0x0000c000| 0x00000800| vbmeta.img|
| 5| boot| 0x0000c800| 0x00020000| boot.img|
| 6| recovery| 0x0002c800| 0x00030000| recovery.img|
| 7| baseparameter| 0x001fcc00| 0x00000800| baseparameter.img|
| 8| super| 0x001fd400| | super.img|

## 2\. Fast Startup

### 2.1 Preparation Before Startup

OK3576 development board has two system login modes: Serial login and hardware preparation before system startup:

+ 12V2A or 12V3A DC Power Cable
+ Debugging Serial Cable (Serial Login Use)

The debug serial port on the development board is a Type-C socket, allowing users to connect the development board to a PC using a USB to Type-C cable to monitor the status of the development board.

### 2.2 Debugging Serial Driver Installation

OK3576 platform utilizes a Type-C interface for the debug serial port (labeled DEBUG on the baseboard). It features an on-board USB-to-UART chip, eliminating the need for customers to purchase a USB-to-serial debug tool. The setup is extremely simple and convenient, but requires installation of the serial port driver. Functions such as Adb and flashing are realized through the Type-C interface (carrier board screen printing TypeC), and OTG related drivers need to be installed.

Serial driver file 3-Tool \\ CP210x \_ Windows \_ Drivers. Zip.

OTG related driver "3-Tool \\ DriverAssitant \_ v5.13.zip"

### 2.3 Serial Login

#### 2.3.1 Serial Port Connection Settings

**Description:**

+ **Serial port terminal login user: serial port terminal automatically logs in root user without password;**
+ **Serial port settings: baud rate 115200, data bit 8, stop bit 1, no parity bit, no flow；**
+ **Hardware: Type-C cable for connecting PC to development board;**
+ **Software: Windows PC requires Super Terminal; choose a familiar serial terminal software.**

In the following, take the putty terminal software as an example to introduce the serial port login method:

Step 1: Connect the serial port number of the computer---check the serial port number from the device manager (Based on the port actually recognized by the computer ).

![Image](./images/OK3576-C_Android_14_User_Manual/1726214204730_e2277f30_f460_4c2b_8965_b807e4ac62ef.png)

Step 2: Open and set up putty, then set the“ line according to the COM port of the computer used, baud rate 115200.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793550889_bac1185f_f1dd_415f_b4bf_d93afae08225.png)

Step 3: After the setting, input the COM port used by the computer in Saved Sessions. The following figure takes COM24 as an example, save the settings, open the serial port again later, and click on the saved port number.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793550972_3992b27b_5d24_4265_a91d_09ea3caae604.png)

#### 2.3.2 Serial Login

After the terminal software on the PC side is set, connect the PC and the development board through the serial port cable, and power on after connecting the power supply. The startup information can be seen through the terminal software.

### 2.4  **Uboot Menu**

OK3576's uboot menu switches between supported screens without the need to recompile and flash the screen.

#### 2.4.1 Display Output of Uboot Menu Dynamic Control

During the startup of uboot, press the space button at the serial port terminal to pop up the control options:

```plain
Hit key to stop autoboot('SPACE'):  0
---------------------------------------------
0:Exit to console
1:Reboot
2:Display type
---------------------------------------------
```

Enter 2 at the terminal to access the Screen Control sub-menu:

```plain
---------------------------------------------
vp0>hdmi vp1>mipi vp2=>dp0
Select  display
0:Exit
1:vp0 display: hdmi
2:vp1 display: mipi
3:vp2 display: dp0
4:primary display: DSI
5:display density: 170
---------------------------------------------
```

Inputs 1, 2, and 3 control the switching of HDMI, MIPI, and DP screens respectively, and a menu option of off means that the display output of the current item is turned off.

Enter 4 to select the main screen. The corresponding main screen should be selected according to the actual product. The default is DSI, i.e. mipi screen.

Input 5 to set the dpi. Multiple screens are displayed at the same time. The dpi of all screen display contents is based on the main screen. Please refer to [https://www.zelyo.cn/tools/Pixelcal/Pixelcal.html  ](https://www.zelyo.cn/tools/Pixelcal/Pixelcal.html)for dpi caculation[.](https://www.zelyo.cn/tools/Pixelcal/Pixelcal.html)

For example, to switch off the DP display, simply press 3

Enter 2 at the terminal to access the Screen Control sub-menu:

```plain
---------------------------------------------
vp0>hdmi vp1>mipi vp2=>off
Select  display
0:Exit
1:vp0 display hdmi
2:vp1 display mipi
3:vp2 display off         # dp displays the output is closed
4:primary display: DSI
5:display density: 170
---------------------------------------------
```

### 2.5 System Shutdown

In general, the power can be turned off directly, if there is data storage, function use and other operations, do not arbitrarily disconnect the power during the operation, in order to prevent irreversible damage to the file, you can only re-burn the firmware. To ensure that data is not completely written, enter the sync command to complete data synchronization before turning off the power.

Turn off the Android system, press the "PWRON" and "V +" buttons at the same time, or press "PWRON" for a long time and click "Shut down".

Press and hold "PWRON" for 6 seconds to force power off.

**Note: For products designed based on the SoM, if there are scenarios where accidental power loss causes the system to shut down unexpectedly, measures such as adding power-loss protection can be incorporated into the design.**

## 3\. Android Function Use and Test

### 3.1 Main Interface Display

![Image](./images/OK3576-C_Android_14_User_Manual/1730793552561_c48281ee_e47d_4c7f_b609_48790a594bc9.png)

### 3.2 Application Drawer

Swipe up on the main screen to bring up the following screen.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793552677_75a59f28_f261_4f0c_8a82_1b52dee819df.png)

**Note: After software version updates, there may be minor differences, which do not represent the actual images for each subsequent version update and are provided for reference only.**

### 3.3 Language Settings

Open the "Settings" app in the application drawer interface and click "System".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793552868_417f92c1_4736_4a8d_ba47_e1ed36ce58a9.png)

Click "Language" to enter the language setting interface.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793552954_cf56ef45_9f32_4748_a692_4754a77700b6.png)

Here you can select the language you want to set.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793553046_a4d626e6_d765_463d_92b3_d132870d4fbd.png)

### 3.4 Picture and Audio View

Store the picture and video files to be viewed into the TF card, and insert the TF card into the development board.

Open the Gallery app in the App Drawer interface

Configure permissions:

![Image](./images/OK3576-C_Android_14_User_Manual/1730793553146_33879878_9e84_496a_ac86_253f6a4102b8.png)

![Image](./images/OK3576-C_Android_14_User_Manual/1730793553248_5e73bd9f_419a_42bf_8059_495dcae541cd.png)

### 3.5 Audio Test

Store the audio file to be played into the TF card, and insert the TF card into the development board.

Open the Music app in the App Drawer interface.

Click "Song" in the interface to enter the song list interface.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793553329_b6dad9e4_c883_4380_a34a_eb8258e0b300.png)

Click Play Music to enter the play interface.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793553406_e7ede4f5_3bfc_4622_a85d_e25ba6ba5bbf.png)

The volume can be adjusted by pressing the physical buttons VOL + and VOL- on the carrier board of the board.

### 3.6 Recording (Mic input Support)

Open the Recorder app in the App Drawer interface.

Click the round button to start recording: 

**Note: the pointer will swing according to the sound level during normal recording.**

![Image](./images/OK3576-C_Android_14_User_Manual/1730793553485_b0c67714_47e7_49c5_b143_b4bd61998220.png)

Click the "square button" to stop recording, and finally click the "save" button to save.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793553585_255b9924_53ca_4385_a677_f57c4a914fa7.png)

Click the "![Image](./images/OK3576-C_Android_14_User_Manual/1730793553665_5074b3ec_8add_4e87_9fd8_afd11a911166.jpg)" button below to display the previously recorded audio file.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793553748_afa445dd_80dc_4b5b_abfb_979684bf1433.png)

Click on the audio file you want to play, and the recording will start playing.

### 3.7 Volume Adjustment

Open the "Settings" app in the application drawer interface, and click "Tone and Vibration" to enter the volume setting interface.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793553821_b6088547_e46a_4b58_b651_b15473fd8d50.png)

This interface allows you to adjust each section's volume and supports media volume adjustment using the physical buttons VOL- and VOL+ on the carrier board.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793553979_a43c885d_5372_4b9d_a925_ca4b454bdc38.png)

### 3.8 Display Settings

Open the "Settings" app in the application drawer interface, and click "Display" to enter the display settings interface.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793554081_74b123f7_8fb5_4e9c_968a_0d6201bd4a3f.png)

Click "brightness" to adjust the brightness of mipi screen.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793554155_82dbcca5_6cb7_4b31_a082_addf98e4a375.png)

The default setting of OK3576 is to never turn off the screen. If you need to turn off the screen automatically, please click the "Screen timeout" option and select the time.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793554235_de014591_cbe9_4910_bf8b_7b2949b70497.png)

If there is no operation on the interface within the set timeout period, the screen will enter the sleep mode. Short press of the "PWRON" button on the carrier board will wake up the screen.

### 3.9 Time Settings（RTC）

Open the "Settings" app in the application drawer interface and click "System".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793554426_00ddef62_bf53_4eda_8a8e_8fe2daa8af9c.png)

Click on “Date \&Time.”

![Image](./images/OK3576-C_Android_14_User_Manual/1730793554530_2dfa19ed_41a8_4bd6_8e64_8c8300b20d13.png)

Turn off Auto Time to use the RTC time, where the date and time can be changed and the time can be synchronized after you power down (make sure you have a coin battery installed).

![Image](./images/OK3576-C_Android_14_User_Manual/1730793554621_3ed5f4c2_21f3_4b0e_a837_11cfdba84e05.png)

### 3.10 Ethernet Test

OK3576 has 2 x Gigabit NIC (Ethernet ETH0 and Ethernet ETH1) on board, which can be expanded by pcie.

**Note: Network priority: Ethernet > wifi > mobile network**

After inserting the network cable, open the "Settings" app in the application drawer interface and click "Network and Internet".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793554699_89b780a1_0d97_4931_9ad6_030e437ff67d.png)

Click "Ethernet":

![Image](./images/OK3576-C_Android_14_User_Manual/1730793554820_d030f45d_04f5_4f82_aa2d_0ac146ee1c00.png)

The default method for obtaining an IP address is “dhcp.”

If you want to set a static IP address, click "EthernetIp mode" "and select" static "to set a static IP address. Only IPV4 is supported.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793554894_bea8217c_d889_4396_acc1_04abaac94511.png)

Click CONNECT to complete the configuration:

After successful connection, open the "Lightning" app in the app drawer interface.

Test the network by entering the [www.forlinx.net](http://www.forlinx.com进行网络测试) in the address bar.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793554973_6db0f40e_ace8_47c3_a7e8_b7b1099c215d.png)

### 3.11 WiFi Test

**Note: Network priority: Ethernet > wifi > mobile network. Unplug the network cable when testing the WiFi.**

Open the "Settings" app in the app drawer and click "Network and Internet".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793555074_f748f1d9_5a9d_47be_bb7a_79b091bf30e2.png)

Click on "Internet".

Turn on the "WLAN" switch, select ssid, and enter the password.

After successful connection, open the "Lightning" app in the app drawer interface.

Test the network by entering the [www.forlinx.net ](http://www.forlinx.com进行网络测试)in the address bar

![Image](./images/OK3576-C_Android_14_User_Manual/1730793555352_4d5c70d8_6492_41aa_a159_f6d31f3407e6.png)

### 3.12 WiFi Hotspot Test

OK3576 supports the sharing of Ethernet or mobile networks through WIFI for WIFI hotspot testing. First, connect the network cable to ensure that the Ethernet can be connected normally.

Open the "Settings" app in the app drawer and click "Network and Internet".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793555438_b7431df0_34f1_4a00_b3df_55f4ecfd20ed.png)

Click "Hotspot \&tethering":

![Image](./images/OK3576-C_Android_14_User_Manual/1730793555529_55b79eac_ff36_4eeb_9794_affd6c390ef7.png)

Click WLAN Hotspot:

![Image](./images/OK3576-C_Android_14_User_Manual/1730793555674_277cb8d6_c054_4641_816d_066ae556ad04.png)

Enable the WLAN hotspot and set the hot spot name and password:

![Image](./images/OK3576-C_Android_14_User_Manual/1730793555792_730b98ba_cec5_4392_8941_22e1e9d137df.png)

After connecting to the hotspot through the mobile phone, you can surf the Internet normally.

### 3.13 4G/5G Module Test

**Note: Network priority: Ethernet > wifi > mobile network. When using the 4G module, dial the S2 to ON.**

The OK3576 carrier board supports 4G modules (EM05) and 5G modules (RM500U). Before the test, please power off the development board, connect the 4G/5G module and insert the SIM card (pay attention to the direction of the SIM card), and start the development board.

Open the "Settings" app in the app drawer and click "Network and Internet".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793555884_d0c647ac_2c88_436f_8c91_d9b30b98c50c.png)

Now you can see that you have successfully connected to China Unicom.

After successful connection, open the "Lighting" app in the app drawer interface.

Test the network by entering the [www.forlinx.net](http://www.forlinx.com进行网络测试) in the address bar.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793556086_75ea80b2_0bef_4754_be83_1ac9d07aeaba.png)

### 3.14 Bluetooth Test

**Description: The current system does not support iPhone Bluetooth connection.**

The WiFi \& Bluetooth integrated module is used in the Bluetooth function test of OK3576 platform, which supports the connection of Bluetooth devices as the main device.

Use the Bluetooth mouse to test, and the test method is as follows:

Open the "Settings" app in the app drawer interface and click "Connected Devices".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793556196_80eaf4e4_b491_4d45_b69a_281bc5dadc6c.png)

Tap "Pair with new device" and turn on Bluetooth mouse pairing mode.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793556289_f28501f0_7db8_420e_97b8_01a3af1b402d.png)

Click the device corresponding to the Bluetooth mouse.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793556381_a8e67080_26e8_4a4c_b43f_b3512f2ac180.png)

Click "Match".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793556490_82474c46_38de_4c75_9e22_b7838e5e8693.png)

Successful connection, mouse pointer appears on desktop.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793556617_5622736c_6a8d_4a3d_abf4_92bd78489c87.png)

### 3.15 Key Test (Sleep Wake-up)

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

The default factory setting is no automatic hibernation. At this time, press the PWRON key lightly to turn off the screen and enter the hibernation state (note that the carrier board cannot be inserted into a wake-up source such as USBOTG, cpu4-7 is turned off, and cpu0-3 is still working). The hibernation print information is as follows:

```plain
console:/ # [  561.621862][  T179] edt_ft5x06 2-0038: Unable to fetch data, error: -6
[  561.631701][  T322] rockchip-vop2 27d00000.vop: [drm:vop2_crtc_atomic_disable] Crtc atomic disable vp1
[  561.687288][  T322] [WLAN_RFKILL]: wlan_early_suspend :enter
[  561.694304][  T164] psci: CPU4 killed (polled 4 ms)
[  561.709159][  T164] psci: CPU5 killed (polled 0 ms)
[  561.718567][  T164] psci: CPU6 killed (polled 0 ms)
[  561.734553][  T164] psci: CPU7 killed (polled 0 ms)
```

At this time, cpu0-3 is still working, and cpu4-7 is closed.

```plain
console:/ # cat /sys/devices/system/cpu/online
0-3
console:/ # cat /sys/devices/system/cpu/offline
4-7
console:/ #
```

In the sleep state, press the PWRON key again to wake up the CPU. Press and hold PWRON to shut down the device

The other buttons have simpler functions, so please test them yourself.

### 3.16 TF Card and USB Storage Test

This test is a test of TF card and USB storage device. The following steps take TF card as an example.

Open the "Settings" app in the application drawer interface and click "Storage" to view the internal storage device and the inserted storage device:

![Image](./images/OK3576-C_Android_14_User_Manual/1730793556715_3ea077b9_1d4f_498e_a4bb_27f8317e892c.png)

Select TF card.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793556828_69dd204e_f5a7_48c2_ab82_04d7d9478483.png)

Click the “File” to manage the files:

![Image](./images/OK3576-C_Android_14_User_Manual/1730793556923_038df4b5_3781_4d78_9ee4_25874caabec8.png)

![Image](./images/OK3576-C_Android_14_User_Manual/1730793557028_cf70e90f_3edc_4ddd_b2dd_6bf298d2851e.png)

### 3.17 USB Mouse Test

After the system is running, insert the USB mouse on the USB host, you will see the mouse pointer in the interface, and you can operate the Android system through the mouse.

### 3.18 USB OTG Interface Test

The OK3576 development board supports USB OTG functionality.

The Typec of the development board is connected to the computer, and the computer will recognize the board as follows:

![Image](./images/OK3576-C_Android_14_User_Manual/1730793557249_c60e9a9f_4c67_43d4_bdae_0e2bed42fb31.jpg)

Open the "Settings" app in the app drawer interface and click "Connected Devices".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793557249_c60e9a9f_4c67_43d4_bdae_0e2bed42fb31.png)

Click “USB“.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793556196_80eaf4e4_b491_4d45_b69a_281bc5dadc6c.png)

Click "File Transfer".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793557669_0b94ea97_8387_412a_a1e7_602ddf166380.png)

Open “This PC” on your computer, and you will see “ok3576\_c”. This allows file transfer via the computer.

### **3.19 Serial Port Test**

OK3576 platform carrier board schematic indicates the breakout of UART0, UART4, UART5, UART6, and UART8, totaling 5 serial ports. Among them, UART0 is the debug port, UART4 is the Bluetooth port, UART5 and UART6 are 485 ports, and UART8 is a TTL port.

| **UART**| **Device Nodes**| **Description**
|----------|----------|----------
| UART0| | Debugging serial port cannot be used directly for this test.
| UART4| /dev/ttyS4| It is used for Bluetooth and is not separately pinned out and can’t be directly used for this test.
| UART5| /dev/ttyS5| RS485
| UART6| /dev/ttyS6| RS485
| UART8| /dev/ttyS8| TTL

Testing will use two RS485 ports, UART5 and UART6. Before testing, ensure proper connection of the two RS485 interfaces: connect A to A and B to B. The two RS485 carrier board interfaces are as follows:

![Image](./images/OK3576-C_Android_14_User_Manual/1730793557922_bdf0e3c7_4cef_4dad_9f6d_73e85b69a974.jpg)

Open the "SerialPortTest" app "in the application drawer and click the" Setup "button

Set Device to ttyS5.

Set the Baud rate "to 115200.

Set Display format "to char.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793558062_b3253ec7_5dbc_4645_9b74_1ffd9a42fe33.png)

Click the "CONSOLE" option in the previous menu to perform the send-receive test:

Open ttyS6 in the command line terminal to send data;

```plain
console:/ # stty -F /dev/ttyS6 raw speed 115200
115200
console:/ # echo 123 > /dev/ttyS6
console:/ #
```

At this time, app receives data from ttyS6, as shown in the figure;

Open ttyS6 in the command line terminal to receive data;

```plain
console:/ # stty -F /dev/ttyS6 raw speed 115200
115200
console:/ # cat /dev/ttyS6
```

Enter the data to be sent in the Emission textbox in the app, and click Send, as shown in the figure below;

![Image](./images/OK3576-C_Android_14_User_Manual/1730793558266_d022d091_083d_4a92_bb96_02256f7c8787.png)

Data from ttyS5 can be received in the command line terminal.

```plain
console:/ # stty -F /dev/ttyS6 raw speed 115200
115200
console:/ # cat /dev/ttyS6
qwer
```

### 3.20 Camera Test

Currently supports OV13855 (connects to CAM1 interface), OV5645 (connects to CAM2, CAM3, CAM4, CAM5), UVC camera (connects to USB interface).

Open the "Camera" app in the application drawer interface and configure the relevant permissions.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793558435_e5053d8e_988c_4016_9241_5f6656c1c1da.png)

Preview Interface.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793558539_f3e19655_c103_4fac_af2d_80d0957cbf93.png)

The preview interface slides to the right, and you can choose to take photos or videos.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793558648_f1d5a294_f094_48f8_85c6_46059f13a9df.png)

Slide left in the preview interface and click the first icon "![Image](./images/OK3576-C_Android_14_User_Manual/1730793558787_2554f9e2_5f7e_4bb1_a655_a82b4d14ac6f.jpg)" to switch cameras (this camera app only supports two cameras).

![Image](./images/OK3576-C_Android_14_User_Manual/1730793558870_3b802f26_7610_4e5f_97cf_59fa25690afc.png)

Open the "MultipleCamera" app "in the application drawer interface to display multiple camera images (640 \* 480) at the same time.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793558952_69756fa3_4fb1_4d50_bc6b_83a2b92701c5.png)

### 3.21 HDMI \& eDP Resolution Setting Test

OK3576 platform supports dynamic setting of HDMI resolution.

OK3576's CPU supports 3 Video Ports, where vp0 supports up to 4K@120Hz 10bit to HDMI, vp1 supports up to 2560x1600@60Hz 10bit to DSI (mipi screen), and vp3 supports up to 1920x1080@60Hz to eDP (TYPE-C). You can modify the video output interface of vp connection by modifying the device tree.

Open the "Settings" app in the app drawer and click "Display".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793559053_5cbce303_afc3_402a_a2af_0f5c23ad6d7c.png)

Click “HDMI“.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793559222_079b57bf_abec_4e08_a63c_72d3727f04dc.png)

You can set HDMI display related parameters here.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793559334_14816cdf_7983_4c11_b3d9_d85b9c11a777.png)

### 3.22 Factory Reset

The OK3576 platform supports restoring factory settings.

Open the "Settings" app in the application drawer interface and click "System".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793559460_b0463266_bbc4_4c6c_a10c_b444e1fafe97.png)

Click "Reset Options".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793559579_a278a245_4314_4060_9d60_c0a76b74a15d.png)

Select the data to be reset according to the actual situation, wait for OK3576 to restore the default factory settings, and do not power off during the process of restoring the factory settings.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793559703_46fea020_f43f_4ddd_8b8f_33a9a935c62f.png)

### 3.23 APK Installation With TF Card

Copy the APK file to the TF card and open the TF card directory in the File app according to the previous section.

Click on the APK file, the window will pop up, click on "Settings"

![Image](./images/OK3576-C_Android_14_User_Manual/1730793559837_b37e61f6_777d_45d6_b56a_1850df6384a2.png)

Allow apps from this source.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793560003_96b9ca87_69d2_4c9d_a35a_d0f849762361.png)

### 3.24 ROOT Permission Test

Open the "Settings" app in the app drawer interface and click "About Tablet”.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793560151_161a89d3_c264_46b9_9b37_ee6ed0c8ee32.png)

Click "Build" 7 times in a row.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793560294_35b28567_cd91_4a13_a2fb_631d16ac6ae3.png)

Return to the previous menu and click "System".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793560486_c2d6392d_ed5a_4823_b56b_adca9b606f29.png)

Click "Developer Options".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793560588_ac300f3b_dbdb_4d1e_8fce_e7fa0cbc4147.png)

Locate Root Authorization. 

This switch controls root privileges including the following:

1. Serial port interrupt su to get root permission;

2. ADB root to get root privileges;

3. System app to get root privileges.

Open the RootChecker "app in the application drawer to test whether system app can get root privileges.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793560946_7f89af88_5cba_4570_a7e8_f095581163a5.png)

### 3.25 Locking Screen Test

**Note: OK3576 does not lock the screen by default.**

Open "Settings" in the app drawer and click "Security \& Privacy".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793561092_c28be54f_8aaa_40aa_91be_bf9388de4d8f.png)

Click "Device Unlock".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793561289_be5887d6_f06a_4f8e_a0c5_01d26f3b52d2.png)

Tap "Screen Lock".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793561434_4b823bfb_7725_47f1_afdd_f0480dd3fdf2.png)

![Image](./images/OK3576-C_Android_14_User_Manual/1730793561629_ade5032a_3c87_48ce_84e2_a853fa496c5e.png)

### **3.26** CAN Test

OK3576-C has two can buses and supports CANFD.

Parameters related to can can be set in the "Settings" app or through the "can" app.

Open "Settings" in the application drawer and click "Network and Internet".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793561733_71af9355_d6e6_4b38_bab7_1e6350a37e60.png)

Click “CAN“.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793561992_ace50021_3eb8_4d1e_bdbd_f4e0f98c7bef.png)

Set the baud rate for can0 and can1.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793562256_d624c6b5_3fa7_4721_afcd_4845d2400587.png)

Short H and L of can0 and can1, respectively.

Open the "can" app in the app drawer.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793562535_8afacedf_d364_490d_9c46_5394844fc868.png)

Click "SETTING" to set can parameters, and then click "CAN \_ ON" to open can.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793562633_c11a7c5d_4cc9_4dfd_84c3_844cb7376d2d.png)

At this time, execute the cangen command (root permission is required) on the command line terminal to see the data in the app.

```plain
console:/ # cangen -vv -n 5 can1
  can1  720   [1]  50
  can1  3A9   [5]  F0 83 11 7A C0
  can1  497   [7]  6E 47 E2 7D F2 82 A1
  can1  58A   [8]  F4 52 01 19 37 A5 2B 18
  can1  778   [4]  0D 0D 59 32
```

![Image](./images/OK3576-C_Android_14_User_Manual/1730793562750_32937def_d743_49e2_a2bb_3c75af90b949.png)

Execute the candump command at the command line terminal, enter hexadecimal data in the text box below the app, and then click SEND to send. At this time, the data can be received at the command line terminal.

```plain
console:/ # candump can1
  can1  123   [8]  12 34 56 78 12 34 56 78
  can1  123   [8]  12 34 56 78 12 34 56 78
  can1  123   [8]  12 34 56 78 12 34 56 78
```

![Image](./images/OK3576-C_Android_14_User_Manual/1730793562859_28c0cad8_f596_4c23_823d_213b5debb926.png)

### **3.27 Watchdog Test**

Open the WatchdogTest "app in the Applications Drawer.

Set the timeout time, click “Start”to start the watchdog, and click “Feed” to feed the dog. If the dog is not fed within the timeout time, the development board will restart.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793562962_258a302b_bf83_4e89_b7c7_1885b9e6a5b2.png)

### **3.28 ADC Test**

Open "Settings" in the app drawer and click "Security \& Privacy".

![Image](./images/OK3576-C_Android_14_User_Manual/1730793563106_dfc810b1_5ec2_46ba_9345_444b90088861.png)

### **3.29 GPIO Test**

The gpio of OK3576-C is divided into CPU direct connection and extended IO.

CPU Direct IO is named as GPIOx \_ YZ (X = 0,1,2,3,4, y = A, B, C, D, Z = 0,1,2,3,4,5,6,7)

pin\_number=x\*32 + (y-‘A’)\*8 + z

The extended IO is named Pxy form (X = 0,1,2, y = 0,1,2,3,4,5,6,7)

pin\_number = 485 + x\*8 + y

e.g.:

GPIO1\_D5（CPU direct connect）

pin\_number = 1\*\_32 + (D-A) + 5 = 1\_32 + 3\*8 + 5 = 61

P12（Extended）

pin\_number = 485 + 1 \* 8 + 2 = 495

Open the GPIOTest "app in the application drawer, enter the calculated pin \_ number in the pin number text box, click Open to open the GPIO, and then you can read or set it to 1 and clear it to 0.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793563247_3b62d3f1_5699_489c_af01_f01f031a524e.png)

### **3.30 Uboot Menu**

Open the "UbootMenu" app "in the application drawer to set functions such as screen switch, home screen, dpi, etc.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793563343_8a230a4e_7984_4764_a55f_984bbeb80bf6.png)

### **3.31 Silent Installation**

Open the SilentInstallDemo "app in the applications drawer, click the install silent button to install silently "/storage/emulated/0/Android/data/com. forlinx. Silent InstallDemo/files/test. apk" APK needs to be placed in this location in advance. ". Users can modify the source code of SilentInstallDemo to achieve silent installation.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793563460_58994a8e_d898_4e77_9543_870228667bc2.png)

## 4\. System Flashing

### 4.1 OTG System Flashing

#### 4.1.1 **OTG Driver Installation**

Path: 3-Tools \\ DriverAssitant\_v5.13.zip

Extract the above path file to any directory and run it with administrator privileges.

Open DriverInstall.exe.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793565145_13d99d4d_bca0_44d3_9b22_b05b752be810.jpg)

Click "Driver Installation”.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793565272_f277f501_d995_4253_82ac_3d1de892f959.jpg)

#### **4.1.2** **OTG Flashing Test**

##### **4.1.2.1 RKDevTool Flashing Test**

Path: 3-Tools \\ RKDevTool\_v3.30\_for\_window.zip

It is a development tool provided by Rockchip Micro. Unzip it to a full English path before use, connect the Typc0 port of the development board and the host computer with a Type-C cable, press and hold the recovery key of the development board and don't release it, then press the reset key to reset the system, and release the recovery key after about two seconds. There will be prompts on the Rockchip development tool : loader device found

**Note: To recognize the device, the recovery button on the development board should be pressed down while the board is powered on. Theoretically, Rockchip development tools have no requirements for the unzip directory. However, some users have feedback that the unzip directory should be in full English. If the tool doesn't match the following figure, please consider unzipping it in an English directory.**

Open the Rockchip development tool:

![Image](./images/OK3576-C_Android_14_User_Manual/1750319091973_df49a9b7_0487_45bb_ae0f_e17c6d58fb45.png)

Click the "Upgrade Firmware" tab, click the "Firmware" button to select the full upgrade image update.img. The program will be parsing the firmware, so wait a while.

![Image](./images/OK3576-C_Android_14_User_Manual/1750319339986_e8e6060c_5e99_4928_a142_e56dfd22b0f1.png)

Click "Advanced Functions"-> "Erase All" to erase.

![Image](./images/OK3576-C_Android_14_User_Manual/1750319533424_f65d5c86_78e3_4a0d_849b_f8900eb94eb0.png)

Click the "Upgrade Firmware" button-> "Upgrade" to upgrade.

![Image](./images/OK3576-C_Android_14_User_Manual/1750319645988_ab89d472_d74b_4ef3_abdd_44fb5ac64af7.png)

**Introduction to MASKROM mode**

If the loader is damaged and cannot enter the Loader mode, press and hold the red Maskrom key and then press the reset key to enter the maskrom mode for flashing.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793565674_814ae2a1_322b_49dd_8151_58f580f1d35e.jpg)

At this time, the system will prompt the discovery of a maskrom device. The flashing process is consistent with the loader mode, so it is best to use an update.img burning.

**Note: Don't click "Device Partition Table" in maskrom mode, it is invalid. A separate flash in maskrom mode will not clear the UBOOT environment variables.**

**Introduction to Downloading the Individual Image Function**

This feature is useful when you need to download a separate image. This function is only applicable in loader flashing mode.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793565777_65cb8f3b_aada_4bd6_91d4_38456fe186bb.jpg)

1. Click ① Download image tab;
2. Click ② Device partition table to read the mirror partition location;
3. Click the ③ check box to select the image to be flashed separately;
4. Click ④Here to select a image;
5. Click ⑤ to execute for flashing;
6. Restart after flashing.

##### **4.1.2.2 Factory Tool Flashing Test**

Factory Tool is a factory batch OTG flashing tool, which does not need to read the image and supports large file flashing. Use this tool if RKDevTool is not compatible. Before use, you need to decompress to the full English path, connect the development board to the host, press the recovery key, press the reset key to reset, and release the recovery key after two seconds. There will be prompts on the Rockchip development tool : loader device found

![Image](./images/OK3576-C_Android_14_User_Manual/1730793565386_ec93e535_b051_4a3d_89c2_af3ca1099564.png) **Note: To recognize the device, the recovery button on the development board should be pressed down while the board is powered on. Theoretically, Rockchip development tools have no requirements for the unzip directory. However, some users have feedback that the unzip directory should be in full English. If the tool doesn't match the following figure, please consider unzipping it in an English directory.**

![Image](./images/OK3576-C_Android_14_User_Manual/1730793565887_ba93bf76_ce65_49a0_b472_406b9b8fa26f.jpg)

Click to select the firmware, and click to start. At this time to recognize the loader device will automatically start burning.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793565977_adf8b5b9_c6be_42c0_9237_14cf7e85c1a6.jpg)

![Image](./images/OK3576-C_Android_14_User_Manual/1730793566105_670d1d49_ec5c_429f_9af3_14f25b7f04c2.jpg)

### **4.2 TF Card Flashing**

TF card production, flashing and testing

**Note: The tested TF card capacity is up to 16G, using 32G and above TF card may fail to burn.**

Copy SDDiskTool\_v1.69.zip from the user profile tools directory to any directory on windows. Run SD\_Firmware\_Tool.exe with administrator privileges.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793566236_19af8aab_0628_448b_8870_655aef6d588f.jpg)

Select the disk device, check "Firmware Upgrade" and select update.img. Click Start Creating.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793566336_f58f3b06_c143_4143_8e2c_b333bf6f4c51.jpg)

![Image](./images/OK3576-C_Android_14_User_Manual/1730793566441_8e6d1f8d_5d7f_4a07_988a_c692f9b04116.jpg)

Insert the TF card into the development board and start, the system will automatically enter the flashing process. When the flashing is complete, both the screen and the serial port will prompt:

Please remove SD CARD!!!, wait for reboot.

At this time, pull out the TF card, the system automatically restarts (please do not power down directly).

During mass production, check the flashing status by SoM heartbeat light.  Heartbeat light modes are as follows:

1\. Kernel startup phase: heartbeat light mode, regular intermittent blinking;

2\. Flashing preparation phase: EMMC indicator (off);

3\. Flashing phase:EMMC indicator (on);

4\. Flashing completion phase: Regular intermittent blinking.

If the automatic restart does not occur after removing the TF card, a manual restart can also complete the burning. Please be patient during the burning process.

## 5\. System OTA Upgrade Test

OTA (over the air) upgrade is a standard software upgrade method provided by Android system. It has powerful functions, and the current version of system OTA upgrade provides two methods of local complete package upgrade and network upgrade.

OTA upgrade package is divided into full upgrade package and incremental upgrade package. The full upgrade package is the complete system, and the incremental upgrade package is the difference package of V2.0 system relative to V1.0 system, which requires the device system to be V1.0 to use this incremental package to upgrade to V2.0.

Refer to the “OK3576-C\_Android14\_User’s Compilation Manual” for compilation.

**<font style="color:#DF2A3F;">OK3576-C 2GB memory version may fail due to insufficient memory, it is recommended that users appropriately trim system services.</font>**

### **5.1 OTA Upgrade**

Copy the compiled upgrade package to the root directory of USB, TF card, or /storage/emulated/0 directory, the system will automatically detect it and pop up the upgrade dialog box.

The following is done in adb mode:

```plain
adb root
adb remount
adb push ok3576_c-ota-eng.root.zip /storage/emulated/0/update.zip
```

After uploading the upgrade package using ADB, it is necessary to restart the development board to trigger the system to detect the upgrade package.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793568208_703b6412_01c4_48c4_b33b_774c7c79d1f8.png)

Click "Installation”.

![Image](./1730793568347_35138ed0_9b5d_4ac1_bb52_230f851c2067.png)

The debugging window prints the following information:

![Image](./images/OK3576-C_Android_14_User_Manual/1730793568499_cd64dd67_8f70_4804_a9cc_fd572e141bd3.jpg)

After that, it will automatically restart and enter the Recovery system to automatically complete the OTA package upgrade. At this time, it cannot be powered off and wait for the upgrade.

When completed, it will automatically restart to the main Android interface.

After the system restarts, a dialog box pops up on the interface to prompt congratulations on the success of the upgrade.

![Image](./images/OK3576-C_Android_14_User_Manual/1730793568604_7d8daa3f_b9df_4cc8_ae55_a392366727f3.png)

Click "Yes".

Finally, you can verify that the android system has been modified.

**Note**: **After the system restarts, the prompt to perform a firmware upgrade is a normal prompt. Since the update.zip file exists, the system will pop up a prompt after waiting for a few minutes. After deleting the update.zip file, the firmware upgrade prompt dialog box will no longer appear.** 