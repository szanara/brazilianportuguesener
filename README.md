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

5. External Codes

Any external code included in this repository is accompanied by a .txt file providing proper attribution and relevant information.

**Additional Notes:**
 - Most comments in the code are written in Brazilian Portuguese.
- If you use the code or datasets from this repository, please reference the corresponding research paper.
