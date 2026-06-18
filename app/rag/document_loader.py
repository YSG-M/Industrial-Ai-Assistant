import pymupdf
from pathlib import Path


def get_pdf_pages_text(file_path: str) -> list:
    
    with pymupdf.open(file_path) as doc:
        file_name = Path(file_path).name
        pages_text = []

        page = 1

        for pdf_page in doc:        
            text = pdf_page.get_text()

            content_type = "text"

            if is_empty_page(text):
                content_type = "empty"

            content = {
                "source": file_name,
                "page": page,
                "text": text,
                "content_type": content_type
            }
            
            pages_text.append(content)
            page += 1
    
    return pages_text

def is_empty_page(page_content: str) -> bool:

    return not page_content.strip()


BASE_DIR = Path(__file__).resolve().parents[2]

pdf_path = (
    BASE_DIR
    / "data"
    / "manuals"
    / "The_Linux_Users_Guide.pdf"
)

pdf_array = get_pdf_pages_text(str(pdf_path))