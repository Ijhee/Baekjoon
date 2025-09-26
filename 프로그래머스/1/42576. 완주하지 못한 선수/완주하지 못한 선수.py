def solution(participant, completion):
    par_dict = dict()

    for p in participant:
        try:
            par_dict[p]
            par_dict[p].append('O')
        except:
            par_dict[p] = ['O']
    
    for c in completion:
        par_dict[c].remove('O')
    
    for dic in par_dict:
        if par_dict[dic] == ['O']:
            return dic