
def prep_reading(reading):
    reading = reading.split('/')
    for i in range(0, len(reading)):
        reading[i] = int(reading[i])
    return reading

def hypertensive(patients):
    hypertensive_patients = 0

    for patient in patients:
        if len(patient) == 1:
            readings = prep_reading(patient[0])
            if readings[0] >= 180 and readings[1] >= 110:
                hypertensive_patients += 1  

        #sum_s = 0
        #sum_d = 0
        if len(patient) >=2:
            sum_s = 0
            sum_d = 0
            for reading in patient:
                readings = prep_reading(reading)
                if readings[0] >= 180 and readings[1] >= 110:
                    hypertensive_patients += 1
                    break
                else:
                    sum_s += readings[0]
                    sum_d += readings[1]
            avg_s = sum_s/len(patient)
            avg_d = sum_d/len(patient)
            if avg_s >= 140 or avg_d >= 90:
                hypertensive_patients += 1
    return hypertensive_patients


print(hypertensive([
["130/90","140/94"],
["160/110"],
["200/120"],
["150/94","140/90","120/90"],
["140/94","140/90","120/80","130/84"]
]))

print(hypertensive([
["130/90","140/94"],
["160/110"],
["150/80"],
["150/92","140/90","120/80"],
["140/94","140/90","120/80"]]))
