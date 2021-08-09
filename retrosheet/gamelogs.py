"""This module downloads game log files from the Retrosheet website. IF RUNNING THE
MODULE, PLEASE RUN FROM ROOT DIRECTORY OF THE PROJECT!
"""

import os
import sys
import argparse
import requests
import zipfile

from tqdm import tqdm


def download(
    start_year,
    end_year,
    url="https://www.retrosheet.org/gamelogs/",
    dl_path="./retrosheet_data/retrosheet_gls/",
):

    # Check if download directory exists, if not make it
    if not os.path.exists(dl_path):
        os.makedirs(dl_path)

    # Delete all of the files that are in the download directory
    for file in os.listdir(dl_path):
        os.remove(os.path.join(dl_path, file))

    # Use context manager with tqdm because it's nicer
    with tqdm(total=end_year - start_year + 1) as pbar:

        # Loop through the years
        for year in range(start_year, end_year + 1):
            pbar.set_description(f"Downloading {year} gamelog.")

            # Download the file
            req = requests.get(url + f"gl{year}.zip")
            with open(os.path.join(dl_path, f"gl{year}.zip"), "wb") as f:
                f.write(req.content)

            # Unzip the file
            pbar.set_description(f"Unzipping gl{year}.zip")
            with zipfile.ZipFile(
                os.path.join(dl_path, f"gl{year}.zip"), "r"
            ) as zip_ref:
                zip_ref.extractall(dl_path)

            # Delete the zipped file
            os.remove(os.path.join(dl_path, f"gl{year}.zip"))
            pbar.update()

    __make_labels([os.path.join(dl_path, file) for file in os.listdir(dl_path)])


def __make_labels(files):
    """Prepend the stat files with labels.

    Args:
        files (list): list of file names that need to be prepended
    """

    labels = [
        "Date",
        "Number of game",
        "Day",
        "Visiting Team",
        "Visiting Team League",
        "Visiting Team Game Number",
        "Home Team",
        "Home Team League",
        "Home Team Game Number",
        "Visiting Team Score",
        "Home Team Score",
        "Length of Game (outs)",
        "Time of Game (Day/Night)",
        "Completion Information",
        "Forfeit Information",
        "Protest Information",
        "Park ID",
        "Attendance",
        "Length of Game (minutes)",
        "Visiting Team Line Score",
        "Home Team Line Score",
        "Visiting Team At-bats",
        "Visiting Team Hits",
        "Visiting Team Doubles",
        "Visiting Team Triples",
        "Visiting Team Homeruns",
        "Visiting Team RBIs",
        "Visiting Team Sacrifice Hits",
        "Visiting Team Sacrifice Flies",
        "Visiting Team Hit-by-pitch",
        "Visiting Team Walks",
        "Visiting Team Intentional Walks",
        "Visiting Team Strikeouts",
        "Visiting Team Stolen Bases",
        "Visiting Team Caught Stealing",
        "Visiting Team Grounded into DP",
        "Visiting Team Awarded First Base due to CI",
        "Visiting Team Left on Base",
        "Visiting Team Pitchers Used",
        "Visiting Team Individual Earned Runs",
        "Visiting Team Earned Runs",
        "Visiting Team Wild Pitches",
        "Visiting Team Balks",
        "Visiting Team Putouts",
        "Visiting Team Assists",
        "Visiting Team Errors",
        "Visiting Team Passed Balls",
        "Visiting Team Double Plays",
        "Visiting Team Triple Plays",
        "Home Team At-bats",
        "Home Team Hits",
        "Home Team Doubles",
        "Home Team Triples",
        "Home Team Homeruns",
        "Home Team RBIs",
        "Home Team Sacrifice Hits",
        "Home Team Sacrifice Flies",
        "Home Team Hit-by-pitch",
        "Home Team Walks",
        "Home Team Intentional Walks",
        "Home Team Strikeouts",
        "Home Team Stolen Bases",
        "Home Team Caught Stealing",
        "Home Team Grounded into DP",
        "Home Team Awarded First Base due to CI",
        "Home Team Left on Base",
        "Home Team Pitchers Used",
        "Home Team Individual Earned Runs",
        "Home Team Earned Runs",
        "Home Team Wild Pitches",
        "Home Team Balks",
        "Home Team Putouts",
        "Home Team Assists",
        "Home Team Errors",
        "Home Team Passed Balls",
        "Home Team Double Plays",
        "Home Team Triple Plays",
        "Home Plate Umpire ID",
        "Home Plate Umpire Name",
        "1B Umpire ID",
        "1B Umpire Name",
        "2B Umpire ID",
        "2B Umpire Name",
        "3B Umpire ID",
        "3B Umpire Name",
        "LF Umpire ID",
        "LF Umpire Name",
        "RF Umpire ID",
        "RF Umpire Name",
        "Visiting Team Manager ID",
        "Visiting Team Manager Name",
        "Home Team Manager ID",
        "Home Team Manager Name",
        "Winning Pitcher ID",
        "Winning Pitcher Name",
        "Losing Pitcher ID",
        "Losing Pitcher Name",
        "Saving Pitcher ID",
        "Saving Pitcher Name",
        "Game Winning RBI Batter ID",
        "Game WInning RBI Batter Name",
        "Visiting Team Starting Pitcher ID",
        "Visiting Team Starting Pitcher Name",
        "Home Team Starting Pitcher ID",
        "Home Team Starting Pitcher Name",
        "Visiting Team Player 1 ID",
        "Visiting Team Player 1 Name",
        "Visiting Team Player 1 Defensive Position",
        "Visiting Team Player 2 ID",
        "Visiting Team Player 2 Name",
        "Visiting Team Player 2 Defensive Position",
        "Visiting Team Player 3 ID",
        "Visiting Team Player 3 Name",
        "Visiting Team Player 3 Defensive Position",
        "Visiting Team Player 4 ID",
        "Visiting Team Player 4 Name",
        "Visiting Team Player 4 Defensive Position",
        "Visiting Team Player 5 ID",
        "Visiting Team Player 5 Name",
        "Visiting Team Player 5 Defensive Position",
        "Visiting Team Player 6 ID",
        "Visiting Team Player 6 Name",
        "Visiting Team Player 6 Defensive Position",
        "Visiting Team Player 7 ID",
        "Visiting Team Player 7 Name",
        "Visiting Team Player 7 Defensive Position",
        "Visiting Team Player 8 ID",
        "Visiting Team Player 8 Name",
        "Visiting Team Player 8 Defensive Position",
        "Visiting Team Player 9 ID",
        "Visiting Team Player 9 Name",
        "Visiting Team Player 9 Defensive Position",
        "Home Team Player 1 ID",
        "Home Team Player 1 Name",
        "Home Team Player 1 Defensive Position",
        "Home Team Player 2 ID",
        "Home Team Player 2 Name",
        "Home Team Player 2 Defensive Position",
        "Home Team Player 3 ID",
        "Home Team Player 3 Name",
        "Home Team Player 3 Defensive Position",
        "Home Team Player 4 ID",
        "Home Team Player 4 Name",
        "Home Team Player 4 Defensive Position",
        "Home Team Player 5 ID",
        "Home Team Player 5 Name",
        "Home Team Player 5 Defensive Position",
        "Home Team Player 6 ID",
        "Home Team Player 6 Name",
        "Home Team Player 6 Defensive Position",
        "Home Team Player 7 ID",
        "Home Team Player 7 Name",
        "Home Team Player 7 Defensive Position",
        "Home Team Player 8 ID",
        "Home Team Player 8 Name",
        "Home Team Player 8 Defensive Position",
        "Home Team Player 9 ID",
        "Home Team Player 9 Name",
        "Home Team Player 9 Defensive Position",
        "Miscellaneous",
        "Acquisition Information",
    ]

    # Prepend the labels array to all of the files
    for file in files:
        __prepend_lines(",".join(labels), file)


def __prepend_lines(line, file):
    """Prepends the file with the inputted string.

    Args:
        line (string): line that will go at the very beginning of the file
        file (string): file name of the file that will be prepended to
    """

    # Create a dummy file
    dummy_file = file + ".bak"

    # Open original file as read only and dummy as write
    with open(file, "r") as readfile, open(dummy_file, "a") as writefile:

        # Write the line at the beginning of the dummy file
        writefile.write(line + "\n")

        # Copy the contents from the original file to the dummy
        for row in readfile:
            writefile.write(row)

    # Replace the original file with the dummy file
    os.remove(file)
    os.rename(dummy_file, file)


if __name__ == "__main__":

    # Must be in root directory
    if not (os.path.exists(".gitignore") or os.path.exists(".README.md")):
        print("PLEASE RUN MODULE/FUNCTION WHILE AT THE ROOT OF THE PROJECT!")
        sys.exit(2)

    # Set up arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "start_year", type=int, help="Start of the range of what years to download"
    )

    parser.add_argument(
        "end_year",
        type=int,
        help="End of the range of what years to download (inclusive)",
    )

    # Parse args
    args = parser.parse_args()

    # Download the statistics
    download(args.start_year, args.end_year)
