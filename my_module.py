import pandas as pd

def format_string(text : str):
    '''
    Reformats the given string so that it has no accents and unnecessary characters

    Args:
        text (str)
    Returns:
        str
    '''
    replace_dict = {
        ' de ':' ',
        ' & ':' ',
        '&':'',
        '%':'',
        '.':'',
        ',':''
    }
    translate_dict = {
        'á':'a',
        'é':'e',
        'í':'i',
        'ó':'o',
        'ú':'u',
        'ã':'a',
        'ê':'e',
        'ç':'c',
        ' ':'_',
        '-':'_'
    }

    new_text = text.lower()

    for item in replace_dict:
        new_text = new_text.replace(item, replace_dict[item])

    translation = new_text.maketrans(translate_dict)

    new_text = new_text.translate(translation)

    return new_text

def format_columns(df : pd.DataFrame):
    '''
    Reformats all of the columns in a dataframe, and returns a {new : old} dictionary that can be used for titling graphs and other uses.

    Args:
        df (pandas.DataFrame)
    returns:
        dict
    '''
    old_columns = df.columns
    new_columns = [format_string(col) for col in old_columns]

    column_dict = {new : old for new, old in zip (new_columns, old_columns)}

    df.columns = new_columns

    return column_dict