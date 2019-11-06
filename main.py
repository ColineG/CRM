import io
import os
import pandas as pd
from config import Config, config
import vobject


class VCFExtractor():
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
        #pk on parcours le generateur ici ? ça le vide, et donc dans la loop en dessous, y'a rien
        #Tu peux l'enlever en dessous
        """
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
        """
        for i, contact in enumerate(vcf_contacts):
            print(i)
            diosf = {}
            for key in contact.contents.keys():
                for k, value in enumerate(contact.contents[key]):
                    diosf = self.explore(value, key, diosf, k)
            aaaa.append(diosf)
            #print()
            #print()

        self.df = pd.DataFrame(aaaa)


if __name__ == '__main__':
    mon_extractor = VCFExtractor(config)
    mon_extractor.read_vcf2()
    df = mon_extractor.df

# Analyse percentage of missing value for each column in the dataframe
    percent_missing = df.isnull().sum() * 100 / len(df)

# Drop empty column in the dataframe
    df = df.drop(columns=['version_0', 'prodid_0', 'n_0_additional', 'n_0_suffix', 'org_0', 'photo_0', 'x-abshowas_0',
                          'uid_0', 'x-abuid_0', 'adr_0_box', 'adr_0_extended', 'adr_0_region', 'x-abadr_0', 'adr_1_box',
                          'adr_1_extended', 'adr_1_region', 'adr_1_country'])

# Rename column in the dataframe
    df.rename(columns={
        'n_0_family': 'last_name',
        'n_0_given': 'first_name',
        'n_0_prefix': 'job_title_0',
        'title_0': 'job_title_1',
        'fn_0': 'company',
        'email_0': 'email_0',
        'email_1': 'email_1',
        'email_2': 'email_2',
        'tel_0': 'tel_0',
        'tel_1': 'tel_1',
        'tel_2': 'tel_2',
        'tel_3': 'tel_3',
        'note_0': 'historic',
        'url_0': 'url_0',
        'url_1': 'url_1',
        'url_2': 'url_2',
        'x-ablabel_0': 'label_0',
        'adr_0_street': 'adr_0_street',
        'adr_1_street': 'adr_1_street',
        'adr_0_city': 'adr_0_city',
        'adr_1_city': 'adr_1_city',
        'adr_0_code': 'adr_0_cp',
        'adr_1_code': 'adr_1_cp',
        'adr_0_country': 'adr_0_country',
        'x-ablabel_1': 'label_1',
        'x-ablabel_2': 'label_2',
        'x-ablabel_3': 'label_3'
    },
        inplace=True)

    df = df[['last_name',
        'first_name',
        'job_title_0',
        'job_title_1',
        'company',
        'email_0',
        'email_1',
        'email_2',
        'tel_0',
        'tel_1',
        'tel_2',
        'tel_3',
        'historic',
        'url_0',
        'url_1',
        'url_2',
        'label_0',
        'adr_0_street',
        'adr_1_street',
        'adr_0_city',
        'adr_1_city',
        'adr_0_cp',
        'adr_1_cp',
        'adr_0_country',
        'label_1',
        'label_2',
        'label_3']]

    df.to_csv('clients.csv', index=True)