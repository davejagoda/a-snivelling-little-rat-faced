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
su - vagrant -c 'cd /vagrant && pipenv install'
su - vagrant -c 'ssh -o "StrictHostKeyChecking no" -T git@github.com'
HEREDOC

HOSTNAME = 'dulwich'
VAGRANTFILE_API_VERSION = '2'
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.ssh.forward_agent = true
  config.vm.box = 'ubuntu/bionic64'
  config.vm.hostname = HOSTNAME
  config.vm.provider 'virtualbox' do |vb|
    vb.name = HOSTNAME
  end
  config.vm.provision 'shell', inline: SCRIPT
end
