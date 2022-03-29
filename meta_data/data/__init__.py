import pathlib
import importlib
import inspect
from typing import Tuple, Dict, Type

from ._base import Action, Status


def init() -> Tuple[Dict[int, Type[Action]], Dict[str, Type[Action]], Dict[int, Type[Status]], Dict[str, Type[Status]]]:
    _action = {}
    _action_by_name = {}
    _status = {}
    _status_by_name = {}

    _action_orig_names = {}

    for path in pathlib.Path(__file__).parent.glob('*.py'):
        if path.stem.startswith('_'): continue
        module = importlib.import_module(f'.{path.stem}', __package__)
        for name in dir(module):
            if name.startswith('_'): continue
            obj = getattr(module, name)
            if not inspect.isclass(obj): continue
            if issubclass(obj, Action):
                _action[obj.id] = obj
                for _name in obj.names:
                    _name = _name.lower()
                    if _name in _action_by_name:
                        raise Exception(f'Duplicate action name: {_name}')
                    _action_by_name[_name] = obj
                for _orig_name in obj._orig_names:
                    _orig_name = _orig_name.lower()
                    _action_orig_names.setdefault(_orig_name, []).append(obj)
            elif issubclass(obj, Status):
                _status[obj.id] = obj
                for _name in obj.names:
                    _name = _name.lower()
                    if _name in _status_by_name:
                        raise Exception(f'Duplicate status name: {_name}')
                    _status_by_name[_name] = obj

    for n, objs in _action_orig_names.items():
        if len(objs) == 1 and n not in _action_by_name:
            _action_by_name[n] = objs[0]

    return _action, _action_by_name, _status, _status_by_name


action, action_by_name, status, status_by_name = init()
