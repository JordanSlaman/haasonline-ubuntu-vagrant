# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.allowed_synced_folder_types = :rsync

  config.vm.define "haas-ubuntu" do |config|
      config.vm.provider :digital_ocean do |provider, override|
        override.vm.box = 'digital_ocean'
        override.ssh.private_key_path = '~/.ssh/haas-ubuntu'
        provider.token = 'DIGITAL_OCEAN_TOKEN'
        provider.image = 'ubuntu-16-04-x64'
        provider.region = 'sgp1'
        provider.size = '1gb'
      end

      config.vm.provision "shell", inline: "/bin/sh /vagrant/provision.sh"
  end
end
