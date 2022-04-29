import numpy as np
nlin = int(input('insira o numero de colunas \n'))
ncol = int(input('insira o numero de linhas \n'))
if(nlin and ncol > 0):
    a = np.arange(nlin*ncol).reshape(nlin, ncol)
    for w in range(ncol):
        for h in range(nlin):
            a[w, h] = int(input(f'qual o valor em [{w},{h}]'))
    print(f'a matriz gerada aleatoriameente é: \n {a} \n')
    b_lin = []
    b_col = []
    for i in range(0, nlin):
        for j in range(0, ncol):
            if (a[i, j] == 0):

                b_lin.append(i)
                b_col.append(j)

    for i in b_lin:
        for k1 in range(0, ncol):
            a[i, k1] = 0

    for i in b_col:
        for k1 in range(0, nlin):
            a[k1, i] = 0
    print(f'a nova matriz após a modificação é: \n{a}\n')
else:
  print('numero de coluna ou linha menor ou igual a 0')