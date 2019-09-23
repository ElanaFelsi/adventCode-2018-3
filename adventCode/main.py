import os
import overlaped_fabric


def main():
    path = os.path.join(os.path.expanduser('~'),
                        'BootCamp',
                        'Python',
                        'python-home-collections-ElanaFelsi',
                        'claims.txt')

    overlaped_fabric.overlapped(path)


if __name__ == '__main__':
    main()
