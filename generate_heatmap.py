def main():

  merge_exp_sigs()

def merge_exp_sigs():
  import glob

  file_names = glob.glob('files_2-17-2017/hdf*.txt')

  for inst_filename in file_names:

    f = open(inst_filename, 'r')
    lines = f.readlines()
    f.close()

main()