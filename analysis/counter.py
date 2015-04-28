import sys, os
from collections import Counter

def main():
    args = sys.argv[1:]
    user_counter = Counter()
    beer_counter = Counter()

    print 'Calculating ...'
    with open(args[0], 'r') as f:
        for line in f:
            line = line.strip().split(' ')
            user_counter[line[0]] += 1
            beer_counter[line[1]] += 1

    print 'Saving ...'
    data_dir = 'data'
    with open(os.path.join(data_dir, 'user_count.txt'), 'w') as f:
        for user in user_counter:
            print >> f, user, user_counter[user]

    with open(os.path.join(data_dir, 'beer_count.txt'), 'w') as f:
        for beer in beer_counter:
            print >> f, beer, beer_counter[beer]

if __name__ == '__main__':
    main()
                
