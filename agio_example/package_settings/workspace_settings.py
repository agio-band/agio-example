from pydantic import BaseModel, Field

from agio.core.settings import APackageSettings, PluginSelectField, DictField
from agio.core.settings.fields import UrlField, StringField, ListField, IntField, RGBColorField, BoolField
from agio.core.settings.validators import RangeLimitValidator


class Template(BaseModel):
    name: str
    value: str = Field(..., widget='TemplatePath', max_length=10)


class ExampleSettings(APackageSettings, label='Example Settings'):
    # bool
    enabled: bool = BoolField(label='Enabled Example')
    # simple int value
    number_value: int
    float_number_value: float
    max_count: int = IntField(
        label='Items Max Count',
        description='Max count of some items',
        default=-1,
    )
    # simple string value
    object_name: str = StringField(label='Super Object Name')

    # special string field
    base_url: str = UrlField(
        label='Base URL',
        description='Base URL parameter description example',
        hint='Example URL hint',
    )
    # compound field
    rgb_channels = RGBColorField(
        label='RGB Channels',
        description='RGB Channels',
    )

    # list of values
    excluded_ids: list[int] = ListField(validators=[RangeLimitValidator(ge=0)])
    # next two fields have different definitions but will be identical
    list_names_1: list[StringField] = ListField(label='List Names One', default=list)
    list_names_2: list[str] = None

    # pydantic models (dict)
    template: Template
    templates: list[Template] = ListField(
        label='Template List',
        description='Publish Template List',
    )
    command_select: str = PluginSelectField('command', label='Select Command Plugin', default='none')
    # # data fields
    constants: dict
    value_map: dict[str, int]

    # TODO
    # env_vars: list[list] = TableField(label='Env Variables', column_labels=('Name', 'Value'))
