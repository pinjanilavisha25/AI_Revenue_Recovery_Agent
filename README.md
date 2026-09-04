# AI Revenue Recovery Agent (Enterprise Edition)

Autonomous fintech compliance and revenue recovery system built for **Razorpay Buildathon (Track 03: AI Revenue Recovery)**. The platform detects failed transactions, enforces deterministic financial policy guardrails, segregates workflow queues, and maintains an immutable audit trail.

## 🚀 Key Features

* **Deterministic Policy Guardrails:** Built-in economic threshold floors (e.g., skipping micro-transactions below a custom value) to save gateway fee overhead.
* **Structured Audit Trail & Timestamping:** Tracks unique transaction IDs, precise execution timestamps, and detailed rationale logs for every decision path.
* **Human Support Escalation Queue:** Automatically separates high-risk card anomalies and complex high-value failures into a dedicated review queue.
* **Visual Analytics & Reporting:** Real-time metrics and bar charts breaking down revenue loss by failure categories (e.g., gateway timeouts, bank declines).
* **CSV Compliance Export:** One-click data export for operations and finance teams.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Framework:** Streamlit
* **Data Manipulation:** Pandas

---

## ⚙️ Quickstart & Installation

Follow these steps to run the application locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/ai-revenue-recovery-agent.git](https://github.com/your-username/ai-revenue-recovery-agent.git)
   cd ai-revenue-recovery-agent

2. Install dependencies:
   Make sure you have Python installed, then run:
   pip install -r requirements.txt

3.Verify files:
Ensure both app.py and transactions.csv are present in the root directory.

4.Launch the application:
  streamlit run app.py



PROJECT ARCHITECTURE
ai-revenue-recovery-agent/
│
├── app.py               # Main Streamlit enterprise dashboard & agent logic
├── transactions.csv     # Synthetic dataset of failed checkout/payment records
├── requirements.txt     # Python package dependencies
└── README.md            # Project documentation

