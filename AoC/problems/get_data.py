import requests

def get_input(session_val, year, day):
    '''
    Gets the input data for a given problem. Saves the data to a file for future reference.
    
    Parameters
    ----------
    session_val : str
        The session value for the user
    year : int
        The year of the problem
    day : int
        The day of the problem

    Returns
    -------
    str
        The input data for the problem
    '''
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    try:
        response = requests.get(url, cookies={"session": session_val})
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    else:
        with open(f"problems/day{day}.txt", "w") as f:
            f.write(response.text)
        return response.text
