import configparser
config = configparser.ConfigParser()
config.read('config/students.conf')
baseURL = config['DEFAULT']['BaseURL']


def create_request_url(endpoint):
    completURL = baseURL + endpoint
    print("Complete URL : ", completURL )
    return baseURL + endpoint

