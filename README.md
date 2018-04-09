# haasonline-ubuntu-vagrant
A Vagrantfile for HaasOnline running on Ubuntu 16.04

## Setup


### Vagrant

Vagrant is a tool that will allow you to easily setup and tear down servers in loval VM's or on cloud providers.

By changing a couple parameters you can easily get a copy of your HaasOnline server running in the cloud for your trading, or locally to test config changes.

This provides transparency and reproducability, because you can read the steps in the provisioning script and execute them yourself, altering as desired.

[Download Vagrant](https://www.vagrantup.com/downloads.html) and install it.


### DigitalOcean

This example hosts the server on DigitalOcean, so you'll need to [get a personal API token from them](https://www.digitalocean.com/community/tutorials/how-to-use-the-digitalocean-api-v2), or learn how to setup Vagrant for a different provider. - If you do feel free to open a PR to this repository.

If you don't have an account, [sign up with this link](https://m.do.co/c/dbdd5f2fb9b0) and you get $10 credit.

Then insert your token on line 14 of the Vagrantfile

```ruby
provider.token = 'DIGITAL_OCEAN_TOKEN'
```

To install the [DigitalOcean plugin](https://github.com/devopsgroup-io/vagrant-digitalocean), run the following command in a shell:

```bash
vagrant plugin install vagrant-digitalocean
```

Once you have the plugin, if you would like to adjust the size or location of the server you will spawn you can do that on lines 16 and 17 of the Vagrantfile.

To see available options use the following commands:

```bash
vagrant digitalocean-list regions DIGITAL_OCEAN_TOKEN
```

```bash
vagrant digitalocean-list sizes DIGITAL_OCEAN_TOKEN
```

### SSH Keys

You should now generate a new SSH KeyPair for your machine.
The following command will generate a a private ssh key: `./keys/haas-ubuntu` and a public ssh key: `./keys/haas-ubuntu.pub`

Vagrant will give your server the public key so it can authenticate you. You must keep your private key safe as it alone is used to authenticate you as the administrator of the server.

```bash
ssh-keygen -t rsa -C "your_email@example.com" -P "" -f ./keys/haas-ubuntu
```


### HaasOnline Linux Package

Place a copy of the linux32.tar.gz file in the `synced_folder` folder.

```
.
├── LICENSE
├── MainSettings.xml
├── README.md
├── Vagrantfile
├── keys
│   ├── README.md
│   ├── haas-ubuntu          <-- you generated these and will keep this secret.
│   └── haas-ubuntu.pub
└── synced_folder
    ├── fix_settings.py
    ├── linux32.tar.gz       <-- you added this.
    └── provision.sh
```

## Run

`vagrant up` Will create a server for you and install HaasOnline

`vagrant ssh` Will connect you, or you can use `ssh root@<IP> -i ./keys/haas-ubuntu`

`vagrant destroy` Deletes the droplet.