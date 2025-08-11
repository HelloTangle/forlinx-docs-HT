# Linux6.1.36_User's Compilation Manual_V1.0

## 1. Preparation Before Compilation

This chapter mainly describes the compilation methods for the source code related to the development board, including the separate compilation of the kernel source code, the compilation of application programs, and the packaging of the flashing image, etc., providing references for users.

### 1.1 Description of the Environment

+ Development environment OS: 20.04.1-Ubuntu   x86\_64
+ Cross-toolchain: aarch64-linux-gnu
+ Development board Bootloader version:U-Boot 2023.04-lf\_v2023.04
+ Development Board Kernel: Linux-6.1.36
+ Development board porting QT version: qt6.5.0

#### 1.1.1 Source Code Description

Program source code: user data\\01-Software Documentation\\03-src\&img\\02-source code                Source Code Description：

| File| Description
|----------|----------
| commit\_id.txt| Stores the internal git version of the source code for version control
| okmx8mp-smarc-uboot.tar.zst| Uboot Source Code
| okmx8mp-smarc-kernel.tar.zst| Kernel Source Code
| okmx8mp-smarc-kernel-extra.tar.zst| Kernel extra module source code
| forlinx-image-qt6-full-fet-mx8mp-smarc-20240229060101.rootfs.tar.zst| Forlinx uses the rootfs package compiled with yocto:
| okmx8mp-smarc-rootfs-overlay.tar.zst| Customized modification content based on rootfs package for Forlinx.
| fsl-imx-xwayland-glibc-x86\_64-forlinx-image-qt6-full-armv8a-fet-mx8mp-smarc-toolchain-6.1-mickledore.sh| The tool chain compiled by yocto is convenient for users to compile QT program.

Files with the md5sum suffix: The md5 value of the file is stored for validation.

### 1.2 Compilation

#### 1.2.1 Rootfs Preparation

Forlinx provides the rootfs package compiled with yocto:   
forlinx-image-qt6-full-fet-mx8mp-smarc-20240229060101.rootfs.tar.zst ，  
Plus, it offers customized modification contents based on the rootfs, okmx8mp-smarc-rootfs-overlay.tar.zst.   
The user can use the above two directories to synthesize rootfs for the OK-MX8MPQ-SMARC development board as follows:   
Environment variables need to be pre-configured ROOTFS \_ DIR, OVERLAY \_ DIR.   
1\. Unzip the rootfs package and the overlay package.

```plain
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk#  tar -I zstd -xf forlinx-image-qt6-full-fet-mx8mp-smarc-20240229060101.rootfs.tar.zst -C ${ROOTFS_DIR}
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk#  tar -I zstd -xf okmx8mp-smarc-rootfs-overlay.tar.zst -C ${OVERLAY_DIR}
```

2\. Delete the unused files in the rootfs package.   
The kernel image and device tree in the boot directory within the rootfs package, as well as the kernel modules in the lib/modules directory, are compiled from the kernel code in Yocto and need to be deleted. The kernel file used by the OK - MX8MPQ - SMARC development board is the one compiled in Section 1.2.3.

```plain
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/okmx8mp-smarc-fs#  rm boot lib/modules/6.1.36* -rf
```

3\. Compile the kernel and install the kernel module to the overlay directory. Compile the Forlinx test program and install it to the overlay directory.   
Refer to Sections 1.2. 3, 1.2. 4, 1.2. 5 for this step.   
4\. Overwrite the overlay directory to the rootfs directory.

```plain
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk#  cp -a overlay/* ${ROOTFS_DIR}/
```

5\. At this point, the rootfs directory is the root file system that will be used.

#### 1.2.2 Uboot Compilation

Uboot is configured as follows:   

Config：okmx8mp-smarc\_defconfig                        

Cross compilation chain: aarch64-linux-gnu-gcc Arch：arm                                                                       

The reference compilation commands are shown below:

```plain
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/uboot#  make CROSS_COMPILE=aarch64-linux-gnu- ARCH=arm okmx8mp-smarc_defconfig
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/uboot#  make CROSS_COMPILE=aarch64-linux-gnu- -j32 V=0
```

The final generated image file is flash.bin.

#### 1.2.3 Kernel Compilation

The kernel is configured as follows:   
config：ok-mx8mp-smarc\_defconfig  
dts：ok-mx8mp-smarc.dts、ok-mx8mp-smarc-2gb.dts  
Cross compilation chain:  aarch64-linux-gnu-gcc  
Arch：arm64  
The reference compilation commands are shown below:

```plain
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/kernel#  make ok-mx8mp-smarc_defconfig ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu-
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/kernel#  make ARCH=arm64 -j8 CROSS_COMPILE=aarch64-linux-gnu- dtbs Image
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/kernel#  make ARCH=arm64 -j8 CROSS_COMPILE=aarch64-linux-gnu- modules
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/kernel#  make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- modules_install \
INSTALL_MOD_PATH=${OVERLAY_DIR}
```

The overlay directory is used to overwrite the rootfs directory, making it easier to replace existing directories and files in the rootfs directory.

#### 1.2.4 Extra of Kernel Compilation

The reference compilation commands are shown below:   
Environment variables need to be pre-configured KERNEL\_DIR，OVERLAY\_DIR.

```plain
#cryptodev_1.12-r0
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/extra/cryptodev_1.12-r0#  make KERNEL_DIR=${KERNEL_DIR} ARCH=arm64 \
CROSS_COMPILE=aarch64-linux-gnu-
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/extra/cryptodev_1.12-r0#  make KERNEL_DIR=${KERNEL_DIR} ARCH=arm64 \
CROSS_COMPILE=aarch64-linux-gnu- \
INSTALL_MOD_PATH=${OVERLAY_DIR} modules_install

#jailhouse
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/extra/jailhouse#  make KDIR=${KERNEL_DIR} ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- 
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/extra/jailhouse#  make KDIR=${KERNEL_DIR} ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- \
INSTALL_MOD_PATH=${OVERLAY_DIR} DESTDIR=${OVERLAY_DIR} modules_install

#kernel-module-isp-vvcam
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/extra/kernel-module-isp-vvcam/vvcam/v4l2#  make KERNEL_SRC=${KERNEL_DIR} ARCH=arm64 \
CROSS_COMPILE=aarch64-linux-gnu-
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/extra/kernel-module-isp-vvcam/vvcam/v4l2#  make KERNEL_SRC=${KERNEL_DIR} ARCH=arm64 \
CROSS_COMPILE=aarch64-linux-gnu- INSTALL_MOD_PATH=${OVERLAY_DIR} modules_install

#imx-dsp-2.1.5
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/extra/imx-dsp-2.1.5#  ./configure --enable-armv8
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/extra/imx-dsp-2.1.5#  make
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/extra/imx-dsp-2.1.5#  make install DESTDIR=${OVERLAY_DIR}
```

#### 1.2.5 Test Program Compilation

There are two kinds of test programs provided by Forlinx: Command line and QT.   
Compile the command line test program. The reference command is as follows:

```plain
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/appsrc/forlinx-cmd#  export CC=aarch64-linux-gnu-gcc
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/appsrc/forlinx-cmd#  make
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/appsrc/forlinx-cmd#  make install INSTALL_PATH=${OVERLAY_DIR}/usr/bin/
```

To compile the QT test program, you need to install the qmake corresponding to the QT version first. Forlinx provides the installation program of qmake and related library files compiled based on yocto:   
fsl-imx-xwayland-glibc-x86\_64-forlinx-image-qt6-full-armv8a-fet-mx8mp-smarc-toolchain-6.1-mickledore.sh  
Users can also compile qmake themselves using yocto.   
Install qmake provided by Forlinx

```plain
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk#  ./fsl-imx-xwayland-glibc-x86_64-forlinx-image-qt6-full-armv8a-fet-mx8mp-smarc-toolchain-6.1-mickledore.sh << EOF
> 
> Y
> EOF
```

**Note that the environment variables configured by default for this tool chain can only be used for QT programs. To compile other images, please install the cross-compilation chain yourself.**   
The reference compilation commands are shown below:

```plain
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/appsrc/forlinx-qt#  source /opt/fsl-imx-xwayland/6.1-mickledore/environment-setup-armv8a-poky-linux
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/appsrc/forlinx-qt#  qmake
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/appsrc/forlinx-qt#  make
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/appsrc/forlinx-qt#  make install
```

The install default installation directory is target. path =./././overlay/usr/bin/, which is written in the.pro file of each QT test program. Please modify it according to the actual situation.

#### 1.2.6 Packaging Flashed Image

The following files and directories are required to package the burn image:   
Kernel image and device tree：Image ok-mx8mp-smarc.dtb ok-mx8mp-smarc-2gb.dtb  
Display logo under Uboot ：pic/logo-1280x800.bmp pic/logo-1024x600.bmp  
Rootfs directory: Refer to 1.2.5 to prepare rootfs   
The directory structure is as follows:

```plain
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk#  tree  -L 1 images/ pic/ okmx8mp-smarc-fs/
images/
├── Image
├── flash.bin
├── ok-mx8mp-smarc-2gb.dtb
└── ok-mx8mp-smarc.dtb
pic/
├── logo-1024x600.bmp
└── logo-1280x800.bmp
okmx8mp-smarc-fs/
├── bin
├── dev
├── etc
├── home
├── lib
├── media
├── mnt
├── opt
├── proc
├── run
├── sbin
├── srv
├── sys
├── tmp
├── unit_tests
├── usr
├── var
└── www

18 directories, 6 files
```

The reference commands are shown below:   
Before executing the packaging command, it is necessary to set environment variables, such as IMAGE PATH and ROOTFS-PATH. The Images directory in the IMAGE PATH directory stores the Kernel image and device tree, while the pic directory stores the logo; ROOTFS-PATH is the rootfs directory.

```plain
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk#  export IMAGE_PATH=/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk#  export ROOTFS_PATH=//mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk/okmx8mp-smarc-fs
root@5d90dd71f33a:/mnt/zzy/smarc_8mp/develop/sdk_20240506/okmx8mp-smarc-sdk#  fakeroot -- ./fakeroot.fs
```

The generated burn image ok8mp-linux-fs.sdcard.a \* is stored in the IMAGE PATH/images directory. Please refer to the user manual for the burn image.