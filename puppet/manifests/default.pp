node default {
  exec { 'apt-update':
    command => '/usr/bin/apt-get update',
  }

  Exec["apt-update"] -> Package <| |>

  package { 'python2.7-psycopg2':
    ensure => installed
  }

  class { 'python':
    version    => 'system',
    pip        => true,
    dev        => true,
    virtualenv => true,
  }

  # Install psycopg2 system-wide. required
  python::pip { 'psycopg2':
    pkgname => 'psycopg2'
  }

  python::virtualenv { "/var/www/${hostname}.${domain}/src/env":
    ensure       => present,
    version      => "system",
    owner        => "vagrant",
    requirements => "/var/www/${hostname}.${domain}/src/requirements.txt",
    cwd          => "/var/www/${hostname}.${domain}/src",
  }

  include users
  include nginx
  include uwsgi
  include utils
}
