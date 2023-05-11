import time
import gc
from matplotlib import pyplot as plt
from KMP import kmp_search
from naive import naive_search
from KR import KRsearch


def main():
    with open("pan-tadeusz-unix.txt", "r", encoding="utf-8") as file:
        text = file.read()
    save_search_graph(text, "SOLO_KR_joined_search_graph.png")



def save_search_graph(text, title):
    words = text.split(" ")
    x_axis = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    y_naive_axis = []
    y_kmp_axis = []
    y_kr_axis = []
    # for data in x_axis:
    #     arr = words[:data]
    #     gc_old = gc.isenabled()
    #     gc.disable()
    #     start = time.process_time()
    #     for word in arr:
    #         naive_search(text, word)
    #     stop = time.process_time()
    #     if gc_old: gc.enable()
    #     y_naive_axis.append(stop - start)

    for data in x_axis:
        arr = words[:data]
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for word in arr:
            KRsearch(text, word)
        stop = time.process_time()
        if gc_old: gc.enable()
        y_kr_axis.append(stop - start)

    # for data in x_axis:
    #     arr = words[:data]
    #     gc_old = gc.isenabled()
    #     gc.disable()
    #     start = time.process_time()
    #     for word in arr:
    #         kmp_search(text, word)
    #     stop = time.process_time()
    #     if gc_old: gc.enable()
    #     y_kmp_axis.append(stop - start)

    #plt.plot(x_axis, y_naive_axis, '-',label="naive search")
    #plt.plot(x_axis, y_kmp_axis, '-',label="KMP search")
    plt.plot(x_axis, y_kr_axis, '-',label="KR search")
    plt.legend()
    plt.title(label='Searching in text with different algorithms time graphs')
    plt.yticks(color='red')
    plt.xlabel(xlabel='Number of words to search')
    plt.ylabel(ylabel='Time in s')
    plt.grid(True)
    plt.savefig(title, dpi=200)


if __name__ == "__main__":
    main()