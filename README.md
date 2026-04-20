# ⚡ AI-Driven EDA Tool for RTL Analysis & Verification

An AI-powered Electronic Design Automation (EDA) assistant that automates Verilog analysis, debugging, and simulation using a **local LLM (Ollama)** with a **Flash-based backend pipeline**.

---

## 🚀 Overview

This project aims to bridge the gap between **AI-based code understanding** and **hardware verification workflows**.

Unlike traditional AI code assistants, this tool integrates:

- 🧠 AI-based RTL analysis  
- 🔁 Simulation feedback loop  
- 🖥️ Local execution (offline-capable)  

---

## 🧩 Architecture
Streamlit UI (Upload & Display)
↓
Flash Local Server (Pipeline Control)
↓
Ollama (LLM for AI Analysis) + ModelSim (Simulation Engine)
↓
Results returned to UI (Logs / Outputs / Debug Info)


---

## ⚙️ Tech Stack

- **Python** – Backend orchestration  
- **Verilog** – Input design language  
- **Ollama (LLM)** – AI-based code analysis  
- **Streamlit** – Frontend UI  
- **ModelSim** – Simulation engine  
- **Flash Pipeline** – Local server execution  

---

## 🔄 Workflow

1. Upload Verilog (`.v`) file via UI  
2. Preprocess and extract module information  
3. Send structured prompt to LLM (Ollama)  
4. Perform:
   - Syntax error detection  
   - Logical issue identification  
   - Code correction suggestions  
5. Trigger simulation using ModelSim  
6. Collect logs and outputs  
7. Display results in UI  

---

## ✨ Features (Current)

- ✅ Verilog file upload via UI  
- ✅ AI-based code analysis (Ollama)  
- ✅ Syntax and logical error detection  
- ✅ Code correction suggestions  
- ✅ Top module identification (basic)  
- ✅ ModelSim simulation integration (partial)  
- ✅ Log output display  

---

## 🚧 Work in Progress

- 🔄 Stable simulation execution pipeline  
- 🔄 Waveform visualization integration  
- 🔄 Circuit diagram generation  
- 🔄 Multi-module support  
- 🔄 Testbench auto-generation  
- 🔄 Improved prompt engineering for accuracy  

---

## ⚠️ Known Limitations

- AI-generated fixes may not always be synthesizable  
- Simulation flow may fail for complex or multi-file designs  
- Limited handling of large RTL projects  
- Error parsing from ModelSim needs refinement  

---

## 💡 Key Idea

This tool implements an **AI + Simulation feedback loop**, where generated fixes are validated using a simulator and iteratively improved.

This approach aligns with emerging **AI-driven EDA workflows**.

---

## 🧠 Future Scope

- Automated testbench generation  
- Integration with open-source tools (Yosys, GTKWave)  
- Full RTL to GDSII flow exploration  
- Performance benchmarking and metrics  

---

## 👨‍💻 Author

**V N S S S R Maheedhar Bhamidipati**  
VLSI Design | FPGA | AI for Hardware  

---
