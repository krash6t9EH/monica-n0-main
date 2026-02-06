import sys
import json
import os
import urllib.request
import urllib.error

# Configuration
# Users should set these environment variables in mcp.json or .env
# OPENAI_API_KEY
# OPENAI_BASE_URL (Full URL to chat/completions or base)

def log(msg):
    sys.stderr.write(str(msg) + "\n")
    sys.stderr.flush()

def call_azure(messages):
    api_key = os.environ.get("OPENAI_API_KEY")
    endpoint = os.environ.get("OPENAI_BASE_URL")
    
    if not api_key or not endpoint:
        return "Error: OPENAI_API_KEY or OPENAI_BASE_URL environment variables are not set. Please configure them in mcp.json."
    
    # URL handling: Try to construct the correct Azure OpenAI URL
    url = endpoint
    if "chat/completions" not in url:
        if not url.endswith("/"): url += "/"
        # You might need to adjust api-version based on your deployment
        url += "chat/completions?api-version=2024-02-15-preview"
    
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key,
        "Ocp-Apim-Subscription-Key": api_key
    }
    
    data = {
        "messages": messages,
        "max_tokens": 1000
    }
    
    try:
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result['choices'][0]['message']['content']
    except urllib.error.HTTPError as e:
        return f"HTTP Error calling Azure: {e.code} - {e.reason}. Body: {e.read().decode('utf-8')}"
    except Exception as e:
        return f"Error calling Azure: {str(e)}"

def main():
    while True:
        try:
            line = sys.stdin.readline()
            if not line: break
            
            request = json.loads(line)
            req_id = request.get("id")
            method = request.get("method")
            
            response = {"jsonrpc": "2.0", "id": req_id}
            
            if method == "initialize":
                response["result"] = {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {},
                        "resources": {}
                    },
                    "serverInfo": {"name": "foundry-mcp", "version": "1.0"}
                }
            elif method == "notifications/initialized":
                # No response needed for notifications, but we must handle the message
                continue
            elif method == "tools/list":
                response["result"] = {
                    "tools": [{
                        "name": "ask_foundry_model",
                        "description": "Send a query to the configured Microsoft Foundry (Azure OpenAI) model.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "question": {"type": "string", "description": "The prompt or question for the model"}
                            },
                            "required": ["question"]
                        }
                    }]
                }
            elif method == "tools/call":
                params = request.get("params", {})
                name = params.get("name")
                args = params.get("arguments", {})
                
                if name == "ask_foundry_model":
                    question = args.get("question")
                    answer = call_azure([{"role": "user", "content": question}])
                    response["result"] = {
                        "content": [{"type": "text", "text": answer}]
                    }
                else:
                    response["error"] = {"code": -32601, "message": "Method not found"}
            
            # Handle Resources/Prompts if needed in future
            
            if "result" in response or "error" in response:
                sys.stdout.write(json.dumps(response) + "\n")
                sys.stdout.flush()
                
        except Exception as e:
            log(f"Critical Error: {e}")

if __name__ == "__main__":
    main()
