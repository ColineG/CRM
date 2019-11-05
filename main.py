import io
import os
import pandas as pd
from config import Config, config
import vobject


class VCFExtractor():
    def __init__(self):
        self.param = Config(config)
        self.df = None

    def read_vcf(self):
        with open(self.param.clients, 'r') as f:
            lines = [l for l in f if not l.startswith('##')]
        return pd.read_csv(
            io.StringIO(''.join(lines)),
            dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str,
                   'QUAL': str, 'FILTER': str, 'INFO': str},
            sep='\t'
        ).rename(columns={'#CHROM': 'CHROM'})

    def explore(self, value, key, dict_dest, num):
        if type(value.value) is str:
            dict_dest[f"{key}_{num}"] = value.value
        elif type(value.value) is list:
            dict_dest[f"{key}_{num}"] = value.value
        elif type(value.value) is bytes:
            dict_dest[f"{key}_{num}"] = value.value
        else:
            #print(value.value.__dict__)
            for key2 in value.value.__dict__.keys():
                dict_dest[f"{key}_{num}_{key2}"] = value.value.__dict__[key2]
        return dict_dest

    def read_vcf2(self):
        with open(self.param.clients, 'r') as f:
            a = f.readlines()
        vcf_contacts = vobject.readComponents(''.join(a))

        diosf = {}
        aaaa = []

        for i, contact in enumerate(vcf_contacts):
            for key in contact.contents.keys():
                for k, value in enumerate(contact.contents[key]):
                    if key in diosf:
                        pass
                    else:
                        diosf[key] = {}
                    try:
                        les_clef = value.value.__dict__.keys()
                        for x in les_clef:
                            if x in diosf[key]:
                                pass
                            else:
                                diosf[key][x] = type(x)
                    except:
                        diosf[key] = type(value.value)

        for i, contact in enumerate(vcf_contacts):
            print(i)
            diosf = {}
            for key in contact.contents.keys():
                for k, value in enumerate(contact.contents[key]):
                    diosf = explore(value, key, diosf, k)
            aaaa.append(diosf)
            #print()
            #print()

        self.df = pd.DataFrame(aaaa)


if __name__ == '__main__':
    mon_extractor = VCFExtractor()

    test.df()