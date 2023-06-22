# m1ngl/edidreader
 - 这是一个可以读取你的屏幕的EDID的Python脚本，基于Linux环境开发。
 - 我在仓库里面放了几个示例
### 运行
```bash
$ ./main.py edid.bin
```
或
```bash
$ ./main.py /sys/class/drm/card0-eDP-0/edid
```

### 后面的0xfc数据类型实在难写，先搁置一段时间...
