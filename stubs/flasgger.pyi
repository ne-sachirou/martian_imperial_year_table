from flask import Flask
import typing as t

def swag_from(
    specs: str = None,
    filetype: str = None,
    endpoint: t.Any = None,
    methods: t.Any = None,
    validation: bool = False,
    schema_id: t.Any = None,
    data: t.Any = None,
    definition: t.Any = None,
    validation_function: t.Any = None,
    validation_error_handler: t.Any = None,
): ...

class Swagger(object):
    def __init__(
        self,
        app: Flask = None,
        config: t.Any = None,
        sanitizer: t.Any = None,
        template: t.Any = None,
        template_file: t.Any = None,
        decorators: t.Any = None,
        validation_function: t.Any = None,
        validation_error_handler: t.Any = None,
        parse: t.Any = False,
        format_checker: t.Any = None,
    ): ...
