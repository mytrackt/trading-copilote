import sys, os, json
import pdfplumber
from pypdf import PdfReader

OUT = r"C:\trading-copilote\_temp_extraction\PDF_OCR"

def clean(t):
    return (t or "").strip()

def extract(path):
    name = os.path.splitext(os.path.basename(path))[0]
    result = {"file": os.path.basename(path), "method": None, "pages": 0, "chars": 0}
    text = ""
    # pdfplumber
    try:
        with pdfplumber.open(path) as pdf:
            result["pages"] = len(pdf.pages)
            parts = []
            for p in pdf.pages:
                parts.append(clean(p.extract_text()))
            text = "\n\n".join([x for x in parts if x])
    except Exception as e:
        result["plumber_error"] = str(e)
    if len(text.strip()) > 200:
        result["method"] = "pdfplumber"
    else:
        # fallback pypdf
        try:
            r = PdfReader(path)
            result["pages"] = len(r.pages)
            parts = [clean(pg.extract_text()) for pg in r.pages]
            t2 = "\n\n".join([x for x in parts if x])
            if len(t2.strip()) > len(text.strip()):
                text = t2
            if len(text.strip()) > 200:
                result["method"] = "pypdf"
        except Exception as e:
            result["pypdf_error"] = str(e)
    if not result["method"]:
        result["method"] = "FAILED_LEVEL1"
    result["chars"] = len(text.strip())
    with open(os.path.join(OUT, name + ".txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return result

if __name__ == "__main__":
    res = extract(sys.argv[1])
    print(json.dumps(res, ensure_ascii=False))
