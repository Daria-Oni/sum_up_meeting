"""
meetsum.py
Author: Daria^^

This Python script uses OpenAI's GPT-3.5-turbo model to automatically generate a summary of a meeting transcript. 
The program can be called from the command line and supports input files in .txt, .pdf, or .docx formats.

**Privacy notice:**
This script sends your text data to OpenAI's servers for processing. 
If your data is sensitive, please review OpenAI's data usage policy before running this script.

Usage: python meetsum.py "<path_to_file>"

where "<path_to_file>" is the path to the meeting transcript file.
"""

import os
import argparse
import textract
import openai
from docx import Document

# Your OpenAI API key
openai.api_key = "<YOUR-OPEN-AI-API-KEY>"

# Maximum number of tokens that can be processed by GPT-3 in one request
# One average 1 token is approximately 4.5 characters including spaces. 
MAX_TOKENS = 4096

def summarize_text(text):
    """
    This function takes a string of text as input and returns a summarized version of the text.
    It uses the OpenAI GPT-3 model to generate the summary.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant for a project manager and a part of the team. Your role is to distill information and present it in an organized and easily digestible manner."},
            {"role": "user", "content": f"I need you to summarize the following text: '{text}'. Please keep it brief and focus on the most critical points. Make a concise title that captures the main theme, and outline only the key points, facts, and discussions. Use bullet points, numbered lists, or sections with subtitles, where appropriate. Try to fit the summary in under one page."},
        ],
    )
    return response["choices"][0]["message"]["content"]

def summarize_meeting(file_path):
    """
    This function takes a path to a meeting transcript file as input,
    reads the content of the file, splits it into chunks if necessary,
    sends each chunk to the summarize_text function to generate a summary,
    then writes the summary to a new .docx file in the same directory as the input file.
    """

    text = textract.process(file_path).decode().lower()

    chunks = [text[i:i+MAX_TOKENS] for i in range(0, len(text), MAX_TOKENS)]

    print(f"Total chunks: {len(chunks)}")

    # Generate a summary for each chunk and concatenate them together
    summary = ""
    for i, chunk in enumerate(chunks):
        print(f"Summarizing chunk {i+1}/{len(chunks)}")
        chunk_summary = summarize_text(chunk)
        summary += chunk_summary + "\n"
        
    # Check if the summary text exceeds the maximum token limit
    tokens = len(summary) / 4.5  # approximate number of tokens
    if tokens > MAX_TOKENS:
        print("Intermediate summary is too long, summarizing again...")
        summary = summarize_text(summary)
    else:
        print("Intermediate summary is within token limit, no additional summarization required.")
    
    print('Generating the summary document...')

    # Create a Word document
    doc = Document()
    doc.add_paragraph(summary)

    summary_file = file_path.replace(os.path.splitext(file_path)[1], "_summary.docx")
    doc.save(summary_file)

    print(f'Summary saved to: {summary_file}')

def main():
    """
    This function parses the command line arguments and calls the summarize_meeting function.
    """

    parser = argparse.ArgumentParser(description="Summarize a meeting transcript.")
    parser.add_argument("file", help="Path to the transcript file (txt, pdf, docx)")
    args = parser.parse_args()

    summarize_meeting(args.file)

if __name__ == "__main__":
    main()