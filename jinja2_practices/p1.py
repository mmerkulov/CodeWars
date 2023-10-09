import yaml
from jinja2 import Environment, FileSystemLoader, BaseLoader


def get_parameters_by_stage(stage: int = 1) -> dict:
    """    Относительно stage будем определять набор параметров, которые будут использоваться в application.yaml
    """
    parameters_dict = dict()
    if stage == 1:
        parameters_dict['topic'] = 'MMS1'
        parameters_dict['consumer_max_pool_records'] = 2
        parameters_dict['greenplum_table'] = 'public.python_kafka_mms_user_t'
    if stage == 2:
        parameters_dict['topic'] = 'MMS1'
        parameters_dict['consumer_max_pool_records'] = 10
        parameters_dict['greenplum_table'] = 'public.python_kafka_mms_user_t'
    if stage == 3:
        parameters_dict['topic'] = 'MMS1'
        parameters_dict['consumer_max_pool_records'] = 2
        parameters_dict['greenplum_table'] = 'public.python_kafka_mms_stage_3'
    return parameters_dict


with open('./mms.yaml', 'r') as r:
    values = yaml.safe_load(r)  # значяения которые мы получили откуда-то, тут из yaml файла
print(type(values))
print(values)  # Load templates file from templtes folder
env = Environment(loader=FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('t.j2')  # это шаблон наш с { }for service in values["kafka"]:
print(service)
file = open("./SVC-" + service['topic'] + ".yaml", "w")
file.write(template.render(service))
file.close()

parameters = get_parameters_by_stage(1)
myString = f'''kafka:         topic: {parameters['topic']}
         greenplum_table: {parameters['greenplum_table']}'''
rt = Environment(loader=BaseLoader()).from_string(myString)
data = rt.render(**get_parameters_by_stage(1))
print(data)
