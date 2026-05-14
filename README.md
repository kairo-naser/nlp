# NLP Labs Repository

This repository contains a collection of Jupyter notebooks for Natural Language Processing (NLP) labs and experiments. The labs cover fundamental NLP concepts, text representation techniques, and machine learning applications on cybersecurity data.

## Contents

### Notebooks
- **4C_Lab_Text_Representation.ipynb**: Lab on text representation techniques including CountVectorizer, TF-IDF, and basic preprocessing.
- **nltk-nlp-lab.ipynb**: Introduction to NLTK library covering tokenization, stop words, POS tagging, and lemmatization.
- **gbt.ipynb**: Training a Gradient Boosting Trees model for text classification using cybersecurity attack data.

### Data Files
- **cybersecurity_attacks.csv**: Dataset containing 40,000 records of cybersecurity attacks with 25 metrics including timestamps, IP addresses, protocols, attack types, and more.
- **evaluation.csv**: Evaluation results and metrics from model training.

### Archive
- **archive/**: Contains archived versions of datasets and documentation.
  - **cybersecurity_attacks.csv**: Original dataset file.
  - **README.md**: Detailed description of the cybersecurity attacks dataset columns.

## Prerequisites

- Python 3.x
- Jupyter Notebook
- Required libraries: pandas, nltk, scikit-learn, etc. (install via pip as needed in notebooks)

## Usage

1. Clone the repository:
   ```
   git clone <repository-url>
   cd nlp
   ```

2. Install dependencies (if not using notebook installs):
   ```
   pip install pandas nltk scikit-learn
   ```

3. Open and run the notebooks in Jupyter:
   ```
   jupyter notebook
   ```

4. Start with the basic labs and progress to machine learning applications.

## Dataset Description

The cybersecurity_attacks.csv dataset includes the following columns:
- Timestamp
- Source/Destination IP Addresses and Ports
- Protocol, Packet Length, Packet Type
- Traffic Type, Payload Data
- Malware Indicators, Anomaly Scores
- Alerts/Warnings, Attack Type, Attack Signature
- Action Taken, Severity Level
- User/Device/Network Information
- Geo-location Data, Proxy Information
- Firewall Logs, IDS/IPS Alerts, Log Source

## Contributing

Feel free to contribute improvements, additional labs, or bug fixes.

## License

[Add license information if applicable]