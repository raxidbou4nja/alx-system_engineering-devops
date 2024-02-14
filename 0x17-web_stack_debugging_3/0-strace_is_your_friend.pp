# Fix bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.

exec { 'fix-wordpress':
  command     => '/bin/true',
  path        => '/usr/local/bin/:/bin/',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'],
}
