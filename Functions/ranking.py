import sqlite3
import math

from calculate_score import point_ranges

mult_dict = {1:0.1, 2:0.4, 3:0.6, 4:0.8, 5:1, 6:1.2, 7:1.4, 8:1.6, 9:1.8, 10:2.1}

#INCLUDE PROPER DATABASE LOCATION BELOW
connection = sqlite3.connect('../schoolfinder/CHSF.db')
c = connection.cursor()


average = '''SELECT sum(total_tested*
composite_score_mean)/sum(total_tested) AS average
FROM act WHERE year = 2015 AND category = "Overall" 
AND category_type = "Overall";'''

test = "SELECT * FROM main;"

r = c.execute(average)


average_ACT = r.fetchall()
average_ACT = average_ACT[0][0]

    


def compute_score(school_id, d_pref, a_pref, max_willing, time_between, act_score, enrollment_pct, persistance_pct, on_track_rate):
    '''
    '''

    d_pref = mult_dict[d_pref]
    a_pref = mult_dict[a_pref]

    distance_score = 1 - (time_between/max_willing) #distance to school / max distance willing to travel
    
    academic_factors = []
    
    if act_score != None:
        school_act = (act.composite_score_mean/average_ACT)
        academic_factors.append(school_act)
    else:
        pass
    if enrollment_pct != None:
        school_enrollment_pct = (cep.enrollment_pct/average_epct)
        academic_factors.append(school_enrollment_pct)
    else:
        pass
    if persistance_pct != None:
        school_persistance_pct = (cep.persist_pct/average_ppct)
        academic_factors.append(school_persistance_pct)
    else:
        pass
    if on_track_rate != None:
        school_on_track_rate = (fot.fot/average_on_track_rate)
        academic_factors.append(school_on_track_rate)
    else:
        pass

    academic_score = sum(academic_factors)/len(academic_factors)

    prelim_score = d_pref * distance_score + a_pref * academic_score

    if school_id in point_ranges:
        difficulty = (point_ranges[school_id][0] + point_ranges[school_id][1])/2

    

        total_score = prelim_score - (LAMBDA * difficulty)

    else:
        total_score = prelim_score

    return total_score
