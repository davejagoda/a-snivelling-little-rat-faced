# -*- mode: ruby -*-
# vi: set ft=ruby :

SCRIPT = <<HEREDOC
# to make this error message go away:
# default: dpkg-preconfigure: unable to re-open stdin: No such file or directory
# set this environment variable:
export DEBIAN_FRONTEND=noninteractive

# apt and pip3 install
apt-get update
apt-get install -y python3-pip
pip3 install pipenv

# pipenv install and add github SSH key to avoid warning
su - vagrant -c 'ssh -o "StrictHostKeyChecking no" -T git@github.com || true'
su - vagrant -c 'git clone git@github.com:davejagoda/a-snivelling-little-rat-faced.git'
su - vagrant -c 'cd a-snivelling-little-rat-faced/ && pipenv install'
HEREDOC

HOSTNAME = 'dulwich'
VAGRANTFILE_API_VERSION = '2'
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = 'ubuntu/bionic64'
  config.vm.hostname = HOSTNAME
  config.vm.provider 'virtualbox' do |vb|
    vb.name = HOSTNAME
  end
  config.vm.provision 'file', source: 'id_rsa',
                      destination: '.ssh/id_rsa'
  config.vm.provision 'file', source: 'id_rsa.pub',
                      destination: '.ssh/id_rsa.pub'
  config.vm.provision 'shell', inline: SCRIPT
  config.vm.synced_folder '.', '/vagrant', disabled: true
end
