import random
import statistics
import plotly.figure_factory as ff 

df = pd.read_csv("data.csv")  
data = df["math score"].tolist()

mean = sum(data)/len(data)
stddev = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

fsds, fsde = mean - stddev, mean + stddev
stds, stde = mean - (2 * stddev), mean + (2 * stddev)
tsds, tsde = mean - (3 * stddev), mean + (3 * stddev) 

listWithinFirst = [result for result in data if result > fsds and result < fsde]
listWithinSecond = [result for result in data if result > stds and result < stde]
listWithinThird = [result for result in data if result > tsds and result < tsde]

print("% within first stddev ", len(listWithinFirst)*100.0/len(data))
print("% within second stddev ", len(listWithinSecond)*100.0/len(data))
print("% within third stddev ", len(listWithinThird)*100.0/len(data))

print("Mean = ", mean)
print("Standard Deviation = ", stddev)
print("Median = ", median)
print("Mode = ", mode)

fig = ff.create_distplot([data],["Result"], show_hist = False)
fig.show()