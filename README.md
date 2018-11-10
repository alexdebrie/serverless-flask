# Serverless-Flask
### API edition.

The fastest way to a Flask application with [Serverless](https://github.com/serverless/serverless).

This version includes APISpec and Marshmallow for easy declaration of input and output for API functions
and automatic generation of swagger. CORS is enabled and can be customized.

## Usage
* [Install yarn](https://yarnpkg.com/lang/en/docs/install/#mac-stable) if you don't have it
```
yarn global install serverless
sls install --url https://github.com/revmischa/serverless-flask --name my-flask-app
cd my-flask-app
yarn setup
# <answer prompts>
sls deploy
```

Once the deploy is complete, run `sls info` to get the endpoint:

```
$ sls info
Service Information
<snip>
endpoints:
  ANY - https://abc6defghi.execute-api.eu-central-1.amazonaws.com/dev <-- Endpoint
  ANY - https://abc6defghi.execute-api.eu-central-1.amazonaws.com/dev/{proxy+}
```

Copy paste into your browser, and _voila_!

## Local development

To develop locally, create a virtual environment and install your dependencies:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then, run your app:

```
sls wsgi serve
 * Running on http://localhost:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```

Navigate to [localhost:5000](http://localhost:5000) to see swagger UI for your API.


## Client CodeGen

Want to generate a client library for your API? No problem.

* Run `make generate-client lang=$LANG`
Where `LANG` can be any language supported by [OpenAPI-Generator](https://github.com/openapitools/openapi-generator#overview).
E.g. `go` or `typescript-axios`.


## Configuration

The `postsetup.js` prompt will walk you through some setup questions that may be
custom to your use case. This includes:
- Whether you want to set up a custom domain that you own, rather than a random assigned one from AWS. For more details on that, look at [this post on setting up a custom domain with API Gateway and Serverless](https://serverless.com/blog/serverless-api-gateway-domain/).
