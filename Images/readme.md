Here's the rephrased version ready to paste into your README:

---

## 🖼️ Visual Documentation & Diagrams

---

### 1. 🤖⚡ AI-Powered EDA Tool — End-to-End Workflow

#### 📋 Description
This diagram walks through the **complete operational journey** of the AI-Powered EDA Tool — from the moment you fire up the terminal all the way to interactive waveform visualization.

#### ✨ Key Highlights
- 🖥️ Launch terminal & spin up the **Ollama LLM server**
- 🐍 Start the **Flask/Python backend** application
- 🔒 Access the **secure local HTTPS** web interface
- 📤 Upload your **Verilog RTL code**
- ⚙️ Execute the **automated EDA pipeline**
- 📊 Auto-generate rich outputs:
  - 🔌 Circuit Diagrams
  - 🔄 FSM Diagrams
  - 📋 Truth Tables
  - 🧠 AI Analysis Summary
  - 📈 PPA Estimates
  - 🌊 Waveform Outputs

#### 🎯 Purpose
> Gives users a **crystal-clear, end-to-end picture** of how the tool behaves during real-time execution.

---

### 2. 🗂️ AI\_EDA\_TOOL — Project Folder Structure

#### 📋 Description
A complete map of the **organized directory hierarchy** powering the AI\_EDA\_TOOL project.

#### ✨ Key Highlights

| Layer | Contents |
|---|---|
| 🌐 **Frontend Layer** | Flask App · HTML Templates |
| ⚙️ **Backend Modules** | Verilog Parser · Simulation Engine · PPA Analyzer · Truth Table Generator |
| 🧠 **AI Engine** | Ollama LLM integration |
| 🎨 **Static Assets** | Circuit Images · FSM Images · CSS Styling |
| 📦 **Runtime Data** | Reports · Waveforms · Logs · Generated Netlists |

#### 🎯 Purpose
> Helps developers instantly grasp the **modular architecture** and **maintainability structure** of the project.

---

### 3. 🏗️ AI / VLSI / System Architecture Models

---

#### 3.1 🧠 AI Model Architecture

##### 📋 Description
Represents the **LLM-driven Verilog understanding pipeline** at the core of AI analysis.

##### 🔁 Flow
```
📄 Verilog Input
   ↓
🔧 Preprocessing
   ↓
🔍 Parsing via PyVerilog
   ↓
🕸️ RTL Graph Construction
   ↓
🤖 Ollama LLM Analysis
   ↓
📦 Structured JSON Generation
   ↓
📊 Visualization Output
```

---

#### 3.2 🔬 VLSI / EDA Flow Model

##### 📋 Description
Depicts the **traditional RTL-to-Visualization EDA transformation pipeline** integrated into the platform.

##### 🔁 Flow
```
📄 Verilog RTL Input
   ↓
🔍 Parsing & Elaboration
   ↓
🔨 RTL Synthesis (Yosys)
   ↓
🔗 Gate-Level Netlist Generation
   ↓
📐 Circuit Graph Conversion
   ↓
🖼️ Visualization
   ↓
⏱️ Future Timing/STA Integration
```

---

#### 3.3 🖥️ System Architecture

##### 📋 Description
The **high-level software architecture** of the AI-EDA Tool at a glance.

##### 🧩 Components

| 🌐 Frontend Web UI | ⚙️ Backend Python Server | 💾 Storage | 🔧 External Tools |
|---|---|---|---|
| Upload Interface | REST API / FastAPI | JSON Repository | Yosys |
| Circuit Viewer | Parser Engine | Netlist Repository | Graphviz |
| FSM Viewer | AI Engine (Ollama LLM) | Logs & Reports | Icarus Verilog |
| Waveform Viewer | Synthesis Engine (Yosys) | | GTKWave |

##### 🎯 Purpose
> Delivers a **complete overview** of the internal software + EDA integration architecture.

---

### 🚀 Summary

These visual representations collectively capture:

| Visual | What It Shows |
|---|---|
| 🔄 **Operational Workflow** | How users interact with the tool step-by-step |
| 📁 **Folder Architecture** | How the project is structured internally |
| 🏗️ **Technical Architecture** | How AI, VLSI, and software components integrate seamlessly |
