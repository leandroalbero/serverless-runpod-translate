[![Validate pull request](https://github.com/leandroalbero/serverless-runpod-translate/actions/workflows/pull-request.yaml/badge.svg)](https://github.com/leandroalbero/serverless-runpod-translate/actions/workflows/pull-request.yaml)
# serverless-runpod-translate (WIP)
Service to be run on a serverless runpod.ai instance to translate messages from English to Spanish.

## Requirements
* A dockerhub account
* A runpod.ai account
* If you want to use the GA to upload to dockerhub, add the following secrets to GH:
  * DOCKER_PASSWORD
  * DOCKER_USERNAME

## Usage
Check [the wiki](https://github.com/leandroalbero/serverless-runpod-translate/wiki) for more detailed information
1. Upload the container image to dockerhub (you can use the GA) and then add it as a template to your runpod.ai account.
Alternatively, you can use my image: `leandroalbero/serverless-runpod:main`
2. Create an API on runpod.ai serverless section, add as many servers as you need and customize the settings to your needs.
3. Call the runsync endpoint with the following payload, don't forget to authenticate with your API key (Bearer token):
```json
{
    "input":{
        "src_lang":"es",    # Optional, defaults to ES
        "target_lang":"en", # Optional, defaults to EN
        "input_text":"Hola mundo, esta es una frase en castellano"
    }
}
```
A response will be returned with the translated text to english:
```json
{
    "delayTime": 502,
    "executionTime": 103,
    "id": "sync-b69596b5-1cf2-4f65-a664-a81831ce563d",
    "output": "Hello world, this is a phrase in Spanish",
    "status": "COMPLETED"
}
```

## Development
... TODO

## Testing results
Using 3 nodes of the cheapest instance type (A4000/A5000, 6vCPU, 16GB RAM), the 99th percentile response time is 18ms on 100 concurrent requests.

**Note**: Cold start of the container is around 15s, so the first request will take that long to complete.
