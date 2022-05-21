import pandas as pd
import tkinter as tk
import tkinter.messagebox


# TODO: add pack methods!
class PCT:
    def __init__(self):
        print("Init")

    def unpack(self, packed):
        check_sum = packed[0]
        data_head = packed[1]
        check_sum += data_head

        i = 1
        while i < 8:
            check_sum += packed[i + 1]
            packed[i] = str((packed[i + 1] & 0x7f) | ((data_head & 0x1) << 7))
            data_head >>= 1
            i += 1

        if (check_sum & 0x7f) != ((packed[9]) & 0x7f):
            return [0, 0, 0, 0, 0, 0, 0, 0]

        return packed[0:8]

    def read_packed_csv(self, data_path):
        try:
            column_names = [
                "module", "datHead", "SecId", "dat1",
                "dat2", "dat3", "dat4", "dat5", "dat6",
                "cal"
            ]
            packed = pd.read_csv(data_path,
                                 names=column_names,
                                 na_values="?", comment='\t',
                                 sep=",", skipinitialspace=True)

            unpacked_column_names = [
                "module", "SecId", "dat1", "dat2",
                "dat3", "dat4", "dat5", "dat6"
            ]
            unpacked = pd.DataFrame(columns=unpacked_column_names)
            ds = []
            count = 0

            for index, row in packed.iterrows():
                row1 = packed.loc[index].values

                ds = self.unpack(row1)
                if (ds == [0, 0, 0, 0, 0, 0, 0, 0]).all():
                    continue

                temp = pd.DataFrame([ds], columns=unpacked_column_names)
                # df = unpacked.append(temp, sort=False)
                unpacked = pd.concat([unpacked, temp], ignore_index=True)
                count += 1

            msg = "Read " + str(count) + " lines."
            tk.messagebox.showinfo('Message', msg)
            return unpacked
        except:
            return [0, 0, 0, 0, 0, 0, 0, 0]

    def read_unpacked_csv(self, data_path):
        try:
            unpacked_column_names = [
                "module", "SecId", "dat1", "dat2",
                "dat3", "dat4", "dat5", "dat6"
            ]
            unpacked = pd.read_csv(data_path,
                                   names=unpacked_column_names,
                                   na_values="?", comment='\t',
                                   sep=",", skipinitialspace=True)

            msg = "Read " + str(len(unpacked)) + " lines."
            tk.messagebox.showinfo('Message', msg)
            return unpacked
        except:
            return [0, 0, 0, 0, 0, 0, 0, 0]


if __name__ == '__main__':
    pct = PCT()
    data_path = "./unpacked.csv"
    hello = pct.read_packed_csv(data_path)

