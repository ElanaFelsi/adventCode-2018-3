import os
import overlaped_fabric

def main():
    path = os.path.join(os.path.expanduser('~'),
                        'BootCamp',
                        'Python',
                        'python-home-collections-ElanaFelsi',
                        'claims.txt')

    overlaped_fabric.open_file(path)



if __name__ == '__main__':
    main()