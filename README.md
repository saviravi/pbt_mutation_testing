### Build Base Docker Image
```docker build -t muttest_base -f Dockerfile.base .```

### Add New Repo Images
- edit `compose.yaml` to add new repo urls 
- ```docker-compose build```
- ```docker-compose run --rm repo1```

### Inside Container
<!-- - ```source venv/bin/activate``` -->
- set `PYTHONPATH` to wherever the source code is 
    - e.g. ```export PYTHONPATH=repo/src```
- install any necessary packages for that specific repo
- if you need to ignore some failing tests: add ```--runner 'pytest -k "not <name of test>"'``` to mutmut run
- ```mutmut run --paths-to-mutate <path to src> --tests-dir <path to tests>```

- export PYTHONPATH=repo/src/
- pip install numpy
- mutmut run --paths-to-mutate repo/src/matching --tests-dir repo/tests --runner 'pytest -k "not test_hospital_optimal and not test_supervisor_optimal"'


- outside of container: 
    - touch .mutmut-cache
    - chmod 606 .mutmut-cache
    - run as detached 
    - docker exec -i <container id> sh -c "sh mutmut_run.sh  > /proc/1/fd/1" to see it in docker logs <container id> --follow
        - maybe don't need the i
