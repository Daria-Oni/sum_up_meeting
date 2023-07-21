# MeetSummary - Meeting summary generator

## Description
MeetSummary is a Python script that uses OpenAI's GPT-3.5-turbo model to automatically generate a summary of a meeting transcript. The program supports input files in .txt, .pdf, or .docx formats. 

## Privacy notice
Please note that this script sends your text data to OpenAI's servers for processing. If your data is sensitive, please review OpenAI's data usage policy before running this script.

## Note on the use of AI model from OpenAI
The script uses OpenAI's AI model to generate the summary. Please be aware that the output is not deterministic, meaning each run might yield a slightly different summary. Furthermore, the quality of the summary is highly dependent on the quality of the AI model's performance and the input data.

## Installation

1. Clone this repository to your local machine.
2. Install the necessary Python libraries. In your terminal, navigate to the directory containing `meetsum.py` and `requirements.txt`, then run the following command:
pip install -r requirements.txt

## Usage
To run the script, use the following command in your terminal:
python meetsum.py "<path_to_file>"

Replace `<path_to_file>` with the path to the meeting transcript file you wish to summarize.

## Output
The script will generate a Word document containing the meeting summary and save it in the same directory as the input file. The name of the output file will be the same as the input file, but with "_summary.docx" appended to the end.

## Note
The OpenAI API key should be provided in the code where indicated.

## Contribution
If you'd like to contribute to this project, feel free to submit a pull request.

