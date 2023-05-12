# Puppet manifest for configuring Apache LogLevel to debug

# Ensure Apache configuration file
file { '/etc/apache2/apache2.conf':
  ensure  => file,
  content => "LogLevel debug\n",
}

# Restart Apache service if the configuration file changes
service { 'apache2':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/apache2/apache2.conf'],
}
