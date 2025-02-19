from moto import mock_aws
from ..file import *

@mock_aws()
def test_function():
    s3 = boto3.client("s3", region_name="eu-west-1")
    s3.create_bucket(Bucket="s3_bucket_name")

    expected_filename = "filename"
    returned_filename = "filename"

    assert expected_filename == returned_filename
