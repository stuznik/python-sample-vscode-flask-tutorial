import pytest
import ds
import pandas as pd
from datetime import datetime

from ds import bigquery as bq 
import gcsfs
import google.cloud.bigquery as bigquery
from google.cloud import bigquery_storage_v1
from typing import Dict, List, Mapping, Tuple, Union

BQ_CLIENT = bigquery.Client(project="d-ml-8576245384")
GCS = gcsfs.GCSFileSystem(project="d-ml-8576245384")
fast_bq_client = bigquery_storage_v1.BigQueryReadClient()




def test_mock():
  assert True


def test_import_dsgdatascience():
  import ds
  print(ds.__version__)
  assert True

def test_will_fail():
  print("This will fail")
  raise Exception("oops")

def test_bq_table_to_df():
  data = {"date_id": [20200104.], "date_key": [20200104.]}
  expected = pd.DataFrame(data)
  
  result = bq.bq_table_to_df(table="d-ml-8576245384.datascience_utils.gcs_to_bq_test")
  result = result.iloc[[4]].reset_index(drop=True)

  if pd.testing.assert_frame_equal(left=expected, right=result, check_dtype=False):
      pass
  else:
    raise Execption("you fail")