from homework_12.train import Train
from homework_12.wagon import Wagon

if __name__ == '__main__':
    train = Train(11234)
    locomotive = Wagon(0)

    wagon1 = Wagon(1)
    setattr(wagon1, 'passenger', 'Dmytruk')
    print(wagon1)
    print(len(wagon1))

    wagon2 = Wagon(2)
    setattr(wagon2, 'passenger', 'Stepaniuk')
    print(wagon2)
    print(len(wagon2))

    train[0] = locomotive
    train[1] = wagon1
    train[2] = wagon2

    print(train.__len__())
    print(len(train))

    print(train)
