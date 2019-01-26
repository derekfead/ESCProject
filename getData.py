import pandas as pd
import os


def getData():
    cwd = os.getcwd()
    inputDataPath = os.path.join(cwd, "InputData")
    data = {}

    # Locations
    locations = set(pd.read_excel(os.path.join(inputDataPath, 'Locations2.xlsx')))

    data.update({'locations': locations})

    # PV data
    gen_capacityMax = pd.read_excel(os.path.join(inputDataPath, 'PV_Capacity2.xlsx'),
                                    sheetname='GenerationCapacities')
    gen_capacityMax = gen_capacityMax.loc['PV_cap'].T
    gen_operationRateMax = pd.read_excel(os.path.join(inputDataPath, 'PV_Generation2.xlsx'))

    data.update({'PV, capacityMax': gen_capacityMax})
    data.update({'PV, operationRateMax': gen_operationRateMax})
    
    # Heat & Battery Storage
    st_capacityMax = pd.read_excel(os.path.join(inputDataPath, 'Storage_capacities2.xlsx'))
    st_capacityMax_TS = st_capacityMax.loc['Thermal Storage']
    st_capacityMax_BS = st_capacityMax.loc['Battery']
    st_capacityMax_HS = st_capacityMax.loc['Hydrogen']
   
    data.update({'TS, capacityMax': st_capacityMax_TS})
    data.update({'BS, capacityMax': st_capacityMax_BS})
    data.update({'HS, capacityMax': st_capacityMax_HS})

    # Transmission Technologies
    tr_distances_el = pd.read_excel(os.path.join(inputDataPath, 'grid_length_matrix2.xlsx'), index_col=0)
    tr_capacityFix_el = pd.read_excel(os.path.join(inputDataPath, 'grid_capacity_matrix2.xlsx'), index_col=0)
    
    data.update({'cables, capacityFix': tr_capacityFix_el})
    data.update({'cables, distances': tr_distances_el})

    data.update({'NG, capacityFix': tr_capacityFix_el})
    data.update({'NG, distances': tr_distances_el})
  
    # Denand Data
    Edemand_operationRateFix = pd.read_excel(os.path.join(inputDataPath, 'E_Demand2.xlsx'))
    Hdemand_operationRateFix = pd.read_excel(os.path.join(inputDataPath, 'Heat_Demand2.xlsx'))
    
    data.update({'Electricity demand, operationRateFix': Edemand_operationRateFix})
    data.update({'Heat demand, operationRateFix': Hdemand_operationRateFix})
    
    # Purchase Data
    Pu_operationRateMax_El = pd.read_excel(os.path.join(inputDataPath, 'purchaseElectricity2.xlsx'))
    Pu_operationRateMax_NG = pd.read_excel(os.path.join(inputDataPath, 'purchaseNaturalGas2.xlsx'))
    
    data.update({'El Purchase, operationRateMax': Pu_operationRateMax_El})
    data.update({'NG Purchase, operationRateMax': Pu_operationRateMax_NG})

    return data