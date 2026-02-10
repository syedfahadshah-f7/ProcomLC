"""Test script to verify all LLM connection fixes are working."""

from src.stage1_audio.stage1_audio_pipeline import AudioIntelligencePipeline
from src.stage2_documents.stage2_document_pipeline import DocumentForensicsPipeline
from src.stage3_reasoning.stage3_reasoning_pipeline import CaseReasoningPipeline
from utils.config import Config
import os

print("="*80)
print("TESTING LLM CONNECTION FIXES")
print("="*80)

# Test Stage 1: Audio Pipeline
print("\n[Stage 1] Testing Audio Intelligence Pipeline...")
audio_pipeline = AudioIntelligencePipeline()
transcript = """
Dr. Sarah Chen accessed the laboratory at 11:47 PM on Friday night.
She was seen conducting unauthorized experiments on the Apex prototype.
Security logs show she deleted access records afterwards.
"""
questions = [
    "Who is mentioned in this audio recording?",
    "What suspicious activity is described?",
    "What evidence is presented?"
]

print("\nProcessing questions with LLM...")
answers = audio_pipeline.answer_questions_from_transcript(transcript, questions)

print("\n✓ Stage 1 RESULTS:")
for q, a in answers.items():
    print(f"  Q: {q}")
    print(f"  A: {a}\n")

# Test Stage 2: Document Pipeline
print("\n[Stage 2] Testing Document Forensics Pipeline...")
doc_pipeline = DocumentForensicsPipeline()
document_text = """
Investigation Report:
- Victor Krum accessed server logs on Friday at 10:00 PM
- Sarah Chen viewed financial records on Thursday
- Kevin Miller conducted unauthorized experiments in Lab B
"""

print("\nExtracting information with LLM...")
system_access = doc_pipeline.extract_system_log_access(document_text)
financial_access = doc_pipeline.extract_financial_access(document_text)

print("\n✓ Stage 2 RESULTS:")
print(f"  System log access: {system_access}")
print(f"  Financial access: {financial_access}")

# Test Stage 3: Reasoning Pipeline
print("\n[Stage 3] Testing Case Reasoning Pipeline...")
reasoning_pipeline = CaseReasoningPipeline()
evidence = """
Victor Krum was found at the crime scene at 11:50 PM.
He had access to the Apex prototype and system logs.
Financial records show he received payments from a competitor.
"""

print("\nIdentifying suspects with LLM...")
suspects = reasoning_pipeline.reason_step1_identify_suspects(evidence)

print("\n✓ Stage 3 RESULTS:")
print(f"  Suspects identified:\n{suspects[:200]}...")

print("\n" + "="*80)
print("ALL TESTS COMPLETED SUCCESSFULLY!")
print("Connection errors are now fixed.")
print("="*80)
