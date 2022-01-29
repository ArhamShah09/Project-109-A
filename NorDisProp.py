import pandas as pd
import statistics as st

df = pd.read_csv("StudentsPerformance.csv")

score = df["math score"].tolist()

score_mean = st.mean(score)

score_mode = st.mode(score)

score_median = st.median(score)
print(score_mean, score_mode, score_median)

score_stdev = st.stdev(score)
print(score_stdev)

stdev_1_start = score_mean-score_stdev
stdev_1_end = score_mean+score_stdev

stdev_2_start = score_mean-(2*score_stdev)
stdev_2_end = score_mean+(2*score_stdev)

stdev_3_start = score_mean-(3*score_stdev)
stdev_3_end = score_mean+(3*score_stdev)

score_data_within_1_stdev = [result for result in score if result > stdev_1_start and result < stdev_1_end]
score_data_within_2_stdev = [result for result in score if result > stdev_2_start and result < stdev_2_end]
score_data_within_3_stdev = [result for result in score if result > stdev_3_start and result < stdev_3_end]

percent_scoredata_within_1_stdev = (len(score_data_within_1_stdev)/len(score))*100
percent_scoredata_within_2_stdev = (len(score_data_within_2_stdev)/len(score))*100
percent_scoredata_within_3_stdev = (len(score_data_within_3_stdev)/len(score))*100

print(percent_scoredata_within_1_stdev)
print(percent_scoredata_within_2_stdev)
print(percent_scoredata_within_3_stdev)