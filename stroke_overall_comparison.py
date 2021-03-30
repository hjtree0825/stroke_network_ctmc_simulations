from stroke_functions import *

repl_num = 100

# Base case
open_file = open("base_mean.pkl", "rb")
loaded_list = pickle.load(open_file)
open_file.close()
Mean1 = loaded_list[0]
Mean2 = loaded_list[1]
Mean3 = loaded_list[2]

open_file = open("base_std.pkl", "rb")
loaded_list = pickle.load(open_file)
open_file.close()
STD1 = loaded_list[0]
STD2 = loaded_list[1]
STD3 = loaded_list[2]

# Base case + added capacity
open_file = open("base_cap_mean.pkl", "rb")
loaded_list = pickle.load(open_file)
open_file.close()
Mean1_cap = loaded_list[0]
Mean2_cap = loaded_list[1]
Mean3_cap = loaded_list[2]

open_file = open("base_cap_std.pkl", "rb")
loaded_list = pickle.load(open_file)
open_file.close()
STD1_cap = loaded_list[0]
STD2_cap = loaded_list[1]
STD3_cap = loaded_list[2]

# Expanded case
open_file = open("base_psc_mean.pkl", "rb")
loaded_list = pickle.load(open_file)
open_file.close()
Mean1_psc = loaded_list[0]
Mean2_psc = loaded_list[1]
Mean3_psc = loaded_list[2]

open_file = open("base_psc_std.pkl", "rb")
loaded_list = pickle.load(open_file)
open_file.close()
STD1_psc = loaded_list[0]
STD2_psc = loaded_list[1]
STD3_psc = loaded_list[2]

# Expanded case + added capacity
open_file = open("base_psc_cap_mean.pkl", "rb")
loaded_list = pickle.load(open_file)
open_file.close()
Mean1_psc_cap = loaded_list[0]
Mean2_psc_cap = loaded_list[1]
Mean3_psc_cap = loaded_list[2]

open_file = open("base_psc_cap_std.pkl", "rb")
loaded_list = pickle.load(open_file)
open_file.close()
STD1_psc_cap = loaded_list[0]
STD2_psc_cap = loaded_list[1]
STD3_psc_cap = loaded_list[2]

# Expanded case + reduced transfer rates
open_file = open("base_psc_red_mean.pkl", "rb")
loaded_list = pickle.load(open_file)
open_file.close()
Mean1_psc_red = loaded_list[0]
Mean2_psc_red = loaded_list[1]
Mean3_psc_red = loaded_list[2]

open_file = open("base_psc_red_std.pkl", "rb")
loaded_list = pickle.load(open_file)
open_file.close()
STD1_psc_red = loaded_list[0]
STD2_psc_red = loaded_list[1]
STD3_psc_red = loaded_list[2]

labels = ["0.15", "0.35", "0.55"]
M1 = [Mean1[0][len(Mean1[0])-1], Mean2[0][len(Mean2[0])-1], Mean3[0][len(Mean3[0])-1]]
M2 = [Mean1_psc[0][len(Mean1_psc[0])-1], Mean2_psc[0][len(Mean2_psc[0])-1], Mean3_psc[0][len(Mean3_psc[0])-1]]
M3 = [Mean1_psc_red[0][len(Mean1_psc_red[0])-1], Mean2_psc_red[0][len(Mean2_psc_red[0])-1], Mean3_psc_red[0][len(Mean3_psc_red[0])-1]]
M4 = [Mean1_psc_cap[0][len(Mean1_psc_cap[0])-1], Mean2_psc_cap[0][len(Mean2_psc_cap[0])-1], Mean3_psc_cap[0][len(Mean3_psc_cap[0])-1]]
x = np.arange(len(labels))  # the label locations
width = 0.125  # the width of the bars
fig, ax = plt.subplots(figsize=(12,8), dpi= 100)
rects1 = ax.bar(x - 4.5*width/3, M1, width, yerr = [1.96*STD1[0][len(STD1[0])-1]/np.sqrt(repl_num), 1.96*STD2[0][len(STD2[0])-1]/np.sqrt(repl_num), 1.96*STD3[0][len(STD3[0])-1]/np.sqrt(repl_num)], label='Base case')
rects2 = ax.bar(x - 1.5*width/3, M2, width, yerr = [1.96*STD1_psc[0][len(STD1_psc[0])-1]/np.sqrt(repl_num), 1.96*STD2_psc[0][len(STD2_psc[0])-1]/np.sqrt(repl_num), 1.96*STD3_psc[0][len(STD3_psc[0])-1]/np.sqrt(repl_num)], label='Expanded case')
rects3 = ax.bar(x + 1.5*width/3, M3, width, yerr = [1.96*STD1_psc_red[0][len(STD1_psc_red[0])-1]/np.sqrt(repl_num), 1.96*STD2_psc_red[0][len(STD2_psc_red[0])-1]/np.sqrt(repl_num), 1.96*STD3_psc_red[0][len(STD3_psc_red[0])-1]/np.sqrt(repl_num)], label='Expanded case, reduced transfer')
rects4 = ax.bar(x + 4.5*width/3, M4, width, yerr = [1.96*STD1_psc_cap[0][len(STD1_psc_cap[0])-1]/np.sqrt(repl_num), 1.96*STD2_psc_cap[0][len(STD2_psc_cap[0])-1]/np.sqrt(repl_num), 1.96*STD3_psc_cap[0][len(STD3_psc_cap[0])-1]/np.sqrt(repl_num)], label='Expanded case, additional Neuro-ICU beds')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Overflow probability')
ax.set_ylabel('Transfer rates at PSC 1')
ax.set_title('Overflow probability by case')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_yticks([0.00, 0.10, 0.20, 0.30, 0.40, 0.50])
ax.legend()
plt.savefig("6_overflow_prob_by_case.pdf")
plt.savefig("6_overflow_prob_by_case.jpg")

