import sys

from rhamt.utils.config import DeprecatedConfigWrapper
from rhamt.utils.config import global_configuration
from rhamt.utils import path

global_configuration.configure(
    config_dir=path.conf_path.strpath,
    crypt_key_file=path.project_path.join('.yaml_key').strpath,
)

sys.modules[__name__] = DeprecatedConfigWrapper(global_configuration)