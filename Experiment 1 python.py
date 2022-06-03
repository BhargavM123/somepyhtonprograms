from collections import Counter

votes = ['IronMan', 'THOR','Dr.Strange', 'CaptainAmerica', 'THOR', 'IronMan', 'CaptainAmerica',
         'Dr.Strange', 'Dr.Strange', 'IronMan','CaptainAmerica', 'THOR', 'Dr.Strange', 'THOR', 'IronMan','Dr.Strange','IronMan','CaptainAmerica','IronMan']

vote_count = Counter(votes)

max_votes = max(vote_count.values())

winner = [i for i in vote_count.keys() if(vote_count[i] == max_votes)]

print('The winner of the election is',winner[0])

