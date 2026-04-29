def convert(music):
    return (music.replace('C#', 'c')
                 .replace('D#', 'd')
                 .replace('F#', 'f')
                 .replace('G#', 'g')
                 .replace('A#', 'a'))

def time_trans(tm):
    hh, mm = map(int, tm.split(':'))
    return hh * 60 + mm

def solution(m, musicinfos):
    answer = []
    m = convert(m)  
    
    for infos in musicinfos:
        start, end, title, music = infos.split(',')
        play_time = time_trans(end) - time_trans(start)
        
        music = convert(music)  
        
        mu_len = len(music)
        melody = (music * (play_time // mu_len) +
                  music[:play_time % mu_len])
        
        if m in melody:
            answer.append((title, play_time))
    
    if not answer:
        return "(None)"
    
    answer.sort(key=lambda x: -x[1])
    return answer[0][0]