package { 'Flask':
  ensure   => '2.1.0',   # Specify the desired version
  provider => 'pip3',    # Use pip3 as the package provider
}
