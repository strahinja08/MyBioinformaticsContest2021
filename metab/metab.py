import re
import itertools as it
import numpy as np
import csv

np.set_printoptions(precision=6)
ifile = '/metab/2.txt'
ofile = '/metab/2_output.txt'

with open(ifile) as csvfile:
    raw = csv.reader(csvfile, delimiter=' ')
    content = [[each for each in row if len(each) != 0] for row in raw]
    amount = content.pop(0)[0]

# print(f'data items: {amount}')

ofile = open(ofile, 'a+')

for en in range(0, len(content), 4):
    Ms = np.array(content[en+1:en+2][0], dtype=np.float64)
    Ks = np.array(content[en+2:en+3][0], dtype=np.float64)
    Ns = np.array(content[en+3:en+4][0], dtype=np.float64)

    s = iter(Ns)

    # (Xi Yi)...(Xi Yn) ... (Xn Yn)
    MK = np.array(np.meshgrid(Ms, Ks)).T.reshape(-1, 2)

    # return MK i where sum of i[0] i[1] > 0
    MK = MK[np.where(np.sum(MK, axis=1) > 0)]

    SMK = np.sum(MK, axis=1)

    # for x in range(len()):
    try:
        while True:
            # DELTA : min (s - MK_sum)
            MK_app_math = (np.abs(next(s)-SMK))

            indici_i_need = np.where(MK_app_math == np.min(MK_app_math))

            # indici i need to Ms and Ks
            in1 = np.where(Ms == MK[indici_i_need][0][0])[0][0]+1
            in2 = np.where(Ks == MK[indici_i_need][0][1])[0][0]+1

            out_str = f'{in1} {in2}'

            ofile.write(out_str+'\n')

    except StopIteration:
        pass

ofile.close()


#############################
# SLOW
#############################

# def gen_tups(list1, list2):
#     tups_list = []
#     for l in list1:
#         li = list(zip([l]*len(list2), list2))
#         tups_list.append(li)

#     tups_dict = {en: tup for en, tup in enumerate(
#         [li for subli in tups_list for li in subli])}

#     return tups_dict

# def retrive_index(di, key, list1, list2):
#     in1 = list1.index(di[key][0])+1
#     in2 = list2.index(di[key][1])+1
#     return (in1, in2)

# for c in range(0, len(content), 4):
#     # data = content[c]
#     # Ms = [float(x) for x in content[c+1].split(' ')]
#     # Ks = [float(x) for x in content[c+2].split(' ')]
#     # Ns = [float(x) for x in content[c+3].split(' ')]

# gen tups
# ditup = gen_tups(Ms, Ks)

# s --- 0, 1 ,2 ,3
# for s in Ns:

#     deltas = {}
#     for key, value in ditup.items():
#         # cond m+a> 0
#         if sum(value) > 0:
#             deltas[key] = abs(s-sum(value))

#     # print(deltas)
#     #   cond min
#     min_delta = min(deltas, key=deltas.get)
#     # print(min_delta)
#     print(retrive_index(ditup, min_delta, Ms, Ks))
