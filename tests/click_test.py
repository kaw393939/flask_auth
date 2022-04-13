import os

from click.testing import CliRunner

from app import create_log_folder

runner = CliRunner()


def test_add():
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, '../logs')
    # make a directory if it doesn't exist
    assert os.path.exists(logdir) == True