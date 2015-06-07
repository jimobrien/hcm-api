VAGRANTFILE_API_VERSION = "2"

domain = "hcm.ly"

settings = {
  :hostname => "hcmapi",
  :box => "hashicorp/precise64",
  :ip => "192.168.50.17"
}

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = settings[:box]
  config.vm.host_name = "#{settings[:hostname]}.#{domain}"

  config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.network :private_network, ip: settings[:ip]

  # Shared folders
  config.vm.synced_folder "src/", "/var/www/#{settings[:hostname]}.#{domain}/src"

  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "puppet/manifests"
    puppet.module_path = "puppet/modules"
    puppet.options = '--verbose --trace'
  end

end

