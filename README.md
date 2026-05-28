<img width="1536" height="1024" alt="ChatGPT Image May 28, 2026, 11_40_38 AM" src="https://github.com/user-attachments/assets/0fa7ad0d-c301-4b00-9143-f3b82d430170" />
# Azure Multi-Modal Compliance Orchestration Engine using LangGraph and LangSmith

## Overview

The **Azure Multi-Modal Compliance Orchestration Engine** is an enterprise-grade AI-powered compliance auditing system designed to analyze video content against regulatory and organizational policies using a deterministic Retrieval-Augmented Generation (RAG) workflow.

This project combines:

* **LangGraph** for orchestrating complex LLM workflows
* **LangSmith** for tracing, debugging, and optimization
* **Azure Video Indexer** for multimodal video ingestion
* **Azure AI Search** for compliance rule retrieval
* **Azure OpenAI (GPT-4o)** for reasoning and violation detection
* **Azure Application Insights** for telemetry and observability

The system transforms unstructured multimedia content into structured, actionable JSON compliance reports with full-stack observability and production-grade monitoring.

---

# Features

* Automated Video Compliance QA Pipeline
* Multi-modal video ingestion (Transcript + OCR extraction)
* RAG-based compliance rule retrieval
* Deterministic compliance violation detection
* LangGraph stateful orchestration workflows
* LangSmith tracing and execution monitoring
* Azure Application Insights telemetry integration
* Structured JSON compliance report generation
* Scalable AI project infrastructure

---

# System Architecture

## High-Level Flow

```text
Video Input
   │
   ▼
Azure Video Indexer
(Transcript + OCR)
   │
   ▼
Chunking & Embedding Pipeline
   │
   ▼
Azure AI Search
(Compliance Rule Retrieval)
   │
   ▼
LangGraph Orchestration Engine
   │
   ├── Retrieval Node
   ├── Context Builder
   ├── Compliance Reasoning Node
   ├── Violation Validator
   └── Report Generator
   │
   ▼
Azure OpenAI GPT-4o
(Deterministic Compliance Analysis)
   │
   ▼
Structured JSON Compliance Report
   │
   ├── LangSmith Tracing
   └── Azure Application Insights Telemetry
```

---

# Tech Stack

| Component              | Technology                           |
| ---------------------- | ------------------------------------ |
| Workflow Orchestration | LangGraph                            |
| LLM Observability      | LangSmith                            |
| LLM Provider           | Azure OpenAI (GPT-4o)                |
| Video Processing       | Azure Video Indexer                  |
| Vector Search          | Azure AI Search                      |
| Embeddings             | Azure OpenAI Embeddings              |
| Monitoring             | Azure Application Insights           |
| Backend                | Python                               |
| Architecture Pattern   | RAG (Retrieval-Augmented Generation) |

---

# Project Structure

```text
├── app/
│   ├── graph/
│   ├── nodes/
│   ├── services/
│   ├── prompts/
│   ├── retrieval/
│   ├── monitoring/
│   └── utils/
│
├── data/
│   ├── compliance_rules/
│   └── sample_videos/
│
├── notebooks/
├── tests/
├── requirements.txt
├── .env.example
└── README.md
```

---

# Prerequisites

Before running the project, ensure you have:

* Python 3.10+
* Azure Subscription
* Azure OpenAI Service
* Azure AI Search
* Azure Video Indexer Account
* LangSmith API Key
* Azure Application Insights Resource

---

# Environment Variables

Create a `.env` file in the root directory.

```env
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_DEPLOYMENT=
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=

AZURE_AI_SEARCH_ENDPOINT=
AZURE_AI_SEARCH_KEY=
AZURE_AI_SEARCH_INDEX=

AZURE_VIDEO_INDEXER_ACCOUNT_ID=
AZURE_VIDEO_INDEXER_API_KEY=
AZURE_VIDEO_INDEXER_LOCATION=

LANGCHAIN_API_KEY=
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=

APPLICATIONINSIGHTS_CONNECTION_STRING=
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-org/your-repo.git
cd your-repo
```

## Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Start the Compliance Pipeline

```bash
python main.py
```

## Example Workflow

1. Upload video content
2. Extract transcript and OCR using Azure Video Indexer
3. Generate embeddings
4. Retrieve relevant compliance policies from Azure AI Search
5. Execute LangGraph orchestration workflow
6. Analyze content using GPT-4o
7. Generate structured JSON compliance report
8. Monitor traces in LangSmith
9. Observe telemetry in Azure Application Insights

---

# Example Compliance Report

```json
{
  "video_id": "sample_video_001",
  "status": "Violation Detected",
  "violations": [
    {
      "rule_id": "COMP-102",
      "severity": "High",
      "timestamp": "00:03:15",
      "description": "Unauthorized disclosure of sensitive information."
    }
  ],
  "summary": "1 critical compliance violation identified."
}
```

---

# LangGraph Workflow

The workflow is orchestrated using LangGraph state machines.

## Core Nodes

* Video Ingestion Node
* Transcript/OCR Processing Node
* Embedding Generation Node
* Compliance Retrieval Node
* Context Aggregation Node
* GPT-4o Reasoning Node
* Violation Validation Node
* JSON Report Generator

---

# Observability

## LangSmith

Used for:

* Prompt tracing
* Execution visualization
* Latency analysis
* Token usage monitoring
* Workflow debugging

## Azure Application Insights

Used for:

* Production telemetry
* Error monitoring
* Distributed tracing
* Performance analytics
* Real-time operational dashboards

---

# What You Will Learn

* Mastering LangGraph orchestration
* Building enterprise RAG systems
* Implementing deterministic compliance workflows
* Integrating Azure AI services
* Building multimodal AI pipelines
* Full-stack LLM observability
* Production-grade AI monitoring

---

# Future Enhancements

* Human-in-the-loop review workflows
* Real-time streaming compliance checks
* Multi-language compliance analysis
* Policy versioning support
* Agentic remediation recommendations
* CI/CD deployment templates
* Kubernetes deployment support

---

# Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

# License

This project is licensed under the MIT License.

---

# Acknowledgements

* LangChain
* LangGraph
* LangSmith
* Microsoft Azure AI Services
* OpenAI

---
