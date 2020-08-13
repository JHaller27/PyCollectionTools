EMPTY_INDENT = '    '
PIPED_INDENT = '|   '
SPLIT_INDENT = '├─'
ELBOW_INDENT = '└─'
ARRAY_INDEX =  '──┐'


def data_struct_as_tree(data, indent='') -> str:
    out_str = ''

    if isinstance(data, dict) and len(data) > 0:
        keys = list(data.keys())
        for kidx in range(len(keys)):
            key = keys[kidx]

            if kidx < (len(keys) - 1):
                next_indent_append = PIPED_INDENT
                item_indent = SPLIT_INDENT
            else:
                next_indent_append =  EMPTY_INDENT
                item_indent = ELBOW_INDENT

            out_str += f'\n{indent}{item_indent} {key}'
            out_str += data_struct_as_tree(data[key], indent + next_indent_append)

    elif isinstance(data, list) and len(data) > 0:
        for idx in range(len(data)):
            child = data[idx]

            if idx < (len(data) - 1):
                next_indent_append = PIPED_INDENT
                item_indent = SPLIT_INDENT
            else:
                next_indent_append =  EMPTY_INDENT
                item_indent = ELBOW_INDENT

            if isinstance(child, dict) or isinstance(child, list):
                out_str += f'\n{indent}{item_indent}{ARRAY_INDEX}'
                out_str += data_struct_as_tree(data[idx], indent + next_indent_append)
            else:
                out_str += f'\n{indent}{item_indent} {child}'

    else:
        out_str += f': {data}'

    return out_str