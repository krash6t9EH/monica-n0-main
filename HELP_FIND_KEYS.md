# How to Find the Right Keys for Microsoft Foundry / Azure

You are seeing multiple keys because Foundry aggregates different resources. Here is how to pick the right one.

## 1. Go to your Foundry Project
Open your project in [Microsoft AI Foundry](https://ai.azure.com/).

## 2. Click on "Deployments" (Left Sidebar)
Do not look at the "Project Settings" or generic "Endpoints" yet. Go specifically to **Deployments**.

## 3. Select the Model You Want to Use
You will see a list of models (e.g., `gpt-4`, `llama-3-70b`). Click on the name of the one you want to access.

## 4. Copy the Details from the Deployment Page
This page shows the **exact** connection details for *that specific model*.

### If it is an Azure OpenAI Model (GPT-4, GPT-3.5):
*   **Target URI / Endpoint**: It will look like: `https://YOUR-RESOURCE-NAME.openai.azure.com/`
*   **Key**: Copy "Key 1".
*   **Use these in `mcp.json`**.

### If it is a "Model as a Service" (Llama, Phi, Mistral):
*   **Target URI / Endpoint**: It will look like: `https://Llama-3-70b-instruct-xyz.eastus.models.ai.azure.com/`
*   **Key**: Copy the "Primary Key".
*   **Use these in `mcp.json`**.

---

**Which one to use?**
*   **Azure OpenAI Endpoint** (`openai.azure.com`): Use this for GPT models.
*   **Serverless Endpoint** (`models.ai.azure.com`): Use this for Llama/Phi models.
*   **Foundry Project Endpoint** (`inference.ml.azure.com`): **IGNORE THIS**. This is for other services.
