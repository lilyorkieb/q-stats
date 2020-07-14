import pandas as pd
import matplotlib.pyplot as plt
import collections
import statistics

def num_matches(delta, window, q_posts, trump_tweets):
    num = 0
    for t in trump_tweets:
        for q in q_posts:
            if (q < (t-delta) and q > (t-(delta+window))):          #q posts first
            #if q > (t-(delta+window)) and q < (t-(delta-window)):  #either one posts first
                num = num + 1
                break
    return num

def create_plot(window_seconds, step_minutes, max_step_minutes):
    bin_map = {}
    bins = range(0, max_step_minutes+step_minutes, step_minutes)
    for i in bins:
        bin_map[i] = num_matches(i*60, window_seconds, df.q.tolist(), df.trump.tolist())
    bin_map = collections.OrderedDict(sorted(bin_map.items()))
    average = 0
    for k,v in bin_map.iteritems():
        average = average + v
    average = average/len(bin_map.keys())
    std = statistics.stdev(bin_map.values())

    plt.bar(range(len(bins)), bin_map.values(), align='center')
    plt.xticks(range(len(bins)), bin_map.keys())
    plt.axhline(y=average)
    plt.axhline(y=average+std)
    plt.axhline(y=average-std)
    plt.ylabel('num posts (q first)')
    plt.xlabel('delta (minutes)')
    for i, label in enumerate(plt.gca().xaxis.get_ticklabels()):
        if(i % 5 != 0):
            label.set_visible(False)
    plt.show(block=True)


df = pd.read_csv('q-trump-combined.csv', index_col=0)
create_plot(60, 1, 120)


