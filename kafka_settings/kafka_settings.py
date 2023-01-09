from pydantic import BaseModel, BaseSettings
import os


# class CorruptedDataModel(BaseModel):
#     enabled: str = 'False'
#
#
# class WorkModeModel(BaseModel):
#     type: str = 'stream'
#     start_delay_millis: str = '0'


class ConsumerPropertiesKafkaModel(BaseModel):
    max_pool_interval_ms: str = '600000'
    max_poll_records: str = '2'


class KafkaModel(BaseModel):
    topic: str = 'MMS1'
    bootstrap_server: str = 'localhost:9092'
    # consumer_group: str = ''
    # poll_timeout: str = 'PT2M'
    # auto_reset_config: str = 'EARLIST'
    consumer_properties: ConsumerPropertiesKafkaModel()


class GreenplumConnectionConfigSettings(BaseModel):
    host: str = 'greenplum'
    port: str = '5432'
    database: str = 'db_dev'
    user: str = 'admin'
    password: str = 'admin'


class GreenplumModel(BaseModel):
    table: str = 'public.python_kafka_mms_user_t'
    connection_config: GreenplumConnectionConfigSettings


class ApplicationSettings(BaseSettings):
    kafka: KafkaModel
    # corrupted_data: CorruptedDataModel()
    greenplum: GreenplumModel


# os.environ['MY_X1'] = '1'
# print(os.environ['MY_X1'])

a = ApplicationSettings(topic='MMS1',
                        bootstrap_server='localhost:9092',
                        )
