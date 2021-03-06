#Import DD API client:
#pip3 install datadog-api-client

#Run with:
#export DD_SITE="datadoghq.com" DD_API_KEY="<DD_API_KEY>" DD_APP_KEY="<DD_APP_KEY>"
#python3 "containertags.py"


import sys
import json
import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import metrics_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)
    metric_name = "kubernetes.containers.running"  # str | The name of the metric.

    # example passing only required values which don't have defaults set
    try:
        # List tags by metric name
        api_response = api_instance.list_tags_by_metric_name(metric_name)
        #pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_tags_by_metric_name: %s\n" % e)


json_data = api_response.to_dict()

json_tags = json_data['data']['attributes']['tags'];


for match in json_tags:
   if match.startswith('kube_cluster_name'):
      print(match)

for match in json_tags:
   if match.startswith('kube_deployment'):
      print(match)

for match in json_tags:
   if match.startswith('kube_container_name'):
      print(match)