from stroke_functions import *

# Initialize
T = 10000
repl_num = 100

service_rate_h = 1./7
service_rate_i = 1./3

Mean1 = []
STD1 = []
Mean2 = []
STD2 = []
Mean3 = []
STD3 = []
Mean4 = []
STD4 = []
Mean5 = []
STD5 = []
Mean6 = []
STD6 = []

cc0 = 15 # number of CSC beds when transfer rate is 15%
cc1 = 15 # number of CSC beds when transfer rate is 35%
cc2 = 15 # number of CSC beds when transfer rate is 55%

for ph in np.arange(0.15, 0.66, 0.2):
    X_outer = []
    cc = csc_bed(ph, cc0, cc1, cc2)
    for iteration in np.arange(repl_num):
        Dist = queue(ph, c1 = cc0, c2 = cc1, c3 = cc2, T = T)
        X_outer.append(Dist/T)
    
    if 0.14 <= ph <= 0.16:
        Mean1.append(np.mean(X_outer, axis = 0))
        STD1.append(np.std(X_outer, axis = 0))
    elif 0.24 <= ph <= 0.26:
        Mean2.append(np.mean(X_outer, axis = 0))
        STD2.append(np.std(X_outer, axis = 0))
    elif 0.34 <= ph <= 0.36:
        Mean3.append(np.mean(X_outer, axis = 0))
        STD3.append(np.std(X_outer, axis = 0))
    elif 0.44 <= ph <= 0.46:
        Mean4.append(np.mean(X_outer, axis = 0))
        STD4.append(np.std(X_outer, axis = 0))
    elif 0.54 <= ph <= 0.56:
        Mean5.append(np.mean(X_outer, axis = 0))
        STD5.append(np.std(X_outer, axis = 0))
    elif 0.64 <= ph <= 0.66:
        Mean6.append(np.mean(X_outer, axis = 0))
        STD6.append(np.std(X_outer, axis = 0))
    else:
        print("ERROR")

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
fig.subplots_adjust(hspace=0.5)
ax1.bar(np.arange(cc0+1), Mean1[0], yerr = 1.96*STD1[0]/np.sqrt(repl_num))
ax2.bar(np.arange(cc1+1), Mean3[0], yerr = 1.96*STD3[0]/np.sqrt(repl_num))
ax3.bar(np.arange(cc2+1), Mean5[0], yerr = 1.96*STD5[0]/np.sqrt(repl_num))
ax1.title.set_text('(a)')
ax2.title.set_text('(b)')
ax3.title.set_text('(c)')
fig.text(0.5, 0.0, 'Bed occupancy', ha='center')
fig.text(0.0, 0.5, 'Occupancy probability', va='center', rotation='vertical')
plt.savefig("1_bed_distribution_base.pdf")
plt.savefig("1_bed_distribution_base.jpg")

plt.figure()
plt.bar(["0.15", "0.35", "0.55"],
        [
            Mean1[0][len(Mean1[0])-1],
            Mean3[0][len(Mean3[0])-1],
            Mean5[0][len(Mean5[0])-1]
        ],
        yerr = [
            1.96*STD1[0][len(STD1[0])-1]/np.sqrt(repl_num),
            1.96*STD3[0][len(STD3[0])-1]/np.sqrt(repl_num),
            1.96*STD5[0][len(STD5[0])-1]/np.sqrt(repl_num)
        ])
plt.xlabel("Transfer rates at PSC 1")
plt.ylabel("Overflow probability")
plt.savefig("1_overflow_probability_base.pdf")
plt.savefig("1_overflow_probability_base.jpg")

save_list = [Mean1, Mean3, Mean5]
open_file = open("base_mean.pkl", "wb")
pickle.dump(save_list, open_file)
open_file.close()

save_list = [STD1, STD3, STD5]
open_file = open("base_std.pkl", "wb")
pickle.dump(save_list, open_file)
open_file.close()
