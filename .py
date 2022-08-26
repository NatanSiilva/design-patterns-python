

import matplotlib.pyplot as plt

def media_movel(value, window):
    length = len(value) 
    mm = []
    
    for i in range(window, length):
        media = sum(value[i-window:i]) / window
        mm.append(media)
        
    return mm

# mm_list = [ i for i in range(0, 50)]
# # print(media_movel(mm_list, 5))


# x = range(0, 30)
# y = media_movel(mm_list, 9)
# print(y)
# plt.plot(10, y)
# plt.show()
