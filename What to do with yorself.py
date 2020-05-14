import sys

lst = []
activity = {}
for line in sys.stdin:
    if line != '\n':
        lst.append(line.rstrip('\n'))
    else:
        break
for st in lst:
    words_count = st.count(' ') + 1
    if words_count not in activity:
        activity[words_count] = ''
    if st not in activity[words_count]:
        activity[words_count] += str(st) + ', '
for activites in activity:
    print(str(activites) + ':', activity[activites][:-2])
'''
kicking at the door
yawn
to count the ants
crawling on the street
stand on one leg
wait two hours
freeze
starve
knocking at the door
yawn
think about his
behavior
listen to empty stomach

lose patience
lose patience
to cry with vexation
lose patience
lose patience
lose consciousness
to cry with vexation
'''
