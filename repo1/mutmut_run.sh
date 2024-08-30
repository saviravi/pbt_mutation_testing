export PYTHONPATH=repo/src/
pip install numpy
mutmut run --paths-to-mutate repo/src/matching --tests-dir repo/tests --runner 'pytest -k "not test_hospital_optimal and not test_supervisor_optimal"'