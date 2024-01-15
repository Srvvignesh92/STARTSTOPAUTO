import pytest
from unittest.mock import patch
from your_script_file import rds_stop, start_db_instance, is_auto_start

# Replace 'your_script_file' with the actual name of the file containing your code.

def test_is_auto_start():
    tags = [
        {'Key': 'AutoStart', 'Value': 'True'},
        {'Key': 'OtherKey', 'Value': 'OtherValue'},
    ]
    assert is_auto_start(tags, 'AutoStart', 'True') is True
    assert is_auto_start(tags, 'AutoStart', 'False') is False

def test_start_db_instance():
    # You may need to adjust this test based on your actual implementation
    with patch('builtins.print') as mock_print:
        client_mock = patch('boto3.client').start()
        client_mock_instance = client_mock.return_value
        client_mock_instance.start_db_instance.return_value = None

        start_db_instance(client_mock_instance, 'test-db')

        client_mock_instance.start_db_instance.assert_called_once_with(DBInstanceIdentifier='test-db')
        mock_print.assert_called_once_with('Database test-db started successfully.')

def test_rds_stop():
    # You may need to adjust this test based on your actual implementation
    with patch('builtins.print') as mock_print:
        client_mock = patch('boto3.client').start()
        client_mock_instance = client_mock.return_value
        client_mock_instance.describe_db_instances.return_value = {
            'DBInstances': [
                {
                    'DBInstanceIdentifier': 'test-db',
                    'DBInstanceArn': 'arn:aws:rds:us-east-1:123456789012:db:test-db',
                },
            ],
        }
        client_mock_instance.list_tags_for_resource.return_value = {
            'TagList': [
                {'Key': 'AutoStart', 'Value': 'True'},
            ],
        }

        rds_stop()

        client_mock_instance.describe_db_instances.assert_called_once()
        client_mock_instance.list_tags_for_resource.assert_called_once_with(
            ResourceName='arn:aws:rds:us-east-1:123456789012:db:test-db'
        )
        client_mock_instance.start_db_instance.assert_called_once_with(DBInstanceIdentifier='test-db')
        mock_print.assert_called_with('The database test-db is set to auto-start.')
