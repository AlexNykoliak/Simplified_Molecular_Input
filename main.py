import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors


def calculate_descriptors(smiles):
    molecule = Chem.MolFromSmiles(smiles)
    return {
        "Molecular Weight": Descriptors.MolWt(molecule),
        "LogP": Descriptors.MolLogP(molecule),
        "Num H Donors": Descriptors.NumHDonors(molecule),
        "Num H Acceptors": Descriptors.NumHAcceptors(molecule),
        "TPSA": Descriptors.TPSA(molecule)
    }


df = pd.read_excel('Anticonv.Clon.ton.seiz..xlsx')

df['Descriptors'] = df.iloc[:, 1].apply(calculate_descriptors)

df.to_excel('output_with_descriptors.xlsx')
