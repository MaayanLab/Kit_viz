import json_scripts
import numpy as np
import pandas as pd

def main():

  merge_exp_sigs()

def merge_exp_sigs():
  load_sigs_to_json()

  merge_sigs_to_mat()

def merge_sigs_to_mat():

  tmp_exp_sigs = json_scripts.load_to_dict('proc_data/exp_sigs.json')

  exp_sigs = {}
  for inst_sig in tmp_exp_sigs:

    if 'CD34' not in inst_sig:
      exp_sigs[inst_sig] = tmp_exp_sigs[inst_sig]

  all_sigs = sorted(exp_sigs.keys())

  num_sigs = len(all_sigs)

  print('num_sigs: ' + str(num_sigs))

  # collect all genes across all experimental signatures
  all_genes = []

  for sig_name in exp_sigs:

    inst_sig = exp_sigs[sig_name]

    for inst_gene in inst_sig:

      # fix sept problems
      if '-SEP' in inst_gene:
        inst_num = inst_gene.split('-')[0]
        inst_gene = 'SEPT'+inst_num

      if inst_gene != '-':
        all_genes.append(inst_gene)

  print(len(all_genes))
  all_genes = sorted(list(set(all_genes)))
  print(len(all_genes))

  num_genes = len(all_genes)

  print('there are ' + str(num_genes) + ' unique genes')

  mat = np.zeros([num_genes, num_sigs])

  # fill in the matrix
  for sig_name in exp_sigs:

    inst_sig = exp_sigs[sig_name]

    col_index = all_sigs.index(sig_name)

    for inst_gene in inst_sig :

      # initialize value as false
      inst_value = False

      if inst_gene in all_genes:
        inst_value = inst_sig[inst_gene]

      if inst_value != False:

        row_index = all_genes.index(inst_gene)

        # fill in matrix
        mat[row_index, col_index] = inst_value

  # save as dataframe
  df = pd.DataFrame(data=mat, columns = all_sigs, index = all_genes)

  df.to_csv('proc_data/exp_sigs.txt', sep='\t')


def load_sigs_to_json():
  import glob

  print('load')

  # normal files
  file_names = glob.glob('files_2-17-2017/hdf_day*.txt')

  # # full char dir files
  # file_names = glob.glob('files_2-17-2017/big*.txt')

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