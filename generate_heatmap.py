def main():

  merge_exp_sigs()

def merge_exp_sigs():
  import glob
  import json_scripts

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