VAGRANTFILE_API_VERSION = "2"

domain = "hcm.ly"

db_settings = {
  :hostname => "hcmdb",
  :box => "ubuntu/trusty64",
}

web_settings = {
  :hostname => "hcmapi",
  :box => "hashicorp/precise64",
  :ip => "192.168.1.17"
}

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define "web" do |web|
    web.vm.box = web_settings[:box]
    web.vm.host_name = "#{web_settings[:hostname]}.#{domain}"

    web.vm.network :forwarded_port, guest: 80, host: 8080
    web.vm.network :private_network, ip: web_settings[:ip]

    # Shared folders
    web.vm.synced_folder "src/", "/var/www/#{web_settings[:hostname]}.#{domain}/src"

    web.vm.provision :puppet do |puppet|
      puppet.manifests_path = "puppet/web/manifests"
      puppet.module_path = "puppet/web/modules"
      puppet.options = '--verbose --trace'
    end

  end

  config.vm.define "db" do |db|
    db.vm.box = db_settings[:box]
    db.vm.host_name = "#{db_settings[:hostname]}.#{domain}"
    db.vm.box = "#{db_settings[:box]}"
    db.vm.network :forwarded_port, guest: 5432, host: 15432

    db.vm.provision :puppet do |puppet|
      puppet.manifests_path = "puppet/db/manifests"
      puppet.module_path = "puppet/db/modules"
      puppet.options = '--verbose --trace'
    end

  end

end

