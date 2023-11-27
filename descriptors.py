from rdkit import Chem
from rdkit.Chem import Descriptors


""" 
Ця конкретна строка SMILES представляє певну органічну молекулу. Нотація кодує структуру молекули, включаючи 
розташування атомів і зв'язки між ними. Вона включає кілька функціональних груп та структурних мотивів:
"""

smiles = "COc1ccc(NC(=O)CN2C(=O)SC(CC(=O)Nc3nccs3)C2=O)cc1"


# Створення молекули RDKit з SMILES формули
molecule = Chem.MolFromSmiles(smiles)

mol_weight = Descriptors.MolWt(molecule)
log_p = Descriptors.MolLogP(molecule)
num_h_donors = Descriptors.NumHDonors(molecule)
num_h_acceptors = Descriptors.NumHAcceptors(molecule)
tpsa = Descriptors.TPSA(molecule)

print("Молекулярна вага:", mol_weight)
print("LogP:", log_p)
print("Кількість донорів водню:", num_h_donors)
print("Кількість акцепторів водню:", num_h_acceptors)
print("Топологічна полярна площа поверхні (TPSA):", tpsa)
