from stroke_functions import *

############################################################################
############################################################################
############################################################################

# Simply change the numbers in this section.

# LOS (in days)
LOS_hemorrhagic = 7
LOS_ischemic = 3

# Number of beds at CSC Neuro-ICU
csc_bed_capacity = 15

# Average daily number of stroke patients examined at PSC
psc_hemorrhagic = 0.3
psc_ischemic = 1.7

# Average daily number of stroke patients examined at CSC
csc_hemorrhagic = 0.45
csc_ischemic = 2.55

# Transfer rates
# (i) PSC 1
# hemorrhagic
psc1_transfer_rate_hemorrhagic = 0.95
# ischemic
psc1_transfer_rate_ischemic = 0.15

# (ii) PSC 2
# hemorrhagic
psc2_transfer_rate_hemorrhagic = 0.95
# ischemic
psc2_transfer_rate_ischemic = 0.15

# (iii) PSC 3
# hemorrhagic
psc3_transfer_rate_hemorrhagic = 0.95
# ischemic
psc3_transfer_rate_ischemic = 0.15


############################################################################
############################################################################
############################################################################

# Initialize (no need to change, in general)
T = 10000
repl_num = 100

# Run simulations
queue_customization(
	psc_hemorrhagic = psc_hemorrhagic, psc_ischemic = psc_ischemic,
	csc_hemorrhagic = csc_hemorrhagic, csc_ischemic = csc_ischemic,
	LOS_hemorrhagic = LOS_hemorrhagic, LOS_ischemic = LOS_ischemic,
	psc1_transfer_rate_hemorrhagic = psc1_transfer_rate_hemorrhagic,
	psc1_transfer_rate_ischemic = psc1_transfer_rate_ischemic,
	psc2_transfer_rate_hemorrhagic = psc2_transfer_rate_hemorrhagic,
	psc2_transfer_rate_ischemic = psc2_transfer_rate_ischemic,
	psc3_transfer_rate_hemorrhagic = psc3_transfer_rate_hemorrhagic,
	psc3_transfer_rate_ischemic = psc3_transfer_rate_ischemic,
	csc_bed_capacity = csc_bed_capacity,
	T = T, repl_num = repl_num
	)

