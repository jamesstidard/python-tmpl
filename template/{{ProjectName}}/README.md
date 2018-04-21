# {{ProjectName}}
{{Description}}

## Install
### Locally
```bash
$ pipenv install
$ pipenv shell
```

### Container
```bash
$ docker build -t {{PackageName}} .
$ CID=`docker run -d {{PackageName}}`
$ docker exec -it $CID /bin/bash
...
$ docker stop $CID; docker rm $CID
```

## Run
Assuming you are in a active virtual environment or container.
```bash
$ {{PackageName}}
```

## Test
Assuming you are in a active virtual environment or container.
```bash
$ pipenv install --dev
$ pytest
```
