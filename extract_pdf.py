import PyPDF2
import sys

def extract_pdf_text(pdf_path, output_path):
    """Extract text from PDF and save to a text file."""
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            text = ""
            total_pages = len(pdf_reader.pages)
            
            print(f"Extracting text from {total_pages} pages...")
            
            for page_num in range(total_pages):
                page = pdf_reader.pages[page_num]
                text += f"\n\n--- Page {page_num + 1} ---\n\n"
                text += page.extract_text()
            
            # Save to text file
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(text)
            
            print(f"Successfully extracted text to {output_path}")
            return True
            
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return False

if __name__ == "__main__":
    pdf_path = "PROCOM_26__ Langchain_Mystries_Rulebook_compressed.pdf"
    output_path = "rulebook_extracted.txt"
    extract_pdf_text(pdf_path, output_path)
