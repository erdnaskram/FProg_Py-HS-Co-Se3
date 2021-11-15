import math


def part1():
    print('\nPart 1:')
    x = ['ab', 'cd']
    print(list(map(list, x)))
    # output: [['a', 'b'], ['c', 'd']]


def part2():
    print('\nPart 2:')
    q = [-1.1, -1.4, 2.3, 2.6, 3.14, 4.0, 17.0]
    # L1 läuft einwandfrei (Lösung von Prof)
    p = [x for x in q if (math.pi >= x >= -math.pi)]
    l1 = list(map(lambda x: 180 * (x + math.pi) / math.pi, p))
    # L2 läuft einwandfrei (Lösung von Student)
    l2 = list(map(lambda x: 180 * (x + math.pi) / math.pi, filter(lambda n: -math.pi <= n <= math.pi, q)))

    print('L1:', l1)
    print('L2:', l2)


def part3():
    print('\nPart 3:')
    q = [1, 3, 5, 8, 10, 13, 18, 36, 36, 78]
    # P1 läuft einwandfrei (Lösung von Prof)
    p1 = [x for x in q[::2] if x % 2 == 0]
    # P2 hat seine Probleme ... (Lösung von Student)
    p2 = list(filter(lambda x: x % 2 == 0 and q.index(x) % 2 == 0, q))

    print('P1:', p1)
    print('P2:', p2)


def part4():
    print('\nPart 4:')
    # Z1 läuft einwandfrei (Lösung von Prof)
    # range(1, x+1) if n % 3 == 0 >> von 3 bis n+1, wenn es durch 3 teilbar ist
    z1 = list(map(lambda x: [n for n in range(1, x+1) if n % 3 == 0], [13, 7]))
    # Z2 läuft einwandfrei (Lösung von Student)
    # range(3, n+1, 3) >> von 3 bis n+1 jedes drittes nehmen
    z2 = list(map(lambda n: [i for i in range(3, n+1, 3)], [13, 7]))

    print('Z1:', z1)
    print('Z2:', z2)


part1()
part2()
part3()
part4()
