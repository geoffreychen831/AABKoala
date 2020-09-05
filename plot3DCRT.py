import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.image as mpimg
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,
                                  AnnotationBbox)
from matplotlib.cbook import get_sample_data


def all_data():
    # load 3DCRT data
    df = pd.read_excel("./Book1.xlsx")
    print(df)

    # print(df.groupby(["x-axis"]).count())
    # axis = df["x-axis"].unique()

    # y
    del df["x-axis"]
    # x-axis pos
    x = pd.DataFrame({"x": 263 * (1, 2, 3, 4, 5, 6,
                                  7, 8, 9, 10, 11, 12,
                                  14, 16.5, 21.5, 24, 29, 31.5,
                                  34.5, 35.5, 36.5, 37.5, 38.5, 39.5,
                                  41.5, 42.5, 43.5, 44.5, 45.5, 46.5,
                                  52, 53, 54, 55,
                                  59, 60, 61, 62)})
    # x = pd.DataFrame({"x": 263 * list(range(1, 39))})
    df["x"] = x
    print(df)

    # adjust canvas size
    plt.figure(figsize=(8.4, 4.8))

    # scatter plot
    allData = plt.scatter(df["x"], df["a"], s=4, c="#424242", zorder=5)

    # set axis
    xlabel_pos = np.unique(df["x"])
    plt.xticks(xlabel_pos, ('6', '10', '15', '18', '6FFF', "10FFF",
                            "6", "10", "15", '18', '6FFF', '10FFF',
                            '6', '6', "6", "6", "6", "6",
                            '6', '10', '15', '18', '6FFF', "10FFF",
                            "6", "10", "15", '18', '6FFF', '10FFF',
                            '6', '10', "15", "18",
                            "6", "10", "15", "18"), rotation=90, fontsize=7)
    plt.yticks(fontsize=7)
    plt.ylim(-0.1, 0.1)

    # add green background
    ax1 = plt.gca()
    ax1.axhspan(-0.03, 0.03, facecolor="#C5E1A5", alpha=1, zorder=2)
    ax1.axhspan(-0.05, 0.05, facecolor="#F1F8E9", alpha=1, zorder=1)
    # ax.set_facecolor("#99FF99")

    # set white margins
    plt.subplots_adjust(left=0.08, right=0.83)

    # set legend
    plt.legend([allData], ['All Data'], bbox_to_anchor=(1.23, 1))

    # save fig
    plt.savefig("3DCRT.png", dpi=300)
    # plt.show()
