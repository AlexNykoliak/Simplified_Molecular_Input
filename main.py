import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors


def getMolDescriptors(mol, missingVal=None):
    result = {}
    for nm, fn in Descriptors._descList:
        try:
            val = fn(mol)
        except:
            val = missingVal
        result[nm] = val
    return result


file = pd.read_excel('Anticonv.Clon.ton.seiz..xlsx')

descriptors = file.iloc[:, 1].apply(
    lambda x: getMolDescriptors(Chem.MolFromSmiles(x)))

new_data = pd.DataFrame(descriptors.tolist())

result_df = pd.concat([file, new_data], axis=1)

result_df.to_excel('output_with_descriptors.xlsx', index=False)
