import os
import pandas as pd

num_poems = 712
df = pd.read_csv("/home/sami_bb/simply/src/updated_twitter.csv")

for i in range(num_poems):
    poem = df["poems"][i]
    action = os.system('mkdir /home/sami_bb/simply/images_2/%s' % (str(i)))
    action2 = os.system('python /home/sami_bb/VQGAN-CLIP/generate.py -p "%s" -s 575 575 -i 80 -se 10' % (str(poem)))
    action3 = os.system('mv output.png /home/sami_bb/simply/images_2/%s' % (str(i)))
    with open('poem.txt', 'w') as f:
            f.write(poem)
    action4 = os.system('mv poem.txt /home/sami_bb/simply/images_2/%s' % (str(i)))

