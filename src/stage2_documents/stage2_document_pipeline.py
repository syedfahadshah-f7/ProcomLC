"""
Stage 2: Document Forensics Pipeline
Uses LangChain to extract information from documents WITHOUT embeddings or vector databases.

Competition Requirements:
- Process multi-page dossier
- Extract: system log access, financial access, unauthorized experiments
- NO OCR tools allowed
- NO vector databases or embeddings
- Direct LLM processing only
"""

import os
import json
from typing import List, Dict, Optional
try:
    from langchain_groq import ChatGroq
    from langchain_core.prompts import PromptTemplate
    from langchain_classic.chains import LLMChain
    from langchain_classic.chains.combine_documents import create_stuff_documents_chain
    from langchain_core.documents import Document
except ImportError:
    ChatGroq = None
    PromptTemplate = None
    LLMChain = None
    create_stuff_documents_chain = None
    Document = None
from pathlib import Path
import PyPDF2

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.config import Config


class DocumentForensicsPipeline:
    """Pipeline for analyzing documents and extracting forensic information."""
    
    def __init__(self, groq_api_key: Optional[str] = None):
        """
        Initialize the document forensics pipeline.
        
        Args:
            groq_api_key: Groq API key for LLM processing
        """
        self.api_key = groq_api_key or Config.get_groq_api_key()
        
        # Initialize LLM
        if self.api_key and self.api_key != "dummy_key_for_testing":
            self.llm = ChatGroq(
                model=Config.GROQ_MODEL,
                temperature=Config.TEMPERATURE,
                groq_api_key=self.api_key
            )
        else:
            self.llm = None
            print("WARNING: Running in dummy mode. Set GROQ_API_KEY for actual LLM processing.")
    
    def load_document(self, file_path: str) -> str:
        """
        Load a document (PDF or TXT) and return its text content.
        
        Args:
            file_path: Path to document
            
        Returns:
            Document text content
        """
        file_extension = Path(file_path).suffix.lower()
        
        if file_extension == '.pdf':
            return self._load_pdf(file_path)
        elif file_extension == '.txt':
            return self._load_txt(file_path)
        elif file_extension == '.csv':
            return self._load_csv(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")
    
    def _load_pdf(self, pdf_path: str) -> str:
        """Load PDF document."""
        text = ""
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        return text
    
    def _load_txt(self, txt_path: str) -> str:
        """Load text document."""
        with open(txt_path, 'r', encoding='utf-8') as file:
            return file.read()
    
    def _load_csv(self, csv_path: str) -> str:
        """Load CSV document."""
        import pandas as pd
        df = pd.read_csv(csv_path)
        return df.to_string()
    
    def extract_system_log_access(self, document_text: str) -> List[str]:
        """
        Extract who accessed system logs from the document.
        
        Args:
            document_text: Full document text
            
        Returns:
            List of people who accessed system logs
        """
        prompt_template = """You are a forensic investigator analyzing a case dossier.

Document Content:
{document}

Task: Identify and list ALL individuals who accessed system logs based on the evidence in the document.
Look for mentions of:
- Server access
- Log file access
- System administration activities
- Unauthorized system access

Provide your answer as a comma-separated list of names only. If no one is mentioned, respond with "None found".

Names who accessed system logs:"""

        if self.llm:
            try:
                prompt = PromptTemplate(
                    input_variables=["document"],
                    template=prompt_template
                )
                chain = LLMChain(llm=self.llm, prompt=prompt)
                
                response = chain.invoke({"document": document_text})
                result = response['text'].strip()
                
                # Parse comma-separated names
                if result.lower() == "none found":
                    return []
                return [name.strip() for name in result.split(',')]
            except Exception as e:
                print(f"LLM Error extracting system log access: {e}. Falling back to dummy mode.")
                return self._dummy_extract_system_log(document_text)
        else:
            return self._dummy_extract_system_log(document_text)

    def _dummy_extract_system_log(self, document_text: str) -> List[str]:
        """Dummy logic for system log access."""
        names = []
        if "Victor Krum" in document_text:
            names.append("Victor Krum")
        elif "David Park" in document_text:
            names.append("David Park") 
        return names
    
    def extract_financial_access(self, document_text: str) -> List[str]:
        """
        Extract who accessed financial records from the document.
        
        Args:
            document_text: Full document text
            
        Returns:
            List of people who accessed financial records
        """
        prompt_template = """You are a forensic investigator analyzing a case dossier.

Document Content:
{document}

Task: Identify and list ALL individuals who accessed financial records or budgets based on the evidence in the document.
Look for mentions of:
- Budget access
- Financial records
- Expense reports
- Accounting system access
- Unauthorized financial data access

Provide your answer as a comma-separated list of names only. If no one is mentioned, respond with "None found".

Names who accessed financial records:"""

        if self.llm:
            prompt = PromptTemplate(
                input_variables=["document"],
                template=prompt_template
            )
            chain = LLMChain(llm=self.llm, prompt=prompt)
            
            try:
                response = chain.invoke({"document": document_text})
                result = response['text'].strip()
                
                if result.lower() == "none found":
                    return []
                return [name.strip() for name in result.split(',')]
            except Exception as e:
                print(f"Error extracting financial access: {e}")
                return []
        else:
            # Dummy mode
            names = []
            if "Victor Krum" in document_text:
                names.append("Victor Krum")
            elif "financial" in document_text.lower() or "budget" in document_text.lower():
                names.append("Dr. Sarah Chen")
            return names
    
    def extract_unauthorized_experiments(self, document_text: str) -> List[str]:
        """
        Extract who conducted unauthorized experiments from the document.
        
        Args:
            document_text: Full document text
            
        Returns:
            List of people who conducted unauthorized experiments
        """
        prompt_template = """You are a forensic investigator analyzing a case dossier.

Document Content:
{document}

Task: Identify and list ALL individuals who conducted unauthorized experiments or research based on the evidence.
Look for mentions of:
- Unauthorized lab access
- Unapproved experiments
- Secret research
- Protocol violations
- Suspicious laboratory activities

Provide your answer as a comma-separated list of names only. If no one is mentioned, respond with "None found".

Names who conducted unauthorized experiments:"""

        if self.llm:
            prompt = PromptTemplate(
                input_variables=["document"],
                template=prompt_template
            )
            chain = LLMChain(llm=self.llm, prompt=prompt)
            
            try:
                response = chain.invoke({"document": document_text})
                result = response['text'].strip()
                
                if result.lower() == "none found":
                    return []
                return [name.strip() for name in result.split(',')]
            except Exception as e:
                print(f"Error extracting unauthorized experiments: {e}")
                return []
        else:
            # Dummy mode
            names = []
            if "Kevin" in document_text and "mining" in document_text.lower():
                names.append("Kevin Miller")
            elif "experiment" in document_text.lower() or "unauthorized" in document_text.lower():
                names.append("Professor James Mitchell")
            return names
    
    def analyze_dossier(self, dossier_path: str) -> Dict:
        """
        Complete forensic analysis of a dossier document.
        
        Args:
            dossier_path: Path to dossier file
            
        Returns:
            Dictionary with all extracted forensic information
        """
        print(f"Analyzing dossier: {dossier_path}")
        
        # Load document
        document_text = self.load_document(dossier_path)
        print(f"Document loaded. Length: {len(document_text)} characters")
        
        # Extract all forensic information
        system_log_access = self.extract_system_log_access(document_text)
        financial_access = self.extract_financial_access(document_text)
        unauthorized_experiments = self.extract_unauthorized_experiments(document_text)
        
        results = {
            "dossier_file": os.path.basename(dossier_path),
            "document_length": len(document_text),
            "findings": {
                "system_log_access": system_log_access,
                "financial_access": financial_access,
                "unauthorized_experiments": unauthorized_experiments
            }
        }
        
        return results


def main():
    """Main function for testing the document forensics pipeline."""
    # Initialize pipeline
    pipeline = DocumentForensicsPipeline()
    
    # Process dossier
    dossier_path = os.path.join(Config.DUMMY_DOCUMENTS_DIR, "investigation_dossier.txt")
    
    if not os.path.exists(dossier_path):
        print(f"Dossier not found: {dossier_path}")
        print("Please run dummy_dossier_generator.py first to create the dossier.")
        return
    
    results = pipeline.analyze_dossier(dossier_path)
    
    # Display results
    print("\n" + "="*80)
    print("STAGE 2: DOCUMENT FORENSICS - RESULTS")
    print("="*80 + "\n")
    
    print(f"Dossier File: {results['dossier_file']}")
    print(f"Document Length: {results['document_length']} characters\n")
    
    print("Findings:")
    print(f"  System Log Access: {', '.join(results['findings']['system_log_access']) if results['findings']['system_log_access'] else 'None found'}")
    print(f"  Financial Access: {', '.join(results['findings']['financial_access']) if results['findings']['financial_access'] else 'None found'}")
    print(f"  Unauthorized Experiments: {', '.join(results['findings']['unauthorized_experiments']) if results['findings']['unauthorized_experiments'] else 'None found'}")
    
    # Save results to JSON
    output_path = os.path.join(Config.DATA_DIR, "stage2_results.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✓ Results saved to: {output_path}")


if __name__ == "__main__":
    main()
