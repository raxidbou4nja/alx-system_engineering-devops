exec { 'killmenow':
  command => 'pkill -f killmenow',
  # Refreshonly ensures the command is only run when notified by another resource
  refreshonly => true,
}

# Notify the exec resource to run when the manifest is applied
Notify['Kill process'] -> Exec['killmenow']
