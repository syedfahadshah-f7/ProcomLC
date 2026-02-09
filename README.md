# LangChain Mysteries Competition Submission

🔍 **AI-based Investigation Competition** - Solve digital mysteries using Speech-to-Text, Document Analysis, and LangChain Reasoning

## 📋 Competition Overview

**Event**: PROCOM 26 - LangChain Mysteries  
**Date**: February 11, 2026  
**Duration**: 3 hours  
**Organizer**: FAST NUCES Karachi

### Scoring Structure
- **Stage 1** (Audio Intelligence): 30%
- **Stage 2** (Document Forensics): 30%
- **Stage 3** (Final Reasoning): 30%
- **Code Quality**: 10%
- **Bonus**: Modular pipelines, logical reasoning, clean documentation

## 🏗️ Project Structure

```
ProcomLangchain/
├── app.py                          # Flask web application
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── README.md                       # This file
│
├── src/                           # Source code
│   ├── utils/
│   │   ├── config.py              # Configuration management
│   │   └── __init__.py
│   │
│   ├── stage1_audio/              # Stage 1: Audio Intelligence
│   │   ├── stage1_audio_pipeline.py    # Speech-to-Text + LangChain Q&A
│   │   ├── audio_generator.py          # Dummy audio file generator
│   │   └── __init__.py
│   │
│   ├── stage2_documents/          # Stage 2: Document Forensics
│   │   ├── stage2_document_pipeline.py # Document analysis (NO embeddings)
│   │   ├── dummy_dossier_generator.py  # Dossier generator
│   │   └── __init__.py
│   │
│   └── stage3_reasoning/          # Stage 3: Final Case Resolution
│       ├── stage3_reasoning_pipeline.py # Multi-step reasoning chain
│       ├── case_generator.py            # Case file generator
│       └── __init__.py
│
├── data/                          # Data directory
│   ├── dummy_audio/               # Generated audio files
│   ├── dummy_documents/           # Generated dossiers
│   ├── dummy_case/                # Generated case files
│   └── *.json                     # Results files
│
└── tests/                         # Unit tests (optional)
```

## 🚀 Quick Start

### 1. Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Create a `.env` file from the template:
```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here  # Optional
```

### 3. Run the Application

#### Option A: Web Interface (Recommended)
```bash
python app.py
```
Then open your browser to: `http://localhost:5000`

#### Option B: Command Line

**Generate Dummy Data:**
```bash
python src/stage1_audio/audio_generator.py
python src/stage2_documents/dummy_dossier_generator.py
python src/stage3_reasoning/case_generator.py
```

**Run Each Stage:**
```bash
# Stage 1: Audio Intelligence
python src/stage1_audio/stage1_audio_pipeline.py

# Stage 2: Document Forensics
python src/stage2_documents/stage2_document_pipeline.py

# Stage 3: Final Case Resolution
python src/stage3_reasoning/stage3_reasoning_pipeline.py
```

## 📊 Competition Stages

### Stage 1: Audio Intelligence (30%)

**Objective**: Process 4 audio files using Speech-to-Text + LangChain to extract answers

**Technology Stack**:
- **Speech-to-Text**: Deepgram (with Diarization) / OpenAI Whisper
- **LLM Processing**: LangChain + OpenAI GPT
- **Q&A Extraction**: Custom prompt engineering

**Implementation**:
- Transcribe audio with speaker diarization
- Use LangChain chains to answer 5-6 questions per audio file
- Extract specific information (names, locations, dates, suspicious activities)

**Files**:
- `src/stage1_audio/stage1_audio_pipeline.py` - Main pipeline (Deepgram integrated)
- `src/stage1_audio/audio_generator.py` - Dummy data generator

---

### Stage 2: Document Forensics (30%)

**Objective**: Extract forensic information from multi-page dossier (PDF, TXT, CSV)

**Key Requirements**:
- ❌ **NO OCR tools allowed**
- ❌ **NO vector databases or embeddings**
- ✅ Direct LLM processing only

**Extraction Targets**:
1. Who accessed system logs
2. Who accessed financial records
3. Who conducted unauthorized experiments

**Technology Stack**:
- **Document Loading**: PyPDF2, pandas (CSV), python-docx
- **Processing**: LangChain with direct LLM calls
- **Method**: `StuffDocumentsChain` or direct prompting

**Files**:
- `src/stage2_documents/stage2_document_pipeline.py` - Main pipeline
- `src/stage2_documents/dummy_dossier_generator.py` - Dossier generator

---

### Stage 3: Final Case Resolution (30%)

**Objective**: Use multi-step reasoning to determine the culprit

**Reasoning Chain**:
1. **Evidence Aggregation**: Combine Stages 1 & 2 results
2. **Suspect Identification**: List all potential suspects
3. **Motive Analysis**: Evaluate motives for each suspect
4. **Opportunity Analysis**: Assess who had opportunity
5. **Means Analysis**: Determine who had the means
6. **Final Determination**: Logical conclusion on the culprit

**Technology Stack**:
- **Reasoning**: LangChain Sequential Chains
- **Logic**: Chain of Thought prompting
- **Output**: Explainable decision with reasoning steps

**Files**:
- `src/stage3_reasoning/stage3_reasoning_pipeline.py` - Reasoning pipeline
- `src/stage3_reasoning/case_generator.py` - Case file generator

## 🎯 Competition Compliance

### ✅ Allowed Technologies
- ✓ Python
- ✓ LangChain
- ✓ Whisper / HuggingFace / Deepgram
- ✓ GPT-style LLMs (OpenAI / Groq)
- ✓ Flask or FastAPI

### ❌ Prohibited Technologies
- ✗ OCR tools
- ✗ Vector databases or embeddings
- ✗ Manual or hard-coded answers
- ✗ Unauthorized APIs

### 🏆 Code Quality Features
- ✓ **Modular Architecture**: Each stage is independent
- ✓ **Clean Documentation**: Comprehensive README and inline comments
- ✓ **Logical Reasoning**: Multi-step reasoning chains with transparency
- ✓ **Error Handling**: Proper exception handling throughout
- ✓ **Dummy Data**: Complete testing without external dependencies

## 🧪 Testing

### With Dummy Data (No API Key Required)

The project includes complete dummy data generation that works without API keys:

```bash
# Generate all dummy data
python src/stage1_audio/audio_generator.py
python src/stage2_documents/dummy_dossier_generator.py
python src/stage3_reasoning/case_generator.py

# Run with basic functionality
python app.py
```

### With OpenAI API Key (Full Functionality)

1. Add `OPENAI_API_KEY` to `.env`
2. Run the application
3. All LangChain reasoning will use actual LLM processing

### 3. Rigorous Multi-Scenario Testing

To ensure robustness, the project includes a rigorous test suite that validates the pipeline against multiple distinct scenarios:

- **Scenario A**: "The Poisoned Researcher" (Original Case)
- **Scenario B**: "The Sabotaged Prototype" (New Test Case)

Run the rigorous test suite:
```bash
python rigorous_tests.py
```
This script will:
1. Generate data for Scenario A
2. Run Stages 1-3
3. Verify correct culprit identification (Sarah Chen)
4. Clean environment
5. Generate data for Scenario B
6. Run Stages 1-3
7. Verify correct culprit identification (Victor Krum)

## 📦 Dependencies

**Core**:
- `langchain` - LangChain framework
- `langchain-openai` - OpenAI integration
- `openai` - OpenAI API client

**Speech & Audio**:
- `openai-whisper` - Speech-to-text transcription
- `gTTS` - Text-to-speech (for dummy audio generation)
- `pydub` - Audio processing

**Documents**:
- `PyPDF2` - PDF processing
- `python-docx` - Word document processing

**Web Framework**:
- `flask` - Web application framework
- `flask-cors` - CORS support

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Web interface |
| `/generate/audio` | POST | Generate dummy audio files |
| `/generate/dossier` | POST | Generate investigation dossier |
| `/generate/case` | POST | Generate case files |
| `/stage1/process` | POST | Run Stage 1 pipeline |
| `/stage2/analyze` | POST | Run Stage 2 pipeline |
| `/stage3/solve` | POST | Run Stage 3 pipeline |
| `/run-all` | POST | Run complete pipeline |
| `/health` | GET | Health check |

## 📝 Mystery Case Overview

The included dummy data tells a cohesive mystery story:

**Victim**: Dr. Robert Kane (biochemistry researcher)  
**Incident**: Found unconscious in lab with evidence of theft  
**Suspects**: 
- Dr. Sarah Chen (professional rival)
- Professor James Mitchell (unauthorized experiments)
- David Park (IT admin with system access)

**Evidence Sources**:
- 4 audio interviews (security, lab assistant, witness, emergency call)
- 8-page investigation dossier
- Additional forensic evidence

**Resolution**: Multi-step reasoning chain determines the culprit based on motive, opportunity, and means

## 🎓 Educational Value

This project demonstrates:
1. **Speech-to-Text Integration** with LangChain
2. **Document Processing** without vector databases
3. **Multi-Step Reasoning Chains** for complex decision-making
4. **Modular Python Architecture** for AI applications
5. **RESTful API Design** with Flask
6. **Prompt Engineering** for specific extraction tasks

## 🤝 Contributing

This is a competition submission. For any questions or issues:
- Contact: (Competition Team)

## 📄 License

Educational/Competition Use

## 🏁 Competition Day Checklist

- [ ] Verify OPENAI_API_KEY is set
- [ ] Test all three stages individually
- [ ] Test complete pipeline (`/run-all`)
- [ ] Ensure no hard-coded answers
- [ ] Verify compliance (no OCR, no embeddings)
- [ ] Check code quality and documentation
- [ ] Prepare for live demonstration

---

**Good luck with the competition! 🚀**
