import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('(^[.])','', (re.sub('([.]$)','',(re.sub('(\s)', 'a',(re.sub('(([.])\\2{1,})', '.', re.sub("[^a-z0-9-_.\s]","",new_id))))))))
    if new_id == "":
        new_id = "a"
    if len(new_id) >15:
        new_id = re.sub('(^[.])','',(re.sub('([.]$)','',new_id[:15])))
    if len(new_id) < 3:
        dong = 3 - len(new_id)
        for i in range(dong):
            new_id += new_id[-1]
    answer = new_id
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))