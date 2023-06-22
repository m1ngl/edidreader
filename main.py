#!/bin/python3
import os
import sys

file = sys.argv.pop()


def _exit(string, status):
    print(string)
    sys.exit(status)


if file == "main.py" or file == "./main.py":
    _exit("没有输入文件", 2)

if not os.path.exists(file):
    _exit("文件不存在", 3)


def getCodeName(num):
    if num == 1.0 or num == 1:
        return "A"
    elif num == 10.0 or num == 10:
        return "B"
    elif num == 11.0 or num == 11:
        return "C"
    elif num == 100.0 or num == 100:
        return "D"
    elif num == 101.0 or num == 101:
        return "E"
    elif num == 110.0 or num == 110:
        return "F"
    elif num == 111.0 or num == 111:
        return "G"
    elif num == 1000.0 or num == 1000:
        return "H"
    elif num == 1001.0 or num == 1001:
        return "I"
    elif num == 1010.0 or num == 1010:
        return "J"
    elif num == 1011.0 or num == 1011:
        return "K"
    elif num == 1100.0 or num == 1100:
        return "L"
    elif num == 1101.0 or num == 1101:
        return "M"
    elif num == 1110.0 or num == 1110:
        return "N"
    elif num == 1111.0 or num == 1111:
        return "O"
    elif num == 10000.0 or num == 10000:
        return "P"
    elif num == 10001.0 or num == 10001:
        return "Q"
    elif num == 10010.0 or num == 10010:
        return "R"
    elif num == 10011.0 or num == 10011:
        return "S"
    elif num == 10100.0 or num == 10100:
        return "T"
    elif num == 10101.0 or num == 10101:
        return "U"
    elif num == 10110.0 or num == 10110:
        return "V"
    elif num == 10111.0 or num == 10111:
        return "W"
    elif num == 11000.0 or num == 11000:
        return "X"
    elif num == 11001.0 or num == 11001:
        return "Y"
    elif num == 11010.0 or num == 11010:
        return "Z"


def inputTable(table):
    tb = {}
    if table[0] == '1':
        tb["输入信号"] = "数字信号"
        if table[1] == '1' and table[2] == '1' and table[3] == '1':
            tb["色深度"] = "Undefined"
        elif table[1] == '0' and table[2] == '0' and table[3] == '0':
            tb["色深度"] = "Undefined"
        elif table[1] == '0' and table[2] == '0' and table[3] == '1':
            tb["色深度"] = "6 Bits per Primary Color"
        elif table[1] == '0' and table[2] == '1' and table[3] == '0':
            tb["色深度"] = "8 Bits per Primary Color"
        elif table[1] == '0' and table[2] == '1' and table[3] == '1':
            tb["色深度"] = "10 Bits per Primary Color"
        elif table[1] == '1' and table[2] == '0' and table[3] == '0':
            tb["色深度"] = "12 Bits per Primary Color"
        elif table[1] == '1' and table[2] == '0' and table[3] == '1':
            tb["色深度"] = "14 Bits per Primary Color"
        elif table[1] == '1' and table[2] == '1' and table[3] == '0':
            tb["色深度"] = "16 Bits per Primary Color"

        if table[4] == '0' and table[5] == '0' and table[6] == '0' and table[7] == '0':
            tb["数字接口支持"] = "Undefined"
        elif table[4] == '0' and table[5] == '0' and table[6] == '0' and table[7] == '1':
            tb["数字接口支持"] = "DVI Supported"
        elif table[4] == '0' and table[5] == '0' and table[6] == '1' and table[7] == '0':
            tb["数字接口支持"] = "HDMI-a Supported"
        elif table[4] == '0' and table[5] == '0' and table[6] == '1' and table[7] == '1':
            tb["数字接口支持"] = "HDMI-b Supported"
        elif table[4] == '0' and table[5] == '1' and table[6] == '0' and table[7] == '0':
            tb["数字接口支持"] = "MDDI Supported"
        elif table[4] == '0' and table[5] == '1' and table[6] == '0' and table[7] == '1':
            tb["数字接口支持"] = "DisplayPort Supported"
        else:
            tb["数字接口支持支持"] = "Undefined"
            tb["兼容VESA DFP 1.XTMDS CRGB"] = table[7] == '1'
    else:
        tb["输入信号"] = "模拟信号"
        tb["同步输入支持-场同步扫描"] = table[3] == '1'
        tb["同步输入支持-同步SOG信号"] = table[4] == '1'
        tb["同步输入支持-同步复合信号"] = table[5] == '1'
        tb["同步输入支持-同步分离信号"] = table[6] == '1'
        tb["屏幕可以自动设置黑白基准"] = table[7] == '1'
        if table[2] == '0' and table[1] == '0':
            tb["信号电平"] = "0.700 0.300 (1.000 V p-p)"
        elif table[2] == '1' and table[1] == '0':
            tb["信号电平"] = "0.714 0.286 (1.000 V p-p)"
        elif table[2] == '0' and table[1] == '1':
            tb["信号电平"] = "1.000 0.400 (1.400 V p-p)"
        elif table[2] == '1' and table[1] == '1':
            tb["信号电平"] = "0.700 0.000 (0.700 V p-p)"

    return tb


def dpmsTable(table):
    tb = {
        "是支持待机的": table[0] == '1',
        "是支持挂起的": table[1] == '1',
        "Active Off/Very Low Power": table[2] == '1'
    }
    if table[3] == '1' and table[4] == '1':
        tb["显示类型"] = "Undefined"
    elif table[3] == '1' and table[4] == '0':
        tb["显示类型"] = "RGB color display"
    elif table[3] == '0' and table[4] == '1':
        tb["显示类型"] = "非RGB多彩色显示"
    elif table[3] == '0' and table[4] == '0':
        tb["显示类型"] = "Monochrome / grayscale display (这个结果可能不准，我尝试了4个显示器都是这个结果)"
    tb["是使用了默认的sRGB色域的"] = table[5] == '1'
    tb["推荐分辨率是第一个详细描述的时序的"] = table[6] == '1'
    tb["是支持GTF标准分辨率的"] = table[7] == '1'
    return tb


def timingTable(table, order1='1', order2='2', vendor=True):
    timing1 = []
    timing2 = []
    vendor_timing = []
    if table[0][0] == '1':
        timing1.append(" 720x400@70Hz <IBM,VGA> ")
    elif table[0][1] == '1':
        timing1.append(" 720x400@88Hz <IBM,VGA2> ")
    elif table[0][2] == '1':
        timing1.append(" 640x480@60Hz <IBM,VGA> ")
    elif table[0][3] == '1':
        timing1.append(" 640x680@66/67Hz <Apple,Mac II> ")
    elif table[0][4] == '1':
        timing1.append(" 640x480@72Hz <VESA> ")
    elif table[0][5] == '1':
        timing1.append(" 640x480@75Hz <VESA> ")
    elif table[0][6] == '1':
        timing1.append(" 800x600@56Hz <VESA> ")
    elif table[0][7] == '1':
        timing1.append(" 800x600@60Hz <VESA> ")

    if table[1][0] == '1':
        timing2.append(" 800x600@72Hz <VESA> ")
    elif table[1][1] == '1':
        timing2.append(" 800x600@75Hz <VESA> ")
    elif table[1][2] == '1':
        timing2.append(" 832x624@75Hz <Apple,Mac II> ")
    elif table[1][3] == '1':
        timing2.append(" 1024x768@87Hz (I) <IBM 信号交错> ")
    elif table[1][4] == '1':
        timing2.append(" 1024x768@60Hz <VESA> ")
    elif table[1][5] == '1':
        timing2.append(" 1024x768@70Hz <VESA> ")
    elif table[1][6] == '1':
        timing2.append(" 1024x760@75Hz <VESA> ")
    elif table[1][7] == '1':
        timing2.append(" 1280x1024@75Hz <VESA> ")

    if vendor:
        if table[2][0] == '1':
            vendor_timing.append(" 1152x870@75Hz <Apple,Mac II> ")
        tb = {
            "时序1": timing1,
            "时序2": timing2,
            "制造商的时序 (可能不准确)": vendor_timing
        }
    else:
        tb = {
            "时序" + order1: timing1,
            "时序" + order2: timing2
        }

    return tb


def propTable(table):
    if table[0] == '0' and table[1] == '0':
        return "1:1 AR"
    elif table[0] == '0' and table[1] == '1':
        return "4:3 AR"
    elif table[0] == '1' and table[1] == '0':
        return "5:4 AR"
    elif table[0] == '1' and table[1] == '1':
        return "16:9 AR"


def refreshRate(table):
    if table[2:8] == '000001':
        return "N/A"
    return int(table[2:8], 2) + 60


# 这是用来获取文本流的函数
def getStream(stream, start: int, end):
    rlist = []
    for i in range(start, end):
        rlist.append(stream[i].to_bytes())
    return rlist


def dumpMDD(mddblock: list):
    tb = {}
    if mddblock[2][0] == b'\xff' or mddblock[2][0] == b'\xfe' or mddblock[2][0] == b'\xfc':
        tb["ASCII Code"] = ''
        for byte in mddblock[4]:
            tb["ASCII Code"] += byte.decode()
    if mddblock[2][0] == b'\xfd':
        tb["最低垂直速度"] = str(int.from_bytes(mddblock[3][0])) + " Hz"
        tb["最高垂直速度"] = str(int.from_bytes(mddblock[4][0])) + " Hz"
        tb["最低水平速度"] = str(int.from_bytes(mddblock[4][1])) + " kHz"
        tb["最高水平速度"] = str(int.from_bytes(mddblock[4][2])) + " kHz"
        tb["支持的最高像素时钟(根据四舍五入)"] = str(int.from_bytes(mddblock[4][3]) * 10) + " MHz"
        if mddblock[4][4] == b'\x02':
            tb["支持第二个GTF时序表"] = True
        elif mddblock[4][4] == b'\x00':
            tb["支持第二个GTF时序表"] = False
    if mddblock[2][0] == b'\xfa':
        tmTB = [
            timingTable([getBytes(mddblock[3][0]), getBytes(mddblock[4][0])], '19', '20', False),
            timingTable([getBytes(mddblock[4][1]), getBytes(mddblock[4][2])], '21', '22', False),
            timingTable([getBytes(mddblock[4][3]), getBytes(mddblock[4][4])], '23', '24', False),
            timingTable([getBytes(mddblock[4][5]), getBytes(mddblock[4][6])], '25', '26', False),
            timingTable([getBytes(mddblock[4][7]), getBytes(mddblock[4][8])], '27', '28', False),
            timingTable([getBytes(mddblock[4][9]), getBytes(mddblock[4][10])], '29', '30', False),
        ]
        tb["描述块里面的时序表"] = tmTB
    #       b'\xfc'和第二个GTF时序表的功能还没写
    return tb


def edidVerify(edidFile):
    checksum = 0
    for x in range(0, 128):
        checksum += int.from_bytes(edidFile[x], byteorder='big', signed=True)
    return checksum

# 信号Flags标志位
def dumpFLags(flags: str):
    tb = {}
    tb["信号是交错的"] = flags[0] == 1
    if tb["信号是交错的"]:
        if flags[1] == '0' and flags[2] == '0':
            tb["立体信号配置"] = "缺省值，没有立体信号"
        elif flags[1] == '0' and flags[2] == '1' and flags[7] == '0':
            if tb["信号是交错的"]:
                tb["立体信号配置"] = "场序立体信号，右图像位于偶数行上"
            else:
                tb["立体信号配置"] = "场序立体信号"
        elif flags[1] == '1' and flags[2] == '0' and flags[7] == '0':
            if tb["信号是交错的"]:
                tb["立体信号配置"] = "场序立体信号，左图像位于偶数行上"
            else:
                tb["立体信号配置"] = "场序立体信号"
        elif flags[1] == '0' and flags[2] == '1' and flags[7] == '1':
            tb["立体信号配置"] = "双路信号交错，右图像位于偶数行上"
        elif flags[1] == '1' and flags[2] == '0' and flags[7] == '1':
            tb["立体信号配置"] = "双路信号交错，左图像位于偶数行上"
        elif flags[1] == '1' and flags[2] == '1' and flags[7] == '0':
            tb["立体信号配置"] = "四路信号交错"
        elif flags[1] == '1' and flags[2] == '1' and flags[7] == '1':
            tb["立体信号配置"] = "并排交错信号"

    if flags[3] == '0' and flags[4] == '0':
        tb["同步信号合成方式"] = "模拟合成"
        tb["抗锯齿"] = flags[5] == '1'
        if flags[6] == '1':
            tb["颜色脉冲同步"] = "三色同步"
        else:
            tb["颜色脉冲同步"] = "颜色只会在绿色信号同步"
    elif flags[3] == '0' and flags[4] == '1':
        tb["同步信号合成方式"] = "双极模拟合成"
        tb["抗锯齿"] = flags[5] == '1'
        if flags[6] == '1':
            tb["颜色脉冲同步"] = "三色同步"
        else:
            tb["颜色脉冲同步"] = "颜色只会在绿色信号同步"
    elif flags[3] == '1' and flags[4] == '0':
        tb["同步信号合成方式"] = "数字合成"
        tb["抗锯齿"] = flags[5] == '1'
        tb["Hsync信号极性为正"] = flags[6] == '1'
    elif flags[3] == '1' and flags[4] == '1':
        tb["同步信号合成方式"] = "数字分离"
        tb["Vsync信号极性为正"] = flags[5] == '1'
        tb["Hsync信号极性为正"] = flags[6] == '1'
    return tb


# 这是用来将十六进制数值转化为二进制的函数，可以加权
def getBytes(bits, weight=1):
    return "{0:08b}".format(int.from_bytes(bits, byteorder='big') * weight)


class EdidCore:
    def __init__(self):
        self.identifier = [b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00', b'\x00']
        #       EDID的标识符 0-7字节
        self.vendor = [b'\x00', b'\x00']
        #       屏幕制造商 8-9字节
        self.ID = [b'\x00', b'\x00']
        #       产品ID 10-11字节
        self.Serial32 = [b'\x00', b'\x00', b'\x00', b'\x00']
        #       32位序列号 12-15字节
        self.madedate = [b'\x00', b'\x00']
        #       生产日期 16-17字节
        self.edidver = [b'\x00', b'\x00']
        #       EDID版本 18-19字节
        self.inputmethod = [b'\x00']
        #       输入信号 20字节
        self.displaysize = [b'\x00', b'\x00']
        #       显示器尺寸[长,宽] 21-22字节
        self.gamma = [b'\x00']
        #       伽玛值 23字节
        self.dpms = [b'\x00']
        #       DPMS支持 24字节
        self.RGLo = [b'\x00']
        #       红绿空间坐标的低位 25字节
        self.BWLo = [b'\x00']
        #       蓝白空间坐标的低位 26字节
        self.Rhi = [b'\x00', b'\x00']
        #       红色空间高位 27-28字节
        self.Ghi = [b'\x00', b'\x00']
        #       绿色空间高位 29-30字节
        self.Bhi = [b'\x00', b'\x00']
        #       蓝色空间高位 31-32字节
        self.Whi = [b'\x00', b'\x00']
        #       白色空间高位 33-34字节
        self.Timing = [b'\x00', b'\x00', b'\x00']
        #       时序表1和2 35-37字节
        # self.pixel = [b'\x00']
        # #       水平的有效像素 38字节
        self.STI = [b'\x00', b'\x00']
        #       新的标准把这里替换成8个时序表
        self.extraTiming = [self.STI, self.STI, self.STI,
                            self.STI, self.STI, self.STI,
                            self.STI, self.STI]
        #       制造商可能在这里写下了额外的时序表，借用一个2字节的变量 41-54字节
        self.frequency = [b'\x00', b'\x00']
        #       像素时钟频率 55-56字节
        self.pixel2 = [b'\x00', b'\x00', b'\x00']
        #       制造商的准确水平像素值 57-59字节
        self.pixel3 = [b'\x00', b'\x00', b'\x00']
        #       制造商的准确垂直像素值 60-62字节
        self.signalOffset = [b'\x00', b'\x00', b'\x00', b'\x00']
        #       制造商写的准确信号量偏移和脉冲信号宽度 63-66字节
        self.imageSize = [b'\x00', b'\x00', b'\x00']
        #       制造商写的图像尺寸 67-69字节
        self.borders = [b'\x00', b'\x00']
        #       ??? 70-71字节
        self.flags = [b'\x00']
        #       一些其他的标志位 72字节
        self.MDDescriptor = [
            [b'\x00', b'\x00'],  # 验证位 2字节
            [b'\x00'], [b'\x00'],  # 保留验证位和块类型位 1+1字节
            [b'\x00'],  # 标志位 1字节
            [b'\x00', b'\x00', b'\x00',
             b'\x00', b'\x00', b'\x00',
             b'\x00', b'\x00', b'\x00',
             b'\x00', b'\x00', b'\x00',
             b'\x00']  # 块的详细内容 13字节
        ]
        #       一个描述表块的定义 18字节/块
        self.MDDTable = [self.MDDescriptor, self.MDDescriptor, self.MDDescriptor]
        #       这样的块一共有三个 73-126字节


edid = EdidCore()
with open(file, 'rb') as f:
    content = f.read()

    edid.identifier = getStream(content, 0, 8)
    edid.vendor = getStream(content, 8, 10)
    edid.ID = getStream(content, 10, 12)
    edid.Serial32 = getStream(content, 12, 16)
    edid.madedate = getStream(content, 16, 18)
    edid.edidver = getStream(content, 18, 20)
    edid.inputmethod = getStream(content, 20, 21)
    edid.displaysize = getStream(content, 21, 23)
    edid.gamma = getStream(content, 23, 24)
    edid.dpms = getStream(content, 24, 25)
    edid.RGLo = getStream(content, 25, 26)
    edid.BWLo = getStream(content, 26, 27)
    edid.Rhi = getStream(content, 27, 29)
    edid.Ghi = getStream(content, 29, 31)
    edid.Bhi = getStream(content, 31, 33)
    edid.Whi = getStream(content, 33, 35)
    edid.Timing = getStream(content, 35, 38)
    edid.extraTiming = [getStream(content, 38, 40), getStream(content, 40, 42), getStream(content, 42, 44),
                        getStream(content, 44, 46), getStream(content, 46, 48), getStream(content, 48, 50),
                        getStream(content, 50, 52), getStream(content, 52, 54)]
    edid.frequency = getStream(content, 54, 56)
    edid.pixel2 = getStream(content, 56, 59)
    edid.pixel3 = getStream(content, 59, 62)
    edid.signalOffset = getStream(content, 62, 66)
    edid.imageSize = getStream(content, 66, 69)
    edid.borders = getStream(content, 69, 71)

    edid.flags = getStream(content, 71, 72)
    timing_table = timingTable([getBytes(edid.Timing[0]),
                                getBytes(edid.Timing[1]),
                                getBytes(edid.Timing[2])])
    edid.MDDTable = [
        [getStream(content, 72, 74), getStream(content, 74, 75),
         getStream(content, 75, 76), getStream(content, 76, 77), getStream(content, 77, 90)],
        [getStream(content, 90, 92), getStream(content, 92, 93),
         getStream(content, 93, 94), getStream(content, 94, 95), getStream(content, 95, 108)],
        [getStream(content, 108, 110), getStream(content, 110, 111),
         getStream(content, 111, 112), getStream(content, 112, 113), getStream(content, 113, 126)]
    ]
    vendor_bytes = int(getBytes(edid.vendor[0], 256)) + int(getBytes(edid.vendor[1]))
    first = (vendor_bytes - (vendor_bytes % 10000000000)) / 10000000000
    second = (vendor_bytes % 10000000000 - vendor_bytes % 100000) / 100000
    third = (vendor_bytes % 100000)

    id_bytes = hex(int.from_bytes(edid.ID[1])) + hex(int.from_bytes(edid.ID[0]))[2:]
    serical_bytes = hex(int.from_bytes(edid.Serial32[0]))[2:] + \
                    hex(int.from_bytes(edid.Serial32[1]))[2:] + \
                    hex(int.from_bytes(edid.Serial32[2]))[2:] + \
                    hex(int.from_bytes(edid.Serial32[3]))[2:]

    if serical_bytes == "0000":
        serical_bytes = "N/A"
    else:
        serical_bytes = "0x" + serical_bytes

    madedate_bytes = {
        "week": int.from_bytes(edid.madedate[0]),
        "year": int.from_bytes(edid.madedate[1]) + 1990
    }

    version_bytes = str(int.from_bytes(edid.edidver[0])) + \
                    "." + \
                    str(int.from_bytes(edid.edidver[1]))

    size_bytes = {
        "长": str(int.from_bytes(edid.displaysize[0])) + "cm",
        "宽": str(int.from_bytes(edid.displaysize[1])) + "cm"
    }

    gamma_bytes = (int.from_bytes(edid.gamma[0]) + 100) / 100

    sRGB_table = {
        "红色": {
            'x': (int(getBytes(edid.Rhi[0], 4), 2) + int(getBytes(edid.RGLo[0])[:2], 2)) / 1024,
            'y': (int(getBytes(edid.Rhi[1], 4), 2) + int(getBytes(edid.RGLo[0])[2:4], 2)) / 1024
        },
        "绿色": {
            'x': (int(getBytes(edid.Ghi[0], 4), 2) + int(getBytes(edid.RGLo[0])[4:6], 2)) / 1024,
            'y': (int(getBytes(edid.Ghi[1], 4), 2) + int(getBytes(edid.RGLo[0])[6:8], 2)) / 1024
        },
        "蓝色": {
            'x': (int(getBytes(edid.Bhi[0], 4), 2) + int(getBytes(edid.BWLo[0])[:2], 2)) / 1024,
            'y': (int(getBytes(edid.Bhi[1], 4), 2) + int(getBytes(edid.BWLo[0])[2:4], 2)) / 1024
        },
        "白点值": {
            'x': (int(getBytes(edid.Whi[0], 4), 2) + int(getBytes(edid.BWLo[0])[4:6], 2)) / 1024,
            'y': (int(getBytes(edid.Whi[0], 4), 2) + int(getBytes(edid.BWLo[0])[6:8], 2)) / 1024
        }
    }

    extra_timing = [timingTable([getBytes(edid.extraTiming[0][0]),
                                 getBytes(edid.extraTiming[0][1])], '3', '4', False),
                    timingTable([getBytes(edid.extraTiming[1][0]),
                                 getBytes(edid.extraTiming[1][1])], '5', '6', False),
                    timingTable([getBytes(edid.extraTiming[2][0]),
                                 getBytes(edid.extraTiming[2][1])], '7', '8', False),
                    timingTable([getBytes(edid.extraTiming[3][0]),
                                 getBytes(edid.extraTiming[3][1])], '9', '10', False),
                    timingTable([getBytes(edid.extraTiming[4][0]),
                                 getBytes(edid.extraTiming[4][1])], '11', '12', False),
                    timingTable([getBytes(edid.extraTiming[5][0]),
                                 getBytes(edid.extraTiming[5][1])], '13', '14', False),
                    timingTable([getBytes(edid.extraTiming[6][0]),
                                 getBytes(edid.extraTiming[6][1])], '15', '16', False),
                    timingTable([getBytes(edid.extraTiming[7][0]),
                                 getBytes(edid.extraTiming[7][1])], '17', '18', False),
                    ]

    frequency_bytes = (int.from_bytes(edid.frequency[0]) * 256 + (int.from_bytes(edid.frequency[1]))) / 100

    hvendorPixel_bytes = int(getBytes(edid.pixel2[2])[:4], 2) * 256 + int(getBytes(edid.pixel2[0]), 2)
    hvendorBlank_bytes = int(getBytes(edid.pixel2[1]), 2) + int(getBytes(edid.pixel2[2])[4:8], 2)
    vvendorPixel_bytes = int(getBytes(edid.pixel3[2])[:4], 2) * 256 + int(getBytes(edid.pixel3[0]), 2)
    vvendorBlank_bytes = int(getBytes(edid.pixel3[1]), 2) + int(getBytes(edid.pixel3[2])[4:8], 2)

    hoffset = int(getBytes(edid.signalOffset[3], 256)[:2] + getBytes(edid.signalOffset[0]), 2)
    hsignalwidth = int(getBytes(edid.signalOffset[3], 256)[2:4] + getBytes(edid.signalOffset[1]), 2)
    voffset = int(getBytes(edid.signalOffset[3], 16)[4:6] + getBytes(edid.signalOffset[2])[:4], 2)
    vsignalwidth = int(getBytes(edid.signalOffset[3], 16)[6:8] + getBytes(edid.signalOffset[2])[4:8], 2)

    himageSize = int(getBytes(edid.imageSize[2])[:4] + getBytes(edid.imageSize[0]), 2)
    vimageSize = int(getBytes(edid.imageSize[2])[4:8] + getBytes(edid.imageSize[1]), 2)
    hborder = int.from_bytes(edid.borders[0])
    vborder = int.from_bytes(edid.borders[1])

    flagsTable = dumpFLags(getBytes(edid.flags[0]))

    if edid.identifier == [b'\x00', b'\xff', b'\xff', b'\xff', b'\xff', b'\xff', b'\xff', b'\x00']:
        print("EDID有效")
    else:
        _exit("EDID无效", 1)

    print("在你的edid文件中，屏幕的制造商是:", getCodeName(first) + getCodeName(second) + getCodeName(third))
    print("产品ID是:", id_bytes)
    print("产品序列号是:", serical_bytes)
    print("制造日期是:", madedate_bytes)
    print("EDID Version:", version_bytes)
    print("基本信息:")
    input_table = inputTable(getBytes(edid.inputmethod[0]))
    for x in input_table:
        print("\t", x, " => ", input_table[x])
    print("屏幕尺寸是:", size_bytes)
    print("屏幕伽玛值是:", "%f" % gamma_bytes)
    base_table = dpmsTable("{0:08b}".format(int.from_bytes(edid.dpms[0], byteorder='big')))
    print("屏幕的基本色彩信息:")
    for x in base_table:
        print("\t", x, " => ", base_table[x])
    print("屏幕的sRGB颜色空间:")
    for x in sRGB_table:
        print("\t", x, " => ", sRGB_table[x])
    print("支持的制式:")
    for x in timing_table:
        print("\t", x, " => ", timing_table[x])
    print("额外的制式(可能不准确):")
    for x in range(0, len(extra_timing)):
        for y in extra_timing[x]:
            print("\t", y, " => ", extra_timing[x][y])
    print("像素的时钟频率:", frequency_bytes, "MHz")
    print("制造商写的横向像素数量:", hvendorPixel_bytes)
    print("制造商写的横向空白像素数量:", hvendorBlank_bytes)
    print("制造商写的垂直像素数量:", vvendorPixel_bytes)
    print("制造商写的垂直空白像素数量:", vvendorBlank_bytes)
    print("制造商写的水平信号偏移量:", hoffset)
    print("制造商写的水平信号脉冲宽度:", hsignalwidth)
    print("制造商写的垂直信号偏移量:", voffset)
    print("制造商写的垂直信号脉冲宽度:", vsignalwidth)
    print("制造商写的水平图像尺寸:", himageSize, "毫米")
    print("制造商写的垂直图像尺寸:", vimageSize, "毫米")
    print("Horizontal Border out of display's addressable area written by vendor:", hborder)
    print("Vertical Border out of display's addressable area written by vendor:", vborder)
    print("信号标志位:")
    for x in flagsTable:
        print("\t", x, " => ", flagsTable[x])
    print("显示器的描述符表:")
    mddtable = dumpMDD(edid.MDDTable[0])
    for x in mddtable:
        print("\t", x, " => ", mddtable[x])
    mddtable = dumpMDD(edid.MDDTable[1])
    for x in mddtable:
        print("\t", x, " => ", mddtable[x])
    mddtable = dumpMDD(edid.MDDTable[2])
    for x in mddtable:
        print("\t", x, " => ", mddtable[x])
    sum = edidVerify(getStream(content, 0, 128))
    print("最后的效验和(能和256整除代表有效):", sum)
    print(sum, "% 256 == 0 ->", sum % 256 == 0)
