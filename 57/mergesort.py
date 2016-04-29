import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')
import numpy as np
import time, random,math

size=32

colors = ['r', 'b', 'g', '#ff7f00', 'y', 'c', 'm']

array = random.sample((range(1,size+1)),size)

def mergeSort(arr, first, last, tmp, rects):
	if last - first < 2:
		return
	middle = (last + first) / 2
	
	mergeSort(arr, first, middle, tmp, rects)
	mergeSort(arr, middle , last, tmp, rects)

	i = first
	j = middle
	for k in range(first, last):
		if i < middle and (j >= last or arr[i] <= arr[j]):
			tmp[k] = arr[i]
			i += 1
		else:
			tmp[k] = arr[j]
			j += 1

	for x in range(first, last):
		arr[x] = tmp[x]

	update_plot(arr, first, last, rects)

def update_plot(arr, first, last, rects):
	if first == last:
		print(str(last) + " " + str(first))
		color = 'k'
	else:
		print(str(last) + " " + str(first))
		color = colors[int(math.log(last-first,2))]
	for x in range(first, last):
		rects[x].set_height(arr[x])
		rects[x].set_facecolor(color)
		fig.canvas.draw()
	time.sleep(1)

def animated_barplot():
	width = 1
	rects = plt.bar(range(size), array, width, align = 'center', color=colors[len(colors) - int(math.log(size)) + 1])
	plt.title("Merge Sort")
	plt.xlabel("Index")
	plt.tick_params(axis='both', labelbottom='off', labeltop='off', top='off', labelleft='off', left='off', labelright='off', right='off')
	plt.xticks(np.arange(size), tuple(map(str, range(size))))
	mergeSort(array, 0, size, [None]*size, rects)

fig = plt.figure()
win = fig.canvas.manager.window
win.after(10, animated_barplot)
plt.show()
