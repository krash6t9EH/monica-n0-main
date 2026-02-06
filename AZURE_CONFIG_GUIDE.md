# Azure AI Configuration for Cline (2026)

To use your Azure credits and models within the Cline extension, follow these configuration settings.

## Option 1: Azure OpenAI (GPT-4o, etc.)
Use this if you have deployed models in the **Azure OpenAI Service**.

- **API Provider**: `Azure OpenAI`
- **Base URL**: `https://{YOUR_RESOURCE_NAME}.openai.azure.com`
- **Azure API Key**: `{YOUR_AZURE_OPENAI_KEY}`
- **Deployment Name**: `{YOUR_DEPLOYMENT_NAME}` (e.g., `gpt-4o`)
- **API Version**: `2024-08-01-preview` (or latest)

## Option 2: Microsoft AI Foundry Model Catalog (Llama, Mistral, Phi)
Use this if you are using "Pay-as-you-go" models from the **AI Foundry / AI Studio Catalog**.

- **API Provider**: `OpenAI Compatible`
- **Base URL**: `{YOUR_TARGET_URI}` (Found in the Deployment tab of AI Foundry)
- **API Key**: `{YOUR_MODEL_KEY}`
- **Model ID**: `{YOUR_DEPLOYMENT_NAME}`

## Common Troubleshooting
1. **Endpoint Suffix**: Ensure your Base URL does *not* end with a slash `/`.
2. **Resource Name**: The resource name is the name of your Azure OpenAI resource, not the project name.
3. **Region**: Ensure your model is deployed in a region that supports the requested API version.
4. **Credits**: Monitor your Azure portal "Cost Management" to ensure your credits are being applied correctly to these endpoints.

---
*Generated for the Monica Project - Digamoni.ca*
