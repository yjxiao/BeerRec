import sys, os

def main():
    args = sys.argv[1:]
    user_count = {}
    beer_count = {}
    data_dir = 'data'
    print 'Reading files ...'
    with open(os.path.join(data_dir, 'user_count.txt'), 'r') as f:
        for line in f:
            line = line.split(' ')
            user_count[line[0]] = int(line[1])

    with open(os.path.join(data_dir, 'beer_count.txt'), 'r') as f:
        for line in f:
            line = line.split(' ')
            beer_count[line[0]] = int(line[1])

    users = user_count.keys()
    beers = beer_count.keys()

    user_cut = input('minimum reviews for the user: ')
    beer_cut = input('minimum reviews for the beer: ')

    print 'Getting valid users & beers ...'
    valid_users = set(user for user in users if user_count[user] >= user_cut)
    valid_beers = set(beer for beer in beers if beer_count[beer] >= beer_cut)

    print 'Filtering ...'
    output = []
    with open(args[0], 'r') as f:
        for line in f:
            user, beer, _ = line.split(' ')
            if user in valid_users and beer in valid_beers:
                output.append(line)

    parts = os.path.splitext(args[0])
    file_name = os.path.join(data_dir, parts[0] + '_u{0}_b{1}.txt'.format(user_cut, beer_cut))
    with open(file_name, 'w') as f:
        f.write(''.join(output))

if __name__ == '__main__':
    main()
            
