# Causal Interpretability & Wanna Contraction

This repository contains the code and data for the following paper:

> **Do Large Language Models Internalize Syntactic Constraints? A Causal Intervention Study of *Wanna* Contraction**

## Overview

This study investigates whether large language models have internalized the syntactic constraints governing *wanna* contraction using causal interpretability methods. We adapt the [CausalGym](https://github.com/aryamanarora/causalgym) framework (Arora et al., 2024) and apply it to the [Pythia](https://github.com/EleutherAI/pythia) model family (Biderman et al., 2023), ranging from 14M to 2.8B parameters.

## Repository Structure

```
wanna_causal_interpretability/
├── wanna_contraction.json             # Dataset
├── data_directional.py                # Directional data loading
├── das_directional.py                 # Directional DAS experiment
├── test_all_directional.py            # Run all experiments
└── causalgym_directional.py           # Google Colab notebook
```

## Requirements

This code is built on top of CausalGym. Please first clone the CausalGym repository and install the required libraries:

```bash
git clone https://github.com/aryamanarora/causalgym.git
cd causalgym
pip install -r requirements.txt
```

Required library versions:

```
numpy==1.26.4
pandas==2.2.2
plotnine==0.14.1
scikit_learn==1.5.2
scipy==1.13.1
torch==2.5.1
tqdm==4.66.6
transformers==4.46.2
```

## Usage

Place `wanna_contraction.json` in the `data/templates/` directory of the CausalGym repository, then run the following commands:

```bash
# wantto_to_wanna condition (want to = base, wanna = source)
python test_all_directional.py --model EleutherAI/pythia-1b \
    --datasets wanna_contraction/wanna_contraction \
    --direction wantto_to_wanna

# wanna_to_wantto condition (wanna = base, want to = source)
python test_all_directional.py --model EleutherAI/pythia-1b \
    --datasets wanna_contraction/wanna_contraction \
    --direction wanna_to_wantto
```

For Google Colab users, `causalgym_directional.py` provides a step-by-step pipeline for running the experiments.

## Citation

If you use this code or data, please cite the original CausalGym paper upon which this study is based:

```bibtex
@inproceedings{arora-etal-2024-causalgym,
  title={CausalGym: Benchmarking causal interpretability methods on linguistic tasks},
  author={Arora, Aryaman and Jurafsky, Dan and Potts, Christopher},
  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},
  pages={14638--14663},
  year={2024}
}
```
