# Customer Support JSON Extractor

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

## 📋 Overview

Customer Support JSON Extractor is a powerful AI-powered tool that automatically parses customer support messages and extracts structured information. It transforms unstructured text into standardized JSON format, making it easy to integrate with ticketing systems, analytics platforms, and customer service workflows.

### Key Features

- **🔍 Intelligent Extraction**: Automatically identifies customer names, emails, and issue details
- **📊 Categorization**: Classifies issues into Billing, Technical, Account, Shipping, Refund, or Other
- **⚠️ Urgency Detection**: Assigns urgency levels (Low, Medium, High, Critical) based on message content
- **😊 Sentiment Analysis**: Detects customer sentiment (Positive, Neutral, Negative)
- **📝 Structured Output**: Returns consistent JSON format for easy integration
- **🛡️ Prompt Injection Protection**: Ignores instructions contained in user messages

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/yourusername/customer-support-json-extractor.git
cd customer-support-json-extractor
pip install -r requirements.txt
```

### Basic Usage

```python
from extractor import SupportExtractor

extractor = SupportExtractor()

# Example customer message
message = """
Hi, I'm Sarah Khan.
My package hasn't arrived for 12 days.
My email is sarah@gmail.com.
Please help immediately.
"""

# Extract structured information
result = extractor.extract(message)

# Output JSON
print(result)
```

**Output:**
```json
{
  "customer_name": "Sarah Khan",
  "email": "sarah@gmail.com",
  "issue_type": "Shipping",
  "urgency": "High",
  "summary": "Package delayed for 12 days.",
  "sentiment": "Negative"
}
```

## 📚 Examples

### Sample Inputs and Expected Outputs

| Input | Output |
|-------|--------|
| "I was charged twice this month. Email: alex99@yahoo.com" | `{"customer_name": "", "email": "alex99@yahoo.com", "issue_type": "Billing", "urgency": "High", "summary": "Customer reports being charged twice.", "sentiment": "Negative"}` |
| "My account keeps logging me out. My name is David." | `{"customer_name": "David", "email": "", "issue_type": "Account", "urgency": "Medium", "summary": "Account repeatedly logs out.", "sentiment": "Negative"}` |
| "Thanks! Everything works perfectly now." | `{"customer_name": "", "email": "", "issue_type": "Other", "urgency": "Low", "summary": "Customer confirms issue is resolved.", "sentiment": "Positive"}` |

## 🏗️ Project Structure

```
customer-support-json-extractor/
├── README.md
├── requirements.txt
├── setup.py
├── extractor/
│   ├── __init__.py
│   ├── main.py           # Main extraction logic
│   ├── models.py         # Data models and schemas
│   ├── parser.py         # Text parsing utilities
│   └── prompts.py        # AI prompts and templates
├── tests/
│   ├── __init__.py
│   ├── test_extractor.py
│   └── test_samples.py
├── examples/
│   ├── sample_inputs.txt
│   ├── sample_outputs.json
│   └── demo.py
└── docs/
    ├── API.md
    └── integration_guide.md
```

## 🔧 Configuration

The extractor can be configured using environment variables or a config file:

```python
# config.py
config = {
    "default_urgency": "Medium",
    "sentiment_threshold": 0.7,
    "custom_keywords": {
        "Billing": ["charge", "payment", "invoice"],
        "Technical": ["crash", "error", "bug"]
    }
}
```

## 🧪 Testing

Run the test suite:

```bash
python -m pytest tests/
```

Run sample tests:

```bash
python tests/test_samples.py
```

## 📦 Dependencies

- Python 3.7+
- json
- re (Regular Expressions)
- typing

For production use, consider integrating with:
- OpenAI GPT API for advanced NLP
- SpaCy for named entity recognition
- FastAPI for REST API deployment

## 🌟 Use Cases

1. **Customer Support Automation**: Automatically categorize and route tickets
2. **Analytics Dashboard**: Track customer sentiment and issue trends
3. **CRM Integration**: Populate support records automatically
4. **Priority Escalation**: Identify urgent issues for immediate attention
5. **Quality Monitoring**: Analyze support team performance

## 🔒 Security

- **Prompt Injection Protection**: The system treats user input as data only, ignoring any instructions
- **Data Sanitization**: All extracted fields are validated and sanitized
- **No External API Calls**: All processing is done locally (unless using optional AI integrations)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

```bash
git clone https://github.com/yourusername/customer-support-json-extractor.git
cd customer-support-json-extractor
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
pre-commit install
```

### Pull Request Process

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python's standard library for maximum compatibility
- Inspired by real-world customer support automation needs
- Designed for easy integration with existing workflows

## 📞 Support

For support, email abdulrehmannadeem825@gmail.com or open an issue on GitHub.

---

**Made with ❤️ for the open source community**
```
## Additional Repository Name Suggestions

1. **`support-ticket-parser`**
   - Description: "AI-powered parser for customer support messages that extracts structured JSON data with sentiment and urgency detection"

2. **`cx-intelligence-extractor`**
   - Description: "Customer experience intelligence tool for extracting structured data from support conversations"

3. **`feedback-jsonifier`**
   - Description: "Convert customer feedback messages into structured JSON with automatic categorization and sentiment analysis"

4. **`ticket-classifier-ai`**
   - Description: "Machine learning powered tool to classify and structure customer support tickets"

5. **`support-message-processor`**
   - Description: "Process customer support messages into structured JSON data for analytics and automation"