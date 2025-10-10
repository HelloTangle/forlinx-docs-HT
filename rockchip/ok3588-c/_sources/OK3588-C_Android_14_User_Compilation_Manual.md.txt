# Android14.0\_User’s Compilation Manual\_V1.0

Document classification: □ Top secret □ Secret □ Internal information ■ Open

## Copyright Notice

The copyright of this manual belongs to Baoding Folinx Embedded Technology Co., Ltd. Without the written permission of our company, no organizations or individuals have the right to copy, distribute, or reproduce any part of this manual in any form, and violators will be held legally responsible.

Forlinx adheres to copyrights of all graphics and texts used in all publications in original or license-free forms.

The drivers and utilities used for the components are subject to the copyrights of the respective manufacturers. The license conditions of the respective manufacturer are to be adhered to. Related license expenses for the operating system and applications should be calculated/declared separately by the related party or its representatives.

## Overview

<font style="color:#333333;">This manual is designed to enable you to quickly understand the </font><font style="color:#333333;">compilation process</font><font style="color:#333333;">of the products and familiarize yourselves with the </font><font style="color:#333333;">compilation</font><font style="color:#333333;">methods </font><font style="color:#333333;">of</font> <font style="color:#333333;">Forlinx</font><font style="color:#333333;"> products. The application needs to be cross-compiled on an </font><font style="color:#333333;">ubuntu</font><font style="color:#333333;">host before it can run on the development board. </font>By following the methods provided in the compilation manual and performing practical operations, you will be able to successfully compile your own software code.

The manual will provide instructions for setting up the environment but there may be some unforeseen issues during the environment setup process. For beginners, it is recommended to use the pre-configured development environment provided by Forlinx. This will allow you to quickly get started and reduce development time.

Linux systems are typically installed in three ways: dual system on a real machine, single system on a real machine, and virtual machine. Different installation methods have their advantages and disadvantages. This manual only provides methods to build ubuntu in a virtual machine.

Hardware Requirements: It is recommended to have at least<font style="color:black;background-color:#ffffff;">16GB</font><font style="color:black;background-color:#ffffff;"> memory or above.It allows for allocating a sufficient memory to the virtual machine (recommended to allocate</font><font style="color:black;background-color:#ffffff;">10GB</font><font style="color:black;background-color:#ffffff;">or above), while still leaving enough resources for other operations on</font><font style="color:black;background-color:#ffffff;">Windows</font><font style="color:black;background-color:#ffffff;">. Insufficient memory allocation may result in slower performance on</font><font style="color:black;background-color:#ffffff;">Windows.</font>

The manual is mainly divided into five chapters:

+ Chapter 1. Virtual Machine software installation - introduction to downloading and installing Vmware software;
+ Chapter 2. provides the loading of the ubuntu system;
+ Chapter 3. Building, setting up, and installing necessary tools for the Ubuntu system and common issues in development environments;
+ Chapter 4. mainly focuses on the deployment and usage of Docker containers, kernel compilation, as well as Android-related source code;
+ Chapter 5. is the description of android application development.

A description of some of the symbols and formats in the manual:

| **Format**| **Meaning**|
|:----------:|----------|
| **Note** | Note or information that requires special attention, be sure to read carefully|
| 📚 | Relevant notes on the test chapters|
| ️️️🛤️ ️ | Indicates the related path.|
| <font style="color:blue;">Blue font on gray background</font>| Refers to commands entered at the command line(Manual input required).|
| <font style="color:black;">Black font</font>| Serial port output message after entering a command|
| **<font style="color:black;">Bold black</font>**| Key information in the serial port output message|
| //| Interpretation of input instructions or output information|
| Username@Hostname| forlinx @ ubuntu: Development environment ubuntu account information, which can be used to determine the environment in which the function operates.|

Example: Search the Docker-CE version:

```plain
forlinx@ubuntu:~$ apt-cache madison docker-ce                   //Find Docker-CE version
docker-ce | 18.06.3~ce~3-0~ubuntu | http://mirrors.aliyun.com/docker-ce/linux/ubuntu/trusty/stable amd64 Packages
```

+ forlinx@ubuntu: the username is forlinx and the hostname is ubuntu, indicating that the user forlinx is used on the development environment ubuntu for operations;
+ //：Explanation of the instruction, no input required;
+ apt-cache madison docker-ce：Blue font on a gray background, indicating the relevant commands that need to be manually entered;
+ **<font style="color:black;">docker-ce \| 18.06.3</font>**<sub>**<font style="color:black;">ce</font>**</sub>**<font style="color:black;">3-0~ubuntu </font>**: The black font with gray background is the output information after the input command, and the bold font is the key information.

## Application Scope

This manual is mainly applicable to the Android14.0 operating system on the Forlinx OK3588-C platform. Other platforms can also refer to it, but there will be differences between different platforms. Please make modifications according to the actual conditions.

## Revision History

| **Date**| **Manual Version**| **Revision History**|
|:----------:|:----------:|----------|
| 2025.09.01| V1.0| OK3588-C_Android14.0_User’s Compilation Manual Initial Version |

## 1\. VMware Virtual Machine Software Installation

<font style="color:#000000;">This chapter mainly introduces the installation of VMware virtual machine, and takes VMware workstation 16 Pro v16.2.3 as an example to show the installation and configuration process of the operating system.</font>

### <font style="color:#000000;">1.1 VMware Software Downloads and Purchase</font>

Go to the VMware website https://www.vmware.com/cn.html to download Workstation Pro and get the product key. VMware is a paid software that requires purchasing, or you can choose to use a trial version.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948545093_9dfd51bc_1a99_41bc_99b3_053234377703.png)

<font style="color:#000000;">After the download is complete, double-click the startup file to start the installer.</font>

### <font style="color:#000000;">1.2 VMware Software Installation</font>

<font style="color:#000000;">Double-click the startup program to enter the installation wizard, and click on "Next".</font>

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948545321_a8938217_413f_4f39_8728_e0bb2f11d936.png)

<font style="color:#000000;">Check I accept the terms in the license agreement and click "Next".</font>

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948545093_9dfd51bc_1a99_41bc_99b3_053234377703_1.png)

<font style="color:#000000;">Modify the installation location to the partition of your computer where the software is installed, and click "Next".</font>

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948545912_32ece1c4_38bb_4496_a961_be28f2b192f4.png)

<font style="color:#000000;">Uncheck and click on "Next".</font>

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948546191_989f0fb8_4b86_4527_ba8a_035475471f42.png)

<font style="color:#000000;">Check Add Shortcut and click "Next".</font>

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948546475_ae0e753a_3dfb_4551_8267_7e2f830ce5c1.png)

<font style="color:#000000;">Click "Install".</font>

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948546913_f2399faf_3dc1_4bcd_bc17_072f0e314be5.png)

<font style="color:#000000;">Wait for the installation to complete.</font>

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948546913_f2399faf_3dc1_4bcd_bc17_072f0e314be5.png)

<font style="color:#000000;">Click "Finish" to try it out. If users need to use it for a long time, they need to buy it from the official and fill in the license.</font>

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948547140_943cc6ed_c801_4dd3_9a0b_649bf99ce7cb.png)

## 2\. Loading the Existing Ubuntu Development Environment

**Note:**

+ **It is recommended for beginners to directly use the pre-built virtual machine environment provided by Forlinx, which already includes installed cross-compiler and Qt environment. After understanding this chapter, you can directly jump to the compilation chapter for further study;**
+ **The development environment provided for general users is: forlinx (username), forlinx (password);**
+ **Please ask your sales representative for the download link.**

There are two ways to use a virtual machine environment in VMware: one is to directly load an existing environment, and the other is to create a new environment. Let's first talk about how to load an existing environment.

First, download the development environment provided by Forlinx. In the development environment documentation, there should be an MD5 checksum file. After downloading the development environment, you should verify the integrity of the compressed package using the MD5 checksum. (You can use an on-line MD5 checksum tool or download a specific MD5 checksum tool for this purpose). To check if the checksum in the verification file matches the checksum of the file itself. If they match, the file download is successful. If they don't match, it suggests that the file may be corrupt, and you should consider downloading it again.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948550732_b0ad6ff0_1657_4c0b_8551_ef5345c5c093.png)

Select all compressed files, right-click and extract to the current folder or your own directory:

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948550929_05258903_2f86_4eb2_8161_73f85bc48237.png)

After the extraction is complete, you will obtain the development environment OK3588-VM16.2.3-ubuntu20.04.

The file "3588 development environment.vmx" in the OK3588-VM16.2.3-ubuntu20.04 folder is the file that you need to open to access the virtual machine.

Open the installed virtual machine.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948551186_78129138_2117_434c_9ae3_b561afd8aedb.png)

Navigate to the directory where the recently extracted OK3588-VM16.2.3-ubuntu20.04 virtual machine file is located, and double-click on the startup file to open it.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948551405_0730c09a_c36a_4e68_b187_6ec418d05eca.png)

Turn on this virtual machine after loading is complete to run it and enter the system's interface.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948551605_a94211f2_1285_4ecc_9a4d_d43152b574a8.png)

The default login account for automatic login in the development environment is "forlinx".

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948551892_df5d5e75_8ee6_4487_8740_9ab0415003c9.png)

## 3\. New Ubuntu Development Environment Setup

**Note: Beginners are not recommended to set up a system on their own. It is recommended to use an existing virtual machine environment. If you do not need to set up the environment, you can skip this section.**

**This chapter mainly explains the building process of Ubuntu system.**

### 3.1 Ubuntu System Setup

#### 3.1.1 Ubuntu Virtual Machine Setup

Step 1: Open the VMware software and click \[File]/ \[New Virtual Machine]. Enter the following interface

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948557881_bf708ddf_4635_4d44_bddb_4e6ee048ccda.png)

Step 2: Select Custom and click “Next”.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948558086_a3cc9a3f_e24e_4638_bfae_215772d6dee8.png)

Select the compatibility with the corresponding version of VMware, which can be found in Help->About VMware Workstation, and click “Next”.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948558261_9926dd9b_2063_45e4_962c_53ddd58f4545.png)

Select Install the operating system later and click “Next”.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948558474_60cdcb0c_a58d_4701_a9e9_f47f57fc96f6.png)

Keep the default settings and click “Next”.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948558651_6ca43874_078f_4ffa_bbc6_6dded8ec796a.png)

Modify the name and installation location of your virtual machine, and click “Next”.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948558907_86549cf9_bfa6_4420_9236_555456013b4f.png)

Configure the number of CPU based on your computer's actual specifications.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948559153_c05ea6ce_e22e_4c6f_8172_3b1309704eb9.png)

The memory size is also set according to the actual situation, and 32g is recommended for Android 14 compilation.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948559336_54b5e834_b27f_4d7b_b855_a534a87ed45a.png)

Set the network type, default to NAT mode then click “Next”. Keep the default values for the remaining steps until you reach the step to specify the disk capacity.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948559534_7164f982_b61d_4bf1_879c_b66baa06e287.png)

The default selection for the IO controller type here is LSI

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948559715_6334de6e_e394_4a9f_b0fe_24eff3f73d46.png)

The default selection here is also SCSI.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948559891_50108085_5316_4e45_b257_349fdee11cf2.png)

Choose to create a new virtual disk here.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948560078_080f6b13_f306_4c35_94f6_0fbe879c9a00.png)

Set the disk size to 500G, select the disk provisioning format, and then click “Next”.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948560319_b9944e6e_19be_4b1e_81a9_537e0f57ba08.png)

Specify the disk file, the default one here is fine.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948560495_155c1f47_6244_4630_abbc_bfbfcc24ce7f.png)

Click “Finish” by default.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948560717_1721904f_d97e_4f6a_aabd_0c462446af69.png)

The virtual machine creation is now complete.

In the next section, we will introduce the installation of Ubuntu system in the virtual machine, which is similar to the installation method in the real machine. Here we describe the method of installing Ubuntu system in a virtual machine.

#### 3.1.2 System Installation

In the previous section, we have created a virtual machine, but we haven’t installed the operating system yet, so the virtual machine cannot be started. Next, install the Ubuntu operating system in the newly created virtual machine.

Step 1: Go to the Ubuntu official website to obtain the Ubuntu20.04 64. The download address is:

[https://old-releases.ubuntu.com/releases/20.04.3/](https://old-releases.ubuntu.com/releases/20.04.3/)

Because the source code is compiled and verified on the 20.04, select and install it. These operations may vary slightly between Ubuntu system versions.

Download “ubuntu-20.04.3-desktop-amd64.iso”

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948560905_6e03158d_9008_4aa1_8d57_88d858267a33.png)

After downloading the mirror image, you can proceed with the system installation operation.

Right-click on the created virtual machine name and select “Settings” from the pop-up menu.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948561135_b4afd6e5_7b4a_474e_9038_9a3782698f4f.png)

The “Virtual Machine Settings” menu will pop up.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948561409_2794c64a_b0ee_4974_8358_5e7262fa4826.png)

Click on CD/DVD (SATA), select “Use ISO image file,” browse and choose the previously downloaded Ubuntu image, then click “OK” to confirm.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948561614_0cb88dd3_caa2_4de9_b8c4_0fe6b3cd51d2.png)

After setting up the image, ensure that the network is available. Then, start the virtual machine and proceed with the installation of the Ubuntu image.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948561827_18b5e8f2_8f95_4e23_99db_b57f83dcdffa.png)

After starting the virtual machine, wait for the installation interface to appear as shown below.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948562058_73d10201_e76e_4dde_b9f6_dce958518eaf.png)

After selecting the language on the left side as shown in the image, click “Install Ubuntu”, and the language selection interface will pop up. The default language of Ubuntu is English, but of course, you can also choose Others.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948562248_f2b8d3fe_26bf_49c7_93d3_f2b7ec605a7a.png)

The default selected language can also be reset at a later stage, after the selection is complete continue.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948562447_e4af3607_9e21_42e4_9748_484b1f77646f.png)

Next, select "Continue" as the default option to proceed with the installation. The installation process might be slow. Then, click "Continue" again.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948562639_f53fa9c6_7cab_4a0a_94df_d258431986e9.png)

By default, when you click on "Install Now", a dialog box will appear as shown in the image. Simply click "Continue" to proceed.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948562843_36141fa1_34eb_4474_94ba_2c4bc801e5ba.png)

Next, select the timezone. You can either click on the Shanghai timezone or enter "Shanghai" (or choose the appropriate timezone based on your location). Then, click "Continue" to proceed.

Finally, set your username and password. You can choose either automatic login or login with a username and password. Click "Continue" to start the automatic installation.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948563096_f829e292_e91d_4feb_9181_a3b5d00594cf.png)

If the internet connection is poor, you can Skip without affecting the installation process.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948563438_497b3c2d_04e3_406f_9b69_4ac67fddf5d1.png)

Click “Restart Now”  to reboot.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948563746_c0b4fa3c_b545_4ee7_a02e_a07756a13c53.png)

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948564045_db7ddaad_404e_4dd1_923a_d44121347b23.png)

The system interface after the reboot is complete.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948564312_58bdec72_3b40_4fb9_81d9_827839eb9d0b.png)

The ubuntu system installation is complete.

#### 3.1.3 Ubuntu Basic Configuration

After installing the Ubuntu20.04 operating system, there are a few configurations to make.

VMware Tools Installation:

Next, install VMware Tools. Without installing this tool, you won't be able to copy and paste and drag file between the Windows host and the virtual machine. First click on "Virtual Machine" on the VMware navigation bar, then click "Install VMware Tools" in the drop-down box.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948564622_9cc5d329_9b59_4caa_9b50_a9ca8d3567f9.png)

Once done, enter Ubuntu and the VMware Tools CD will appear on your desktop and click into it.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948564828_c95a8738_342d_48cf_aa0d_2ce9f0688ce1.png)

Enter and see a compressed file VMwareTools-10.3.10-12406962.tar.gz (it may be different for different VM versions); copy the file under the home directory (i.e. the directory with the home personal username)

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948565047_f7eb41f4_04f9_44cf_83d4_9ae26e6c0727.png)

Press \[Ctrl+Alt+T] to bring up the Terminal Command Interface and enter the command:

```bash
forlinx@ubuntu:~$ sudo tar xvf VMwareTools-10.3.10-12406962.tar.gz
```

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948565286_1ef6065e_3d24_4e5f_8897_873d80375ae1.png)

After the extraction is complete, a file named “vmware-tools-distrib" will appear.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948565577_9b5c7d23_ba69_4450_ae68_7c64bbc7fb63.png)

Go back to the terminal and type cd vmware-tools-distrib to enter the directory.

Enter: sudo ./images/OK3588-C_Android_14_User_Compilation_Manual/vmware-install.pl followed by pressing Enter. Then, enter your password and the installation process will begin. When prompted, you can input "yes" and press Enter to proceed. For any other inquiries, simply press Enter to go with the default installation settings.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948565768_0d4f434b_99f4_4fa1_8626_6f88a32aa91a.png)

Once the VMware tools is complete, we can implement file copy and paste between Windows and Ubuntu.

The virtual machine is displayed full screen:

If the virtual machine is not able to be displayed in full screen, you can resolve this issue by clicking on "View" and selecting "Autofit Guest." This will adjust the display to fit the screen automatically, enabling you to have a full-screen experience in the virtual machine.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948565963_6aadd47e_76b8_4541_91fd_27310afed0e3.png)

Make most of the system settings in the location shown. A lot of the setup requirements on Ubuntu can be done here.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948566192_9b3cc384_6683_448d_8b69_1d46a054caf7.png)

Virtual machine hibernation settings:

Also, the default hibernation is 5min, if you don't want to set hibernation, just set it to Never by setting Power->Blank screen.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948566454_b4fe4dc1_abf2_45b9_b36d_96835a98ba1c.png)

#### 3.1.4 Virtual Machine Network Settings 

##### 3.1.4.1 NAT Connection 

By default, after the virtual machine is installed, the network connection method is set to NAT, which shares the host machine's IP address. This configuration does not need to be changed when performing tasks like installing dependencies or compiling code.

When the VMware virtual NIC is set to NAT mode in a virtual machine, the network in the Ubuntu environment can be set to dynamic IP. In this mode the virtual NAT device and the host NIC are connected to communicate for Internet access. This is the most common way to access the external network.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948566750_83c42de6_a1a6_45e1_800c_1d7a628c5826.png)

##### 3.1.4.2 Bridge Connection

When the VMware virtual NIC device is in bridge mode, the host NIC and the virtual machine NIC communicate through the virtual bridge, and the network IP and the host need to be set in the same network segment in the Ubuntu environment. If accessing an external network, you need to set the DNS to be consistent with the host NIC. If TFTP, SFTP and other servers are used, the network contact mode of the virtual machine needs to be set as the bridge mode.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948566942_a5dee5ef_e480_446b_a0b5_ec244a4a9d8c.png)

### 3.2 Installation of the Necessary Libraries for Android Compilation

**Note: If you use the development environment provided by us, this section can be skipped directly.**

Android compilation requires the installation of several toolkits. Make sure that your computer or virtual machine can be connected to the Internet normally before the operation in this section. If the network is disconnected during the installation, please follow the following steps to install.

1. Install and compile the necessary packages for Android.

```bash
forlinx@ubuntu:~$ sudo apt-get update
forlinx@ubuntu:~$ sudo apt-get install software-properties-common
forlinx@ubuntu:~$ sudo add-apt-repository ppa:openjdk-r/ppa
forlinx@ubuntu:~$ sudo apt-get update
forlinx@ubuntu:~$ sudo apt-get install uuid \
    uuid-dev \
    zlib1g-dev \
    liblz-dev \
    liblzo2-2 \
    liblzo2-dev \
    lzop \
    git curl \
    u-boot-tools \
    mtd-utils \
    android-sdk-libsparse-utils \
    openjdk-8-jdk \
    device-tree-compiler \
    gdisk \
    m4 \
    make bc fakeroot unzip zip gawk busybox libstdc++6 lib32stdc++6 \
  bison flex python libssl-dev cpio lz4 rsync
```

The following libraries also need to be installed when using the Network Configuration Tool and menuconfig:

```bash
forlinx@ubuntu:~$ sudo apt-get update                           //Update the download source information
forlinx@ubuntu:~$ sudo apt-get install libncurses*              //For building text-based user interfaces
forlinx@ubuntu:~$ sudo apt-get install net-tools                //Network configuration tool
```

1. Switch to the JDK version

If you have previously installed another version of the JDK, you will need to switch versions.

To view the installed version:

```bash
forlinx@ubuntu:~$ update-java-alternatives -l
```

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948567133_412cc33e_dd69_4c60_8a0e_745e504cf5a5.png)

```bash
forlinx@ubuntu:~$ sudo update-alternatives --config java
```

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948567350_9c68b1d9_c5b7_4f82_b1a3_1d872d448cf9.png)

Enter the option corresponding to java8 and press Enter to confirm.

## 4\. Android System Compilation

Users can access the documentation and source code of the software and hardware through the web link provided by our company.

The compilation process needs to be carried out in the docker container. The program should be modified outside the docker as far as possible. The vim command in the docker is not very convenient to use.

### 4.1 Software Configuration File Path

OK3588-C platform, the software configuration file path is as follows:

| **Document type**| **path**
|:----------:|----------
| Kernel configuration file| kernel/configs/OK3588-C-Android.config
| Device tree file| arch/arm64/boot/dts/rockchip/FET3588.dtsi   arch/arm64/boot/dts/rockchip/OK3588-C-Common.dtsi   arch/arm64/boot/dts/rockchip/OK3588-C-Camera.dtsi   arch/arm64/boot/dts/rockchip/OK3588-C-Android.dts
| android| device/rockchip/rk3588/ok3588\_c/

### 4.2 Android System Compilation

#### 4.2.1 Preparation Before Compilation

Please confirm the size of the swap partition of the current system. If the swap partition is insufficient, the compilation of the Android source code will fail. 32G is recommended. It is recommended to adjust the development environment memory to 16G.

1\. View the swap partition:

```bash
forlinx@ubuntu:~$ cat  /proc/swaps
```

The virtual machine provided by Forlinx has been configured with the swap partition by default. If you use other virtual machines, you can increase the size of the swap partition by creating a swap file:

```bash
forlinx@ubuntu:~$ sudo swapoff /swapfile
forlinx@ubuntu:~$ sudo fallocate -l 32G /swapfile
forlinx@ubuntu:~$ sudo chmod 600 /swapfile
forlinx@ubuntu:~$ sudo mkswap /swapfile
forlinx@ubuntu:~$ sudo swapon /swapfile
forlinx@ubuntu:~$ sudo vim /etc/fstab
```

Adding the following at the end of the/etc/fstab file:

```bash
/swapfile none swap sw 0 0
```

2\. It is recommended to adjust the memory of the development environment to 16G. Low memory may cause the compilation to fail.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948574809_2e6c95da_4b96_42a9_b331_10cea2161e7d.png)

The source code package of the Android 14 system is placed in the data in the form of a volume compression package. Copy all the compression packages to the/home/forlinx/work/directory of the development environment, which is described below.

#### 4.2.2 Source Code Copy and Release

Source Code Path: Software\\ 2-Image and Source \\ 1-Source Code

The source code in the data is a volume compression package, which needs to be merged first, and then decompressed and released.

1. Copy all source code compressed packages to the/home/forlinx/work directory of the development environment, and perform MD5 verification.

You can directly drag the source code package on the computer to the folder on the desktop of the virtual machine, or use the shared folder to use the command copy. Here we focus on the use of the shared folder.

There are many kinds of file transfers between ubuntu and Windows hosts. After installing VMware Tools, you can set up a virtual machine shared folder to mount the file directory of the Windows host to ubuntu for file sharing.

Click "Virtual Machine" on the menu bar and select "Settings".

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948575021_2620975b_90cb_401c_859a_0e075730c818.png)

Click "Options", enable "Shared Folders", set the shared directory on the Windows host, and click "OK".

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948575253_85157bd2_ec8d_4580_8b2e_9ee03380e1a9.png)

After the file-sharing setup of the virtual machine is complete, place the source zip in the shared folder of the Windows host, here we name it “share”.

Shared folder in ubuntu in the mount directory /mnt/hgfs/share.

Copy the source code from the shared folder to ubuntu's /home/forlinx/work directory for md5 checksum:

```plain
forlinx@ubuntu:~$ cp /mnt/hgfs/share/OK3588-android14-source* /home/forlinx/work/      
forlinx@ubuntu:~$ cd /home/forlinx/work
forlinx@ubuntu:~/work$ md5sum OK3588-android14-source*
```

If the returned MD5 check code is consistent with the check code in the data, the source code can be merged.

2. Merge and unpack Android source code.

First, merge the archives into a single archive:

```plain
forlinx@ubuntu:~/work$ cat OK3588-android14-source.tar.bz2.* > OK3588-android14-source.tar.bz2
```

Decompress the combined compressed package

```plain
forlinx@ubuntu:~/work$ tar xvf OK3588-android14-source.tar.bz2
```

3. Modify source code file group.

View the current account ID. This example takes the development environment forlinx account provided by Forlinx as an example.

```plain
forlinx@ubuntu:~/work/$ id
uid=1000(forlinx) gid=1000(forlinx) groups=1000(forlinx),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),108(lpadmin),124
(sambashare)
```

Modify source code file group.

```plain
forlinx@ubuntu:~/work/$ sudo chown 1000:1000 -R OK3588-android14-source
forlinx@ubuntu:~/work/$ ls -l
drwxr-xr-x 4 forlinx forlinx        4096  4月 19 10:50 OK3588-android14-source
```

4. Add the Java runtime environment variable at the end of the.bashrc environment variable file in the user's home directory:

```plain
forlinx@ubuntu:~$ vim /home/forlinx/.bashrc
```

The additions are as follows:

```plain
export _JAVA_OPTIONS="-Xms64m -Xmx2g"
export MAVEN_OPTS="-Xms5120m -Xmx5120m"
```

Note: The development environment we provide modifies the.bashrc file as a hidden file, which can be viewed with the ls -a command and modified with the vim command.

```plain
forlinx@ubuntu:~$ source ~/.bashrc
```

#### 4.2.3 Android System Compilation

The android system compilation part of OK3588 platform supports full and partial compilation. All contents will be automatically compiled and packaged into an image that can be directly used for flashing. Part of the compilation is mainly used in the product development phase to compile the Linux kernel device tree or android system.

1\. Enter docker environment

To compile this system, you need to switch to the forlinx account

```plain
root@4d199700bc75:/# su forlinx
forlinx@4d199700bc75:/$
```

2\. Full compilation

Enter the longan directory and execute the following command:

```plain
forlinx@4d199700bc75:/$ cd /home/forlinx/work/OK3588-android14-source/
forlinx@4d199700bc75:~/OK3588-android14-source/$ source build/envsetup.sh;lunch ok3588_c-userdebug
forlinx@4d199700bc75:~/OK3588-android14-source/$ ./images/OK3588-C_Android_14_User_Compilation_Manual/build.sh -KAuop
```

Because the android system is too large, the compilation time is slightly longer. Please wait patiently for the compilation to be completed. The compiled image is located in the rockdev/Image-ok3588\_c/directory. The image file is a update. img

3\. Compile the kernel separately

```plain
forlinx@4d199700bc75:/$ cd /home/forlinx/work/OK3588-android14-source/
forlinx@4d199700bc75:~/OK3588-android14-source/$ source build/envsetup.sh;lunch ok3588_c-userdebug
forlinx@4d199700bc75:~/OK3588-android14-source/$ ./images/OK3588-C_Android_14_User_Compilation_Manual/build.sh -Ku
```

The compiled boot. img is /out/target/product/ok3588\_c$.

## 5\. Android Application Development

This chapter explains how to set up the Android application development environment, including downloading and installing the Android SDK and Android Studio integrated development environment, as well as using the OK3588 development board for on-device debugging. It is highly suitable for Android beginners to learn from and refer to.

### 5.1 Setting up the Android Application Development Environment

#### 5.1.1 JDK（Java SE Development Kit）Download and Installation

Since the Android application code is written in Java, you need to install the JDK on Windows first. The JDK can be downloaded as follows:

It is recommended to install Java 8, visit the website [https://www.oracle.com/java/technologies/downloads](https://www.oracle.com/java/technologies/downloads), and select the Windows x64 version of Java 8 in the page. You can also directly visit the website [https://www.oracle.com/java/technologies/downloads/#java8-windows](https://www.oracle.com/java/technologies/downloads/#java8-windows) to enter the download page.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948582611_6f4ec5ad_d1dd_41c7_a5a3_501af900752a.png)

Accept the agreement and proceed with the download.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948582902_63d904bc_7040_4b76_881a_5d31c8398ac3.png)

Currently, download JDK from the official Oracle website requires registration for an Oracle account. You may also choose alternative download methods.

After the download is completed, double-click the installer to complete the installation according to the wizard's prompts.

After the installation is complete, you need to add the JDK command to the Path environment variable. Use the following method to add the path of the JDK command to the Path environment variable:

1. Right-click on "My Computer" -> Properties, then select the "Advanced system settings" option on the left navigation.
2. Click the "Environment Variables" option in the lower right corner.
3. In "System Variables", find the Path environment variable, and double-click it; according to the actual installation path to set the java environment variable; the default installation adds the following content "C:\\Program Files\\Java\\jdk1.8.0\_211\\bin” (depending on the customer's actual installation path).
4. Click "OK" to complete the environment variable settings.

The following is a screenshot of the win7 system:

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948583119_8a2fe105_af4f_47e9_b00e_fd5ad79ab321.png)

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948583326_dfa375b4_106b_41d2_899d_050d28e61753.png)

The following is a screenshot of the win10 system:

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948583552_08df0653_3c4f_4351_915a_8b6caf1af6c8.png)

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948583772_8cff969a_88fb_4eec_b2cd_aa70ba58df5a.png)

5. Check that the installation was successful.

After completing the above settings, restart the computer, open the command prompt tool in the DOS window of the computer, and enter:

```bash
javac -version
```

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948583993_8adb117c_a468_4a0b_a527_2be49055cb95.png)

The correct display of the Java version indicates a successful installation.

#### 5.1.2 Android Studio Installation

Android Studio is a new development tool for Android launched by Google at I/O 2013. Please visit http://www.android-studio.org/ww.android-studio.org to download. It is recommended to download version 3.5.2.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948584195_ab7ea8fd_78ff_42c6_be79_0a1ad3a92f84.png)

After downloading, follow the prompts to install it. When the installation is complete, the following figure appears:

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948584513_90b1a4e6_f502_4c46_b745_73650892bbcb.png)

Select “Do not import settings ":

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948584712_2d71f708_7bc5_4889_b1b8_a3d663364b0e.png)

Select “Cancel ":

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948584951_0ed6797c_efe4_4b0c_94ea_b1df944f8386.png)

Click "Next" to go to the next step:

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948585186_509f50d1_8ed7_4670_9ed0_a3bcbcb5465d.png)

Select "custom" here:

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948585402_861b5b20_9309_4813_bf4d_7cf8007f261f.png)

Choose a UI theme based on your personal preference:

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948585661_057124d7_8242_4388_81f4_e220f1e144f4.png)

Select the installation path of Android SDK according to the actual situation:

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948585864_49669f8a_caba_4c0c_8808_3d4d5a5ebd52.png)

Select the memory size for the emulator:

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948586052_4ba843fc_2083_4273_b3c1_915a012fc7e2.png)

Click “Finish”.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948586400_a78b7c9f_cf97_45d4_a052_066f8efb8a41.png)

When the installation is complete, click“Finish”.

#### 5.1.3 Helloworld Project Creation

1. Select “start a new android studio project”：

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948586698_3732ed46_d7f8_4d79_9e2a_c34d5dafe3b2.png)

2. Choose “Empty Activity”:

Click "Next" to modify the project name and select the minimum supported android version:

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948587142_715898f0_4813_4651_bc32_9dbc2d5449b4.png)

Click “Finish”.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948587335_41f4a149_2660_4a15_9b7b_d936729b190c.png)

Tools such as Gradle will be downloaded for the first use, so please be patient.

3. Installl android 14.0 SDK

Click "File"-> "settings" to search SDK and open the interface as shown in the figure below:

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1756801277243_0e6463b1_1761_4ec8_8a2f_eb4e88512f41.png)

Check "Android API 34" and click "OK" to install.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948587843_6238498e_379c_4b79_8231_4f388d67da02.png)

4\. Modify "build. Gradle" ":

Modify all 32 in the file to 34, and press Ctrl + s to save the modified file.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948588079_60aacc2f_b3c4_45f9_94d4_8f4cdec5974c.png)

5. Compilation

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948588354_d3b996bd_a60a_48be_8982_b6e2b029778e.png)

Click "build"-> "Make Project" to recompile.

6. Run

After compiling, link the OTG cable to the USB port of your PC and click the green triangle icon in the menu bar.

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948588649_d50c64b6_cf0f_447d_8f5c_4b9d8160802d.png)

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948588919_30a0549d_2330_4329_982d_e148a5b086ed.png)

### 5.2 Apk Platform Signature

Note: If there is no OpenSSL command in your windows system, please go to[http://slproweb.com/products/Win32OpenSSL.html](http://slproweb.com/products/Win32OpenSSL.html) to down load and install it, and set environment variables.

In the Android platform, SELinux divides apps into three types, including untrusted\_app which has no platform signature and system privileges, platform\_app which has platform signature and no system privileges, and system\_app which has platform signature and system privileges. This chapter will introduce how to sign the apk and obtain system permissions.

1. Make signature document.

Copy build/target/product/security/platform.x509.pem and build/target/product/security/platform.pk8 in Android system to windows.

Open a command line window to execute:

```bash
openssl pkcs8 -in platform.pk8 -inform DER -outform PEM -out shared.priv.pem –nocrypt
openssl pkcs12 -export -in platform.x509.pem -inkey shared.priv.pem -out shared.pk12 -name androiddebugkey
```

Enter password: android

```bash
keytool -importkeystore -deststorepass android -destkeypass android -destkeystore debug.keystore -srckeystore shared.pk12 -srcstoretype PKCS12 -srcstorepass android -alias androiddebugkey
```

The key-alias and password can be modified to other contents as required. Save the signature file debug. keystore files to your usual directory.

2. Set andorid studio

Open any android studio project and add the shared UID in the AndroidManifest.xml, for example:

```bash
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.forlinx.helloworld"
android:sharedUserId="android.uid.system">
```

Click “File”->“project structure”:

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948589137_bad4b3b6_84de_4a2d_9325_e2cf9c6eb817.png)

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948589345_4d3f3932_29d0_467a_abd9_804f9ccccb1d.png)

Click “OK”.

To add the signature configuration for the debug and release versions, click "Build"in the Android Studio menu bar and "Edit Build Type...".

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948589537_c9c1a980_f795_4b64_a59f_794b82f7c997.png)

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948589799_4ccc5a8d_775a_40a7_a1a6_9c1a2d1442c2.png)

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948590074_e933ce81_efb5_4df3_9dfc_ef6c52cf3e7b.png)

Click "OK" when the modification is completed.

Click the run button "" of android studio to ![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948590265_8244c674_804b_41c8_8afd_60cf9d268109.png) start the app. Enter in the serial port:

ps –AZ

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948590452_aa7095d5_6885_459a_9d4a_8d7f368a6904.png)

Confirm whether your app has become system \_ app.

If the app prints the following error when running:

![Image](./images/OK3588-C_Android_14_User_Compilation_Manual/1718948590687_a118cc80_b7a6_48fb_9eff_76e31db29af8.png)

Solution: Uninstall the APP in the system, restart the board, and reinstall and run it.

### 5.3 Pre - installation Method of APK in System

1. Create a new directory in Android system:

```bash
forlinx@ubuntu:~/work/OK3588-android14-source$ mkdir packages/apps/helloworld
```

Copy the apk that needs to be pre-installed (no signature is required) to the directory. Take the helloworld.apk as an example:

```bash
forlinx@ubuntu:~/work/OK3588-android14-source$ cp helloworld.apk packages/apps/helloworld
```

2. Create a new Android. mk at packages/apps/helloworld

```bash
forlinx@ubuntu:~/work/OK3588-android14-source$vi packages/apps/helloworld/Android.mk
```

Add the following:

```bash
    LOCAL_PATH := $(call my-dir)
    include $(CLEAR_VARS)
    LOCAL_MODULE := helloworld
    LOCAL_SRC_FILES := helloworld.apk
    LOCAL_MODULE_CLASS := APPS
    LOCAL_MODULE_SUFFIX := .apk
    LOCAL_BUILT_MODULE_STEM := package.apk
    LOCAL_CERTIFICATE := platform
    LOCAL_DEX_PREOPT := false
    LOCAL_PRIVILEGED_MODULE := true
    include $(BUILD_PREBUILT)
```

3. <font style="color:#000000;">Modify at the same time device/rockchip/rk3588/ok3588\_c/ok3588\_c.mk</font>

```bash
forlinx@ubuntu:~/work/OK3588-android14-source$ vi device/rockchip/rk3588/ok3588_c/ok3588_c.mk
```

Add the followings:

```bash
PRODUCT_PACKAGES += \
helloworld
```

4. Recompile the image