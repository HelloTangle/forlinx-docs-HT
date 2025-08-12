# Quick Boot

Document classification: □ Top secret □ Secret □ Internal information ■ Open

## Copyright

The copyright of this manual belongs to Baoding Folinx Embedded Technology Co., Ltd. Without the written permission of our company, no organizations or individuals have the right to copy, distribute, or reproduce any part of this manual in any form, and violators will be held legally responsible.

Forlinx adheres to copyrights of all graphics and texts used in all publications in original or license-free forms.

The drivers and utilities used for the components are subject to the copyrights of the respective manufacturers. The license conditions of the respective manufacturer are to be adhered to. Related license expenses for the operating system and applications should be calculated/declared separately by the related party or its representatives.

## Application Scope                                                                                               

This note is primarily applicable to the Linux 5.15 operating system on the Forlinx OKT527-C platform. Other platforms can also refer to it, but there may be differences between platforms, requiring modifications according to your actual requirements.

## Methods for Quick Boot

The quick boot of T527 generally involves modifications to parts such as U-Boot environment variables and the kernel.   
**(1) Optimization of U-Boot Quick Boot**

Modify the U-Boot environment variables. Change the delay bootdelay to 0 seconds to eliminate the waiting time for entering the U-Boot menu. 

Open the following file:   
device/config/chips/t527/configs/okt527/longan/env.cfg

Find bootdelay = 1 and change it to bootdelay = 0.

```bash
#uboot system env config
bootdelay=0					//Default delay is 1 s, change to 0
```

Turn off the boot0 debug information printing. Modify the following file:

device/config/chips/t527/configs/okt527/sys\_config.fex  
modify debug\_mode to 0

```bash
[product]
version = "527"
machine = "okt527"

[platform]
eraseflag   = 0
debug_mode  = 0			//Default is 1 s, change to 0
```

**(2) Optimization of Kernel Quick Boot**

Reduce the collection of kernel printing information. 

Open the following file:

kernel/linux-5.15/drivers/char/random.c

Change CRNG\_READY in the last line of the following code to CRNG\_EMPTY.

```bash
static enum {
        CRNG_EMPTY = 0, /* Little to no entropy collected */
        CRNG_EARLY = 1, /* At least POOL_EARLY_BITS collected */
        CRNG_READY = 2  /* Fully initialized with POOL_READY_BITS collected */
} crng_init __read_mostly = CRNG_EMPTY;
#define crng_ready() (likely(crng_init >= CRNG_EMPTY))	//默认为CRNG_READY，改为CRNG_EMPTY
```

Modify the serial port printing priority. 

Open the following file:   
device/config/chips/t527/configs/okt527/longan/env.cfg

Modify loglevel to 0

```bash
init=/init
loglevel=0			//Default is 8 s, change to 0
selinux=0
```

**(3) Optimization of File System Startup**

Trim unnecessary services that start automatically at boot to reduce the startup time. 

Open the following file:

buildroot/buildroot-202205/package/allwinner/post\_build.sh

Delete the /etc/preinit service by commenting out the following 7 lines.

```bash
add_preinit_to_inittab(){
        if [ -e ${TARGET_DIR}/etc/inittab ]; then
                #insert preinit
#               grep "::sysinit:/etc/preinit" ${TARGET_DIR}/etc/inittab >/dev/null
#                if [ $? -eq 0 ]; then
#                        echo "preinit is already in inittab!"
#                else
#                        echo "preinit is not in inittab, add it!"
#                        sed -i '/Startup the system/a ::sysinit:/etc/preinit' ${TARGET_DIR}/etc/inittab
#                fi		*/
                #commented ttyS0, insert /bin/sh
```

You can also delete unnecessary services, such as the Bluetooth service. Delete platform/forlinx/overlay\_rootfs/etc/init.d/S40nxp, or rename it to 40nxp so that this service will not start.

After the modifications are completed, save the changes and exit. Then perform a full compilation, package the image, and burn it to the board. After making the above modifications, the boot test shows that the device can start up in about 7 - 8 seconds.