from stroke_functions import *

# Initialize
T = 10000
repl_num = 100

service_rate_h = 1./7
service_rate_i = 1./3

Mean1_psc_cap = []
STD1_psc_cap = []
Mean2_psc_cap = []
STD2_psc_cap = []
Mean3_psc_cap = []
STD3_psc_cap = []
Mean4_psc_cap = []
STD4_psc_cap = []
Mean5_psc_cap = []
STD5_psc_cap = []
Mean6_psc_cap = []
STD6_psc_cap = []

cc0 = 17 # number of CSC beds when transfer rate is 15%
cc1 = 17 # number of CSC beds when transfer rate is 35%
cc2 = 17 # number of CSC beds when transfer rate is 55%

for ph in np.arange(0.15, 0.66, 0.2):
    X_outer = []
    cc = csc_bed(ph, cc0, cc1, cc2)
    for iteration in np.arange(repl_num):
        Dist = queue_ext(ph, c1 = cc0, c2 = cc1, c3 = cc2, T = T)
        X_outer.append(Dist/T)
    
    if 0.14 <= ph <= 0.16:
        Mean1_psc_cap.append(np.mean(X_outer, axis = 0))
        STD1_psc_cap.append(np.std(X_outer, axis = 0))
    elif 0.24 <= ph <= 0.26:
        Mean2_psc_cap.append(np.mean(X_outer, axis = 0))
        STD2_psc_cap.append(np.std(X_outer, axis = 0))
    elif 0.34 <= ph <= 0.36:
        Mean3_psc_cap.append(np.mean(X_outer, axis = 0))
        STD3_psc_cap.append(np.std(X_outer, axis = 0))
    elif 0.44 <= ph <= 0.46:
        Mean4_psc_cap.append(np.mean(X_outer, axis = 0))
        STD4_psc_cap.append(np.std(X_outer, axis = 0))
    elif 0.54 <= ph <= 0.56:
        Mean5_psc_cap.append(np.mean(X_outer, axis = 0))
        STD5_psc_cap.append(np.std(X_outer, axis = 0))
    elif 0.64 <= ph <= 0.66:
        Mean6_psc_cap.append(np.mean(X_outer, axis = 0))
        STD6_psc_cap.append(np.std(X_outer, axis = 0))
    else:
        print("ERROR")

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
fig.subplots_adjust(hspace=0.5)
ax1.bar(np.arange(cc0+1), Mean1_psc_cap[0], yerr = 1.96*STD1_psc_cap[0]/np.sqrt(repl_num))
ax2.bar(np.arange(cc1+1), Mean3_psc_cap[0], yerr = 1.96*STD3_psc_cap[0]/np.sqrt(repl_num))
ax3.bar(np.arange(cc2+1), Mean5_psc_cap[0], yerr = 1.96*STD5_psc_cap[0]/np.sqrt(repl_num))
ax1.title.set_text('(a)')
ax2.title.set_text('(b)')
ax3.title.set_text('(c)')
fig.text(0.5, 0.0, 'Bed occupancy', ha='center')
fig.text(0.0, 0.5, 'Occupancy probability', va='center', rotation='vertical')
plt.savefig("5_bed_distribution_add_psc_cap.pdf")
plt.savefig("5_bed_distribution_add_psc_cap.jpg")

save_list = [Mean1_psc_cap, Mean3_psc_cap, Mean5_psc_cap]
open_file = open("base_psc_cap_mean.pkl", "wb")
pickle.dump(save_list, open_file)
open_file.close()

save_list = [STD1_psc_cap, STD3_psc_cap, STD5_psc_cap]
open_file = open("base_psc_cap_std.pkl", "wb")
pickle.dump(save_list, open_file)
open_file.close()

