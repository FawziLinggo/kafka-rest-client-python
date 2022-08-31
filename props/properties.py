from jproperties import Properties

configs = Properties()
with open('../config.properties', 'rb') as config_file:
    configs.load(config_file)


class PropsConfig:
    try:
        # Producer
        url_producer = configs.get("url_producer").data
        topic_producer_name = configs.get("topic_producer_name").data

        # Security
        ca_crt = configs.get("ca_crt").data
        user = configs.get("user").data
        password = configs.get("password").data

        # Consumer
        url_consumer=configs.get("url_consumer").data
        auto_offset_reset=configs.get("auto_offset_reset").data
        group_id=configs.get("group_id").data
        topic_consumer_name=configs.get("topic_consumer_name").data
        instance=configs.get("instance").data
        format_data=configs.get("format_data").data

    except :
        print("Error in Config")

