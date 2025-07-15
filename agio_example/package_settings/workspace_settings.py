from pydantic import BaseModel
from agio.core.settings import APackageSettings
from agio.core.settings.fields import UrlField, StringField, ListField, IntField, RGBColorField
from agio.core.settings.validators import RangeLimitValidator


class SoftwareModel(BaseModel):
    name: str
    version: str



class ExampleSettings(APackageSettings):
    # simple int value
    max_count: int = IntField(
        label='Max Count',
        description='Max count of some items',
        default=-1,
    )
    # simple string value
    default_name: str = StringField(
        label='Default Name',
    )
    # special string field
    base_url: str = UrlField(
        label='Base URL',
        description='Base URL parameter description example',
    )
    # list of values
    excluded_ids: list[int] = ListField(validators=[RangeLimitValidator(le=5)])
    # list of pydantic models (dicts)
    software_list: list[SoftwareModel] = ListField(
        label='Software List',
        description='Software List',
        default=list,
    )
    # special list field
    rgb_channels = RGBColorField(
        label='RGB Channels',
        description='RGB Channels',
    )
    # next two fields have different definitions but will be identical
    list_names_1 = ListField(label='List Names 1', default=list, field=StringField)
    list_names_2: list[str] = None

