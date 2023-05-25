#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys 

if __name__ == '__main__':
    l = []
    for line in sys.stdin:
        k, v = line.split(',')
        l.append((k,v))
    l.sort(key = lambda x:x[1], reverse = True)
    for i in l:
        sys.stdout.write("{},{}\n").format(i[0], i[1])

