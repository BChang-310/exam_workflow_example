import numpy as np
import sys


############################
# Read Exam Template ipynb #
############################
# Open exam ipynb, save the text as a variable, close the file
exam_file = open("Exam1A_Fall2021.ipynb", 'r')
exam_text = exam_file.read()
exam_file.close()

#######################
# Randomize Questions #
#######################
def to_ascii(a_string):
    return np.sum([ord(c) for c in a_string])

ascii_random_seed = to_ascii(sys.argv[1])  # Set random seed, this will be an input (based on username) on the GitHub workflow
np.random.seed(ascii_random_seed)

# Question 1 #
##############
q1_A = np.random.randint(0, 30, size=12)
q1_B = np.random.randint(0, 30, size=12)
q1_u = np.random.randint(0, 30, size=3)
q1_w = np.random.randint(0, 30, size=3)
q1_alpha = np.random.randint(0, 30, size=1)[0]  # returns as a list so just get the number
q1_beta = np.random.randint(0, 30, size=1)[0]

# Sorry the TMP variables are named in a funky way...for some reason replace wasn't agreeing with me - Alex
for i in range(len(q1_A)):
    exam_text = exam_text.replace(fr'TMPA{i}A', f"{q1_A[i]}")
    exam_text = exam_text.replace(fr'TMPB{i}B', f"{q1_B[i]}")

for i in range(len(q1_u)):
    exam_text = exam_text.replace(f"TMPU{i}", f"{q1_u[i]}")
    exam_text = exam_text.replace(f"TMPW{i}", f"{q1_w[i]}")

exam_text = exam_text.replace(f"TMPALPHA", f"{q1_alpha}")
exam_text = exam_text.replace(f"TMPBETA", f"{q1_beta}")

# Question 2 #
##############
q2_a = np.random.randint(0, 5, size=1)[0]
q2_b = np.random.randint(6, 10, size=1)[0]
exam_text = exam_text.replace(f"TMP21", f"{q2_a}")
exam_text = exam_text.replace(f"TMP22", f"{q2_b}")

# Question 3 #
##############
# Nothing to randomize

# Question 4 #
##############
q4_X = np.random.randint(0, 50, size=4)
q4_Y = np.random.randint(0, 50, size=4)

for i in range(len(q4_X)):
    exam_text = exam_text.replace(fr'TMP4{i}X', f"{q4_X[i]}")
    exam_text = exam_text.replace(fr'TMP4{i}Y', f"{q4_Y[i]}")

# Question 5 #
##############
# inspired by depths in meters in Fig.4., Greenberg & Castagna (1992)
depth = np.arange(2600, 2700, 0.5)
N = len(depth)

# randomize starting depth
depth += np.random.randint(60) * 10

# range for Dp is set to [200,250] ms/km, somewhat inspired
# by Fig.4. Greenberg & Castagna (1992)
Dp_min = 200
Dp_max = 250
Dp = Dp_min + (Dp_max - Dp_min) * np.random.rand(N)

# Model used for synthetic data: Greenberg & Castagna (1992)
# Table 1, sandstone reference
# where Vs, Vp assumed in km/s

# Vs = 0.80416*Vp - 0.85588
#
Vp = (1000 / Dp)  # in km/s
Vs = (0.80416 * Vp - 0.85588)  # in km/s
Ds = (1000 / Vs)  # in km/ms

file = open('acoustic.txt', 'w')

file.write('Acoustic travel times for South Texas Clastic Formation\n')
file.write('Depth (m)       Dp (ms/km)      Ds (ms/km)\n')

for i in range(N):
    line = str(depth[i]) + '    ' + str(Dp[i]) + '    ' + str(Ds[i]) + '\n'
    file.write(line)
file.close()

# Question 6 #
##############
# Nothing to randomize

###############################
# Write Randomized Exam ipynb #
###############################
# The name of the output can be modified, but can keep the same since GitHub is taking care of distribution.
# Renaming it to something new for testing
output_file = open('Exam1A_Fall2021.ipynb', 'w')
output_file.write(exam_text)
output_file.close()
