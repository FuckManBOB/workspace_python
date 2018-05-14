##Matplotlib图像组成


###通常情况下，我们可以将Matplotlib图像分成三层结构:

###画布：figure

###绘图区：axes

###数据区：plot



	matplotlib.pyplot.subplot(*args, **kwargs)
	在给定的网格位置返回一个坐标轴子图




## matplotlib.pyplot.figure

### API figure
	
	matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)

	Parameters:
				num : 整型或字符串类型，可选参数，默认值为none










### 绘图布局的创建主要有三种方法：
- fig, axes = pyplot.subplots(行数,列数)

- axes = figure.add_subplot(行数,列数,序号)

- axes = figure.add_axes([left,bottom,width,height])

在学习这三种方法之前我们首先需要了解以下几点知识点：

- 无论使用何种方法创建，每一个axes都是一个独立的图层

- 每个图层除了绘图区以外都是透明的

- 图层之间相互独立互不影响

- 当两个axes绘图区之间有重叠的时候，创建命令在前的axes图层位置更靠近底层

- axes.set_zorder()方法可改变当前图层层次高度，参数值越小位置越靠近底层




##matplotlib.animation.FuncAnimation
FuncAnimation常用于动态图的绘制，通过反复调用函数func来制作动画

class matplotlib.animation.FuncAnimation(fig, func, frames=None, init_func=None, fargs=None, save_count=None, **kwargs)

介绍下该类的接口及使用：

参数介绍：
	
	fig:
		# 画布对象:用于绘制，调整大小和其他所需事件的图形对象
	 	matplotlib.figure.Figure 
	
	func:
		# 被重复调用的函数（由第三个参数按照指定方式来同步触发func），一般被用于坐标图形的绘制
		callable
		eg:
			# 实现了类FuncAnimation后func会以帧的方式被frames同步触发重复调用，并且函数中的参数均由类参数中的frames和fargs指定。*fargs可以设置也可以不设置。
			def func(frame, *fargs)

	frames：
			#  类型可以是迭代器、生成器函数、整型，默认选项None
		eg:
			# 整型： func(frame)每帧调用都会从0开始，下次为1，在下次调用为2...直到调用frame为4时，重新以0开始，周而复始。
			frames=5

			# 迭代器：frames=np.linspace(0, 2*np.pi, 128)
					
			#生成器函数：frames=data_gen
						def data_gen():
		    				if x_data.__len__() != 0 and y_data.__len__() != 0:
		        				yield x_data.pop(), y_data.pop()
		    				yield None

			注：这里会将yield即迭代的结果传给func函数的第一个参数来为func提供服务。

			# 默认为None时：frame作为每帧调用func函数的参数从0开始一直递增
			frames=None

	init_func：
			# 用于初始化要显示的图形的函数。 如果该参数为None，则按照func被调用的第一帧为初始图形结果来显示，若设置了初始化函数，该功能将在第一帧之前被调用一次。
			注意：如果blit参数设置了True，init_func函数必须返回一组可重绘的plt.plot的返回值。
			
	
	fargs：
			# fargs参数为tuple或者默认None，用于给func传递额外所需的参数。

	save_count：
			# save_count参数为整型或者默认None，

	interval：
			# interval参数为数字或者默认None，用于每一帧(frame)调用时的时间间隔。默认为200ms

	repeat_delay：
			# repeat_delay参数为数字或者默认为None，用于延迟动画绘制，即使frame触发了func进行绘制，但视图绘制也会按照repeat_delay设置的延迟时间进行显示。

	repeat：
			# repeat参数为布尔值默认为True，用于控制当帧序列完成时动画是否应该重复。

	blit：
			# blit参数为布尔值默认为False，控制是否使用blitting来优化绘图。

			注意：blit为True时，均需要返回iterable_of_artists，否则会出错
				 def func(frame, *fargs) -> iterable_of_artists:
				 def init_func() -> iterable_of_artists:
		