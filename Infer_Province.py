import re
import pandas as pd

AOAV_DATA_PATH = r'AOAV_Afghan_casualty_2020.csv'
AOAV_DESCRIPTION_COLUMN_INDEX = 6
PROVINCE_COLUMN = 'Province'
PROVINCE_COLUMN_INDEX = 8
DISTRICT_LOOKUP_DATA_PATH = r'AfghanDistricts.csv'
ALL_DISTRICTS_DATA_PATH = r'AfghanDistricts.txt'

print('Loading AOAV data...')
AOAV_Data = pd.read_csv(AOAV_DATA_PATH)
RowNumber = len(AOAV_Data.index)

AOAV_Data[PROVINCE_COLUMN] = ['' for i in range(RowNumber)]

print('Loading data on Afghan districts...')
District_lookup_data = pd.read_csv(DISTRICT_LOOKUP_DATA_PATH)
DistrictNumber = len(District_lookup_data.index)
LookUpDict = {str(District_lookup_data.iat[i, 1]).lower(): District_lookup_data.iat[i, 0] for i in range(DistrictNumber)}

print('Compiling regexes...')
AfghanProvincesRegex = re.compile(
    r'(Badakhshan)|(Badghis)|(Baghlan)|(Balkh)|(Bamyan)|(Daykundi)|(Farah)|(Faryab)|(Ghazni)|(Ghor)|(Helmand)|(Hilmand)|(Herat)|(Hirat)|(Jowzjan)|(Jawzjan)|(Kabul)|(Kandahar)|(Kapisa)|(Khost)|(Kunar)|(Kunduz)|(Laghman)|(Logar)|(Nangarhar)|(Nimruz)|(Nimroz)|(Nuristan)|(Paktia)|(Paktya)|(Paktika)|(Panjshir)|(Panjsher)|(Parwan)|(Samangan)|(Sar-e Pol)|(Sari Pul)|(Takhar)|(Uruzgan)|(Oruzgan)|(Maydan Wardak)|(Wardak)|(Zabul)',
    re.IGNORECASE
    )


SpellingRegulariserDict = {
    'Bamiyan': 'Bamyan',
    'Hilmand': 'Helmand',
    'Hirat': 'Herat',
    'Jawzjan': 'Jowzjan',
    'Nimroz': 'Nimruz',
    'Paktya': 'Paktia',
    'Panjsher': 'Panjshir',
    'Sari Pul': 'Sar-e Pol',
    'Saripul': 'Sar-e Pol',
    'Daikundi': 'Daykundi',
    'Maydan Wardak': 'Wardark',
    'Uruzgan': 'Oruzgan'
    }


with open(ALL_DISTRICTS_DATA_PATH) as f:
    AfghanDistricts = f.read().split('\n')

AfghanDistrictsRegex = re.compile(
    ''.join((
        '((?<=\W)(',
        ')(?=\W))|((?<=\W)('.join(AfghanDistricts),
        ')(?=\W))'
        )),
    re.IGNORECASE)

print('Regexes compiled, attempting to infer province data...')
for i in range(RowNumber):
    if (match := AfghanProvincesRegex.search(AOAV_Data.iat[i, AOAV_DESCRIPTION_COLUMN_INDEX])):
        Province = match.group(0)
    elif (match := AfghanDistrictsRegex.search(AOAV_Data.iat[i, AOAV_DESCRIPTION_COLUMN_INDEX])):
        Province = LookUpDict[match.group(0).lower()]
    else:
        Province = None

    if Province:
        if Province in SpellingRegulariserDict:
            Province = SpellingRegulariserDict[Province]
        AOAV_Data.iat[i, PROVINCE_COLUMN_INDEX] = Province

print('Task complete; now saving...')
AOAV_Data.to_csv('Cleaned_AOAV_Data.csv')
print('All done! Your file has been saved as a csv :)')
