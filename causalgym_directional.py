# Clone CausalGym GitHub Repository
!git clone https://github.com/aryamanarora/causalgym.git
%cd causalgym


# Uninstall existing libraries to match versions required by CausalGym
!pip uninstall -y transformers torch torchvision torchaudio


# Install libraries matching the versions required by CausalGym
# Session will restart after running this code!
!pip install -r requirements.txt


# Re-clone CausalGym GitHub Repository
!git clone https://github.com/aryamanarora/causalgym.git
%cd causalgym


from google.colab import files
import os

uploaded = files.upload()
for filename in uploaded.keys():
    os.rename(filename, f'/content/causalgym/{filename}')


# Check library versions required for CausalGym implementation
# CausalGym requires specific versions of the following libraries

# numpy==1.26.4
# pandas==2.2.2
# plotnine==0.14.1
# scikit_learn==1.5.2
# scipy==1.13.1
# torch==2.5.1
# tqdm==4.66.6
# transformers==4.46.2


import numpy, pandas, plotnine, sklearn, scipy, torch, tqdm, transformers

print(numpy.__version__)
print(pandas.__version__)
print(plotnine.__version__)
print(sklearn.__version__)
print(scipy.__version__)
print(torch.__version__)
print(tqdm.__version__)
print(transformers.__version__)


# Verify CausalGym GitHub Repository clone
!ls


# CausalGym GitHub Repository templates directory
# Customized dataset JSON files must exist in this directory
!ls data/templates


# Upload JSON files
from google.colab import files
uploaded = files.upload()


# Paste JSON files into data/templates directory
!cp wanna_contraction.json data/templates/wanna_contraction.json


# Verify JSON file upload
!ls data/templates


# wantto_to_wanna condition: want_to=base, wanna=src
!python test_all_directional.py --model EleutherAI/pythia-6.9b --datasets wanna_contraction/wanna_contraction --direction wantto_to_wanna
!python test_all_directional.py --model EleutherAI/pythia-6.9b --datasets wanna_contraction/wanna_contraction --direction wantto_to_wanna --manipulate dog-give


# wanna_to_wantto condition: wanna=base, want_to=src
!python test_all_directional.py --model EleutherAI/pythia-6.9b --datasets wanna_contraction/wanna_contraction --direction wanna_to_wantto
!python test_all_directional.py --model EleutherAI/pythia-6.9b --datasets wanna_contraction/wanna_contraction --direction wanna_to_wantto --manipulate dog-give


# Verify JSON file creation
# 2 files per model (original + dog-give)
!ls logs/das


# Download experimental result JSON files
# Download 2 files per model (wantto_to_wanna + wanna_to_wantto)
import glob, time
from google.colab import files

for json_file in sorted(glob.glob('logs/das/*pythia-6.9b*.json')):
    files.download(json_file)
    time.sleep(1)


import warnings, logging
import plot as plot_module
from plot import plot_per_pos
import os, shutil, glob, pandas as pd

logging.getLogger('matplotlib.font_manager').setLevel(logging.ERROR)


# Plot for wantto_to_wanna direction (Source: want to -> Base: wanna)
os.makedirs('logs/das_wantto_to_wanna', exist_ok=True)
for f in glob.glob('logs/das/*wanna_contraction*wantto_to_wanna.json'):
    shutil.copy(f, 'logs/das_wantto_to_wanna/')
if os.path.exists('logs/das_wantto_to_wanna/combined.csv'):
    os.remove('logs/das_wantto_to_wanna/combined.csv')

plot_module.classification['wanna_contraction'] = 'Custom'
plot_module.classification_order.append('Custom')

df = plot_module.load_directory('logs/das_wantto_to_wanna/', reload=True)
df['manipulate'] = df['manipulate'].fillna('none').replace('orig', 'none')
df['step'] = -1
df.to_csv('logs/das_wantto_to_wanna/combined.csv', index=False)

plot_per_pos('logs/das_wantto_to_wanna/', reload=False, metric='odds', plot_all=True, template_filename='wanna')


# Plot for wanna_to_wantto direction (Source: wanna -> Base: want to)
os.makedirs('logs/das_wanna_to_wantto', exist_ok=True)
for f in glob.glob('logs/das/*wanna_contraction*wanna_to_wantto.json'):
    shutil.copy(f, 'logs/das_wanna_to_wantto/')
if os.path.exists('logs/das_wanna_to_wantto/combined.csv'):
    os.remove('logs/das_wanna_to_wantto/combined.csv')

plot_module.classification['wanna_contraction'] = 'Custom'
plot_module.classification_order.append('Custom')

df = plot_module.load_directory('logs/das_wanna_to_wantto/', reload=True)
df['manipulate'] = df['manipulate'].fillna('none').replace('orig', 'none')
df['step'] = -1
df.to_csv('logs/das_wanna_to_wantto/combined.csv', index=False)

plot_per_pos('logs/das_wanna_to_wantto/', reload=False, metric='odds', plot_all=True, template_filename='wanna')


# Convert PDF to PNG and display inline
!apt-get install -q poppler-utils

from IPython.display import display, Image
import glob, subprocess

for directory in ['logs/das_wantto_to_wanna', 'logs/das_wanna_to_wantto']:
    for pdf in sorted(glob.glob(f'{directory}/figs_*_odds_all.pdf')):
        png = pdf.replace('.pdf', '.png')
        subprocess.run(['pdftoppm', '-r', '150', '-png', '-singlefile', pdf, png.replace('.png', '')])
        print(f'=== {directory} ===')
        display(Image(png))


# Download PNG File
import glob, os
from google.colab import files

for directory in ['logs/das_wantto_to_wanna', 'logs/das_wanna_to_wantto']:
    direction = directory.split('logs/das_')[-1]  # 'wantto_to_wanna' 또는 'wanna_to_wantto'
    for png in sorted(glob.glob(f'{directory}/figs_*_odds_all.png')):
        new_name = f'logs/das_wantto_to_wanna/figs_wanna_contraction_{direction}_odds_all.png'
        os.rename(png, new_name)
        files.download(new_name)