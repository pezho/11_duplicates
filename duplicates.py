
from collections import defaultdict
import os


def get_all_files(path):
    all_files = defaultdict(list)
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            all_files[(os.path.getsize(full_path), file)].append(full_path)
    return all_files


def main():
    path = input('Enter directory (.): ') or '.'
    print('Duplicates:')
    for key, value in get_all_files(path).items():
        if len(value) > 1:
            print('Find {} duplicates of file {}'.format(
                    len(value), os.path.basename(key[1])), 
                    '\n\t'.join(value), sep='\n\t')


if __name__ == '__main__':
    main()
