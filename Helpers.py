"""
Custom Functions created by @Albrt Um and @Paul Torres

"""



from math import exp
from scipy.stats import norm
from scipy import stats
import seaborn as sns
import numpy as np 
import pandas as pd


def transform_INDP(df_):
    """
    Aggregating INDP categories
    """
    dataframe = df_.copy()
    dataframe['INDP'].fillna('None', inplace=True)
    dataframe['INDP'] = dataframe['INDP'].astype('str')
    conditions = [
        dataframe['INDP'].str.startswith('01'),
        dataframe['INDP'].str.startswith('02'),
        dataframe['INDP'].str.startswith('03'),
        dataframe['INDP'].str.startswith('04'),
        dataframe['INDP'].str.startswith('05'),
        dataframe['INDP'].str.startswith('06'),
        dataframe['INDP'].str.startswith('07'),
        dataframe['INDP'].str.startswith('10'),
        dataframe['INDP'].str.startswith('11'),
        dataframe['INDP'].str.startswith('12'),
        dataframe['INDP'].str.startswith('13'),
        dataframe['INDP'].str.startswith('14'),
        dataframe['INDP'].str.startswith('15'),
        dataframe['INDP'].str.startswith('16'),
        dataframe['INDP'].str.startswith('17'),
        dataframe['INDP'].str.startswith('18'),
        dataframe['INDP'].str.startswith('19'),
        dataframe['INDP'].str.startswith('20'),
        dataframe['INDP'].str.startswith('21'),
        dataframe['INDP'].str.startswith('22'),
        dataframe['INDP'].str.startswith('23'),
        dataframe['INDP'].str.startswith('24'),
        dataframe['INDP'].str.startswith('25'),
        dataframe['INDP'].str.startswith('26'),
        dataframe['INDP'].str.startswith('27'),
        dataframe['INDP'].str.startswith('28'),
        dataframe['INDP'].str.startswith('29'),
        dataframe['INDP'].str.startswith('30'),
        dataframe['INDP'].str.startswith('31'),
        dataframe['INDP'].str.startswith('32'),
        dataframe['INDP'].str.startswith('33'),
        dataframe['INDP'].str.startswith('34'),
        dataframe['INDP'].str.startswith('35'),
        dataframe['INDP'].str.startswith('36'),
        dataframe['INDP'].str.startswith('37'),
        dataframe['INDP'].str.startswith('38'),
        dataframe['INDP'].str.startswith('39'),
        dataframe['INDP'].str.startswith('40'),
        dataframe['INDP'].str.startswith('41'),
        dataframe['INDP'].str.startswith('42'),
        dataframe['INDP'].str.startswith('43'),
        dataframe['INDP'].str.startswith('44'),
        dataframe['INDP'].str.startswith('45'),
        dataframe['INDP'].str.startswith('46'),
        dataframe['INDP'].str.startswith('47'),
        dataframe['INDP'].str.startswith('48'),
        dataframe['INDP'].str.startswith('49'),
        dataframe['INDP'].str.startswith('50'),
        dataframe['INDP'].str.startswith('51'),
        dataframe['INDP'].str.startswith('52'),
        dataframe['INDP'].str.startswith('53'),
        dataframe['INDP'].str.startswith('54'),
        dataframe['INDP'].str.startswith('55'),
        dataframe['INDP'].str.startswith('56'),
        dataframe['INDP'].str.startswith('57'),
        dataframe['INDP'].str.startswith('60'),
        dataframe['INDP'].str.startswith('61'),
        dataframe['INDP'].str.startswith('62'),
        dataframe['INDP'].str.startswith('63'),
        dataframe['INDP'].str.startswith('64'),
        dataframe['INDP'].str.startswith('65'),
        dataframe['INDP'].str.startswith('66'),
        dataframe['INDP'].str.startswith('67'),
        dataframe['INDP'].str.startswith('68'),
        dataframe['INDP'].str.startswith('69'),
        dataframe['INDP'].str.startswith('70'),
        dataframe['INDP'].str.startswith('71'),
        dataframe['INDP'].str.startswith('72'),
        dataframe['INDP'].str.startswith('73'),
        dataframe['INDP'].str.startswith('74'),
        dataframe['INDP'].str.startswith('75'),
        dataframe['INDP'].str.startswith('76'),
        dataframe['INDP'].str.startswith('77'),
        dataframe['INDP'].str.startswith('78'),
        dataframe['INDP'].str.startswith('79'),
        dataframe['INDP'].str.startswith('80'),
        dataframe['INDP'].str.startswith('81'),
        dataframe['INDP'].str.startswith('82'),
        dataframe['INDP'].str.startswith('83'),
        dataframe['INDP'].str.startswith('84'),
        dataframe['INDP'].str.startswith('85'),
        dataframe['INDP'].str.startswith('86'),
        dataframe['INDP'].str.startswith('87'),
        dataframe['INDP'].str.startswith('88'),
        dataframe['INDP'].str.startswith('89'),
        dataframe['INDP'].str.startswith('90'),
        dataframe['INDP'].str.startswith('91'),
        dataframe['INDP'].str.startswith('92'),
        dataframe['INDP'].str.startswith('93'),
        dataframe['INDP'].str.startswith('94'),
        dataframe['INDP'].str.startswith('95'),
        dataframe['INDP'].str.startswith('96'),
        dataframe['INDP'].str.startswith('97'),
        dataframe['INDP'].str.startswith('98'),
        dataframe['INDP'].str.startswith('99'),
    ]
    choices = [
        'AGR1',
        'AGR2',
        'EXT1',
        'EXT2',
        'UTL1',
        'UTL2',
        'CON',
        'MFG1',
        'MFG2',
        'MFG3',
        'MFG4',
        'MFG5',
        'MFG6',
        'MFG7',
        'MFG8',
        'MFG9',
        'MFG10',
        'MFG11',
        'MFG12',
        'MFG13',
        'MFG14',
        'MFG15',
        'MFG16',
        'MFG17',
        'MFG18',
        'MFG19',
        'MFG20',
        'MFG21',
        'MFG22',
        'MFG23',
        'MFG24',
        'MFG25',
        'MFG26',
        'MFG27',
        'MFG28',
        'MFG29',
        'MFG30',
        'WHL1',
        'WHL2',
        'WHL3',
        'WHL4',
        'WHL5',
        'WHL6',
        'RET1',
        'RET2',
        'RET3',
        'RET4',
        'RET5',
        'RET6',
        'RET7',
        'RET8',
        'RET9',
        'RET10',
        'RET11',
        'RET12',
        'TRN1',
        'TRN2',
        'TRN3',
        'TRN4',
        'INF1',
        'INF2',
        'INF3',
        'INF4',
        'FIN1',
        'FIN2',
        'FIN3',
        'FIN4',
        'PRF1',
        'PRF2',
        'PRF3',
        'PRF4',
        'PRF5',
        'PRF6',
        'EDU',
        'MED1',
        'MED2',
        'MED3',
        'MED4',
        'SCA1',
        'SCA2',
        'ENT1',
        'ENT2',
        'SRV1',
        'SRV2',
        'SRV3',
        'SRV4',
        'SRV5',
        'SRV6',
        'ADM1',
        'ADM2',
        'ADM3',
        'MIL1',
        'MIL2',
        'MIL3',
        'None'
         
    ]
    
    dataframe['INDP'] = np.select(conditions,choices, 'None')
    
    
    
    
    return dataframe





def paul_pipeline(df):
    df['CIT_STATUS'] = np.where(df['CIT'] != 5, 1, 0)
    df['BORN_CIT'] = np.where((df['CITWP'].isna()) & ((df['CIT'] != 4) & (df['CIT'] != 5)), 1, 0)
    conditions = [ (df['CIT_STATUS'] == 1),(df['CIT_STATUS'] == 0)]
    choices = [0,1]
    df['CITWP'] = np.select(conditions, choices, df['CITWP'] )
    conditions = [(df['AGEP'] < 15),((df['AGEP'] >= 15) & (df['COW'].isna()))]
    choices = [0,10]
    df['COW'] = np.select(conditions, choices, df['COW'] )
    conditions = [ (df['AGEP'] < 5)]
    choices = [0]
    df['DDRS'] = np.select(conditions, choices, df['DDRS'] )
    conditions = [ (df['AGEP'] < 5)]
    choices = [0]
    df['DPHY'] = np.select(conditions, choices, df['DPHY'] )
    conditions = [ (df['AGEP'] < 5)]
    choices = [0]
    df['DREM'] = np.select(conditions, choices, df['DREM'] )
    df['ENG'] = np.where(df['AGEP'] < 5, 1, df['ENG'])
    df['ENG'] = np.where(df['ENG'].isna(), 5, df['ENG'])
    conditions = [ (df['ESR'] == 3) & (df['JWMNP'].isna()),df['JWMNP'].isna()]
    choices = [0,201]
    df['JWMNP'] = np.select(conditions, choices, df['JWMNP'] )
    df['JWRIP'] = np.where(df['JWRIP'].isna(), 0, df['JWRIP'] )
    conditions = [ df['AGEP'] < 15,(df['ESR'] == 3) & (df['JWMNP'].isna())]
    choices = [0,13]
    df['JWTR'] = np.select(conditions, choices, df['JWTR'] )
    df['JWTR'] = np.where(df['JWTR'].isna(), 14, df['JWTR'] )
    df['MARHD'] = np.where(df['AGEP'] < 15, 0, df['MARHD'] )
    df['MARHD'] = np.where(df['MARHD'].isna(), 3, df['MARHD'] )
    df['MARHM'] = np.where(df['AGEP'] < 15, 0, df['MARHM'] )
    df['MARHM'] = np.where(df['MARHM'].isna(), 3, df['MARHM'] )
    df['MARHT'] = np.where(df['AGEP'] < 15, 0, df['MARHT'] )
    df['MARHT'] = np.where(df['MARHD'].isna(), 4, df['MARHD'] )
    df['MARHYP'] = np.where(df['AGEP'] < 15, 0, df['MARHYP'] )
    df['MARHYP'] = np.where(df['MARHYP'].isna(), 1, df['MARHYP'] )
    df['MIG'] = np.where(df['AGEP'] < 1, 0, df['MIG'] )
    df['MIL'] = np.where(df['AGEP'] < 17, 0, df['MIL'])
    conditions = [ df['AGEP'] < 17,(df['MIL'] == 4),(df['MIL'] == 3)]
    choices = [2,3,4]
    df['MLPCD'] = np.select(conditions, choices, df['MLPCD'] )
    conditions = [ df['AGEP'] < 17,(df['MIL'] == 4),(df['MIL'] == 3)]
    choices = [2,3,4]
    df['MLPE'] = np.select(conditions, choices, df['MLPE'] )
    conditions = [ df['AGEP'] < 17,(df['MIL'] == 4),(df['MIL'] == 3)]
    choices = [2,3,4]
    df['MLPFG'] = np.select(conditions, choices, df['MLPFG'] )
    conditions = [ df['AGEP'] < 17,(df['MIL'] == 4),(df['MIL'] == 3)]
    choices = [2,3,4]
    df['MLPH'] = np.select(conditions, choices, df['MLPH'] )
    conditions = [ df['AGEP'] < 17,(df['MIL'] == 4),(df['MIL'] == 3)]
    choices = [2,3,4]
    df['MLPI'] = np.select(conditions, choices, df['MLPI'] )
    conditions = [ df['AGEP'] < 17,(df['MIL'] == 4),(df['MIL'] == 3)]
    choices = [2,3,4]
    df['MLPJ'] = np.select(conditions, choices, df['MLPJ'] )
    conditions = [ df['AGEP'] < 17,(df['MIL'] == 4),(df['MIL'] == 3)]
    choices = [2,3,4]
    df['MLPK'] = np.select(conditions, choices, df['MLPK'] )
    conditions = [ df['AGEP'] < 16,(df['ESR'] != 3) & (df['ESR'].notna())]
    choices = [0,4]
    df['NWLK'] = np.select(conditions, choices, df['NWLK'] )
    df['NWLK'] = np.where(df['NWLK'].isna(), 5, df['NWLK'] )
    df['SCH'] = np.where(df['SCH'].isna(),0,df['SCH'])
    df['DECADE'] = np.where(df['BORN_CIT'] == 1, 0, df['DECADE'])
    df['ESP'] = np.where(df['ESP'].isna(),0,df['ESP'])
    conditions = [ df['ESR'] ==3,(df['ESR'] != 3) & (df['ESR'].notna()) & (df['ESR'] != 6)]
    choices = [0,4]
    df['JWDP'] = np.select(conditions, choices, df['JWDP'] )
    df['JWDP'] = np.where(df['JWDP'].isna(),0,df['JWDP'])
    df['MIGSP'] = np.where(df['AGEP'] < 1,0,df['ST'])
    df['MSP'] = np.where(df['AGEP'] < 15,0,df['MSP'])
    df['NOP'] = np.where(df['NOP'].isna(),0,df['NOP'])
    df['OC'] = np.where(df['OC'].isna(),0,df['OC'])
    df['OCCP'] = np.where(df['AGEP'] < 16,0,df['OCCP'])
    df['OCCP'] = np.where(df['OCCP'].isna(),1,df['OCCP'])
    df['RC'] = np.where(df['RC'].isna(),3,df['RC'])
    df['SCIENGP'] = np.where(df['SCIENGP'].isna(),0,df['SCIENGP'])
    df['VPS'] = np.where(df['AGEP'] < 17,0,df['VPS'])
    df['VPS'] = np.where((df['MIL'] !=1) |(df['MIL'] !=2) ,16,df['VPS'])
    df['PAP'] = np.where(df['PAP'].isna(),0,df['PAP'])
    df['SSP'] = np.where(df['SSP'].isna(),0,df['SSP'])
    df['WKHP'] = np.where(df['WKHP'].isna(),0,df['WKHP'])
    df['WAGP'] = np.where(df['WAGP'].isna(),0,df['WAGP'])
    df['PERNP'] = np.where(df['PERNP'].isna(),0,df['PERNP'])
    df['PINCP'] = np.where(df['PINCP'].isna(),0,df['PINCP'])
    df['PAP'] = np.where(df['PAP'].isna(),0,df['PAP'])
    df['SSP'] = np.where(df['SSP'].isna(),0,df['SSP'])
    df['WKHP'] = np.where(df['WKHP'].isna(),0,df['WKHP'])
    df['WAGP'] = np.where(df['WAGP'].isna(),0,df['WAGP'])
    df['PERNP'] = np.where(df['PERNP'].isna(),0,df['PERNP'])
    df['PINCP'] = np.where(df['PINCP'].isna(),0,df['PINCP'])
    
    df = transform_INDP(df)
    
    
    df = df[['RT', 'SPORDER', 'PUMA', 'ADJINC', 'PWGTP', 'CITWP',
       'COW', 'DDRS', 'DEAR', 'DPHY', 'DREM', 'ENG', 'JWMNP', 'JWRIP', 'JWTR', 'MARHD',
       'MARHM', 'MARHT', 'MARHYP', 'MIG', 'MIL','MLPCD', 'MLPE',
       'MLPFG', 'MLPH', 'MLPI', 'MLPJ', 'MLPK', 'NWLK','PAP',
       'RELP', 'SCH', 'SSP', 'WAGP', 'WKHP', 'DECADE', 'DIS', 'ESP',
        'HISP', 'INDP', 'MIGSP', 'MSP', 'NOP', 'OC',
       'OCCP', 'PERNP', 'PINCP', 'QTRBIR', 'RACWHT',
       'RC', 'SCIENGP', 'VPS', 'WAOB','CIT_STATUS', 'BORN_CIT', 'HICOV']]

    

    return df


def add_minutes(df_):
    """
    converting arrival at work and departure at work to minutes
    """
    
    dataframe = df_.copy()
    
    conditions = [
        dataframe['JWAP'].isin([1, 2, 3, 4, 5, 6, 7]),
        dataframe['JWAP'].isin([8, 9, 10]),
        dataframe['JWAP'].gt(10) & dataframe['JWAP'].lt(22),
        dataframe['JWAP'].gt(21)
    ]
    choices = [
        (dataframe['JWAP'] - 1) * 5,
        ((dataframe['JWAP'] - 8) * 5) + 40,
        ((dataframe['JWAP'] - 11) * 5) + 60,
        ((dataframe['JWAP'] - 22) * 5) + 120
    ]
    
    dataframe['JWAP_mins'] = np.select(conditions, choices, 0)
    
    conditions = [
        dataframe['JWDP'].isin([1, 2, 3, 4, 5, 6]),
        dataframe['JWDP'].gt(6) & dataframe['JWDP'].lt(20),
        dataframe['JWDP'].gt(19) & dataframe['JWDP'].lt(79),
        dataframe['JWDP'].gt(78) & dataframe['JWDP'].lt(133),
        dataframe['JWDP'].gt(132) & dataframe['JWDP'].lt(137),
        dataframe['JWDP'].gt(136) & dataframe['JWDP'].lt(149),
        dataframe['JWDP'].isin([149, 150])
    ]
    choices = [
        (dataframe['JWDP'] - 1) * 30,
        ((dataframe['JWDP'] - 7) * 10) + 180,
        ((dataframe['JWDP'] - 20) * 5) + 300,
        ((dataframe['JWDP'] - 79) * 10) + 600,
        ((dataframe['JWDP'] - 133) * 30) + 1140,
        ((dataframe['JWDP'] - 137) * 10) + 1260,
        ((dataframe['JWDP'] - 149) * 30) + 1380
    ]
    dataframe['JWDP_mins'] = np.select(conditions, choices, 0)
    
    conditions = [
        dataframe['JWAP_mins'] < dataframe['JWDP_mins'],
        dataframe['JWAP_mins'] > dataframe['JWDP_mins']
    ]
    choices = [
        (1440 - dataframe['JWDP_mins']) + dataframe['JWAP_mins'],
        dataframe['JWAP_mins'] - dataframe['JWDP_mins']
    ]
    dataframe['TOTAL_commute'] = np.select(conditions, choices, 0)
    
    return dataframe


def dropping_features(df_):
    """
    Dropping features based off of 3 conditions.
    1. Dropping unwanted features
    2. Dropping duplicate columns after missing handled
    3. Dropping flags and weights
    """
    
    dataframe = df_.copy()
    # 1. Dropping Unwanted features
    dataframe.drop(columns = ['DIVISION','REGION','ST','DRAT','DRATX','GCM',
                              'HINS3','HINS5','HINS6','FOD1P','FOD2P','LANP','MIGPUMA',
                             'PAOC','PRIVCOV','PUBCOV','RAC2P','RAC3P','SFN','SFR'], inplace=True)
    
    # 2. Dropping duplicate columns after missing handled
    dataframe.drop(columns = ['DOUT', 'FER', 'INTP', 'LANX', 'MARHW', 'OIP',
                             'RETP', 'SCHG', 'SCHL', 'SEMP', 'SSIP', 'WKL', 'WKW',
                             'WRK', 'YOEP', 'DRIVESP', 'ESR', 'NAICSP', 'POBP','POWSP',
                             'RAC1P','SCIENGRLP', 'SOCP','NWAB', 'NWAV', 'NWLA'], inplace=True)
    
    # 3. Drpoping flags and weights
    dataframe.drop(columns =['FCITP', 'FDEYEP', 'FDOUTP',
                           'FDPHYP', 'FDREMP', 'FENGP', 'FFERP', 'FFODP', 'FGCLP', 'FHINS1P',
                           'FHINS3C', 'FHINS3P', 'FHINS4P', 'FHINS5C', 'FHINS5P', 'FINTP',
                           'FJWDP', 'FJWRIP', 'FJWTRP', 'FLANXP', 'FMARHDP', 'FMARHMP','JWAP',
                           'FMARHWP', 'FMARHYP', 'FMIGP', 'FMILPP','MIL', 'FOCCP', 'FPAP', 'FPERNP',
                           'FPINCP', 'FRETP', 'FSCHGP', 'FSCHLP', 'FSEMP', 'FWAGP', 'FWKLP',
                           'FWKWP', 'FWRKP', 'PWGTP1', 'PWGTP2', 'PWGTP6', 'PWGTP7',
                           'PWGTP11', 'PWGTP12', 'PWGTP13', 'PWGTP14', 'PWGTP15', 'PWGTP16',
                           'PWGTP18', 'PWGTP19', 'PWGTP22', 'PWGTP27', 'PWGTP28', 'PWGTP29',
                           'PWGTP33', 'PWGTP34', 'PWGTP35', 'PWGTP41', 'PWGTP44', 'PWGTP45',
                           'PWGTP46', 'PWGTP49', 'PWGTP50', 'PWGTP53', 'PWGTP59', 'PWGTP60',
                           'PWGTP62', 'PWGTP63', 'PWGTP64', 'PWGTP67', 'PWGTP69', 'PWGTP70',
                           'PWGTP72', 'PWGTP73', 'PWGTP76', 'PWGTP78', 'PWGTP79','CITWP',
       'COW', 'DDRS', 'DEAR', 'DPHY', 'DREM', 'ENG', 'GCL', 'HINS1',
       'HINS2',  'HINS7', 'JWMNP', 'JWRIP', 'JWTR', 'MARHD',
       'MARHM', 'MARHT', 'MARHYP', 'MIG', 'MLPB', 'MLPCD', 'MLPE',
       'MLPFG', 'MLPH', 'MLPI', 'MLPJ', 'MLPK', 'NWLK', 'NWRE', 'PAP',
       'RELP', 'SCH', 'SSP', 'WAGP', 'WKHP', 'DECADE', 'DIS', 'ESP',
       'HICOV', 'HISP', 'INDP', 'JWDP', 'MIGSP', 'MSP', 'NOP', 'OC',
       'OCCP', 'PERNP', 'PINCP', 'POVPIP', 'POWPUMA', 'QTRBIR', 'RACWHT',
       'RC', 'SCIENGP', 'VPS', 'WAOB','FHINS4C','GCR'], inplace=True)
    
    return dataframe



def alberts_turn(df_):
    """
    'DIVISION', 'REGION', 'ST', 'AGE', 'CITIZEN', 'DEYE', 'DIS_ALONE',
       'DIS_VETP', 'DIS_VET', 'FER', 'GCM', 'GCR', 'MEDCAID', 'TRICARE',
       'HI_VA', 'INTP', 'LANX', 'MAR', 'MARHW', 'MIL', 'MLPA', 'NWAB',
       'NWAV', 'NWLA', 'OIP', 'RETP', 'SCHG', 'SCHL', 'SEMP', 'SEX',
       'SSIP', 'WKL', 'WKW', 'WRK', 'YR_ENTER_US', 'ANC', 'ANCES1',
       'ANC2P', 'DRIVESP', 'ESR', 'DEGREE1', 'DEGREE2', 'WK_ARR_TME',
       'LAN_HOME', 'MIGPUMA', 'NAICSP', 'NATIVITY', 'PAOC', 'POBP',
       'POWSP', 'PRIVCOV', 'PUBCOV', 'RAC1P', 'RAC2P', 'RAC3P', 'RACAIAN',
       'RACASN', 'RACBLK', 'RACNH', 'RACNUM', 'RACPI', 'RACSOR',
       'SCIENGRLP', 'SFN', 'SFR', 'SOCP', 'FCITP', 'FDEYEP', 'FDOUTP',
       'FDPHYP', 'FDREMP', 'FENGP', 'FFERP', 'FFODP', 'FGCLP', 'FHINS1P',
       'FHINS3C', 'FHINS3P', 'FHINS4P', 'FHINS5C', 'FHINS5P', 'FINTP',
       'FJWDP', 'FJWRIP', 'FJWTRP', 'FLANXP', 'FMARHDP', 'FMARHMP',
       'FMARHWP', 'FMARHYP', 'FMIGP', 'FMILPP', 'FOCCP', 'FPAP', 'FPERNP',
       'FPINCP', 'FRETP', 'FSCHGP', 'FSCHLP', 'FSEMP', 'FWAGP', 'FWKLP',
       'FWKWP', 'FWRKP', 'PWGTP1', 'PWGTP2', 'PWGTP6', 'PWGTP7',
       'PWGTP11', 'PWGTP12', 'PWGTP13', 'PWGTP14', 'PWGTP15', 'PWGTP16',
       'PWGTP18', 'PWGTP19', 'PWGTP22', 'PWGTP27', 'PWGTP28', 'PWGTP29',
       'PWGTP33', 'PWGTP34', 'PWGTP35', 'PWGTP41', 'PWGTP44', 'PWGTP45',
       'PWGTP46', 'PWGTP49', 'PWGTP50', 'PWGTP53', 'PWGTP59', 'PWGTP60',
       'PWGTP62', 'PWGTP63', 'PWGTP64', 'PWGTP67', 'PWGTP69', 'PWGTP70',
       'PWGTP72', 'PWGTP73', 'PWGTP76', 'PWGTP78', 'PWGTP79'
       
    """
    dataframe = df_.copy()

    # DIS_ALONE
    conditions = [dataframe['DOUT'].eq(1), dataframe['DOUT'].eq(2)]
    choices = ['Yes', 'No']
    dataframe['DOUT_cat'] = np.select(conditions, choices, 'LT_15yrs')
    
    # FER
    conditions = [dataframe['FER'].eq(1), dataframe['FER'].eq(2)]
    choices = ['Yes', 'No']
    dataframe['FER_cat'] = np.select(conditions, choices, 'Not_Applicable')
    
    # MLPA 
    conditions = [ dataframe['AGEP'] < 17,(dataframe['MIL'] == 4),(dataframe['MIL'] == 3)]
    choices = [2,3,4]
    dataframe['MLPA'] = np.select(conditions, choices, dataframe['MLPA'] )
    
    # INTP
    dataframe['INTP_cat'] = np.where(dataframe['INTP'].isna(), 0, dataframe['INTP'])
    
    # LANX
    conditions = [dataframe['LANX'].eq(1), dataframe['LANX'].eq(2)]
    choices = ['Other_Lang', 'English_Lang']
    dataframe['LANX_cat'] = np.select(conditions, choices, 'Baby_Lang')
    
    # MARHW
    dataframe['MARHW_cat'] = np.where(dataframe['MARHW'].isna(), 'Unknown', dataframe['MARHW'])
    
    # MIL
    conditions = [dataframe['MIL'].eq(1), dataframe['MIL'].eq(2), dataframe['MIL'].eq(3), dataframe['MIL'].eq(4)]
    choices = ['Active', 'Past Active', 'Reserves', 'Never Served']
    dataframe['MIL_cat'] = np.select(conditions, choices, 'LT_17yrold')
    
    # MLPA
    conditions = [dataframe['MLPA'].eq(0), dataframe['MLPA'].eq(1)]
    choices = ['No_Served', 'Yes_Served']
    dataframe['MLPA_cat'] = np.select(conditions, choices, 'LT_17yrold')
    
    # OIP
    dataframe['OIP_cat'] = np.where(dataframe['OIP'].isna(), 0, dataframe['OIP'])
    
    # RETP
    dataframe['RETP_cat'] = np.where(dataframe['RETP'].isna(), 0 , dataframe['RETP'])
    
    # SCHG
    conditions = [
        dataframe['SCHG'].eq(1), dataframe['SCHG'].eq(2), dataframe['SCHG'].eq(3), dataframe['SCHG'].eq(4), 
        dataframe['SCHG'].eq(5), dataframe['SCHG'].eq(6), dataframe['SCHG'].eq(7), dataframe['SCHG'].eq(8), 
        dataframe['SCHG'].eq(9), dataframe['SCHG'].eq(10), dataframe['SCHG'].eq(11), dataframe['SCHG'].eq(12),
        dataframe['SCHG'].eq(13), dataframe['SCHG'].eq(14), dataframe['SCHG'].eq(15), dataframe['SCHG'].eq(16)]
    choices = [
        'Nursery', 'Kindergarten', 'Grade_1', 'Grade_2',
        'Grade_3', 'Grade_4', 'Grade_5', 'Grade_6',
        'Grade_7', 'Grade_8', 'Grade_9', 'Grade_10',
        'Grade_11', 'Grade_12', 'Undergrad', 'Graduate']
    dataframe['SCHG_cat'] = np.select(conditions,choices, 'Not_Attending')
    
    # SCHL
    conditions = [
        dataframe['SCHL'].eq(1), dataframe['SCHL'].eq(2), dataframe['SCHL'].eq(3), dataframe['SCHL'].eq(4), 
        dataframe['SCHL'].eq(5), dataframe['SCHL'].eq(6), dataframe['SCHL'].eq(7), dataframe['SCHL'].eq(8), 
        dataframe['SCHL'].eq(9), dataframe['SCHL'].eq(10), dataframe['SCHL'].eq(11), dataframe['SCHL'].eq(12),
        dataframe['SCHL'].eq(13), dataframe['SCHL'].eq(14), dataframe['SCHL'].eq(15), dataframe['SCHL'].eq(16),
        dataframe['SCHL'].eq(17), dataframe['SCHL'].eq(18), dataframe['SCHL'].eq(19), dataframe['SCHL'].eq(20),
        dataframe['SCHL'].eq(21), dataframe['SCHL'].eq(22), dataframe['SCHL'].eq(23), dataframe['SCHL'].eq(24)]
    choices = [
        'No_School', 'Nursery', 'Kindergarten', 'Grade_1', 
        'Grade_2', 'Grade_3', 'Grade_4', 'Grade_5', 
        'Grade_6', 'Grade_7', 'Grade_8', 'Grade_9', 
        'Grade_10', 'Grade_11', 'Grade_12', 'HS_Diploma', 
        'GED_alt', 'LT1_College', 'NoDegree_College','Associates', 
        'Bachelors', 'Masters', 'Professional', 'Doctorate']
    dataframe['SCHL_cat'] = np.select(conditions, choices, 'LT_3yrold')
    
    # SEMP
    dataframe['SEMP_cat'] = np.where(dataframe['SEMP'].isna(), 0, dataframe['SEMP'])
    
    # SSIP
    dataframe['SSIP_cat'] = np.where(dataframe['SSIP'].isna(), 0 , dataframe['SSIP'])
    
    # WKL
    conditions = [dataframe['WKL'].eq(1), dataframe['WKL'].eq(2), dataframe['WKL'].eq(3)]
    choices = ['LT1', 'BT1_5', 'GT5']
    dataframe['WKL_cat'] = np.select(conditions, choices, 'LT_16yrsold')
    
    # WKW
    conditions = [
        dataframe['WKW'].eq(1), dataframe['WKW'].eq(2), dataframe['WKW'].eq(3),
        dataframe['WKW'].eq(4), dataframe['WKW'].eq(5), dataframe['WKW'].eq(6)]
    choices = [
        '50_52wks', '48_49wks', '40_47wks',
        '27_39wks', '14_26wks', 'LT_14wks']
    dataframe['WKW_cat'] = np.select(conditions, choices, 'Not_Worked')
    
    # WRK
    conditions = [dataframe['WRK'].eq(1), dataframe['WRK'].eq(2)]
    choices = ['Worked', 'Not_Worked']
    dataframe['WRK_cat'] = np.select(conditions, choices, 'Not_Reported')
    
    # YR_ENTER_US
    conditions = [
        dataframe['YOEP'].lt(1949.1), 
        dataframe['YOEP'].lt(1959.1) & dataframe['YOEP'].gt(1949.9),
        dataframe['YOEP'].lt(1969.1) & dataframe['YOEP'].gt(1959.9),
        dataframe['YOEP'].lt(1979.1) & dataframe['YOEP'].gt(1969.9),
        dataframe['YOEP'].lt(1989.1) & dataframe['YOEP'].gt(1979.9),
        dataframe['YOEP'].lt(1999.1) & dataframe['YOEP'].gt(1989.9),
        dataframe['YOEP'].lt(2009.1) & dataframe['YOEP'].gt(1999.9),
        dataframe['YOEP'].lt(2019.1) & dataframe['YOEP'].gt(2009.9),
        dataframe['YOEP'].isna()]
    choices = [
        'Below_50s',
        'Immigr_50s',
        'Immigr_60s',
        'Immigr_70s',
        'Immigr_80s',
        'Immigr_90s',
        'Immigr_00s',
        'Immigr_10s',
        'Naturalized']
    dataframe['YOEP_cat'] = np.select(conditions,choices, 'Unknown')
    
    # DRIVESP
    conditions = [dataframe['DRIVESP'].eq(1), dataframe['DRIVESP'].eq(2), dataframe['DRIVESP'].eq(3),
                 dataframe['DRIVESP'].eq(4), dataframe['DRIVESP'].eq(5), dataframe['DRIVESP'].eq(6)]
    choices = ['1_driver', '2_driver', '3_driver',
              '4_driver', '5_6_driver', 'GT7_driver']
    dataframe['DRIVESP_cat'] = np.select(conditions, choices, 'No_Drive')
    
    # ESR
    conditions = [dataframe['ESR'].eq(1), dataframe['ESR'].eq(2), dataframe['ESR'].eq(3),
                 dataframe['ESR'].eq(4), dataframe['ESR'].eq(5), dataframe['ESR'].eq(6)]
    choices = ['Employed_at_work', 'Employed_not_work', 'Unemployed',
              'ArmedForces_at_work', 'ArmedForces_not_work', 'Not_Labor']
    dataframe['ESR_cat'] = np.select(conditions, choices, 'LT_16yrsold')
    
    # NAICSP
    dataframe['NAICSP'].fillna('None', inplace=True)
    conditions = [
        dataframe['NAICSP'].str.startswith('11'),
        dataframe['NAICSP'].str.startswith('21'),
        dataframe['NAICSP'].str.startswith('22'),
        dataframe['NAICSP'].str.startswith('23'),
        dataframe['NAICSP'].str.startswith('31'),
        dataframe['NAICSP'].str.startswith('32'),
        dataframe['NAICSP'].str.startswith('33'),
        dataframe['NAICSP'].str.startswith('3M'),
        dataframe['NAICSP'].str.startswith('42'),
        dataframe['NAICSP'].str.startswith('44'),
        dataframe['NAICSP'].str.startswith('45'),
        dataframe['NAICSP'].str.startswith('4M'),
        dataframe['NAICSP'].str.startswith('51'),
        dataframe['NAICSP'].str.startswith('52'),
        dataframe['NAICSP'].str.startswith('53'),
        dataframe['NAICSP'].str.startswith('54'),
        dataframe['NAICSP'].str.startswith('55'),
        dataframe['NAICSP'].str.startswith('56'),
        dataframe['NAICSP'].str.startswith('61'),
        dataframe['NAICSP'].str.startswith('62'),
        dataframe['NAICSP'].str.startswith('71'),
        dataframe['NAICSP'].str.startswith('72'),
        dataframe['NAICSP'].str.startswith('81'),
        dataframe['NAICSP'].str.startswith('92'),
        dataframe['NAICSP'].str.startswith('99'),]
    choices = [
        'AGR',
        'EXT',
        'UTL',
        'CON',
        'MFG1',
        'MFG2',
        'MFG3',
        'MFG3',
        'WHL',
        'RET1',
        'RET2',
        'RET2',
        'INF',
        'FIN1',
        'FIN2',
        'PRF1',
        'PRF2',
        'PRF3',
        'EDU',
        'MED',
        'ENT1',
        'ENT2',
        'SRV',
        'ADM',
        'No_Work']
    dataframe['NAICSP_cat'] = np.select(conditions, choices, 'No_Work')
    

    # POBP
    dataframe['POBP_cat'] = np.where(dataframe['POBP'].eq(36), 1, 0)
    
    # POWSP
    dataframe['POWSP_cat'] = np.where(dataframe['POWSP'].eq(36), 1, 0)
    
    # RAC1P
    conditions = [
        dataframe['RAC1P'].eq(1), dataframe['RAC1P'].eq(2), dataframe['RAC1P'].eq(3),
        dataframe['RAC1P'].eq(4), dataframe['RAC1P'].eq(5), dataframe['RAC1P'].eq(6),
        dataframe['RAC1P'].eq(7), dataframe['RAC1P'].eq(8), dataframe['RAC1P'].eq(9),]
    choices = [
        'White', 'Black', 'American_Indian',
        'Alaska_Native', 'American_Indian',' Asian',
        'Native_Hawaii', 'Some_Other', 'GT2_race']
    dataframe['RAC1P_cat'] = np.select(conditions, choices, 'Unknown')
    
    # SCIENGRLP
    conditions = [dataframe['SCIENGRLP'].eq(1), dataframe['SCIENGRLP'].eq(2)]
    choices = ['Yes', 'No']
    dataframe['SCIENGRLP_cat'] = np.select(conditions, choices, 'LT_Bachelors')
    
    # SOCP
    dataframe['SOCP'].fillna('None', inplace=True)
    conditions = [
        dataframe['SOCP'].str.startswith('111'),
        dataframe['SOCP'].str.startswith('112'),
        dataframe['SOCP'].str.startswith('113'),
        dataframe['SOCP'].str.startswith('119'),
        dataframe['SOCP'].str.startswith('131'),
        dataframe['SOCP'].str.startswith('132'),
        dataframe['SOCP'].str.startswith('151'),
        dataframe['SOCP'].str.startswith('152'),
        dataframe['SOCP'].str.startswith('171'),
        dataframe['SOCP'].str.startswith('172'),
        dataframe['SOCP'].str.startswith('173'),
        dataframe['SOCP'].str.startswith('191'),
        dataframe['SOCP'].str.startswith('192'),
        dataframe['SOCP'].str.startswith('193'),
        dataframe['SOCP'].str.startswith('194'),
        dataframe['SOCP'].str.startswith('195'),
        dataframe['SOCP'].str.startswith('211'),
        dataframe['SOCP'].str.startswith('212'),
        dataframe['SOCP'].str.startswith('231'),
        dataframe['SOCP'].str.startswith('232'),
        dataframe['SOCP'].str.startswith('251'),
        dataframe['SOCP'].str.startswith('252'),
        dataframe['SOCP'].str.startswith('253'),
        dataframe['SOCP'].str.startswith('254'),
        dataframe['SOCP'].str.startswith('259'),
        dataframe['SOCP'].str.startswith('271'),
        dataframe['SOCP'].str.startswith('272'),
        dataframe['SOCP'].str.startswith('273'),
        dataframe['SOCP'].str.startswith('274'),
        dataframe['SOCP'].str.startswith('291'),
        dataframe['SOCP'].str.startswith('292'),
        dataframe['SOCP'].str.startswith('299'),
        dataframe['SOCP'].str.startswith('311'),
        dataframe['SOCP'].str.startswith('312'),
        dataframe['SOCP'].str.startswith('319'),
        dataframe['SOCP'].str.startswith('331'),
        dataframe['SOCP'].str.startswith('332'),
        dataframe['SOCP'].str.startswith('333'),
        dataframe['SOCP'].str.startswith('339'),
        dataframe['SOCP'].str.startswith('351'),
        dataframe['SOCP'].str.startswith('352'),
        dataframe['SOCP'].str.startswith('353'),
        dataframe['SOCP'].str.startswith('359'),
        dataframe['SOCP'].str.startswith('371'),
        dataframe['SOCP'].str.startswith('372'),
        dataframe['SOCP'].str.startswith('373'),
        dataframe['SOCP'].str.startswith('391'),
        dataframe['SOCP'].str.startswith('392'),
        dataframe['SOCP'].str.startswith('393'),
        dataframe['SOCP'].str.startswith('394'),
        dataframe['SOCP'].str.startswith('395'),
        dataframe['SOCP'].str.startswith('396'),
        dataframe['SOCP'].str.startswith('397'),
        dataframe['SOCP'].str.startswith('399'),
        dataframe['SOCP'].str.startswith('411'),
        dataframe['SOCP'].str.startswith('412'),
        dataframe['SOCP'].str.startswith('413'),
        dataframe['SOCP'].str.startswith('414'),
        dataframe['SOCP'].str.startswith('419'),
        dataframe['SOCP'].str.startswith('431'),
        dataframe['SOCP'].str.startswith('432'),
        dataframe['SOCP'].str.startswith('433'),
        dataframe['SOCP'].str.startswith('434'),
        dataframe['SOCP'].str.startswith('435'),
        dataframe['SOCP'].str.startswith('436'),
        dataframe['SOCP'].str.startswith('439'),
        dataframe['SOCP'].str.startswith('451'),
        dataframe['SOCP'].str.startswith('452'),
        dataframe['SOCP'].str.startswith('453'),
        dataframe['SOCP'].str.startswith('454'),
        dataframe['SOCP'].str.startswith('471'),
        dataframe['SOCP'].str.startswith('472'),
        dataframe['SOCP'].str.startswith('473'),
        dataframe['SOCP'].str.startswith('474'),
        dataframe['SOCP'].str.startswith('475'),
        dataframe['SOCP'].str.startswith('491'),
        dataframe['SOCP'].str.startswith('492'),
        dataframe['SOCP'].str.startswith('493'),
        dataframe['SOCP'].str.startswith('499'),
        dataframe['SOCP'].str.startswith('511'),
        dataframe['SOCP'].str.startswith('512'),
        dataframe['SOCP'].str.startswith('513'),
        dataframe['SOCP'].str.startswith('514'),
        dataframe['SOCP'].str.startswith('515'),
        dataframe['SOCP'].str.startswith('516'),
        dataframe['SOCP'].str.startswith('517'),
        dataframe['SOCP'].str.startswith('518'),
        dataframe['SOCP'].str.startswith('519'),
        dataframe['SOCP'].str.startswith('531'),
        dataframe['SOCP'].str.startswith('532'),
        dataframe['SOCP'].str.startswith('533'),
        dataframe['SOCP'].str.startswith('534'),
        dataframe['SOCP'].str.startswith('535'),
        dataframe['SOCP'].str.startswith('536'),
        dataframe['SOCP'].str.startswith('537'),
        dataframe['SOCP'].str.startswith('551'),
        dataframe['SOCP'].str.startswith('552'),
        dataframe['SOCP'].str.startswith('553'),
        dataframe['SOCP'].str.startswith('559'),
        dataframe['SOCP'].str.startswith('999'),]
    choices = [
        'MGR1',
        'MGR2',
        'MGR3',
        'MGR4',
        'BUS1',
        'FIN1',
        'CMM1',
        'CMM2',
        'ENG1',
        'ENG2',
        'ENG3',
        'SCI1',
        'SCI2',
        'SCI3',
        'SCI4',
        'SCI5',
        'CMS1',
        'CMS2',
        'LGL1',
        'LGL2',
        'EDU1',
        'EDU2',
        'EDU3',
        'EDU4',
        'EDU5',
        'ENT1',
        'ENT2',
        'ENT3',
        'ENT4',
        'MED1',
        'MED2',
        'MED3',
        'HLS1',
        'HLS2',
        'HLS3',
        'PRT1',
        'PRT2',
        'PRT3',
        'PRT4',
        'EAT1',
        'EAT2',
        'EAT3',
        'EAT4',
        'CLN1',
        'CLN2',
        'CLN3',
        'PRS1',
        'PRS2',
        'PRS3',
        'PRS4',
        'PRS5',
        'PRS6',
        'PRS7',
        'PRS8',
        'SAL1',
        'SAL2',
        'SAL3',
        'SAL4',
        'SAL5',
        'OFF1',
        'OFF2',
        'OFF3',
        'OFF4',
        'OFF5',
        'OFF6',
        'OFF7',
        'FFF1',
        'FFF2',
        'FFF3',
        'FFF4',
        'EXT1',
        'EXT2',
        'EXT3',
        'EXT4',
        'EXT5',
        'PPR1',
        'PPR2',
        'PPR3',
        'PPR4',
        'PRD1',
        'PRD2',
        'PRD3',
        'PRD4',
        'PRD5',
        'PRD6',
        'PRD7',
        'PRD8',
        'PRD9',
        'TRN1',
        'TRN2',
        'TRN3',
        'TRN4',
        'TRN5',
        'TRN6',
        'TRN7',
        'MIL1',
        'MIL2',
        'MIL3',
        'MIL4',
        'No_Work']
    dataframe['SOCP_cat'] = np.select(conditions, choices, 'No_Work')

    
    
    dataframe = add_minutes(dataframe)
    dataframe = dropping_features(dataframe)
    
    return dataframe

def additional_feature_engineering(df, house):
    """
    After first merge of two dataframes, we combine feature edits on this section.
    
    """
    
    
    
    _df = pd.merge(df, house[['SERIALNO', 'NP', 'TYPE', 'FINCP', 'HINCP']], on ='SERIALNO')

    conditions = [_df['SEX'] == 1, _df['SEX'] == 2]
    choices = ['Male','Female']
    _df['SEX'] = np.select(conditions, choices)
    
    conditions = [_df['ENG'] == 1, _df['ENG'] == 2, _df['ENG'] == 3,_df['ENG'] == 4, _df['ENG'] == 5]
    choices = ['Very Well','Well','Not Well', 'Not at All', 'Only English']
    _df['ENG'] = np.select(conditions, choices)
    
    _df = _df[_df['AGEP'] > 17]


    conditions = [_df['RAC1P_cat'].eq('White'), _df['RAC1P_cat'].eq('Black'), _df['RAC1P_cat'].eq(' Asian'), _df['RAC1P_cat'].eq('Some_Other'),
                 _df['RAC1P_cat'].eq('GT2_race'), _df['RAC1P_cat'].isin(['American_Indian','Native_Hawaii', 'Alaska_Native'])]
    choices = ['White', 'Black', 'Asian', 'Other', 'More Than One Race', 'American Indigenous']
    _df['RACES'] = np.select(conditions, choices, 'Unknown')


    _df['MIL_STAT'] = np.where((_df['MIL_cat'] != 'Never_Served'),'Served', "Didn't Serve")

    conditions = [_df['MAR'].eq(1), _df['MAR'].eq(2), _df['MAR'].eq(3), _df['MAR'].eq(4), _df['MAR'].eq(5)]
    choices = ['Married', 'Widowed', 'Divorced', 'Separated', 'Never Married']
    _df['MAR'] = np.select(conditions, choices, 'Unknown')


    _df['DIS'] = np.where(_df['DIS'].eq(1), 'Disabled','Not Disabled')
    _df['HICOV'] = np.where(_df['HICOV'].eq(1), 'Insured','Not Insured')
    
    conditions = [_df['INDP'].str.startswith('AGR'), _df['INDP'].str.startswith('EXT'), _df['INDP'].str.startswith('UTL'),
             _df['INDP'].str.startswith('CON'), _df['INDP'].str.startswith('MFG'), _df['INDP'].str.startswith('WHL'),
             _df['INDP'].str.startswith('RET'), _df['INDP'].str.startswith('TRN'), _df['INDP'].str.startswith('INF'),
             _df['INDP'].str.startswith('FIN'), _df['INDP'].str.startswith('PRF'), _df['INDP'].str.startswith('EDU'),
             _df['INDP'].str.startswith('MED'),              
             _df['INDP'].str.startswith('SCA'), _df['INDP'].str.startswith('ENT'), _df['INDP'].str.startswith('SRV'),
             _df['INDP'].str.startswith('ADM'), _df['INDP'].str.startswith('MIL'), _df['INDP'].str.startswith('None')]
    choices = ['Agriculture', 'Extraction', 'Utilities',
          'Construction', 'Manufacturing', 'Wholesale',
          'Retail', 'Transportation', 'Information',
          'Finance', 'Professional', 'Education',
          'Medical',
          'Social Service', 'Entertainment', 'Service',
          'Administration', 'Military', 'None']
    _df['INDUSTRY'] = np.select(conditions, choices, 'None')
    
    conditions = [_df['SOCP_cat'].str.startswith('MGR'), _df['SOCP_cat'].str.startswith('BUS'),_df['SOCP_cat'].str.startswith('FIN'),
             _df['SOCP_cat'].str.startswith('CMM'),_df['SOCP_cat'].str.startswith('ENG'),_df['SOCP_cat'].str.startswith('SCI'),
             _df['SOCP_cat'].str.startswith('CMS'),_df['SOCP_cat'].str.startswith('LGL'),_df['SOCP_cat'].str.startswith('EDU'),
             _df['SOCP_cat'].str.startswith('ENT'),_df['SOCP_cat'].str.startswith('MED'),_df['SOCP_cat'].str.startswith('HLS'),
             _df['SOCP_cat'].str.startswith('PRT'),_df['SOCP_cat'].str.startswith('EAT'),_df['SOCP_cat'].str.startswith('CLN'),
             _df['SOCP_cat'].str.startswith('PRS'),_df['SOCP_cat'].str.startswith('SAL'),_df['SOCP_cat'].str.startswith('OFF'),
             _df['SOCP_cat'].str.startswith('FFF'),_df['SOCP_cat'].str.startswith('CON'),_df['SOCP_cat'].str.startswith('EXT'),
             _df['SOCP_cat'].str.startswith('RPR'),_df['SOCP_cat'].str.startswith('PRD'),_df['SOCP_cat'].str.startswith('TRN'),
             _df['SOCP_cat'].str.startswith('MIL'),_df['SOCP_cat'].str.startswith('No_')]
    choices = ['MGR', 'BUS', 'FIN',
              'CMM','ENG','SCI',
              'CMS','LGL','EDU',
              'ENT','MED','HLS',
              'PRT','EAT','CLN',
              'PRS','SAL','OFF',
              'FFF','CON','EXT',
              'RPR','PRD','TRN',
              'MIL','None']
    _df['SOCP_recat'] = np.select(conditions, choices, 'None')
    
    condition = [_df['MARHYP'].gt(1900)]
    choices = [2018 - _df['MARHYP']]
    _df['MAR_YEARS'] = np.where(_df['MARHYP'].gt(1900), 2018 - _df['MARHYP'], 0)
    
    conditions = [_df['AGEP'].gt(64), _df['AGEP'].gt(39) & _df['AGEP'].lt(65)]
    choices = ['65 and over', 'Between 40 and 64']
    _df['AGE_cat'] = np.select(conditions, choices, 'Under 40')
    
    return _df

def dropping_last_columns(df):
    """
    Final round of dropped columns for model
    """
    df.drop(columns = [ 'FAGEP', 'FANCP', 'FCITWP','HINS4','MIL',
           'FCOWP', 'FDDRSP', 'FDEARP', 'FDISP', 'FDRATP', 'FDRATXP', 'FESRP',
           'FGCMP', 'FGCRP', 'FHICOVP', 'FHINS2P', 'FHINS6P', 'FHINS7P',
           'FHISP', 'FINDP', 'FJWMNP', 'FLANP', 'FMARP', 'FMARHTP', 'FMIGSP',
           'FMILSP', 'FOIP', 'FPOBP', 'FPOWSP', 'FPRIVCOVP', 'FPUBCOVP',
           'FRACP', 'FRELP', 'FSCHP', 'FSEXP', 'FSSIP', 'FSSP', 'FWKHP',
           'FYOEP', 'PWGTP3', 'PWGTP4', 'PWGTP5', 'PWGTP8', 'PWGTP9',
           'PWGTP10', 'PWGTP17', 'PWGTP20', 'PWGTP21', 'PWGTP23', 'PWGTP24',
           'PWGTP25', 'PWGTP26', 'PWGTP30', 'PWGTP31', 'PWGTP32', 'PWGTP36',
           'PWGTP37', 'PWGTP38', 'PWGTP39', 'PWGTP40', 'PWGTP42', 'PWGTP43',
           'PWGTP47', 'PWGTP48', 'PWGTP51', 'PWGTP52', 'PWGTP54', 'PWGTP55',
           'PWGTP56', 'PWGTP57', 'PWGTP58', 'PWGTP61', 'PWGTP65', 'PWGTP66',
           'PWGTP68', 'PWGTP71', 'PWGTP74', 'PWGTP75', 'PWGTP77', 'PWGTP80',
           'RT_x', 'SPORDER_x', 'PUMA_x', 'ADJINC_x', 'PWGTP_x'], inplace=True, errors = 'ignore')
    df.drop(columns = ['MLPA','MLPCD', 'MLPE', 'MLPFG', 'MLPH','MLPI','MLPJ','MLPK'], inplace = True,errors = 'ignore')
    df = df[df['AGEP'] > 17]
    df.drop(columns = ['RAC1P_cat'], inplace=True)

    df.drop(columns=['SERIALNO','ANC1P','ANC2P','SOCP_cat','RT_y','SPORDER_y','PUMA_y', 'ADJINC_y', 'MARHYP', 'MIGSP'],inplace=True, errors = 'ignore')
    
    df['HICOV'] = np.where(df['HICOV'].eq('Insured'), 1, 0)
    
    df.drop(columns = ['PWGTP_y'], inplace=True)
    
    return df
