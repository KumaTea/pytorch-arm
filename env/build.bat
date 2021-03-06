Rem PULL
Rem NO NEED TO PULL BEFORE!!!

Rem BUILD

cd py39
docker build --pull -t kumatea/build:py39-arm .
cd ..

cd py38
docker build --pull -t kumatea/build:py38-arm .
cd ..

cd py37
docker build --pull -t kumatea/build:py37-arm .
cd ..

cd py36
docker build --pull -t kumatea/build:py36-arm .
cd ..

Rem cd pypy37
Rem docker build --pull -t kumatea/build:pypy37-arm .
Rem cd ..

Rem cd pypy36
Rem docker build --pull -t kumatea/build:pypy36-arm .
Rem cd ..


Rem PUSH

docker push kumatea/build:py39-arm
docker push kumatea/build:py38-arm
docker push kumatea/build:py37-arm
docker push kumatea/build:py36-arm
Rem docker push kumatea/build:pypy37
Rem docker push kumatea/build:pypy36
