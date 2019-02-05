Installation of docker in ubuntu/ Wimdows :

For Ubuntu and windows go to terminal and powershell respectively:

sudo apt-get update

sudo apt-get install -y apt-transport-https ca-certificates

sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | sudo tee /etc/apt/sources.list.d/docker.list

sudo apt-get update

sudo apt-get install -y docker-engine

sudo service docker start

docker version


There might be a problem like this:


'cannot connect to the docker daemon' . Or 

'permission denied while trying to connect to the Docker daemon socket'

If one of these  is the case:

simply run :
sudo usermod -a -G docker $USER(your original user namee)




