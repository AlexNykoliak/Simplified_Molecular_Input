from rdkit import Chem
import rdkit
from rdkit.Chem import Descriptors
import pandas as pd

def getMolDescriptors(mol, missingVal=None):
    ''' calculate the full list of descriptors for a molecule
    
        missingVal is used if the descriptor cannot be calculated
    '''
    res = {}
    for nm,fn in Descriptors._descList:
        try:
            val = fn(mol)
        except:
            import traceback
            traceback.print_exc()
            val = missingVal
        res[nm] = val
    return res

suppl = Chem.SmilesMolSupplier('Anticonv.Clon.ton.seiz..xlsx')
df = pd.read_excel('Anticonv.Clon.ton.seiz..xlsx', usecols=[1])

# df

#                                            Unnamed: 1
# 0                     O=C(Nc1nccs1)\C=C\2/SC(=O)NC2=O
# 1          CCOC(=O)CN1C(=O)S\C(=C/C(=O)Nc2nccs2)\C1=O
# 2           Fc1ccc(CN2C(=O)SC(CC(=O)Nc3nccs3)C2=O)cc1
# 3    COc1ccc(NC(=O)CN2C(=O)SC(CC(=O)Nc3nccs3)C2=O)cc1
# 4   FC(F)(F)c1ccccc1NC(=O)CN2C(=O)SC(CC(=O)Nc3nccs...
# 5         O=C(CC1SC(=O)N(CC(=O)Nc2nccs2)C1=O)Nc3nccs3
# 6   [K+].FC(F)(F)c1cccc(Cc2cnc(NC(=O)\C=C\3/SC(=O)...
# 7      Clc1ccc(Cc2cnc(NC(=O)\C=C\3/SC(=O)NC3=O)s2)cc1
# 8                Fc1ccc(\C=C\2/SC(=NC2=O)Nc3nccs3)cc1
# 9     [O-][N+](=O)c1cccc(\C=C\2/SC(=NC2=O)Nc3nccs3)c1
# 10           CN(C)c1ccc(\C=C\2/SC(=NC2=O)Nc3nccs3)cc1
# 11      O=C1N\C(=N/c2nccs2)\S/C/1=C/3\C(=O)Nc4ccccc34
# 12      Oc1ccc(\C=C\2/S\C(=N\c3nccs3)\N(CC=C)C2=O)cc1
# 13                 Cc1nnc(NC(=O)\C=C\2/SC(=O)NC2=O)s1
# 14                [K+].O=C(CC1NC(=O)[N-]C1=O)Nc2nccs2
# 15         NC1=NC(=O)\C(=C\c2ccc(cc2)[N+](=O)[O-])\S1
# 16  CC(C)(C)c1cc(\C=C\2/S\C(=N\c3nccs3)\NC2=O)cc(c...
# 17  CC(=O)c1sc(\N=C\2/NC(=O)\C(=C\c3cc(c(O)c(c3)C(...
# 18  [O-][N+](=O)c1cccc(\C=C\2/S\C(=N\c3nccs3)\NC2=...
# 19   [O-][N+](=O)c1ccccc1\C=C\2/S\C(=N\c3nccs3)\NC2=O
# 20  [O-][N+](=O)c1cccc(\C=C\2/S\C(=N\c3nc[nH]n3)\N...
# 21  [O-][N+](=O)c1cccc(c1)c2oc(\C=C(/C#N)\c3nc(cs3...
# 22   O=C1N\C(=N/c2nccs2)\S/C/1=C\c3cccc(OCc4ccccc4)c3
# 23                    O=C(CN1C(=O)Sc2ccccc12)Nc3nccs3
# 24                          Nc1nnc(SCC(=O)Nc2nccs2)s1
# 25  [O-][N+](=O)c1ccc(\C=C\2/S\C(=N\c3nccs3)\NC2=O...
# 26  CC(=O)c1sc(\N=C\2/NC(=O)\C(=C\c3cccc(c3)[N+](=...
# 27  Cc1nn(c(NCCO)c1\C=C\2/S\C(=N\c3nccs3)\NC2=O)c4...
# 28       O=C1N\C(=N/c2nccs2)\S/C/1=C\c3ccc4cc[nH]c4c3
# 29           O=C1N\C(=N/c2nccs2)\S/C/1=C\C=C\c3ccccc3
# 30                         Cc1onc(c1)\N=C\2/NC(=O)CS2
# 31        COc1ccc(\C=C\2/S\C(=N\c3cc(C)on3)\NC2=O)cc1
# 32  Cc1onc(c1)\N=C\2/NC(=O)\C(=C\c3c[nH]c4ccccc34)\S2
# 33  Cc1onc(c1)\N=C\2/NC(=O)\C(=C\c3c([nH]c4ccccc34...
# allDescrs = [getMolDescriptors(m) for m in mols]

all_descriptors = 