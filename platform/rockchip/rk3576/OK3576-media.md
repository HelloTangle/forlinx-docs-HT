

OK3576平台音视频部分应用层软件采用的是Gstreamer，支持硬件编解码。本节所有的示例均是基于Gstreamer命令行的形式。如果您需要带界面的播放器，您也可以使用qt的多媒体类，同样支持硬编解，可以参考Qt测试章节。

OK3576平台内部有一个视频处理单元VPU，支持以下格式的视频硬编解：

视频解码： H.264, H.265, VP9,AV1,AVS2。

视频编码： H264、H.265。

OK3576平台硬件编解码参数表：

| Video Decoder | Format | Profile | Resolution & Frame rate |
| --- | --- | --- | --- |
|  | H.265 | main 10 | 8K@30fps or 4K@120fps |
|  | H.264 | main 10 | 4K@60fps |
|  | VP9 | Profile 0/2 | 8K@30fps or 4K@120fps |
|  | AV1 | Profile 0/2 | 8K@30fps or 4K@120fps |
|  | AVS2 | main 10 | 8K@30fps or 4K@120fps |
| Video Encoder | H.264 | multi-stream | 4K@60fps |
|  | H.265 | multi-stream | 4K@60fps |


## 4.1 音频和视频播放体验
### 4.1.1使用gst-play播放器播放视频和音频
Gplay 是基于 Gstreamer 实现的音视频播放器，能够自动根据硬件自动选择合适的插件进行音视频播放，运行也十分简单。

```plain
root@ok3576-buildroot:/#<font style="color:#0000FF;"> gst-play-1.0 /userdata/1080p_30fps_h265-30S.mp4</font>

//播放带声音视频文件，由耳机放音测试

Press 'k' to see a list of keyboard shortcuts.

Now playing /userdata/1080p_30fps_h265-30S.mp4

Redistribute latency...

======> lhj add func:mpp_dec_init line:608 ok mpp_dec_debug:0

[  112.236844] dwhdmi-rockchip 27da0000.hdmi: Rate 149430000 missing; compute N dynamically

Redistribute latency...

[  112.282339] dwhdmi-rockchip 27da0000.hdmi: Rate 149430000 missing; compute N dynamically

Redistribute latency...

Redistribute latency...

Redistribute latency...

0:00:30.0 / 0:00:30.0

Reached end of play list.
```

### 4.1.2使用gst-launch 播放视频
```plain
root@ok3576-buildroot:/#<font style="color:#0000FF;"> gst-launch-1.0 filesrc location=/userdata/1080p_60fps_h265-30S.mp4 ! qtdemux ! queue ! h265parse ! mppvideodec ! waylandsink</font>

//仅播放视频

Setting pipeline to PAUSED ...

Pipeline is PREROLLING ...

Redistribute latency...

======> lhj add func:mpp_dec_init line:608 ok mpp_dec_debug:0

Redistribute latency...

Pipeline is PREROLLED ...

Prerolled, waiting for async message to finish...

Setting pipeline to PLAYING ...

Redistribute latency...

New clock: GstSystemClock

Got EOS from element "pipeline0".

Execution ended after 0:00:30.000513681

Setting pipeline to NULL ...

Freeing pipeline ...
```

### 4.1.3使用gst-launch 播放音频
```plain
root@ok3576-buildroot:/#<font style="color:#0000FF;"> gst-launch-1.0 filesrc location=/userdata/piano2-CoolEdit.mp3 ! id3demux ! mpegaudioparse ! mpg123audiodec ! alsasink device=plughw:1,0</font>

//仅播放音频

Setting pipeline to PAUSED ...

Pipeline is PREROLLING ...

Redistribute latency...

Pipeline is PREROLLED ...

Prerolled, waiting for async message to finish...

Setting pipeline to PLAYING ...

Redistribute latency...

New clock: GstAudioSinkClock

Got EOS from element "pipeline0".

Execution ended after 0:00:06.360500639

Setting pipeline to NULL ...

Freeing pipeline ...
```

### 4.1.4使用gst-launch 播放视频和音频
```plain
root@ok3576-buildroot:/#<font style="color:#0000FF;"> gst-launch-1.0 filesrc location=/userdata/1080p_60fps_h265-30S.mp4 ! qtdemux name=dec dec. ! queue ! h265parse ! mppvideodec ! waylandsink dec. ! queue ! decodebin ! alsasink device=plughw:1,0</font>

//播放带声音视频文件

Setting pipeline to PAUSED ...

Pipeline is PREROLLING ...

Redistribute latency...

======> lhj add func:mpp_dec_init line:608 ok mpp_dec_debug:0

Redistribute latency...

Redistribute latency...

Redistribute latency...

Pipeline is PREROLLED ...

Prerolled, waiting for async message to finish...

Setting pipeline to PLAYING ...

Redistribute latency...

New clock: GstAudioSinkClock

Got EOS from element "pipeline0".

Execution ended after 0:00:30.001881098

Setting pipeline to NULL ...

Freeing pipeline ...
```

## 4.2 视频硬编码
### 4.2.1视频硬编码H.264
```plain
root@ok3576-buildroot:/#<font style="color:#0000FF;"> gst-launch-1.0 videotestsrc num-buffers=600 ! video/x-raw,framerate=30/1,width=3840,height=2160 ! mpph264enc ! h264parse ! mp4mux ! filesink location=test.mp4</font>

Setting pipeline to PAUSED ...

Pipeline is PREROLLING ...

Redistribute latency...

Pipeline is PREROLLED ...

Prerolled, waiting for async message to finish...

Setting pipeline to PLAYING ...

Redistribute latency...

New clock: GstSystemClock

Got EOS from element "pipeline0".

Execution ended after 0:00:31.765292066

Setting pipeline to NULL ...

Freeing pipeline ...
```

### 4.2.2视频硬编码H.265
```plain
root@ok3576-buildroot:/#<font style="color:#0000FF;"> gst-launch-1.0 videotestsrc num-buffers=600 ! video/x-raw,framerate=60/1,width=3840,height=2160 ! mpph265enc ! h265parse ! mp4mux ! filesink location=test.mp4</font>

Setting pipeline to PAUSED ...

Pipeline is PREROLLING ...

Redistribute latency...

Pipeline is PREROLLED ...

Prerolled, waiting for async message to finish...

Setting pipeline to PLAYING ...

Redistribute latency...

New clock: GstSystemClock

0:00:06.9 / 0:00:10.0 (69.5 %)


```

## 4.3 视频硬解码
### 4.3.1解码并播放H264格式视频
```plain
root@ok3576-buildroot:/# <font style="color:#0000FF;">gst-launch-1.0 filesrc location=/userdata/1080p_30fps_h264-30S.mp4 ! qtdemux ! queue ! h264parse ! mppvideodec ! waylandsink</font>

Setting pipeline to PAUSED ...

Pipeline is PREROLLING ...

Redistribute latency...

======> lhj add func:mpp_dec_init line:608 ok mpp_dec_debug:0

Redistribute latency...

Pipeline is PREROLLED ...

Prerolled, waiting for async message to finish...

Setting pipeline to PLAYING ...

Redistribute latency...

New clock: GstSystemClock

Got EOS from element "pipeline0".

Execution ended after 0:00:30.000555181

Setting pipeline to NULL ...

Freeing pipeline ...
```



### 4.3.2解码并播放H264格式视频带音频
```plain
root@ok3576-buildroot:/# <font style="color:#0000FF;">gst-launch-1.0 filesrc location=/userdata/1080p_30fps_h264-30S.mp4 ! qtdemux name=demux demux.video_0 ! queue ! h264parse ! mppvideodec ! waylandsink demux.audio_0 ! queue ! aacparse ! faad ! alsasink device=plughw:1,0</font>

Setting pipeline to PAUSED ...

Pipeline is PREROLLING ...

Redistribute latency...

======> lhj add func:mpp_dec_init line:608 ok mpp_dec_debug:0

Redistribute latency...

Redistribute latency...

Redistribute latency...

Pipeline is PREROLLED ...

Prerolled, waiting for async message to finish...

Setting pipeline to PLAYING ...

Redistribute latency...

New clock: GstAudioSinkClock

Got EOS from element "pipeline0".

Execution ended after 0:00:30.002234765

Setting pipeline to NULL ...

Freeing pipeline ...
```

### 4.3.3解码并播放H265格式视频
```plain
root@ok3576-buildroot:/# <font style="color:#0000FF;">gst-launch-1.0 filesrc location=/userdata/1080p_60fps_h265-30S.mp4 ! qtdemux ! h265parse ! mppvideodec ! waylandsink</font>

Setting pipeline to PAUSED ...

Pipeline is PREROLLING ...

Redistribute latency...

======> lhj add func:mpp_dec_init line:608 ok mpp_dec_debug:0

Redistribute latency...

Pipeline is PREROLLED ...

Prerolled, waiting for async message to finish...

Setting pipeline to PLAYING ...

Redistribute latency...

New clock: GstSystemClock

Got EOS from element "pipeline0".

Execution ended after 0:00:30.000445014

Setting pipeline to NULL ...

Freeing pipeline ...
```

### 4.3.4解码并播放H265格式视频带音频
```plain
root@ok3576-buildroot:/# <font style="color:#0000FF;"> gst-launch-1.0 filesrc location=/userdata/4k_60fps_h265-30S.mp4 ! qtdemux name=demux demux.video_0 ! queue ! h265parse ! mppvideodec ! waylandsink demux.audio_0 ! queue ! aacparse ! faad ! alsasink</font>

Pipeline is PREROLLING ...

[ 1705.438451] dwhdmi-rockchip fde80000.hdmi: Rate 266625000 missing; computeRedistribute latency. ..

NRedistribute latency...

 dynamically

Pipeline is PREROLLED ...

Setting pipeline to PLAYING ...

Redistribute latency...

New clock: GstAudioSinkClock

0:00:01.4 / 0:00:30.0 (4.8 %)
```

### 4.3.5 解码并播放 VP9 格式视频
```plain
root@ok3576-buildroot:/# <font style="color:#0000FF;">gst-launch-1.0 filesrc location=/userdata/1080p_60fps_vp9-30S.mp4  ! qtdemux ! vp9parse ! mppvideodec ! waylandsink</font>

Setting pipeline to PAUSED ...

Pipeline is PREROLLING ...

Pipeline is PREROLLED ...

Prerolled, waiting for async message to finish...

Setting pipeline to PLAYING ...

Redistribute latency...

New clock: GstSystemClock

^Chandling interrupt. (10.3 %)

Interrupt: Stopping pipeline ...

Execution ended after 0:00:03.189342028
```

### 4.3.6 解码并播放 VP9 格式视频带音频
```plain
root@ok3576-buildroot:/#  <font style="color:#0000FF;">gst-launch-1.0 filesrc location=/userdata/1080p_60fps_vp9-30S.mp4 ! qtdemux name=demux demux.video_0 ! queue ! vp9parse ! mppvideodec ! waylandsink demux.audio_0 ! queue ! aacparse ! faad ! alsasink device=plughw:2,0</font>

Setting pipeline to PAUSED ...

Pipeline is PREROLLING ...

[  341.745740] dwhdmi-rockchip 27da0000.hdmi: Rate 149430000 missing; compute N dynamically

Redistribute latency...

Redistribute latency...

Pipeline is PREROLLED ...

Prerolled, waiting for async message to finish...

Setting pipeline to PLAYING ...

Redistribute latency...

New clock: GstAudioSinkClock

^Chandling interrupt. (1.3 %)

Interrupt: Stopping pipeline ...

Execution ended after 0:00:00.451334462
```

## 4.4 摄像头测试
OK3576支持OV13855 MIPI摄像头、UVC摄像头，首先来测试一下UVC摄像头，这里以罗技C270进程测试，将USB摄像头插入开发板，将自动安装uvc驱动。

### 4.4.1 UVC Camera测试
#### **4.4.1.1摄像头识别检测和格式支持查询**
摄像头识别检测

root@ok3576-buildroot:/# <font style="color:#0000ff;">v4l2-ctl --list-devices		</font>//查看UVC camera设备结点，可见/dev/video20&21为USB摄像头结点

UVC Camera (046d:0825) (usb-xhci-hcd.0.auto-1.1):

```plain
    /dev/video20

    /dev/video21

    /dev/media2
```

格式支持查询

root@ok3576-buildroot:/# <font style="color:#0000ff;">v4l2-ctl --list-formats-ext -d /dev/video20 	</font>//查看摄像头支持的格式

ioctl: VIDIOC_ENUM_FMT

```plain
    Type: Video Capture



    [0]: 'YUYV' (YUYV 4:2:2)

            Size: Discrete 640x480

                    Interval: Discrete 0.033s (30.000 fps)

                    Interval: Discrete 0.040s (25.000 fps)

                    Interval: Discrete 0.050s (20.000 fps)

                    Interval: Discrete 0.067s (15.000 fps)

                    Interval: Discrete 0.100s (10.000 fps)

                    Interval: Discrete 0.200s (5.000 fps)

            Size: Discrete 160x120

                    Interval: Discrete 0.033s (30.000 fps)

                    Interval: Discrete 0.040s (25.000 fps)

                    Interval: Discrete 0.050s (20.000 fps)

                    Interval: Discrete 0.067s (15.000 fps)

                    Interval: Discrete 0.100s (10.000 fps)

                    Interval: Discrete 0.200s (5.000 fps)

            Size: Discrete 176x144

                    Interval: Discrete 0.033s (30.000 fps)

                    Interval: Discrete 0.040s (25.000 fps)

                    Interval: Discrete 0.050s (20.000 fps)

                    Interval: Discrete 0.067s (15.000 fps)

                    Interval: Discrete 0.100s (10.000 fps)

                    Interval: Discrete 0.200s (5.000 fps)

            Size: Discrete 320x176

                    Interval: Discrete 0.033s (30.000 fps)

                    Interval: Discrete 0.040s (25.000 fps)

                    Interval: Discrete 0.050s (20.000 fps)

                    Interval: Discrete 0.067s (15.000 fps)

                    Interval: Discrete 0.100s (10.000 fps)

                    Interval: Discrete 0.200s (5.000 fps)
```

#### **4.4.1.2摄像头采集格式查询和修改**
摄像头采集格式查询

root@ok3576-buildroot:/# <font style="color:#0000ff;">v4l2-ctl -V -d /dev/video20</font>

Format Video Capture:

```plain
    Width/Height      : 640/480

    Pixel Format      : 'YUYV' (YUYV 4:2:2)

    Field             : None

    Bytes per Line    : 1280

    Size Image        : 614400

    Colorspace        : sRGB

    Transfer Function : Rec. 709

    YCbCr/HSV Encoding: ITU-R 601

    Quantization      : Default (maps to Limited Range)

    Flags             :
```

#### **4.4.1.3摄像头图像预览和拍照**
摄像头图像预览

```plain
root@ok3576-buildroot:/# <font style="color:#0000FF;">gst-launch-1.0  v4l2src device=/dev/video20 ! videoconvert ! video/x-raw,format=NV12,width=640,height=480  ! waylandsink</font>

Setting pipeline to PAUSED ...

Pipeline is live and does not need PREROLL ...

Pipeline is PREROLLED ...

Setting pipeline to PLAYING ...

New clock: GstSystemClock

Redistribute latency...

0:00:04.8 / 99:99:99.
```

摄像头拍照

```plain
root@ok3576-buildroot:/# <font style="color:#0000FF;">gst-launch-1.0 v4l2src device=/dev/video20 num-buffers=1 ! videoconvert ! video/x-raw,format=NV12,width=640,height=480 ! jpegenc ! filesink location=pic.jpg</font>

Setting pipeline to PAUSED ...

Pipeline is live and does not need PREROLL ...

Pipeline is PREROLLED ...

Setting pipeline to PLAYING ...

New clock: GstSystemClock

Redistribute latency...

Got EOS from element "pipeline0".

Execution ended after 0:00:00.941724595

Setting pipeline to NULL ...

Freeing pipeline ...

//执行完成后查看根目录下生成的pic.jpg文件即可
```



### 4.4.2  OV13855测试 
⚡⚡⚡ 当前资料调用ov13855 摄像头时，<font style="color:rgb(0, 0, 0);">图像显示偏绿，目前正在完善中，请谨慎选择。</font>

#### **4.4.2.1 摄像头识别检测和格式支持查询 **
root@ok3576-buildroot:/#   v4l2-ctl --list-devices

rkcif (platform:rkcif-mipi-lvds):

```plain
    /dev/video0

    /dev/video1

    /dev/video2

    /dev/video3

    /dev/video4

    /dev/video5

    /dev/video6

    /dev/video7

    /dev/video8

    /dev/video9

    /dev/video10

    /dev/media0
```

rkisp_mainpath (platform:rkisp-vir0): //cam1

```plain
    /dev/video55

    /dev/video56

    /dev/video57

    /dev/video58

    /dev/video59

    /dev/video60

    /dev/video63

    /dev/media5
```

#### **4.4.2.2 摄像头预览**
```plain
root@ok3576-buildroot:/# <font style="color:#0000FF;">gst-launch-1.0 v4l2src device=/dev/video55 ! video/x-raw, format=NV12, width=1920, height=1080, framerate=30/1 ! waylandsink</font>

Setting pipeline to PAUSED ...

Using mplane plugin for capture

Pipeline is live and does not need PREROLL ...

Pipeline is PREROLLED ...

Setting pipeline to PLAYING ...

New clock: GstSystemClock

[  314.354521] rkisp_hw 27c00000.isp: set isp clk = 702000000Hz

[  314.361618] rkisp rkisp-vir0: first params buf queue

[  314.362034] rkcif-mipi-lvds: stream[0] start streaming

[  314.362194] rockchip-mipi-csi2 mipi0-csi2: stream on, src_sd: 000000003df896bb, sd_name:rockchip-csi2-dphy0

[  314.362209] rockchip-mipi-csi2 mipi0-csi2: stream ON

[  314.362247] rockchip-csi2-dphy0: dphy0, data_rate_mbps 1080

[  314.362523] rockchip-csi2-dphy csi2-dcphy0: csi2_dphy_s_stream stream on:1, dphy0, ret 0

[  314.362537] ov13855 3-0036: ov13855_s_stream: on: 1, 4224x3136@30

Redistribute latency...

0:00:02.0 / 99:99:99.
```



#### **4.4.2.3 摄像头拍照**
```plain
root@ok3576-buildroot:/# <font style="color:#0000FF;">gst-launch-1.0 v4l2src device=/dev/video5 num-buffers=1 ! video/x-raw,format=NV12,width=640,height=480 ! mppjpegenc ! filesink location=pic.jpg</font>

//摄像头拍照（前置）

Setting pipeline to PAUSED ...

Using mplane plugin for capture

Pipeline is live and does not need PREROLL ...

Pipeline is PREROLLED ...

Setting pipeline to PLAYING ...

New clock: GstSystemClock

[  434.443953] rkisp_hw 27c00000.isp: set isp clk = 702000000Hz

[  434.451747] rkisp rkisp-vir0: first params buf queue

[  434.452082] rkcif-mipi-lvds: stream[0] start streaming

[  434.452177] rockchip-mipi-csi2 mipi0-csi2: stream on, src_sd: 000000003df896bb, sd_name:rockchip-csi2-dphy0

[  434.452187] rockchip-mipi-csi2 mipi0-csi2: stream ON

[  434.452217] rockchip-csi2-dphy0: dphy0, data_rate_mbps 1080

[  434.452685] rockchip-csi2-dphy csi2-dcphy0: csi2_dphy_s_stream stream on:1, dphy0, ret 0

[  434.452695] ov13855 3-0036: ov13855_s_stream: on: 1, 4224x3136@30

[  434.587464] rkisp-vir0: MIPI drop frame

Redistribute latency...

Got EOS from element "pipeline0".

Execution ended after 0:00:00.149978098

Setting pipeline to NULL ...

[  434.668086] rkisp-vir0: MIPI drop frame

[  434.668485] rkcif-mipi-lvds: stream[0] start stopping, total mode 0x2, cur 0x2

[  434.708426] rockchip-mipi-csi2 mipi0-csi2: stream off, src_sd: 000000003df896bb, sd_name:rockchip-csi2-dphy0

[  434.708454] rockchip-mipi-csi2 mipi0-csi2: stream OFF

[  434.709488] rockchip-csi2-dphy csi2-dcphy0: csi2_dphy_s_stream_stop stream stop, dphy0

[  434.709501] rockchip-csi2-dphy csi2-dcphy0: csi2_dphy_s_stream stream on:0, dphy0, ret 0

[  434.709528] ov13855 3-0036: ov13855_s_stream: on: 0, 4224x3136@30

[  434.709842] rkcif-mipi-lvds: stream[0] stopping finished, dma_en 0x0

root@ok3576-buildroot:/# ls

//查看是否生成 pic.jpg，可拷贝到 pc 查看

bin               data  etc   lib    linuxrc     media  oem  pic.jpg  rockchip-test  run   sdcard  system  udisk     usr  vendor

busybox.fragment  dev   info  lib64  lost+found  mnt    opt  proc     root           sbin  sys     tmp     userdata  var
```



### 4.2.3 OV5645 测试
**<font style="color:#000000;">摄像头对应节点</font>**

CAM2 ：rkcif-mipi-lvds1 

CAM3 ：rkcif-mipi-lvds2 

CAM4 ：rkcif-mipi-lvds4 

CAM5 ：rkcif-mipi-lvds3 

以测试 CAM5 为例

#### **4.2.3.1、摄像头识别检测**
root@rk3576-buildroot:/#   v4l2-ctl --list-devices

rkcif (platform:rkcif-mipi-lvds4):

```plain
    /dev/video44

    /dev/video45

    /dev/video46

    /dev/video47

    /dev/video48

    /dev/video49

    /dev/video50

    /dev/video51

    /dev/video52

    /dev/video53

    /dev/video54

    /dev/media4
```

#### **4.2.3.2、查看支持格式**
root@ok3576-buildroot:/#  v4l2-ctl --list-formats-ext -d /dev/video44

ioctl: VIDIOC_ENUM_FMT

```plain
    Type: Video Capture Multiplanar



    [0]: 'NV16' (Y/UV 4:2:2)

            Size: Stepwise 64x64 - 1920x1080 with step 8/8

    [1]: 'NV61' (Y/VU 4:2:2)

            Size: Stepwise 64x64 - 1920x1080 with step 8/8

    [2]: 'NV12' (Y/UV 4:2:0)

            Size: Stepwise 64x64 - 1920x1080 with step 8/8

    [3]: 'NV21' (Y/VU 4:2:0)

            Size: Stepwise 64x64 - 1920x1080 with step 8/8

    [4]: 'YUYV' (YUYV 4:2:2)

            Size: Stepwise 64x64 - 1920x1080 with step 8/8

    [5]: 'YVYU' (YVYU 4:2:2)

            Size: Stepwise 64x64 - 1920x1080 with step 8/8

    [6]: 'UYVY' (UYVY 4:2:2)

            Size: Stepwise 64x64 - 1920x1080 with step 8/8

    [7]: 'VYUY' (VYUY 4:2:2)

            Size: Stepwise 64x64 - 1920x1080 with step 8/8
```

#### **4.2.3.3、摄像头预览**
root@ok3576-buildroot:/#   <font style="color:#0000ff;">gst-launch-1.0 v4l2src device=/dev/video11 ! video/x-raw, format=NV12, width=1920,height=1080, framerate=30/1 ! waylandsink</font>

Setting pipeline to PAUSED ...

Using mplane plugin for capture

Pipeline is live and does not need PREROLL ...

Pipeline is PREROLLED ...

Setting pipeline to PLAYING ...

New clock: GstSystemClock

Redistribute latency...

0:00:06.3 / 99:99:99.

