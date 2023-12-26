# Doku: Open Source Observability for LLMs
[![Doku](https://img.shields.io/badge/Doku-orange)](https://github.com/dokulabs/doku)
[![License](https://img.shields.io/github/license/dokulabs/doku?label=license&logo=github&color=f80&logoColor=fff%22%20alt=%22License)](https://github.com/dokulabs/python-sdk/blob/main/LICENSE)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/dokulabs/doku)](https://github.com/dokulabs/python-sdk/pulse)
[![GitHub Contributors](https://img.shields.io/github/contributors/dokulabs/doku)](https://github.com/dokulabs/python-sdk/graphs/contributors)

[![Artifact Hub](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/doku)](https://artifacthub.io/packages/search?repo=doku)
[![Python Library Version](https://img.shields.io/github/tag/dokulabs/python-sdk.svg?&label=dokumetry%20version&logo=pypi)](https://pypi.org/project/dokumetry/)
[![NPM Package Version](https://img.shields.io/github/tag/dokulabs/node-sdk.svg?&label=dokumetry%20version&logo=npm)](https://www.npmjs.com/package/dokumetry)



Doku is an open-source observability tool engineered for Large Language Models (LLMs). Designed for ease of integration into existing LLM applications, Doku offers unparalleled insights into usage, performance, and overhead—allowing you to analyze, optimize, and scale your AI applications and LLM usage effectively. 

Whether you're working with OpenAI, Cohere, or Anthropic, It tracks all your LLM requests transparently and conveys the insights needed to make data-driven decisions. From monitoring usage and understanding latencies to managing costs and collaborating effortlessly, Doku grants you the lens to view your models in high definition.

Leveraging Doku, you can get:

- 🕵️ **In-depth LLM Monitoring**: Track every request to LLM platforms like OpenAI with precision, ensuring comprehensive visibility over your model's interactions.
- 🎛️ **Granular Usage Insights of your LLM Applications**: Assess your LLM's performance and costs with fine-grained control, breaking down metrics by environment (such as staging or production) or application, to optimize for efficiency and scalability.
- 📈 **Connect to Observability Platformss**: Export LLM Observablity data and insights from Doku to popular observability platforms such as Grafana Cloud or Datadog.
- 👥 **Team-centric Workflow**: Enhance team collaboration with seamless data sharing capabilities, creating an integrated environment for observability-driven teamwork.

## Supported LLMs:

- ✅ [OpenAI](https://openai.com/)
- ✅ [Cohere](https://cohere.com/)
- ✅ [Anthropic](https://www.anthropic.com/)

And this is only the beginning—as we grow, so will our list of supported LLM platforms. We're dedicated to continually refining our features to enhance your LLM and Generative AI observability experience.


## 🚀 Getting Started with Doku

Jumpstart your journey with Doku by deploying it via our Helm chart, designed to simplify the installation process on any Kubernetes cluster.

### Deploying with Helm 📦 

To install the Doku Helm chart, follow these steps:

1. Add the Doku Helm repository to your Helm setup:

```shell
helm repo add dokulabs https://dokulabs.github.io/helm/
```

2. Update your Helm repositories to fetch the latest chart information:

```shell
helm repo update
```

3. Install the Doku chart with the release name `doku`:

```shell
helm install doku dokulabs/doku
```

**NOTE**:
> As Doku does not have a built-in visualization UI yet, it is preferred that you set up the `observabilityPlatform` configuration within the [values.yaml](https://github.com/dokulabs/doku/tree/main/helm/doku/values.yaml) file in the Helm Chart. Doing so enables visualization of the LLM Observability data processed by Doku using an external observability platform.

For a detailed list of configurable parameters for the Helm chart, refer to the `values.yaml` file in the [Helm chart](https://github.com/dokulabs/doku/tree/main/helm/doku).

### 🔑 Generating an API Key

Once Doku is up and running, proceed to generate your first API key:

1. Hit the `/api/keys` endpoint of the Doku service:

```shell
curl -X POST http://<Doku-URL>/api/keys \
-H 'Authorization: ""' \
-H 'Content-Type: application/json' \
-d '{"Name": "YourKeyName"}'
```

**Note**: 
> - For your initial API call, `Authorization` header can be set to `""`. 
> - Store the provided API key securely; it will be required to pass the generated and a valid API Ke in `Authorization` header  for subsequent API calls.

### ⚡️ Automatically send LLM Observability Data to Doku

With the `dokumetry` SDKs for [Python](https://github.com/dokulabs/python-sdk) and [NodeJS](https://github.com/dokulabs/node-sdk), sending observability data to Doku is just **TWO** lines of code in your application. Once integrated, the SDKs take care of capturing and conveying LLM usage data directly to your Doku instance, requiring minimal effort on your part.

#### Python

Install the `dokumetry` [Python SDK](https://pypi.org/project/dokumetry/) using pip:

```shell
pip install dokumetry
```

Add the following two lines to your application code:

```python
import dokumetry

dokumetry.init(llm=client, doku_url="YOUR_DOKU_URL", token="YOUR_DOKU_TOKEN")
```

##### Example Usage for monitoring `OpenAI` Usage:

```python
from openai import OpenAI
import dokumetry

client = OpenAI(
    api_key="YOUR_OPENAI_KEY"
)

# Pass the above `client` object along with your DOKU URL and Token and this will make sure that all OpenAI calls are automatically tracked.
dokumetry.init(llm=client, doku_url="YOUR_DOKU_URL", token="YOUR_DOKU_TOKEN")

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

Refer to the `dokumetry` [Python SDK repository](https://github.com/dokulabs/python-sdk) for more advanced configurations and use cases.

#### Node

Install the `dokumetry` [NodeJS SDK](https://www.npmjs.com/package/dokumetry) using npm:

```shell
npm install dokumetry
```

Add the following two lines to your application code:

```javascript
import DokuMetry from 'dokumetry';

DokuMetry.init({llm: openai, dokuURL: "YOUR_DOKU_URL", token: "YOUR_DOKU_TOKEN"})
```

##### Example Usage for monitoring `OpenAI` Usage:

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

Refer to the `dokumetry` [NodeJS SDK repository](https://github.com/dokulabs/node-sdk) for more advanced configurations and use cases.

## Security

Doku uses key based authentication mechanism to ensure the security of your data. Be sure to keep your API keys confidential and manage permissions diligently. Refer to our [Security Policy](SECURITY)

## Contributing

We welcome contributions to the Doku project. Please refer to [CONTRIBUTING](CONTRIBUTING) for detailed guidelines on how you can participate.

## License

Doku is available under the [GPL-3.0](LICENSE).

## Support

For support, issues, or feature requests, submit an issue through the [GitHub issues](https://github.com/dokulabs/doku/issues) associated with this repository.

## Visualize! Analyze! Optimize!

Join us on this voyage to reshape the future of AI insights. Share your thoughts, suggest features, and explore contributions. Engage with us on [GitHub](https://github.com/dokulabs/doku) and be part of Doku's community-led innovation.
