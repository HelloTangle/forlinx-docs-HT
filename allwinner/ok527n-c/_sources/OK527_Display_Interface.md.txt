# Display Interface

Document classification: □ Top secret □ Secret □ Internal information ■ Open

## Copyright

The copyright of this manual belongs to Baoding Folinx Embedded Technology Co., Ltd. Without the written permission of our company, no organizations or individuals have the right to copy, distribute, or reproduce any part of this manual in any form, and violators will be held legally responsible.

Forlinx adheres to copyrights of all graphics and texts used in all publications in original or license-free forms.

The drivers and utilities used for the components are subject to the copyrights of the respective manufacturers. The license conditions of the respective manufacturer are to be adhered to. Related license expenses for the operating system and applications should be calculated/declared separately by the related party or its representatives.

## Application Scope

This manual is primarily applicable to the Forlinx OKT527 platform running Linux5.15. It can be used as a reference for other platforms, but differences between platforms may exist, and customers will need to modify it to suit their own use.

## Debugging of MIPI Screen Initialization Sequence

This test is based on the user materials of OK527 - C \& OK527N - C\_Linux5.15.147 + Qt5.15.8. The old BSP does not support this modification.

## Introduction

For T527 screen debugging, the U - Boot device tree and the kernel device tree need to be modified respectively. Currently, the U - Boot source code is not open - sourced. You can first debug the kernel. After the kernel works normally, contact us to debug the U - Boot.

device/config/chips/t527/configs/okt527/uboot-board.dts

kernel/linux-5.15/arch/arm64/boot/dts/allwinner/OKT527-C-Common.dtsi

Adjusting the parameters of the MIPI screen is not very different from other screens. You need to configure the pins, backlight, and screen parameters. Only some MIPI screens need to add an initialization sequence.

## Modification Method

Take the kernel device tree as an example, and the same applies to the U - Boot device tree.

```plain
&dsi0 {
        status = "disabled";
        pinctrl-0 = <&dsi0_4lane_pins_a>;	//Configure pins
        pinctrl-1 = <&dsi0_4lane_pins_b>;	//Configure pins
        pinctrl-names = "active","sleep";

        panel: panel@0 {
                compatible = "allwinner,virtual-panel";
                status = "okay";
                reg = <0>;
                power0-supply = <&reg_cldo3>;
                power1-supply = <&reg_dcdc4>;
                power2-supply = <&reg_cldo1>;

                backlight = <&backlight0>;	//Backlight configuration. Note that the backlight enable pin PI12 needs to be commented out.
                //Or replace it with the actually used pin, as there is a discrepancy here with the hardware.

        power-delay-ms = <0>;
        reset-delay-ms = <0>;								//Reset pin delay
        enable-delay-ms = <0>;
        reset-gpios = <&pio PI 12 GPIO_ACTIVE_HIGH>;	//Configure the screen's reset pin, and remap the backlight enable pin to this location according to the hardware design.
        width-mm = <68>;										//Screen width
        height-mm = <121>;									//Screen height

        dsi,flags = <(MIPI_DSI_MODE_VIDEO | MIPI_DSI_MODE_VIDEO_BURST | MIPI_DSI_MODE_NO_EOT_PACKET)>;
        dsi,format = <0>; //<MIPI_DSI_FMT_RGB888>;
        dsi,lanes  = <4>;		//Lane number configuration
        panel-init-sequence = [	//Initialization sequence
            ];
      //  panel-exit-sequence = [	//Close the sequence, some screens require
      //      ];

                display-timings {
                        native-mode = <&dsi_timing0>;

                        dsi_timing0: timing0 {	//Screen parameter configuration
                hback-porch     = <48>;
                hfront-porch    = <40>;
                hactive         = <1024>;
                hsync-len       = <48>;
                vback-porch     = <48>;
                vfront-porch    = <40>;
                vactive         = <600>;
                vsync-len       = <4>;
                clock-frequency = <45000000>;
                vsync-active    = <0>;
                hsync-active    = <0>;
                de-active       = <0>;
                pixelclk-active = <0>;
                        };
                };
```

The above is the content of DSI. The initialization sequence needs to be filled in according to Allwinner’s defined logic. Generally, the initialization provided by the screen manufacturer is added in the driver. So the format is generally as follows:

```plain
#if 1 //zheng shao
SPI_WriteComm(0xFF);
SPI_WriteData(0x77);
SPI_WriteData(0x01);
SPI_WriteData(0x00);
SPI_WriteData(0x00);
SPI_WriteData(0x10);

SPI_WriteComm(0xC0);
SPI_WriteData(0x3B);	
SPI_WriteData(0x00);
··· ···							//Part of the content is omitted
SPI_WriteComm(0x11);

Delay(120);

SPI_WriteComm(0x29);

SPI_WriteComm(0x36);
SPI_WriteData(0x00);

SPI_WriteComm(0x3A);
SPI_WriteData(0x60);
#endif
```

After modification, it should be:

```plain
39 00 06 FF 77 01 00 00 10
39 00 03 C0 3B 00
··· ···										//Part of the content is omitted
05 78 01 11
05 00 01 29
15 00 02 36 00
15 00 02 3A 60
```

The original data format is: Write several data sequentially at a certain address.

The new data format is: \[Packet type]\[Sending delay]\[Data length]\[\*n MIPI screen initialization data] // Hexadecimal numbers

Packet type: When the length of the written data is 1, 2, 3, and above, it is 05, 15, 39 respectively.

Sending delay: Fill in 00 when there is no delay. If there is a delay, convert it to a hexadecimal number. For example, the above - mentioned delay of 120 corresponds to 78.

Data length: It refers to the number of bytes of the original address and data. For example, in the first group, 0x77 0x01 0x00 0x00 0x10 are written sequentially at 0xff, a total of 5 bytes, so the total is 6 bytes.

Initialization data: Fill in the address and data of the original data.

Some original data are in the following format, which are arranged according to the address, the number of data, and the data value.

```plain
{0x9B,12,{0x03,0x6A,0x03,0x7F,0x03,0x96,0x03,0xB7,0x03,0xDF,0x03,0xFF}},
{0x36,1,{0x0A}},
{0x11,0,{0x00}},
{REGFLAG_DELAY, 120, {}},
```

Similarly, count the address and the number of data, determine the delay, and fill them in according to Allwinner’s format.

```plain
39 00 0d 9b 03 6a 03 7f 03 96 03 b7 03 df 03 ff
15 00 02 36 0a
05 78 01 11 
```

Fill all the initialization sequences into the device tree according to the above - mentioned format. After modifying other screen parameters, compile and test the display of the MIPI screen.

If there is still no display, check the backlight, measure the pin waveforms of the MIPI screen, and confirm that the initialization sequence is written successfully. If the screen shows a garbled image, adjust the screen parameters.