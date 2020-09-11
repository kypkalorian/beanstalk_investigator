import boto3
import json
import time
import difflib

client = boto3.client('elasticbeanstalk')


response = client.describe_configuration_settings(
    ApplicationName='BeanstalkPlatformTest',
    EnvironmentName='NodeJsPlatform4Test'
)

conf_settings = response['ConfigurationSettings']

print(len(conf_settings))

opts_list = []

for conf_items in conf_settings:

    print("\n=========================================>\n")

    option_settings = conf_items['OptionSettings']

    for item in option_settings:
        print(json.dumps(item, indent=4, default=str))

        namespace = item.get('Namespace', "EMPTY")
        optionname = item.get('OptionName', "EMPTY")
        value = item.get('Value', "EMPTY")

        curr_string = f"{namespace}.{optionname} = {value}"

        opts_list.append(curr_string)


with open(f"output-{time.time()}.json", 'w') as f:
    f.write(json.dumps(opts_list, indent=4, default=str))


