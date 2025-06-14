# 🧾 Bid Proposal Generator (YAML → DOCX)

This is a lightweight Python automation tool that generates professional bid/proposal letters in `.docx` format. It takes structured data from a YAML file and fills a Word template with that information using placeholder rendering.

This is my **first ever project on GitHub** 🚀 — built to automate tender documentation tasks!

---

## 🔧 What It Does

- Reads data from a YAML file (like tender name, bidder name, to-do list)
- Determines what kind of document needs to be generated
- Builds a professional proposal letter body
- Fills a Word `.docx` template with the content
- Outputs the final document to a specified folder

---

## 🗂 Folder Structure

```
bid-proposal-generator/
├── main.py               # Entry point – calls all other modules
├── ai_writer.py          # Generates the main letter body from YAML data
├── doc_writer.py         # Renders a .docx using docxtpl
├── yaml_utils.py         # Loads YAML data
├── input/                # YAML instruction files
│   └── instructions.yaml
├── templates/            # Word template files with {{placeholders}}
│   └── sample_template.docx
├── output/               # Final generated .docx documents
├── requirements.txt
└── README.md
```

---

## ▶ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/bid-proposal-generator.git cd bid-proposal-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your input YAML in `input/instructions.yaml`  
   Example:
   ```yaml
   to_do:
     - bid submission letter
   tender_name: "Smart School Labs RFP"
   tendering_authority: "Department of Education"
   bidder_name: "KompanionsX"
   ```

4. Run the program:
   ```bash
   python main.py
   ```

5. Output document appears in the `output/` folder.


## 💬 Connect
**Prasshant Rana** 
Feel free to connect on [LinkedIn]https://www.linkedin.com/in/prasshant-rana-30b5881a7/ or contribute ideas to improve it!
 
