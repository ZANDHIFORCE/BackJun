def solution(video_len, pos, op_start, op_end, commands):
    mvideo, mpos, mop_start, mop_end = min_from(video_len), min_from(pos), min_from(op_start), min_from(op_end)
    
    for cmd in commands:
        if cmd == "next":
            mpos = next(mvideo, mpos, mop_start, mop_end)
        elif cmd == "prev":
            mpos = prev(mvideo, mpos, mop_start, mop_end)
        else:
            raise Exception("존재하지 않는 커맨드")
    return str_from(mpos)

def next(mvideo, mpos, mop_start, mop_end):
    mpos = skip_op(mpos, mop_start, mop_end)
    mpos += 10
    if mpos > mvideo:
        mpos = mvideo
    return skip_op(mpos, mop_start, mop_end)

def prev(mvideo, mpos, mop_start, mop_end):
    mpos = skip_op(mpos, mop_start, mop_end)
    mpos -= 10
    if mpos<0:
        mpos = 0
    return skip_op(mpos, mop_start, mop_end)

def min_from(str1):
    return int(str1[0])*600 + int(str1[1])*60 + int(str1[3])*10 + int(str1[4])

def str_from(min):
    s_hour, s_min = str(min//60), str(min%60)
    if len(s_hour) == 1:
        s_hour = "0" + s_hour
    if len(s_min) == 1:
        s_min = "0" + s_min
    return s_hour+ ":" + s_min

def skip_op(mpos, mop_start, mop_end):
    if mop_start<=mpos<mop_end:
        return mop_end;
    return mpos