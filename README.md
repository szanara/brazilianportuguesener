# brazilianportuguesener
 This repository corresponds to the implementation for the research work titled "Combining Model Soups and Domain Adaptation for Portuguese Named Entity Recognition".


**Folder Structure and Descriptions:**

1. codes_to_extract

* Contains the prompts used to extract entities via Large Language Models (LLMs).
* Both the prompts and the comments in the code are written in Brazilian Portuguese.
* Feel free to adapt the prompts or comments to suit your needs.


2. Data

* Includes the datasets used in the experiments.
* Contains scripts for data preparation and preprocessing.

3. fewshot_selection

* Provides the code used for few-shot sample selection.
* Ensures consistent sample usage across different models by following the random selection method described in the paper.
* Includes code for similarity calculations to select the closest tokens.

3. Gliner

* Contains the notebook used to execute experiments with Gliner.

4. post_processing

* Features utility functions for post-processing.
* Helps handle cases where models did not produce the expected output format by removing unwanted information.

5. notebooks
* Notebooks that use the functions located in the `codes_to_extract` folder. These notebooks support both modes:
  -  zero-shot bner
  -  zero shot
  -  few-shot bner.
  -  few-shot
  
The data used is the prepared data, which is generated and stored in a folder after running the script `Preparing_data.py`.
The notebooks illustrate how to use the functions with this data. The BNER notebooks are indicated by the “tip” at the end of the file name.
For more details about what “bner” means, please refer to the paper.
   
6. External Codes

Any external code included in this repository is accompanied by a .txt file providing proper attribution and relevant information.

**Additional Notes:**
 - Most comments in the code are written in Brazilian Portuguese.
- If you use the code or datasets from this repository, please cite the following research paper:

Souza, M., Monteiro, M., & Zanchettin, C. (2026).
Tackling low-resource NER: Exploring model soup, domain adaptation, few-shot and zero-shot strategies.
Applied Soft Computing, 189, 114501.
🔗 https://www.sciencedirect.com/science/article/pii/S1568494625018149
 >  @article{SOUZA2026114501,
  title   = {Tackling low-resource NER: Exploring model soup, domain adaptation, few-shot and zero-shot strategies},
  journal = {Applied Soft Computing},
  volume  = {189},
  pages   = {114501},
  year    = {2026},
  issn    = {1568-4946},
  doi     = {https://doi.org/10.1016/j.asoc.2025.114501},
  url     = {https://www.sciencedirect.com/science/article/pii/S1568494625018149},
  author  = {Maynara Souza and Monique Monteiro and Cleber Zanchettin},
  keywords= {Named entity recognition (NER), Low-resource languages, Few-shot learning, Model soups}
} 



**Codes related to model soup and domain adaptation are available on: https://github.com/monilouise/opt-bert-ner**
