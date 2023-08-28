'''
RunPod | Tests | CLI | Commands
'''

import unittest
from unittest.mock import patch

from click.testing import CliRunner

from runpod.cli.commands import runpod_cli

class TestCommands(unittest.TestCase):
    ''' A collection of tests for the CLI commands. '''

    def setUp(self):
        self.runner = CliRunner()

    def test_runpod_cli(self):
        ''' Tests the runpod_cli command. '''
        with patch('click.echo') as mock_echo:
            result = self.runner.invoke(runpod_cli)
            assert result.exit_code == 0
            assert mock_echo.call_count == 1

    def test_store_api_key(self):
        ''' Tests the store_api_key command. '''
        with patch('click.echo') as mock_echo, \
            patch('runpod.cli.commands.set_credentials') as mock_set_credentials:

            result = self.runner.invoke(
                runpod_cli, ['store_api_key', '--profile', 'test', 'API_KEY_1234'])
            assert result.exit_code == 0
            mock_set_credentials.assert_called_with('API_KEY_1234', 'test')
            assert mock_echo.call_count == 2

if __name__ == "__main__":
    unittest.main()
