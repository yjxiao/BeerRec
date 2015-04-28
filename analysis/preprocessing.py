import os

def main():
    """ construct a tab separated file from the original txt file """
    data_dir = "data"
    review = []
    count = 0
    nf = open(os.path.join(data_folder, 'beer.tsv'), 'w')
    with open(os.path.join(data_folder, 'beeradvocate.txt')) as f:
        while True:
            line = f.readline()
            # do something if line is not empty
            if line:
                # if current line is newline symbol, write previous review into newfile then reset review
                if line == '\n':
                    nf.write('\t'.join(review)+'\n')
                    review = []
                    # verbose
                    count += 1
                    if count % 50000 == 0:
                        print '{} reviews read.'.format(count)
                    continue
                # if not newline, append to current review
                else:
                    # replace tab as space
                    line = line.replace('\t', ' ')
                    content = line.split(':', 1)
                    review.append(content[1].strip())

            # if line is empty, we reached end of the file, write the last review into newfile then break
            elif len(review) != 0:
                nf.write('\t'.join(review))
                nf.close()
                break
            else:
                nf.close()
                break

if __name__ == '__main__':
    main()
                
