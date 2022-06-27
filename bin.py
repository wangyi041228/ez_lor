from struct import unpack, pack
from json import dump, load


def reader(path_in, path_out, txt_mode=True):
    with open(path_in, 'rb') as f1, open(path_out, 'w+', encoding='utf-8') as fout:
        lines = []
        temp0 = f1.read(12)
        block_n = unpack('l', f1.read(4))[0]
        for m in range(block_n):
            temp1 = f1.read(4)
        for m in range(block_n):
            temp2 = unpack('l', f1.read(4))[0]
            temp3 = unpack('l', f1.read(4))[0]
            temp4 = unpack('h', f1.read(2))[0]
            if temp4 == 0:
                continue
            temp5 = f1.read(11)
            keyvalues_n = unpack('l', f1.read(4))[0]
            for _ in range(keyvalues_n * 2):
                temp7 = unpack('h', f1.read(2))[0]
                ten = f1.read(temp7).decode('utf-8')
                if ten and ten[-1] == '\r':
                    ten = ten[:-1]
                lines.append(ten.replace("\n", "@"))

        output = []
        while lines:
            output.append((lines.pop(0), lines.pop(0)))
        output.sort()
        if txt_mode:
            for pair in output:
                fout.write(f'{pair[0]}\n{pair[1]}\n')
        else:
            out_dict = {}
            for pair in output:
                out_dict[pair[0]] = pair[1]
            dump(out_dict, fout, indent=2, ensure_ascii=False)


def writer(path_base_bin, path_dict, path_out, txt_mode=True):
    def copy_bytes(length):
        _temp = f1.read(length)
        fout.write(_temp)
        return _temp

    with open(path_base_bin, 'rb') as f1, open(path_dict, 'r', encoding='utf-8') as f2, open(path_out, "wb") as fout:
        if txt_mode:
            dic = {}
            while key := f2.readline().strip('\n').replace('@', '\n'):
                value = f2.readline().strip('\n').replace("@", "\n")
                dic[key] = value
        else:
            dic = load(f2)

        copy_bytes(12)
        block_n = unpack('l', copy_bytes(4))[0]

        for _ in range(block_n):
            copy_bytes(4)

        for _ in range(block_n):
            copy_bytes(4)
            copy_bytes(4)
            temp3 = unpack('h', copy_bytes(2))[0]
            if temp3 == 0:
                continue
            copy_bytes(11)
            keyvalues_n = unpack('l', copy_bytes(4))[0]
            for _ in range(keyvalues_n):
                key_length = unpack('h', copy_bytes(2))[0]
                key_decoded = copy_bytes(key_length).decode('utf-8')
                value_length_bytes = f1.read(2)
                value_length = unpack('h', value_length_bytes)[0]
                value_origin = f1.read(value_length)

                if key_decoded in dic:
                    value_new = dic[key_decoded]
                    value_encoded = value_new.encode(encoding='UTF-8')
                    fout.write(pack('h', len(value_encoded)))
                    fout.write(value_encoded)
                else:
                    fout.write(value_length_bytes)
                    fout.write(value_origin)


if __name__ == '__main__':
    reader(r'D:\Desktop\0\220626\2.20E.bin',
           r'D:\Desktop\0\220626\2.20E.txt',
           True)

    writer(r'D:\Desktop\0\220626\3.9E.bin',
           r'D:\Desktop\0\220626\2.20C修复86版字典排序.txt',
           r'D:\Desktop\0\220626\3.9C.bin',
           True)
