import matplotlib.pyplot as plt
import numpy as np

methods = ['lz4', 'bzip2','lz4hc','lzma', 'snappy', 'zstd', 'zlib']
speeds = [100, 200, 300, 400, 500, 600, 700]
IPP = [50, 60, 40, 50, 80, 70, 40]
Vanilla = [10, 20, 30, 40, 50, 60, 70]

barWidth = 0.25
#br1 = np.arange(len(speeds))
#br2 = [x + barWidth for x in br1]
#br3 = [x + barWidth for x in br2]

plt.bar(methods,speeds, color='r', width=0.25)
plt.bar(methods,IPP, color='b', width=0.25)
plt.bar(methods,Vanilla, color='g',width=0.25)
plt.title('Compression Speed in MB/s')
plt.xlabel('methods')
plt.ylabel('compression speed in MB/s')
plt.legend(loc='best')  # legend text comes from the plot's label parameter.
plt.show()
