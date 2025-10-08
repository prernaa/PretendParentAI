# PretendParentAI
PretendParentAI — Relatable, Story-Driven Dialogue Generation using Instruction Fine-Tuning (SFT) with PEFT (QLoRA)

## Overview
**PretendParentAI** fine-tunes **Mistral Instruct v0.3** on Reddit parenting data using **Quantized Low-Rank Adaptation (QLoRA)**.  
The goal was to explore whether instruction tuning on real-world parenting discussions could make model responses more *empathetic, warm, and relatable* — while retaining clarity and helpfulness.

## Instruction Tuning (PretendParentAI)

**Base Model:** `mistralai/Mistral-7B-Instruct-v0.3`  
**Fine-tuning Method:** SFT (Supervised Fine Tuning) and PEFT (Parameter Efficient Fine Tuning) with QLoRA (Quantized Low-Rank Adaptation)  
**Compute:** Google Colab A100 (4 hours for 38.4K samples; estimated 112 hrs on T4)  
**Training Samples:** 38,400  
**Validation Samples:** 7,781  
**Epochs:** 2 (best model: `checkpoint-1600`, end of epoch 1)

### Training Summary
| Step | Training Loss | Validation Loss |
|------|----------------|-----------------|
| 400  | 1.9096 | 1.9477 |
| 800  | 1.9365 | 1.9242 |
| 1200 | 1.9312 | 1.9129 |
| **1600** | **1.9265** | **1.9102** |
| 2000 | 1.7578 | 1.9420 |
| 2400 | 1.7656 | 1.9409 |
| 2800 | 1.7687 | 1.9394 |
| 3200 | 1.7579 | 1.9395 |

> Validation loss began increasing in epoch 2, indicating overfitting.  
> **Best model:** `checkpoint-1600` (after 1 epoch).

---

## Evaluation

### Quantitative Metrics

**BLEU**
| Model | BLEU | P@1 | P@2 | P@3 | P@4 | Length Ratio |
|--------|------|-----|-----|-----|-----|---------------|
| Mistral Instruct v0.3 | 0.00695 | 0.1661 | 0.0140 | 0.0023 | 0.0004 | 1.59 |
| PretendParentAI | 0.00624 | 0.1740 | 0.0169 | 0.0016 | 0.0003 | 1.73 |

**ROUGE**
| Model | ROUGE-1 | ROUGE-2 | ROUGE-L | ROUGE-Lsum |
|--------|----------|----------|-----------|--------------|
| Mistral Instruct v0.3 | 0.1774 | 0.0161 | 0.0977 | 0.1040 |
| PretendParentAI | **0.2068** | **0.0215** | **0.1057** | **0.1059** |

**BERTScore (avg.)**
| Model | Precision | Recall | F1 |
|--------|------------|--------|----|
| Mistral Instruct v0.3 | 0.8334 | 0.8440 | 0.8386 |
| PretendParentAI | 0.8323 | 0.8462 | **0.8391** |

> ROUGE and BERTScore show marginal improvement; BLEU remains low (expected for open-ended tasks).

### LLM-as-a-Judge Evaluation

Evaluation used **GPT-4o** as an LLM judge to compare responses from:
- **System A:** Mistral Instruct v0.3 (base)
- **System B:** PretendParentAI (fine-tuned)

Each system was scored on:  
*helpfulness, empathy/tone, creativity, clarity, relatability, adoptability, and overall preference.*

|              | winner\_helpfulness | winner\_empathy\_tone | winner\_creativity | winner\_clarity | winner\_relatability | winner\_adoptability | winner\_overall |
|--------------|---------------------|-----------------------|--------------------|-----------------|----------------------|----------------------|-----------------|
| **System A** | **0.90**            | 0.30                  | 0.47               | **0.90**        | 0.02                 | **0.72**             | **0.72**        |
| **System B** | 0.10                | **0.70**              | **0.48**            | 0.10            | **0.98**             | 0.28                 | 0.28            |
| **Tie**      | 0.00                | 0.00                  | 0.05               | 0.00            | 0.00                 | 0.00                 | 0.00            |

**Interpretation**
- **System A (Mistral)** remains more *helpful*, *clear*, and *adoptable*.  
- **System B (PretendParentAI)** excels in *empathy* and *relatability*, and is slightly more *creative*.  
- While System A’s responses are helpful 90% of the time, their adoptability is 72% — showing that *users sometimes prefer System B due to emotional tone and resonance, despite lower clarity*.

---

## Key Learnings
1. Fine-tuning on Reddit data increases empathy and warmth but decreases clarity and factual helpfulness.  
2. Reddit’s casual, noisy, non-evidence-based writing style limits instruction-tuning quality.  
3. More empathetic and relatable advice can increase **adoptability** even if clarity declines.  
4. Future approaches should explore **preference optimization** (e.g., DPO) as a way to increase empathy and relatability in responses while maintaining clarity. 

---

## Next Steps
- Apply **Direct Preference Optimization (DPO)** to balance empathy and clarity.  
- Generate a **synthetic curated dataset** (GPT-generated, not Reddit).  
- Continue using **Mistral Instruct v0.3** as base model with PEFT.  
- Develop **multi-objective alignment** to jointly optimize empathy and factual quality.

---

## Datasets
- **Training Data:** Reddit parenting posts (not publicly shared; contact author for details).  
- **Evaluation Data:** `data_to_share/reddit_gpt_test_samples.jsonl`  
- **Base Model Responses:** `data_to_share/reddit_gpt_test_samples_base_response.jsonl`  
- **Fine-Tuned Model Responses:** `data_to_share/reddit_gpt_test_samples_ft_response.jsonl`  
- **LLM-as-a-Judge Results:** `data_to_share/pretendparentai_gpt_as_judge_output.csv`

---

## Repository Structure
```plaintext
instruction_tuning_qlora/
├── 1_Dataset_Curation_For_Mistral.ipynb
├── 2_Instruction_Tuning_Mistral_7B_Instruct.ipynb
├── 3_and_5_Instruction_Tuning_Evaluation.ipynb
├── 4_GPT_Generate_Test_Reddit_Samples.ipynb
├── 6_GPT_as_a_Judge.ipynb
data_to_share/
├── reddit_gpt_test_samples.jsonl
├── reddit_gpt_test_samples_base_response.jsonl
├── reddit_gpt_test_samples_ft_response.jsonl
└── pretendparentai_gpt_as_judge_output.csv
```
---

## Citation
If you use this work or methodology, please cite as:
```plaintext
@misc{chikersal2025pretendparentai,
author = {Prerna Chikersal},
title = {PretendParentAI – Instruction Fine-Tuning Mistral-7B on Reddit Parenting Data using QLoRA},
year = {2025},
publisher = {GitHub},
howpublished = {\url{https://github.com/prernaa/PretendParentAI}},
note = {Hugging Face Model: https://huggingface.co/prernac1/pretendparentai}
}
```
