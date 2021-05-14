import matplotlib.pyplot as plt
import numpy as np

men_means = (0.769, 0.893, 0.891, 0.579, 0.830, 0.682, 0.278,
             0.576, 0.894, 0.943, 0.773, 0.773, 0.939, 0.881, 0.937, 0.145, 0.890, 0.476, 0.920)

ind = np.arange(len(men_means))  # the x locations for the groups
width = 0.6 # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, men_means, width,
                color='#4472C4')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('DICE coefficient')
ax.set_title('Testing set')
ax.set_xticks(ind)
ax.set_xticklabels(('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                    '15', '16', '17', '18', '19', '平均值'))
ax.hlines(0.740, -1, 19, linestyles='--', colors='r')
ax.legend()

#plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
#plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.
    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.5, 'left': 0.5}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


# ax.plot(men_means[:5],5,'--')

autolabel(rects1, "center")

plt.annotate(u"Mean:0.740", xy=(19, 0.740), xytext=(19, 0.9), arrowprops=dict(facecolor='red', shrink=0.1, width=2))
#plt.savefig("D:/1.jpg")
plt.show()