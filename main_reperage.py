import pandas as pd
from config import Config, config
import vobject


class REPERAGEExtractor():
    def __init__(self, config):
        self.param = Config(config)
        self.df = None

    def explore(self, value, key, dict_dest, num):
        if type(value.value) is str:
            dict_dest[f"{key}_{num}"] = value.value
        elif type(value.value) is list:
            dict_dest[f"{key}_{num}"] = value.value
        elif type(value.value) is bytes:
            dict_dest[f"{key}_{num}"] = value.value
        else:
            for key2 in value.value.__dict__.keys():
                dict_dest[f"{key}_{num}_{key2}"] = value.value.__dict__[key2]
        return dict_dest

    def read_vcf2(self):
        with open(self.param.reperages, 'r') as f:
            a = f.readlines()
        vcf_contacts = vobject.readComponents(''.join(a))

        diosf = {}
        aaaa = []

        for i, contact in enumerate(vcf_contacts):
            print(i)
            diosf = {}
            for key in contact.contents.keys():
                for k, value in enumerate(contact.contents[key]):
                    diosf = self.explore(value, key, diosf, k)
            aaaa.append(diosf)

        self.df = pd.DataFrame(aaaa)


if __name__ == '__main__':
    mon_extractor = REPERAGEExtractor(config)
    mon_extractor.read_vcf2()
    df = mon_extractor.df

# Analyse percentage of missing value for each column in the dataframe
    percent_missing = df.isnull().sum() * 100 / len(df)

# Drop empty column in the dataframe
    df = df.drop(columns=['version_0', 'prodid_0', 'n_0_additional', 'n_0_suffix', 'org_0', 'photo_0', 'x-abshowas_0',
                          'uid_0', 'x-abuid_0', 'adr_0_box', 'adr_0_extended', 'adr_0_region', 'x-abadr_0', 'adr_1_box',
                          'adr_1_extended', 'adr_1_region', 'adr_1_country'])

