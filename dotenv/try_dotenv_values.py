from dotenv import dotenv_values as dv

test_config = dv('.env')

config = {
    **dv(".env"),
    **dv(".env.local")
}

print(test_config)
print('*' * 20)
print(config)
