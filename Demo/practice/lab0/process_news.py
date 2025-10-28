#!/usr/bin/env python3
"""
Lab 0: News Text Processing and Keyword Extraction
Processes news articles and extracts titles, dates, and keywords.
"""

import os
import csv
from pathlib import Path
from collections import Counter
import re


def read_article(filepath):
    """
    Read a news article file and extract title, date, and content.
    
    Args:
        filepath: Path to the news article file
        
    Returns:
        dict with 'title', 'date', and 'content' keys
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    article = {
        'title': '',
        'date': '',
        'content': ''
    }
    
    for i, line in enumerate(lines):
        if line.startswith('Title:'):
            article['title'] = line.replace('Title:', '').strip()
        elif line.startswith('Published:'):
            article['date'] = line.replace('Published:', '').strip()
        elif line.startswith('Content:'):
            # Everything after "Content:" is the article content
            article['content'] = ''.join(lines[i:]).replace('Content:', '').strip()
            break
    
    return article


def extract_keywords(text, num_keywords=3):
    """
    Extract the most common keywords from text.
    
    Args:
        text: The text to analyze
        num_keywords: Number of keywords to extract (default: 3)
        
    Returns:
        list of top keywords
    """
    # Convert to lowercase and remove punctuation
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Split into words
    words = text.split()
    
    # Common stop words to filter out
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
        'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
        'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these',
        'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'them', 'their',
        'what', 'which', 'who', 'when', 'where', 'why', 'how', 'all', 'each',
        'every', 'both', 'few', 'more', 'most', 'other', 'some', 'such', 'no',
        'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very'
    }
    
    # Filter out stop words and short words
    filtered_words = [
        word for word in words 
        if word not in stop_words and len(word) > 3
    ]
    
    # Count word frequencies
    word_counts = Counter(filtered_words)
    
    # Get top keywords
    top_keywords = [word for word, count in word_counts.most_common(num_keywords)]
    
    return top_keywords


def process_news_articles(articles_dir, output_csv):
    """
    Process all news articles in a directory and save to CSV.
    
    Args:
        articles_dir: Directory containing news article files
        output_csv: Path to output CSV file
    """
    # Find all .txt files in the articles directory
    articles_path = Path(articles_dir)
    txt_files = sorted(articles_path.glob('*.txt'))
    
    if not txt_files:
        print(f"No .txt files found in {articles_dir}")
        return
    
    print(f"Found {len(txt_files)} news articles to process")
    
    # Process each article
    results = []
    for txt_file in txt_files:
        print(f"Processing: {txt_file.name}")
        
        # Read article
        article = read_article(txt_file)
        
        # Extract keywords from content
        keywords = extract_keywords(article['content'], num_keywords=3)
        
        # Store result
        results.append({
            'filename': txt_file.name,
            'title': article['title'],
            'date': article['date'],
            'keyword1': keywords[0] if len(keywords) > 0 else '',
            'keyword2': keywords[1] if len(keywords) > 1 else '',
            'keyword3': keywords[2] if len(keywords) > 2 else ''
        })
    
    # Write to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['filename', 'title', 'date', 'keyword1', 'keyword2', 'keyword3']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    
    print(f"\nResults saved to: {output_csv}")
    print(f"Processed {len(results)} articles successfully!")


def main():
    """Main function to run the news processing script."""
    # Define paths
    articles_dir = '../sample_news_articles'
    output_csv = 'news_data.csv'
    
    # Process articles
    process_news_articles(articles_dir, output_csv)
    
    # Display results
    print("\n" + "="*60)
    print("Preview of extracted data:")
    print("="*60)
    
    with open(output_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"\nFile: {row['filename']}")
            print(f"Title: {row['title'][:60]}...")
            print(f"Date: {row['date']}")
            print(f"Keywords: {row['keyword1']}, {row['keyword2']}, {row['keyword3']}")


if __name__ == '__main__':
    main()
