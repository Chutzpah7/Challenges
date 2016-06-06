import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')
import numpy as np
import time, random, math

size=11

#array = random.sample((range(1, size + 1)), size)
array = list(xrange(size, 0, -1))
def bubble_sort(arr, rects):
	sorted = True
	for x in range(0, size - 1):
		update_plot(arr, '#000000', x-1, x+1, 0, rects)
		update_plot(arr, '#f3f315', x, x + 2, .3, rects)
		if arr[x] > arr[x + 1]:
			tmp = arr[x]
			arr[x] = arr[x + 1]
			arr[x + 1] = tmp
			sorted = False
		update_plot(arr, '#32cd32', x, x + 2, .3, rects)
	update_plot(arr, '#000000', size - 2, size, 0, rects)
	if not sorted:
		bubble_sort(arr, rects)
	else:
		update_plot(arr, '#32cd32', 0, size, 0, rects)

def update_plot(arr, color, first, last, nsecs, rects):
	for x in range(first, last):
		rects[x].set_height(arr[x])
		rects[x].set_facecolor(color)
		fig.canvas.draw()
	if nsecs != 0:
		time.sleep(nsecs)

def animated_barplot():
	width = 1
	rects = plt.bar(range(size), array, width, align = 'center', color='k')
	plt.title("Bubble Sort")
	plt.xlabel("Index")
	plt.tick_params(axis='both', labelbottom='off', labeltop='off', top='off', labelleft='off', left='off', labelright='off', right='off')
	plt.xticks(np.arange(size), tuple(map(str, range(size))))
	bubble_sort(array, rects)

fig = plt.figure()
win = fig.canvas.manager.window
win.after(10, animated_barplot)
plt.show()