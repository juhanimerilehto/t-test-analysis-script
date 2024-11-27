# Statistical Analysis Suite - T-Test Module

**Version 1.0**
### Creator: Juhani Merilehto - @juhanimerilehto - Jyväskylä University of Applied Sciences (JAMK), Likes institute

![JAMK Likes Logo](./assets/likes_str_logo.png)

## Overview

T-Test analysis script. This Python-based tool enables automated statistical analysis using Student's t-test for comparing means between two groups. Developed for the Strategic Exercise Information and Research unit in Likes Institute, at JAMK University of Applied Sciences, this module provides comprehensive statistical output including visualizations, Excel reports, and terminal feedback.

## Features

- **Automated Analysis**: Complete t-test analysis with minimal setup required
- **Comprehensive Output**: Statistical results, visualizations, and detailed Excel reports
- **Data Visualization**: Automated generation of boxplots and swarmplots
- **Excel Integration**: Detailed results exported to Excel workbooks
- **Terminal Feedback**: Real-time analysis results in the terminal
- **Tested**: Script tested to work with simulated data

## Hardware Requirements

- **Python:** 3.8 or higher
- **RAM:** 8GB recommended
- **Storage:** 1GB free space for analysis outputs
- **OS:** Windows 10/11, MacOS, or Linux

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/juhanimerilehto/t-test-analysis-script.git
cd t-test-analysis-script
```

### 2. Create a virtual environment:
```bash
python -m venv stats-env
source stats-env/bin/activate  # For Windows: stats-env\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python t-test.py
```

With custom parameters:
```bash
python t-test.py --excel_path "your_data.xlsx" --group_column "Group" --value_column "Value"
```

## Configuration Parameters

- `excel_path`: Path to Excel file (default: 'data.xlsx')
- `group_column`: Column containing group labels (default: 'Group')
- `value_column`: Column containing measurements (default: 'Value')
- `group1_name`: Name of first group (default: 'Control')
- `group2_name`: Name of second group (default: 'Treatment')
- `output_prefix`: Prefix for output files (default: 'ttest')

## File Structure

```plaintext
statistical-analysis-suite/
├── ttest/
│   ├── assets/
│   │   └── likes_str_logo.png
│   ├── ttest_analysis.py
│   ├── requirements.txt
│   └── README.md
```

## Credits

- **Juhani Merilehto (@juhanimerilehto)** – Specialist, Data and Statistics
- **JAMK Likes** – Organization sponsor

## License

This project is licensed for free use under the condition that proper credit is given to Juhani Merilehto (@juhanimerilehto) and JAMK Likes institute. You are free to use, modify, and distribute this project, provided that you mention the original author and institution and do not hold them liable for any consequences arising from the use of the software.