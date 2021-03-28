from stroke_source import *

g = r.Random(1234)

def next_arrival(arrival_rate):
    U = g.uniform(0,1)
    arrival_time = -1./arrival_rate * m.log(U)

    return arrival_time

def next_service(service_rate):
    U = g.uniform(0,1)
    service_time = -1./service_rate * m.log(U)

    return service_time

def redirect(p):
    U = g.uniform(0,1)
    if p >= U:
        red = 1
    else:
        red = 0
    return(red)

def countX(lst, x): 
    count = 0
    for ele in lst: 
        if (ele == x): 
            count = count + 1
    return count 


def queue(ph, arrival_rate_p_h = 2.0*0.15, arrival_rate_p_i = 2.0*0.85,
          arrival_rate_c_h = 3.0*0.15, arrival_rate_c_i = 3.0*0.85,
          service_rate_h = 1./7, service_rate_i = 1./3,
          c1 = 15, c2 = 15, c3 = 15,
          psc1_tr_h = 0.95,
          psc2_tr_h = 0.95, psc2_tr_i = 0.15,
          psc3_tr_h = 0.95, psc3_tr_i = 0.15,
          T = 1000):
    # Initialize
    pi = ph
    patid = 0
    red_prop_h1 = psc1_tr_h # ph
    red_prop_i1 = pi
    red_prop_h2 = psc2_tr_h # 0.15
    red_prop_i2 = psc2_tr_i # 0.15
    red_prop_h3 = psc3_tr_h # 0.15
    red_prop_i3 = psc3_tr_i # 0.15
    Q = []
    X = []
    if 0.14 <= ph <= 0.16:
        cc = c1
    elif 0.24 <= ph <= 0.26:
        cc = cc0
    elif 0.34 <= ph <= 0.36:
        cc = c2
    elif 0.44 <= ph <= 0.46:
        cc = cc0
    elif 0.54 <= ph <= 0.56:
        cc = c3
    elif 0.64 <= ph <= 0.66:
        cc = cc0
    else:
        print("ERROR", ph)
    sent = 0
    overflown = 0
    #####
    # Degugging
    #####
    CSC = []
    csc_entered = 0
    total_busy_serv1 = 0
    #####
    LenQ = []
    LenX = []
    Time = []
    Dist = np.zeros(cc+1)

    next_arrival_P1_h = next_arrival(arrival_rate_p_h)
    next_arrival_P1_i = next_arrival(arrival_rate_p_i)
    next_arrival_P2_h = next_arrival(arrival_rate_p_h)
    next_arrival_P2_i = next_arrival(arrival_rate_p_i)
    next_arrival_P3_h = next_arrival(arrival_rate_p_h)
    next_arrival_P3_i = next_arrival(arrival_rate_p_i)
    next_arrival_C_h = next_arrival(arrival_rate_c_h)
    next_arrival_C_i = next_arrival(arrival_rate_c_i)
    next_complete = m.inf
    Event = [next_arrival_P1_h, next_arrival_P1_i, next_arrival_P2_h, next_arrival_P2_i, next_arrival_P3_h, next_arrival_P3_i, next_arrival_C_h, next_arrival_C_i, next_complete]


    # Next event
    t = min(Event)

    while t < T:
        Time.append(t)
        LenQ.append(len(Q))
        LenX.append(len(X))

        Update_vec = np.zeros(cc + 1)
        Update_vec[len(X)] = 1

        if t == next_arrival_P1_h:
            patid += 1
            if redirect(red_prop_h1) == 1:
                sent += 1
                stype = 1
                if len(X) >= cc:
                    Q.append([patid, stype]) # type == 1: hem; type == 2: isch
                else:
                    LOS = next_service(service_rate_h)
                    X.append([patid, stype, t + LOS])
                    next_complete = min(sublist[2] for sublist in X)
            next_arrival_P1_h = t + next_arrival(arrival_rate_p_h)
        elif t == next_arrival_P1_i:
            patid += 1
            if redirect(red_prop_i1) == 1:
                sent += 1
                stype = 2
                if len(X) >= cc:
                    Q.append([patid, stype])
                else:
                    LOS = next_service(service_rate_i)
                    X.append([patid, stype, t + LOS])
                    next_complete = min(sublist[2] for sublist in X)
            next_arrival_P1_i = t + next_arrival(arrival_rate_p_i)

        elif t == next_arrival_P2_h:
            patid += 1
            if redirect(red_prop_h2) == 1:
                sent += 1
                stype = 1
                if len(X) >= cc:
                    Q.append([patid, stype])
                else:
                    LOS = next_service(service_rate_h)
                    X.append([patid, stype, t + LOS])
                    next_complete = min(sublist[2] for sublist in X)
            next_arrival_P2_h = t + next_arrival(arrival_rate_p_h)
        elif t == next_arrival_P2_i:
            patid += 1
            if redirect(red_prop_i2) == 1:
                sent += 1
                stype = 2
                if len(X) >= cc:
                    Q.append([patid, stype])
                else:
                    LOS = next_service(service_rate_i)
                    X.append([patid, stype, t + LOS])
                    next_complete = min(sublist[2] for sublist in X)
            next_arrival_P2_i = t + next_arrival(arrival_rate_p_i)

        elif t == next_arrival_P3_h:
            patid += 1
            if redirect(red_prop_h3) == 1:
                sent += 1
                stype = 1
                if len(X) >= cc:
                    Q.append([patid, stype])
                else:
                    LOS = next_service(service_rate_h)
                    X.append([patid, stype, t + LOS])
                    next_complete = min(sublist[2] for sublist in X)
            next_arrival_P3_h = t + next_arrival(arrival_rate_p_h)
        elif t == next_arrival_P3_i:
            patid += 1
            if redirect(red_prop_i3) == 1:
                sent += 1
                stype = 2
                if len(X) >= cc:
                    Q.append([patid, stype])
                else:
                    LOS = next_service(service_rate_i)
                    X.append([patid, stype, t + LOS])
                    next_complete = min(sublist[2] for sublist in X)
            next_arrival_P3_i = t + next_arrival(arrival_rate_p_i)

        elif t == next_arrival_C_h:
            patid += 1
            csc_entered += 1
            stype = 1
            if len(X) >= cc:
                overflown += 1
                Q.append([patid, stype])
            else:
                LOS = next_service(service_rate_h)
                X.append([patid, stype, t + LOS])
                next_complete = min(sublist[2] for sublist in X)
            next_arrival_C_h = t + next_arrival(arrival_rate_c_h)
        elif t == next_arrival_C_i:
            patid += 1
            csc_entered += 1
            stype = 2
            if len(X) >= cc:
                overflown += 1
                Q.append([patid, stype])
            else:
                LOS = next_service(service_rate_i)
                X.append([patid, stype, t + LOS])
                next_complete = min(sublist[2] for sublist in X)
            next_arrival_C_i = t + next_arrival(arrival_rate_c_i)

        elif t == next_complete:
            compl = min(sublist[2] for sublist in X)
            for i in np.arange(len(X)):
                if X[i][2] == compl:
                    ind = i
            X.pop(ind)
            if len(X) > 0 :
                next_complete = min(sublist[2] for sublist in X)
            else:
                next_complete = m.inf

        Event = [next_arrival_P1_h, next_arrival_P1_i, next_arrival_P2_h, next_arrival_P2_i, next_arrival_P3_h, next_arrival_P3_i, next_arrival_C_h, next_arrival_C_i, next_complete]
        tp = t
        t = min(Event)
        total_busy_serv1 = total_busy_serv1 + len(X)*(t-tp)
        Dist = Dist + Update_vec * (t - tp)

        if len(X) >= cc + 1:
            print("ERROR!")
            break

    return(Dist)

def csc_bed(ph, cc0, cc1, cc2):
    if 0.14 <= ph <= 0.16:
        cc = cc0
    elif 0.24 <= ph <= 0.26:
        cc = cc0
    elif 0.34 <= ph <= 0.36:
        cc = cc0
    elif 0.44 <= ph <= 0.46:
        cc = cc0
    elif 0.54 <= ph <= 0.56:
        cc = cc0
    elif 0.64 <= ph <= 0.66:
        cc = cc0
    else:
        print("error")
    return(cc)

def queue_ext(ph, arrival_rate_p_h = 2.0*0.15, arrival_rate_p_i = 2.0*0.85,
              arrival_rate_c_h = 3.0*0.15, arrival_rate_c_i = 3.0*0.85,
              service_rate_h = 1./7, service_rate_i = 1./3,
              c1 = 15, c2 = 15, c3 = 15,
              psc1_tr_h = 0.95,
              psc2_tr_h = 0.95, psc2_tr_i = 0.15,
              psc3_tr_h = 0.95, psc3_tr_i = 0.15,
              psc4_tr_h = 0.95, psc4_tr_i = 0.15,
              T = 1000):
    # Initialize
    pi = ph
    patid = 0
    red_prop_h1 = psc1_tr_h # ph
    red_prop_i1 = pi
    red_prop_h2 = psc2_tr_h
    red_prop_i2 = psc2_tr_i
    red_prop_h3 = psc3_tr_h
    red_prop_i3 = psc3_tr_i
    red_prop_h4 = psc4_tr_h
    red_prop_i4 = psc4_tr_i
    Q = []
    X = []
    if 0.14 <= ph <= 0.16:
        cc = c1
    elif 0.24 <= ph <= 0.26:
        cc = cc0
    elif 0.34 <= ph <= 0.36:
        cc = c2
    elif 0.44 <= ph <= 0.46:
        cc = cc0
    elif 0.54 <= ph <= 0.56:
        cc = c3
    elif 0.64 <= ph <= 0.66:
        cc = cc0
    else:
        print("ERROR", ph)
    sent = 0
    overflown = 0
    #####
    # Degugging
    #####
    CSC = []
    csc_entered = 0
    total_busy_serv1 = 0
    #####
    LenQ = []
    LenX = []
    Time = []
    Dist = np.zeros(cc+1)

    next_arrival_P1_h = next_arrival(arrival_rate_p_h)
    next_arrival_P1_i = next_arrival(arrival_rate_p_i)
    next_arrival_P2_h = next_arrival(arrival_rate_p_h)
    next_arrival_P2_i = next_arrival(arrival_rate_p_i)
    next_arrival_P3_h = next_arrival(arrival_rate_p_h)
    next_arrival_P3_i = next_arrival(arrival_rate_p_i)
    next_arrival_P4_h = next_arrival(arrival_rate_p_h)
    next_arrival_P4_i = next_arrival(arrival_rate_p_i)
    next_arrival_C_h = next_arrival(arrival_rate_c_h)
    next_arrival_C_i = next_arrival(arrival_rate_c_i)
    next_complete = m.inf
    Event = [
        next_arrival_P1_h, next_arrival_P1_i,
        next_arrival_P2_h, next_arrival_P2_i,
        next_arrival_P3_h, next_arrival_P3_i,
        next_arrival_P4_h, next_arrival_P4_i,
        next_arrival_C_h, next_arrival_C_i,
        next_complete
    ]


    # Next event
    t = min(Event)

    while t < T:
        Time.append(t)
        LenQ.append(len(Q))
        LenX.append(len(X))

        Update_vec = np.zeros(cc + 1)
        Update_vec[len(X)] = 1

        if t == next_arrival_P1_h:
            patid += 1
            if redirect(red_prop_h1) == 1:
                sent += 1
                stype = 1
                if len(X) >= cc:
                    Q.append([patid, stype]) # type == 1: hem; type == 2: isch
                else:
                    LOS = next_service(service_rate_h)
                    X.append([patid, stype, t + LOS])
                    next_complete = min(sublist[2] for sublist in X)
            next_arrival_P1_h = t + next_arrival(arrival_rate_p_h)
        elif t == next_arrival_P1_i:
            patid += 1
            if redirect(red_prop_i1) == 1:
                sent += 1
                stype = 2
                if len(X) >= cc:
                    Q.append([patid, stype])
                else:
                    LOS = next_service(service_rate_i)
                    X.append([patid, stype, t + LOS])
                    next_complete = min(sublist[2] for sublist in X)
            next_arrival_P1_i = t + next_arrival(arrival_rate_p_i)

        elif t == next_arrival_P2_h:
            patid += 1
            if redirect(red_prop_h2) == 1:
                sent += 1
                stype = 1
                if len(X) >= cc:
                    Q.append([patid, stype])
                else:
                    LOS = next_service(service_rate_h)
                    X.append([patid, stype, t + LOS])
                    next_complete = min(sublist[2] for sublist in X)
            next_arrival_P2_h = t + next_arrival(arrival_rate_p_h)
        elif t == next_arrival_P2_i:
            patid += 1
            if redirect(red_prop_i2) == 1:
                sent += 1
                stype = 2
                if len(X) >= cc:
                    Q.append([patid, stype])
                else:
                    LOS = next_service(service_rate_i)
                    X.append([patid, stype, t + LOS])
                    next_complete = min(sublist[2] for sublist in X)
            next_arrival_P2_i = t + next_arrival(arrival_rate_p_i)

        elif t == next_arrival_P3_h:
            patid += 1
            if redirect(red_prop_h3) == 1:
                sent += 1
                stype = 1
                if len(X) >= cc:
                    Q.append([patid, stype])
                else:
                    LOS = next_service(service_rate_h)
                    X.append([patid, stype, t + LOS])
                    next_complete = min(sublist[2] for sublist in X)
            next_arrival_P3_h = t + next_arrival(arrival_rate_p_h)
        elif t == next_arrival_P3_i:
            patid += 1
            if redirect(red_prop_i3) == 1:
                sent += 1
                stype = 2
                if len(X) >= cc:
                    Q.append([patid, stype])
                else:
                    LOS = next_service(service_rate_i)
                    X.append([patid, stype, t + LOS])
                    next_complete = min(sublist[2] for sublist in X)
            next_arrival_P3_i = t + next_arrival(arrival_rate_p_i)
        
        elif t == next_arrival_P4_h:
            patid += 1
            if redirect(red_prop_h4) == 1:
                sent += 1
                stype = 1
                if len(X) >= cc:
                    Q.append([patid, stype])
                else:
                    LOS = next_service(service_rate_h)
                    X.append([patid, stype, t + LOS])
                    next_complete = min(sublist[2] for sublist in X)
            next_arrival_P4_h = t + next_arrival(arrival_rate_p_h)
        elif t == next_arrival_P4_i:
            patid += 1
            if redirect(red_prop_i4) == 1:
                sent += 1
                stype = 2
                if len(X) >= cc:
                    Q.append([patid, stype])
                else:
                    LOS = next_service(service_rate_i)
                    X.append([patid, stype, t + LOS])
                    next_complete = min(sublist[2] for sublist in X)
            next_arrival_P4_i = t + next_arrival(arrival_rate_p_i)

        elif t == next_arrival_C_h:
            patid += 1
            csc_entered += 1
            stype = 1
            if len(X) >= cc:
                overflown += 1
                Q.append([patid, stype])
            else:
                LOS = next_service(service_rate_h)
                X.append([patid, stype, t + LOS])
                next_complete = min(sublist[2] for sublist in X)
            next_arrival_C_h = t + next_arrival(arrival_rate_c_h)
        elif t == next_arrival_C_i:
            patid += 1
            csc_entered += 1
            stype = 2
            if len(X) >= cc:
                overflown += 1
                Q.append([patid, stype])
            else:
                LOS = next_service(service_rate_i)
                X.append([patid, stype, t + LOS])
                next_complete = min(sublist[2] for sublist in X)
            next_arrival_C_i = t + next_arrival(arrival_rate_c_i)

        elif t == next_complete:
            compl = min(sublist[2] for sublist in X)
            for i in np.arange(len(X)):
                if X[i][2] == compl:
                    ind = i
            X.pop(ind)
            if len(X) > 0 :
                next_complete = min(sublist[2] for sublist in X)
            else:
                next_complete = m.inf

        Event = [
            next_arrival_P1_h, next_arrival_P1_i,
            next_arrival_P2_h, next_arrival_P2_i,
            next_arrival_P3_h, next_arrival_P3_i,
            next_arrival_P4_h, next_arrival_P4_i,
            next_arrival_C_h, next_arrival_C_i,
            next_complete
        ]
        tp = t
        t = min(Event)
        total_busy_serv1 = total_busy_serv1 + len(X)*(t-tp)
        Dist = Dist + Update_vec * (t - tp)

        if len(X) >= cc + 1:
            print("ERROR!")
            break

    return(Dist)

    
def queue_customization(
        psc_hemorrhagic, psc_ischemic,
        csc_hemorrhagic, csc_ischemic,
        LOS_hemorrhagic, LOS_ischemic,
        psc1_transfer_rate_hemorrhagic,
        psc1_transfer_rate_ischemic,
        psc2_transfer_rate_hemorrhagic,
        psc2_transfer_rate_ischemic,
        psc3_transfer_rate_hemorrhagic,
        psc3_transfer_rate_ischemic,
        csc_bed_capacity, T, repl_num):
    Mean = []
    STD = []
    X_outer = []

    for iteration in np.arange(repl_num):
        Dist = queue(
            c1 = csc_bed_capacity, c2 = csc_bed_capacity, c3 = csc_bed_capacity,
            arrival_rate_p_h = psc_hemorrhagic, arrival_rate_p_i = psc_ischemic,
            arrival_rate_c_h = csc_hemorrhagic, arrival_rate_c_i = csc_ischemic,
            service_rate_h = 1./LOS_hemorrhagic, service_rate_i = 1./LOS_ischemic,
            psc1_tr_h = psc1_transfer_rate_hemorrhagic, ph = psc1_transfer_rate_ischemic,
            psc2_tr_h = psc2_transfer_rate_hemorrhagic, psc2_tr_i = psc2_transfer_rate_ischemic,
            psc3_tr_h = psc3_transfer_rate_hemorrhagic, psc3_tr_i = psc3_transfer_rate_ischemic,
            T = T)
        X_outer.append(Dist/T)
    Mean.append(np.mean(X_outer, axis = 0))
    STD.append(np.std(X_outer, axis = 0))
    fig, (ax1) = plt.subplots(1, 1)
    fig.subplots_adjust(hspace=0.5)
    ax1.bar(np.arange(csc_bed_capacity+1), Mean[0], yerr = 1.96*STD[0]/np.sqrt(repl_num))
    #ax1.title.set_text('(a)')
    fig.text(0.5, 0.0, 'Bed occupancy', ha='center')
    fig.text(0.0, 0.5, 'Occupancy probability', va='center', rotation='vertical')
    plt.savefig("bed_distribution_cust.pdf")
    plt.savefig("bed_distribution_cust.jpg")

    plt.figure()
    plt.bar([psc1_transfer_rate_ischemic],
            [
                Mean[0][len(Mean[0])-1]
            ],
            yerr = [
                1.96*STD[0][len(STD[0])-1]/np.sqrt(repl_num)
            ])
    plt.xlabel("Transfer rates at PSC 1")
    plt.ylabel("Overflow probability")
    plt.savefig("overflow_probability_cust.pdf")
    plt.savefig("overflow_probability_cust.jpg")

    mean_fin = Mean[0][len(Mean[0])-1]*100
    std_fin = 1.96*STD[0][len(STD[0])-1]/np.sqrt(repl_num)*100
    print("Overflow probability is {mean:.2f} +/- {CI:.2f}" \
        .format(mean = mean_fin, CI = std_fin))
