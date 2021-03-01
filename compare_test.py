from compare_ssim import cmp_ssim
import os

lngth13 = os.listdir('figures/qual_results/sketchy/13')
print(lngth)
for i in range(len(lngth13)):
  cmp_ssim --first lngth13[i] --second lngth13[i+1]

