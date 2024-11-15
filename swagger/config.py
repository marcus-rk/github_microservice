from flasgger import Swagger

def init_swagger(app):
    swagger_config = {
        "headers": [],
        "specs": [{
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs"
    }
    
    template = {
        "swagger": "2.0",
        "info": {
            "title": "GitHub Repository Stats API",
            "description": "API for retrieving GitHub repository statistics",
            "version": "1.0.0"
        }
    }
    
    return Swagger(app, config=swagger_config, template=template)
