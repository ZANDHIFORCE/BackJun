def solution(bandage, health, attacks):
    attacks_dict = dict(attacks)    #attacks [[2,10], ..., [9, 15]] -> attacks_dict = {2:10, ..., 9:15}
    d_day = max(attacks_dict.keys())    #d_day: 종료시간
    CAST_TIME, HEAL, BONUS_HEAL = bandage   #CAST_TIME, HEAL, BONUS_HEAL: 시전시간, 초당 회복량, 추가 회복량
    FULL_HP = health    #FULL_HP: 최대체력
    enduration = 0  #지속시간
    
    for i in range(1, d_day+1):
        #오늘이 공격받는 날이면? -> HP깎고 죽었는지 확인, 지속시간 리셋
        if  i in attacks_dict:
            health = health - attacks_dict[i]
            if check_dead(health):
                return -1
            enduration = 0
        #오늘은 평화로운 날이면? -> 회복하는날!!
        else:
            enduration += 1
            if enduration<CAST_TIME:
                health = min(FULL_HP, health + HEAL)
            else:
                enduration = 0
                health = min(FULL_HP, health + (HEAL+BONUS_HEAL))
        
    return health

def check_dead(health):
    return health<=0