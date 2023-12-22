# Installs Flask version 2.1.0 using the pip3 provider

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
