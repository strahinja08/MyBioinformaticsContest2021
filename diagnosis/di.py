import numpy as np
import csv
import pandas as pd

# from multiprocessing import Pool


def gen_phil(content):
    return dict(zip(
        np.arange(1, int(content[0][0])+1),
        np.array([1]+content[1], dtype=int)))


def gen_ic(content):
    return dict(zip(
        np.arange(1, int(content[0][0])+1),
        np.array(content[2], dtype=int)))


def gen_diseases(content):
    # print('disease...')
    d_index = int(content[3][0])
    return [np.array(content[x][1:], dtype=int) for x in range(4, 4+d_index)]


def gen_patients(content):
    # print('patient...')
    p_index = 5 + int(content[3][0])
    return [np.array(content[x][1:], dtype=int)
            for x in range(p_index, len(content))]


def run(disease, patients, func, df_phil, ic):

    with open(ofile, 'w+') as owrite:

        for x in range(len(patients)):
            results = []
            # print('working on comb')
            comb = [[np.array(np.meshgrid(x, di)).T.reshape(-1, 2)
                    for di in disease] for x in patients[x]]

            # 0 => [(p11,d11) (p11,d12) (p11,d13)...], [(p11,d21)...]
            res = np.apply_along_axis(
                lambda x: [max([func(z, df_phil, ic) for z in y]) for y in x], 0, comb),

            owrite.write(f"{np.argmax(np.sum(res[0], axis=0))+1}\n")


def recursive_f(x, di, row):
    if len(row) > 0 and row[-1] == 1:
        return row

    if di[x]:
        row.append(di[x])
        return recursive_f(di[x], di, row)

    else:
        return row


def di_to_df_phil(di):
    "import dict, output dataframe!"

    out_di = {}

    for x, y in di.items():

        ph_row = [x, y]
        recursive_f(y, di, ph_row)
        out_di[x] = [ph_row]

    return pd.DataFrame(out_di, index=['phil']).T


def func(params, df, ic):
    "import params tuple (i,j) both for disease or patient"
    m = np.intersect1d(df.at[params[0], 'phil'],
                       df.at[params[1], 'phil']).max()
    return ic[m]


if __name__ == '__main__':
    ifile = '/diagnosis/test1.txt'
    ofile = '/diagnosis/test1_out.txt'

    with open(ifile) as csvfile:
        content = csv.reader(csvfile, delimiter=' ')
        content = [[x for x in row if len(x) > 0] for row in content]

    df_phil = di_to_df_phil(gen_phil(content))
    ic = gen_ic(content)

    run(gen_diseases(content), gen_patients(content), func, df_phil, ic)
