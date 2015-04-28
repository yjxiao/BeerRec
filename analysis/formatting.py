import sys
import os

def main():
    args = sys.argv[1:]
    beer_dict = {}
    user_dict = {}
    current = 1
    feats = ['app', 'aro', 'pal', 'tas', 'ova']    # five ratings for different features
    ratings = {}
    for feat in feats:
        ratings[feat] = []

    count = 0
    with open(args[0], 'r') as f:
        for line in f:
            count += 1
            if count % 10000 == 0:
                print 'Reading {} records ...'.format(count)
                
            line = line.strip().split('\t')
            beer_name, beer_id = line[:2]
            beer_ratings = line[5:10]
            user_name = line[11]
            if beer_id not in beer_dict:
                beer_dict[beer_id] = beer_name
            if user_name not in user_dict:
                user_dict[user_name] = current
                current += 1

            # rating triplets (string)
            for i, feat in enumerate(feats):
                ratings[feat].append(' '.join([str(user_dict[user_name]), beer_id, beer_ratings[i]]))
            
    print 'Saving results ...'
    data_dir = 'data'
    for feat in feats:
        filename = os.path.join(data_dir, '{}_ratings.txt'.format(feat))
        with open(filename, 'w') as f:
            f.write('\n'.join(ratings[feat]))

    with open(os.path.join(data_dir, 'user_ids.txt'), 'w') as f:
        for user in user_dict:
            print >> f, user, user_dict[user]
    with open(os.path.join(data_dir, 'beer_ids.tsv'), 'w') as f:
        for beer in beer_dict:
            print >> f, '\t'.join([beer_dict[beer], beer])

if __name__ == '__main__':
    main()
                
            
