#!/usr/bin/env bash
#create a custom http response

# 2-puppet_custom_http_response_header.pp
class nginx_custom_headers {
  # Get the hostname of the server
  $hostname = $::hostname

  # Install the nginx package
  package { 'nginx':
    ensure => installed,
  }

  # Add the custom header to nginx.conf
  file_line { 'add_x_served_by_header':
    path    => '/etc/nginx/nginx.conf',
    line    => "add_header X-Served-By $hostname;",
    match   => "^http {",
    ensure  => present,
  }

  # Restart nginx to apply changes
  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
  }
}

# Apply the class to the node
node 'your_node_name' {
  include nginx_custom_headers
}
