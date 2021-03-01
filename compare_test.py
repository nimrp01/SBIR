from compare_ssim import cmp_ssim
import os

lngth = len(os.listdir('figures/qual_results/sketchy/13'))
print(lngth)
for i in range(lngth):
  cmp_ssim --first (os.listdir('figures/qual_results/sketchy/13')[i]) --second (os.listdir('figures/qual_results/sketchy/13')[i+1])
  cmp_ssim --first os.listdir('figures/qual_results/sketchy/23')[i] --second os.listdir('figures/qual_results/sketchy/23')[i+1]
  cmp_ssim --first os.listdir('figures/qual_results/sketchy/27')[i] --second os.listdir('figures/qual_results/sketchy/27')[i+1]
  cmp_ssim --first os.listdir('figures/qual_results/sketchy/3')[i] --second os.listdir('figures/qual_results/sketchy/3')[i+1]
  cmp_ssim --first os.listdir('figures/qual_results/sketchy/4')[i] --second os.listdir('figures/qual_results/sketchy/4')[i+1]
