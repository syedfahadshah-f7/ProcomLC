"""
Test Runner Script
Runs all stages sequentially to verify the complete pipeline.
"""

import os
import sys

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.utils.config import Config


def main():
    """Run complete test of all stages."""
    print("="*80)
    print("LANGCHAIN MYSTERIES - COMPLETE PIPELINE TEST")
    print("="*80)
    print()
    
    # Step 1: Generate dummy data
    print("STEP 1: Generating Dummy Data")
    print("-"*80)
    
    print("\n1.1 Generating audio files...")
    try:
        from src.stage1_audio.audio_generator import AudioGenerator
        AudioGenerator().generate_mystery_case_audio()
        print("✓ Audio files generated")
    except Exception as e:
        print(f"✗ Error generating audio: {e}")
        return False
    
    print("\n1.2 Generating investigation dossier...")
    try:
        from src.stage2_documents.dummy_dossier_generator import DossierGenerator
        DossierGenerator().generate_investigation_dossier()
        print("✓ Dossier generated")
    except Exception as e:
        print(f"✗ Error generating dossier: {e}")
        return False
    
    print("\n1.3 Generating case files...")
    try:
        from src.stage3_reasoning.case_generator import CaseGenerator
        CaseGenerator().generate_additional_evidence()
        print("✓ Case files generated")
    except Exception as e:
        print(f"✗ Error generating case files: {e}")
        return False
    
    # Step 2: Run Stage 1
    print("\n" + "="*80)
    print("STEP 2: Running Stage 1 - Audio Intelligence")
    print("-"*80)
    
    try:
        from src.stage1_audio.stage1_audio_pipeline import AudioIntelligencePipeline
        
        pipeline = AudioIntelligencePipeline()
        questions = [
            "Who is mentioned in this audio recording?",
            "What location is discussed?",
            "What time or date is mentioned?",
            "What suspicious activity is described?",
            "What evidence is presented?",
        ]
        
        results = pipeline.process_all_audio_files(Config.DUMMY_AUDIO_DIR, questions)
        print(f"\n✓ Stage 1 completed: Processed {len(results)} audio files")
        
        # Save results
        import json
        output_path = os.path.join(Config.DATA_DIR, "stage1_results.json")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        print(f"✓ Results saved to: {output_path}")
        
    except Exception as e:
        print(f"✗ Error in Stage 1: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Step 3: Run Stage 2
    print("\n" + "="*80)
    print("STEP 3: Running Stage 2 - Document Forensics")
    print("-"*80)
    
    try:
        from src.stage2_documents.stage2_document_pipeline import DocumentForensicsPipeline
        import json
        
        pipeline = DocumentForensicsPipeline()
        dossier_path = os.path.join(Config.DUMMY_DOCUMENTS_DIR, "investigation_dossier.txt")
        
        results = pipeline.analyze_dossier(dossier_path)
        print(f"\n✓ Stage 2 completed")
        print(f"  - System log access: {', '.join(results['findings']['system_log_access']) or 'None'}")
        print(f"  - Financial access: {', '.join(results['findings']['financial_access']) or 'None'}")
        print(f"  - Unauthorized experiments: {', '.join(results['findings']['unauthorized_experiments']) or 'None'}")
        
        # Save results
        output_path = os.path.join(Config.DATA_DIR, "stage2_results.json")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        print(f"✓ Results saved to: {output_path}")
        
    except Exception as e:
        print(f"✗ Error in Stage 2: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Step 4: Run Stage 3
    print("\n" + "="*80)
    print("STEP 4: Running Stage 3 - Final Case Resolution")
    print("-"*80)
    
    try:
        from src.stage3_reasoning.stage3_reasoning_pipeline import CaseReasoningPipeline
        import json
        
        # Load previous results
        with open(os.path.join(Config.DATA_DIR, "stage1_results.json"), 'r') as f:
            audio_results = json.load(f)
        
        with open(os.path.join(Config.DATA_DIR, "stage2_results.json"), 'r') as f:
            document_results = json.load(f)
        
        pipeline = CaseReasoningPipeline()
        additional_files = [os.path.join(Config.DUMMY_CASE_DIR, "additional_evidence.txt")]
        
        results = pipeline.solve_case(audio_results, document_results, additional_files)
        print(f"\n✓ Stage 3 completed")
        
        # Display final determination
        final = results['reasoning_steps']['step5_final_determination']
        print("\nFINAL DETERMINATION:")
        print("-"*80)
        print(final[:500] + "..." if len(final) > 500 else final)
        
        # Save results
        output_path = os.path.join(Config.DATA_DIR, "stage3_results.json")
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        print(f"\n✓ Results saved to: {output_path}")
        
    except Exception as e:
        print(f"✗ Error in Stage 3: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Summary
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    print("✓ All stages completed successfully!")
    print(f"\nResults saved to: {Config.DATA_DIR}")
    print("\nFiles created:")
    print("  - stage1_results.json")
    print("  - stage2_results.json")
    print("  - stage3_results.json")
    print("\nTo run the web interface:")
    print("  python app.py")
    print("\nThen open: http://localhost:5000")
    print("="*80)
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
