import json_scripts
import numpy as np
import pandas as pd

def main():

  merge_exp_sigs()

def merge_exp_sigs():
  load_sigs_to_json()

  merge_sigs_to_mat()

def merge_sigs_to_mat():
  exp_sigs = json_scripts.load_to_dict('proc_data/exp_sigs.json')

  num_sigs = len(exp_sigs.keys())

  # collect all genes across all experimental signatures
  all_genes = []

  for sig_name in exp_sigs:

    print(sig_name)

    inst_sig = exp_sigs[sig_name]

    for inst_gene in inst_sig:
      all_genes.append(inst_gene)

  print(len(all_genes))
  all_genes = list(set(all_genes))
  print(len(all_genes))

  num_genes = len(all_genes)

  print('there are ' + str(num_genes) + ' unique genes')

  mat = np.zeros([num_genes, num_sigs])

  print(mat.shape)


def load_sigs_to_json():
  import glob

  file_names = glob.glob('files_2-17-2017/hdf*.txt')

  # store all signatures in a dictionary
  exp_sigs = {}

  for inst_filename in file_names:

    inst_sig = inst_filename.split('.txt')[0].split('/')[1].split('_chdir')[0]

    # initialize dictionary for signature
    exp_sigs[inst_sig] = {}

    f = open(inst_filename, 'r')
    lines = f.readlines()

    for inst_line in lines:
      inst_line = inst_line.strip().split(',')

      inst_gene = inst_line[0]
      inst_value = inst_line[1]

      exp_sigs[inst_sig][inst_gene] = inst_value

    f.close()

  json_scripts.save_to_json(exp_sigs, 'proc_data/exp_sigs.json', indent='indent')

main()