import json_scripts
import numpy as np
import pandas as pd
import glob

def main():

  '''
  I'm just going to add the perturbation signatures as up/dn values.
  I'll generate comma separated files in the files_2-17-2017/ directory
  '''

  file_names = glob.glob('Pert_sigs/*.json')

  for inst_filename in file_names:

    inst_pert = json_scripts.load_to_dict(inst_filename)

    pert_name = inst_filename.split('/')[1].split('.json')[0]

    up_genes = inst_pert['upGenes']
    dn_genes = inst_pert['dnGenes']

    bin_sig = []

    for inst_gene in up_genes:
      bin_sig.append(inst_gene + ',1')

    for inst_gene in dn_genes:
      bin_sig.append(inst_gene + ',-1')

    # save bin_sig to file
    fw = open('files_2-17-2017/' + pert_name + '.txt', 'w')

    for inst_val in bin_sig:
      fw.write(inst_val + '\n')

    fw.close()



main()