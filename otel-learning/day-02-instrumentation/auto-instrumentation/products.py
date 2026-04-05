from flask import Flask

app = Flask(__name__)

@app.route("/")
def charge():
    return "Here are all of the available products"

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)


# for auto-instrumentation install opentelemetry-distro, opentelemetry-exporter-otlp
# and the run opentelemetry-bootstrap -a install it will install all instrumentation libraries required for your application.
'''
    --traces_exporter         or  OTLP_TRACES_EXPORTER
    --metrics_exporter        or  OTLP_METRICS_EXPORTER   <<===  env vars should be exported and CLI configs are attached at command execution.
    --service_name            or  OTLP_SERVICE_NAME
    --exporter_otlp_endpoint  or  OTLP_EXPORTER_ENDPOINT 

    during ENV variables the endpoint is not automatically appended with /v1/traces or /v1/metrics and logs we need to configure it manually. but in CLI way the exporter will automatically append this.
'''


'''
    opentelemetry-instrument --traces_exporter console --service_name products --metrics_exporter console python products.py
                                                    ( or )
                            opentelemetry-instrument python products.py

D:\OTelInstrumentation\day-02\AutoInstrumentation> * Serving Flask app 'products'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [12/Feb/2026 23:32:34] "GET / HTTP/1.1" 200 -
{
    "name": "GET /",
    "context": {
        "trace_id": "0x694332e6eec1954dd99b58e14c449774",
        "span_id": "0x9a44ec0893b21fc5",
        "trace_state": "[]"
    },
    ...
}
'''
