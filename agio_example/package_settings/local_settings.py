from agio.core.settings import APackageSettings, StringField


class ExampleSettings(APackageSettings):
    example_required_value: int
    example_value_with_default: str = 'example'
    example_with_custom_label = StringField('', label='Custom Label')

