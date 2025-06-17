#  AI Tender Proposal Generator – Learning Journey

This document tracks the development of an AI-powered system to auto-generate tender proposal letters using structured YAML inputs, a local LLM (Mistral), and DOCX templates.

---

## 1️⃣ Project Goal: From Manual to Automated Proposals

-  **Objective**: Auto-generate `.docx` proposal letters using structured YAML + AI-generated content.
-  **Deliverable**: Professionally styled `.docx` file with:
  - Pre-filled fields from YAML
  - AI-written main body
  - Proper formatting and alignment

---

## 2️⃣ Input Format Experiments

### ✅ What Worked
- Used `.yaml` to define structure (bidder, tender, to_do_task)
- YAML parsed easily using `pyyaml.safe_load()`

### ❌ What Didn’t Work
- `.txt` instruction format was ambiguous and fragile
- Flattening YAML caused placeholder mismatches

### 🔁 Fixes
- Reverted to nested YAML
- Used dot-notation in templates: `{{ tender.bid_tender_no }}`

---

## 3️⃣ Template Strategy (docx)

### ✅ What Worked
- Used Word `.docx` template with placeholders
- Rendered using `docxtpl` for basic fields

### ❌ What Didn’t Work
- `{{ content }}` got split into runs — not detected
- Direct `para.text` replacement removed all formatting

### 🔁 Fixes
- Created `[( content )]` as special placeholder
- Injected AI-generated body post-render using `python-docx`

---

## 4️⃣ AI Generation: Mistral via ctransformers

### ✅ What Worked
- Used `ctransformers` to load `Mistral-7B-Instruct.Q4_K_M.gguf`
- Built concise prompts using selected YAML fields
- Generated high-quality letter body

### ❌ What Didn’t Work
- Token limit (512) caused cutoff in long responses
- Model sometimes added syntax errors (e.g., invalid Python list)

### 🔁 Fixes
- Added prompt length control
- Used regex instead of `eval()` to parse model outputs
- Prompted model to "end with a concluding sentence"

---

## 5️⃣ Placeholder Handling

### ✅ What Worked
- Replaced most placeholders via `docxtpl.render()`
- For `[( content )]`, used `python-docx` to find and replace paragraph
- Used `run.add_break()` for line breaks in AI content

### ❌ What Didn’t Work
- Word’s visual text ≠ actual placeholder structure
- Placeholder split into multiple `<w:r>` went undetected

### 🔁 Fixes
- Retyped broken placeholders in Word manually
- Verified with `repr(para.text)` to debug structure

---

## 6️⃣ Output Generation

### ✅ What Worked
- `.docx` file saved to output folder with proper content
- Used `.tmp.docx` to stage rendering before injecting content
- Added timestamp/versioning logic (planned)

### ❌ What Didn’t Work
- FileNotFoundError due to missing output folder
- PermissionError when saving over open file

### 🔁 Fixes
- Used `os.makedirs()` to ensure folder exists
- Added `.save()` safely with exception handling

---

## 7️⃣ Modularization & Code Organization

### ✅ What Worked
- Separated logic into utils:
  - `yaml_loader.py`
  - `ai_writer.py`
  - `doc_writer.py`
  - `model_loader.py`
- Final `main.py` orchestrates the flow

### ❌ What Didn’t Work
- Initially crammed all logic into one script
- Import issues across modules

### 🔁 Fixes
- Used `if __name__ == "__main__":` for testing
- Added `sys.path.append()` to resolve module imports

---

## 8️⃣ Testing & Debugging

### ✅ What Worked
- Used dummy YAML files for testing
- Print logs and debug checkpoints at each step
- Printed model prompt, selected keys, and generated body

### ❌ What Didn’t Work
- Model output disappeared due to wrong file path
- Errors went unnoticed without logging

### 🔁 Fixes
- Verified save paths
- Added try/except and print debugging

---

## 9️⃣ Advanced Experiments

### ✅ What Worked
- Added table from YAML using `python-docx`
- Preserved text formatting: bold, italics, alignment
- Aligned content using `WD_ALIGN_PARAGRAPH.JUSTIFY`

### ❌ What Didn’t Work
- Bullet lists and numbering not preserved
- Markdown → Word conversion still pending

---

## 🔚 Final Working Flow

1.  Read YAML data  
2.  Use Mistral LLM (via `ctransformers`) to generate letter body  
3.  Inject AI content into YAML as `content`  
4.  Use `docxtpl` to fill standard placeholders  
5.  Use `python-docx` to replace `[( content )]` with rich text  
6.  Save final `.docx` to output folder  

---

##  Tools & Technologies Learned

| Category       | Tools / Libraries                         |
|----------------|-------------------------------------------|
| YAML Handling  | `pyyaml`                                  |
| AI Model       | `Mistral-7B-Instruct.Q4_K_M.gguf` via `ctransformers` |
| Word Editing   | `docxtpl`, `python-docx`                  |
| OCR Extraction | `pytesseract`, `pdfplumber`, `PyMuPDF`    |
| Code Structure | `os`, `sys`, `re`, `logging`, `ast`       |
| Prompt Design  | Dynamic prompt building + key selection AI |
| Debugging      | `try/except`, `print`, file path checks   |

---

