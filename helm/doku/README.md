# Doku Helm Chart
[![Artifact Hub](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/doku)](https://artifacthub.io/packages/search?repo=doku)

## Introduction

Doku is an observability tool for Large Language Models (LLM). This Helm chart deploys Doku and its required components, including TimescaleDB, on a Kubernetes cluster.

## Installation

To install the Doku chart with the release name `my-doku`:

```bash
helm repo add dokulabs https://dokulabs.github.io/doku/
helm install doku dokulabs/doku
```

## Getting Started post Installation

After the Doku chart is successfully deployed to your Kubernetes cluster, you'll need to generate an API key that can be used by the Dokumetry SDKs to authenticate requests to the Doku platform.

### Generating Your First API Key

To create an API key, follow these steps:

1. Determine the external IP address or hostname of the Doku service. If you're using a LoadBalancer service type, you can find this information by running:

    ```bash
    kubectl get svc -l "app.kubernetes.io/name=doku"
    ```

    Look for the `EXTERNAL-IP` value in the output if service type is LoadBalancer/NodePort. Else port-forward the service locally.

2. Use the following `curl` command to make a POST request to the `/api/keys` endpoint:

    ```bash
    curl -X POST http://<Doku-URL>/api/keys \
    -H 'Authorization: ""' \
    -H 'Content-Type: application/json' \
    -d '{"Name": "Ishan"}'
    ```

    Replace `<Doku-URL>` with the actual external IP address or hostname of your Doku service. If you port-fowareded your service, You will need to specify the port aswell(Default is `9044`)

    **Note**: The `Authorization` header can be set to an empty string (`""`) for the first request since no API keys exist yet. In any following requests to Doku endpoints, you will need to use this api key in the `Authorization` header.

3. The above command will return a JSON response containing your new API key. Here's an example response:

    ```json
    {
        "status": "200",
        "message": "dk*****************",
    }
    ```

    Store the provided API key securely; this is the only time you will see it in full.

## Start sending LLM Observability data to Doku

Once Doku has been installed in your cluster and API Key, You can configure the `dokumetry` Python and Node SDKs in your LLM Application. These SDKs are designed to collect and send observability data directly to your instance of Doku, providing valuable insights and metrics to monitor and analyze the performance and usage of your Large Language Models (LLM).

## Configuration

The following table lists the configurable parameters of the Doku chart and their default values.

| Parameter                                   | Description                                                                                          | Default                                                                       |
|---------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| `nameOverride`                              | Override the name of the chart                                                                       | `""`                                                                          |
| `fullnameOverride`                          | Override the full name of the chart                                                                  | `""`                                                                          |
| `replicaCount`                              | Number of Doku replicas                                                                              | `1`                                                                           |
| `image.repository`                          | Container image repository                                                                           | `ghcr.io/dokulabs/ingester`                                                   |
| `image.pullPolicy`                          | Container image pull policy                                                                          | `IfNotPresent`                                                                |
| `image.tag`                                 | Container image tag (defaults to the chart's `appVersion`)                                           | `""`                                                                          |
| `imagePullSecrets`                          | Image pull secrets for Pod                                                                           | `[]`                                                                          |
| `service.type`                              | Kubernetes Service type                                                                              | `LoadBalancer`                                                                |
| `service.port`                              | Service port                                                                                         | `9044`                                                                        |
| `service.sessionAffinity`                   | Service session affinity                                                                             | `None`                                                                        |
| `resources.limits.cpu`                      | CPU limit                                                                                            | `1000m`                                                                       |
| `resources.limits.memory`                   | Memory limit                                                                                         | `1280Mi`                                                                      |
| `resources.requests.cpu`                    | CPU request                                                                                          | `100m`                                                                        |
| `resources.requests.memory`                 | Memory request                                                                                       | `128Mi`                                                                       |
| `podAnnotations`                            | Annotations to be added to pods                                                                      | `{}`                                                                          |
| `nodeSelector`                              | Node labels for pod assignment                                                                       | `{}`                                                                          |
| `tolerations`                               | Tolerations for pod assignment                                                                       | `[]`                                                                          |
| `affinity`                                  | Affinity for pod assignment                                                                          | `{}`                                                                          |
| `ingress.enabled`                           | Enable ingress controller resource                                                                   | `false`                                                                       |
| `ingress.className`                         | Name of the IngressClass cluster                                                                     | `""`                                                                          |
| `ingress.annotations`                       | Ingress annotations                                                                                  | `{}`                                                                          |
| `ingress.hosts[0].host`                     | Hostname to your installation                                                                        | `chart-example.local`                                                         |
| `ingress.hosts[0].paths[0].path`            | Path within the URL structure                                                                        | `/`                                                                           |
| `ingress.hosts[0].paths[0].pathType`        | Ingress path type                                                                                    | `ImplementationSpecific`                                                      |
| `ingress.tls`                               | TLS configuration                                                                                    | `[]`                                                                          |
| `config.configMap.existingConfig`           | Use an existing config file                                                                          | `false`                                                                       |
| `config.configMap.name`                     | Name of the ConfigMap to use                                                                         | `""`                                                                          |
| `config.configMap.filename`                 | Name of the config file in the ConfigMap                                                             | `"l"`                                                                         |
| `config.secret.existingSecret`              | Use an existing secret for database credentials                                                      | `false`                                                                       |
| `config.secret.name`                        | Name of the existing secret                                                                          | `""`                                                                          |
| `config.secret.passwordKey`                 | Key in the secret that contains the TimescaleDB User's password                                      | `""`                                                                          |
| `config.secret.usernameKey`                 | Key in the secret that contains the TimescaleDB User name                                            | `""`                                                                          |
| `config.pricingInfo.url`                    | URL to download Pricing data file                                                                    | `https://raw.githubusercontent.com/dokulabs/ingester/main/assets/pricing.json` |
| `config.dbConfig.name`                      | Name of the database                                                                                 | `postgres`                                                                    |
| `config.dbConfig.username`                  | Database username (ignored if `config.secret.existingSecret` is `true`)                              | `admin`                                                                       |
| `config.dbConfig.password`                  | Database password (ignored if `config.secret.existingSecret` is `true`)                              | `DOKU`                                                                        |
| `config.dbConfig.host`                      | Database host (automatic if TimescaleDB is deployed by the chart)                                    | `{{ .Release.Name }}-db.{{ .Release.Namespace }}.svc.cluster.local`           |
| `config.dbConfig.port`                      | Database port                                                                                        | `5432`                                                                        |
| `config.dbConfig.sslmode`                   | SSL mode for database connection                                                                     | `require`                                                                     |
| `config.dbConfig.maxOpenConns`              | Maximum open database connections                                                                    | `10`                                                                          |
| `config.dbConfig.maxIdleConns`              | Maximum idle database connections                                                                    | `10`                                                                          |
| `config.dbConfig.dataTable`                 | Name of the table to store data                                                                      | `DOKU`                                                                        |
| `config.dbConfig.apiKeyTable`               | Name of the table to store API keys                                                                  | `APIKEY`                                                                      |
| `config.observabilityPlatform.enabled`      | Enable export to the Observability Platform (optional)                                               | `false`                                                                       |
| `config.observabilityPlatform.grafanaCloud.logsUrl` | Grafana Cloud Logs URL (optional)                | `https://logs-prod-us-central1.grafana.net`                                   |
| `config.observabilityPlatform.grafanaCloud.logsUsername` | Grafana Cloud Logs Username (optional)         | `your_loki_username`                                                          |
| `config.observabilityPlatform.grafanaCloud.cloudAccessToken` | Grafana Cloud API Token (optional)            | `your_grafana_cloud_api_token`                                                |
| `timescaledb.enabled`                       | Enable TimescaleDB submodule                                                                         | `true`                                                                        |
| `timescaledb.fullnameOverride`              | Override the full name of the TimescaleDB Release                                                    | `{{ .Release.Name }}-db`                                                      |
| `timescaledb.secrets.credentials.PATRONI_admin_PASSWORD` | Password for the TimescaleDB admin user            | `DOKU`                                                                        |
| `timescaledb.service.primary.type`          | Kubernetes Service type for TimescaleDB                                                              | `LoadBalancer`                                                                 |
| `timescaledb.service.primary.port`          | Service port for TimescaleDB                                                                         | `5432`                                                                        |
| `timescaledb.persistentVolumes.data.size`   | Size of the persistent volume for TimescaleDB data                                                   | `10Gi`                                                                        |


**Note**: Although the table above shows the parameters. Refer to [`values.yaml`](values.yaml) for a full list.

### Configuring Doku

You can adjust the Doku configuration by specifying each parameter using the `--set key=value` argument to `helm install`. For example:

```bash
helm install doku \
  --set service.type=NodePort \
  --set service.port=8080 \
  dokulabs/doku
```

Alternatively, you can provide a YAML file that specifies the values for the required parameters while installing the chart. For example:

```bash
helm install doku -f values.yaml dokulabs/doku
```

## Uninstalling the Chart

To uninstall/delete the `doku` deployment:

```bash
helm delete doku
```

## Upgrading the Chart

To upgrade the `doku` deployment:

```bash
helm upgrade doku dokulabs/doku
```

If you've made any changes to [`values.yaml`](values.yaml), remember to use the `-f` flag to provide the updated file.

### Support

For support, issues, or feature requests, submit an issue through the [GitHub issues](https://github.com/dokulabs/ingester/issues) associated with this repository.
