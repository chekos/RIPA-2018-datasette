from typing import List

def subset_of_columns(pattern: str, list_of_columns: List) -> List:
    """Matches a pattern against a list of column names and returns list of matches

    Parameters
    ----------
    pattern : str
        Pattern to match against columns. i.e. `RAE_`, `G_`, `ADS_`
    list_of_columns : List
        Columns to test patterns against

    Returns
    -------
    List
        List of columns matching the pattern.
    """

    matches = [col for col in list_of_columns if col.startswith(pattern)]
    return matches