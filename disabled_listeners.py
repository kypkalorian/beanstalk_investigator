import boto3


def custom_environment_update(env_name, item, value):

    split_idx = None
    for idx, char in enumerate(item):
        if char == '.':
            split_idx = idx
            break

    namespace, setting = item[:split_idx], item[split_idx + 1:]

    print(env_name)
    print(namespace)
    print(setting)
    print(value)

    quit()

    option_setting = {
        # 'ResourceName': 'string',
        'Namespace': namespace,
        'OptionName': setting,
        'Value': value,
    }

    client = boto3.client('elasticbeanstalk')

    response = client.update_environment(
        # ApplicationName='string',
        # EnvironmentId='string',
        EnvironmentName=env_name,
        # GroupName='string',
        # Description='string',
        # Tier={
        #     'Name': 'string',
        #     'Type': 'string',
        #     'Version': 'string'
        # },
        # VersionLabel='string',
        # TemplateName='string',
        # SolutionStackName='string',
        # PlatformArn='string',
        OptionSettings=[
            option_setting,
        ],
        # OptionsToRemove=[
        #     {
        #         'ResourceName': 'string',
        #         'Namespace': 'string',
        #         'OptionName': 'string'
        #     },
        # ]
    )


custom_environment_update("NodeJsPlatform4Test", "aws:elb:listener:80.ListenerEnabled", False)