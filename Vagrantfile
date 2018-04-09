# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.allowed_synced_folder_types = :rsync

  config.vm.define "haas-ubuntu" do |config|
      config.vm.provider :digital_ocean do |provider, override|
        override.vm.box = 'digital_ocean'
        override.ssh.private_key_path = './keys/haas-ubuntu'
        provider.ssh_key_name = 'haas-ubuntu-vagrant'

        config.vm.synced_folder ".", "/vagrant", disabled: true
        config.vm.synced_folder "synced_folder", "/synced_folder"

        provider.token = 'DIGITAL_OCEAN_TOKEN'
        provider.image = 'ubuntu-16-04-x64'
        provider.region = 'sgp1'
        provider.size = 's-1vcpu-1gb'
      end

      config.vm.provision "shell", inline: "/bin/sh /synced_folder/provision.sh"
  end
end
