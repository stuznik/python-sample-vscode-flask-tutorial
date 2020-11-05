def test_mock():
  assert True


def test_import_dsgdatascience():
  import ds
  print(ds.__version__)
  assert True

def test_will_fail():
  print("This will fail")
  raise Exception("oops")