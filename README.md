# Doku: Open Source Observability for LLMs

Welcome to Doku, the open source observability platform crafted for the world of Large Language Models (LLM). In an era where LLMs are revolutionizing how we interact with technology, Doku provides an indispensable tool for developers and teams seeking deep insights into LLM performance and usage. By offering the ability to send observability data to platforms like Grafana Cloud, Doku ensures that you are always on top of your LLM's health and efficiency.

Serving as a bridge between your language models and keen analytics, Doku stands out with its ability to collect, centralize, and transmit observability data with ease. A visualization UI for Doku is under development, which will soon empower users to monitor and analyze their LLM usage directly within Doku itself.

As an open source initiative, Doku welcomes contributions and input from the community. It is built with the vision of making LLM observability seamless and accessible.

## Supported LLMs:

- ✅ OpenAI
- ✅ Cohere
- ✅ Anthropic

We plan to extend our support to more LLMs, always refining observability.


## Getting Started with Doku

Jumpstart your journey with Doku by deploying it via our Helm chart, designed to simplify the installation process on any Kubernetes cluster.

### Deploying with Helm

To install the Doku Helm chart, follow these steps:

1. Add the Doku Helm repository to your Helm setup:

```shell
helm repo add dokulabs https://dokulabs.io/helm/charts
```

2. Update your Helm repositories to fetch the latest chart information:

```shell
helm repo update
```

3. Install the Doku chart with the release name `my-doku`:

```shell
helm install doku dokulabs/doku
```

For a detailed list of configurable parameters for the Helm chart, refer to the `values.yaml` file in the Doku [Helm chart](https://github.com/dokulabs/doku/tree/main/helm/doku).

### Generating an API Key

Once Doku is up and running, proceed to generate your first API key:

1. Hit the `/api/keys` endpoint of the Doku service:

```shell
curl -X POST http://<Doku-URL>/api/keys \
-H 'Authorization: ""' \
-H 'Content-Type: application/json' \
-d '{"Name": "YourKeyName"}'
```

**Note**: 
- For your initial API call, `Authorization` header can be set to `""`. 
- Store the provided API key securely; it will be required to pass the generated and a valid API Ke in `Authorization` header  for subsequent API calls.

### Automatically send LLM Observability Data

Elevate your LLM observability by integrating the `dokumetry` Python and NodeJS SDKs into your applications.

#### Python

Install the `dokumetry` Python SDK using pip:

```shell
pip install dokumetry
```

##### Example Usage for tracking `OpenAI` Usage:

```python
from openai import OpenAI
import dokumetry

client = OpenAI(
    api_key="YOUR_OPENAI_KEY"
)

# Pass the above `client` object along with your DOKU URL and Token and this will make sure that all OpenAI calls are automatically tracked.
dokumetry.init(client, doku_url="YOUR_DOKU_URL", token="YOUR_DOKU_TOKEN")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is LLM Observability",
        }
    ],
    model="gpt-3.5-turbo",
)
```

#### Node

Install the `dokumetry` NodeJS SDK using npm:

```shell
npm install dokumetry
```

##### Example Usage for tracking `OpenAI` Usage:

```javascript
import OpenAI from 'openai';
import DokuMetry from 'dokumetry';

const openai = new OpenAI({
  apiKey: 'My API Key', // defaults to process.env["OPENAI_API_KEY"]
});

// Pass the above `openai` object along with your DOKU URL and Token and this will make sure that all OpenAI calls are automatically tracked.
DokuMetry.init({llm: openai, dokuURL: "YOUR_DOKU_URL", token: "YOUR_DOKU_TOKEN"})

async function main() {
  const chatCompletion = await openai.chat.completions.create({
    messages: [{ role: 'user', content: 'What are the key to effective observability?' }],
    model: 'gpt-3.5-turbo',
  });
}

main();
```

Refer to the SDK documentation for more advanced configurations and use cases.

---

Doku is an evolving platform, and we're excited to have you onboard this journey. Your feedback, feature requests, and contributions can help shape Doku into the ultimate observability solution for LLM. Get in touch with us through our [GitHub repository](https://github.com/dokulabs/doku).

Looking into the future, Doku will soon bring its own visualization interface to further enhance your observational prowess. Stay tuned, and let's build a transparent, observable future for AI!