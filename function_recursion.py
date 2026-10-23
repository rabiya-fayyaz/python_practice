study_sessions =[45,30,60,20,15]
def total_study_time(study_sessions):
    if len(study_sessions) == 0:
        return 0
     
    return study_sessions[0] + total_study_time(study_sessions[1:])
print(total_study_time(study_sessions)) 

def count_sessions(study_sessions):
    if len(study_sessions) == 0:
        return 0
     
    return 1 + count_sessions(study_sessions[1:])
print(count_sessions(study_sessions))

def longest_session(study_sessions):
    if len(study_sessions) ==0:
        return 0
    else:
        longest = longest_session(study_sessions[1:])
        if longest > study_sessions[0]:
            return longest
        else:
            return study_sessions[0]
print(longest_session(study_sessions))