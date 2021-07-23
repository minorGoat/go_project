from pathlib import Path
import sys
import os


def start():
    while True:
        path = input("Enter path to go sgf library.\nPress q to exit.\n")
        p = Path(path)
        if path == 'q':
            print("process terminated, bye")
            sys.exit()
        elif p.is_dir():
            print('thanks!')
            files = os.listdir(path)
            ans = input(f'there are {len(files)} files\nproceed? (y/n)')
            if ans == 'y':
                print('great')
                return path
            elif ans == 'n':
                continue
        else:
            print('directory does not exist, try again')


sgf_path = start()
sgf_files = os.listdir(sgf_path)
print(sgf_path + '/')



