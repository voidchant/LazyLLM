from importlib import import_module


# Document schemas import TaskType from parsing_service.base. Loading a schema
# must not import workers, which themselves depend on completed doc_service
# schemas (including when a relay child unpickles a DocServer service).
_EXPORTS = {
    '_Processor': ('.impl', '_Processor'),
    'DocumentProcessor': ('.server', 'DocumentProcessor'),
    'DocumentProcessorWorker': ('.worker', 'DocumentProcessorWorker'),
}


def __getattr__(name):
    if name not in _EXPORTS:
        raise AttributeError(name)
    module_name, attribute = _EXPORTS[name]
    value = getattr(import_module(module_name, __name__), attribute)
    globals()[name] = value
    return value

__all__ = [
    '_Processor',
    'DocumentProcessor',
    'DocumentProcessorWorker',
]
