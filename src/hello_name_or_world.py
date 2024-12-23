def hello(name=None):
    
    if name == '' or type(name) is not str:
        return 'Hello, World!'
    
    cap_name = name.title()
    
    return f'Hello, {cap_name}!'