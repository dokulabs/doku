# Doku: Open Source Observability for LLMs

Unlock the full potential of your Language Learning Models (LLMs) with Doku—a powerful, open-source observability platform that seamlessly integrates into your existing stack. With a developer-centric approach, Doku goes beyond traditional monitoring to offer a comprehensive suite of features that put you in command of your LLM applications.

Whether you're working with OpenAI, Cohere, or Anthropic, Doku is your partner in harnessing the intricate data flow of LLMs. It tracks all your LLM requests transparently and conveys the insights needed to make data-driven decisions. From monitoring usage and understanding latencies to managing costs and collaborating effortlessly, Doku grants you the lens to view your models in high definition.

The future-rich platform empowers you to:

- 📝 **Monitor each LLM request**: Keep a pulse on all interactions with platforms like OpenAI, ensuring no detail slips through the cracks.
- 💾 **Elevate Data Analysis**: Export crucial LLM data to popular observability platforms such as Grafana Cloud or Datadog.
- 📊 **Understanding usage for each environement and application**: Gauge performance and expense for each enviroment(staging, production) and alos have the option further drill down to analyze usage per application basis.
- 🚀 **Collaborate and Share**: Bring your team into the loop with easy data sharing, fostering a collaborative observability environment.

## Supported LLMs:

- ✅ OpenAI
- ✅ Cohere
- ✅ Anthropic

And this is only the beginning—as we grow, so will our list of supported LLM platforms. We're dedicated to continually refining our features to enhance your observability experience.


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

### Generating an API Key 🔑

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

#### Visualize! Analyze! Optimize!

Join us on this voyage to reshape the future of AI insights. Share your thoughts, suggest features, and explore contributions. Engage with us on [GitHub](https://github.com/dokulabs/doku) and be part of Doku's community-led innovation.