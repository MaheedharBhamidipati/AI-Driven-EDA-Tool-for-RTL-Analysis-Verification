import os
import shutil
import sys

# Fix encoding (Windows)
sys.stdout.reconfigure(encoding='utf-8')

# =========================================================
# 🧹 CLEAN CACHE
# =========================================================
def delete_pycache(root_dir="."):
    for root, dirs, files in os.walk(root_dir):
        for d in dirs:
            if d == "__pycache__":
                shutil.rmtree(os.path.join(root, d))

delete_pycache()

# =========================================================
# ⚙️ ENV SETUP
# =========================================================
os.environ["PYTHONIOENCODING"] = "utf-8"
sys.path.append("D:/AI_EDA_TOOL")

from flask import Flask, render_template, request

# =========================================================
# 🔌 IMPORT BACKEND MODULES
# =========================================================
from backend.utils.cleaner import clear_runs
from backend.ai.ai_engine import analyze_verilog
from backend.parser.verilog_parser import find_top_module, extract_ports
from backend.simulation.tb_generator import generate_testbench
from backend.simulation.simulator import run_simulation
from backend.parser.diagram import generate_circuit_diagram
from backend.truth.truth_table import generate_truth_table
from backend.ppa.ppa_analyzer import run_yosys, extract_ppa
from backend.parser.fsm_generator import generate_fsm_diagram
from backend.parser.netlist_visualizer import generate_netlist_diagram

# =========================================================
# 🚀 APP INIT
# =========================================================
app = Flask(__name__, static_folder="D:/AI_EDA_TOOL/static")

BASE_PATH = "D:/AI_EDA_TOOL/"
RUNS_PATH = BASE_PATH + "runs/"

# =========================================================
# 🧠 FORMAT AI OUTPUT (🔥 NEW FIX)
# =========================================================
def format_ai_output(ai_result):
    fixed_code = ai_result.get("fixed_code", "")
    explanation = ai_result.get("explanation", [])
    errors = ai_result.get("errors", [])

    # Convert explanation → paragraph
    if isinstance(explanation, list):
        explanation = "\n\n".join([str(e) for e in explanation if e])

    # Convert errors → bullet list
    if isinstance(errors, list):
        errors = "\n".join([f"- {str(e)}" for e in errors if e])

    return fixed_code, explanation, errors

# =========================================================
# 🧠 MAIN ROUTE
# =========================================================
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        clear_runs()
        file = request.files["file"]

        if file:
            try:
                # ===============================
                # 📂 SAVE FILE
                # ===============================
                design_path = os.path.join(RUNS_PATH, "design.v")
                file.save(design_path)

                with open(design_path, "r") as f:
                    code = f.read()

                # ===============================
                # 🤖 AI ANALYSIS
                # ===============================
                ai_result = analyze_verilog(code)

                fixed_code, ai_explanation, ai_error = format_ai_output(ai_result)
                model_used = ai_result.get("model_used", "N/A")

                # ===============================
                # 🔍 TOP MODULE
                # ===============================
                top_module = find_top_module(code)

                if not top_module or top_module == "Not Found":
                    return "<h2>Top module not found</h2>"

                if isinstance(top_module, list):
                    top_module = top_module[0]

                # ===============================
                # 🔌 PORTS
                # ===============================
                ports = extract_ports(code, top_module)
                ports = [(str(p[0]), str(p[1])) for p in ports]

                # ===============================
                # 🧪 TESTBENCH
                # ===============================
                tb_code = generate_testbench(top_module, ports, code)

                with open(RUNS_PATH + "tb.v", "w", encoding="utf-8") as f:
                    f.write(tb_code)

                # ===============================
                # ⚡ SIMULATION
                # ===============================
                sim_result = run_simulation()

                # ===============================
                # 📊 OTHER ANALYSIS
                # ===============================
                generate_circuit_diagram(code)
                generate_fsm_diagram(code)
                truth_df = generate_truth_table(code)

                yosys_report = run_yosys(top_module)
                ppa = extract_ppa(yosys_report)

                generate_netlist_diagram()

                port_count = len(ports)
                input_ports = [p for p in ports if p[0] == "input"]
                sim_cycles = 2 ** len(input_ports)

                # ===============================
                # 🎨 RENDER UI
                # ===============================
                return render_ui(
                    top_module, ports, sim_result,
                    fixed_code, ai_explanation, ai_error, model_used,
                    truth_df, port_count, sim_cycles, ppa
                )

            except Exception as e:
                return f"<h2>ERROR:</h2><pre>{str(e)}</pre>"

    return render_template("index.html")

# =========================================================
# 🎨 UI RENDER (🔥 IMPROVED)
# =========================================================
def render_ui(top_module, ports, sim_result,
              fixed_code, ai_explanation, ai_error, model_used,
              truth_df, port_count, sim_cycles, ppa):

    return f"""
<style>
body {{ font-family: Arial; background: #0d1117; color: #e6edf3; padding: 20px; }}
.panel {{ background:#161b22; padding:20px; margin-bottom:15px; border-radius:10px; }}
pre {{ background:#0d1117; color:#00ffcc; padding:12px; border-radius:8px; overflow-x:auto; }}
h2 {{ color:#58a6ff; }}
h3 {{ color:#58a6ff; margin-top:10px; }}
.error {{ color:#ff6b6b; }}
</style>

<h2>File Processed Successfully</h2>

<div class="panel">
<h3>🤖 AI Analysis</h3>

<b>Model Used:</b> {model_used}<br><br>

<h3>🔧 Fixed Code</h3>
<pre>{fixed_code}</pre>

<h3>🧠 Explanation</h3>
<div style="white-space: pre-wrap; line-height:1.6;">
{ai_explanation}
</div>

<h3 class="error">⚠ Errors</h3>
<pre class="error">{ai_error}</pre>
</div>

<div class="panel">
<h3>🔍 Top Module</h3>
<pre>{top_module}</pre>
</div>

<div class="panel">
<h3>🔌 Ports</h3>
<pre>{ports}</pre>
</div>

<div class="panel">
<h3>🧪 Simulation Output</h3>
<pre>{sim_result}</pre>
</div>

<div class="panel">
<h3>📊 Truth Table</h3>
{truth_df.to_html(index=False)}
</div>

<div class="panel">
<h3>📏 PPA Analysis</h3>
<pre>
Area  : {ppa['area']} cells
Delay : {ppa['delay']}
Power : {ppa['power']} mW
</pre>
</div>

<div class="panel">
<h3>🔌 Circuit Diagram</h3>
<img src="/static/circuit.png" width="450">
</div>

<div class="panel">
<h3>🔁 FSM Diagram</h3>
<img src="/static/fsm.png" width="450">
</div>

<div class="panel">
<h3>🔗 Netlist</h3>
<img src="/static/netlist.png" width="500">
</div>

<div class="panel">
<h3>⚙️ Metrics</h3>
Ports: {port_count}<br>
Simulation Cycles: {sim_cycles}
</div>
"""

# =========================================================
# ▶️ RUN
# =========================================================
if __name__ == "__main__":
    app.run(debug=True)