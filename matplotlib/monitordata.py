# _*_ codeing:utf-8 _*_
# Author: Tjj   Date: 2018/4/20

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.image as img
import matplotlib as mpl
import matplotlib.animation as animation
import time, threading
import random





# 修改matplotlib属性参数如轴线颜色
mpl.rcParams['ytick.color'] = 'white'
mpl.rcParams['xtick.color'] = 'white'
mpl.rcParams['axes.edgecolor'] = 'white'

# 读取背景图片
bgimg = img.imread('./img/bgimg.jpg')
mapimg = img.imread('./img/map.jpg')


# 定制画布(figure)
def make_figure():

    # 首先创建画布
    fig = plt.figure(figsize=(12, 5))

    # 设置画布背景图片,需要考虑背景图片尺寸是否大于画布尺寸，若小于会有空白背景
    fig.figimage(bgimg)
    return fig

# 定制子图(axes)
def make_axes(fig):
    # 调整子图间的布局
    fig.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.1, hspace=0.3, wspace=0.8)

    # 绘制左侧一列的绘图区(子图subplot)
    ax1 = plt.subplot2grid((3, 12), (0, 0), colspan=3, fc='greenyellow')

    ax2 = plt.subplot2grid((3, 12), (1, 0), colspan=3, fc='lightgreen')
    ax2.set_xlim(-1, 1)  # 设置X轴坐标限制范围
    ax2.set_ylim(-1, 1)  # 设置X轴坐标限制范围
    ax2.spines['right'].set_visible(False)  # 设置右侧轴不可见
    ax2.spines['top'].set_visible(False)  # 设置上边轴不可见
    ax2.spines['left'].set_position('center')  # 将左侧轴设置到中间显示
    ax2.spines['bottom'].set_position('center')  # 将底部轴设置到中间显示

    ax3 = plt.subplot2grid((3, 12), (2, 0), colspan=3, fc='springgreen')

    # 绘制中间一列的绘图区(子图subplot)
    ax4 = plt.subplot2grid((3, 12), (0, 3), rowspan=2, colspan=6, fc='None')
    # ax4.imshow(mapimg)

    ax5 = plt.subplot2grid((3, 12), (2, 3), colspan=2, fc='aqua', polar=True)

    ax6 = plt.subplot2grid((3, 12), (2, 5), colspan=2, fc='dodgerblue', polar=True)
    ax6.yaxis.set_major_locator(ticker.NullLocator())

    ax7 = plt.subplot2grid((3, 12), (2, 7), colspan=2, fc='royalblue', polar=True)
    ax7.yaxis.set_major_locator(ticker.NullLocator())

    # 绘制右侧一列的绘图区(子图subplot)
    ax8 = plt.subplot2grid((3, 12), (0, 9), colspan=3, fc='plum', polar=True)

    ax9 = plt.subplot2grid((3, 12), (1, 9), colspan=3, fc='mediumpurple')

    ax10 = plt.subplot2grid((3, 12), (2, 9), colspan=3, fc='purple', polar=True)

    return ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10


# 定制数据区(plot)
def make_plot(axeslist):
    axeslist[0].set_xlim(0, 100)
    axeslist[0].set_ylim(0, 100)

    axeslist[2].set_xlim(0, 100)
    axeslist[2].set_ylim(0, 100)
    # 子图1进行数据绘制初始化
    ln1, = axeslist[0].plot([], [], 'ro')

    # 子图3进行数据绘制初始化
    ln3, = axeslist[2].plot([], [])
    return ln1, ln3


# 线程模块
def loop_1():
    print('thread %s is running...' % threading.current_thread().name)
    while True:
        x_data_1.append(random.randint(1, 100))
        y_data_1.append(random.randint(1, 100))
        print('x_data_1:', x_data_1)
        print('y_data_1:', y_data_1)
        time.sleep(6)



# 线程模块
def loop_3():
    print('thread %s is running...' % threading.current_thread().name)
    while True:
        x_data_3.append(random.randint(1, 100))
        y_data_3.append(random.randint(1, 100))
        print('x_data_3:', x_data_3)
        print('y_data_3:', y_data_3)
        time.sleep(6)



def data_gen():
    if x_data_1.__len__() != 0 and y_data_1.__len__() != 0:
        yield 1, x_data_1.pop(), y_data_1.pop()
    yield None

    if x_data_3.__len__() != 0 and y_data_3.__len__() != 0:
        yield 3, x_data_3.pop(), y_data_3.pop()
    yield None

'''
def init():
    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)

    ax3.set_xlim(0, 100)
    ax3.set_ylim(0, 100)
    #return ln,
'''

def update(data, *fargs):
    if data != None:
        if data[0] == 1:
            ax1_xdata.append(data[1])
            ax1_ydata.append(data[2])

            fargs[0].set_data(ax1_xdata, ax1_ydata)
        elif data[0] == 3:
            ax3_xdata.append(data[1])
            ax3_ydata.append(data[2])
            fargs[1].set_data(ax3_xdata, ax3_ydata)
    #return ln,



if __name__ == '__main__':

    x_data_1 = []
    y_data_1 = []

    x_data_3 = []
    y_data_3 = []

    ax1_xdata, ax1_ydata = [], []
    ax3_xdata, ax3_ydata = [], []

    thd_1 = threading.Thread(target=loop_1, name='LoopThread_1')
    thd_3 = threading.Thread(target=loop_3, name='LoopThread_3')
    thd_1.start()
    thd_3.start()

    fig = make_figure()
    axeslist = []
    axeslist = make_axes(fig)
    lnlist = []
    lnlist = make_plot(axeslist)
    ani = animation.FuncAnimation(fig, update, frames=data_gen, blit=False, fargs=lnlist)

    plt.show()
