from tqdm import tqdm
import time

prog_list = [1,2,3,4] #---> the progress will be longer or shorter by the number of list

for pro in tqdm(prog_list):
	time.sleep(1)
