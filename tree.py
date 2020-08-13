EMPTY_INDENT = '    '
PIPED_INDENT = '|   '
SPLIT_INDENT = '├─'
ELBOW_INDENT = '└─'
ARRAY_INDEX =  '──┐'


def data_struct_as_tree(data, indent='') -> str:
    out_str = ''

    if isinstance(data, dict) and len(data) > 0:
        keys = list(data.keys())
        for kidx in range(len(keys) - 1):
            key = keys[kidx]

            out_str += f'\n{indent}{SPLIT_INDENT} {key}'
            out_str += data_struct_as_tree(data[key], indent + PIPED_INDENT)

        key = keys[-1]
        out_str += f'\n{indent}{ELBOW_INDENT} {key}'
        out_str += data_struct_as_tree(data[key], indent + EMPTY_INDENT)

    elif isinstance(data, list) and len(data) > 0:
        for idx in range(len(data) - 1):
            out_str += f'\n{indent}{SPLIT_INDENT}{ARRAY_INDEX}'
            out_str += data_struct_as_tree(data[idx], indent + PIPED_INDENT)

        out_str += f'\n{indent}{ELBOW_INDENT}{ARRAY_INDEX}'
        out_str += data_struct_as_tree(data[-1], indent + EMPTY_INDENT)

    else:
        out_str += f': {data}'

    return out_str