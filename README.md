# Bid Proposal Generator 
This is a lightweight Python automation tool that generates professional bid/proposal letters in `.docx` format. It takes structured data from a YAML file and fills a Word template with that information using placeholder rendering.

This is my **first ever project on GitHub** — built to automate tender documentation tasks!

---

## What It Does

1. Loads structured YAML input
      Reads key information like:
         Task to perform (to_do_task)
         Tender details (tender.name, tender.bid_tender_no, etc.)
         Bidder profile and team (bidder.name, bidder.key_personnel.name, etc.)

2. Flattens nested YAML keys
      Nested keys like bidder.key_personnel.name are flattened into dot notation for easy access during selection.

3. Selects relevant fields using AI (Mistral model)
      The prompt_builder.py constructs a prompt asking the AI model (Using ctransformers) to pick only the YAML fields needed for the task (e.g. “Write a bid submission letter”).

4. Generates the letter body using AI (Mistral model)
      Using ctransformers, a prompt is sent to the Mistral model with the filtered YAML data. The model generates a clean, formal paragraph for the main body.

5. Fills a Word .docx template
      The generated letter body and other fields (like date, tender name, etc.) are inserted into a Word document using docxtpl and {{placeholder}} tags.

6. Exports the final document
      The completed proposal letter is saved to the /output/ directory, ready to send or upload.
---

## Folder Structure

```
bid-proposal-generator/
├── main.py
├── README.md
├── requirements.txt
│
├── input/
│   └── data_file.yaml
│
├── output/
│   └── output.docx
│
├── templates/
│   └── sample_format.docx
│
├── utils/
   ├── ai_writer.py
   ├── data_utils.py
   ├── doc_writer.py
   ├── model_loader.py
   ├── prompt_builder.py
   └── yaml_loader.py

```

---

## How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/bid-proposal-generator.git
   cd bid-proposal-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your input YAML in `input/data_file.yaml`  
   Example:
   ```yaml
   to_do:
     - bid submission letter
   tender_name: "Smart School Labs RFP"
   tendering_authority: "Department of Education"
   bidder_name: "KompanionsX"
   ```
4. Open utils/prompt_builder.py to edit how the AI is instructed:
   build_key_selection_prompt() — Adjust which YAML fields are considered important for the task.
   build_letter_body_prompt() — Change tone, formatting, or structure of the letter.

5. Run the program:
   ```bash
   python main.py
   ```

## Connect
**Prasshant Rana** 
Feel free to connect on https://www.linkedin.com/in/prasshant-rana-30b5881a7/ or contribute ideas to improve it!
 
