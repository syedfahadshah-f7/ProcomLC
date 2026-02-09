"""
Flask Application for LangChain Mysteries Competition
Main entry point for the competition submission.
"""

from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import os
import json
import sys

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from utils.config import Config
from stage1_audio.stage1_audio_pipeline import AudioIntelligencePipeline
from stage2_documents.stage2_document_pipeline import DocumentForensicsPipeline
from stage3_reasoning.stage3_reasoning_pipeline import CaseReasoningPipeline

app = Flask(__name__)
CORS(app)

# Initialize pipelines
audio_pipeline = None
document_pipeline = None
reasoning_pipeline = None


def init_pipelines(api_key=None):
    """Initialize all pipelines with API key."""
    global audio_pipeline, document_pipeline, reasoning_pipeline
    
    audio_pipeline = AudioIntelligencePipeline(openai_api_key=api_key)
    document_pipeline = DocumentForensicsPipeline(openai_api_key=api_key)
    reasoning_pipeline = CaseReasoningPipeline(openai_api_key=api_key)
    
    print("✓ All pipelines initialized")


# HTML Template for web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>LangChain Mysteries - Competition Submission</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }
        .container { max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
        h2 { color: #34495e; margin-top: 30px; }
        .stage { background: #ecf0f1; padding: 20px; margin: 20px 0; border-radius: 5px; }
        .stage h3 { margin-top: 0; color: #2980b9; }
        button { background: #3498db; color: white; border: none; padding: 12px 24px; border-radius: 5px; cursor: pointer; font-size: 16px; margin: 5px; }
        button:hover { background: #2980b9; }
        .result { background: #d5f4e6; padding: 15px; margin: 10px 0; border-left: 4px solid #27ae60; border-radius: 3px; }
        .error { background: #f8d7da; padding: 15px; margin: 10px 0; border-left: 4px solid #dc3545; border-radius: 3px; }
        pre { background: #2c3e50; color: #ecf0f1; padding: 15px; border-radius: 5px; overflow-x: auto; }
        .status { padding: 10px; margin: 10px 0; border-radius: 5px; }
        .status.success { background: #d4edda; border: 1px solid #c3e6cb; }
        .status.warning { background: #fff3cd; border: 1px solid #ffeaa7; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 LangChain Mysteries Competition Submission</h1>
        <p><strong>Team Submission System</strong> - All 3 Stages Implemented</p>
        
        <div class="status warning">
            <strong>⚠️ API Key Required:</strong> Set your OPENAI_API_KEY in the .env file for full functionality.
            Currently running in: <span id="mode">{{ "Production" if api_key else "Demo Mode" }}</span>
        </div>
        
        <div class="stage">
            <h3>📊 Stage 1: Audio Intelligence (30%)</h3>
            <p>Process audio files using Speech-to-Text + LangChain Q&A</p>
            <button onclick="runStage1()">Run Stage 1</button>
            <button onclick="generateAudio()">Generate Dummy Audio</button>
            <div id="stage1-result"></div>
        </div>
        
        <div class="stage">
            <h3>📄 Stage 2: Document Forensics (30%)</h3>
            <p>Extract information from dossier (NO embeddings, direct LLM processing)</p>
            <button onclick="runStage2()">Run Stage 2</button>
            <button onclick="generateDossier()">Generate Dummy Dossier</button>
            <div id="stage2-result"></div>
        </div>
        
        <div class="stage">
            <h3>🧠 Stage 3: Final Case Resolution (30%)</h3>
            <p>Multi-step reasoning chain to determine the culprit</p>
            <button onclick="runStage3()">Run Stage 3</button>
            <button onclick="generateCase()">Generate Dummy Case Files</button>
            <div id="stage3-result"></div>
        </div>
        
        <h2>📋 Complete Pipeline</h2>
        <button onclick="runAll()" style="background: #e74c3c; font-size: 18px; padding: 15px 30px;">
            🚀 Run All Stages
        </button>
        <div id="all-results"></div>
    </div>
    
    <script>
        function showResult(elementId, data, isError=false) {
            const el = document.getElementById(elementId);
            if (isError) {
                el.innerHTML = '<div class="error"><strong>Error:</strong> ' + data + '</div>';
            } else {
                el.innerHTML = '<div class="result"><pre>' + JSON.stringify(data, null, 2) + '</pre></div>';
            }
        }
        
        async function generateAudio() {
            try {
                const response = await fetch('/generate/audio', { method: 'POST' });
                const data = await response.json();
                showResult('stage1-result', data);
            } catch (error) {
                showResult('stage1-result', error.message, true);
            }
        }
        
        async function generateDossier() {
            try {
                const response = await fetch('/generate/dossier', { method: 'POST' });
                const data = await response.json();
                showResult('stage2-result', data);
            } catch (error) {
                showResult('stage2-result', error.message, true);
            }
        }
        
        async function generateCase() {
            try {
                const response = await fetch('/generate/case', { method: 'POST' });
                const data = await response.json();
                showResult('stage3-result', data);
            } catch (error) {
                showResult('stage3-result', error.message, true);
            }
        }
        
        async function runStage1() {
            try {
                showResult('stage1-result', { status: 'Processing audio files...' });
                const response = await fetch('/stage1/process', { method: 'POST' });
                const data = await response.json();
                showResult('stage1-result', data);
            } catch (error) {
                showResult('stage1-result', error.message, true);
            }
        }
        
        async function runStage2() {
            try {
                showResult('stage2-result', { status: 'Analyzing dossier...' });
                const response = await fetch('/stage2/analyze', { method: 'POST' });
                const data = await response.json();
                showResult('stage2-result', data);
            } catch (error) {
                showResult('stage2-result', error.message, true);
            }
        }
        
        async function runStage3() {
            try {
                showResult('stage3-result', { status: 'Running reasoning chain...' });
                const response = await fetch('/stage3/solve', { method: 'POST' });
                const data = await response.json();
                showResult('stage3-result', data);
            } catch (error) {
                showResult('stage3-result', error.message, true);
            }
        }
        
        async function runAll() {
            showResult('all-results', { status: 'Running complete pipeline...' });
            try {
                const response = await fetch('/run-all', { method: 'POST' });
                const data = await response.json();
                showResult('all-results', data);
            } catch (error) {
                showResult('all-results', error.message, true);
            }
        }
    </script>
</body>
</html>
"""


@app.route('/')
def index():
    """Home page with web interface."""
    api_key = Config.OPENAI_API_KEY
    return render_template_string(HTML_TEMPLATE, api_key=api_key)


@app.route('/generate/audio', methods=['POST'])
def generate_audio():
    """Generate dummy audio files."""
    try:
        from stage1_audio.audio_generator import AudioGenerator
        generator = AudioGenerator()
        generator.generate_mystery_case_audio()
        return jsonify({
            "status": "success",
            "message": "Dummy audio files generated",
            "location": Config.DUMMY_AUDIO_DIR
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/generate/dossier', methods=['POST'])
def generate_dossier():
    """Generate dummy dossier."""
    try:
        from stage2_documents.dummy_dossier_generator import DossierGenerator
        generator = DossierGenerator()
        generator.generate_investigation_dossier()
        return jsonify({
            "status": "success",
            "message": "Investigation dossier generated",
            "location": Config.DUMMY_DOCUMENTS_DIR
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/generate/case', methods=['POST'])
def generate_case():
    """Generate dummy case files."""
    try:
        from stage3_reasoning.case_generator import CaseGenerator
        generator = CaseGenerator()
        generator.generate_additional_evidence()
        return jsonify({
            "status": "success",
            "message": "Case files generated",
            "location": Config.DUMMY_CASE_DIR
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/stage1/process', methods=['POST'])
def process_stage1():
    """Process audio files for Stage 1."""
    try:
        questions = [
            "Who is mentioned in this audio recording?",
            "What location is discussed?",
            "What time or date is mentioned?",
            "What suspicious activity is described?",
            "What evidence is presented?",
        ]
        
        results = audio_pipeline.process_all_audio_files(Config.DUMMY_AUDIO_DIR, questions)
        
        # Save results
        output_path = os.path.join(Config.DATA_DIR, "stage1_results.json")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        
        return jsonify({
            "status": "success",
            "stage": 1,
            "results": results
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/stage2/analyze', methods=['POST'])
def process_stage2():
    """Analyze dossier for Stage 2."""
    try:
        dossier_path = os.path.join(Config.DUMMY_DOCUMENTS_DIR, "investigation_dossier.txt")
        results = document_pipeline.analyze_dossier(dossier_path)
        
        # Save results
        output_path = os.path.join(Config.DATA_DIR, "stage2_results.json")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        
        return jsonify({
            "status": "success",
            "stage": 2,
            "results": results
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/stage3/solve', methods=['POST'])
def process_stage3():
    """Solve case for Stage 3."""
    try:
        # Load previous results
        stage1_path = os.path.join(Config.DATA_DIR, "stage1_results.json")
        stage2_path = os.path.join(Config.DATA_DIR, "stage2_results.json")
        
        if os.path.exists(stage1_path):
            with open(stage1_path, 'r') as f:
                audio_results = json.load(f)
        else:
            audio_results = []
        
        if os.path.exists(stage2_path):
            with open(stage2_path, 'r') as f:
                document_results = json.load(f)
        else:
            document_results = {}
        
        # Additional case files
        additional_files = []
        case_file = os.path.join(Config.DUMMY_CASE_DIR, "additional_evidence.txt")
        if os.path.exists(case_file):
            additional_files.append(case_file)
        
        results = reasoning_pipeline.solve_case(audio_results, document_results, additional_files)
        
        # Save results
        output_path = os.path.join(Config.DATA_DIR, "stage3_results.json")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        
        return jsonify({
            "status": "success",
            "stage": 3,
            "results": results
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/run-all', methods=['POST'])
def run_all_stages():
    """Run all stages in sequence."""
    try:
        # Generate all dummy data first
        from stage1_audio.audio_generator import AudioGenerator
        from stage2_documents.dummy_dossier_generator import DossierGenerator
        from stage3_reasoning.case_generator import CaseGenerator
        
        print("Generating dummy data...")
        AudioGenerator().generate_mystery_case_audio()
        DossierGenerator().generate_investigation_dossier()
        CaseGenerator().generate_additional_evidence()
        
        # Run Stage 1
        print("\nRunning Stage 1...")
        questions = [
            "Who is mentioned in this audio recording?",
            "What location is discussed?",
            "What time or date is mentioned?",
            "What suspicious activity is described?",
            "What evidence is presented?",
        ]
        stage1_results = audio_pipeline.process_all_audio_files(Config.DUMMY_AUDIO_DIR, questions)
        
        # Run Stage 2
        print("\nRunning Stage 2...")
        dossier_path = os.path.join(Config.DUMMY_DOCUMENTS_DIR, "investigation_dossier.txt")
        stage2_results = document_pipeline.analyze_dossier(dossier_path)
        
        # Run Stage 3
        print("\nRunning Stage 3...")
        additional_files = [os.path.join(Config.DUMMY_CASE_DIR, "additional_evidence.txt")]
        stage3_results = reasoning_pipeline.solve_case(stage1_results, stage2_results, additional_files)
        
        all_results = {
            "status": "success",
            "message": "All stages completed successfully",
            "stage1": stage1_results,
            "stage2": stage2_results,
            "stage3": stage3_results
        }
        
        # Save combined results
        output_path = os.path.join(Config.DATA_DIR, "all_results.json")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(all_results, f, indent=2)
        
        return jsonify(all_results)
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "pipelines_initialized": all([audio_pipeline, document_pipeline, reasoning_pipeline]),
        "api_key_configured": bool(Config.OPENAI_API_KEY and Config.OPENAI_API_KEY != "dummy_key_for_testing")
    })


if __name__ == '__main__':
    print("="*80)
    print("LangChain Mysteries Competition - Server Starting")
    print("="*80)
    
    # Initialize pipelines
    init_pipelines()
    
    # Validate configuration
    if Config.validate():
        print("✓ Configuration valid - API key configured")
    else:
        print("⚠ Warning: Running in demo mode without API key")
        print("  Set OPENAI_API_KEY in .env file for full functionality")
    
    print(f"\n🚀 Server running at: http://localhost:5000")
    print("   Open this URL in your browser to access the web interface\n")
    print("="*80)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
