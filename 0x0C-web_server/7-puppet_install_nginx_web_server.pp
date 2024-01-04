package { 'nginx':
  ensure => 'present',
}

exec { 'apt-update':
  command => 'sudo apt-get update',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
  before  => Package['nginx'],
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  require   => Package['nginx'],
  subscribe => Exec['configure_nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

exec { 'configure_nginx':
  command  => 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \\/redirect_me {\\n\\t\\treturn 301 https:\\/\\/oluwaseundasilva.hashnode.dev\\/;\\n\\t}/" /etc/nginx/sites-available/default',
  path     => ['/usr/bin', '/usr/sbin', '/bin'],
  require  => File['/etc/nginx/sites-available/default'],
  notify   => Service['nginx'],
}

exec { 'restart_nginx':
  command  => 'sudo service nginx restart',
  path     => ['/usr/bin', '/usr/sbin', '/bin'],
  require  => Exec['configure_nginx'],
  subscribe => File['/etc/nginx/sites-available/default'],
}
