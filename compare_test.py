from compare_ssim import cmp_ssim
import os

lngth = os.listdir('figures/qual_results/sketchy/13')
print(lngth)
for i in range(len(lngth)):
  cmp_ssim --first lngth[i] --second lngth[i+1]

