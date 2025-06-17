# Introduction

This project is divided into **two parts**:
1. **Extraction Layer** – Parsing, structuring, and labeling unstructured tender PDFs  
2. **Letter Generation Layer** – Using structured data to auto-generate formal proposal letters

1. # AI Tender Extraction & Structuring - Learning Journey

A step-by-step evolution of building an intelligent pipeline to process, extract, structure, and semantically label tender documents (PDFs of all kinds – scanned, typed, mixed).

---

2. # Initial Setup
- ✅ Installed required tools: `pdfplumber`, `PyMuPDF`, `pytesseract`, `pdf2image`
- ❌ Faced pip/path issues → Fixed by updating pip, adding Python & Tesseract to system PATH
- ✅ Manually set `pytesseract.pytesseract.tesseract_cmd` to avoid detection issues

---

3. # Base Extraction Logic
- ✅ Developed hybrid approach:
  - `fitz` → primary for layout and clean text
  - fallback to `pdfplumber` for tables
  - fallback to OCR (`pytesseract`) when no text present
- ✅ Found image-only PDFs failing → root cause: no extractable text layer

---

4. # Hybrid Logic Implementation
- ✅ Built per-page extractor routing:
  - If `.get_text()` fails → try pdfplumber
  - If still fails or blank → use OCR
- ✅ Dynamic fallback ensures best extractor per page
- ✅ Added debug logging for extractor choice

---

5. # Chunking & Text Structuring
- ✅ Used sentence + paragraph-based chunking for semantic grouping
- ✅ Initial chunks had no labels → hard to find “Eligibility” or “Submission Docs”
- ✅ Exported all chunks to `compiled_chunks.txt` for analysis

---

6. # Instructor Embedding Layer
- ✅ Used `Instructor-XL` model for embedding
- ✅ Applied cosine similarity to match questions (like “What is eligibility?”)
- ✅ Chunking quality directly affected embedding output
- ✅ Fixed by improving semantic chunking (paragraph-level)

---

7. # Pre-labeling Strategy Shift
- ✅ Idea: Why not label chunks first before chunking?
- ✅ Found redundant to split and relabel again
- ✅ Plan: do structuring and labeling in a single LLM pass
- ✅ Discovered [`unstructured`](https://github.com/Unstructured-IO/unstructured) library

---

8. # Experiments with `unstructured` Library
- ✅ Installed and tested `partition_text()`, `partition_pdf()`
- ❌ Errors on accessing `.category` → fixed with `.category_name` or fallback check
- ❌ File path bugs → fixed by verifying path and extension
- ✅ Clearer metadata tags helped organize document blocks

---

9. # Detecting Scanned vs Text Pages
- ✅ Learned: Some pages are text-based, some images, some both
- ✅ Used `page.get_images()` from `fitz` to detect images
- ✅ Logic: “If no text + has image → OCR that page”
- ✅ Now dynamically detect and route extractor per page

---

10. # Key Realizations
- ❌ Some sections (like tables) are embedded as images even in digital PDFs
- ✅ Decided to process **per block** (text, image, table) not just per page
- ✅ Better to post-process and restructure text before semantic chunking
- ✅ AI labeling works best on cleaned, structured paragraphs

---

11. # Future Plan Ideas
- ✅ Label each paragraph using open-source LLM → output YAML/JSON with `type`, `content`
- ✅ Use OCR layout + font size signals to detect headings and sub-sections
- ✅ Combine extraction + structuring + AI labeling in one end-to-end step

---

# Modular Component Summary

## 1. Data Extraction Layer
| Tool         | Strength                                  | Weakness                                  |
|--------------|-------------------------------------------|--------------------------------------------|
| pdfplumber   | ✅ Table extraction                        | ❌ Fails on image-based tables              |
| pdfminer     | ✅ Identifies layout elements              | ❌ Weak with images, OCR not supported      |
| PyMuPDF      | ✅ Accurate block parsing + layout info    | ✅ Detects image blocks                     |
| pytesseract  | ✅ Works on scanned docs                   | ❌ Hindi OCR noisy, removed via regex       |

---

## 2. Semantic Understanding Layer
-  `Instructor-XL`: used for instruction-tuned embeddings
-  Chunking Logic:
  - ✅ Sentence + paragraph-based best
  - ❌ Random/page-based chunking reduced semantic precision

---

## 3. Post-Processing Layer
- ✅ Combined text + OCR + table content
- ✅ Tagged outputs like `[HEADING]`, `[TABLE]`, `[BODY]`, `[IMAGE]`
- ❌ Merging layout-wise still not perfect (to be improved)

---

## 4. Errors & Fixes
| Error                             | Fix                                                   |
|----------------------------------|--------------------------------------------------------|
| PyMuPDF not found                | `pip install pymupdf`                                 |
| fitz confusion                   | Clarified fitz is part of pymupdf                     |
| CropBox warning in PyMuPDF       | Switched to MediaBox or ignored safely                |
| Codebase conflicts during merge  | Reset to stable branch with working full flow         |

---

## 5. What Worked Best
-  Hybrid Extraction:
  - PyMuPDF for layout
  - pdfplumber for tables
  - pytesseract for fallback OCR
- AI Labeling:
  - INSTRUCTOR-XL + cosine for matching
  - Paragraph-level granularity best
- Output:
  - Per-page structured text
  - Tagged elements for easy downstream parsing
  - Searchable and clean

---

#  Tools & Techniques Learned

| Category              | Tools/Concepts Learned                                |
|-----------------------|--------------------------------------------------------|
| PDF Processing        | pdfplumber, PyMuPDF, pdfminer, pdf2image              |
| OCR & Image Handling  | pytesseract, Tesseract path setup, Hindi cleanup      |
| Semantic AI           | Instructor-XL, sentence-transformers, cosine similarity|
| Document Structuring  | unstructured library, chunking logic                  |
| Programming Skills    | Modular script design, fallback logic, exception handling |
| Future Concepts       | AI paragraph labeling, YAML outputs, block-wise routing|

---
 It is still not complete...
 # I paused on this and started working on generation part... 

