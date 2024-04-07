import time

def contagem_regressiva():
    while t:
        mins, segs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, segs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('O tempo acabou!')

t = int(input(f'Digite o tempo em segundos: '))

contagem_regressiva(t)