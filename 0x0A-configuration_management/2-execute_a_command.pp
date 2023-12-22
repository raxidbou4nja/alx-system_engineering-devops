# Kills a process named "killmenow"

exec { 'killmenow':
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell',
  # Treats exit status 0 and 1 as successful
  returns  => [0, 1],
}
