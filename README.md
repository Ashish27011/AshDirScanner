# AshDirScanner 🔎

AshDirScanner is a Python-based web directory scanner designed for learning web reconnaissance and HTTP request handling.

The tool takes a target URL, generates paths from a wordlist, sends HTTP requests, filters responses, and produces a structured report.

## 🚀 Features

- Target URL validation
- Wordlist-based path generation
- HTTP request scanning
- Response filtering
- HTTP status code detection
- Server header extraction
- Content-Type detection
- Content-Length detection
- Request delay using `time.sleep()`
- Terminal-based results
- Automatic report generation

## 🧠 Project Workflow

```text
Target URL
    ↓
Validator
    ↓
Wordlist
    ↓
URL Generation
    ↓
Response Filtering
    ↓
HTTP Scanner
    ↓
Response Analysis
    ↓
Reporter
    ↓
report.txt
