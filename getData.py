import pandas as pd
import os


def getData():
    cwd = os.getcwd()
    inputDataPath = os.path.join(cwd, "InputData")
    data = {}

    # Locations
    locations = set(pd.read_excel(os.path.join(inputDataPath, 'Locations.xlsx')))

    data.update({'locations': locations})

    # PV data
    gen_capacityMax = pd.read_excel(os.path.join(inputDataPath, 'PV_Capacity.xlsx'),
                                    sheetname='GenerationCapacities')
    gen_capacityMax = gen_capacityMax.loc['PV_south'].T
    gen_operationRateMax = pd.read_excel(os.path.join(inputDataPath, 'PV_Generation.xlsx'))

    data.update({'PV, capacityMax': gen_capacityMax})
    data.update({'PV, operationRateMax': gen_operationRateMax})

    # Hydrogen & Battery Storage
    bt_capacityMax = pd.read_excel(os.path.join(inputDataPath, 'Battery_capacities.xlsx'))
    data.update({'BS, capacityMax': bt_capacityMax})

    Edemand_operationRateFix = pd.read_excel(os.path.join(inputDataPath, 'E_Demand.xlsx'))
    data.update({'Electricity demand, operationRateFix': Edemand_operationRateFix})
    
    
    return data
