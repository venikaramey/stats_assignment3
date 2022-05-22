import scipy.stats as sts
from scipy.stats import norm
import math
import numpy as np

# Problem statement 1
print("# Problem statement 1")
p_mean = 100
p_std = 15
n = 36
sample_mean = 108
alpha = 0.05
SE = p_std/n**0.5
print(f"SE: {SE}")
Z = (sample_mean-p_mean)/SE
print(f"Z_score: {Z}")
print("by looking at z- table and p-value associated with 3.20 is 0.9993")
print("The probability of having value less than 108 is 0.9993 and more than or equals to 108 is (1-0.9993)=0.0007.")
print("Sice the probability of having mean glucose level more than or equals to 108  is 0.0007 which is  less than 0.05 so we will reject the Null hypothesis i.e. there is raw cornstarch effect.")

# Problem statement 2
print("# Problem statement 2")
n1 = 100
n2 = 100
R1 = 0.52            #Republicans from state 1
D1 = 0.48            #Democrats from state 1
R2 = 0.47            #Republicans from state 2
D2 = 0.53            #Democrats from state 2

mu = R1 - R2
print(f"mu: {mu}")
std = math.sqrt(((R1 * D1 ) / n1) + ((R2 * D2) /n2))
print(f"std: {std}")
x = 0
Z_R1_R2 = ( x - mu)/std
print(f"Z_p1_p2 : {Z_R1_R2}")
print("From Z table we find that the probability of a z-score being -0.7082 or less is 0.24.")
print("Therefore, the probability that the survey will show a greater percentage of Republican voters in the second state than in the first state is 0.24")

# Problem statement 3
print("# Problem statement 3")
#The z score tells you how many standard deviations from the mean your score is
x = 1100 #
mu = 1026 # Population Mean
sd = 209 #population standard deviation
z = ( x - mu)/sd
print("Z Score : ",z)
#the above calculation shows that my score is 0.35 standard deviations above the mean
print("My Score is in the range {} - {}  with a  zscore {:.2f}".format(mu - sd,mu + sd,z))